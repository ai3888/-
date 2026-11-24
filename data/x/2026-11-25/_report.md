# X 上的 AI 前沿 · 2026-11-25

**一句话**：OpenAI 这天发了三件硬货——蛋白质设计做了湿实验验证、开源了给 agent 用的 Linux 防御运行时、GPT-6 Cyber 一次验证 948 个内核漏洞；Anthropic 则在「agent 会不会越狱」上做了一手评估。

## 值得看（13 条）

| 分 | 内容 | 链接 |
|---|---|---|
| 5 | 新预印本：GPT-6 直接设计蛋白质，且有湿实验验证 | [OpenAI](https://x.com/OpenAI/status/2125334383490105601) |
| 5 | Shirudo：开源 Linux 运行时，agent 写 eBPF 规则做实时防御 | [OpenAI](https://x.com/OpenAI/status/2124980590717911527) |
| 4 | GPT-6 Cyber 一次验证 948 个可本地提权的内核漏洞 | [OpenAI](https://x.com/OpenAI/status/2125007927098699827) |
| 4 | Anthropic Siren：沙箱可逃时，agent 会不会逃 | [AnthropicAI](https://x.com/AnthropicAI/status/2125341904644763678) |
| 4 | 回到「神经元基」做可解释性 | [AnthropicAI](https://x.com/AnthropicAI/status/2125365268381929637) |
| 4 | AA 加了 harness 横评：没有全局最强的 harness | [ArtificialAnlys](https://x.com/ArtificialAnlys/status/2125069725977968935) |
| 4 | Epoch 审查 4 个基准：1 个 Verified、3 个 Flawed | [EpochAIResearch](https://x.com/EpochAIResearch/status/2124945252725510614) |
| 4 | 百度 ERNIE 5.5 Flash Preview 开放权重，280B/14B、1M 上下文 | [AdinaYakup](https://x.com/AdinaYakup/status/2125143435485274357) |
| 4 | DeepCrossAttention：把残差连接改成动态路由 | [GoogleResearch](https://x.com/GoogleResearch/status/2124933889131164116) |
| 4 | LlamaIndex 开源 OCRia-1（4B）与 8.1M 的 CPU 版 | [dotey](https://x.com/dotey/status/2125317908326744410) |
| 4 | 只看训练前 20%，能预测这次训练的结果吗 | [omarsar0](https://x.com/omarsar0/status/2125256189831508395) |
| 4 | 黎曼假设反转补充：「25 万页」是玩笑，但证明仍称成立 | [dotey](https://x.com/dotey/status/2125081053098373590) |
| 3 | Inkling 2 Mini 微调：22GB 显存、快 1.8–3.1 倍 | [UnslothAI](https://x.com/UnslothAI/status/2125243469094605071) |

## 统计

- 打开页面 41 / 上限 50
- 抓到帖子 96 条（去重 95），挑出 13 条（5 分 2、4 分 10、3 分 1）
- 失败 1 个页面：`lmarena_ai`（连续第 22 天）
- 第五步（长帖串）继续跳过

## 判断

- **重要更正：昨天那 40 个页面全挂，不是 X 改版，是暂时性故障。** 今天同一个 `x_extract.js` 在 39/40 个页面上正常工作（含 OpenAI、Anthropic 这些大号），说明昨晚是浏览器端执行环境卡住了。我前天基于 karpathy 单页做的「X 改版」判断是错的——那个页面恰好是新 UI，属于分批灰度，不是全面改版。
- **黎曼假设这条我降级了**：Alpöge 本人承认「25 万页文档」是玩笑、Lean 代码很乱，但仍称证明成立。所以昨天那个 5 分给得偏乐观，今天补了这条反转，让读者自己判断。
- **日期空档**：`data/x/` 里 **11-24 是空的**（那天 21:30 的提醒到的时候 DSH 没开），今天的窗口从 11-24 下午开始。
