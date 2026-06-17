---
name: d2-diagrams
description: >-
  One skill to diagram them all. D2-powered: describe in text, get professional
  diagrams in SVG/PNG/PDF/PPTX/GIF/ASCII/HTML — with auto layout.
  Absorbs: architecture-diagram (semantic colors + HTML wrapper) + excalidraw (hand-drawn + pastel) + fireworks-tech-graph (UML) + effective-html (interactive HTML).

  TRIGGER on: 画图/架构图/流程图/序列图/类图/ER图/思维导图/时间线/网络拓扑/
  状态机/用例图/对比图/数据流图/可视化/拓扑图/示意图/
  architecture/flowchart/sequence diagram/class diagram/er diagram/
  timeline/mind map/uml/system diagram/network topology/
  create a diagram/draw diagram/generate diagram/data flow diagram/interactive diagram/full-screen diagram
version: 1.0.0
license: MIT
dependencies:
  - d2 (terrastruct/d2 v0.7.1+)
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [d2, diagram, architecture, flowchart, sequence, uml, er, timeline,
           mindmap, network, topology, visualization, text-to-diagram]
    related_skills: [architecture-diagram, excalidraw]
---

# D2 Diagrams — Universal Text-to-Diagram Skill

> **One skill to diagram them all.** D2-powered: describe in text, get professional
> diagrams in SVG/PNG/PDF/PPTX/GIF/ASCII/HTML — with auto layout.

Built on [terrastruct/d2](https://github.com/terrastruct/d2) (24.4K⭐).

| Source | What's absorbed |
|--------|----------------|
| **architecture-diagram** | Semantic color palette + HTML wrapper with Summary Cards + pulse animation + dark grid bg |
| **excalidraw / excalidraw-diagram-generator** | Hand-drawn aesthetics via `--sketch` + pastel palette + 9 diagram types |
| **fireworks-tech-graph** | Full UML coverage (class/use case/state machine/ER) + formal diagram types + shape vocabulary |
| **design-system** (CC) | Healthcare dark-theme palette (tech blue / health green / warning orange) |

## Quick Start

```bash
# 1. Verify D2 is installed
d2 version

# 2. Write your diagram
echo '用户 -> 网关 -> 服务A -> 数据库' > arch.d2

# 3. Generate
d2 arch.d2 arch.svg
start arch.svg   # Windows
open arch.svg    # macOS
```

## Output Formats

| Format | Command | Best For |
|--------|---------|----------|
| SVG | `d2 input.d2 output.svg` | Web, docs, sharing |
| PNG | `d2 input.d2 output.png` | WeChat, slides, reports |
| PDF | `d2 input.d2 output.pdf` | Print, formal docs |
| PPTX | `d2 input.d2 output.pptx` | Presentations |
| GIF | `d2 input.d2 output.gif` | Animated diagrams |
| ASCII | `d2 input.d2 output.txt` | WeChat inline, terminals |
| HTML | wrap SVG with architecture-wrapper.html | Dark-theme summary page |

## Workflow

### Step 1: Understand the Request
Determine: diagram type, core message, output format, style preference.

### Step 2: 🛑 CHECKPOINT · STOP — Choose Diagram Type

| Type | D2 Approach | Best For |
|------|-------------|----------|
| Architecture | Layer containers (client -> gateway -> services -> data) | System design |
| Flowchart | Sequential nodes + diamonds for decisions | Workflows, CI/CD |
| Sequence | Participants -> message arrows -> return arrows | API calls, protocols |
| Class (UML) | Class containers with attributes/methods | OOP, domain models |
| ER | Entity containers with key fields | Database schema |
| State Machine | State containers + transition arrows | Entity lifecycle |
| Use Case | `shape: person` + `shape: oval` | System requirements |
| Comparison | Column containers + feature checkmarks | A/B evaluations |
| Timeline | Time-ordered phases with milestones | Project planning |
| Mind Map | Nested containers from root | Brainstorming |
| Network Topology | `shape: cloud` + dashed subnets | Infrastructure |
| Data Flow | Source -> transform -> sink | ETL, data pipelines |
| Agent/Memory | Input -> reason -> tools -> memory -> output | AI architecture |

**🔴 CHECKPOINT · CONFIRM** — before generating:
1. Confirm diagram type with user (especially for complex diagrams)
2. Confirm output format (SVG for web, PNG for WeChat, etc.)
3. Confirm style preference (dark/light, hand-drawn, semantic colors)

### Step 3: Write D2 Source

```d2
vars: { d2-config: { layout-engine: dagre; theme-id: 0 } }
title: { label: "Title"; near: top-center; style.font-size: 24 }
layer1: {
  componentA: { style.fill: "#34d399" }
  componentB: { shape: cylinder; style.fill: "#a78bfa" }
}
layer1.componentA -> layer1.componentB: connects
```

### Step 4: Validate and Render

```bash
d2 validate input.d2
d2 input.d2 output.svg
d2 --theme=200 --sketch input.d2 output.svg   # dark + hand-drawn
d2 --watch input.d2 output.svg                 # live reload
```

### macOS Installation

```bash
brew install d2
d2 version  # verify
```

### Linux Installation

```bash
# Ubuntu/Debian via apt
sudo apt-get install d2
# Or via snap
sudo snap install d2 --classic
```

### Minimum Version

D2 v0.6.0+ required (2023-09 release). Older versions lack `--layout=elk` and some themes.

### Step 5: Optional HTML Wrapper (Architecture only)
1. Generate SVG, then load `templates/architecture-wrapper.html`
2. Replace `[SVG_CONTENT]` with the SVG markup
3. Fill in Summary Card titles and items

### Step 7: HTML Interactive Diagram (effective-html fusion)

When user wants a **full-screen interactive HTML diagram** (not just static SVG), generate a self-contained HTML file with:

**Core principles (from effective-html):**
- **Light on prose** — the diagram IS the content, not a page with a diagram
- **High-quality SVG** — hand-crafted SVG, not auto-generated
- **Dark mode** — CSS variables on `:root` / `html.dark`, theme toggle button, `localStorage` persistence
- **Apply-before-paint** — `<script>` in `<head>` to prevent flash of light mode
- **Flow animation** — clickable flow chips that highlight request paths with marching ants animation
- **Clickable nodes** — hover highlights, detail cards on click

**Workflow:**
1. Generate D2 source for the diagram structure
2. Render to SVG (or hand-write SVG for complex layouts)
3. Copy `templates/html-diagram.html` as base, replace placeholders:
   - `{title}` → diagram title
   - `{WIDTH}` / `{HEIGHT}` → SVG viewBox dimensions
   - `<!-- SVG diagram from D2 or hand-crafted -->` → actual SVG markup
   - Add flow chips for different scenarios
   - Add clickable nodes with detail cards
4. Save as `.html` file — fully self-contained, no external dependencies

---

## 🎯 End-to-End Example (完整示例)

Here's a complete workflow from D2 source to HTML deliverable:

**1. Write D2 source** (`arch.d2`):
```d2
vars: { d2-config: { layout-engine: dagre } }
title: { label: "用户服务架构图"; near: top-center; style.font-size: 24 }
frontend: 用户前端 { shape: hexagon; style.fill: "#22d3ee" }
gateway: API网关 { shape: hexagon; style.fill: "#fbbf24" }
users: 用户服务 { style.fill: "#34d399" }
orders: 订单服务 { style.fill: "#34d399" }
db: { shape: cylinder; style.fill: "#a78bfa" }
frontend -> gateway: HTTPS
gateway -> users: REST
gateway -> orders: REST
users -> db: SELECT
orders -> db: INSERT
```

**2. Render to SVG**:
```bash
d2 arch.d2 arch.svg
```

**3. Wrap in HTML** (optional, for architecture diagrams):
- Copy `templates/architecture-wrapper.html`
- Replace `[SVG_CONTENT]` with SVG markup
- Fill Summary Cards

**4. Or generate interactive HTML** (Step 7):
- Copy `templates/html-diagram.html`
- Replace placeholders
- Save as `arch.html`

---

## Diagram Type Details

### Architecture Diagram
- Layers: Client -> Gateway -> Services -> Data/Storage -> External
- `shape: cylinder` for databases, `shape: hexagon` for gateways
- Semantic colors: cyan=frontend, green=backend, violet=database, amber=cloud, rose=security
- Theme: `--theme=200` or `--theme=303` (C4)

```d2
展示层: { 前端: {shape: hexagon; style.fill: "#22d3ee"} }
业务层: { 用户服务: {style.fill: "#34d399"} }
数据层: { DB: {shape: cylinder; style.fill: "#a78bfa"} }
展示层.前端 -> 业务层.用户服务 -> 数据层.DB
```

### Flowchart
- `shape: oval` for start/end, `shape: diamond` for decisions
- Pastel fills work well with `--sketch`

```d2
开始: {shape: oval; style.fill: "#22c55e"}
决策: {shape: diamond; style.fill: "#fff3bf"}
通过: {style.fill: "#b2f2bb"}
不通过: {style.fill: "#ffc9c9"}
开始 -> 决策
决策 -> 通过: yes {style.stroke: "#22c55e"}
决策 -> 不通过: no {style.stroke: "#ef4444"}
```

### Sequence Diagram (D2 auto-layout works great)
```d2
用户 -> 服务: POST /api
服务 -> 数据库: SELECT
数据库 -> 服务: result {style.stroke-dash: 3}
服务 -> 用户: 200 OK {style.stroke-dash: 3}
```

### Data Flow
- Use layered containers for tiers: Source → Transform → Sink
- Use `style.stroke-dash: 3` for async/buffered flows
- Use `style.fill` to distinguish data states

```d2
source: { shape: cylinder; style.fill: "#22d3ee"; label: "数据源" }
etl: ETL处理 { style.fill: "#34d399" }
warehouse: 数据仓库 { shape: cylinder; style.fill: "#a78bfa" }
bi: BI展示 { shape: hexagon; style.fill: "#fbbf24" }
source -> etl: 采集 {style.stroke-dash: 3}
etl -> warehouse: 加载
warehouse -> bi: 查询
```

### Agent/Memory
- Input -> reason -> tools -> memory -> output
- Use containers for each agent phase

### State Machine (detailed)
- States: containers with `shape: rounded_rect`
- Transitions: labeled arrows with conditions
- Use `near:` to position transitions

```d2
vars: { d2-config: { layout-engine: elk } }
建档: { shape: rounded_rect; style.fill: "#22d3ee" }
随访: { shape: rounded_rect; style.fill: "#34d399" }
评估: { shape: rounded_rect; style.fill: "#fbbf24" }
干预: { shape: rounded_rect; style.fill: "#a78bfa" }
复查: { shape: rounded_rect; style.fill: "#fb7185" }
建档 -> 随访: 患者注册
随访 -> 评估: 数据收集
评估 -> 干预: 风险分级
干预 -> 复查: 制定方案
复查 -> 随访: 指标达标
```

### Use Case Diagram (UML)
```d2
actor: {shape: person}
系统边界: {style.stroke-dash: 4
  创建订单: {shape: oval}
  支付: {shape: oval}
}
actor -> 系统边界.创建订单
actor -> 系统边界.支付
```

### Comparison / Feature Matrix
```d2
特征: { 自动布局: {}; 多格式: {}; 手绘风: {} }
D2: { 自动布局: {style.fill: "#22c55e"}; 多格式: {style.fill: "#22c55e"} }
Mermaid: { 自动布局: {style.fill: "#22c55e"}; 多格式: {style.fill: "#22c55e"} }
```

---

## Color Themes

### Built-in D2 Themes
Light: 0=Neutral, 1=Neutral Grey, 3=Flagship, 4=Cool Classics, 8=Colorblind,
100=Vanilla Nitro, 103=Earth Tones, 104=Everglade Green, 300=Terminal,
301=Terminal Grey, 302=Origami, 303=C4 (arch), 105=Buttered Toast
Dark: 200=Dark Mauve, 201=Dark Flagship

### Semantic Color Palette (Architecture)

| Component | Fill | Stroke |
|-----------|------|--------|
| Frontend | rgba(8,51,68,0.4) | #22d3ee |
| Backend | rgba(6,78,59,0.4) | #34d399 |
| Database | rgba(76,29,149,0.4) | #a78bfa |
| Cloud/AWS | rgba(120,53,15,0.3) | #fbbf24 |
| Security | rgba(136,19,55,0.4) | #fb7185 |
| Message Bus | rgba(251,146,60,0.3) | #fb923c |
| External | rgba(30,41,59,0.5) | #94a3b8 |

### Pastel Palette (Whiteboard / `--sketch` mode)

| Use | Fill | Hex |
|-----|------|-----|
| Input / Source | Light Blue | #a5d8ff |
| Success / Output | Light Green | #b2f2bb |
| Warning / External | Light Orange | #ffd8a8 |
| Processing | Light Purple | #d0bfff |
| Error / Critical | Light Red | #ffc9c9 |
| Notes / Decisions | Light Yellow | #fff3bf |
| Storage / Data | Light Teal | #c3fae8 |

### Healthcare Dark Theme (for medical dashboards)

```d2
vars: { d2-config: { theme-id: 200 } }
db: { style.fill: "#1e3a5f"; style.stroke: "#00d4ff"; style.font-color: "#e5e5e5" }
```

| Semantic | Hex |
|----------|-----|
| Primary / Tech | #00d4ff |
| Success / Normal | #10b981 |
| Warning | #f59e0b |
| Danger / Critical | #ef4444 |
| Info / Link | #06b6d4 |
| Special | #a855f7 |
| BG Primary | #0a0e17 |

---

## Shape Vocabulary

| Concept | D2 Shape |
|---------|----------|
| Service | `{}` (default) |
| Database | `{shape: cylinder}` |
| User | `{shape: person}` |
| Decision | `{shape: diamond}` |
| Terminal | `{shape: oval}` |
| Gateway | `{shape: hexagon}` |
| Cloud | `{shape: cloud}` |
| Document | `{shape: page}` |
| Storage | `{shape: stored_data}` |
| Multi-items | `style.multiple: true` |

## Styling

```d2
node: {
  style.fill: "#22d3ee"
  style.stroke: "#0284c7"
  style.stroke-width: 2
  style.stroke-dash: 4       # dashed border
  style.font-color: "#fff"
  style.font-size: 14
  style.bold: true
  style.rounded: true
  style.shadow: true
  style.multiple: true       # stacked items
  width: 200; height: 80
}
```

## Arrow Styles

| Style | Syntax |
|-------|--------|
| Solid | `A -> B` |
| Dashed | `A -> B {style.stroke-dash: 3}` |
| Labeled | `A -> B: label` |
| Bold | `A -> B {style.stroke-width: 3}` |
| Bi-directional | `A <-> B` |

## Icons
```d2
db: { icon: https://icons.terrastruct.com/tech/database.svg; label: "MySQL" }
```

## Multi-Environment (Layers / Scenarios)
```d2
场景: { 开发: { srv: "dev-api" }; 生产: { srv: "prod-api" } }
```
Render specific: `d2 --target='scenarios.生产' input.d2 output.svg`

## Animated SVG
```bash
d2 --animate-interval=3000 input.d2 output.svg
```

---

## ⚠️ Failure Modes & Troubleshooting

### D2 not found
```bash
# Install on Windows
winget install Terrastruct.D2

# Install on macOS/Linux
curl -fsSL https://d2lang.com/install.sh | sh -s --

# Verify
d2 version   # should print v0.6.0+
```

### Windows path issues (git-bash)
**Problem:** `/tmp/file.d2` maps to `C:\tmp\file.d2` which d2.exe can't see.
**Fix:** Use Windows absolue paths with single quotes:
```bash
d2 'C:\Users\you\diagram.d2' out.svg
# OR use MSYS path that maps correctly
d2 '/c/Users/you/diagram.d2' out.svg
```

### D2 syntax error
```bash
# Validate first
d2 validate input.d2

# Common D2 syntax mistakes:
# - Missing closing brace: `layer: { node` → should be `layer: { node }`
# - Invalid shape name: `{shape: box}` → should be `{shape: hexagon}`
# - Layer ref with missing dot: `layer1node -> layer2node` → `layer1.node -> layer2.node`
# - Style on wrong level: put styles INSIDE the node, not outside
```

### Layout looks wrong (overlapping, cramped)
```bash
# Try different layout
d2 --layout=elk input.d2 output.svg

# Increase padding
d2 --pad=200 input.d2 output.svg

# Check if dagre works better (default)
```

### Container connections not appearing
```bash
# Use parent.child syntax, not just child name
containerA.service1 -> containerB.service2: correct✅
service1 -> service2: wrong❌ (D2 can't find them)
```

### Theme not applying
```bash
# Theme IDs must be set in the vars block OR via CLI
d2 --theme-id=200 input.d2 output.svg

# Not all themes work with --sketch
```

### PNG export fails
```bash
# D2 needs Chromium for PNG (auto-downloads on first use)
# If stuck, try SVG instead
d2 input.d2 output.svg
# Then convert SVG -> PNG manually
```

### Large SVG files (>5MB)
Large D2 diagrams with many nodes produce huge SVGs. When embedding in HTML:
- **Limit**: Keep under 5MB SVG for smooth browser rendering
- **Workaround**: Use `d2 --pad 40` to reduce spacing, or split into multiple diagrams
- **Alternative**: Export as PNG instead for smaller file size

### PDF/PPTX/GIF fail
These formats require more system resources. Try SVG first:
```bash
d2 input.d2 output.svg
```

---

## 🛡️ Safety & Boundary

### What this skill WILL do:
- Write `.d2` files to disk in the working directory
- Run `d2.exe` CLI commands to generate diagrams
- Accept user-provided text for diagram content
- Render to multiple output formats via D2 CLI

### What this skill will NOT do:
- ❌ Delete or modify files outside the skill's output
- ❌ Send data to external servers (D2 runs entirely locally)
- ❌ Execute arbitrary shell commands (only `d2` subcommands)
- ❌ Access private data or credentials
- ❌ Modify system settings

### 🛑 CHECKPOINT · STOP — When to ask the user:
1. **🔴 Output format requires unavailable tool** (e.g. PNG needs Chromium)
2. **🔴 D2 CLI not installed** — confirm with user before guiding installation
3. **🔴 Request unclear** — user request doesn't clearly map to a supported diagram type
4. **🛑 Large diagram (>20 nodes)** — confirm splitting strategy

---

## 🚫 Anti-Patterns (When NOT to use this skill)

| Scenario | Why NOT | Use instead |
|----------|---------|-------------|
| **20+ complex data flows** | D2 gets messy with cross-connections | **纯CSS/HTML手写** (see `references/css-handwritten-diagrams.md`) |
| **Need large readable text** | D2 default font small & grey | **PureCSS** (see `references/css-handwritten-diagrams.md`) |
| Animated charts/graphs | D2 outputs static SVG/PNG | p5js, manim-video |
| Bar/line/pie charts | D2 not a charting library | officecli-chart-colors (Excel) |
| Photo-realistic diagrams | D2 is vector diagrams | comfyui, canvas-design |
| Complex 3D rendering | D2 is 2D only | manim-video, p5js |
| Editing existing draw.io files | D2 has different format | drawio skill |
| Simple text annotation | Overkill for one label | Just type it |
| Database ERD from live schema | D2 can't reverse-engineer | sqlkg (SQL parsing) |
| Data visualization dashboards | D2 is static diagrams | officecli-data-dashboard |

---

## Windows (git-bash) Notes
- D2 `.exe` in `~/bin/` (Hermes) AND `~/AppData/Roaming/npm/` (Claude Code)
- Use Windows absolute paths: `d2.exe "C:\\path\\to\\file.d2" out.svg`
- `/tmp/file.d2` (C:\\tmp\\file.d2) not seen by d2.exe — use explicit path
- Install: `winget install Terrastruct.D2` or download via ghproxy
