#!/usr/bin/env python3
"""
D2 SVG → Archify HTML 转换器

将 D2 生成的 SVG 文件转换为包含暗色/亮色切换和导出功能的单文件 HTML。

用法:
    python d2_to_archify.py input.svg output.html "标题" "副标题"

作为库调用:
    from d2_to_archify import render_archify_html
    
    html = render_archify_html(
        svg_content='<svg>...</svg>',
        title="架构图",
        subtitle="系统架构说明",
        cards=[
            {'title': '架构', 'items': ['三层设计', 'REST API']},
        ]
    )
"""

import sys
import os
from pathlib import Path


def render_archify_html(svg_content: str, title: str = "Diagram", subtitle: str = "", 
                       cards: list = None) -> str:
    """
    将 SVG 内容包裹在 Archify 风格的 HTML 模板中。
    
    Args:
        svg_content: SVG 文件内容字符串
        title: 图表标题
        subtitle: 副标题
        cards: 信息卡片列表，每项包含 'title' 和 'items'
    
    Returns:
        完整的 HTML 字符串
    """
    if cards is None:
        cards = []
    
    # 信息卡片 HTML
    cards_html = ""
    for card in cards:
        items_html = "".join(f"<li>{item}</li>" for item in card.get('items', []))
        cards_html += f'<div class="card"><h3>{card["title"]}</h3><ul>{items_html}</ul></div>'
    
    if not cards_html:
        cards_html = '<div class="card"><h3>说明</h3><ul><li>双击导出</li></ul></div>'
    
    # 转义 SVG 内容（处理引号等）
    escaped_svg = svg_content.replace('<!--', '&lt;!--').replace('-->', '--&gt;')
    
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>
:root {{
  --bg: #ffffff;
  --fg: #1a1a2e;
  --card-bg: #f8f9fa;
  --border: #e9ecef;
}}
[data-theme="dark"] {{
  --bg: #0a0e17;
  --fg: #e5e5e5;
  --card-bg: #1a1e2e;
  --border: #2d3748;
}}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  background: var(--bg);
  color: var(--fg);
  transition: background 0.3s, color 0.3s;
}}
.toolbar {{
  position: fixed;
  top: 10px;
  right: 10px;
  display: flex;
  gap: 8px;
  z-index: 100;
}}
.btn {{
  padding: 8px 16px;
  border: 1px solid var(--border);
  background: var(--card-bg);
  color: var(--fg);
  border-radius: 6px;
  cursor: pointer;
  font-size: 14px;
  transition: opacity 0.2s;
}}
.btn:hover {{ opacity: 0.8; }}
.diagram-container {{
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px 20px;
}}
.diagram-container svg {{
  max-width: 100%;
  height: auto;
}}
.cards {{
  position: fixed;
  bottom: 10px;
  left: 10px;
  display: flex;
  gap: 10px;
  z-index: 100;
}}
.card {{
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 12px;
  max-width: 200px;
}}
.card h3 {{
  font-size: 14px;
  margin-bottom: 8px;
  border-bottom: 1px solid var(--border);
  padding-bottom: 4px;
}}
.card ul {{
  list-style: none;
  font-size: 12px;
}}
.card li {{
  padding: 2px 0;
}}
@media print {{
  .toolbar, .cards {{ display: none; }}
  body {{ background: white; }}
}}
</style>
<script>
(function(){{
  var t = localStorage.getItem('theme');
  if(t === 'dark' || (!t && matchMedia('(prefers-color-scheme:dark)').matches)) {{
    document.documentElement.setAttribute('data-theme', 'dark');
  }}
}})();
</script>
</head>
<body>
<div class="toolbar">
  <button class="btn" onclick="toggleTheme()">🌙 深色 / ☀️ 浅色</button>
  <button class="btn" onclick="exportSVG()">📷 导出 SVG</button>
</div>
<div class="diagram-container">
  {escaped_svg}
</div>
<div class="cards">
  {cards_html}
</div>
<script>
function toggleTheme() {{
  var html = document.documentElement;
  var current = html.getAttribute('data-theme');
  var next = current === 'dark' ? 'light' : 'dark';
  html.setAttribute('data-theme', next);
  localStorage.setItem('theme', next);
}}
function exportSVG() {{
  var svg = document.querySelector('.diagram-container svg');
  if(!svg) return;
  var serializer = new XMLSerializer();
  var source = serializer.serializeToString(svg);
  var blob = new Blob([source], {{type: 'image/svg+xml;charset=utf-8'}});
  var url = URL.createObjectURL(blob);
  var a = document.createElement('a');
  a.href = url;
  var filename = '{title}'.replace(/[^a-zA-Z0-9\u4e00-\u9fa5]/g, '_') + '.svg';
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}}
</script>
</body>
</html>"""
    
    return html


def main():
    if len(sys.argv) < 3:
        print("用法: python d2_to_archify.py input.svg output.html [标题] [副标题]")
        print("示例: python d2_to_archify.py arch.svg arch.html '微服务架构' 'V1.0'")
        sys.exit(1)
    
    input_svg = sys.argv[1]
    output_html = sys.argv[2]
    title = sys.argv[3] if len(sys.argv) > 3 else "Diagram"
    subtitle = sys.argv[4] if len(sys.argv) > 4 else ""
    
    if not os.path.exists(input_svg):
        print(f"错误: 文件不存在 {input_svg}")
        sys.exit(1)
    
    with open(input_svg, 'r', encoding='utf-8') as f:
        svg_content = f.read()
    
    html = render_archify_html(svg_content, title=title, subtitle=subtitle)
    
    with open(output_html, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ 已生成 {output_html} ({len(html):,} bytes)")


if __name__ == '__main__':
    main()
