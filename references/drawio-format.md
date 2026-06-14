# Draw.io XML 输出模式

除了 D2 原生格式（SVG/PNG/PDF/PPTX/GIF/ASCII），d2-diagrams 也支持
输出 draw.io XML 格式（.drawio 文件），可拖入 app.diagrams.net 编辑。

## 什么时候用 draw.io 模式

- 用户需要后续在 draw.io 中手动编辑
- 用户需要 draw.io 特有的图标库（AWS/GCP/Azure）
- 用户希望利用 draw.io 的协作功能
- D2 输出不够精确，需要手工微调

## Draw.io XML 基础结构

```xml
<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="app.diagrams.net">
  <diagram name="Page-1" id="page1">
    <mxGraphModel dx="1420" dy="786" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="0" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <!-- cells here -->
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

## 核心元素类型

### 矩形（服务/组件）
```xml
<mxCell id="s1" value="Service Name" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#4a9eed;fontColor=#ffffff;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="200" height="60" as="geometry" />
</mxCell>
```

### 圆角矩形（流程步骤）
```xml
<mxCell id="p1" value="Process Step" style="rounded=1;arcSize=20;whiteSpace=wrap;html=1;fillColor=#b2f2bb;" vertex="1" parent="1">
  <mxGeometry x="100" y="200" width="180" height="60" as="geometry" />
</mxCell>
```

### 菱形（决策点）
```xml
<mxCell id="d1" value="Decision?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fff3bf;" vertex="1" parent="1">
  <mxGeometry x="150" y="300" width="120" height="80" as="geometry" />
</mxCell>
```

### 数据库（圆柱）
```xml
<mxCell id="db1" value="Database" style="shape=cylinder;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=15;fillColor=#a78bfa;fontColor=#ffffff;" vertex="1" parent="1">
  <mxGeometry x="100" y="400" width="120" height="80" as="geometry" />
</mxCell>
```

### 箭头（连接线）
```xml
<mxCell id="a1" value="label" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;entryX=0.5;entryY=0;strokeWidth=2;" edge="1" parent="1" source="s1" target="p1">
  <mxGeometry relative="1" as="geometry" />
</mxCell>
```

### 泳道/分组
```xml
<mxCell id="g1" value="Group Name" style="swimlane;whiteSpace=wrap;html=1;startSize=30;fillColor=#e5dbff;" vertex="1" parent="1">
  <mxGeometry x="50" y="50" width="800" height="500" as="geometry" />
</mxCell>
```

## 颜色映射（D2 → draw.io）

| D2 语义色 | Draw.io fillColor | 用途 |
|-----------|-------------------|------|
| #22d3ee (Cyan) | #4a9eed | 前端 |
| #34d399 (Emerald) | #22c55e | 后端 |
| #a78bfa (Violet) | #8b5cf6 | 数据库 |
| #fbbf24 (Amber) | #f59e0b | 云服务 |
| #fb7185 (Rose) | #ef4444 | 安全 |
| #a5d8ff (Light Blue) | #dbeafe | 输入节点 |
| #b2f2bb (Light Green) | #dcfce7 | 成功/输出 |
| #ffd8a8 (Light Orange) | #fed7aa | 警告 |
| #ffc9c9 (Light Red) | #fecaca | 错误/关键 |

## 布局建议

- x, y 坐标：从 (100, 100) 开始，水平间距 250px，垂直间距 150px
- 矩形宽：200px，高：60px
- 菱形宽：120px，高：80px
- 箭头使用 `orthogonalEdgeStyle` 获得直角拐弯
- 使用 `swimlane` 做层次分组

## 完整示例：架构图

参考 `references/examples/drawio-architecture.drawio`
