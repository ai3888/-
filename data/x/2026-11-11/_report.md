# X 上的 AI 前沿 · 2026-11-11

**一句话**：这几天的发布全砸在同一个 30 小时里——NVIDIA 开源 GR00T 2、Google 用 AI 证明了 Signal 协议、Gemini 4 Carbon 与 Qwen4 同时开卖、MiniMax 图像模型开放权重，是近期最密集的一天。

## 值得看（14 条）

| 分 | 内容 | 链接 |
|---|---|---|
| 5 | GR00T 2：开源的机器人 System One 模型，端侧脱线、权重全归你 | [DrJimFan](https://x.com/DrJimFan/status/2120186651741655428) |
| 5 | 首次用 AI 在代码层面证明 Signal 加密实现是安全的（AlphaProof） | [GoogleDeepMind](https://x.com/GoogleDeepMind/status/2120484246401777737) |
| 4 | Gemini Robotics 2.5：学几百种日常技能，叠衣、烘焙、分拣零件 | [GoogleDeepMind](https://x.com/GoogleDeepMind/status/2120169787896525104) |
| 4 | Gemini 4 Carbon 正式开放，定位「长程任务最强」 | [GoogleDeepMind](https://x.com/GoogleDeepMind/status/2120219371473617099) |
| 4 | Qwen4 系列公布，Qwen4-Max 已进预览 | [Alibaba_Qwen](https://x.com/Alibaba_Qwen/status/2120335993643684315) |
| 4 | AA × DeepMind 上线 MKA：agent 读工程图/建筑图/临床影像 | [ArtificialAnlys](https://x.com/ArtificialAnlys/status/2120220567038984212) |
| 4 | Omni Flash 1.2 视频编辑榜第 2，成本降 31% | [ArtificialAnlys](https://x.com/ArtificialAnlys/status/2120283459805749688) |
| 4 | 微软：不加数据不加训练，只换 harness 让 Llama3-8B 长上下文 +64.18 分 | [omarsar0](https://x.com/omarsar0/status/2120160305347260443) |
| 4 | Nod：n8n 开源的本地个人 agent，自带电脑和浏览器 | [omarsar0](https://x.com/omarsar0/status/2120500412763742329) |
| 4 | Stanford CS329Z 课程全公开，作业是从零写一个 Claude Code | [dotey](https://x.com/dotey/status/2120388990616433083) |
| 4 | pi-H3：单张 B200 九秒出 10 秒带音频 768p 视频，去掉 VAE 解码器 | [HanshengCh](https://x.com/HanshengCh/status/2120186218176491876) |
| 4 | MiniMax-H3-Image 开放权重，支持 16 张参考图 | [sep_is_heim](https://x.com/sep_is_heim/status/2120257150421475438) |
| 4 | TRL 在 agent 轨迹上 SFT：2B 模型 5.5% → 34.4% | [SergioPaniego](https://x.com/SergioPaniego/status/2120177440282788028) |
| 4 | Jason Wei 的「基准的基准」：2026 年各实验室到底报了哪些评测 | [_jasonwei](https://x.com/_jasonwei/status/2120283338640621826) |

## 统计

- 打开页面 50 / 上限 50（40 个配置页面 + 10 次重试，没余量做长帖串）
- 抓到帖子 99 条，挑出 14 条（5 分 2、4 分 12）
- 失败 1 个页面：`lmarena_ai`（连续第 9 天，`page.evaluate` 15 秒上限）
- 首轮有 10 个页面 `goto` 超时（导航已提交但等不到 load），我改了脚本：这种情况继续用该页面、等 load 后再提取，重试后 9/10 成功

## 判断

- 今天密度很高，14 条全是 4 分以上，没有凑数：两个 5 分一个是「开源权重 + 端侧运行」的机器人模型，一个是「AI 证明真实加密实现」——都属于会被反复引用的里程碑。
- Qwen4 只给 4 分：官方那条是发布口径，没数字也没评测，Qwen4-Max 还只是预览。
- 今天池子里仍有大量「10 个仓库/8 个第二大脑」清单体和 NSFW 模型，一条没进。
- 提醒：10 号的定时任务因为 DSH 没开而漏跑，`data/x/` 里没有 11-10 目录。
