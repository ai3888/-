# 第二大脑

把你和各个 AI 的聊天记录、还有你的资料，存成一个属于自己的记忆库：每段对话都存下来，按主题整理成分支，再写一份「关于我」；PDF、图片、文档这些文件原样保管。换一个 AI、或者用 API 接新模型时，先让它读 `memory/index.md`，它就知道你是谁、聊过什么，不用你从头解释。

记忆库就是一堆 Markdown 文件，不绑定任何一家 AI，谁都能读。

## ⚠️ 只能放在私有仓库

记忆库里是你全部的私人聊天，所以这套程序只能在**私有**仓库里用。自带的 GitHub Actions 发现仓库是公开的，会直接停下，不处理任何聊天记录。

公开的「项目雷达」仓库（`ai3888/-`）里的 `second-brain/` 文件夹只是代码：那里的 `memory/` 和 `inbox/` 被 `.gitignore` 忽略，不会被提交。

## 怎么运作

```
inbox/                    ← 你放进来的导出文件和资料
  │  python memory.py import inbox
  ▼
memory/conversations/     每段对话一个 Markdown（原文，按来源和月份分文件夹）
memory/files/             其他文件原样存放（PDF、图片、文档……），按月份分文件夹
  │  python memory.py organize   GPT 给每段对话写一句话摘要和要点、归到分支、记下关于你的信息
  ▼
memory/index.md           入口：给 AI 的说明 + 关于我 + 所有分支（每个附一句话）
memory/profile.md         关于我：基本情况、在做的事、常用工具、偏好、目标、不喜欢的
memory/branches/          每个分支一个文件：分支总结 + 每段对话的摘要和原文链接
```

AI 读的时候一层层往下：先读 `index.md`（几千字），需要细节再读某个分支，还要更细才读原文。token 只花在用得上的地方。

## 开始使用

1. **新建私有仓库**：GitHub 右上角 + → New repository，名字比如 `memory`，一定选 **Private**。把这个文件夹里的文件放进去（也可以让 Claude 帮你建好）
2. **配置模型**（和项目雷达一样）：新仓库 Settings → Secrets and variables → Actions
   - Secrets 里添加 `OPENAI_API_KEY`
   - Variables 里可以添加 `OPENAI_MODEL`（默认 `gpt-4o-mini`）和 `OPENAI_BASE_URL`（用中转或国内模型时填）
   - 不配置也能用：导出的聊天记录只存原文，不整理分支；GPT 写的存档卡片（见下一节）不需要 key，照样归到分支
3. **导出聊天记录**：

   | 来源 | 怎么导出 | 放进 inbox 的文件 |
   |---|---|---|
   | ChatGPT | Settings → Data controls → Export data，邮件里下载 zip | zip，或者里面的 `conversations.json` |
   | Claude | Settings → Privacy → Export data，邮件里下载 zip | zip，或者里面的 `conversations.json` |
   | DeepSeek | 网页版设置里导出全部对话 | zip，或者里面的 `conversations.json`（按开源项目 Conversation Export Workbench 的格式说明支持，还没用真实导出验证过，读不出来会提示） |
   | Gemini、Grok、Qwen、Perplexity 等 | 装浏览器扩展 [AI Chat Exporter](https://github.com/Covai-Labs/ace)，打开对话导出 JSON | `.json`，一段对话一个文件；ChatGPT、Claude 的单段对话也能这样导，和官方导出的同一段会自动对上 |
   | 自己用 API 聊的 | 存成 OpenAI 消息格式（见下方） | `.json` 或 `.jsonl` |
   | Kimi、豆包等其他 AI | 把对话复制下来，或者把 `gpt-prompt.md` 贴给它，让它「存档」 | 一段对话一个 `.md` 或 `.txt`，第一行 `# 标题` |
   | 笔记 | 直接写 | `.md` 或 `.txt`，和对话一样会被整理进分支 |
   | 其他资料（PDF、图片、Word、Excel……） | 直接上传 | 原样存进 `memory/files/`，在 `index.md` 里列出来，但不会读里面的内容 |

4. **上传**：打开新仓库的 `inbox` 文件夹 → Add file → Upload files。网页上传单个文件最大 25MB，导出的 zip 太大时，解压后只把 `conversations.json` 重新压缩成 zip 再传（纯文字压缩后会小很多）
5. **等几分钟**：Actions 自动导入、整理，原文件删掉，结果提交到 `memory/`。第一次对话多的话，每次最多整理 300 段，剩下的每天凌晨接着整理，也可以在 Actions 页面手动点 Run workflow

以后定期（比如每月）再导出一次、上传一次就行。导出文件里是全部历史，已经存过的会自动跳过；之前的对话后来又聊了新内容，会更新原文并重新整理。

## 让 GPT 帮忙整理：存档卡片

不想花 API 的钱，可以让 ChatGPT 里的 GPT 当场整理。把 [`gpt-prompt.md`](gpt-prompt.md) 放进 ChatGPT「项目」的说明里，之后在这个项目里聊天：

- 说「**交底**」：GPT 把它记得的关于你的一切写成卡片，一次性把记忆库填起来
- 说「**存档**」：GPT 把这次对话写成一张卡片（自带分支、摘要、要点、关于我），下载后上传到 `inbox/`
- 说「**更新存档**」：同一件事有了进展，用同一个文件名重写，旧卡片被替换

卡片已经整理好了，程序直接归到分支，不再调用 API。其他 AI（Claude、DeepSeek……）照着 `gpt-prompt.md` 写的卡片也一样能用。

## 分支：提前定好，互不影响

分支设定在 `branches.toml`，每个分支写一句说明和别的叫法：

```toml
[[branches]]
name = "AI 工具/第二大脑"
about = "把和各个 AI 的聊天、资料存进私有仓库，按主题整理"
aliases = ["第二大脑", "记忆库"]
```

- 预设的分支没有内容也会列在 `index.md` 里，AI 一看就知道东西该归到哪
- 卡片里写的是别名（「记忆库」「项目/第二大脑」），会自动归到正式名字下，不会分裂成好几个分支
- 想改名：把旧名字写进新分支的 `aliases`，旧卡片会跟过去
- 各分支互不影响：`index.md` 和 `gpt-prompt.md` 都写明了，聊哪个主题就以哪个分支为准，别的分支只能当参考并说明出处
- 想一次设定很多分支：对 GPT 说「**列分支**」，它会按你的情况写一份 `branches.toml`，上传到 `inbox/` 就自动替换。格式不对的话不会替换，文件留在 `inbox/`，运行日志里会说明原因

## 让 AI 读你的记忆

- **能调用网络 API 的**（GPTs 的 Action、Agent、自己写的程序）：建一个只读 token：GitHub 头像 → Settings → Developer settings → Fine-grained tokens → Generate new token，Repository access 只选这个私有仓库，Permissions 里 Contents 选 Read-only。然后：

  ```
  GET https://api.github.com/repos/<你的用户名>/<仓库名>/contents/memory/index.md
  Authorization: Bearer <token>
  Accept: application/vnd.github.raw
  ```

  分支和原文同理，把路径换成 `memory/` 加上 `index.md` 里的链接。
- **ChatGPT / Claude 的项目（Projects）**：把 `index.md` 和 `profile.md` 上传成项目文件。
- **DeepSeek、Kimi、豆包等连不上仓库的 AI**：上传 `memory/记忆包.md` 这一个文件就行。它把工作说明、关于我和各分支的内容合在一起，每次更新记忆库时自动重新生成。
- **任何 AI，复制粘贴**：`python memory.py context 关键词`，会打印 `index.md` 加上和关键词相关的分支，贴到对话开头。
- **用 API 接新模型**：把 `index.md` 的内容放进 system prompt。

token 就是你全部记忆的钥匙：只给只读权限、只选这一个仓库，不要贴到公开的地方。

## 自己用 API 聊天的记录格式

```json
[
  {
    "id": "可选，同一段对话保持不变，再导入时会更新原来那段",
    "title": "标题",
    "messages": [
      {"role": "user", "content": "……"},
      {"role": "assistant", "content": "……"}
    ]
  }
]
```

`.jsonl` 每行一段也可以。

## 在自己电脑上运行

需要 Python 3.11 或更高版本，不用安装任何依赖：

```bash
export OPENAI_API_KEY=sk-...                       # 可选，不设置就只存原文
python3 memory.py import ~/Downloads/chatgpt.zip   # 也可以是文件夹
python3 memory.py organize
python3 memory.py context 投资 美股 > 给AI的背景.txt
```

## 说明

- 整理时，对话内容会发给你配置的模型服务。不想发出去就不配置 key，只存原文。
- 各家 AI 的网页版和 App 都没有提供读取聊天记录的接口，没法每聊一句就自动存进来，目前只能定期导出，或者聊完说「存档」。
- 认出是聊天记录、但一段对话都没读出来的文件（比如导出格式变了），也当资料存进 `memory/files/`，不会被删掉。
- 分支的大类在 `memory.toml` 的 `suggested_branches` 里改。改完想把所有对话重新归类：`python memory.py organize --redo`。
- 认不出来是聊天记录的文件都当资料存进 `memory/files/`，内容一样的只存一份。GitHub 不收超过 100MB 的文件，大的视频、安装包别往这里放。
- 整理时只记你自己说的或明确认可的事，AI 的建议不会记成「关于我」；还没采纳的建议在要点里标「AI 建议：」。
