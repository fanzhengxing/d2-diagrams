# D2 Syntax Cheatsheet

## Basics
```d2
# Comment
x -> y                    # Simple arrow
x -> y: label           # Arrow with label
x <-> y                 # Bi-directional
x -> y {style.stroke-dash: 3}  # Dashed arrow
x -> y {style.stroke-width: 3} # Bold arrow
```

## Containers (Grouping)
```d2
parent: {
  child1: "name"
  child2: {shape: cylinder}
  child1 -> child2: "connects"
}
```

## Cross-container connections
```d2
parent1.child -> parent2.child2: "跨容器连接"
```

## Shape Types
| Shape | Code | Visual |
|-------|------|--------|
| Rectangle (default) | `x: {}` | Box |
| Cylinder | `x: {shape: cylinder}` | Database |
| Diamond | `x: {shape: diamond}` | Decision |
| Oval | `x: {shape: oval}` | Start/End |
| Hexagon | `x: {shape: hexagon}` | Gateway |
| Person | `x: {shape: person}` | User/Actor |
| Cloud | `x: {shape: cloud}` | External |
| Page | `x: {shape: page}` | Document |
| Stored Data | `x: {shape: stored_data}` | Storage |
| Circle | `x: {shape: circle}` | Node |
| Square | `x: {shape: square}` | Box |
| Triangle | `x: {shape: triangle}` | Direction |

## Styling
```d2
node: {
  style.fill: "#22d3ee"       # Background color
  style.stroke: "#0284c7"     # Border color
  style.stroke-width: 2       # Border width
  style.stroke-dash: 4        # Dashed border
  style.font-color: "#fff"    # Text color
  style.font-size: 14         # Font size
  style.bold: true            # Bold text
  style.italic: true          # Italic text
  style.underline: true       # Underline
  style.opacity: 0.8          # Opacity
  style.rounded: true         # Rounded corners
  style.shadow: true          # Drop shadow
  style.multiple: true        # Stacked/multiple items
  width: 200                  # Width in pixels
  height: 80                  # Height in pixels
}
```

## Arrow Styling
```d2
A -> B: label {
  style.stroke: "#ef4444"     # Arrow color
  style.stroke-width: 2       # Arrow thickness
  style.stroke-dash: 3        # Dashed arrow
  style.animated: true        # Animated flow (?)
  style.opacity: 0.7
}
```

## Config Block
```d2
vars: {
  d2-config: {
    layout-engine: dagre     # or elk
    theme-id: 0              # 0 = Neutral Default
    dark-theme-id: 200       # 200 = Dark Mauve
    sketch: false            # true for hand-drawn
    pad: 100                 # Padding
  }
}
```

## CLI Flags
```bash
d2 input.d2 output.svg                    # Default render
d2 --theme=200 input.d2 output.svg        # Dark theme
d2 --dark-theme=200 input.d2 output.svg   # Auto dark mode
d2 --sketch input.d2 output.svg           # Hand-drawn style
d2 --layout=elk input.d2 output.svg       # ELK layout
d2 --pad=50 input.d2 output.svg           # Padding
d2 --scale=2 input.d2 output.png          # Scale up PNG
d2 --watch input.d2 output.svg            # Live reload
d2 --animate-interval=3000 input.d2 output.svg  # Auto-transition
d2 input.d2 output.txt                    # ASCII art
d2 input.d2 output.pptx                   # PowerPoint
d2 input.d2 output.gif                    # Animated GIF
d2 validate input.d2                      # Validate only
d2 fmt input.d2                           # Format/pretty-print
```

## Icons
```d2
service: {
  icon: https://icons.terrastruct.com/tech/database.svg
  label: "MySQL"
}
```

## Variables
```d2
vars: {
  color-primary: "#22d3ee"
  label-text: "My Label"
}
node: style.fill: vars.color-primary
```

## Special Features
- **Multi-board**: `scenarios { dev {} prod {} }` 
- **Layers**: `layers { api {} db {} }`
- **Steps**: `steps { step1 {} step2 {} }`
- **Auto-animate**: `--animate-interval=3000` for multi-board SVGs
- **Watch mode**: `--watch` auto-reloads in browser
