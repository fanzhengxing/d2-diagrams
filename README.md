# D2 Diagrams 🎯

> **One skill to diagram them all.** 说句话就出图 — 自然语言 → 专业图表，自动布局。

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![D2](https://img.shields.io/badge/D2-v0.7.1+-orange)](https://github.com/terrastruct/d2)
[![Hermes](https://img.shields.io/badge/Hermes-Skill-purple)](https://hermes-agent.nousresearch.com)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-green)](https://code.claude.com)
[![GitHub Stars](https://img.shields.io/github/stars/fanzhengxing/d2-diagrams?style=social)](https://github.com/fanzhengxing/d2-diagrams)

```
                                             ╭──────────────────────╮
   描述: "画个微服务架构图"                     │    SVG · PNG · PDF   │
     ↓                                       │   PPTX · GIF · ASCII  │
   D2 声明式语法 → 自动布局(dagre/ELK) →      │   · HTML暗色包装      │
                                             ╰──────────────────────╯
```

---

## 🌟 一句话

**说句话就出图** — 用自然语言描述你的系统，D2 自动布局生成专业图表。
支持 **13 种图类型、7 种输出格式、22 个内置主题**。

Built on [terrastruct/d2](https://github.com/terrastruct/d2) (24.4K⭐) — the most popular text-to-diagram engine.

## 🎨 能画什么

| 图类型 | 示例场景 |
|--------|----------|
| 🏗️ **架构图** | 系统部署、微服务拓扑、云架构 |
| 🔀 **流程图** | 业务流程、CI/CD 流水线、算法 |
| 🔄 **序列图** | API 调用、协议交互、OAuth 流程 |
| 📦 **类图 (UML)** | OOP 设计、领域模型 |
| 🗃️ **ER 图** | 数据库表设计、数据关系 |
| ⚙️ **状态机** | 实体生命周期、工作流状态 |
| 👤 **用例图** | 系统需求、角色权限 |
| 📊 **对比图** | A/B 评估、工具对比 |
| 📅 **时间线** | 项目里程碑、甘特图 |
| 🧠 **思维导图** | 头脑风暴、知识体系 |
| 🌐 **网络拓扑** | 基础设施、子网架构 |
| ➡️ **数据流图** | ETL 管道、数据处理 |
| 🤖 **Agent 架构** | AI 智能体、Memory 架构 |

## 🚀 快速开始

```bash
# 1. 安装 D2
winget install Terrastruct.D2              # Windows
curl -fsSL https://d2lang.com/install.sh | sh -s --   # macOS/Linux

# 2. 写个图
echo '用户 -> 网关 -> 服务A -> 数据库' > arch.d2

# 3. 出图
d2 arch.d2 arch.svg
```

### 在 Agent 中触发

直接在对话里说：
> "画个 OAuth2 序列图"
> "帮我画个微服务架构图"
> "用 D2 生成一个 CI/CD 流程图"
> "画个数据仓库 ETL 分层架构"
> "做个 D2 vs Mermaid 对比图"

## 📤 输出格式

```bash
d2 input.d2 output.svg       # 网页/文档/分享
d2 input.d2 output.png       # 微信/幻灯片/报告
d2 input.d2 output.pdf       # 打印/正式文档
d2 input.d2 output.pptx      # 演示文稿
d2 input.d2 output.gif       # 动图
d2 input.d2 output.txt       # ASCII 纯文本（微信聊天友好）
d2 input.d2 output.html      # 交互式 HTML（暗色模式 + 流动画 + 点击详情）
```

## 🎯 核心能力

| 能力 | 说明 |
|------|------|
| 🤖 **自动布局** | dagre/ELK 自动排版，告别手工对坐标 |
| 🎭 **22 主题** | 暗色/亮色/手绘/C4 架构/终端风格一键切换 |
| ✏️ **手绘风格** | `--sketch` 一键手绘质感 |
| 🖼️ **图标支持** | 内置 1000+ 图标库 |
| 📺 **Live Reload** | `--watch` 修改即预览 |
| 🏗️ **多场景** | layers/scenarios 一套图多视图 |
| 🔒 **纯本地** | 全离线运行，无数据泄露风险 |
| 🌐 **HTML 交互** | 自包含 HTML 图：暗色模式、流动画、点击节点详情、主题切换 |

## 🧩 融合来源

这个 Skill 吸收了四个前辈的最佳实践：

| 来源 | 吸收了什么 |
|------|------------|
| **[architecture-diagram](https://github.com/Cocoon-AI/architecture-diagram-generator)** (5.9K⭐) | 语义配色体系 + HTML 暗色包装模板 + Summary Cards |
| **excalidraw** (Hermes 自带) | `--sketch` 手绘美学 + 粉彩调色板 + 9 种图类型分类 |
| **[fireworks-tech-graph](https://www.npmjs.com/package/@yizhiyanhua-ai/fireworks-tech-graph)** (CC) | UML 全套覆盖 + 形状词汇 + 正式图类型定义 |
| **[design-system](https://github.com/Sunwood-ai-labs/draw-io-skill)** (CC) | 医疗暗色主题配色（科技蓝/健康绿/警告橙） |

## 📂 文件结构

```
d2-diagrams/
├── SKILL.md                    # Skill 主定义（含完整工作流）
├── README.md                   # 本文件（公共传播页）
├── references/
│   ├── d2-cheatsheet.md        # D2 语法速查
│   └── examples/               # 各类图的 D2 源文件
│       ├── architecture.d2     # 架构图示例
│       ├── flowchart.d2        # 流程图示例
│       └── sequence.d2         # 序列图示例
├── templates/
│   ├── architecture-wrapper.html  # SVG→HTML 暗色包装模板
│   └── html-diagram.html          # 交互式 HTML 图模板（暗色模式+流动画+点击详情）
└── test-prompts.json           # 验证测试用例
```

## 🛡️ 安全

- ✅ 全程本地运行，无外部 API 调用
- ✅ 不读取/上传任何用户数据
- ✅ 只写 `.d2` 文件和对应的输出文件
- ✅ 不会修改已有文件或系统设置

## ⚙️ 安装到你的 Agent

### Hermes（小马）
```bash
# 已自动安装到 skills/d2-diagrams/
```

### Claude Code
```bash
cp -r d2-diagrams/ ~/.claude/skills/
```

## 📝 License

MIT — 自由使用、修改、分发。

## 🙏 致谢

- [terrastruct/d2](https://github.com/terrastruct/d2) — 核心引擎
- [Cocoon-AI/architecture-diagram-generator](https://github.com/Cocoon-AI/architecture-diagram-generator) — 配色+HTML模板
- [yizhiyanhua-ai/fireworks-tech-graph](https://www.npmjs.com/package/@yizhiyanhua-ai/fireworks-tech-graph) — UML覆盖
