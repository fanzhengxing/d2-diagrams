import re

with open('claude-code-arch.svg', 'r', encoding='utf-8') as f:
    svg = f.read()

# D2 outer SVG has viewBox but no width/height — add them so the holder gets dimensions
# Extract viewBox from outer SVG tag: viewBox="0 0 W H"
m = re.search(r'<svg[^>]*viewBox="0 0 (\d+) (\d+)"', svg)
SVG_W, SVG_H = (int(m.group(1)), int(m.group(2))) if m else (1617, 3160)

# Inject width/height into first <svg> tag if missing
svg = re.sub(
    r'(<svg\b)([^>]*viewBox="0 0 \d+ \d+")',
    lambda mo: mo.group(1) + f' width="{SVG_W}" height="{SVG_H}"' + mo.group(2),
    svg, count=1
)

html = '''<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Claude Code Architecture</title>
<script>
  (function(){
    var s=localStorage.getItem('cc-arch-theme');
    var d=s?s==='dark':matchMedia('(prefers-color-scheme:dark)').matches;
    document.documentElement.classList.toggle('dark',d);
  })();
</script>
<style>
  :root {
    --bg: #f8fafc;
    --surface: #ffffff;
    --ink: #0f172a;
    --body: #334155;
    --muted: #94a3b8;
    --line: #e2e8f0;
    --accent: #0ea5e9;
    --accent-soft: rgba(14,165,233,0.10);
  }
  html.dark {
    --bg: #0f172a;
    --surface: #1e293b;
    --ink: #f1f5f9;
    --body: #cbd5e1;
    --muted: #64748b;
    --line: #334155;
    --accent: #38bdf8;
    --accent-soft: rgba(56,189,248,0.12);
  }
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    background: var(--bg);
    color: var(--body);
    font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
    display: flex;
    flex-direction: column;
    height: 100vh;
    overflow: hidden;
  }

  /* ── Top bar ─────────────────────────────────────────────── */
  .topbar {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 10px 20px;
    border-bottom: 1px solid var(--line);
    background: var(--surface);
    flex-shrink: 0;
    z-index: 10;
  }
  .topbar h1 {
    font-size: 16px;
    font-weight: 600;
    color: var(--ink);
    letter-spacing: -0.01em;
  }
  .topbar .subtitle {
    font-size: 12px;
    color: var(--muted);
  }
  .spacer { flex: 1; }

  /* ── Chips (flow filters) ────────────────────────────────── */
  .chips { display: flex; gap: 6px; align-items: center; }
  .chip {
    font-size: 11px;
    font-family: ui-monospace, "SF Mono", Menlo, monospace;
    padding: 4px 10px;
    border: 1px solid var(--line);
    border-radius: 999px;
    background: transparent;
    color: var(--muted);
    cursor: pointer;
    transition: all .15s;
    white-space: nowrap;
  }
  .chip:hover { border-color: var(--accent); color: var(--accent); }
  .chip.on {
    background: var(--accent);
    border-color: var(--accent);
    color: #fff;
  }

  /* ── Theme toggle ────────────────────────────────────────── */
  .theme-btn {
    font-size: 11px;
    padding: 4px 10px;
    border: 1px solid var(--line);
    border-radius: 6px;
    background: transparent;
    color: var(--muted);
    cursor: pointer;
  }
  .theme-btn:hover { border-color: var(--muted); }

  /* ── Zoom controls ───────────────────────────────────────── */
  .zoom-controls {
    display: flex;
    gap: 4px;
    align-items: center;
  }
  .zoom-btn {
    width: 26px; height: 26px;
    border: 1px solid var(--line);
    border-radius: 5px;
    background: transparent;
    color: var(--body);
    cursor: pointer;
    font-size: 14px;
    display: flex; align-items: center; justify-content: center;
  }
  .zoom-btn:hover { background: var(--accent-soft); }
  .zoom-label {
    font-size: 11px;
    color: var(--muted);
    min-width: 36px;
    text-align: center;
    font-family: ui-monospace, monospace;
  }

  /* ── Diagram stage ───────────────────────────────────────── */
  .stage {
    flex: 1;
    overflow: hidden;
    position: relative;
    cursor: grab;
  }
  .stage.dragging { cursor: grabbing; }

  .transform-wrap {
    position: absolute;
    top: 0; left: 0;
    transform-origin: 0 0;
    will-change: transform;
  }

  .svg-holder {
    display: block;
    line-height: 0;
  }
  /* Fix D2 dark-bg rect covering everything */
  .svg-holder svg .fill-N7 { fill: transparent !important; }
  /* In dark mode, invert light fills for readability */
  html.dark .svg-holder { filter: none; }

  /* ── Layer highlight ─────────────────────────────────────── */
  .layer-dim .d2-svg [class*="fill-"] { opacity: 0.15 !important; }
  .layer-dim .d2-svg .layer-on { opacity: 1 !important; }

  /* ── Detail card ─────────────────────────────────────────── */
  #detail-card {
    position: fixed;
    right: 20px;
    bottom: 20px;
    width: 300px;
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 12px;
    padding: 16px;
    box-shadow: 0 8px 32px rgba(0,0,0,.12);
    display: none;
    z-index: 100;
  }
  #detail-card h3 { font-size: 15px; color: var(--ink); margin-bottom: 6px; }
  #detail-card p { font-size: 12.5px; line-height: 1.6; color: var(--body); }
  .card-close {
    position: absolute;
    top: 10px; right: 12px;
    background: none; border: none;
    font-size: 16px; color: var(--muted);
    cursor: pointer; line-height: 1;
  }
  .card-close:hover { color: var(--ink); }

  /* ── Legend ──────────────────────────────────────────────── */
  .legend {
    display: flex;
    gap: 14px;
    align-items: center;
    padding: 6px 20px;
    border-top: 1px solid var(--line);
    background: var(--surface);
    flex-shrink: 0;
    flex-wrap: wrap;
  }
  .legend-item {
    display: flex;
    align-items: center;
    gap: 5px;
    font-size: 11px;
    color: var(--muted);
  }
  .legend-dot {
    width: 10px; height: 10px;
    border-radius: 2px;
    flex-shrink: 0;
  }
</style>
</head>
<body>

<div class="topbar">
  <div>
    <h1>Claude Code — Architecture Overview</h1>
    <div class="subtitle">5-layer architecture · built on terrastruct/d2</div>
  </div>
  <div class="spacer"></div>
  <div class="chips">
    <span style="font-size:11px;color:var(--muted);margin-right:2px;">Highlight:</span>
    <button class="chip on" data-layer="all">All Layers</button>
    <button class="chip" data-layer="user">User Interface</button>
    <button class="chip" data-layer="cli">CLI / REPL</button>
    <button class="chip" data-layer="agent">Agent Core</button>
    <button class="chip" data-layer="tools">Tools</button>
    <button class="chip" data-layer="external">External</button>
  </div>
  <div class="zoom-controls">
    <button class="zoom-btn" id="zoom-out">−</button>
    <span class="zoom-label" id="zoom-label">100%</span>
    <button class="zoom-btn" id="zoom-in">+</button>
    <button class="zoom-btn" id="zoom-fit" title="Fit to window">⊡</button>
  </div>
  <button class="theme-btn" id="theme-toggle">🌙 Dark</button>
</div>

<div class="stage" id="stage">
  <div class="transform-wrap" id="transform-wrap">
    <div class="svg-holder" id="svg-holder">
SVG_PLACEHOLDER
    </div>
  </div>
</div>

<div class="legend">
  <div class="legend-item"><div class="legend-dot" style="background:#22d3ee"></div>User Interface</div>
  <div class="legend-item"><div class="legend-dot" style="background:#fb923c"></div>CLI / REPL</div>
  <div class="legend-item"><div class="legend-dot" style="background:#34d399"></div>Agent Core</div>
  <div class="legend-item"><div class="legend-dot" style="background:#a78bfa"></div>Built-in Tools</div>
  <div class="legend-item"><div class="legend-dot" style="background:#fbbf24"></div>External Services</div>
  <div class="legend-item" style="margin-left:auto;font-size:11px;color:var(--muted)">Scroll to zoom · Drag to pan · Click node for details</div>
</div>

<div id="detail-card">
  <button class="card-close" id="card-close">×</button>
  <h3 id="card-title"></h3>
  <p id="card-body"></p>
</div>

<script>
// ── Node descriptions ───────────────────────────────────────────────
var NODE_INFO = {
  'Terminal': { desc: 'Primary CLI entry point. Users run `claude` in any terminal. Supports interactive REPL and one-shot commands (-p flag).' },
  'VS Code\\nExtension': { desc: 'IDE integration via Language Server Protocol bridge. Inline diff previews, keyboard shortcuts, and sidebar panel.' },
  'JetBrains\\nPlugin': { desc: 'IntelliJ-family IDE plugin (IDEA, PyCharm, WebStorm). Same LSP bridge as VS Code.' },
  'Web App\\n(claude.ai/code)': { desc: 'Browser-based interface at claude.ai/code. Communicates via WebSocket to the same Claude Code backend.' },
  'REPL\\n(interactive loop)': { desc: 'Read-Eval-Print Loop that drives each conversation turn. Manages prompt submission, tool approval UX, and streaming output rendering.' },
  'Slash Commands\\n(/help /clear /plan)': { desc: 'Built-in commands: /help, /clear, /plan, /review, /compact, /doctor, /config, etc. Invoked inline during conversation.' },
  'Skills System\\n(~/.claude/skills/)': { desc: 'Markdown-based skill files loaded as system context. Each skill provides domain knowledge, workflows, and tool guidance.' },
  'Hooks\\n(settings.json)': { desc: 'Shell commands that fire on events: PreToolUse, PostToolUse, Stop, SessionStart. Configured in .claude/settings.json.' },
  'Memory System\\n(CLAUDE.md / .md files)': { desc: 'Persistent context files: CLAUDE.md (project instructions), ~/.claude/CLAUDE.md (global), rules/*.md, and project memory files.' },
  'Main Loop\\n(turn-based)': { desc: 'Central orchestrator. Sends messages to Anthropic API, receives tool calls, dispatches to Tool Executor, loops until no more tool calls.' },
  'Context Manager\\n(compression / inject)': { desc: 'Manages the context window: injects CLAUDE.md / memory files, triggers auto-compression when context approaches limits.' },
  'Tool Executor\\n(permission check)': { desc: 'Validates each tool call against permission settings. Prompts user for approval if the tool is not pre-allowed. Runs hooks before/after execution.' },
  'Plan Mode\\n(EnterPlanMode)': { desc: 'Switches to read-only planning mode. Claude explores the codebase and writes a plan file for user approval before executing changes.' },
  'Sub-Agent Manager\\n(Agent / Workflow)': { desc: 'Spawns parallel sub-agents via the Agent tool or Workflow scripts. Manages concurrency cap (min(16, cpu-2)), result collection, and background tasks.' },
  'File Tools\\n(Read/Write/Edit/Glob)': { desc: 'Read: cat-n format with line numbers. Write: full file overwrite. Edit: exact string replacement (requires prior Read). Glob: pattern file search.' },
  'Bash Tool\\n(shell execution)': { desc: 'Runs shell commands in git-bash. Persists working directory between calls. Timeout up to 10 min. Sandboxed by permission settings.' },
  'Search Tools\\n(Grep / WebSearch)': { desc: 'Grep: ripgrep-backed content search with regex, file type filters, context lines. WebSearch: live web search for current information.' },
  'Browser Tools\\n(Playwright MCP)': { desc: 'Full browser automation via Playwright MCP. Supports navigate, click, type, screenshot, network inspection, and JS evaluation.' },
  'Task Tools\\n(TaskCreate/Update)': { desc: 'In-session task list management. TaskCreate, TaskUpdate (status/owner/deps), TaskList, TaskGet. Visible to user as a progress tracker.' },
  'MCP Servers\\n(plugin ecosystem)': { desc: 'Model Context Protocol servers extend Claude with custom tools. Configured in .claude/settings.json mcpServers. Examples: claude-mem, fetch, playwright.' },
  'Anthropic API\\n(Messages API)': { desc: 'POST /v1/messages endpoint. Supports streaming (SSE), tool_use content blocks, vision, extended thinking, and prompt caching.' },
  'Claude Models\\n(Opus/Sonnet/Haiku)': { desc: 'Model family: claude-opus-4-8 (most capable), claude-sonnet-4-6 (balanced), claude-haiku-4-5 (fast). Routed by model ID in API requests.' },
  'GitHub\\n(gh CLI / PRs)': { desc: 'GitHub CLI integration for PR creation, issue management, CI checks, and code review. Accessed via `gh` commands through the Bash tool.' },
  'Web Services\\n(WebFetch / WebSearch)': { desc: 'External HTTP services. WebFetch converts HTML to markdown for LLM consumption. WebSearch provides live search results with citations.' },
};

// ── Layer color keywords (match D2 fill hex fragments) ──────────────
var LAYER_COLORS = {
  user:     ['cffafe', 'ecfeff'],
  cli:      ['ffedd5', 'fff7ed'],
  agent:    ['d1fae5', 'f0fdf4'],
  tools:    ['ede9fe', 'f5f3ff'],
  external: ['fef3c7', 'fffbeb'],
};

// ── Transform state ──────────────────────────────────────────────────
var scale = 1;
var tx = 0, ty = 0;
var isDragging = false;
var dragStartX, dragStartY, dragTx, dragTy;
var wrap = document.getElementById('transform-wrap');
var stage = document.getElementById('stage');

function applyTransform() {
  wrap.style.transform = 'translate(' + tx + 'px,' + ty + 'px) scale(' + scale + ')';
  document.getElementById('zoom-label').textContent = Math.round(scale * 100) + '%';
}

var SVG_W = __SVG_W__;
var SVG_H = __SVG_H__;

function fitView() {
  var stageW = stage.clientWidth;
  var stageH = stage.clientHeight;
  if (!stageW || !stageH) return;
  var s = Math.min(stageW / SVG_W, stageH / SVG_H) * 0.92;
  scale = s;
  tx = (stageW - SVG_W * s) / 2;
  ty = Math.max(10, (stageH - SVG_H * s) / 2);
  applyTransform();
}

// Scroll to zoom
stage.addEventListener('wheel', function(e) {
  e.preventDefault();
  var rect = stage.getBoundingClientRect();
  var mx = e.clientX - rect.left;
  var my = e.clientY - rect.top;
  var delta = e.deltaY > 0 ? 0.9 : 1.1;
  var newScale = Math.max(0.15, Math.min(5, scale * delta));
  tx = mx - (mx - tx) * (newScale / scale);
  ty = my - (my - ty) * (newScale / scale);
  scale = newScale;
  applyTransform();
}, { passive: false });

// Drag to pan
stage.addEventListener('mousedown', function(e) {
  if (e.button !== 0) return;
  isDragging = true;
  dragStartX = e.clientX; dragStartY = e.clientY;
  dragTx = tx; dragTy = ty;
  stage.classList.add('dragging');
});
window.addEventListener('mousemove', function(e) {
  if (!isDragging) return;
  tx = dragTx + (e.clientX - dragStartX);
  ty = dragTy + (e.clientY - dragStartY);
  applyTransform();
});
window.addEventListener('mouseup', function() {
  isDragging = false;
  stage.classList.remove('dragging');
});

// Zoom buttons
document.getElementById('zoom-in').onclick = function() {
  scale = Math.min(5, scale * 1.2);
  applyTransform();
};
document.getElementById('zoom-out').onclick = function() {
  scale = Math.max(0.15, scale / 1.2);
  applyTransform();
};
document.getElementById('zoom-fit').onclick = fitView;

// Keyboard shortcuts
window.addEventListener('keydown', function(e) {
  if (e.key === '+' || e.key === '=') { scale = Math.min(5, scale * 1.2); applyTransform(); }
  if (e.key === '-') { scale = Math.max(0.15, scale / 1.2); applyTransform(); }
  if (e.key === '0') { fitView(); }
  if (e.key === 'Escape') { document.getElementById('detail-card').style.display = 'none'; }
});

// ── Theme toggle ─────────────────────────────────────────────────────
var themeBtn = document.getElementById('theme-toggle');
function updateThemeBtn() {
  var dark = document.documentElement.classList.contains('dark');
  themeBtn.textContent = dark ? '☀ Light' : '🌙 Dark';
}
themeBtn.onclick = function() {
  var d = document.documentElement.classList.toggle('dark');
  localStorage.setItem('cc-arch-theme', d ? 'dark' : 'light');
  updateThemeBtn();
};
updateThemeBtn();

// ── Layer chips ───────────────────────────────────────────────────────
document.querySelectorAll('.chip').forEach(function(chip) {
  chip.onclick = function() {
    document.querySelectorAll('.chip').forEach(function(c) { c.classList.remove('on'); });
    this.classList.add('on');
    var layer = this.dataset.layer;
    var svgHolder = document.getElementById('svg-holder');
    if (layer === 'all') {
      svgHolder.style.filter = 'none';
      // restore all opacity
      svgHolder.querySelectorAll('[fill]').forEach(function(el) {
        el.style.opacity = '';
      });
      return;
    }
    // dim elements not in layer by checking fill hex
    var targetHexes = LAYER_COLORS[layer] || [];
    svgHolder.querySelectorAll('[fill]').forEach(function(el) {
      var fill = (el.getAttribute('fill') || '').toLowerCase().replace('#', '');
      var match = targetHexes.some(function(h) { return fill.indexOf(h) !== -1; });
      el.style.opacity = match ? '' : '0.12';
    });
  };
});

// ── Node click → detail card ──────────────────────────────────────────
document.getElementById('svg-holder').addEventListener('click', function(e) {
  // walk up to find a text element with content
  var el = e.target;
  var text = '';
  while (el && el !== this) {
    if (el.tagName === 'text' || el.tagName === 'tspan') {
      text = el.textContent.trim();
      if (text) break;
    }
    el = el.parentElement;
  }
  if (!text) return;

  // find matching node info (partial match)
  var info = null;
  for (var key in NODE_INFO) {
    // normalize \\n to space for comparison
    var norm = key.replace(/\\\\n/g, ' ').replace(/\\n/g, ' ');
    if (norm.indexOf(text) !== -1 || text.indexOf(norm.split(' ')[0]) !== -1) {
      info = NODE_INFO[key];
      break;
    }
  }
  if (!info) return;

  var card = document.getElementById('detail-card');
  document.getElementById('card-title').textContent = text;
  document.getElementById('card-body').textContent = info.desc;
  card.style.display = 'block';
  e.stopPropagation();
});

// Close card on stage click
stage.addEventListener('click', function() {
  document.getElementById('detail-card').style.display = 'none';
});
document.getElementById('card-close').onclick = function() {
  document.getElementById('detail-card').style.display = 'none';
};

// ── Init ──────────────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', function() {
  fitView();
});
</script>
</body>
</html>
'''

html = html.replace('SVG_PLACEHOLDER', svg)
html = html.replace('__SVG_W__', str(SVG_W))
html = html.replace('__SVG_H__', str(SVG_H))

with open('claude-code-arch.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Done: claude-code-arch.html written, size:', len(html), 'bytes')
