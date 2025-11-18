# Quick Reference Guide

Fast lookup for common tasks, patterns, and parameters in the IFS Fractal Generator project.

---

## 🎯 Common Tasks

### Adding a New Preset

```json
{
  "name": "My Fractal",
  "description": "Brief description",
  "iterations": 8,
  "seed": 42,
  "instance_base": "Cube",
  "transforms": [
    {
      "scale": [0.5, 0.5, 0.5],
      "rotation": [0, 0, 45],
      "translation": [1, 0, 0],
      "weight": 0.33
    }
  ],
  "color_palette": {
    "mode": "iteration_depth",
    "stops": [[0, "#1B5E20"], [1, "#81C784"]]
  }
}
```

**Steps**:
1. Create JSON file in `/src/presets/`
2. Validate against `schema.json`
3. Test in Blender
4. Add reference image to `/assets/reference_images/`
5. Generate preview render for `/assets/preview_renders/`

---

### Loading a Preset in Blender

**Manual Method**:
```python
import json
from pathlib import Path

# Load preset
preset_path = Path("src/presets/barnsley.json")
with open(preset_path) as f:
    preset = json.load(f)

# Access parameters
iterations = preset["iterations"]
transforms = preset["transforms"]
```

**Using Preset Loader** (future):
```python
from utils.preset_loader import load_preset, apply_preset

preset = load_preset("barnsley")
apply_preset(preset, node_group)
```

---

### Adjusting Performance

**For Faster Preview**:
- Reduce iterations: 4-6
- Use Points output mode
- Disable color mapping temporarily
- Lower transform count

**For Final Quality**:
- Increase iterations: 10-12
- Use Instanced output mode
- Realize only for export
- Enable full color gradients

**Memory Warning Signs**:
- Viewport lag > 1 second
- Point count > 10 million
- Blender memory > 8GB

---

### Exporting Fractals

**GLB (Web/Games)**:
1. Set output mode to "Realized"
2. File → Export → glTF 2.0
3. Select fractal object
4. Enable "Apply Modifiers"
5. Export

**PLY (Point Cloud)**:
1. Set output mode to "Points"
2. File → Export → Stanford (.ply)
3. Select object
4. Choose binary format for size

**Alembic (Animation)**:
1. Animate iteration count
2. File → Export → Alembic
3. Set frame range
4. Enable "Flatten Hierarchy"

---

## 📐 Parameter Ranges

### Recommended Ranges

| Parameter | Min | Typical | Max | Notes |
|-----------|-----|---------|-----|-------|
| Iterations | 1 | 8 | 12 | Exponential growth |
| Scale | 0.1 | 0.5 | 1.0 | Values > 1 explode |
| Rotation | -360 | 0-90 | 360 | Degrees |
| Translation | -10 | -2 to 2 | 10 | Blender units |
| Weight | 0.0 | 0.25-0.5 | 1.0 | Probability 0-100% |
| Seed | 0 | 1-100 | 9999 | Any integer |

### Classic Fractal Parameters

**Barnsley Fern**:
```
Iterations: 10
Transforms: 4
Scale: [0.85, 0.04, 0.2, 0.15] (varied per transform)
Weights: [0.85, 0.07, 0.07, 0.01]
```

**Sierpiński Triangle**:
```
Iterations: 8
Transforms: 3
Scale: [0.5, 0.5, 0.5] (uniform)
Translation: toward vertices
Weights: [0.33, 0.33, 0.34]
```

**Menger Cube**:
```
Iterations: 4 (caution: grows extremely fast)
Transforms: 20 (complex)
Scale: [0.33, 0.33, 0.33]
Weights: equal distribution
```

---

## 🎨 Color Palettes

### Nature Themes

**Forest Green**:
```json
"stops": [
  [0.0, "#1B5E20"],
  [0.5, "#4CAF50"],
  [1.0, "#81C784"]
]
```

**Autumn**:
```json
"stops": [
  [0.0, "#BF360C"],
  [0.5, "#FF6F00"],
  [1.0, "#FDD835"]
]
```

**Ocean**:
```json
"stops": [
  [0.0, "#01579B"],
  [0.5, "#0288D1"],
  [1.0, "#4FC3F7"]
]
```

### Abstract Themes

**Neon**:
```json
"stops": [
  [0.0, "#E91E63"],
  [0.5, "#9C27B0"],
  [1.0, "#3F51B5"]
]
```

**Monochrome**:
```json
"stops": [
  [0.0, "#212121"],
  [0.5, "#757575"],
  [1.0, "#EEEEEE"]
]
```

---

## 🔧 Node Setup Patterns

### Basic Transform Pattern

```
Input Geometry → Instance on Points → Transform Geometry → Merge by Distance
```

### Probabilistic Branching

```
Random Value [Seed + Index] → Compare [< Weight] → Switch [Pass/Discard]
```

### Iteration Tracking

```
Repeat Zone → Index Node → Store Named Attribute ["iteration"]
```

### Color Mapping

```
Attribute ["iteration"] → Map Range [0 to MaxIter] → Color Ramp → Set Color
```

---

## 🐛 Troubleshooting

### Problem: Fractal doesn't appear

**Possible Causes**:
- All weights sum to 0
- Transform scales are 0
- Iteration count is 0
- Instance mesh is empty

**Solutions**:
1. Check weight values > 0
2. Verify scale values between 0.1-1.0
3. Set iterations to at least 3
4. Assign valid instance mesh

---

### Problem: Viewport is slow

**Immediate Fixes**:
- Reduce iterations by 2-3
- Switch to Points output mode
- Hide other objects in scene
- Disable color mapping

**Long-term Solutions**:
- Optimize transform count
- Use LOD system
- Enable viewport culling
- Upgrade hardware

---

### Problem: Export fails

**Common Issues**:
- Too many instances (>10M)
- Instances not realized
- Invalid geometry (non-manifold)
- File path too long

**Solutions**:
1. Reduce iterations before export
2. Enable "Realize Instances" modifier
3. Use Merge by Distance node
4. Use shorter file paths

---

### Problem: Preset won't load

**Check**:
- Valid JSON syntax (use validator)
- All required fields present
- Values within acceptable ranges
- File encoding is UTF-8

**Validation Command**:
```bash
python -m json.tool preset.json
```

---

## 📊 Performance Benchmarks

### Expected Point Counts

| Transforms | Iter 4 | Iter 6 | Iter 8 | Iter 10 | Iter 12 |
|------------|--------|--------|--------|---------|---------|
| 2 | 16 | 64 | 256 | 1,024 | 4,096 |
| 3 | 81 | 729 | 6,561 | 59,049 | 531,441 |
| 4 | 256 | 4,096 | 65,536 | 1,048,576 | 16,777,216 |
| 8 | 4,096 | 262,144 | 16,777,216 | 1B+ | 💥 |

**Formula**: `Points = Transforms ^ Iterations`

### Viewport Performance Targets

| Quality | FPS | Max Points | Iterations | Notes |
|---------|-----|------------|------------|-------|
| Interactive | 60 | 100K | 6-7 | Smooth manipulation |
| Preview | 30 | 500K | 8-9 | Acceptable lag |
| Final | 10 | 2M | 10-11 | Render quality |
| Export | N/A | 10M | 12+ | Offline processing |

---

## 🔑 Keyboard Shortcuts (Future UI)

### Planned Shortcuts

| Action | Shortcut | Context |
|--------|----------|---------|
| Toggle Preview Mode | `Shift+P` | Viewport |
| Load Next Preset | `Ctrl+]` | Viewport |
| Load Previous Preset | `Ctrl+[` | Viewport |
| Randomize Seed | `Shift+R` | Viewport |
| Reset to Default | `Ctrl+Alt+R` | Properties |
| Quick Export | `Ctrl+Shift+E` | Viewport |

---

## 📝 Code Snippets

### Batch Generate Presets

```python
import bpy
from pathlib import Path
import json

presets_dir = Path("src/presets")
output_dir = Path("output/renders")

for preset_file in presets_dir.glob("*.json"):
    with open(preset_file) as f:
        preset = json.load(f)
    
    # Apply preset (pseudo-code)
    apply_preset(preset)
    
    # Render
    bpy.ops.render.render(write_still=True)
    
    # Save
    output_path = output_dir / f"{preset['name']}.png"
    bpy.data.images['Render Result'].save_render(str(output_path))
```

### Animate Iteration Count

```python
import bpy

node_group = bpy.data.node_groups['IFS_Generator']
iterations_input = node_group.inputs['Iterations']

# Keyframe animation
for frame in range(1, 121):
    iterations = int(frame / 20) + 1  # 1 to 6 over 120 frames
    node_group.inputs['Iterations'].default_value = iterations
    node_group.inputs['Iterations'].keyframe_insert('default_value', frame=frame)
```

### Validate All Presets

```bash
#!/bin/bash
for preset in src/presets/*.json; do
  echo "Validating $preset..."
  python -c "
import json
import jsonschema

with open('src/presets/schema.json') as f:
    schema = json.load(f)

with open('$preset') as f:
    preset = json.load(f)

jsonschema.validate(preset, schema)
print('✓ Valid')
"
done
```

---

## 🌐 File Paths

### Key Files

```
IFS-Fractal-Generator/
├── docs/
│   ├── architecture.md          # System design
│   ├── development-plan.md      # Roadmap
│   ├── glossary.md             # Terminology
│   ├── quick-reference.md      # This file
│   └── diagrams/               # Visual docs
├── src/
│   ├── geometry_nodes/
│   │   └── ifs_generator.blend # Core node group
│   ├── presets/
│   │   ├── schema.json         # Validation schema
│   │   ├── barnsley.json       # Fern preset
│   │   └── sierpinski.json     # Triangle preset
│   └── utils/
│       ├── preset_loader.py    # Preset management
│       └── validator.py        # Schema validation
└── assets/
    ├── reference_images/       # Mathematical references
    └── preview_renders/        # Example outputs
```

---

## 🔗 Quick Links

### Documentation
- [Full Architecture](./architecture.md)
- [Development Plan](./development-plan.md)
- [System Diagrams](./diagrams/system-overview.md)
- [Glossary](./glossary.md)

### External Resources
- [Blender Geometry Nodes Docs](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/)
- [Fractals Everywhere (Book)](https://archive.org/details/fractalseverywhe00barn)
- [MCP Specification](https://modelcontextprotocol.io)
- [JSON Schema Tutorial](https://json-schema.org/learn/getting-started-step-by-step)

---

## 💡 Tips & Tricks

### Performance
- ⚡ Use instancing until final export
- ⚡ Cache heavy calculations in subgroups
- ⚡ Limit viewport samples during interaction
- ⚡ Profile with Blender's performance overlay

### Workflow
- 🎯 Start with low iterations, increase gradually
- 🎯 Save variants as separate presets
- 🎯 Use descriptive preset names
- 🎯 Document unusual parameter combinations

### Debugging
- 🔍 Use Viewer nodes to inspect intermediate geometry
- 🔍 Check point counts with Geometry Info node
- 🔍 Visualize attributes with Spreadsheet editor
- 🔍 Test transforms individually before combining

### Creativity
- 🎨 Blend multiple fractals with different seeds
- 🎨 Animate transform parameters for organic motion
- 🎨 Use custom instance meshes (leaves, crystals)
- 🎨 Layer fractals with different materials

---

**Last Updated**: 2025-11-11  
**Version**: 1.0  
**Applies to**: Phase 1-2 Development

