# 小游戏流量分发与选品分析 Skill · 安装与使用

> 一套**渠道无关、App 无关**的常态化游戏分析框架。给三张日表 CSV，自动产出流量分发评估、新用户分配评估、品类供需选品的自包含 HTML 报告。

## 一、安装（3 步）

1. 拿到 `minigame-traffic-analysis/` 文件夹（或 zip 解压）
2. 放到：
   - **用户级（推荐）**：`~/.workbuddy/skills/minigame-traffic-analysis/`
   - **项目级**：`{你的项目}/.workbuddy/skills/minigame-traffic-analysis/`
3. 搞定。对你的 WorkBuddy 说「跑一遍小游戏流量分析」即可触发。

> 前置：机器有 `python3`（macOS/Linux 自带；Windows 在微软商店装 Python 3）。

## 二、一条命令出报告

```bash
cd minigame-traffic-analysis
python3 scripts/aggregate.py \
  --reg   注册指标.csv \
  --act   活跃指标.csv \
  --ad    广告日表.csv \
  --channel wetv \
  --countries 印度尼西亚,泰国,马来西亚,菲律宾 \
  --report report.html
```

- 不写 `--countries` 会按活跃量**自动取 Top4 国家**，其余归「其他」
- 不写 `--report` 则只生成 `data.json`，可后续用 `python3 scripts/gen_report.py --data data.json --out report.html` 单独渲染
- 报告 `report.html` 是**单文件**：ECharts 和数据已内联，双击即可在浏览器打开，无需联网/起服务

## 三、你要给的三张表

| 表 | 关键列（列名含这些字即可，无需改名） |
|---|---|
| 注册指标 | 日期、游戏名、国家/地区、用户类型、注册uv、次留率、7留率、（三级品类） |
| 活跃指标 | 日期、游戏名、国家/地区、用户类型、活跃uv、人均在线时长、人均活跃次数、次留率、7留率、（三级品类） |
| 广告收入 | 日期、游戏名、国家/地区、广告曝光pv、ecpm、分成前收入（三级品类） |

英文列名（date / appid / country / dau / ret_d1 / ecpm / revenue 等）也已内置支持。

## 四、报告里有什么

- **S0 大盘总览**：DAU、收入、ARPDAU、新用户次留 + 日趋势 + 国家盘子
- **S1 存量流量分发**：游戏×国家四象限（留存×变现），气泡=规模，附 RQ 与动作表
- **S2 新用户分配**：游戏×国家四象限（新用户次留×变现），附分配动作表
- **S3 品类供需选品**：供给×需求质量象限，附选品结论表
- **S4 方法论**：为什么这样对比才科学（防规模偏差）
- **S5 Skill 设计**：本框架如何复用到其他 App

## 五、常见问题

- **品类显示「ⓘ 名称推断」**：数据源三级品类缺失，按游戏名规则推断，落地前建议补齐官方品类
- **图表空白**：用浏览器直接打开 `report.html`；若用 file:// 仍异常，起个本地服务 `python3 -m http.server` 再访问
- **想换国家/窗口**：改 `--countries`、`--days` 重跑即可
- **列名识别失败**：脚本会提示缺哪列，按提示补列名或调整表头关键字

详见 `SKILL.md`。
