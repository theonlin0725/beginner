# 信号研判 · 已研判示例（few-shot / 测试夹具）

> **用途**：展示「决策导向信号研判层」如何把一批原始采集条目转成严格 JSON。
> 本例输入 = 用户提供的 4 条 GNews 韩国社媒聚合条目（2026-07-27 ~ 2026-08-01）。
> **结论：4 条全部 `pass_review: false`**——纯社媒搜索/单帖噪音、无具体事件/政策/禁忌/与游戏无关。这正是"宁缺毋滥"的过滤器价值：一批热闹的原始信号，过筛后为 0。

---

## 输入 batch

```json
[
  {"id": 0, "region": "韩国", "topics_hint": ["hotspot", "culture"], "title": "sky_children_of_the_light - بحث - x.com", "summary": "GNews 聚合到 X 平台关于《Sky: Children of the Light》的搜索结果链接", "source_name": "GNews Social - Korea game on X", "source_type": "news_query", "published": "Sat, 01 Aug 2026 22:23:43 GMT"},
  {"id": 1, "region": "韩国", "topics_hint": ["hotspot", "culture"], "title": "m (@gatitadtae) on X - x.com", "summary": "GNews 聚合到 X 用户 @gatitadtae 的帖子链接", "source_name": "GNews Social - Korea game on X", "source_type": "news_query", "published": "Mon, 27 Jul 2026 21:07:11 GMT"},
  {"id": 2, "region": "韩国", "topics_hint": ["hotspot", "culture"], "title": "\"수원작떄기사는곳 (탤 𝗭𝗭𝗔𝗡𝗚𝗨).eyu\" - Results on X | Live Posts & Updates - x.com", "summary": "GNews 聚合到一条韩语 X 平台搜索结果（含'수원'等关键词）", "source_name": "GNews Social - Korea game on X", "source_type": "news_query", "published": "Wed, 29 Jul 2026 03:00:30 GMT"},
  {"id": 3, "region": "韩国", "topics_hint": ["hotspot", "culture"], "title": "아니 성현이 숨꼭 촬영하면서 칼답한거 개웃겨.. 단톡방 지분율 1위야 ㅁㅊㅋㅋㅋ 말투 걍 위버스랑 다를게 없음 - x.com", "summary": "GNews 聚合到一条 X 帖子，粉丝讨论某偶像拍摄花絮并对比 Weverse（HYBE 粉丝社区平台）语气", "source_name": "GNews Social - Korea game on X", "source_type": "news_query", "published": "Fri, 31 Jul 2026 11:11:15 GMT"}
]
```

## 输出 JSON（分类模型产出）

```json
{"results":[
  {
    "id": 0,
    "relevance": 0.15,
    "pass_review": false,
    "drop_reason": "社媒搜索噪音，无具体事件/政策/禁忌，无法落到具体游戏决策",
    "nature": "mixed",
    "topic": "hotspot",
    "compliance_clause": [],
    "targets": [],
    "affected_games": "",
    "level": "low",
    "fact": "GNews 于 2026-08-01 聚合到一条 X 平台关于《Sky: Children of the Light》的搜索结果链接，无具体事件内容。",
    "impact": "",
    "action": "",
    "summary_zh": "韩国社媒关于《Sky》的搜索聚合，无实质事件",
    "event_key": "korea sky cotl social noise"
  },
  {
    "id": 1,
    "relevance": 0.1,
    "pass_review": false,
    "drop_reason": "社媒单帖无标题无内容，无具体事件",
    "nature": "mixed",
    "topic": "hotspot",
    "compliance_clause": [],
    "targets": [],
    "affected_games": "",
    "level": "low",
    "fact": "GNews 于 2026-07-27 聚合到一条 X 用户 @gatitadtae 的帖子链接，无实质内容。",
    "impact": "",
    "action": "",
    "summary_zh": "韩国社媒单帖，无实质内容",
    "event_key": "korea x post noise"
  },
  {
    "id": 2,
    "relevance": 0.12,
    "pass_review": false,
    "drop_reason": "社媒搜索词噪音，无法落到具体游戏/禁忌/政策条款",
    "nature": "mixed",
    "topic": "culture",
    "compliance_clause": [],
    "targets": [],
    "affected_games": "",
    "level": "low",
    "fact": "GNews 于 2026-07-29 聚合到一条韩语 X 平台搜索结果（含'수원'等关键词），无具体事件内容。",
    "impact": "",
    "action": "",
    "summary_zh": "韩国社媒搜索词聚合，无实质事件",
    "event_key": "korea x search noise"
  },
  {
    "id": 3,
    "relevance": 0.1,
    "pass_review": false,
    "drop_reason": "与游戏无关（K-pop 粉丝帖 / Weverse 粉丝社区平台）",
    "nature": "mixed",
    "topic": "hotspot",
    "compliance_clause": [],
    "targets": [],
    "affected_games": "",
    "level": "low",
    "fact": "GNews 于 2026-07-31 聚合到一条 X 帖子，内容为粉丝讨论某偶像（성현이）拍摄花絮并对比 Weverse（HYBE 粉丝社区平台）语气，与游戏无关。",
    "impact": "",
    "action": "",
    "summary_zh": "韩国 K-pop 粉丝帖，与游戏无关",
    "event_key": "korea kpop weverse noise"
  }
]}
```

## 研判要点（为什么全丢）

| id | 现象 | 决策标准判定 | drop_reason |
|----|------|--------------|-------------|
| 0 | 《Sky》的 X 搜索结果链接 | 仅聚合链接，无事件/政策/禁忌，改变不了任何选品或合规决策 | 社媒搜索噪音 |
| 1 | 某用户单条 X 帖链接 | 无标题无正文，无信息量 | 社媒单帖无内容 |
| 2 | 韩语搜索词聚合 | 搜索词本身 ≠ 事件，无法落到具体游戏/题材/禁忌 | 搜索词噪音 |
| 3 | K-pop 粉丝讨论偶像/Weverse | 与游戏无关（Weverse 是 HYBE 粉丝社区，非游戏） | 与游戏无关 |

> 若未来出现 `pass_review: true` 的同区域社媒条目（如"韩国玩家因某游戏内宗教符号发起 #抵制"且 ≥2 独立来源交叉），其 `event_key` 应与既有基线做跨期去重（见 `dedupe_baseline.md`）。
