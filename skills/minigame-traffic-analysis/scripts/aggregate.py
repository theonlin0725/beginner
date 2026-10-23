# -*- coding: utf-8 -*-
"""
小游戏流量分发与选品分析 —— 通用数据聚合脚本（参数化、零硬编码）

输入：注册指标 / 活跃指标 / 广告收入 三张日表 CSV（建议 30 天）
输出：data.json（供 gen_report.py 渲染为自包含 HTML 报告）

科学对比设计（详见 SKILL.md）：
- 效率指标一律用比率型，与规模解耦（留存率、ARPDAU、RQ）
- 留存只统计可观测窗口（次留<=MAX-1，7留<=MAX-7），避免近期"假0%"污染
- 对比基准一律在国家内部（游戏 vs 该国大盘加权均值）
- 列名自动探测、日期与国家 TopN 自动识别，支持任意 App / 渠道 / 国家

用法：
  python3 aggregate.py --reg 注册.csv --act 活跃.csv --ad 广告.csv \
      --channel wetv --countries 印度尼西亚,泰国,马来西亚,菲律宾 \
      --report report.html
"""
import csv, json, re, os, sys, argparse
from collections import defaultdict
from datetime import datetime, timedelta

# ---------- 列名自动探测（contains 匹配，别名从具体到模糊）----------
FIELD_ALIASES = {
    'date':     ['日期', 'stat_date', 'statdate', '数据日期', 'date'],
    'game':     ['游戏名', 'appid', 'app_id', 'app', '游戏'],
    'country':  ['国家/地区', '国家', 'country', 'region', '地区'],
    'usertype': ['用户类型', '用户', 'usertype', 'type'],
    'cat':      ['三级品类', '品类', 'category', 'cat'],
    'reg_uv':   ['注册uv', '新增uv', 'reg_uv', 'new_uv'],
    'act_uv':   ['活跃uv', '活跃dau', 'act_uv', 'dau'],
    'ret_d1':   ['次留率', '次留', 'd1', 'ret_d1'],
    'ret_d7':   ['7留率', '七留率', '7留', 'd7', 'ret_d7'],
    'dur':      ['人均在线时长', '在线时长', 'dur', '时长'],
    'times':    ['人均活跃次数', '活跃次数', 'times'],
    'ad_pv':    ['广告曝光pv', '曝光pv', 'ad_pv', 'impressions'],
    'ad_clk':   ['广告点击pv', '点击pv', 'ad_clk', 'clicks'],
    'ecpm':     ['ecpm/美元', 'ecpm', 'ecpm美元'],
    'rev':      ['广告分成前收入/美元', '分成前收入', '收入/美元', 'rev', 'revenue'],
}


def _norm_col(s):
    return re.sub(r'[\s/]', '', (s or '').lower())


def detect_columns(header):
    """列名探测：
    第一轮：按别名优先级（列表中靠前者优先）做精确（去噪）匹配，
           保证 '游戏名' 优先于 'appid'、'注册uv' 优先于 '注册uv日环比'。
    第二轮：按包含匹配，取列名最短者兜底。
    """
    hdr = [(c, _norm_col(c)) for c in (header or [])]
    taken = set()
    mapping = {}
    # 第一轮：按 names 优先级精确匹配
    for field, names in FIELD_ALIASES.items():
        chosen = None
        for n in names:
            nn = _norm_col(n)
            for col, cl in hdr:
                if col in taken:
                    continue
                if cl == nn:
                    chosen = col
                    break
            if chosen:
                break
        if chosen:
            mapping[field] = chosen
            taken.add(chosen)
    # 第二轮：包含匹配，取列名最短者
    for field, names in FIELD_ALIASES.items():
        if field in mapping:
            continue
        best = None
        for col, cl in hdr:
            if col in taken:
                continue
            for n in names:
                if n.lower() in cl:
                    if best is None or len(col) < len(best[0]):
                        best = (col, n)
                    break
        if best:
            mapping[field] = best[0]
            taken.add(best[0])
    return mapping


def num(s):
    s = (s or '').strip().replace(',', '').replace('%', '')
    if s in ('', '-', '-9999', 'nan', 'None'):
        return 0.0
    try:
        return float(s)
    except Exception:
        return 0.0


def pct(s):
    return num(s) / 100.0 if '%' in (s or '') else num(s)


def to_dt(d):
    return datetime.strptime(str(int(float(d))), '%Y%m%d')


def to_int(dt):
    return int(dt.strftime('%Y%m%d'))


def fmt_cn(dt):
    return dt.strftime('%Y.%m.%d')


# ---------- 品类映射（数据自带值 -> 分析品类）----------
DATA_CAT_MAP = {'消除': '消除', '益智': '益智解谜', '塔防': '塔防射击'}


def infer_category(name):
    n = (name or '').lower()
    rules = [
        (r'mahjong|tile match|tile party|come match|combo pop|crush|pop$|match', '消除'),
        (r'sort|screw|water puzzle|color water', '分类整理(Sort)'),
        (r'arrow|sudoku|rope|puzzle king|tricky|screen detective|detective', '益智解谜'),
        (r'snipe|shoot|wars|troop|defense|dorm|capybara', '塔防射击'),
        (r'store|factory|farm|dreamy', '模拟经营'),
        (r'rescue|save ', '救援闯关'),
    ]
    for pat, cat in rules:
        if re.search(pat, n):
            return cat
    return '其他'


def main():
    ap = argparse.ArgumentParser(description='小游戏流量分发与选品分析 · 数据聚合')
    ap.add_argument('--reg', required=True, help='注册指标 CSV')
    ap.add_argument('--act', required=True, help='活跃指标 CSV')
    ap.add_argument('--ad', required=True, help='广告收入 CSV')
    ap.add_argument('--out', default='data.json', help='输出 data.json 路径')
    ap.add_argument('--report', default=None, help='可选：同时渲染 HTML 报告的路径')
    ap.add_argument('--channel', default='未指定渠道', help='渠道名（仅用于报告展示）')
    ap.add_argument('--title', default=None, help='报告标题（默认按渠道生成）')
    ap.add_argument('--days', type=int, default=30, help='分析窗口天数（默认30）')
    ap.add_argument('--countries', default=None, help='指定分析国家，逗号分隔；默认自动取 Top 活跃国家')
    ap.add_argument('--top-n', type=int, default=4, help='未指定 --countries 时展示的 TopN 国家数')
    args = ap.parse_args()

    # ---- 读取并探测列名 ----
    def load(path):
        with open(path, encoding='utf-8-sig') as f:
            r = csv.DictReader(f)
            mp = detect_columns(r.fieldnames or [])
            rows = list(r)
        return mp, rows

    m_reg, reg_rows = load(args.reg)
    m_act, act_rows = load(args.act)
    m_ad, ad_rows = load(args.ad)

    must = {
        'reg.日期': m_reg.get('date'), 'reg.游戏': m_reg.get('game'),
        'act.日期': m_act.get('date'), 'act.游戏': m_act.get('game'), 'act.活跃uv': m_act.get('act_uv'),
        'ad.游戏': m_ad.get('game'), 'ad.收入': m_ad.get('rev'),
    }
    missing = [k for k, v in must.items() if not v]
    if missing:
        sys.exit('缺少必要列，请检查 CSV 表头：' + ', '.join(missing))

    def g(row, mp, field):
        c = mp.get(field)
        return row.get(c) if c else None

    # ---- 探测 MAX_DATE 与可观测窗口 ----
    all_dates = set()
    for rows, mp in ((reg_rows, m_reg), (act_rows, m_act), (ad_rows, m_ad)):
        for row in rows:
            d = g(row, mp, 'date')
            if d:
                try:
                    all_dates.add(int(float(d)))
                except Exception:
                    pass
    if not all_dates:
        sys.exit('未能从三张表解析出任何日期')
    MAX_DT = max(to_dt(d) for d in all_dates)
    D1_CUT = to_int(MAX_DT - timedelta(days=1))
    D7_CUT = to_int(MAX_DT - timedelta(days=7))

    # ---- 自动确定分析国家 ----
    if args.countries:
        COUNTRIES = [c.strip() for c in args.countries.split(',') if c.strip()]
    else:
        cuv = defaultdict(float)
        for row in act_rows:
            game = g(row, m_act, 'game')
            c = g(row, m_act, 'country')
            if game in ('ALL', '') or c in ('ALL', '', None):
                continue
            cuv[c] += num(g(row, m_act, 'act_uv'))
        COUNTRIES = sorted(cuv, key=lambda x: -cuv[x])[:args.top_n]
    ALL_COUNTRIES = COUNTRIES + ['ALL']

    def norm_country(c):
        if c in ('ALL', '全部', 'all'):
            return 'ALL'
        return c if c in COUNTRIES else '其他'

    CAT_FROM_DATA = {}

    def get_category(game):
        return CAT_FROM_DATA.get(game) or infer_category(game)

    # ---- 读注册表（不跳过 game=ALL 的大盘行；仅大盘行不更新品类映射）----
    reg_uv = defaultdict(float)
    reg_d1 = defaultdict(lambda: [0.0, 0.0])
    reg_d7 = defaultdict(lambda: [0.0, 0.0])
    reg_daily = defaultdict(lambda: defaultdict(float))
    for row in reg_rows:
        d = g(row, m_reg, 'date')
        game = g(row, m_reg, 'game')
        c = norm_country(g(row, m_reg, 'country'))
        if d is None:
            continue
        d = int(float(d))
        cat = g(row, m_reg, 'cat')
        if game not in ('ALL', '') and cat not in ('未知', 'ALL', '', None):
            CAT_FROM_DATA[game] = DATA_CAT_MAP.get(cat, cat)
        uv = num(g(row, m_reg, 'reg_uv'))
        key = (game, c)
        reg_uv[key] += uv
        if d <= D1_CUT:
            reg_d1[key][0] += pct(g(row, m_reg, 'ret_d1')) * uv
            reg_d1[key][1] += uv
        if d <= D7_CUT:
            reg_d7[key][0] += pct(g(row, m_reg, 'ret_d7')) * uv
            reg_d7[key][1] += uv
        if c == 'ALL':
            reg_daily[game][d] += uv

    # ---- 读活跃表 ----
    act_uv = defaultdict(float)
    act_dur = defaultdict(lambda: [0.0, 0.0])
    act_cnt = defaultdict(lambda: [0.0, 0.0])
    act_d1 = defaultdict(lambda: [0.0, 0.0])
    act_d7 = defaultdict(lambda: [0.0, 0.0])
    act_daily = defaultdict(lambda: defaultdict(float))
    for row in act_rows:
        d = g(row, m_act, 'date')
        game = g(row, m_act, 'game')
        c = norm_country(g(row, m_act, 'country'))
        ut = g(row, m_act, 'usertype') or 'ALL'
        if d is None:
            continue
        d = int(float(d))
        cat = g(row, m_act, 'cat')
        if game not in ('ALL', '') and cat not in ('未知', 'ALL', '', None):
            CAT_FROM_DATA[game] = DATA_CAT_MAP.get(cat, cat)
        uv = num(g(row, m_act, 'act_uv'))
        key = (game, c, ut)
        act_uv[key] += uv
        act_dur[key][0] += num(g(row, m_act, 'dur')) * uv
        act_dur[key][1] += uv
        act_cnt[key][0] += num(g(row, m_act, 'times')) * uv
        act_cnt[key][1] += uv
        if d <= D1_CUT:
            act_d1[key][0] += pct(g(row, m_act, 'ret_d1')) * uv
            act_d1[key][1] += uv
        if d <= D7_CUT:
            act_d7[key][0] += pct(g(row, m_act, 'ret_d7')) * uv
            act_d7[key][1] += uv
        if c == 'ALL':
            act_daily[(game, ut)][d] += uv

    # ---- 读广告表（不跳过 game=ALL 大盘行）----
    ad_rev = defaultdict(float)
    ad_pv = defaultdict(float)
    ad_ecpm = defaultdict(lambda: [0.0, 0.0])
    for row in ad_rows:
        game = g(row, m_ad, 'game')
        c = norm_country(g(row, m_ad, 'country'))
        cat = g(row, m_ad, 'cat')
        if game not in ('ALL', '') and cat not in ('未知', 'ALL', '', None):
            CAT_FROM_DATA[game] = DATA_CAT_MAP.get(cat, cat)
        rev = num(g(row, m_ad, 'rev'))
        pv = num(g(row, m_ad, 'ad_pv'))
        key = (game, c)
        ad_rev[key] += rev
        ad_pv[key] += pv
        ad_ecpm[key][0] += num(g(row, m_ad, 'ecpm')) * pv
        ad_ecpm[key][1] += pv

    # ---- 聚合输出 ----
    games = sorted({k[0] for k in act_uv if k[0] != 'ALL'})

    def w(d, key):
        a, b = d[key]
        return round(a / b, 4) if b > 0 else None

    def build_matrix(usertype):
        rows = []
        for game in games:
            for c in ALL_COUNTRIES:
                uv = act_uv.get((game, c, usertype), 0.0)
                if uv <= 0:
                    continue
                rev = ad_rev.get((game, c), 0.0) if usertype == 'ALL' else None
                item = {
                    'game': game, 'country': c, 'cat': get_category(game),
                    'act_uv': round(uv), 'avg_dau': round(uv / args.days, 1),
                    'dur': w(act_dur, (game, c, usertype)),
                    'times': w(act_cnt, (game, c, usertype)),
                    'd1': w(act_d1, (game, c, usertype)),
                    'd7': w(act_d7, (game, c, usertype)),
                }
                if usertype == 'ALL':
                    item['rev'] = round(rev, 2)
                    item['arpdau'] = round(rev / uv * 1000, 3) if uv > 0 else None
                    item['ecpm'] = w(ad_ecpm, (game, c))
                    item['ad_pv_per_dau'] = round(ad_pv.get((game, c), 0) / uv, 2) if uv > 0 else None
                if usertype == '新用户':
                    item['reg_uv'] = round(reg_uv.get((game, c), 0.0))
                    item['reg_d1'] = w(reg_d1, (game, c))
                    item['reg_d7'] = w(reg_d7, (game, c))
                rows.append(item)
        return rows

    matrix_all = build_matrix('ALL')
    matrix_new = build_matrix('新用户')

    bench = {}
    for c in ALL_COUNTRIES:
        uv = act_uv.get(('ALL', c, 'ALL'), 0.0)
        rev = ad_rev.get(('ALL', c), 0.0)
        bench[c] = {
            'act_uv': round(uv), 'rev': round(rev, 2),
            'arpdau': round(rev / uv * 1000, 3) if uv > 0 else None,
            'd1': w(act_d1, ('ALL', c, 'ALL')), 'd7': w(act_d7, ('ALL', c, 'ALL')),
            'dur': w(act_dur, ('ALL', c, 'ALL')),
            'new_d1': w(reg_d1, ('ALL', c)), 'new_d7': w(reg_d7, ('ALL', c)),
            'reg_uv': round(reg_uv.get(('ALL', c), 0.0)),
            'ecpm': w(ad_ecpm, ('ALL', c)),
        }

    for row in matrix_all:
        c = row['country']
        tot_uv = sum(r['act_uv'] for r in matrix_all if r['country'] == c)
        tot_rev = sum(r['rev'] for r in matrix_all if r['country'] == c)
        if tot_uv > 0 and tot_rev > 0 and row['act_uv'] > 0:
            su = row['act_uv'] / tot_uv
            sr = row['rev'] / tot_rev
            row['share_uv'] = round(su, 4)
            row['share_rev'] = round(sr, 4)
            row['rq'] = round(sr / su, 3) if su > 0 else None
    for row in matrix_new:
        c = row['country']
        tot = sum(r.get('reg_uv', 0) for r in matrix_new if r['country'] == c)
        if tot > 0:
            row['share_reg'] = round(row.get('reg_uv', 0) / tot, 4)

    cat_rows = []
    for c in ALL_COUNTRIES:
        agg = defaultdict(lambda: {'uv': 0.0, 'rev': 0.0, 'reg': 0.0,
                                   'd7n': 0.0, 'd7d': 0.0, 'd1n': 0.0, 'd1d': 0.0,
                                   'durn': 0.0, 'durd': 0.0, 'games': set()})
        for r in matrix_all:
            if r['country'] != c:
                continue
            a = agg[r['cat']]
            a['uv'] += r['act_uv']
            a['rev'] += r['rev']
            a['games'].add(r['game'])
            if r['d7'] is not None:
                a['d7n'] += r['d7'] * r['act_uv']
                a['d7d'] += r['act_uv']
            if r['d1'] is not None:
                a['d1n'] += r['d1'] * r['act_uv']
                a['d1d'] += r['act_uv']
            if r['dur'] is not None:
                a['durn'] += r['dur'] * r['act_uv']
                a['durd'] += r['act_uv']
        for r in matrix_new:
            if r['country'] != c:
                continue
            agg[r['cat']]['reg'] += r.get('reg_uv', 0)
        tot_uv = sum(a['uv'] for a in agg.values())
        tot_rev = sum(a['rev'] for a in agg.values())
        tot_reg = sum(a['reg'] for a in agg.values())
        for cat, a in agg.items():
            if a['uv'] <= 0:
                continue
            cat_rows.append({
                'country': c, 'cat': cat, 'n_games': len(a['games']),
                'act_uv': round(a['uv']), 'rev': round(a['rev'], 2), 'reg_uv': round(a['reg']),
                'share_uv': round(a['uv'] / tot_uv, 4) if tot_uv else None,
                'share_rev': round(a['rev'] / tot_rev, 4) if tot_rev else None,
                'share_reg': round(a['reg'] / tot_reg, 4) if tot_reg else None,
                'arpdau': round(a['rev'] / a['uv'] * 1000, 3) if a['uv'] else None,
                'd1': round(a['d1n'] / a['d1d'], 4) if a['d1d'] else None,
                'd7': round(a['d7n'] / a['d7d'], 4) if a['d7d'] else None,
                'dur': round(a['durn'] / a['durd'], 2) if a['durd'] else None,
                'rq': round((a['rev'] / tot_rev) / (a['uv'] / tot_uv), 3) if tot_uv and tot_rev and a['uv'] else None,
            })

    trend = []
    for d in sorted(act_daily.get(('ALL', 'ALL'), {})):
        trend.append({
            'date': str(d),
            'dau': round(act_daily[('ALL', 'ALL')].get(d, 0)),
            'new': round(act_daily[('ALL', '新用户')].get(d, 0)),
            'reg': round(reg_daily.get('ALL', {}).get(d, 0)),
        })

    cat_map_out = [{'game': gm, 'cat': get_category(gm),
                    'src': '数据' if gm in CAT_FROM_DATA else '名称推断'} for gm in games]

    start_dt = MAX_DT - timedelta(days=args.days - 1)
    date_range_str = f"{fmt_cn(start_dt)} – {fmt_cn(MAX_DT)}（{args.days}天）"
    title = args.title or f"{args.channel} 小游戏流量分发与选品分析"

    out = {
        'meta': {
            'date_range': f"{to_int(start_dt)}-{to_int(MAX_DT)}",
            'date_range_str': date_range_str,
            'days': args.days,
            'd1_cut': str(D1_CUT), 'd7_cut': str(D7_CUT),
            'channel': args.channel, 'title': title,
            'cat_inferred': sum(1 for gm in games if gm not in CAT_FROM_DATA),
            'cat_total': len(games),
        },
        'bench': bench, 'matrix_all': matrix_all, 'matrix_new': matrix_new,
        'cats': cat_rows, 'trend': trend, 'cat_map': cat_map_out,
    }
    with open(args.out, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False)

    print('games:', len(games), '| countries:', COUNTRIES,
          '| MAX_DATE:', to_int(MAX_DT), '| D1_CUT:', D1_CUT, 'D7_CUT:', D7_CUT)
    print('inferred categories:', out['meta']['cat_inferred'], '/', len(games))
    print('data.json ->', args.out)

    if args.report:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import gen_report
        p = gen_report.build_report(out, args.report, args.title, args.channel)
        print('report ->', p, os.path.getsize(p), 'bytes')


if __name__ == '__main__':
    main()
