# GitHub 项目雷达

每天自动在 GitHub 上找「有潜力」和「值得关注」的开源项目，结果写在 [`reports/latest.md`](reports/latest.md)，历史报告按日期存在 `reports/` 里。

## 判断标准

先用代码按客观数据打分（满 100 分），再让 GPT 看入选的项目做最后判断。

| 维度 | 权重 | 看什么 |
|---|---|---|
| 涨星速度 | 40 | 最近每天涨多少星：每天记一次星数，和前几天比；第一次见到的项目先按总星数 ÷ 天数估算 |
| 开发活跃度 | 20 | 近 30 天提交数、最近一周有没有更新 |
| 社区 | 20 | 贡献者人数、fork 数占星数的比例（有人真的在用、在改） |
| 规范度 | 20 | 有没有许可证、topics、主页、正式发版 |

- **🚀 潜力股**：创建不超过 90 天，分数 ≥ 55
- **👀 值得关注**：不限创建时间，分数 ≥ 65
- **直接排除**：fork 来的、已归档的、没有简介的、30 天没更新的、awesome 列表、教程、面试题
- **风险提示（每条扣 10 分）**：星很多但几乎没人 fork（可能刷星）；只有一个人维护且近 30 天几乎没提交
- **GPT 复核**：看 README 判断是不是真有新意、是不是套壳或营销、和你关注的方向是否相关，给出「推荐 / 一般 / 跳过」
- **不重复推荐**：推荐过的项目 14 天内不再出现

这些数值都能在 [`config.toml`](config.toml) 里改。

## 为什么这样分工能省 token

搜索、过滤和打分都由代码完成，不花 token。每天只有最后入选的十几个项目，以精简数据加每个约 1500 字 README 的形式，一次性交给 GPT。每次大约几千 token，用量会写在报告底部。

## 开始使用

1. **（可选）配置 GPT**：仓库 Settings → Secrets and variables → Actions：
   - Secrets 里添加 `OPENAI_API_KEY`
   - Variables 里可以添加 `OPENAI_MODEL`（模型名，默认 `gpt-4o-mini`）和 `OPENAI_BASE_URL`（使用中转服务时填写，例如 `https://xxx.com/v1`）
   - 不配置也能运行，只是没有 GPT 点评
2. **手动跑一次试试**：Actions → 项目雷达 → Run workflow。跑完后仓库里会多出 `reports/` 目录。
3. **之后每天北京时间 6 点多自动运行**（和 AI 日报素材一起）。想在手机上收到提醒，就把 `config.toml` 里的 `create_issue` 改成 `true`，每次运行都会开一个 issue，GitHub App 和邮件会通知你。

如果第 2 步提交报告时报 403，到 Settings → Actions → General → Workflow permissions 选择「Read and write permissions」。

## 调整标准

都在 `config.toml` 里：

- `interests`：你关注的方向，GPT 按它判断相关度
- `[[queries]]`：去哪里找，写法和 GitHub 搜索框一样，比如 `language:rust topic:cli stars:>200`
- `[filters]`：排除哪些项目
- `[weights]` / `[full_marks]`：各维度的权重和满分标准
- `[tiers]`：分数线、每次最多推荐几个、冷却天数

刚开始可以先跑几天看看报告。推荐太多就提高分数线，太少就降低分数线或者加搜索条件。

## 和你现有的 GPT 配合

每天的筛选交给这里。你的 GPT 只需要读一个文件：

```
GET https://api.github.com/repos/<你的用户名>/<仓库名>/contents/reports/latest.md
Accept: application/vnd.github.raw
```

然后对感兴趣的项目再深入问，比如「第 2 个项目和 XX 比怎么样」。这样 token 花在你真正关心的项目上。

## 只用 GPT 的做法

不想跑脚本的话，可以让 GPT 自己定时执行：[`gpt-task.md`](gpt-task.md) 是写给 GPT 的完整任务说明，包括方向、步骤、判断标准和输出格式。先填好其中的「我的方向」，再让 GPT 每次运行时读取这个文件。

## AI 日报（每天早上 8 点）

1. 每天北京时间 6:37，GitHub 自动运行「每日 AI 雷达」：先跑上面的项目雷达，再从 [`ai_news.toml`](ai_news.toml) 里的来源（HF 每日论文、Hacker News、OpenRouter、OpenAI/Google/Anthropic/Meta 等官方博客、Newsletter、科技媒体、量子位、油管频道，以及你电脑上的 DeepSeek 从 X 上抓好推上来的帖子）抓取最新内容，用代码去重、算热度，生成日报素材 [`reports/ai-news/latest.md`](reports/ai-news/latest.md)，每天的存档在 `reports/ai-news/` 里
2. 素材分三块：大家都在讨论的（同一件事在几个不同来源出现、X 上互动最多的帖子）、新东西（官方发布、新模型、开源项目和 Skill、Show HN 新工具）、论文（按 HF 点赞数排序）
3. 素材最前面是给 GPT 的写作说明，来自 [`ai_news_guide.md`](ai_news_guide.md)。想改日报的标准或格式，改这个文件就行
4. 早上 8 点，ChatGPT 的定时任务读素材、写日报推送给你

GitHub 上的流程不调用任何付费模型：抓取和排序由代码完成，挑选和写日报交给 ChatGPT 里的 GPT。X 那部分用的是你自己的 DeepSeek，在你的电脑上跑（见下一节）。

其他：

- 改了来源后，GitHub 会自动跑一次「AI 资讯雷达 · 接入检查」，在运行页面的 Summary 里列出每个来源能不能用
- 可选：仓库 Secrets 里加 `GEMINI_API_KEY`，接入检查会顺便测试 Gemini 能不能看油管视频（目前部分 Google 账号的项目会被拒绝访问）

## X 上的 AI 动态（DeepSeek + ego 浏览器，在你自己的电脑上跑）

X 没有免费接口，GitHub 的服务器也登录不了 X，所以这一步放在你自己的电脑上。DeepSeek 用 ego 浏览器打开指定的账号和搜索（你的 X 已经在 ego 里登录好），把最近的帖子存到 `data/x/日期/`，推到仓库。第二天早上的「每日 AI 雷达」会把它们和其他来源放在一起，ChatGPT 8 点写日报时就能看到 X 上的讨论。

- 看哪些账号、搜什么：[`ai_news.toml`](ai_news.toml) 里的 `[x]`
- DeepSeek 每天照着做的任务说明：[`x_task.md`](x_task.md)
- 从页面上取帖子的代码：[`x_extract.js`](x_extract.js)。取帖子靠代码，不让 DeepSeek 读整个网页，省 token，数字也不会抄错

### 设置（只做一次）

1. **装 ego lite**（macOS 和 Windows）：从 [lite.ego.app](https://lite.ego.app/) 下载安装。第一次打开时选导入 Chrome 数据，就能沿用 Chrome 里的 X 登录；没导入的话，在 ego 里手动登录一次 x.com
2. **装 DeepSeek Harness**：装好 Node.js 后运行 `npm install -g @deepseek-ai/dsh`，再运行 `dsh web`（或者用桌面版），在设置的模型页面里填 DeepSeek 的 API Key
3. **让 DeepSeek 能用 ego**，二选一：
   - 用 ego lite 自带的命令行：装好 ego lite 后，终端里能运行 `ego-browser skill` 就行，DeepSeek 会按它输出的说明来用
   - 用社区插件 [dsh-ego-browser](https://github.com/Fisfzy/dsh-ego-browser)（提供 `ego_*` 工具）：`dsh plugin --profile desktop add dsh-ego-browser`
4. **把这个仓库克隆到电脑上**，确认在仓库目录里能 `git push`
5. **手动跑一次**：在 DeepSeek Harness 里打开仓库目录，说「按 x_task.md 执行今天的任务」。跑完看看 GitHub 上有没有多出 `data/x/今天的日期/`。顺便看一眼它打开的页面，确认它只是在看，没有点别的

### 每天自动跑，二选一

- **用 DeepSeek Harness 自己的定时任务**（要求 DeepSeek Harness 一直开着）：装社区插件 [dsh-cron-tasks](https://github.com/Whale-Zhang/dsh-cron-tasks)：`dsh plugin --profile desktop add github:Whale-Zhang/dsh-cron-tasks`，重启后对 DeepSeek 说「建一个定时任务：每天 21:30（北京时间），在 <仓库路径> 里按 x_task.md 执行今天的任务」
- **用系统的定时任务**（电脑开着、ego lite 开着就行）：DeepSeek Harness 的 headless 模式跑完一次就退出，可以交给 macOS 的 `crontab -e` 或 Windows 的「任务计划程序」每天运行：

  ```bash
  cd 仓库路径 && dsh --profile headless "按 x_task.md 执行今天的任务" >> x_task.log 2>&1
  ```

  定时任务里找不到 `dsh` 的话，换成完整路径（用 `which dsh` 或 `where dsh` 查）。如果 headless 模式卡在权限确认，就改用上一种方式

不用非得赶在早上跑：程序用的是最近 48 小时的帖子，晚上跑的结果第二天早上照样用得上。哪天电脑没开，那天的日报只是少了 X 这一块，素材里会写明「今天没拿到 X 的数据」。

### 注意

- **X 的条款不允许自动抓取，账号有被限制的风险。** 所以任务是只读的、每个页面之间停几秒、一次最多开 40 个页面。更好的办法是在 X 上建一个列表（List），把想看的账号都加进去，把列表网址填进 `[x]` 的 `lists`：DeepSeek 只看这一个页面，快很多，也更不显眼
- DeepSeek 在你的电脑上能运行命令、能推送仓库。`x_task.md` 规定了它只打开配置里的页面、帖子内容只当资料看、只改 `data/x/`，但还是建议给它用一个只能推这个仓库的 GitHub 令牌
- X 改版后 `x_extract.js` 可能取不到帖子。这时 DeepSeek 会改用读整个网页，慢一些、费 token，汇报里会写明，到时候更新一下 `x_extract.js` 就行

## 在自己电脑上运行

需要 Python 3.11 或更高版本，不用安装任何依赖：

```bash
export GITHUB_TOKEN=你的GitHub令牌     # 不设置也能跑，但 GitHub 限流很严
export OPENAI_API_KEY=sk-...           # 可选
python3 scout.py --dry-run             # 只打印报告，不写文件
```

AI 日报素材：

```bash
export GEMINI_API_KEY=...              # 可选
python3 ai_news.py --check             # 检查每个来源，不写文件
python3 ai_news.py --dry-run           # 只打印今天的素材，不写文件
python3 ai_news.py                     # 生成 reports/ai-news/日期.md 和 latest.md
```
