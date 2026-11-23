# X 上的 AI 前沿 · 2026-11-23

**一句话**：黎曼假设从「传闻」升级成「有形式化验证进展」的事件，是今天唯一够 5 分的东西；其余是垂直领域开放权重、评测方法论和一个很现实的 agent 验证问题。

## 值得看（10 条）

| 分 | 内容 | 链接 |
|---|---|---|
| 5 | 黎曼假设：Alpöge + Claude 交付 1700 万行 Lean，Lean FRO/Mathlib 已发布验证声明 | [dotey](https://x.com/dotey/status/2124282462343967111) |
| 4 | 蚂蚁 LingSante-3.1-flash：560B/25B 激活，医疗基准对标 Astra，1M 上下文 | [arankomatsuzaki](https://x.com/arankomatsuzaki/status/2124597469522870272) |
| 4 | Google：用「注入 bug」给 ML 工程 agent 造评测 | [omarsar0](https://x.com/omarsar0/status/2124584960464220408) |
| 4 | RoboQuest：最强模型只解出 23.2% 的物理任务 | [omarsar0](https://x.com/omarsar0/status/2124549311174427069) |
| 4 | Hy4-flash 的 Engram 表换 Q4_0：67.3→35.6GB，KL 最多涨 2% | [bnjmn_marie](https://x.com/bnjmn_marie/status/2124534984732225777) |
| 4 | OpenAI 主张用困惑度而不是 FLOPs 当行业监管指标 | [swyx](https://x.com/swyx/status/2124583459356373052) |
| 3 | 「Agent 说验证过了」怎么才敢信：定标准、用独立检查器 | [dotey](https://x.com/dotey/status/2124603209394078089) |
| 3 | agent 平台的关键原语：agent 与实例/会话必须拆开 | [omarsar0](https://x.com/omarsar0/status/2124506354324840953) |
| 3 | Google AI 订阅或于 12/2 进入第三方 harness，Hermes 首批 | [testingcatalog](https://x.com/testingcatalog/status/2124473529764852190) |
| 3 | Opus 4.7/4.8 可能比 4.6 更小，新版基准或与困惑度高度相关 | [polynoamial](https://x.com/polynoamial/status/2124603793430167558) |

## 统计

- 打开页面 42 / 上限 50
- 抓到帖子 51 条，挑出 10 条（5 分 1、4 分 5、3 分 4）
- 失败 2 个页面：`lmarena_ai`（连续第 20 天）和 `search-1`（arXiv 搜索，`page.evaluate` 15 秒上限，重试仍失败）
- 第五步（长帖串）继续跳过

## 判断

- **日期与空档**：这轮是 11-22 21:30 的提醒晚到 13 小时触发的，按规则用「今天（北京时间）= 11-23」。所以 `data/x/` 里 **11-22 是空的**，中间断了一天。
- **黎曼假设这次改判为 5 分**：昨天只有当事人一句「我证出来了」，我按传闻排除；今天 Lean FRO 与 Mathlib Initiative 就 Lean 验证发了联合声明，交付物是 1700 万行 Lean 代码——有了可核验的第三方依据，才写进 `_picks.json`。这条也说明了为什么昨天那个判断是对的。
- 今天`search-1`（arXiv 关键词搜索）挂了，所以论文来源只剩 `search-2`（Hugging Face）和账号主页，覆盖面会窄一点。
