---
created: 2026-05-28
last_updated: 2026-05-29
review_cycle: 90d
decay_threshold: never
status: active
type: methodology
scope: system
form: null
confidence: partially-validated
source: distilled
layer: 2
promoted_from: 对话沉淀（2026-05-28 与 AI 协作讨论）
promoted_to: []
knowledge_kind: procedural
abstraction_level: principle
paired_doc: biz-wiki/game/multi-style-ab-testing.md
author: null
evidence_level: single-conversation
tags: [游戏, 商业视觉, 封面图, 海报图, 横向封面, 竖版海报, 故事性, 多方案, prompt 工程, 方法论]
---

> ⚠️ **v4.x 历史方法论 · 已被 v5.0 取代**（2026-06-05）
>
> 本文档是 v4.x 系列横版方法论，**保留作演进史**。
> **v5.0 起新主源**：
> - 工作流总纲：[`soul/workflows/game-cover-sop.md`](../../soul/workflows/game-cover-sop.md)
> - 学习控制台：[`wiki/sources/game-poster-learning-sop/cover.html`](../../wiki/sources/game-poster-learning-sop/cover.html)
>
> v5 改动要点：
> - 横版/竖版/Banner 共用同一套 SOP（10 步流程 + 主角分型 + 9 段模板 + 8 项硬检查）
> - Banner 6 锁归位（构图层「三条底线」 + 表现层底线）
> - C↔D 晋升路径建立翻车账本沉淀机制
>
> 如需 v4 历史细节请继续阅读下方；如需当前生产规范请到 v5 主源。

---

# 游戏商业视觉故事性多方案分叉方法论（Core + 横向封面 Adapter）

> **来源**：2026-05-28 与 AI 协作讨论 · 关于"锁定风格后多方案该怎么分叉"的方法论确立
> **输入**：在「同一产品多风格 A/B 测试」之外，发现一个更适合**已有明确 DNA**产品的分叉路径；2026-05-29 明确拆分 Core 通用层与比例 Adapter
> **日期**：2026-05-28 / 2026-05-29
> **适用**：已锁定游戏原生美术 DNA，需要在**不背离游戏本体**的前提下，做有意义、可评审、商业可落地的多方案；当前已实证的是横向封面 Adapter，竖版海报 Adapter 待学习沉淀

---

## 术语边界（2026-05-29 固化）

为避免横竖图方法互相污染，后续统一使用以下命名：

| 名称 | 固定含义 | 典型比例 | 备注 |
|------|---------|---------|------|
| **封面图** | 横向游戏列表封面 | `16:9` / `5:3` / `4:3` / `3:2` | 当前本文档已沉淀并部分实证的 Adapter；默认以 `16:9` 母版生成，主体锁中央安全区，裁切两侧背景兼容窄横版 |
| **海报图** | 竖版游戏广告 / 商店 / 活动主视觉 | `9:16` / `2:3` / `3:4` / `4:5` | 默认以 `9:16` 母版生成，主体锁中央安全区，裁切上下背景兼容短竖版 |

> 以后说"封面图"，默认不是泛指所有 key art，而是横向游戏列表容器；说"海报图"，默认指竖版容器。

---

## 【v4 新增 · 2026-05-29】素材准入清单（Step 0 准入门）

> **触发条件**：当用户要求生成「游戏封面图 / 海报图 / 商业视觉」时，AI 必须先检查以下 4 项素材是否齐全；**任一必选项缺失，必须先停下来向用户索取，不允许进入后续 Core Layer / Format Adapter 任何流程**。
>
> **历史背景**：2026-05-29 实证发现 AI 在没有用户提供游戏名的前提下，会用训练先验"猜"游戏名（如把素材描述成 GTA / Resident Evil / Forza 等）。这是**伪识别**，会污染 DNA 卡和 gameplay_lock。本节作为最强硬约束加入。

### 素材清单

| # | 类型 | 字段 | 必选 | 用途 |
|---|------|------|:---:|------|
| 1 | 文本 | **游戏名字** | ✅ | DNA 卡身份锚 / 标题排版 / Logo 安全区；AI 不允许猜 |
| 2 | 文本 | **广告语 / Tagline** | ⬜ | 副标题 / 底部商业信息；缺失则 Brief 中显式 `null` |
| 3 | 正方形图 | **游戏 ICON（1:1）** | ✅ | 角色资产剥离起点 / 风格 DNA 比对锚（Memory 57615156） |
| 4 | 长方形图 | **游戏画面截图** | ✅ | 真实玩法可视化锚定 → `gameplay_lock` 与玩法 Fidelity 自检（Step 8）的事实基准 |

### AI 行为协议

收到生成需求时，**第一动作**必须是：

```text
在生成之前，请先确认提供以下素材：

  ✅ 必选 1：游戏名字（文本）
  ⬜ 可选  ：广告语 / tagline（如有）
  ✅ 必选 2：游戏 ICON（正方形图）
  ✅ 必选 3：游戏画面截图（长方形图）

【为什么需要】
- 游戏名字 → AI 无法靠看图识别游戏；必须由你提供
- ICON → 角色资产剥离 / 风格 DNA 锚定起点
- 画面截图 → 玩法 Fidelity 自检的基准（防止把三消画成桌游）
```

### 完整性检查表

| 项目 | 检查 | 缺失时行为 |
|------|------|-----------|
| 游戏名字 | 文本是否给出？ | 停下来索取，不接受"随便起一个"或"先不重要" |
| 广告语 | 文本是否给出？ | 可继续，Brief 中 `tagline: null` 显式标注 |
| ICON | 是否提供 1:1 图？ | 停下来索取；横图≠ICON，要明确指出 |
| 截图 | 是否提供横向截图？ | 停下来索取；海报/Key Art ≠ 截图 |

### 反模式

- ❌ 用户没给游戏名 → AI 凭训练先验猜测"这看起来像 XX 游戏"
- ❌ 用户没给 ICON → AI 直接用泛化 DNA 卡进入选项流程
- ❌ 用户没给截图 → AI 跳过玩法 Fidelity 自检，假设玩法类型
- ❌ 用户给的"截图"实为另一张海报 → AI 不指出差异，直接当玩法证据

### 适用范围

本清单**对横向封面图、竖版海报图都生效**。Format Adapter 切换不改变素材准入要求。Step 0 不通过 → 后续步骤全部不允许执行。

### 输入素材 ≠ 输出画面元素（2026-05-29 v4.3 修正）

**实战失败反馈**：`Tricky Puzzle` 首轮 GPT Image 生成结果质量明显下降，并且封面图中出现游戏 ICON。用户明确指出：**封面图里出现游戏 icon 是绝对不能接受的表现**。

因此新增硬约束：

> Step 0 提供的 `ICON` / `游戏截图` 都是 **reference-only inputs**，不是可放入画面的素材。默认情况下，封面图 / 海报图里禁止出现 app icon、方形图标、手机截图框、底部导航、关卡菜单 UI、loading bar 或对截图的直接复刻。

| 素材 | 正确用途 | 默认禁止 |
|------|----------|----------|
| ICON | 角色资产剥离 / 色彩 DNA / 线条与 UI 风格锚定 | **禁止出现在封面/海报画面内** |
| 游戏截图 | 玩法机制 / 真实 UI 语言 / gameplay_lock 基准 | 禁止复刻截图 UI、关卡菜单、底部导航、手机框、loading bar |

每条最终 prompt 必须追加：

```text
Do not include the game app icon, square app icon, mobile app store icon, desktop icon,
phone screenshot frame, bottom navigation bar, loading bar, level menu UI, or direct copy of the provided screenshots.
Use the provided icon and screenshots only as reference for art style, character identity, UI color language, and gameplay fidelity.
```

例外：只有当用户明确要求「强转化买量广告卡」且明确说要展示 app icon / download button 时，才允许出现 ICON。默认的横向封面图和竖版海报图一律禁止。

---

## 方法论分层：Core Layer + Format Adapter

本文档不再把所有规则都绑定在 `16:9` 上，而拆成两层：

```text
游戏商业视觉方法论
├── Core Layer：游戏视觉核心锁（跨比例复用）
│   ├── 游戏 DNA 锁
│   ├── 风格 Fidelity
│   ├── 角色 Fidelity
│   ├── 玩法 Fidelity / gameplay_lock
│   ├── 高危玩法误导清单
│   ├── 角色资产剥离 + 姿态重构原则
│   └── Prompt 双层结构
│
├── Format Adapter A：横向封面图（已沉淀）
│   ├── 横向容器声明：16:9 / 5:3 / 4:3 / 3:2
│   ├── 横向安全裁切：16:9 母版 → 裁左右背景兼容 5:3 / 4:3 / 3:2
│   ├── 横向构图与缩略图识别
│   ├── 4 杠杆差异化矩阵
│   └── 横向封面 prompt 模板
│
└── Format Adapter B：竖版海报图（已沉淀，见 game-poster-learning-sop.md）
    ├── 图形比例层 / 表现因素层分离
    ├── 8 个竖版构图模板
    ├── 标题 / 主体 / 留白 / 动线占比阈值
    ├── 周期性喂图学习与反馈进化协议
    └── 竖版海报 prompt 思考契约
```

### 可跨比例复用的内容

以下内容属于 **Core Layer**，后续学习竖版海报图时直接复用，不重新发明：

- 游戏 DNA 锁
- 三维 Fidelity（风格 / 角色 / 玩法）
- `gameplay_lock`
- 高危玩法误导清单
- 从真实游戏 icon / 截图中剥离角色资产，而不是纯 prompt 重绘
- 保持角色身份一致前提下做姿态重构 / 动作迁移
- Prompt 双层结构（思考契约 + 自然语言终端 prompt）
- "视觉差异化 ≠ 玩法真实性"这条红线

### 必须随比例重学的内容

以下内容属于 **Format Adapter**，横竖图不能直接互套：

- 构图重心与视觉动线
- 主角占画比例
- 场景展开方式
- 标题 / CTA / 奖励信息的安全区
- 留白位置
- 横向缩略图识别 vs 竖向海报冲击力

> 结论：竖版海报图学习时，只新增 Vertical Poster Adapter；不要推翻 Core Layer，也不要污染已沉淀的横向封面 Adapter。

---

## 核心论点

**在锁定风格之后，多方案分叉的默认维度，不应该再是"换风格"，而应该是"换故事"。**

\[ \text{多方案分叉} = \text{同一风格 DNA} + \text{不同叙事时刻 / 角色任务 / 情绪目标} \]

---

## 为什么是故事性，不是风格

### 风格分叉的问题

锁定 DNA 之后还做风格分叉（糖果 3D / 编辑海报 / 赛博潮流），等于**在重新改游戏气质**。这违反了 Skill 14281778 + 19794651 的铁律：风格化只能服务游戏本体，不能凌驾游戏本体。

### 故事性分叉同时满足三件事

| 目标 | 风格分叉 | 故事性分叉 |
|------|---------|----------|
| 保住游戏本体 | ❌ 容易概念过载 | ✅ DNA 完全锁定 |
| 保住方案差异化 | ✅ 但代价是跑偏 | ✅ 来自叙事，不来自风格宇宙 |
| 保住可评审性 | ⚠️ 评审凭模糊直觉 | ✅ 能明确说"我要邀请感 / 胜利感 / 悬念感" |
| 适合商业 A/B | ⚠️ 变量太多无法归因 | ✅ 风格、角色、色彩全锁，只测叙事偏好 |

### 与「多风格 A/B 测试」的关系（**不冲突，是接力**）

| 阶段 | 用什么方法 | 适用场景 |
|------|----------|---------|
| 进入陌生市场 / 不知道用户偏好哪种调性 | `multi-style-ab-testing.md`（多风格分叉） | 冷启动、跨代际、跨文化 |
| 已锁定风格 DNA / 知道用户喜欢什么调性 | **本文档**（故事性分叉） | 商业化迭代、CTR 优化、上架 A/B |

**先用多风格找到对的风格，再用故事性挖深这个风格的最大转化潜力。** 这两份方法论是上下游关系。

---

## 5 个故事维度（结构化变量，不是泛泛而谈）

每个 story_mode 必须由这 5 个维度组合定义，不允许只写"更有故事感"。

### 1. 时间点（Moment）

> 这张图发生在故事的哪一秒？

| 取值 | 含义 | 心理效应 |
|------|------|---------|
| `before` | 即将发生 | 悬念最强，"接下来会怎样" |
| `during` | 动作爆点 | 冲击最强，"正在发生" |
| `after` | 结果已发生 | 成就感最强，"赢了/解决了" |

**这是最重要的故事开关。** 同一个角色、同一个动作，仅仅因为"时间点"不同，故事完全不同。

---

### 2. 角色任务（Character Goal）

> 主角此刻在"做什么"？

| 取值 | 示例 |
|------|------|
| `invite` | 邀请你 / 欢迎你进入 |
| `solve` | 解决玩法问题 |
| `face_crisis` | 面对危机（轻量级） |
| `victory` | 取得胜利 |
| `discover` | 发现惊喜 / 探索新区域 |
| `guide` | 带你进入新世界 |

> ⚠️ 同一个动作（如"举盾"），在不同 character_goal 下含义完全不同：
> - 举盾欢迎你进入 → invite
> - 举盾挡住危机 → face_crisis
> - 举盾庆祝通关 → victory

---

### 3. 观众关系（Viewer Relation）

> 画面在对谁说话？

| 取值 | 效果 |
|------|------|
| `direct_eye_contact` | 直面玩家，强点击率，最像邀请 |
| `look_at_target` | 角色看向画面里的目标，故事正在发生 |
| `back_to_viewer` | 角色背对玩家，更像"探索/进入" |
| `multi_character` | 群像互动，关系感最强 |

---

### 4. 冲突强度（Conflict Level）

> 有 tension，但强度怎么控制？

| 取值 | 适用游戏类型 |
|------|------------|
| `none` | 治愈休闲 / 收集养成 |
| `low (safe excitement)` | 休闲 puzzle / 三消 / 益智 — **大多数休闲游戏的甜点区** |
| `medium` | 卡牌 / 策略 / 轻度 RPG |
| `high` | 动作 / 对抗 / 硬核 |

> 🎯 **safe excitement** 概念：对休闲游戏，不能做"生死对决"，但仍然要有戏。
> 例如：一块关键拼图快到位了 / 城堡机关要被解开了 / 宝箱要开了 / 路要打通了 / 奖励即将喷发了。

---

### 5. 结果导向（Reward Signal）

> 这张图的目标是传达哪种玩家欲望？

| 取值 | 玩家心理 |
|------|---------|
| `try_it` | 我想点进去试试 |
| `nearly_winning` | 我觉得这局快赢了 |
| `loot_rich` | 我觉得奖励很多 |
| `world_interesting` | 我觉得这个世界很有趣 |
| `character_lovely` | 我觉得这个角色很可爱 |

---

## 【v4.4 新增 / v4.10 加固】AI 默认行为约束（2026-05-29 · 基于 Tricky Puzzle 实证；2026-06-01 基于 Grill Skewer Pop / Brain Trick / Girl Rescue 复盘加固）

> **触发背景**：2026-05-29 用户要求"以后不要我提了用上杠杆差异化策略你才用上"。这意味着 4 杠杆差异化策略是**默认行为**，不需要用户显式触发。
> **实证来源**：Tricky Puzzle 首轮 GPT Image 生成质量下降 + 封面出现游戏 ICON。
> **v4.10 加固背景**：2026-06-01 三个案例复盘发现 AI 会在局部优化时漏掉全局约定：一是把 `no text / no logo` 写进 Negative 导致游戏名被模型压掉；二是忘记默认 A/B/C 多剧本，只给单 prompt。此类错误视为 SOP Preflight 未执行。

### 默认行为规则（含 Prompt Preflight）

#### 规则 0：【v4.15 修正】封面 Prompt Preflight（单层清晰标题 / 多剧本 / 禁止自相矛盾）

**行为约束**：每次用户要求「生成某游戏封面 prompt」时，AI 在输出正文前必须先过以下 8 项检查，缺一项即视为 SOP 未完成：

| # | 检查项 | 必须满足 |
|---|--------|----------|
| 1 | 单层清晰标题 | 每条 prompt 必须有 `[Title Lock — Flexible Single Title 2.1]`；游戏名只出现一层清晰可读标题，位置可居中/中上/侧中/边缘，但禁止机械贴边和角落小贴片 |
| 2 | 禁止冲突 | Negative 里禁止裸写 `no text` / `no logo`；必须写 `No extra readable text except the exact game title "<game>"`，并禁止 duplicate title layers / giant background title text |
| 3 | 多剧本 | 默认输出 A/B/C 三套差异化 prompt；除非用户明确说「只给一版」 |
| 4 | 主体类型 | 先判断 `subject_type`：`character` / `gameplay_object` / `hybrid` / `scenario_puzzle` |
| 5 | 玩法可读 | 不能只画好看的主题图，必须体现真实玩法机制 |
| 6 | 参考图使用 | 不复制 UI 截图、不重建模糊脸，只抽取视觉 DNA / 资产特征 / 玩法线索 |
| 7 | 三套差异化 | A/B/C 必须在构图、情绪、玩法焦点上真的不同，不只是换措辞 |
| 8 | 出海素材裁切规范 | 横版 16:9：中央 75% 宽度安全区；竖版 9:16：中央 70% 高度安全区；Banner：只裁宽度三档母版（3.5:1 / 5.2:1 / 8:1），上下不裁高度 |

**标准开场框**（在写 prompt 前先输出）：

```text
策略判断：
- subject_type: <character | gameplay_object | hybrid | scenario_puzzle>
- 玩法核心: <一句话>
- 封面必须表达: <3 个要点>
- 本次输出: A/B/C 三套差异化方案
```

#### 规则 1：默认出多题材方案，不用户提醒

**行为约束**：当用户要求生成封面图/海报图时，AI **默认输出至少 3 个故事题材方案**供用户选择，不需要用户说"给我多个方案"。

例外：用户明确指定只要 1 个方案时，才只出 1 个。

#### 规则 2：每条 prompt 必须显式包含 L1/L2/L3/L4

**行为约束**：每条自然语言 prompt 产出前，必须先在思考契约里明确填入 L1 / L2 / L3 / L4 四个维度的具体取值，线性化时必须把四个杠杆全部写入 prompt，不能省略。

格式示例（在 prompt 中可见）：
```
L1 camera: low-angle heroic shot
L2 lighting: warm golden hour with soft rim
L3 setting: throne hall with marble pillars
L4 visual weight: hero dominant 65%+
```

#### 规则 3：绝对禁止出现游戏按钮

**行为约束**：**默认情况下，封面图和海报图中永远不允许出现购买按钮 / download button / app store badge / 评分按钮 / 分享按钮**。

例外：只有用户**明确要求**「强转化买量广告卡」并明确说要在画面里展示 app icon / download button 时，才允许出现。

违规处理：任何一条 prompt 如果没有包含 ICON 负面锁，视为 SOP 执行不合规，需要返工。

#### 规则 4：主动应用 4 杠杆差异化，不等待用户提醒

**行为约束**：4 杠杆差异化策略是**每次生成多方案时的默认行为**，不是可选项。AI 在产出多方案时必须：

1. 先输出差异化矩阵（L1/L2/L3/L4 × N 方案的表格）
2. 自检：每两个方案至少错开 3 个杠杆
3. 每条 prompt 线性化时显式写入 L1/L2/L3/L4 取值

**不需要用户说"记得用 4 杠杆差异化策略"，AI 必须自己记得**。

#### 规则 4.5：【v4.9 / v4.10 新增】主体类型路由（不要把所有游戏都当人物封面）

**行为约束**：在写 A/B/C prompt 之前，AI 必须先判断封面主体类型，不允许默认套用「人物 C 位」模板。

| subject_type | 适用场景 | 正确策略 | 典型案例 |
|--------------|----------|----------|----------|
| `character` | 游戏截图/ICON 中存在清晰人物主体，玩法也由人物动作承载 | `Subject Lock` + 角色保真 + 姿态重构 | RPG / 动作 / 角色经营 |
| `gameplay_object` | 人物很小或不是核心，玩法物件才是主体 | `Game Asset Lock` + 玩法物件保真 + 玩法机制可读 | `Grill Skewer Pop`：烤串 / 烤炉 / 三消匹配 |
| `hybrid` | 人物是情绪钩子，但玩法机制必须同屏读出 | 人物冲突 + 玩法前景/路径/棋盘同权重 | `Girl Rescue`：公主/龙 + 方向箭头方块路径 |
| `scenario_puzzle` | 情境反转 / 找线索 / 脑洞解谜，核心是「哪里不对」 | 荒诞情境 + 高亮线索 + 手势/放大镜/问号，不做纯人物海报 | `Brain Trick`：找热狗 / 穷人家庭 / 社交反转 |

**v4.10 三个实证结论**：

1. `Grill Skewer Pop` 不能只画「好看的烤串广告」，必须画出 **三消/合成玩法**：格子/烤炉棋盘、三个相同烤串连线、combo burst。
2. `Brain Trick` 不能只画人物关系图，必须画出 **脑洞解谜行为**：荒诞场景、明显但不直白的线索、手势/问号/放大镜引导。
3. `Girl Rescue` 不能只画「公主大战龙」，必须画出 **方向箭头方块救援路径**：前景箭头块、正确路径、龙威胁、公主目标点。

#### 规则 5：【v4.7 升级 — AI 内部闭环执行】角色资产剥离（AI 自动跑剥离图层 + 图生图，用户零额外操作）

**v4.5 → v4.6 → v4.7 演进**：
- v4.5：在 prompt 文字层加 `Subject Lock` 段 → 失败（text-to-image 模型不"看"参考图）
- v4.6：要求 AI 给出 image-to-image / Midjourney --cref / ComfyUI 三选一**工具路径**让用户去操作 → 失败（用户被迫切平台 / 当工具搬运工 / 改流程）
- **v4.7：AI 在 SOP 内部自动跑完整条剥离链路，用户输入端零变化（依然只给 icon + 截图 + 游戏名），输出端零变化（依然只看到最终封面）**

**v4.7 行为约束（核心：AI 闭环原则）**：

1. **❌ 禁止让用户切平台 / 当工具搬运工**。具体禁止：
   - 让用户去 ChatGPT 网页手动上传截图
   - 让用户去 Discord 上传图床获取 URL
   - 让用户自己跑 ComfyUI 工作流
   - 让用户在多个工具之间复制粘贴 prompt
2. **✅ AI 必须使用 3000 平台 MCP 工具链自动跑完**（默认通道）：
   ```
   [用户给的截图]
       ↓ AI 自动 base64 上传
   [3000 inner_url]
       ↓ AI 自动调 3000_comfyui_divide（按 hints 拆主角 / 配角 / 背景）
   [纯净角色透明 PNG × N]
       ↓ AI 自动调 3000_generate_image（model=gpt-image-2, image=PNGs, input_fidelity=high）
   [角色一致的封面图]
       ↓ AI 异步轮询 3000_query_generate_async_task_result
   [给用户最终图]
   ```
3. **唯一可让用户做的事**：提供 AI 文件系统访问不到的物理素材（一次性给 icon + 截图 + 游戏名），其他全程 AI 自动跑。
4. **保留 v4.5 的 Subject Lock + Pose Reconstruction 文字段** 写进图生图的 prompt，作为**视觉输入的语言锚点辅助**（不是唯一约束，视觉输入是核心）。

**3000 MCP 工具链调用清单（AI 内部执行，用户不可见）**：

| 步骤 | MCP 工具 | 关键参数 | 作用 |
|---|---|---|---|
| 1 | `3000_get_app_list` | — | 拿 app_id（"微信游戏设计"=495） |
| 2 | `3000_get_upload_token` | app_id | 拿 upload_url + token |
| 3 | （HTTP POST 到 upload_url） | base64 图片 | 拿 inner_url |
| 4 | `3000_comfyui_divide` | image=inner_url, hints="主角描述,配角描述,背景" | 输出多个透明 PNG 图层 |
| 5 | `3000_query_generate_async_task_result` | trigger_id | 轮询拆分结果 |
| 6 | `3000_generate_image` | model_name=gpt-image-2, image=[PNG_url1,2,3], input_fidelity=high, prompt=场景重构 | 图生图 |
| 7 | `3000_query_generate_async_task_result` | trigger_id | 轮询出图结果 |

**违反处理**：
- AI 让用户自己切平台、自己上传、自己复制 URL → **视为 v4.7 不合规，需返工**（v4.7 新增）
- AI 只交付纯文字 prompt 让用户去 ChatGPT 手动跑 → **视为 v4.7 不合规，需返工**（v4.6 已立 + v4.7 加固）

**为什么 v4.7 必须 AI 闭环**：v4.6 的"给用户三条工具路径让他选"看似严谨，实际上等于把"流程整合"工作甩给用户——用户的真实诉求从来都是「输入端不变 + 输出端拿到正确结果」，**整合工具链是 AI 的本职工作，不是用户的负担**。3000 平台 MCP 已经把"剥离图层 + 图生图 + 异步轮询"全部 API 化，AI 没有任何理由不闭环。

**为什么这条是硬规则**：用户付费生成 N 张图的核心目的是让玩家"在商店里一眼认出这是同一个游戏的同一群角色"。如果 AI 自由重绘，封面里的角色和游戏内的角色完全两个人 → 玩家点进去发现货不对板 → CTR 高但留存崩。本规则与 Step 8 玩法 Fidelity 同等级。

### 违反处理

| 违规场景 | 处理方式 |
|---------|---------|
| 用户没说多方案，AI 只出了一个方案 | 视为未完成 SOP，用户可要求返工 |
| prompt 没有 `[Title Lock — Flexible Single Title 2.1]` | 视为 v4.15 Preflight 不合规，需返工 |
| Negative 裸写 `no text` / `no logo`，导致游戏名被禁止 | 视为 prompt 自相矛盾，需改为 `No extra readable text except the exact game title`，并禁止重复标题层和背景巨字层 |
| 没有先输出 `subject_type / 玩法核心 / 封面必须表达 / A-B-C 输出声明` 策略框 | 视为 v4.10 Preflight 不合规，需补写 |
| prompt 里没有 L1/L2/L3/L4 显式表述 | 视为 SOP 执行不合规，需补写 |
| prompt 没有按钮负面锁（默认情况） | 视为 SOP 执行不合规，需补写 |
| 没有先输出差异化矩阵就出 prompt | 视为 SOP 执行不合规，需返工 |
| **prompt 用通用 chibi 描述自由重绘人物，未从素材剥离角色** | **视为 SOP 执行不合规，需返工**（v4.5 新增） |
| **只交付纯文字 prompt，未给出 image-to-image / Midjourney --cref / ComfyUI IP-Adapter 任一可执行路径** | **视为 SOP 执行不合规，需返工**（v4.6 新增 — 因为纯文字无法兑现角色一致性） |
| **AI 让用户切平台 / 当工具搬运工 / 自己上传图 / 自己复制 URL** | **视为 SOP 执行不合规，需返工**（v4.7 新增 — 工具链整合是 AI 本职工作，必须走 3000 MCP 内部闭环） |

---

## 标准 SOP（11 步 + v4.10 Preflight — 2026-06-01 加固，含标题锁 / 多剧本 / 主体类型路由）

```text
风格锁定后的多方案生产流程
─────────────────────────
Step 0. 【v4 新增】素材准入检查                      ← 最强硬约束
        - 游戏名字 ✅ 必选 / 广告语 ⬜ 可选
        - ICON 正方形 ✅ 必选 / 游戏画面截图 ✅ 必选
        任一必选缺失 → 停下来索取，不允许进入 Step 1
Step 0.5.【v4.10 新增】Prompt Preflight + 主体类型路由
        - 先输出策略判断框：subject_type / 玩法核心 / 封面必须表达 / A-B-C 输出声明
        - 每条 prompt 必须有 [Title Lock — Flexible Single Title 2.1]：只保留一层清晰标题；位置可居中/中上/侧中/边缘，但禁止机械贴边和角落小贴片
        - Negative 禁止裸写 no text / no logo；只能写 no extra readable text except exact game title，并禁止 duplicate title layers / giant background title text
        - 默认 A/B/C 三套差异化剧本，除非用户明确说只要一版
        - subject_type 必须在 character / gameplay_object / hybrid / scenario_puzzle 中判定
        - 横版封面必须启用 safe-crop：16:9 母版主体锁中央 75% 宽度，左右各 12.5% 只放可裁切背景，兼容裁成 5:3 / 4:3 / 3:2；2:1 作为横向宽屏特例从 16:9 裁上下
        - 竖版海报必须启用 safe-crop：9:16 母版主体锁中央 70% 高度，上下各 15% 只放可裁切背景，兼容裁成 2:3 / 3:4 / 4:5
        - 长条 banner 必须启用 width-only safe-crop：只裁左右，不裁高度；标准长条 3.5:1 母版（74%×90% 安全区），超长 5.2:1 母版（76%×90% 安全区），极窄广告条 8:1 母版（74%×90% 安全区）
Step 1. 输出《游戏原生美术 DNA 卡》              ← 必须用户确认
        【v3 新增】DNA 卡里必须包含 gameplay_lock 字段
        【v4 强调】DNA 卡必须基于 Step 0 提供的 ICON + 截图建立，禁止靠图像识别猜
Step 2. 选定一个 style_mode（如 soft-3d-casual-royal-puzzle）
Step 3. 不发散风格，发散 story_mode
Step 4. 每个 story_mode 绑定 5 维度变量（时间点/角色任务/观众关系/冲突/结果导向）
Step 5. 用 4 杠杆差异化矩阵自检                    ← v2 防止"伪分叉"
Step 6. Fidelity 默认全部 ≥ 85%                    ← v2 不混入低 Fidelity 探索方案
Step 7. 生成 prompt 时只改故事变量+杠杆，不改 DNA 锁
Step 8. 【v3 新增】玩法 Fidelity 自检              ← 防止"玩法误导"
Step 9. 【v4.4 新增】AI 默认行为检查               ← 不需用户提醒才执行
        - 默认出多题材方案（≥3 个）
        - 每条 prompt 必须显式包含 L1 camera / L2 lighting / L3 setting / L4 visual weight
        - 默认禁止出现游戏按钮（每条 prompt 必带购买/下载按钮负面锁）
        - 主动应用 4 杠杆差异化，不等待用户提醒
Step 10. 【v4.6 立 / v4.7 改写】Prompt 内置 Subject Lock + Pose Reconstruction
        - prompt 是否有 Subject Lock 文字描述？（视觉输入的语言锚点辅助）
        - prompt 是否有 Pose Reconstruction？（按故事题材改动作 / 表情 / 视线 / 道具）
        - 是否避免了 generic chibi / cute character 等自由人设描述？
        以上任一漏做 → 返回 Step 7 重写
Step 11. 【v4.7 新增】AI 自动执行 3000 MCP 剥离图层 + 图生图闭环   ← 角色一致性核心硬约束
        AI 内部自动执行（用户零额外操作，不需要切平台）：
        ① 读取 Step 0 的 ICON + 截图 → base64 上传 3000 → 拿 inner_url
        ② 调 3000_comfyui_divide(image=截图, hints="主角描述,配角描述,背景")
           → 输出 N 张纯净透明 PNG 角色图层 + 1 张背景图层
        ③ 异步轮询 3000_query_generate_async_task_result 拿剥离结果
        ④ 调 3000_generate_image(model_name=gpt-image-2, image=[剥离后的角色PNG列表],
           input_fidelity=high, prompt=Step 10 的多方案 prompt)
        ⑤ 异步轮询拿最终封面图
        ⑥ 直接给用户最终图（用户不接触 inner_url / trigger_id / token / 异步状态）

        ⚠️ v4.7 关键认知：
           - 工具链整合是 AI 本职工作，不是用户负担
           - 用户输入端永远只给 icon + 截图 + 游戏名
           - AI 必须用 3000 MCP 内部闭环，不允许让用户切平台 / 当搬运工
           - 图生图比 text-to-image 更强：把"角色 PNG 作为视觉输入"喂模型，
             比英文 prompt 描述角色信息密度高 100×，是兑现角色一致性的唯一物理路径
```

> ⚠️ Step 0 / Step 0.5 / Step 5 / Step 6 / Step 8 / Step 10 / Step 11 都是硬约束，任何一步漏做 = 没完成 SOP。
> ⚠️ Step 0 是最前置的硬门槛——AI 不允许靠训练先验猜游戏名，必须用户提供。
> ⚠️ Step 0.5 是 prompt 输出前的防漏项闸门——游戏名 Title Lock、多剧本 A/B/C、subject_type 路由、Negative 禁止自相矛盾都在这里拦截。
> ⚠️ Step 11 是出图的最终物理保障——前面 10 步都是为它做准备；漏 Step 11 走纯 text-to-image，角色一致性就崩了。

---

## 【v2 新增】视觉差异化 4 杠杆矩阵（防伪分叉的核心机制）

> **作用域（2026-05-29 v4.2 修正）**：本节属于 **Core Layer**，**对横向封面图、竖版海报图都生效**，**跨 Adapter 复用**。原本被误读为"只对横向封面"是因为本节首次实证在横向封面上，但 4 杠杆是「同 DNA 下做 N 个方案的差异化数学」，与容器比例无关。竖版海报的具体映射见 `game-poster-learning-sop.md` §0.7。
>
> **背景**：v1 方法论只用「5 个故事维度」做分叉，但实测发现，如果**镜头/光线/场景/角色占比**这 4 个视觉强力杠杆全锁死，生成出的 5 个方案人眼扫过去仍然觉得"都是同一个画面换了个动作"。这是**伪分叉**。

### 4 杠杆定义

| 杠杆 | 它管什么（抽象 · 跨题材） | 当前实例取值池（休闲皇室拼图，需按题材替换） |
|------|--------------------------|----------------------------------------------|
| **L1 镜头机位**（Camera） | 视角与拍摄机位 | 平视中景 / 仰角英雄镜 / 俯视棋盘 / 过肩主观 / 大特写 / 远景剪影 / 等距悬浮 |
| **L2 光线戏剧性**（Lighting Drama） | 戏剧性与情绪 | 暖光柔和 / 冷暖对撞 / 黄金时刻 / 单光源黑暗剧院 / 月夜冷光 / 高饱和泛光 / 漫射魔法 |
| **L3 场景空间**（Setting） | 世界容器（强题材依赖） | 主厅 / 屋顶夜景 / 户外花园 / 迷你世界 / 王座大厅 / 地牢秘室 / 桌面棋盘 |
| **L4 角色占画比例**（Hero Weight） | 角色与玩法元素权重 | 主导 60%+ / 50-50 平衡 / 玩法主导（角色 ≤25%） / 缺席或仅背影 / 多角色同框 |

> ⚠️ **「它管什么」一列是永久定义，不能换**；**「当前实例取值池」一列是 case 数据，每个新游戏题材必须重写一份**——硬套休闲皇室拼图的取值会污染新项目（例如赛车 / 三国 / 二次元 / 暗黑生存的 L3 场景完全不同）。

### 强制差异化规则

**每个方案对比上一个方案，至少在 4 杠杆中错开 3 个杠杆**，否则视为伪分叉、必须返工。

### 输出格式：差异化矩阵表（必须先输出再写 prompt）

每次产出多方案前，**必须先输出**类似下表，让用户/自己一眼看出"差距够不够大"：

| 维度 | 方案 A | 方案 B | 方案 C | 方案 D | 方案 E |
|------|-------|-------|-------|-------|-------|
| L1 镜头 | 仰角 | 俯视 | 远景平视 | 等距悬浮 | 过肩主观 |
| L2 光线 | 戏剧聚光 | 均匀柔光 | 黄金日落 | 漫射魔法 | 冷蓝+金对撞 |
| L3 场景 | 王座大厅 | 棋盘桌面 | 城堡屋顶 | 悬浮岛屿 | 地牢秘室 |
| L4 占比 | 60% | 25% | 50% | 15% | 40%背影 |

> 📌 矩阵自检：横向看每两列至少 3 行不同 → 通过；任意两列只 1-2 行不同 → 返工。

---

## 【v2 新增】Fidelity 默认档约束（2026-05-28）

### 默认行为

**多方案产出默认全部 Fidelity ≥ 85%**，即"原生 DNA 升级"档。**不混入低 Fidelity 探索方案**。

### 跨界探索方案的显式触发

只有当用户输入包含以下关键词之一时，才允许产出 Fidelity 50-75% 的"跨界 / 概念化"方案：

- `跨界`
- `概念化`
- `节日特投`
- `探索向`
- `扩风格`
- `运营`

且跨界方案**必须单独成组、不与原生方案混合呈现**，并在方案标题处明确标注 `Fidelity 70%（探索向）` 之类的标签。

### 为什么默认只出 85%+

实测教训（2026-05-28，《Come Match》项目）：当 5 个方案里混入 2 个 Fidelity 70% 的跨界方案，会出现以下问题：
1. **决策成本变高**：用户得先判断"这跨界方案要不要"，再决策视觉方向
2. **风险耦合**：跨界方案如果跑得好，会拉走对原生方案的注意力，导致原生方案没被充分迭代
3. **角色资产污染风险**：低 Fidelity 方案需要大幅度风格化，容易与 Skill 19794651 的"局部资产保护"红线冲突

所以默认行为是**保守**：用户没显式说要跨界，就一律产出原生 90% 档。

---

## 【v3 新增】玩法 Fidelity 锁（防玩法误导，2026-05-28 v3）

> **背景**：v2 的 4 杠杆矩阵成功拉开了 5 方案的视觉差距，但实战《Come Match》后发现：方案 B2「俯视棋盘 + 木质桌面 + 网格摆放」在视觉上确实独立，但**意外把游戏类目从"三消"暗示成了"桌游/棋类"** —— 用户被吸引下载后预期落差，**CTR 没问题但留存崩**。这比"伪分叉"更危险。

### 三维 Fidelity 体系（v3 完整版）

| Fidelity 维度 | 管什么 | 由什么锁定 |
|--------------|--------|-----------|
| **风格 Fidelity** | 视觉是否像原游戏（色调/渲染/比例） | DNA 卡的 `style_mode` |
| **角色 Fidelity** | 角色身份是否一致 | DNA 卡的角色资产 + Memory 57615156/72072029 |
| **【v3 新增】玩法 Fidelity** | 封面里展示的玩法元素是否符合游戏真实玩法机制 | DNA 卡的 `gameplay_lock` |

> 三维 Fidelity 默认全部 ≥85%，缺一不可。

### DNA 卡升级：新增 `gameplay_lock` 字段

DNA 卡（中间产物 JSON）必须新增字段，例如：

```json
{
  "style_mode": "soft-3d-casual-royal-puzzle",
  "character_assets": ["king-with-crown", "queen", "prince"],
  "gameplay_lock": {
    "primary_genre": "match-3",
    "core_mechanic": "swap and match colorful gems to clear the board",
    "visual_signature": ["floating colored gems", "sparkle/burst effect", "score combo"],
    "negative_genre_lock": ["board game", "chess", "card game", "billiards", "solitaire", "bubble shooter"]
  }
}
```

### 高危杠杆值清单（容易触发玩法误导）

经实战归纳，4 杠杆里以下取值组合**最容易触发玩法误导**，使用时必须谨慎：

| 杠杆 | 高危取值 | 容易暗示的错误类目 | 替代写法 | 验证状态 |
|------|---------|------------------|---------|---------|
| L1 镜头 | 俯视棋盘 70°（top-down board view） | 桌游/棋类/卡牌 | 配合"floating gems / no grid lines / no wooden board"中和 | 🟢 已实证 |
| L3 场景 | 木棋盘桌面（wooden board, tabletop） | 桌游/桌面玩具 | 改"floating gem array / magical air-suspended gems" | 🟢 已实证 |
| L3 场景 | 卡牌桌（card table） | 卡牌类 | 改"crystal display / treasure platform" | ⚪ 推测 |
| L3 场景 | 球桌（pool table / billiard） | 台球类 | 直接换场景 | ⚪ 推测 |
| L3 场景 | 旋转转盘（spinning wheel） | 老虎机/抽奖 | 慎用，除非游戏本身有抽奖玩法 | ⚪ 推测 |
| L4 占比 | 玩法元素以"网格阵列方式精确排布" | 策略/桌游 | 改"散落 / 漂浮 / 聚合" | 🟢 已实证 |

> 🟢 已实证 = 至少经过一次真实跑图验证有效；⚪ 推测 = 基于经验推断，未经实战，下次踩到记得升级标记。
> ⚠️ 这张表会随实战不断扩展。每次踩坑后记得回填。

### Step 8 自检 Checklist（出 prompt 前必过）

每个 prompt 写完后，**逐条自检**，任一失败 → 改 prompt：

- [ ] 画面里出现的玩法可视化元素是否符合 `gameplay_lock.primary_genre`？
- [ ] 是否触发了 `negative_genre_lock` 列表里的视觉暗示？
- [ ] 是否使用了"高危杠杆值清单"里的取值？如使用了，是否做了中和处理？
- [ ] 一个**完全不知道这个游戏**的人，看到这张封面，会以为这是什么类目的游戏？答案是否=`primary_genre`？

> 第 4 条是终极检验。如果答案不一致 → 必须改。

### 反向玩法锁（可选增强）

对支持 negative prompt 的模型（如 Stable Diffusion / Flux），可在 prompt 末尾追加：

```
Negative prompt: board game, chess, checkers, card game, billiards, solitaire,
wooden game board with grid lines, tabletop strategy game.
```

> ⚠️ 对 Midjourney 这类不强支持 negative prompt 的模型，依赖 Step 8 自检比加 negative 更可靠。

---

## 【v2 新增】多方案产出标准动作（强制 SOP）

```text
收到"出 N 个方案"需求后的标准动作
──────────────────────────────
0. 【v4.10 新增】先输出《策略判断》
   - subject_type: character | gameplay_object | hybrid | scenario_puzzle
   - 玩法核心: 一句话说明真实玩法
   - 封面必须表达: 3 个要点
   - 本次输出: A/B/C 三套差异化方案（除非用户明确只要一版）
1. 输出《差异化诊断》
   - 如果是首轮：列 4 杠杆 × N 方案的策略矩阵
   - 如果是迭代：先复盘上一轮哪些杠杆没拉开，再列新矩阵
2. 自检：每两个方案至少 3 个杠杆不同
3. 直接产出自然语言 prompt 成品（不需要用户确认方向）
4. Fidelity 全部 ≥ 85%（除非用户显式触发跨界关键词）
5. 【v3 新增】每个 prompt 写完后过一遍 Step 8 玩法 Fidelity Checklist
   - 重点扫"高危杠杆值清单"，命中即必须中和或换写法
6. 【v4.15 修正】每个 prompt 写完后过 Title / Negative Checklist
   - 必须有 [Title Lock — Flexible Single Title 2.1]
   - 必须只保留一层清晰可读标题；标题位置可多样化，但不能机械贴边或缩成角落小贴片
   - Negative 必须允许 exact game title，禁止裸写 no text / no logo，同时禁止 duplicate title layers / giant background title text
```

> ❌ 反模式：跳过诊断直接出 prompt
> ❌ 反模式：诊断完后停下来等用户"确认方向"再写 prompt（过度小心，浪费用户时间）
> ❌ 反模式：v3 — 视觉差异化做对了但忘了玩法 Fidelity 自检（CTR 高留存崩）
> ✅ 正确：诊断 + 4 杠杆自检 + prompt + 玩法 Fidelity 自检 一气呵成

---

## Prompt 双层结构（中间产物 + 终端产物）

> ⚠️ **重要修正（2026-05-28）**：JSON 契约本身不是 prompt，而是"思考契约"。文生图模型（3000 / Midjourney / SD / DALL·E）的输入格式都是**自然语言段落**，不是 JSON。AI 在产出方案时**必须同时给出两层**，或至少给出第二层。

### 第一层：思考契约（中间产物，不可直接投喂）

作用：给"人/AI"做结构化思考，保证不漏要素。每条故事性方案**思考时必须**覆盖以下字段。

```json
{
  "format_adapter": "horizontal_cover | vertical_poster | wide_banner",
  "container": "horizontal game cover",
  "aspect_ratio": "16:9 | 5:3 | 4:3 | 3:2",
  "horizontal_safe_crop": "16:9 master; critical title / subject / gameplay proof inside centered 75% width safe zone; left/right 12.5% are expendable background only",
  "title_treatment": "single readable exact game title only; flexible placement such as center / upper-center / side-center / composed edge placement; inherit scene color, lighting, shadow, material, or motion direction; no duplicate title layers, no giant background title text, no tiny isolated corner sticker",
  "dna_lock": "<游戏原生美术 DNA 一句话描述>",
  "fidelity": "85% | 90% | 95%",
  "story_mode": "<方案标签，如 invitation / puzzle_breakthrough / reward_celebration>",
  "moment": "before | during | after",
  "character_goal": "invite | solve | face_crisis | victory | discover | guide",
  "viewer_relation": "direct_eye_contact | look_at_target | back_to_viewer | multi_character",
  "conflict_level": "none | low | medium | high",
  "reward_signal": "try_it | nearly_winning | loot_rich | world_interesting | character_lovely",
  "negative_style_constraints": "<禁止偏离 DNA 的风格关键词列表>"
}
```

> ⚠️ `negative_style_constraints` 与 Skill 19794651 第 3 步对齐，每条 prompt 末尾**强制**带反向风格锁。

### 第二层：自然语言 Prompt（终端产物，可直接投喂）

把契约**线性化**成连贯英文段落，按以下固定结构组织（v4.10 起为 6 段，标题锁为必填）：

```
段落 1（容器声明）: A <aspect_ratio> horizontal game cover for <游戏类型/题材> called "<game_name>".（封面图用 16:9 / 5:3 / 4:3 / 3:2；推荐先出 16:9 母版；海报图未来换 vertical poster adapter）
段落 2（Title Lock）: [Title Lock — Flexible Single Title 2.1] Render the exact game title once as one clear readable title layer. Placement may be center / upper-center / side-center / composed edge placement, but never a tiny isolated corner sticker or mechanically glued top-edge logo. The title should inherit scene color, lighting, shadow, material, or motion direction while staying legible. Do NOT add any other readable text besides the exact game title. Do NOT create duplicate title layers or giant background title text.
段落 2.5（Horizontal Safe-Crop Layout）: 16:9 母版兼容 5:3 / 4:3 / 3:2。标题、主体、脸、手、玩法证据、关键道具全部放在中央 75% 宽度安全区；左右各 12.5% 只放 atmosphere / scenery / blur / particles / repeated pattern 等可裁切背景。
段落 3（主体与动作 / 玩法物件 / 情境线索）: 按 subject_type 写 Subject Lock / Game Asset Lock / Scenario Puzzle Lock。
段落 4（场景与构图）: 背景 / 中景 / 前景 / Logo 安全区 — 对应 composition 字段。
段落 5（光影与色彩与质感）: 光照方向、色彩重心、材质 — 对应 dna_lock 的展开 + lighting + color_emphasis + energy_level。
段落 6（负面提示）: 禁止 UI / 按钮 / 截图框 / 随机文字，但必须允许 exact game title：No extra readable text except the exact game title "<game_name>"; no duplicate title layers; no giant background title text.
```

**线性化规则**：

1. ✅ 用**自然英文句子**串联，禁止保留 JSON 括号和 key 名
2. ✅ 游戏名必须进入 `[Title Lock — Flexible Single Title 2.1]`，且要求模型只渲染一层清晰 exact title；位置可多样化，但禁止机械贴边、角落小贴片、重复标题层、背景巨字层
3. ✅ DNA 锁的关键词（紫袍 / 金冠 / 半哑光 / 微 SSS 等）必须出现在主体段或风格段，**不能省略**
4. ✅ `story_mode` 的差异化关键词（如 invite gesture / about-to-snap / radial burst）必须出现在主体段
5. ✅ 负面提示禁止裸写 `no text` / `no logo`；必须写 `No extra readable text except the exact game title "<game_name>"`，并禁止 duplicate title layers / giant background title text
6. ❌ 禁止把契约 JSON 当 prompt 直接给用户——必须线性化

### 投喂适配

| 工具 | 输入框 | 负面提示位置 |
|------|--------|------------|
| Midjourney | 单一 prompt 框 | 末尾 `--no ...` |
| SD WebUI / ComfyUI | Positive prompt 框 | 单独的 Negative prompt 框 |
| 3000 | 看 3000 当前的输入约定 | 同上 |
| DALL·E / GPT-Image | 单一 prompt 框 | 直接写 "no xxx, no yyy" 在描述中 |

> 📌 **AI 产出方案的标准动作**：先在脑内填好契约 → 再线性化成 6 段英文（含 Title Lock）→ **只把第二层给用户**（除非用户明确要中间产物用于编程化调用）。

---

## 默认推荐三件套（休闲游戏起手式）

当用户没有明确指定 story_mode 数量与方向时，AI **默认**输出以下三个方案，并标注每个的商业意图。

### 方案 A · 邀请型（Invitation）

| 字段 | 取值 |
|------|------|
| story_mode | `invitation` |
| moment | `before`（第一步动作之前） |
| character_goal | `invite` |
| viewer_relation | `direct_eye_contact` |
| conflict_level | `none` |
| reward_signal | `try_it` |

- **商业意图**：默认主封面、新用户列表点击
- **画面要点**：角色面向玩家、伸手邀请、Logo 一侧、玩法元素形成"通往玩法"的路径

### 方案 B · 解题瞬间型（Puzzle Breakthrough）

| 字段 | 取值 |
|------|------|
| story_mode | `puzzle_breakthrough` |
| moment | `during`（关键一手即将成立） |
| character_goal | `solve` |
| viewer_relation | `look_at_target` |
| conflict_level | `low` |
| reward_signal | `nearly_winning` |

- **商业意图**：强调玩法属性，A/B 测"玩法导向"是否更吸引人
- **画面要点**：玩法焦点居中、角色作为引导而非主角、动线指向关键块

### 方案 C · 胜利爆发型（Reward Celebration）

| 字段 | 取值 |
|------|------|
| story_mode | `reward_celebration` |
| moment | `after`（一手成功之后） |
| character_goal | `victory` |
| viewer_relation | `multi_character` 或 `direct_eye_contact` |
| conflict_level | `none` |
| reward_signal | `loot_rich` |

- **商业意图**：强调留存 / 正反馈 / 转化
- **画面要点**：角色庆祝姿态、奖励喷发、画面更亮但保持 DNA 风格

> 🎯 三件套覆盖了**点击前 / 玩中 / 玩后**三个心理时刻，是商业化封面的最大公约数。

---

## 进阶方案池（按需扩展）

当三件套不够、或需要更细颗粒度 A/B 时，可从以下池中挑选：

### 方案 D · 发现型（Discovery）
- moment: `before` · character_goal: `discover` · viewer_relation: `back_to_viewer`
- **适用**：希望增加世界观感，封面不只是"角色 + Logo"

### 方案 E · 安全危机型（Safe Crisis）
- moment: `during` · character_goal: `face_crisis` · conflict_level: `low`
- **适用**：希望有"事件感"和参与感，但不想过度戏剧化

### 方案 F · 群像关系型（Multi-Character Bond）
- viewer_relation: `multi_character` · reward_signal: `world_interesting`
- **适用**：游戏有明确多角色阵容（如卡牌 / 收集养成）

---

## 自检清单（AI 输出方案前必过）

```text
□ 是否输出过 DNA 卡并取得用户确认？
□ Fidelity 是否明确标注（默认 85%-90%，超出必须用户特批）？
□ 5 个维度是否全部填写（不能写"更有故事感"这种模糊语言）？
□ 是否带 negative_style_constraints？
□ 方案之间的差异是否来自"叙事变量"，而不是来自"换风格"？
□ 是否说清每个方案的商业意图（点击 / 转化 / 留存）？
```

---

## 反模式

### 反模式 1：风格也跟着变
❌ 方案 A 是糖果 3D 邀请，方案 B 是赛博潮流邀请 → 退回到了风格分叉，违反 Skill 19794651。

### 反模式 2：故事维度只填一两个
❌ 只写 `story_mode: invitation`，其他 4 个维度留空 → AI 仍然会发散，方案差异不可控。

### 反模式 3：叙事过载
❌ 一张封面同时讲"邀请 + 解题 + 胜利" → 信息过载，CTA 不明，违反 Skill 「避免概念过载」铁律。

### 反模式 4：忘了商业意图
❌ 只输出 5 个故事维度，但不说每个方案要测什么、为谁服务 → 评审无法决策，沦为"AI 自嗨"。

---

## 【竖版海报 Adapter】竖版海报设计体系 v1.0（2026-05-29 新增）

> **设计理念**：竖版海报（海报图）的本质不是“横图的简单裁切”，而是通过**纵向主轴、上下分层、巨物尺度差、强排版系统、破框重叠**来构建高级商业感与叙事张力的独立体系。文字在此是一等公民，构图与文字排版必须在 prompt 中一体化设计。

### 1. 竖向排版系统：三层级黄金网格（The Vertical Information Grid）

任何海报图的 prompt 撰写，必须在脑内或思考契约中预留并规划以下三个层级，禁止将画面填满而无文字预留区：

| 区域 | 占比 | 承载功能 | 典型 Prompt 写入方式 |
|------|------|----------|----------------------|
| **顶部 (Top Zone)** | 15% - 20% | 品牌标识、杂志刊头、活动徽章、留白空气透视 | "Top 15% is clean sky/blank space reserved for brand logo" / "Bold editorial masthead spans across the top" |
| **中部 (Middle Zone)** | 50% - 60% | 英雄主体、视觉巨物、冲突、故事爆点 | "The middle zone features a giant..." / "Subject overlaps the background element" |
| **底部 (Bottom Zone)** | 20% - 30% | 电影级标题、Slogan、Credits落款、CTA、预约按钮、条形码/期号等 | "Bottom third contains a large cinematic title block 'XXX' in serif font, with tiny movie credits and release dates below" |

---

### 2. 六大经典竖版海报类别与视觉签名

根据海量顶尖游戏（THE FINALS、生化危机、重返未来1999、三角洲行动、彩虹六号、PlayStation、旺达与巨像）的实战案例，竖版海报归纳为以下 6 种标准范式：

#### A. 潮流编辑与运动品牌型 (Editorial & Brand Campaign)
*   **适用场景**：时尚电竞、年轻枪战、角色/皮肤宣发、赛季音乐。
*   **核心视觉签名**：
    *   纯色高饱和背景（红/黄/蓝/绿），无写实三维空间。
    *   超大几何文字背景墙（如 "THE FINALS" / "DELTA FORCE"），字母顶天立地。
    *   人物（像抠图一样）重叠在背景巨字前方，武器或身体局部“破框”超出。
    *   版面边缘带有印刷标记（registration marks）、校色条（color bars）或竖排侧边英文。
*   **Prompt 示例片段**：
    `A 9:16 vertical poster in bold brand campaign style. High-saturation crimson red background with a massive, stylized white block text "THE FINALS" as a massive graphic backdrop wall. In the foreground, a high-detail samurai character in dark red lacquer armor stands in a dynamic katana-slashing pose, overlapping and breaking out of the white letters behind him. Soft atmospheric smoke trails of red fog drift across. Clean logo safe areas. Vertical registration marks and color strips on the far right edge of the poster.`

#### B. 电影级赛事主视觉型 (Cinematic Esports & Monumental Event)
*   **适用场景**：大型战队邀请赛、周年庆盛典、版本主视觉。
*   **核心视觉签名**：
    *   绝对的纵向中心轴。
    *   中部/中上部是巨大的纪念碑式图腾、奖杯、或代表赛事届数的巨型发光立体数字。
    *   强烈而戏剧性的单一顶部顶光/探照灯（spotlight），形成仪式感。
    *   人物作“多层小队层叠”：最下方是极小的士兵剪影背影，向中心神殿/巨型数字进发；两侧是中景战友，背景隐约浮现巨型领袖头像。
*   **Prompt 示例片段**：
    `A 9:16 vertical cinematic event poster with a powerful vertical center axis. The center is dominated by a monumental, giant concrete number "6" with a tactical pistol silhouette carved inside, lit from directly above by a single powerful white searchlight beaming down from a stormy sky. At the bottom, a squad of five elite modern soldiers in tactical gear is shown from behind as tiny silhouettes, walking forward into the light. The background is a layered dark metallic stadium with distant flags. Low-saturation cool blue and slate-gray color palette, atmospheric fog and sparks.`

#### C. 经典双人背靠背/多人层叠叙事型 (Back-to-Back & Tiered Character Collage)
*   **适用场景**：剧情章节、双主角游戏、硬核写实、重度叙事。
*   **核心视觉签名**：
    *   **双人背靠背 (Back-to-Back)**：一男一女或双主角，一人面朝左侧看，另一人面朝右侧看。两人背部贴合。使用“强分屏/强光影对比”（如左侧冷光、右侧暖光；或一侧是黑暗，一侧是火光）。背景是一条纵向视觉分界线（火车、大厅拱门、光柱）。
    *   **多角色对角线叠层 (Diagonal Tiers)**：最上方是最大比例的男主角侧脸或俯视（ Leon 比例约35%），眼神深邃；下方斜向叠层缩小放置次要角色（女一、女二、反派），最底部逐渐隐入写实场景。
    *   **双重曝光/叠层剪影 (Silhouette Overlay)**：用巨大主角的半身侧脸剪影（Ada Wong）作为视觉容器，在剪影内叠透村庄、废墟等场景的二次曝光。
*   **Prompt 示例片段**：
    `A 9:16 vertical cinematic narrative poster. Two professional special agents, a male and a female, stand back-to-back in the center. The female agent on the left is shown in profile facing left, lit by cool blue moonlight. The male agent on the right is shown in profile facing right, lit by warm orange firelight from a burning train engine behind them. Deep heavy shadows split them. In the bottom third, a distressed, grunge title block reads "RESIDENT EVIL". Moody, high-contrast chiaroscuro lighting, gritty film grain texture.`

#### D. 复古叙事电影海报型 (Retro Illustrated Movie Poster)
*   **适用场景**：剧情向、解谜、有年代感的活动。
*   **核心视觉签名**：
    *   手绘插画风、粗粝版画感，带有宣纸或脏纸磨损纹理（vintage worn paper texture）。
    *   具有时代感和手写艺术感的标题直接设计在画面底部。
    *   采用强烈的“隐喻视觉符号”而非大人物：公路通向月光下的孤零旧宅、旋转的胶片环绕着奔跑的女孩、星空黑胶唱片轨道。
*   **Prompt 示例片段**：
    `A 9:16 vertical retro illustrated movie poster. The background is a circular framing device of stylized dark tree branches under a cloudy night sky with a full moon. In the center, a lonely retro car on a desolate highway is driving away towards a dark Victorian mansion on a hill with a single red glowing window. Hand-drawn mid-century illustration style, thick ink lines, grunge watercolor wash, sepia and navy blue color tones. At the bottom, stylized vintage title typography reads "The Haunted Highway". Entire poster has a worn folded paper crease texture.`

#### E. 巨物图腾与尺度差史诗型 (Colossal Giant & Scale Contrast)
*   **适用场景**：史诗奇幻、巨兽对决、冒险探索。
*   **核心视觉签名**：
    *   极端的画面“尺度差”。
    *   最底部是微小的骑马主角或行军小队（比例 ≤5%）。
    *   中景和背景是顶天立地的巨像、巨兽或巨型废墟，轮廓巨大而沉重。
    *   大面积的逆光（backlighting）、尘埃粒子、浓重的雾气与空气透视，突出空间的无限庞大。
*   **Prompt 示例片段**：
    `A 9:16 vertical epic fantasy poster. In the bottom-center foreground, a tiny, lone horseman is shown from behind, riding a galloping black horse across a grassy valley, occupying only 5% of the frame. In the massive, misty background, a colossal ancient stone colossus with glowing eyes towers between two towering cliffs, its giant silhouette partially obscured by thick golden sunlit fog. Low angle, looking up. Grand scale, atmospheric dust motes catching the rays of sunset. Minimalist elegant title "SHADOW OF COLOSSUS" in the bottom-center.`

#### F. 强转化广告卡片型 (Conversion-Oriented Ad Card)
*   **适用场景**：买量素材、应用商店详情页。
*   **核心视觉签名**：
    *   精美的扁平圆角卡片 UI，白色底板与有色信息面板。
    *   游戏画面被框在卡片内部，但最显眼的角色“身体或手”不规则地伸出框外，造成强烈的 3D 破框动感。
    *   底部包含小正方形 App Icon、醒目的圆角“下载”或“预约”高光按钮、精炼的卖点文字。
*   **Prompt 示例片段**：
    `A 9:16 high-conversion mobile game ad poster. The composition features a rounded-corner clean white card floating over a dark background. Inside the card is a dramatic screenshot of a multiplayer horror dungeon game. A key monster character in a crimson red hood stands prominently in the right foreground, her sharp clawed hand breaking out of the card frame in a 3D pop-out effect. At the bottom of the poster, there is a square game app icon, clean bold text "Play with Friends", and a highly visible white rounded button with the text "DOWNLOAD". Professional mobile ad campaign layout.`

---

### 3. 竖向“破框重叠”艺术与文字融合 (The Art of Layering and Breaking Frame)

高水准竖版海报的灵魂在于**图层深度 (Z-depth)**。绝对禁止“图是图，字是字”的简单贴字。AI 在编写 prompt 时，必须明确声明图层关系：

```text
【Z-depth 1 (最前)】：破框局部（如刀刃、向前伸的手、飞溅的泥土/火花、 registration marks 标记）
【Z-depth 2 (次前)】：标题/刊头字（Title Text / Masthead）
【Z-depth 3 (中部)】：主英雄/巨像（Hero Character / Subject）- 遮挡 Z-depth 2 的部分文字
【Z-depth 4 (背景)】：巨大数字、地标背景、天空、或者大面积色块（Background / Silhouette）
```

通过这种层级声明，AI 能引导模型生成极具设计感、字图融为一体的高级版面。

---

### 4. 竖向 Format Adapter 思考契约与 Prompt 模版

写竖版海报 prompt 时，第一层思考契约更新如下：

```json
{
  "format_adapter": "vertical_poster",
  "poster_type": "magazine_cover | cinematic_event | back_to_back_narrative | retro_movie_poster | colossal_scale | mobile_ad_card | brand_campaign",
  "aspect_ratio": "9:16 | 2:3 | 3:4 | 4:5",
  "vertical_safe_crop": "9:16 master; critical title / subject / gameplay proof inside centered 70% height safe zone; top/bottom 15% are expendable background only",
  "information_density": "low | medium | high",
  "top_system": "<masthead / brand_logo / clean_sky>",
  "main_subject_strategy": "<layered_squad / back_to_back / giant_silhouette / diagonal_collage / cropped_closeup>",
  "bottom_system": "<cinematic_credits / CTA_download_button / giant_brand_title / vintage_title>",
  "typography_role": "structural_background | overlapping_hero | decorative_labels | clean_slogan",
  "dna_lock": "<承袭 Core Layer>",
  "gameplay_lock": "<承袭 Core Layer>"
}
```

#### 自然语言海报 Prompt 模版（终端产物 5 段式）

```text
段落 1 (容器与类型声明): A <aspect_ratio> vertical game poster in <poster_type> style for <游戏类型>, featuring a strong top-middle-bottom hierarchy.（海报图推荐先出 9:16 母版）
段落 1.5 (Vertical Safe-Crop Layout): 9:16 母版兼容 2:3 / 3:4 / 4:5。标题、主体、脸、手、玩法证据、关键道具全部放在中央 70% 高度安全区；顶部 15% 和底部 15% 只放 sky / wall / atmosphere / blur / particles / floor 等可裁切背景。
段落 2 (主体角色、叠层与动作): 详细描述中部 (Middle Zone) 主体角色、姿态、Z-depth 破框与重叠关系。
段落 3 (场景、地标与透视): 描述场景。如果是巨物则说明尺度差，如果是联名则写地标。
段落 4 (光影、色彩与质感): 配合海报类型（如 cinematic / duotone / vintage print / dark chiaroscuro）描述。
段落 5 (排版、标题、底部系统与负面词): 声明文字位置（如 "Top area features...", "Bottom third contains..."）与 `--no` 负面风格锁。
```

---

### Adapter 3：长条 Banner（v4.16 · 出海素材只裁宽度规范）

> 应用场景：商店首屏 banner、活动入口图、游戏内嵌横幅、官网通栏、广告条。经复盘确认：旧版 3:1 单母版 / 双向裁切方案会压缩高度、削弱商业画面表现，已废弃。

**母版选择标准**：Banner 统一采用「只裁宽度，不裁高度」三档母版。目标图只从母版左右裁切；上下只保留呼吸边距，不作为裁切区。

| Banner 档位 | 适用比例 | 母版 | 推荐尺寸 | 安全区 | 裁切方式 |
|---|---:|---|---|---|---|
| 标准长条 Banner | 2.6:1 ~ 3.5:1 | 3.5:1 | 1792×512 | 中央 74% 宽 × 90% 高 | 只裁左右；左右各 13% 可裁，顶部/底部各 5% 呼吸边距 |
| 超长 Banner | 4.0:1 ~ 5.2:1 | 5.2:1 | 2080×400 | 中央 76% 宽 × 90% 高 | 只裁左右；左右各 12% 可裁，顶部/底部各 5% 呼吸边距 |
| 极窄广告条 | 6.0:1 ~ 8.0:1 | 8:1 | 2560×320 / 2400×300 | 中央 74% 宽 × 90% 高 | 只裁左右；左右各 13% 可裁，顶部/底部各 5% 呼吸边距 |

写长条 banner prompt 时，第一层思考契约更新如下：

```json
{
  "format_adapter": "standard_long_banner | ultra_long_banner | extreme_strip_ad",
  "container": "commercial horizontal game banner",
  "aspect_ratio": "3.5:1 | 3:1 | 5.2:1 | 5:1 | 4:1 | 8:1 | 6:1",
  "banner_safe_crop": "width-only crop; never crop height; keep critical title / subject / gameplay proof inside tier-specific centered safe rectangle; left/right are expendable background only; top/bottom are breathing margins only",
  "banner_template_lock": "choose one modular commercial banner template first: left-title-right-hero | left-hero-right-title | center-title-two-side-heroes | center-hero-two-side-info | reward-promo | event-tournament | diagonal-split | oversized-object | target-lock | extreme-strip",
  "banner_composition_lock": "commercial banner layout, not cropped gameplay screenshot: dominant title mass + oversized hero/key object + graphic background + 1-3 gameplay/reward/event symbols; every horizontal third of the safe area has a role; no empty flat slab",
  "reading_rhythm": "left-to-right horizontal flow; title block and hero subject visually connected by motion line, target line, light beam, perspective road, particles, object overlap, or shared lighting",
  "dna_lock": "<承袭 Core Layer>",
  "gameplay_lock": "<承袭 Core Layer>"
}
```

#### 自然语言 Banner Prompt 模版（终端产物 6 段式）

```text
段落 1 (容器声明): A <aspect_ratio> commercial horizontal game banner for <游戏类型> called "<game_name>".（先按目标比例选择 3.5:1 / 5.2:1 / 8:1 对应母版）
段落 1.5 (Banner Composition Lock): 不能像游戏截图横裁；必须是商业横幅版式：大标题模块 + 大主体/关键物件 + 简化图形背景 + 1~3 个玩法符号；安全区内部必须有足够信息密度，不能出现大面积空色块。
段落 1.6 (Banner Safe-Crop Layout): 只裁宽度，不裁高度。按档位写清安全区：3.5:1 = 74%×90%；5.2:1 = 76%×90%；8:1 = 74%×90%。左右为可裁背景；上下只是呼吸边距，不放可裁关键内容。
段落 2 (Title Lock): 单层清晰 exact game title；位置可居中/中上/侧中/合理边缘，但不能机械贴边或角落小贴片；禁止重复标题层和背景巨字层。
段落 3 (主体与动作 / 玩法物件 / 情境线索): 按 subject_type 写 Subject Lock / Game Asset Lock / Scenario Puzzle Lock；主体要像商业主视觉，不能缩成截图里的小目标。
段落 4 (场景、节奏、连接): 标题模块和主体必须用运动线、目标线、光束、透视路、粒子、物体重叠或共享光影连接成一个整体。
段落 5 (光影与色彩与质感): 配合 banner 风格（promotional / cinematic / high-saturation / minimal product 等）描述。
段落 6 (负面词): 禁止 UI / 按钮 / 截图框 / 随机文字 / 大面积空色块 / 关键元素触边 / 截断主体或标题。
```

#### Banner 商业横幅模板库（v4.17 · 必先选模板再写 prompt）

| 模板 | 结构 | 适用 |
|---|---|---|
| 1. 左文右主体 | 左 35% 大标题 / 中右 55% 大主体 / 边缘延展 | 射击、跑酷、动作、有明确主角/怪物/载具 |
| 2. 左主体右文 | 左 45% 大主体 / 右 40% 标题或卖点 / 边缘延展 | 赛车、摩托、体育、冲刺动作 |
| 3. 中央大标题 + 两侧主体 | 左角色/道具 / 中央巨大标题 / 右角色/奖励 | 活动、节日、多角色、IP、联动 |
| 4. 中央主体 + 两侧信息 | 左标题 / 中央最大主体 / 右奖励或玩法符号 | 奖励型、角色+道具、休闲活动 |
| 5. 大数字/奖励促销型 | 角色/道具 + 巨大数字/奖励 + CTA-like 图形 | bonus、rebate、抽奖、福利广告 |
| 6. 赛事/活动信息条 | 小 logo/信息 + 超大标题 + 日期/奖池/角色 | 竞技、赛事、MOBA、卡牌、联赛 |
| 7. 斜切分屏/多角色拼接 | 3~4 个斜切面板 + 统一标题 | 多角色、多阵营、RPG、派对、卡牌 |
| 8. 大物件横穿型 | 一个巨大道具/载具横跨中间 + 标题贴合 | 赛车、摩托、武器、飞机、机甲、产品型道具 |
| 9. 目标锁定/瞄准型 | 大标题 + 巨大目标主体 + 准星/雷达/目标线 | 射击、狙击、找目标、塔防打击、追捕 |
| 10. 极窄广告条极简型 | 一个标题 + 一个主体 + 一个爆点 + 极简背景 | 6:1~8:1 极窄通栏广告 |

**Banner 必写 6 个锁**：

```text
[Banner Safe-Crop Lock]
只裁宽度，不裁高度；按 3.5:1 / 5.2:1 / 8:1 选择母版和安全区。

[Modular Layout Lock]
使用明确模块：标题模块 / 主体模块 / 辅助符号模块；每个横向三分区都必须有职责。

[Title Mass Lock]
标题是一层，但必须是主视觉块，不是角落 logo；通常占 25%~55% 宽度或 40%~80% 高度。

[Hero Scale Lock]
主体要商业化放大，可侧边切入、破框、局部裁切，但核心识别不能被破坏。

[Graphic Background Lock]
禁止空色块；背景必须有渐变、光效、斜切、纹理、粒子、剪影或图形结构。

[Module Connection Lock]
标题模块和主体模块必须用运动线、目标线、光束、透视路、粒子、物体重叠或共享光影连接。
```

**按类型优先选模板**：射击/狙击优先模板 9；赛车/摩托优先模板 2/8；跑酷优先模板 1/4；活动/节日优先模板 3/5；竞技/赛事优先模板 6/7；极窄广告位优先模板 10。

---

## 与现有 Memory / Skills / 沉淀的关系

> ⚠️ **2026-05-29 v4 架构变更**：本文档现在是**游戏商业视觉故事性分叉方法论的「单一真相源」**。Memory 19794651 / 65488524 均退化为"路由指针 + 术语边界"，不再展开规则细节。任何规则变更只在本文档发生。

### 单一真相源原则

| 文件 / Memory | 角色 | 内容深度 |
|---------------|------|---------|
| **本文档**（narrative-driven-cover-variants.md） | ⭐ **单一真相源** | Core Layer / 横向封面 Adapter / DNA 锁 / Fidelity 控制 / 4 杠杆矩阵 / 双层 prompt SOP / 反向风格锁 / 全部细节 |
| Memory 19794651（游戏商业视觉方法论路由） | 路由指针 | 做封面图/海报图前必读本文档；规则细节只在文档维护 |
| Memory 14281778（封面风格扩展） | 风格池来源 | 视觉风格灵感库，本文档在风格选定**之后**接力 |
| Memory 57615156（角色资产真实剥离） | **强制依赖** | 所有故事变量都在"已剥离的真实角色资产"上做姿态/动作迁移，不改身份 |
| Memory 72072029（角色身份锁 + 姿态重构） | 实现路径 | 故事维度变化时角色仍保持身份一致，仅做姿态/表情/视线变化 |
| Memory 65488524（封面图 / 海报图术语边界） | 容器约束 | 封面图=横向游戏列表封面（16:9/5:3/3:2）；海报图=竖版图（9:16/3:4/4:5/2:3） |
| `biz-wiki/game/multi-style-ab-testing.md` | 上游接力 | 多风格 A/B 跑出胜出风格后，用本文档做深度商业化分叉 |

### 为什么采用单一真相源

历史问题：Memory 和文档双源记录同一规则，容易漂移、不一致、跨电脑同步困难。
新分工：
- ✅ Memory = **抽象红线 + 路由指针**（跨项目可携带，但不展开规则）
- ✅ 文档 = **完整 SOP**（git 可追踪、可 review、可跨电脑同步）
- ✅ 规则变更只发生在文档，Memory 永远只是"去那里读"

---

## 开放问题 / 待验证

- 三件套（邀请 / 解题 / 胜利）的实际 CTR 表现，需要在真实项目（如 `Come Match`）上线后回填
- `safe excitement` 的"安全阈值"是否需要做 conflict_level 的更细分级？
- discovery / multi_character 这类进阶方案，在休闲品类是否会拉低 CTR？需要数据验证
- 故事维度组合是否存在"已知反组合"（如 `back_to_viewer + try_it` 是否天然冲突）？

---

## 出处与迭代

- **首次确立**：2026-05-28，与 AI 协作的封面方法论讨论中提出并落地为方法论
- **v2 升级**：2026-05-28（同日晚），实战《Come Match》5 方案后发现"伪分叉"问题，新增 4 杠杆差异化矩阵 / Fidelity 默认档约束 / 多方案 SOP；同时确立"本文档为单一真相源"，Memory 19794651 退化为路由指针
- **v3 升级**：2026-05-28（同日 17:30），v2 修正后再战《Come Match》，5 方案视觉差异已拉开但发现方案 B2「俯视棋盘」意外把游戏类目从三消暗示成桌游；新增「玩法 Fidelity」第三维 Fidelity 体系 / DNA 卡 `gameplay_lock` 字段 / 高危杠杆值清单 / Step 8 自检 Checklist；SOP 从 7 步升级到 8 步
- **v4 架构升级**：2026-05-29，将方法论拆为 **Core Layer（跨比例复用）+ Format Adapter（随比例变化）**；固化术语："封面图"=横向游戏列表封面（16:9/5:3/3:2），"海报图"=竖版图（9:16/3:4/4:5/2:3）；后续喂竖图时只新增 Vertical Poster Adapter，不推翻 Core Layer
- **v4.1 准入门升级**：2026-05-29，新增 Step 0 素材准入清单（游戏名字 ✅ / 广告语 ⬜ / ICON ✅ / 截图 ✅）；明确 AI 不允许靠图像识别猜游戏名（实证背景：本日两轮海报学习中 AI 把训练先验里的 GTA / Resident Evil / Forza 等知名游戏当成识别结果汇报）；SOP 从 8 步升级到 9 步（含 Step 0），同步更新到 `game-poster-learning-sop.md` 和 HTML 控制台
- **v4.2 全局策略重定位**：2026-05-29，把「4 杠杆差异化矩阵」从横向封面 Adapter 章节提升为 **Core Layer 全局策略**，明确对横向 / 竖版都生效；4 杠杆定义表拆为「抽象定义（永久）/ 实例取值池（每题材重写）」两列，避免后人把休闲皇室拼图的具体值当通用规则；HTML 控制台中把「4 杠杆速查」从横向 section 抽出，做成紫色 ★ 全局 section（包含 A 抽象定义 / B 强制差异化规则 / C 高危值通用模式 / D 自检模板）；横向 section 内部保留的速查表改名为「构图差异化矩阵 · 当前题材实例」，加 ⚠️ 实例参数提醒
- **v4.4 默认行为约束（2026-05-29）**：基于 Tricky Puzzle 实证 + 用户明确要求"不需提醒才用"，新增「AI 默认行为约束」4 条规则：(a) 默认出多题材方案（≥3），不需用户提醒；(b) 每条 prompt 必须显式包含 L1 camera / L2 lighting / L3 setting / L4 visual weight；(c) 默认禁止出现游戏按钮（每条 prompt 必带购买按钮/下载按钮的负面锁）；(d) 主动应用 4 杠杆差异化，不等待用户提醒。SOP 从 9 步升级为 10 步（含 Step 9 AI 默认行为检查）。违反处理：未出多方案 / prompt 缺 L1-L4 / 无按钮负面锁 / 未先输出差异化矩阵 → 视为不合规需返工。
- **v4.5 角色资产剥离硬约束（2026-05-29 · Grill Skewer Pop 实证驱动）**：用户实测发现 AI 出 prompt 时用通用 chibi 描述自由重绘人物，没有从 Step 0 素材里剥离真实角色 → 与游戏内角色货不对板，违反 Memory 57615156 / 72072029。将"角色资产剥离 + 姿态重构"从「继承列表项」升级为**默认行为约束第 5 条**；SOP 从 9 步升级到 10 步（新增 Step 10 角色资产剥离自检）；Prompt 模板新增 Subject Lock + Pose Reconstruction 两个必填字段；HTML 控制台新增红色规则 5 卡片。违反处理：prompt 用 generic chibi 描述自由人设 → 视为 SOP 不合规需返工。
- **v4.6 工具通道硬约束（2026-05-29 · Grill Skewer Pop 二次实证打脸）**：用户实测 v4.5 的方案 B 出图后**第二次反馈**——即使 prompt 写了 Subject Lock 段，GPT Image 2 出来的人物依然是凭训练先验自由重绘的全新人物。**真因**：text-to-image 模型本质上不"看"参考图，只读文字 prompt；英文文字描述信息密度比视觉输入低 100×，永远做不到角色身份精确还原。**v4.5 致命漏洞**：把"prompt 写 Subject Lock 段"当成了"角色资产剥离已落地"——这只是 AI 自我安慰，对模型生成无视觉约束力。**v4.6 修正**：规则 5 升级到工具层硬约束——禁止只交付纯文字 prompt，必须同时给出 image-to-image / Midjourney --cref / ComfyUI IP-Adapter 三选一可执行路径；Step 10 自检新增"是否走了视觉输入通道？"硬检查项；违反处理新增对应一行。**架构教训**：在 prompt 文字层修角色一致性 bug = 修错了层级，必须升到工具/工作流层。
- **v4.7 AI 内部闭环（2026-05-29 · Grill Skewer Pop 三次反馈打脸）**：v4.6 规则上线当天，用户**第三次反馈**——"你给我三条工具路径让我自己选 + 自己上传 + 自己切平台 = 你在新增工序、改我流程"。**真因**：v4.6 把"工具链整合"工作甩给用户，违反"AI 闭环原则"——用户的真实诉求永远是「输入端不变 + 输出端拿到正确结果」。**v4.6 致命漏洞**：误解了"工具层硬约束"的执行主体——不是让用户去操作工具，而是让 AI 自己调用工具。**v4.7 修正**：规则 5 重写为"AI 自动跑 3000 MCP 工具链"——AI 内部用 `3000_comfyui_divide` 剥离主角图层 + `3000_generate_image` (gpt-image-2, image=PNGs, input_fidelity=high) 跑图生图，全程异步轮询自己处理；用户输入端依然只给 icon + 截图 + 游戏名（v4 Step 0 不变），输出端依然只看到最终封面图，**用户对工具链零感知**。SOP 从 10 步升级到 11 步（新增 Step 11 = AI 自动执行剥离图层 + 图生图闭环）；违反处理新增"AI 让用户切平台 / 当搬运工"一行。**架构教训**：v4.6 在工具层立约束没错，错在搞错执行主体；工具链整合是 AI 本职工作，必须 AI 闭环。
- **v4.3 Reference-only 红线**：2026-05-29，基于 `Tricky Puzzle` 首轮 GPT Image 生成失败（封面图中出现 app icon，质量显著下降），新增「输入素材 ≠ 输出画面元素」硬约束：Step 0 的 ICON / 游戏截图只可作为 reference-only inputs，默认禁止出现在封面 / 海报画面内；每条 prompt 必带 app icon / screenshot UI / bottom navigation / loading bar / level menu 的负面锁；只有用户明确要求「强转化买量广告卡」时才允许展示 app icon / download button
- **v4.9 subject_type 路由（2026-06-01 · Grill Skewer Pop 实证驱动）**：发现原 archetype 池几乎全是「人物本位」，对人物不占主体的玩法型游戏会退化成语言描述兜底。新增 `subject_type = character | gameplay_object | hybrid | scenario_puzzle` 路由：无人物/物件主导游戏走 `Game Asset Lock`，hybrid 同屏保留人物情绪钩子 + 玩法机制，scenario_puzzle 强调荒诞情境 + 视觉线索。新增 5 个 gameplay_object archetype（product_hero / abundance_overflow / isometric_diorama / collection_grid / gameplay_burst），并明确 Grill Skewer Pop 必须体现三消匹配而不只是烤串广告。
- **v4.10 Prompt Preflight 加固（2026-06-01 · Grill Skewer Pop / Brain Trick / Girl Rescue 复盘）**：用户连续指出 AI 漏掉「游戏名必须渲染」和「默认 A/B/C 多剧本」两项全局约定。新增 Step 0.5：输出 prompt 前必须声明 subject_type / 玩法核心 / 封面必须表达 / A-B-C 输出声明；每条 prompt 必须包含 `[Title Lock — mandatory game title]`；Negative 禁止裸写 `no text` / `no logo`，必须写 `No extra text except the exact game title "<game>"`；默认三套差异化 prompt，除非用户明确只要一版。
- **v4.14 Integrated Typography System（2026-06-02 · 已废弃）**：曾尝试用「背景巨字层 + 可读主标题层」解决贴边 logo 问题，但实测会把标题引向错误的双层效果，不再作为默认方法论。
- **v4.15 Flexible Single Title（2026-06-03 · Morph Runner 复盘修正）**：标题只保留一层清晰 exact game title；标题位置要多样化，可居中/中上/侧中/边缘，但禁止机械贴边和角落小贴片；标题通过色彩、光影、阴影、材质、透视或运动方向融入画面，而不是重复成背景巨字层。Negative 明确禁止 duplicate title layers / giant background title text。
- **v4.16 出海游戏素材裁切规范（2026-06-04 · Banner 裁切复盘定版）**：将 16:9 横版、9:16 竖版与 Banner 裁切统一为出海素材裁切规范。横版沿用 16:9 母版中央 75% 宽度安全区；竖版沿用 9:16 母版中央 70% 高度安全区；Banner 废弃 3:1 单母版和双向裁切，改为只裁宽度三档母版：3.5:1 标准长条（74%×90%）、5.2:1 超长（76%×90%）、8:1 极窄广告条（74%×90%），上下只做呼吸边距，不裁高度。
- **v4.17 Banner 商业横幅模板库（2026-06-04 · 多轮 Banner 案例学习）**：确认 Banner 不是“宽图/截图横裁”，而是商业横幅版式。新增 10 类模板：左文右主体、左主体右文、中央大标题两侧主体、中央主体两侧信息、奖励促销、赛事信息条、斜切分屏、大物件横穿、目标锁定、极窄广告条。Banner prompt 必须先选模板，再写 prompt；新增 Safe-Crop / Modular Layout / Title Mass / Hero Scale / Graphic Background / Module Connection 六个锁。
- **状态**：`partially-validated` — Core Layer 中的 Step 8 玩法 Fidelity 自检 + 高危杠杆值清单中的「俯视棋盘 / 木棋盘桌面 / 网格阵列」三条**已经过单点实战验证**（修正后用户实测效果显著提升）；横向封面 Adapter 已部分实证，竖版海报 Adapter 待学习；完整 `validated` 仍需多游戏 × 多轮 A/B CTR 数据
- **下次复盘节点**：第一个采用本方法论的项目（候选：`Come Match`）上线 A/B 后，回填三件套实际 CTR 表现
- **可能的迭代方向**：
  1. 把 5 个维度 → JSON Schema 化，配 validator
  2. 把"默认三件套" → 做成 `.codebuddy/skills/` 下的可调用 skill
  3. 沉淀失败案例（哪些故事维度组合在哪类游戏不 work）
