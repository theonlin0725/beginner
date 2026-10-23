---
name: game-cover-sop
description: Generate production-grade prompts for mobile game commercial visuals (horizontal cover, vertical poster, banner) using the HuaClaw v5.0 SOP. This skill should be used when the user requests a game cover image, poster, banner, key visual, store screenshot, ad creative, or any prompt for game commercial illustration. It enforces a 4-asset intake gate (game name / category / icon / gameplay screenshot), runs subject-type routing (character / gameplay_object / hybrid / scenario_puzzle), applies the 4-lever differentiation matrix (camera / lighting / setting / weight), produces a 9-segment prompt template, and runs the 8-item formal preflight before output. Use whenever the user mentions 游戏封面图 / 海报 / banner / key visual / 商业视觉 / store creative / ad creative for any mobile game.
---

# Game Cover SOP — v5.0 Master Workflow

This skill produces commercial-grade prompts for mobile game visuals (horizontal cover, vertical poster, banner). It is the executable form of the HuaClaw v5.0 game commercial visual SOP (`soul/workflows/game-cover-sop.md`).

## When to Trigger

Activate this skill whenever the user request involves any of:

- 生成 / 制作 / 写 prompt：游戏封面图、海报图、Banner、Key Visual、商店素材、广告创意、出海素材
- "帮我做一张《...》游戏的封面" / "给这个游戏出一份海报 prompt" / "banner 怎么写"
- 把游戏 ICON + 游戏截图喂进来要求出图、出 prompt、出 brief、出方案
- 关键词触发：subject_type / archetype / 4 杠杆 / 9 段 prompt / 海报 SOP / 出图工作站

Do NOT activate for: pure character concept art / 非游戏品类设计 / 无需商业目的的 illustration / UI 设计 / icon 设计本身。

## Core Mental Model (Always Hold This in Mind)

```
1. 必备素材    — 4 项准入：游戏名 / 类型 / ICON / 截图（任一缺失 → 停下来索取）
2. 全局策略    — 4 杠杆差异化（camera / lighting / setting / visual weight）
3. 构图的方法  — 构图层 C1-C4 + Format Adapter ｜ 表现因素层 + 叙事变量
4. 生产流程    — ① 10 步流程 → ② 主角分型 → ③ 9 段模板 → ④ 8 项硬检查
5. 输出速查表  — 横/竖/Banner 各自版式骨架
```

横向 / 竖版 / Banner 共用同一套 ① 流程 + ② 主角分型 + ③ 9 段模板 + ④ 8 项硬检查。只在差异点参数化。

## Mandatory Workflow (Execute In Order)

### Step 0: 素材准入门（强约束 — 任一必选缺失就停下）

When the user requests a game visual, FIRST present this checklist before anything else:

```text
在生成之前，请先确认提供以下素材：

  ✅ 必选 1：游戏名字（文本）
  ✅ 必选 2：游戏品类（match-3 / RPG / shooter / puzzle 等）
  ✅ 必选 3：游戏 ICON（正方形图）
  ✅ 必选 4：游戏画面截图（长方形图 ≥1 张）
  ⬜ 可选  ：广告语 tagline / 角色立绘 / 已有素材

【为什么需要】
- 游戏名字 → AI 不靠图像识别去猜，避免训练先验编造
- 品类 → 分型路由的输入
- ICON → 风格 DNA 锚点 + 角色资产剥离起点
- 截图 → 玩法 Fidelity 自检的真实基准（防止把箭头消除画成桌游这类高危误导）
```

If any required asset is missing, STOP and request it. Do not proceed to options.

### Step 1: subject_type 路由（决定整张图的 C 位是谁）

Before writing any prompt, run subject_type routing:

| subject_type | 触发条件 | C 位是 |
|---|---|---|
| **character** | 强角色品类（rpg / action / adventure / card battle）；游戏名含 hero / girl / 主角 | 角色立绘 / 角色组 |
| **gameplay_object** | 玩法物件主导品类（match-3 / cooking / idle / simulation / 箭头消除 / 拼图）；无角色资产 | 玩法核心物件 |
| **hybrid** | 救援/逃脱型（rescue / escape / save princess）；或玩法主导品类 + 已上传角色 | 角色 + 玩法机制同屏 |
| **scenario_puzzle** | 脑洞 / 找茬 / 找物 / 社交反转 | 荒诞情境 + 视觉线索 + 解谜动作 |

**关键纠错**：品类 = "puzzle" 不能默认走 scenario_puzzle。「箭头消除 / 路径解谜 / 连连看 / 物理消除」属于 **gameplay_object**，主体是玩法物件本身。游戏名含 "escape" 不一定是 hybrid 救援，可能是 escape room 解谜。**遇到长尾品类务必让用户口述「玩法核心做什么动作 / 主体物件长什么样」再分型，不要按品类字段直接判**。

### Step 2: 用 4 杠杆 + 主角分型 + 叙事变量产出 3 套差异化方案

每张方案需要在以下 4 个杠杆上至少错开 3 个：

- **L1 Camera**：视角 / 镜头距离 / 透视
- **L2 Lighting**：色温 / 光向 / 反差
- **L3 Setting**：环境 / 时间 / 背景层级
- **L4 Visual Weight**：主体面积 / 留白分布 / 焦点位置

叙事变量（5 维度，跨格式通用）：moment / character_goal / viewer_relation / conflict_level / reward_signal。详见 `references/workflow-v5.md` 第 4 节。

### Step 3: 渲染 9 段 prompt 模板

每条 prompt 必须显式包含以下 9 段（subject_type 不同则模板分流）：

```
段落 1   容器声明（A 16:9 commercial cover for ...）
段落 1.5 Composition Lock（横/竖/Banner 各自的版式锁）
段落 1.6 Safe-Crop Lock（按档位写安全区尺寸）
段落 2   Title Lock — Flexible Single Title 2.1（exact 标题，禁止重复标题层）
段落 3   主体/玩法 Lock（Subject Lock / Game Asset Lock / Scenario Puzzle Lock，按 subject_type 分流）
段落 4   连接与节奏（标题 ↔ 主体 用什么视觉装置串联）
段落 5   光影色彩
段落 6   负面词（按 subject_type 加专项负面）
```

模板的具体写法（subject_type 4 向分流）见 `references/workflow-v5.md` 第 4 节，以及 `references/narrative-driven-variants.md` 第 5 章。

### Step 4: 跑 8 项硬检查（纯 prompt 形式校验）

```
P1 标题是否单层清晰？     P2 Negative 是否裸写 no text？
P3 是否默认 A/B/C 3 套？  P4 subject_type 是否显式判定？
P5 是否显式写 L1/L2/L3/L4？P6 是否先列差异化矩阵？
P7 竖版是否先确认主体位置？P8 玩法 Fidelity 自检是否执行？
```

任一未通过 → 改 prompt 不要交付。

### Step 5: 默认输出 3 套差异化方案 + 1 张差异化矩阵表

```text
方案 A — [archetype 名] · subject_type=...
   L1 / L2 / L3 / L4 / story / pose
   完整 9 段 prompt

方案 B — [archetype 名] · subject_type=...
   ...

方案 C — [archetype 名] · subject_type=...
   ...

差异化矩阵：
| 杠杆 | A | B | C |
| L1   | ... | ... | ... |
| L2   | ... | ... | ... |
| L3   | ... | ... | ... |
| L4   | ... | ... | ... |
```

## How to Use the Bundled Resources

### `references/workflow-v5.md`（主参考，~16KB）

加载时机：进入 Step 2-4 时务必读取，作为 9 段模板、4 杠杆定义、subject_type 分流细则的权威。

### `references/narrative-driven-variants.md`（~80KB）

加载时机：当 subject_type=character 或 hybrid 时按需 grep 加载。包含 11 个 character archetype 的完整 L1-L4 取值池、5 维度叙事变量取值池、玩法误导高危清单。

不要全文读取（80KB 太大），用 grep 按关键词定向取片段：

```
grep -n "moment\|character_goal\|reward_signal" references/narrative-driven-variants.md
grep -n "误导高危\|fidelity" references/narrative-driven-variants.md
grep -n "archetype" references/narrative-driven-variants.md
```

### `references/poster-adapter-v4.md`（~31KB）

加载时机：当用户明确做**竖版海报**且需要 v4 时期的「图形比例层 + 表现因素层」详细取值池时。v5 主源已整合，多数情况下不需要读这一份。

### `assets/cover.html`（~145KB · 学习控制台）

This is the visual control panel that shows the SOP options to the user. Use cases:

- 用户问「能不能给我看选项池」「想自己挑视角 / 版式 / 配色」 → 把这个 HTML 部署到本地 / anydev 让用户浏览
- 用户做新游戏想 hands-on 选 archetype → 用这个页面交互式选项

部署方式（最简）：

```bash
cd <skill 路径>/assets && python3 -m http.server 8080
# 然后访问 http://localhost:8080/cover.html
```

If the user already has the asset deployed elsewhere (e.g., `wiki/sources/game-poster-learning-sop/cover.html` in HuaClaw repo), reference that location instead of redeploying.

## Common Anti-Patterns to Avoid

1. **「品类 = puzzle 就走 scenario_puzzle」是错的**——必须先问玩法核心动作。
2. **「上传图就够了，模型自己会读」是错的**——图生图模型只复制视觉风格，不推理玩法。Prompt 里必须把玩法动作 + 玩法物件用文字写清楚。
3. **「单一方案就好」是错的**——默认 3 套差异化，且 4 杠杆错开至少 3 个。
4. **「让标题贴边做小 logo」是错的**——v4.17 起 Title Lock 要求标题作为视觉块，宽度 25-55% 或高度 40-80%。
5. **「Banner 当横向截图来写」是错的**——Banner 是商业横幅版式，必须模块化（标题 + 主体 + 辅助符号），三分区职责明确。

## Output Quality Bar

输出应当：

- ✅ 9 段 prompt 完整，标题 / Lock / 负面词都显式
- ✅ 3 套方案 + 1 张差异化矩阵
- ✅ subject_type 在每条 prompt 顶部显式声明
- ✅ 任何 archetype 选取都回溯到「这个游戏的玩法实际是什么」而不是「品类字段是什么」

输出不应当：

- ❌ 上来就写 prompt 不做素材准入
- ❌ 把所有方案都套同一个 archetype
- ❌ 给一段 prompt 然后说「你也可以试试这样」（必须是结构化 3 选 1）
- ❌ 用一段散文说「画一个英雄」式的弱 prompt
