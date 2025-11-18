# Glossary

Technical terminology and concepts used throughout the IFS Fractal Generator project.

---

## Mathematical & Fractal Concepts

### Affine Transformation
A geometric transformation that preserves lines and parallelism. In this project, composed of **Scale**, **Rotation**, and **Translation** operations applied to point coordinates.

### Barnsley Fern
A classic IFS fractal resembling a fern leaf, created using four weighted affine transformations. Often used as a demonstration of how simple rules create complex organic patterns.

### Deterministic Randomness
Randomness that produces repeatable results when given the same seed value. Enables reproducible fractals across different sessions and machines.

### Fractal
A geometric shape that exhibits self-similarity at multiple scales. Created through recursive application of simple rules.

### IFS (Iterated Function System)
A mathematical framework for generating fractals by repeatedly applying a set of functions (transforms) to points. Each iteration produces a more detailed approximation of the final fractal shape.

### Iteration
A single cycle through the transformation process. More iterations produce more detailed fractals but increase computational cost exponentially.

### Menger Cube (Menger Sponge)
A 3D fractal created by recursively removing cube segments from a larger cube. The 3D analog of the Sierpiński carpet.

### Self-Similarity
The property where a structure looks similar at different scales. A key characteristic of fractals.

### Sierpiński Triangle
A classic 2D fractal formed by repeatedly subdividing a triangle into smaller triangles. Created using three transforms scaling toward each vertex.

### Transform Set
A collection of affine transformations that define a specific fractal. Each transform has scale, rotation, translation, and probability weight parameters.

### Weight (Probability Weight)
A value between 0 and 1 that determines how often a transform is applied. Enables creation of asymmetric fractals like the Barnsley Fern.

---

## Blender-Specific Terms

### Asset Browser
Blender's system for managing reusable components (materials, node groups, objects). The IFS generator can be distributed as an asset.

### Blender Python API (bpy)
Python interface for programmatic control of Blender. Used for preset loading, export automation, and future MCP integration.

### Dependency Graph
Blender's system for tracking relationships between objects, modifiers, and data. Automatically recalculates when parameters change.

### Geometry Nodes
Blender's procedural modeling system using a node-based workflow. The core technology powering this fractal generator.

### Instance / Instancing
Efficient rendering technique where geometry is referenced rather than duplicated. Critical for performance with millions of fractal points.

### Modifier
A non-destructive operation applied to geometry. Geometry Nodes are applied as modifiers in Blender.

### Node Group
A reusable collection of nodes that can be treated as a single unit. The IFS generator is implemented as a node group.

### Node Socket
Input or output connection point on a node. Carries data (geometry, numbers, vectors) between nodes.

### Realize Instances
Converting instanced geometry into actual mesh data. Required for some export formats but computationally expensive.

### Repeat Zone
A special Geometry Nodes construct that enables iteration loops. Core mechanism for applying multiple fractal iterations.

### Viewport
Blender's 3D view window where geometry is displayed interactively. Performance optimizations target smooth viewport interaction.

---

## Project-Specific Terms

### Color Ramp
A gradient mapping system that assigns colors based on iteration depth. Creates visual distinction between fractal levels.

### Export Pipeline
The process of converting procedural fractal geometry into standard 3D file formats (GLB, PLY, Alembic, USD).

### Instance Mesh
The base geometry shape (cube, sphere, custom mesh) that gets replicated at each fractal point.

### Iteration Attribute
A stored value on each point indicating which iteration created it. Used for color mapping and analysis.

### MCP (Model Context Protocol)
A standard for AI agents to interact with external tools. Future integration layer enabling natural language fractal generation.

### MCP Server
A process that exposes IFS generator functionality as tools callable by AI agents (like Claude).

### MCP Tool
A specific function exposed via MCP (e.g., `generate_fractal`, `modify_parameters`, `export_geometry`).

### Output Mode
Determines final geometry format: **Points** (point cloud), **Instanced** (geometry references), or **Realized** (full mesh).

### Preset
A JSON file containing complete fractal configuration (transforms, colors, parameters). Enables quick switching between fractals.

### Preset Schema
JSON Schema definition that validates preset file structure. Ensures consistency and catches errors.

### Preview Mode
Reduced-quality rendering mode with fewer iterations for real-time interaction. Switches to full quality when idle.

### Seed Value
Integer controlling random number generation for deterministic behavior. Same seed produces identical fractals.

### Transform Branch
One of multiple parallel paths in the node tree, each applying a different transformation.

---

## Technical & Development Terms

### Add-on
Blender's plugin system. Future UI layer will be distributed as an add-on for easy installation.

### Batch Processing
Automated generation of multiple fractals without manual interaction. Used for creating galleries or variations.

### Exponential Growth
The rapid increase in point count with each iteration (e.g., 4 transforms × 10 iterations = 1,048,576 points).

### JSON (JavaScript Object Notation)
Human-readable data format used for storing presets and configuration.

### Node Tree
The complete graph of connected nodes forming the IFS generator logic.

### Performance Guardrail
System limits (max iterations, warnings) preventing crashes from excessive geometry.

### Schema Validation
Automated checking of JSON files against a defined structure. Catches errors before loading presets.

### Subgraph / Sub-network
A grouped collection of nodes within a larger node tree. Used for organization and reusability.

### UI Panel
Custom interface section in Blender's sidebar containing fractal controls.

---

## File & Folder Terms

### `/assets/`
Repository folder containing visual resources (icons, reference images, preview renders).

### `/docs/`
Repository folder containing project documentation and architecture diagrams.

### `/src/`
Repository folder containing source code, node groups, presets, and utilities.

### `/src/geometry_nodes/`
Folder containing the `.blend` file with the IFS generator node group.

### `/src/presets/`
Folder containing JSON preset files for various fractals.

### `/src/mcp/`
Folder for future Model Context Protocol integration code.

### `/src/utils/`
Folder containing Python utility modules (preset loader, validators, helpers).

### `.blend File`
Blender's native file format storing scenes, objects, and node groups.

### `barnsley.json`
Preset file defining parameters for the Barnsley Fern fractal.

### `ifs_generator.blend`
Main Blender file containing the IFS fractal generator node group.

### `preset_loader.py`
Python script for reading JSON presets and applying them to the node group.

### `schema.json`
JSON Schema file defining valid preset structure.

---

## UI/UX Terms

### Operator
In Blender add-on development, a class that performs an action (e.g., loading a preset, exporting geometry).

### Property
A stored value in Blender that can be linked to UI elements (sliders, checkboxes, dropdowns).

### Panel
A section in Blender's UI containing controls and information.

### Modal Dialog
A popup window requiring user interaction before continuing.

### Toast Notification
A temporary, non-intrusive message that appears briefly then disappears.

---

## Performance Terms

### Bottleneck
The slowest part of a process that limits overall performance. In this project, typically the geometry merge operations.

### Caching
Storing computed results to avoid recalculation. Blender's dependency graph uses caching extensively.

### Culling
Removing geometry outside the visible area to improve performance. Especially useful for large fractals.

### Debouncing
Delaying action until user input stops changing. Prevents excessive recalculations during slider dragging.

### Frame Time
Time to render a single frame in the viewport. Target is <16ms for 60fps.

### LOD (Level of Detail)
Showing simplified geometry when viewing from far away or during interaction.

### Realization Cost
The computational expense of converting instances to full geometry. Can increase memory usage 100x+.

---

## Future Concepts

### Agent Workflow
A multi-step process executed by an AI agent, potentially involving generation, refinement, and export.

### Cloud Preset Repository
A planned online library of community-created fractal presets.

### Collaborative Editing
A conceptual feature allowing multiple users to work on fractals simultaneously.

### Fractal Blending
Planned feature to combine multiple fractals into hybrid forms.

### L-System
Alternative fractal generation method using formal grammars. Potential future extension beyond IFS.

### Preset Marketplace
Planned community platform for sharing and discovering fractal configurations.

### Real-time Shader
GPU-based rendering approach for faster preview. Future optimization possibility.

---

## Acronyms

| Acronym | Full Term | Context |
|---------|-----------|---------|
| API | Application Programming Interface | Blender Python API, MCP API |
| DLA | Diffusion-Limited Aggregation | Alternative fractal type (not implemented) |
| FPS | Frames Per Second | Viewport performance metric |
| GN | Geometry Nodes | Blender's procedural system |
| GLB | GL Binary Format | 3D export format |
| GLTF | GL Transmission Format | 3D export format (text version) |
| HDRI | High Dynamic Range Image | Lighting technique |
| IFS | Iterated Function System | Core fractal algorithm |
| JSON | JavaScript Object Notation | Data format for presets |
| LOD | Level of Detail | Performance optimization |
| MCP | Model Context Protocol | AI agent integration standard |
| PBR | Physically Based Rendering | Advanced material system |
| PLY | Polygon File Format | Point cloud export format |
| RGB | Red Green Blue | Color representation |
| UI | User Interface | Interactive controls |
| USD | Universal Scene Description | 3D pipeline format |
| UX | User Experience | Interaction design |

---

## Usage Examples

### In Documentation
> "The **Repeat Zone** executes the **transform set** for each **iteration**, with each **transform branch** applying **affine transformations** based on **probability weights**."

### In Code Comments
```python
# Load preset and validate against schema
preset = load_preset("barnsley.json")
if validate_schema(preset):
    apply_to_node_group(preset)
```

### In User Interface
```
Iterations: [slider] (6)
Seed: [input] (42)
Preset: [dropdown] ▼ Barnsley Fern
Output Mode: ○ Points ● Instanced ○ Realized
```

---

## Related Reading

For deeper understanding of these concepts:
- **IFS Theory**: "Fractals Everywhere" by Michael Barnsley
- **Blender GN**: Official Blender 4.x documentation
- **MCP Protocol**: [modelcontextprotocol.io](https://modelcontextprotocol.io)
- **JSON Schema**: [json-schema.org](https://json-schema.org)

---

**Note**: This glossary is a living document. New terms will be added as the project evolves through development phases.

