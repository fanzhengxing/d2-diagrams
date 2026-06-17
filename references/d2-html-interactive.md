# D2 → Interactive HTML 交互架构图

将 D2 渲染的 SVG 包裹成自包含 HTML 页面，支持深色主题、图层筛选、缩放拖拽、悬浮提示。

## 流程

1. 写 D2 源文件 → 2. `d2 validate` 验证 → 3. `d2 input.d2 output.svg` 渲染 → 4. 读取 SVG 内容 → 5. 包裹进 HTML 模板

## HTML 模板关键要求

### 模板位置

`templates/architecture-wrapper.html` — **已升级为邢台风格**（深色科技风、大字体、网格背景）

### SVG 尺寸问题（必读）

D2 生成的 SVG 内嵌子 SVG 可能有 `viewBox="-161 -172 2706 2274"` 的偏移，需要：

```css
/* SVG wrapper 自适应 */
.svg-wrapper svg {
  display: block;
  width: 100%;
  height: 100%;
}
```

### 关键修复：fill-N7 背景覆盖

D2 深色主题会在 SVG 根 `<rect>` 上设置 `fill="#1E1E2E"`（class `fill-N7`）。**必须用 `!important` 覆盖为透明**，否则会遮挡外层深色背景：

```css
.svg-wrapper svg .fill-N7 {
  fill: transparent !important;
}
```

### 核心交互功能

| 功能 | 实现 |
|------|------|
| **缩放** | 滚轮缩放（以鼠标位置为中心）、按钮缩放、键盘`+/-` |
| **拖拽平移** | 鼠标按下拖拽，`mousedown/move/up` 事件 |
| **适应窗口** | `fitView()` 自动计算最佳缩放比例 |
| **图层筛选** | 按 SVG `fill` 属性中的 hex 色匹配节点，非目标层 `opacity: 0.15` |
| **悬浮提示** | 监听 SVG 节点 → 鼠标移入显示 title/desc |
| **键盘快捷** | `+/−` 缩放，`0` 重置，`f` 适应窗口，`L` 图层面板，`Esc` 关闭提示 |
| **主题切换** | 深色/浅色模式切换，保留当前缩放和平移状态 |

### 图层颜色映射参考

| 层 | 主色 | D2 fill 特征 |
|----|------|-------------|
| 前端 | #22d3ee (Cyan) | `cffafe` / `22d3ee` |
| 网关 | #06b6d4 / #fb7185 | `ecfeff` / `fef2f2` |
| 服务 | #34d399 (Emerald) | `ecfdf5` |
| 数据库 | #a78bfa (Violet) | `f5f3ff` |
| 外部 | #fbbf24 (Amber) | `fef3c7` |
| 消息 | #fb923c (Orange) | `ffedd5` |
| 安全 | #fb7185 (Rose) | `fff1f2` |

JS 筛选逻辑按这些 hex 色片段匹配 SVG fill 属性。

## Python 打包脚本

用 Python 读取 SVG 文件内容并拼接 HTML（避免 shell 引号问题）：

```python
with open('output.svg', 'r') as f:
    svg = f.read()

html_template = open('templates/architecture-wrapper.html', 'r').read()
html = html_template.replace('[SVG_CONTENT]', svg)
html = html.replace('[架构图标题]', '项目名称')
html = html.replace('[副标题/描述]', '简短描述')
html = html.replace('[项目名称]', '项目名')
html = html.replace('[日期]', '2026-06-17')

with open('output.html', 'w') as f:
    f.write(html)
```

**注意**：shell 内联 python 长字符串容易引号冲突，**务必用 `write_file` 写脚本文件再执行**。

## 完整参考

邯郸基层医疗平台架构图：
- D2 源文件: `health_platform_arch.d2`
- 输出 SVG: `health_platform_arch_dark.svg` (用 `--theme=200` 深色)
- 交互 HTML: `health_platform_arch.html`

## 注意事项

1. **D2 深色主题背景**：渲染时用 `--theme=200` 生成深色 SVG，HTML 模板也是深色背景，两者颜色可能不完全一致，`fill-N7` 覆盖是关键修复
2. **SVG viewBox 偏移**：D2 生成的 SVG 可能有负值 viewBox，HTML 模板中的 `.transform-container` + CSS transform 可以正确处理
3. **字体大小**：D2 默认字体较小（10-12px），如果需要在 HTML 中放大，可以在 SVG 内容注入后用 JS 遍历修改 `font-size` 属性
4. **大图性能**：如果 SVG 节点超过 500 个，图层筛选可能会卡顿，建议先用 D2 精简节点数量
