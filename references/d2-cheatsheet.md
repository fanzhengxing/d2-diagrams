# D2 Syntax Cheatsheet

## Basics
```d2
x -> y                    # Simple arrow
x -> y: label           # With label
x <-> y                 # Bi-directional
x -> y {style.stroke-dash: 3}  # Dashed
```

## Containers
```d2
parent: {
  child1: "Book"
  child2: {shape: cylinder}
  child1 -> child2: "stores"
}
```

## Cross-container
```d2
group1.service -> group2.db: calls
```

## Shape Types
| Shape | Code |
|-------|------|
| Rectangle | `{}` (default) |
| Cylinder (DB) | `{shape: cylinder}` |
| Diamond (decision) | `{shape: diamond}` |
| Oval (start/end) | `{shape: oval}` |
| Hexagon (gateway) | `{shape: hexagon}` |
| Person | `{shape: person}` |
| Cloud | `{shape: cloud}` |
| Page (document) | `{shape: page}` |
| Stored Data | `{shape: stored_data}` |

## Styling Reference
```d2
node: {
  style.fill: "#22d3ee"        # Background
  style.stroke: "#0284c7"      # Border
  style.stroke-width: 2
  style.stroke-dash: 4         # Dashed
  style.font-color: "#fff"     # Text
  style.font-size: 14
  style.bold: true
  style.italic: true
  style.rounded: true
  style.shadow: true
  style.opacity: 0.8
  style.multiple: true         # Stacked
  width: 200
  height: 80
}
```

## CLI Flags
```bash
d2 input.d2 output.svg                    # SVG
d2 --theme=200 input.d2 output.svg        # Dark theme
d2 --sketch input.d2 output.svg           # Hand-drawn
d2 --layout=elk input.d2 output.svg       # ELK layout
d2 --watch input.d2 output.svg            # Live reload
d2 --animate-interval=3000 input.d2 output.svg  # Auto-transition
d2 input.d2 output.txt                    # ASCII art
d2 input.d2 output.pptx                   # PowerPoint
d2 input.d2 output.gif                    # Animated GIF
d2 validate input.d2                      # Validate syntax
d2 fmt input.d2                           # Format file
```

## Config Block
```d2
vars: {
  d2-config: {
    layout-engine: dagre  # or elk
    theme-id: 0           # 0=Neutral, 200=Dark, 300=Terminal, 303=C4
    pad: 100
  }
}
```

## Icons
```d2
service: {
  icon: https://icons.terrastruct.com/tech/database.svg
  label: "MySQL"
}
```
