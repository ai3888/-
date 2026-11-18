# X 上的 AI 前沿 · 2026-11-18

**一句话**：GPT-6.2 Astra/Sol 发布（更便宜但更强），腾讯把 224B、1M 上下文的 Hy4 flash 开放权重；同一天 Epoch 用「我们自己干的活」给所有前沿模型泼了盆冷水——最强模型还是追不上人类承包商。

## 值得看（13 条）

| 分 | 内容 | 链接 |
|---|---|---|
| 5 | GPT-6.2 Astra/Sol：刷新纪录，成本不到 GPT-6 Astra 的 1/3 | [OpenAI](https://x.com/OpenAI/status/2122750124543926515) |
| 5 | 腾讯 Hy4 flash 开放权重：224B/12B 激活、1M 上下文、原生多模态 | [TencentHunyuan](https://x.com/TencentHunyuan/status/2122912575302119554) |
| 4 | Epoch：最强模型仍追不上真人做 Epoch 自己的工作 | [EpochAIResearch](https://x.com/EpochAIResearch/status/2122808111849488867) |
| 4 | AA-Robotics 换榜首：GPT-6.2 Astra 79 分（+10） | [ArtificialAnlys](https://x.com/ArtificialAnlys/status/2122757022710104131) |
| 4 | 微软 MAI-Image-2.7 图像编辑第一，价格只有后四名的 1/6 | [ArtificialAnlys](https://x.com/ArtificialAnlys/status/2122754535206846610) |
| 4 | Antigravity 机器人插件：接机械臂、MuJoCo 里练、真机上跑 | [GoogleDeepMind](https://x.com/GoogleDeepMind/status/2122767521925230896) |
| 4 | Google RSI 论文：在控制层级上做持续递归自我改进 | [omarsar0](https://x.com/omarsar0/status/2122701047118635485) |
| 4 | Self-Improving Memory：模型自己发现记忆技能再练进权重 | [omarsar0](https://x.com/omarsar0/status/2122817030277509231) |
| 4 | 预训练不要 LR 衰减：局部回归 + 检查点平均 | [rasbt](https://x.com/rasbt/status/2122721652433715481) |
| 4 | MoE 训练基建：12.9B→1.2T，最多 512 张 B300 | [TaoTianhua](https://x.com/TaoTianhua/status/2122808677270970814) |
| 4 | 微软开源 bitnet.cpp：100B 1-bit 模型单 CPU 可跑 | [byteonai](https://x.com/byteonai/status/2122717876054310952) |
| 4 | NVIDIA 放出投机解码 draft：接受率 +46% | [HuggingPapers](https://x.com/HuggingPapers/status/2122737583361057024) |
| 4 | Marin Mochi 535B 放出全部 57 个中间 checkpoint | [dlwh](https://x.com/dlwh/status/2122799840057004296) |

## 统计

- 打开页面 40 / 上限 50
- 抓到帖子 116 条（去重 115），挑出 13 条（5 分 2、4 分 11、3 分 0）
- 失败 1 个页面：`lmarena_ai`（连续第 16 天，`page.evaluate` 15 秒上限）
- 第五步（长帖串）继续跳过

## 判断

- 今天密度很高，够格的全在 4 分以上：模型发布（GPT-6.2、Hy4 flash）、评测（Epoch、AA 三条）、研究（RSI、记忆、预训练范式）、基建（MoE 训练、bitnet.cpp、投机解码、中间 checkpoint）。
- **最有信息量的是 Epoch 那条负面结论**：几个前沿模型在「Epoch 自己干的活」上还达不到人类承包商水平，GPT-6.2 Astra 反而因为过度谨慎漏了关键部分——这类「模型自己当客户」的评测比排行榜分数更能说明问题。
- GPT-6.2 的发布节奏值得注意：官方口径强调「成本不到上一代三分之一」，而社交平台上大量「6.2 好差」的评价被 dotey 等指出是早期版本造成的观感差异。
