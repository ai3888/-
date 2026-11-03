# X 上的 AI 前沿 · 2026-11-03

**一句话**：今天是「改权重」的主场——Mistral Large 4 开放权重，GPT-6 Astra 不训练直接把 0.8B 模型的数学能力拔高 6 倍；另外补上两个新基准（AA-PersonalityBench、GDPx）和一批 agent 工具。

## 值得看（14 条）

| 分 | 内容 | 链接 |
|---|---|---|
| 5 | Mistral Large 4 开放权重，1T 总参 / 52B 激活，附技术报告 | [MistralAI](https://x.com/MistralAI/status/2117562068220195097) |
| 4 | 权重空间编程：改 0.016% 权重，MATH-500 7.9%→48.1% | [dotey](https://x.com/dotey/status/2117408133773705525) |
| 4 | Hugging Face 复现上面这个结果，开源模型 + demo | [NielsRogge](https://x.com/NielsRogge/status/2117541532827848972) |
| 4 | AA-PersonalityBench：Kimi K3.1 Pro 性格漂移 30 个百分位 | [ArtificialAnlys](https://x.com/ArtificialAnlys/status/2117385943959093677) |
| 4 | AI 写代码把 Git 撑爆：OpenAI 的 Pando、Anthropic 的 Scion | [dotey](https://x.com/dotey/status/2117484277277286623) |
| 4 | Hydrogen-1.0：专门给科研的开放权重模型 | [omarsar0](https://x.com/omarsar0/status/2117414488152694941) |
| 4 | Sage 2-Extract：带原文出处的结构化抽取，便宜 166 倍 | [omarsar0](https://x.com/omarsar0/status/2117310105314086985) |
| 4 | Hume Audio Decision API：音频原生决策，一次调用替代十个模型 | [omarsar0](https://x.com/omarsar0/status/2117294007487205438) |
| 4 | GDPx 基准：最强模型在 agent 任务上只有 12% | [omarsar0](https://x.com/omarsar0/status/2117282765804630305) |
| 4 | OpenAI LifeVal：衡量个人助理在真实生活任务上的表现 | [OpenAI](https://x.com/OpenAI/status/2117307611338997846) |
| 4 | 数据受限预训练的最优缩放配方，集成重新有用 | [andrewgwils](https://x.com/andrewgwils/status/2117387171653177481) |
| 4 | Claude Messages API 上线 message threads 公测 | [dotey](https://x.com/dotey/status/2117339521683448221) |
| 4 | CoT 可控性：熵在 thinking 标签后几个 token 就骤降 | [omarsar0](https://x.com/omarsar0/status/2117277307866063107) |
| 4 | 美团 LongCat-2.5：1.6T 总参 / 49B 激活的多模态 agent 模型 | [testingcatalog](https://x.com/testingcatalog/status/2117285744548970683) |

## 统计

- 打开页面 45 / 上限 50
- 抓到帖子 89 条，挑出 14 条（5 分 1、4 分 13、3 分 0）
- 失败 1 个页面：`lmarena_ai`（连续第 5 天，`page.evaluate` 15 秒上限）；`AnthropicAI` 首次加载超时后重试成功
- 长帖串 3 条展开失败（帖子页返回空），空文件已删除，未提交

## 判断

- 今天「口号/口水」明显变少，一手发布变多，是账号池换过之后的正常状态。
- 值得警惕的一条：权重空间编程这类结果，我先按「论文」收录，等 Hugging Face 复现的可复现性被更多人验证后再看是否升到 5 分。
