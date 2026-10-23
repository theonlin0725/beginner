# 游戏商业视觉 SOP · v5.0 工作流总纲

> **状态**：v5.0 · 2026-06-05 起为新主源
> **配套控制台**：`wiki/sources/game-poster-learning-sop/cover.html`（学习/查阅）
> **配套真出图工作站**：`tools/game-cover-sop/`（暂未同步到 v5，待阶段 2）
> **历史主源**：`biz-wiki/game/narrative-driven-cover-variants.md` + `game-poster-learning-sop.md`（v4.x 系列，保留作为演进史，不再优先采纳）

---

## 0. v5 相对 v4 的变化（为什么要写这份新主源）

**v4.x 历史包袱**：
- "Core Layer + Format Adapter" 把横版作为主、竖版/Banner 作为附属，导致横版/竖版/Banner 各自重复 SOP（10 步流程、9 段模板、硬检查表都被各自实例化一遍）
- 「构图差异化矩阵 · 当前题材实例」按"题材专属"分类，预设题材是高危分类轴，但实战发现"翻车"和人群/渠道/地区/subject_type 都强相关
- "AI 默认行为规则"作为流程步骤插在前面，本质是输出前自检，混淆了"流程动作"和"形式校验"
- "P6 执行模板"是 4×5 空白填表，纯演示无价值
- Banner 6 锁混合了 prompt 形式约束和构图设计原则，被打包成"输出前自检"用错了归位
- subject_type 路由埋在硬检查表附录里，位置和重要性不匹配
- C 表（负面禁止）/ D 表（题材实例化）没有衔接关系，知识沉淀机制空缺

**v5 改造方向**：
1. **职责单一**：每张表只管一类事，不混
2. **跨格式参数化**：横/竖/Banner 共用同一套 ① 流程 + ② 主角分型 + ③ 9 段模板 + ④ 8 项硬检查；只在差异点参数化
3. **设计原则归位**：Banner 6 锁等设计原则归到构图层 / 表现层底线；P 表回归纯 prompt 形式校验
4. **建立沉淀机制**：D 表「项目翻车账本」7 列上下文 + C↔D 晋升路径

---

## 1. 工作流核心结构（5 个一级模块）

```
1. 必备素材    — 准入门 4 项：游戏名 / 类型 / ICON / 截图
2. 全局策略    — 4 杠杆差异化矩阵（A 定义 / B 数学 / C 通用负面 / D 项目翻车账本）
3. 构图的方法  — 左右两栏：构图层 C1-C4 + Format Adapter ｜ 表现因素层 + 叙事变量
4. 生产流程    — ① 10 步流程 → ② 主角分型 → ③ 9 段模板 → ④ 8 项硬检查
5. 输出速查表  — 横/竖/Banner 各自版式骨架速查
```

---

## 2. ① 10 步流程（跨格式 · 三格式通用）

10 步是思考动作 / 时间顺序，跨格式通用。差异只在「画幅取值」「线性化分段数」两处参数化。

| # | 步骤 | 共性动作 | 横 / 竖 / Banner 差异 |
|---|------|---------|----------------------|
| 1 | 读取 DNA 与 gameplay_lock | 锁游戏原生风格、角色、玩法，不让画面跑偏 | 通用 |
| 2 | 选择画幅 | 容器决定后续构图，先选母版再考虑裁切 | 横版 16:9 / 5:3 / 4:3 / 3:2<br>竖版 9:16 / 2:3 / 3:4 / 4:5<br>Banner 3.5:1 / 5.2:1 / 8:1（只裁宽不裁高）|
| 3 | 填写构图层 4 维度 | C1 视角 / C2 版式 / C3 面积 / C4 动线；至少错开 3 个维度 | 通用（取值池受画幅约束）|
| 4 | 填写表现层 | 色彩 / 字体 / 光影 / 质感 + 商业信息密度 | 通用 |
| 5 | 绑定故事变量 | 时间点 / 角色任务 / 观众关系 / 冲突 / 结果导向 | 通用 |
| 6 | Fidelity 自检（≥85%）| 风格 / 角色 / 玩法 fidelity ≥85%；扫高危杠杆值清单 | 通用 |
| 7 | 线性化 Prompt | 按 ③ 9 段模板组织文本 | 横/竖 用 5 段；Banner 用全 9 段 |
| 8 | 追加负面锁 | 负面风格锁 + 负面玩法锁 | 通用 |
| 9 | 差异化矩阵自检 | 两列至少错开 3 行；否则伪分叉返工 | 通用 |
| 10 | 生成后复盘 | 实证翻车 → 登记 D 表 7 列上下文 | 通用 |

---

## 3. ② 主角分型（写 prompt 前先判 C 位）

### 决策流程

```
(0) 自动判定启发式
    gameName 正则
      ├─ brain/trick/iq/test/riddle  → scenario_puzzle
      ├─ rescue/save/pull/draw       → hybrid
      └─ match/pop/merge/blast/crush → gameplay_object
    资产证据
      ├─ character 资产 ≥ 1 张  → character
      └─ character = 0 + 物件矩阵 → gameplay_object
    fallback
      └─ character（最大兼容性）

(1) 锁定 archetype 池
    character        → 11 个 character archetype
    gameplay_object  → 5 个 gameplay_object archetype
    hybrid           → character + gameplay_object 池子合并
    scenario_puzzle  → 3 个 scenario_puzzle archetype

(2) 决定 9 段模板段落 3「主体段」标签
    character        → [Subject Lock]
    gameplay_object  → [Game Asset Lock]
    hybrid           → [Subject Lock] + [Game Asset Lock]（标题锁两端可见）
    scenario_puzzle  → [Scenario Puzzle Lock]

(3) 决定 L4 占比取值范围
    character        → hero dominant 60%+
    gameplay_object  → gameplay_object 60%+，character ≤ 25% 或缺席
    hybrid           → 50/50 共存
    scenario_puzzle  → scene 60%+ + 线索物分散 5-15%

(4) 决定 Title 段位置策略
    character        → 上中或侧面（主角占 C 位）
    gameplay_object  → 叠在玩法物件上方/下方
    hybrid           → 两侧（不挡任何一边主体）
    scenario_puzzle  → 贴顶或贴底（中央留给找谜题）
```

### 核心价值
**避免"所有游戏都按角色海报套模板"**——subject_type 是 prompt 写作前的分型分流闸，错一步后面全错。

### 扩展规则
- 新增 subject_type 类型 → 必须同步：archetype 池 + 主体段 Lock 标签 + L4 占比 + Title 位置策略
- 不得在自动判定走完之前直接套 character（会出"无关角色站中间"翻车）

---

## 4. ③ 9 段 prompt 输出模板（跨格式）

### 段落 DNA 5 字段
每个段落都有：段号 / 名称 / 职责 / 内容 / 三格式差异（+隐含的翻车证据，溯源到 D 表）

### 9 段定义

| 段号 | 名称 | 内容（prompt 文本结构）| 横/竖/Banner 差异 |
|-----|------|-----|-----|
| 1 | 容器声明 | `A <ratio> commercial <orientation> game <type> for <genre> called "<game_name>"` | ratio 按 Step 2 取值；orientation: horizontal cover / vertical poster / horizontal banner |
| 1.5 | Composition Lock | 商业横幅版式：标题模块 + 大主体 + 图形背景 + 1-3 玩法符号 | **仅 Banner**；横版/竖版略过 |
| 1.6 | Safe-Crop | 主体安全区 | 横:16:9 中央75%宽 / 竖:9:16 中央70%高 / Banner:只裁宽不裁高三档母版 |
| 2 | Title Lock | 单层清晰 exact title；位置可居中/中上/侧中/边缘 | 通用（按 P1/P2 硬检查规范）|
| 3 | 主体/玩法 | 按 ② 主角分型写对应 Lock 标签 | 通用，由 ② 决定 |
| 4 | 连接与节奏 | 标题和主体用运动线/光束/透视路/粒子/物体重叠连接 | 通用 |
| 5 | 光影色彩 | 按表现因素层（色彩/光影/质感）写主调和氛围 | 通用 |
| 6 | 负面词 | 禁止 UI/按钮/截图框/空色块/触边/截断/duplicate title layers/giant background title | 通用 |

### 扩充规则（应/不该新增段落）

**✅ 应新增段落**：
- 新型翻车反复出现，现有 8 段救不了（如发现 AI 出图带水印 → 加防水印锁段）
- 某格式独有的硬约束没地方放（如竖版海报"商业信息密度锁" → 用小数号插入）
- AI 模型新版本需要新引导段
- subject_type 扩展导致需要新主体段

**❌ 不该新增段落**：
- 取值池更新 → 进表现因素层
- 一次性某游戏特殊文案 → 进 D 表
- 措辞优化 → 更新对应段「内容」字段
- 纯形式问题 → 进 P 表
- 纯设计原则 → 进表现层底线 / Banner 构图三条底线

### 编号规则
- **整数号** 段7/段8 → 通用段
- **小数号** 段4.5 → 仅某格式特化段
- **差异变体不拆段** → 写在「三格式差异」列里

### 扩充工作流
```
实证翻车 → 判断原因
   ├─ 缺职责段          → 新增段落（按 5 字段填齐）
   ├─ 内容描述不到位    → 更新对应段「内容」字段
   ├─ 仅形式问题        → 进 P 表
   └─ 仅设计原则        → 进底线提示
   ↓
（若新增段落）同时在 D 表登记本次翻车作为段落新增的来源溯源
```

---

## 5. ④ 8 项硬检查表（纯 prompt 形式校验 · 三格式通用）

**职责**：只校验 prompt 文本是否合规（标题段格式/Negative 写法/是否多方案/杠杆是否显式 ...），不管「画面好不好看」。
**画面设计原则**：Banner/竖版/横版的版式、面积分配、动线、背景质感属于构图层/表现因素层，不归 P 表。

| # | 检查项 | 修法（关键） |
|---|--------|------|
| P1 | 单层清晰标题（Title Lock 2.1）| 新增独立段 `[Title Lock — Flexible Single Title 2.1]`；Banner 子规则：标题宽 25-55% 或高 40-80%，不是角落 logo |
| P2 | Negative 不裸写 no text | 改 `No extra readable text except the exact game title "<游戏名>"` + 禁止 duplicate title layers / giant background title |
| P3 | 默认 A/B/C 三套剧本 | 不等用户提醒，默认输出 ≥3 套差异化方案 |
| P4 | subject_type 显式判定 | 开场框先判 subject_type，再选取值池（详见 ② 主角分型）|
| P5 | 每条 prompt 显式写 L1/L2/L3/L4 | 每条 prompt 都列 `L1 camera: ... · L2 lighting: ... · L3 setting: ... · L4 visual weight: ...` |
| P6 | 差异化矩阵先输出 | 写 prompt 前先列 4×N 差异化表格，自检至少错 3 行 |
| P7 | 玩法 Fidelity 高危值扫描 | Step 0.5 玩法 Fidelity 自检，命中高危必须中和或换写法 |
| P8 | 出海素材 safe-crop 写入 | 横版:16:9 中央75%宽 / 竖版:9:16 中央70%高 / Banner:只裁宽三档母版 3.5:1 / 5.2:1 / 8:1 |

---

## 6. 全局策略 · C 表 + D 表 + 晋升路径

### C 表（负面禁止 · 跨题材通用）
**职责**：跨题材通用的高危模式（哪些「杠杆 × 取值」会反伤 CTR/留存）

字段：杠杆（L1-L4 / 通用）/ 通用高危模式 / 为什么危险 / 缓解方向

**入表门槛**：实证翻车（不是审美偏好）；多题材印证后从 D 表晋升上来

### D 表（项目翻车账本 · 实证案例库）
**职责**：每条记录 = 一次具体出图项目里被实证翻车的案例

**7 列上下文**：项目·批次 / 题材 / 人群·渠道·地区 / subject_type / 杠杆×取值 / 翻车证据 / 缓解方向·可否晋升 C

**核心理念**：翻车风险不只跟"题材"有关，还跟人群/渠道/地区/subject_type/同期友商占位强相关。每条记录带完整上下文坐标。

### C ↔ D 晋升路径
```
某次出图后 → 实证翻车（CTR 高但留存崩 / 被认错品类）
   ↓
归因到具体「杠杆 × 取值」+ 完整上下文坐标
   ↓
登记 D 表「项目翻车账本」
   ↓
判断扩散性：
   ├─ 仅本游戏触发      → 留 D 表（题材实例）
   └─ ≥2 个题材独立印证 → 晋升 C 表（跨题材通用），D 表保留作"案例溯源"
```

**晋升判定责任人**（v5 起需要明确）：
- 真出图工作站每月 review D 表，AI 提议晋升候选
- 用户人工 confirm 后执行搬运

---

## 7. 表现层底线（三格式通用 · 不可逾越）

**位置**：全局表现因素层 section 顶部

- **禁止空色块背景**：背景至少含渐变/光效/斜切/纹理/粒子/剪影之一
- **颗粒/质感/胶片噪点至少 1 项**：避免"塑料感"
- **层次至少 3 层**：前景 / 中景 / 背景必须有视觉层级

---

## 8. Banner 构图三条底线（仅 Banner · v4.17 → v5 归位）

**位置**：Banner adapter 02 构图层 section 顶部

- **Modular Layout**：横向三分区（标题 / 主体 / 辅助符号）
- **Hero Scale 破框**：主体侧切/破框/局部裁切；prompt 写 "extends beyond frame" / "side cropped"
- **Module Connection**：标题和主体之间必须有视觉连接（运动线/光束/粒子/物体重叠/透视路）

---

## 9. 输出前自检（AI 默认行为 5 条）

**位置**：「输出前自检 · AI 默认行为规则」一级模块

线性化 Prompt 后、发送给模型前的最后一道关：

1. 默认出多题材方案（≥3 套）
2. 每条 prompt 显式包含 L1/L2/L3/L4
3. 绝对禁止游戏按钮（购买/下载/app store badge/评分/分享/CTA）
4. 主动应用 4 杠杆差异化（先输出矩阵，再写 prompt）
5. 角色资产剥离（AI 自动跑 3000 MCP 工具链闭环：comfyui_divide → generate_image gpt-image-2 input_fidelity=high；用户输入端零变化）

---

## 10. 跨格式工作流的"分型分流图"

```
准入门 4 项 (游戏名 / 类型 / ICON / 截图)
   ↓
② 自动判定 subject_type
   ↓
全局策略 (4 杠杆差异化矩阵 + 故事 5 维度)
   ↓
③ 选择画幅 (横版 / 竖版 / Banner)
   ↓
④ 构图层 C1-C4 (按画幅约束取值)
   ↓
⑤ 表现因素层 (色彩 / 字体 / 光影 / 质感 + 表现层底线)
   ↓
⑥ Fidelity 自检 + 高危杠杆值扫描
   ↓
⑦ 线性化 Prompt (按 9 段模板 / Banner 用全 9 段)
   ↓
⑧ 8 项硬检查 P1-P8 (prompt 形式合规)
   ↓
⑨ 输出前自检 5 条 (AI 默认行为合规)
   ↓
出图 → 复盘 → 实证翻车 → 登记 D 表
   ↓ ≥2 题材印证后
晋升 C 表 (沉淀为通用知识)
```

---

## 11. v5 与其他系统的对齐状态

| 系统 | v5 同步状态 |
|------|-----------|
| 学习控制台 cover.html | ✅ 已重构（v5.0 · 2026-06-05）|
| 本工作流总纲 | ✅ 本文档（v5.0）|
| biz-wiki/game/*.md（v4 历史主源）| ⚠️ 顶部加 deprecation 提示，保留作演进史 |
| 真出图工作站 tools/game-cover-sop/ | ❌ 未同步（阶段 2 待办）|
| 3000 MCP 工具链 | ❌ 未同步（阶段 2 待办）|
| D 表自动登记机制 | ❌ 未建立（阶段 3 待办）|
| C↔D 晋升执行人 | ⚠️ 已定义为"用户月度 review + AI 提议候选"，未实操 |

---

## 12. 出处与迭代

| 日期 | 版本 | 主要变化 |
|------|------|---------|
| 2026-06-05 | **v5.0** | 控制台结构重构 + 本工作流总纲建立。Banner 6 锁归位（构图层/表现层）；P 表回归纯形式校验；D 表 7 列上下文；C↔D 晋升路径；9 段模板扩充准则 |
| 2026-06-01 | v4.10 | Prompt Preflight 7 项 + subject_type 四向路由 + scenario_puzzle 分型 |
| 2026-05-29 | v4.4 | AI 默认行为约束（基于 Tricky Puzzle 实证）|
| 2026-05-28 | v3 | 玩法 Fidelity 锁 |
| 2026-05-27 | v2 | 视觉差异化 4 杠杆矩阵 + Fidelity 默认档 |
| 历史 | v1 | Core Layer + Format Adapter 基础架构 |

---

## 13. 引用规则（其他 AI / 工具应该读这份的方式）

- **真出图前必读**：本文档 § 1-9（结构 / 流程 / 主角分型 / 9 段模板 / 硬检查 / 底线 / 默认行为）
- **写 prompt 时**：按 ③ 9 段模板逐段填值，每条 prompt 都通过 P1-P8 硬检查
- **出图后**：按 § 6 D 表登记翻车案例（即使没翻车，也建议留一行"无翻车 · 上下文坐标 · 后续可作晋升判定参考"）
- **想扩充 SOP 时**：按 § 4 扩充规则判断该改哪张表（P 表 / 段落 / 表现层底线 / 构图层底线 / D 表 / C 表）

---

## 14. 配套资源

- **学习控制台**：`wiki/sources/game-poster-learning-sop/cover.html`（浏览器打开 · 只读型工具）
- **真出图工作站**：`tools/game-cover-sop/` (`localhost:3737`)（阶段 2 后才与 v5 对齐）
- **资产库入口**：`资产库/index.html`（卡片墙）
- **历史主源 v4**：
  - `biz-wiki/game/narrative-driven-cover-variants.md`（横版方法论）
  - `biz-wiki/game/game-poster-learning-sop.md`（竖版 SOP）
- **决策记录**：`soul/decisions-log.md`（搜索 v5.0）
