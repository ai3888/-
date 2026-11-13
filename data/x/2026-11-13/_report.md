# X 上的 AI 前沿 · 2026-11-13

**一句话**：Google 的第三款 Gemini 4 模型（Hydrogen）落地并带来一串「性价比」问题的讨论，DeepSeek 把整个 App 能力开放成 API，llama.cpp 终于到 1.0——今天没有颠覆性发布，但工程侧的信息量很足。

## 值得看（12 条）

| 分 | 内容 | 链接 |
|---|---|---|
| 4 | Gemini 4 Hydrogen：比 3.8 Flash 快 2.5 倍，智能超 Argon | [GoogleDeepMind](https://x.com/GoogleDeepMind/status/2120940338869055788) |
| 4 | Hydrogen 智能略低于 Sonnet 5.5/Sol，成本约 Sonnet 的 1/3 | [ArtificialAnlys](https://x.com/ArtificialAnlys/status/2120941511223185722) |
| 4 | effort 拉满的代价：token 翻倍、智能 +3 分、成本 +68% | [ArtificialAnlys](https://x.com/ArtificialAnlys/status/2120941516407337325) |
| 4 | 腾讯 Hy4 智能指数第 3，CWE-Bench 第一 | [ArtificialAnlys](https://x.com/ArtificialAnlys/status/2121137661180256653) |
| 4 | DeepSeek 把 App 的搜索/文件/语音能力搬进 API | [deepseek_ai](https://x.com/deepseek_ai/status/2121247896918253875) |
| 4 | llama.cpp 发布 1.0.0 | [ggerganov](https://x.com/ggerganov/status/2121246103312212124) |
| 4 | Inkling 2 Small 权重开放，Apache 2.0 | [thinkymachines](https://x.com/thinkymachines/status/2120982625582195011) |
| 4 | Claude Meetings：把 Claude 拉进 Google Meet 里干活 | [dotey](https://x.com/dotey/status/2120979951599931793) |
| 4 | JoMoHa：harness 编辑器本身也用 RL 训练 | [omarsar0](https://x.com/omarsar0/status/2121035321211318565) |
| 4 | OWE-Bench：26 个长程工程任务，Fable 5.2 每题烧 2 亿 token | [_jasonwei](https://x.com/_jasonwei/status/2120933804638613581) |
| 4 | Gemini 4 定价混乱：同价、便宜 25%、12 月翻倍 | [simonw](https://x.com/simonw/status/2121039423441981444) |
| 3 | 思维链该不该动：可监控性与优化的长期矛盾 | [rasbt](https://x.com/rasbt/status/2120895037064020406) |

## 统计

- 打开页面 41 / 上限 50
- 抓到帖子 89 条，挑出 12 条（5 分 0、4 分 11、3 分 1）
- 失败 1 个页面：`lmarena_ai`（连续第 11 天，`page.evaluate` 15 秒上限）
- 长帖串展开卡住（和昨天同一种卡法），已终止并删除半成品，`_picks.json` 里的理由用的是主页摘要

## 判断

- **今天没有 5 分**。最接近的是 llama.cpp 1.0（生态意义大，但帖子里没有技术细节）和 Gemini 4 Hydrogen（官方数字只有一个「2.5 倍」，实测数据在 AA 那边）。按「一手 + 具体信息」的标准都停在 4。
- 反常的是：今天模型发布不少，但**真正有价值的分析都在评测机构和小 V 那边**——AA 的三条（成本结构、effort 边际收益、Hy4 排名）比官方通稿信息密度高得多。
- 继续跳过：英伟达 CEO 变动与员工联名信、Anthropic IPO、各种清单体和 NSFW 模型。这些刷屏但不属于你要的五个方向。
