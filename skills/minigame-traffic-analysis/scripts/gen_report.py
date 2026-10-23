# -*- coding: utf-8 -*-
"""将聚合产出的 data.json 渲染为自包含单文件 HTML 报告。

同事拿到报告后双击即可在浏览器打开，无需联网、无需起服务（ECharts 与数据均已内联）。
"""
import json, os


def build_report(data, out_path, title=None, channel=None):
    here = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.normpath(os.path.join(here, "..", "assets"))
    with open(os.path.join(assets_dir, "template.html"), encoding="utf-8") as f:
        tpl = f.read()
    with open(os.path.join(assets_dir, "echarts.min.js"), encoding="utf-8") as f:
        echarts = f.read()

    meta = data.get("meta", {})
    title = title or meta.get("title") or "小游戏流量分发与选品分析"
    channel = channel or meta.get("channel") or "未指定渠道"
    date_range = meta.get("date_range_str") or meta.get("date_range") or "—"

    tpl = (tpl
           .replace("__TITLE__", title)
           .replace("__H1__", title)
           .replace("__DATE_RANGE__", date_range)
           .replace("__CHANNEL__", channel)
           .replace("__ECHARTS__", "<script>" + echarts + "</script>")
           .replace("__DATA__",
                    "<script>window.DATA=" + json.dumps(data, ensure_ascii=False).replace("</", "<\\/") + ";</script>"))
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    return out_path


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(description="渲染小游戏分析报告")
    ap.add_argument("--data", required=True, help="aggregate.py 产出的 data.json")
    ap.add_argument("--out", default="report.html", help="输出 HTML 路径")
    ap.add_argument("--title", default=None, help="报告标题")
    ap.add_argument("--channel", default=None, help="渠道名")
    a = ap.parse_args()
    data = json.load(open(a.data, encoding="utf-8"))
    p = build_report(data, a.out, a.title, a.channel)
    print("report:", p, os.path.getsize(p), "bytes")
