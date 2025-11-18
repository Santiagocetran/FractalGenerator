# IFS Fractal Generator: System Architecture

## 1. Project Overview

### Purpose
The **IFS Fractal Generator** is a procedural geometry system built entirely within Blender's Geometry Nodes framework. It implements Iterated Function Systems (IFS) to generate self-similar fractal structures through recursive transformation of point clouds and instanced geometry.

### Key Characteristics
- **Zero Python at Core**: Pure Geometry Nodes implementation for maximum portability and performance
- **Preset-Driven**: JSON configuration files define fractal behavior without modifying node graphs
- **Real-Time Interactive**: All parameters exposed for live manipulation and animation
- **Extensible Architecture**: Designed for future MCP integration and UI layer additions

### Design Philosophy
1. **Separation of Concerns**: Node logic, presets, and future agent interfaces remain decoupled
2. **Performance First**: Instancing-based approach with configurable quality levels
3. **Educational Foundation**: Clean structure suitable for learning procedural geometry concepts
4. **Production Ready**: Sufficient guardrails and optimization for practical use

---

## 2. Core Architecture Components

### 2.1 Geometry Nodes Engine
The foundation layer consists of a modular Geometry Nodes group implementing the IFS algorithm.

**Primary Node Group**: `IFS_Generator`

**Input Interface**:
- `Iterations` (Integer, 1–12): Recursion depth
- `Seed` (Integer): Deterministic randomness control
- `Transform Set [1-8]`: Individual transform configurations
  - Scale (Vector XYZ)
  - Rotation (Euler XYZ)
  - Translation (Vector XYZ)
  - Probability Weight (Float, 0–1)
- `Instance Mesh` (Geometry): Base shape to replicate
- `Output Mode` (Menu): Points / Instanced / Realized

**Core Algorithm Structure**:
```
Initialize → Repeat Zone → Transform Application → Merge → Output Modulation
```

**Internal Mechanics**:
- **Repeat Zone**: Contains iteration loop with state propagation
- **Transform Nodes**: Probabilistic branching using Compare + Switch patterns
- **Attribute Capture**: Stores iteration index for downstream color mapping
- **Instance to Points**: Converts geometry to transformable point cloud per iteration

### 2.2 Preset System
JSON files encode complete fractal definitions, enabling non-destructive switching between configurations.

**Schema Structure**:
```json
{
  "name": "Fractal Name",
  "description": "Brief explanation",
  "iterations": 10,
  "seed": 42,
  "instance_base": "Cube",
  "transforms": [
    {
      "scale": [0.5, 0.5, 0.5],
      "rotation": [0, 0, 45],
      "translation": [1, 0, 0],
      "weight": 0.5
    }
  ],
  "color_palette": {
    "mode": "iteration_depth",
    "stops": [[0, "#2E7D32"], [1, "#81C784"]]
  },
  "performance": {
    "preview_iterations": 6,
    "final_iterations": 10
  }
}
```

**Preset Categories**:
- **Classic 2D**: Barnsley Fern, Sierpiński Triangle/Carpet
- **3D Structures**: Menger Cube, Sierpiński Pyramid
- **Organic Forms**: Tree variations, coral structures
- **Experimental**: Custom mathematical constructs

### 2.3 Future Integration Layers

#### MCP Agent Interface (Planned)
Natural language interaction layer for preset generation and modification.

**Capabilities**:
- "Generate a 4-transform fractal with spiral tendency"
- "Adjust Barnsley Fern to make it more compact"
- "Export current fractal as GLB with 8 iterations"

**Technical Approach**:
- MCP server exposes tools for preset manipulation
- Agent parses intent → generates/modifies JSON
- Blender Python API applies preset to node group
- Optional: Real-time parameter animation via agent

#### Export & Rendering Pipeline (Planned)
Automated output generation with format conversion.

**Export Targets**:
- GLB/GLTF (web-ready)
- PLY (point cloud analysis)
- Alembic (animation cache)
- USD (pipeline integration)

---

## 3. Data Flow Architecture

### 3.1 Static Configuration Flow
```
User Selection → JSON Preset Load → Node Group Parameter Mapping → Geometry Generation
```

**Key Stages**:
1. **Preset Selection**: UI or script identifies target JSON file
2. **Schema Validation**: Ensures structural correctness
3. **Parameter Injection**: Python driver updates node group inputs
4. **Geometry Evaluation**: Blender's dependency graph executes node tree

### 3.2 Real-Time Interaction Flow
```
Parameter Adjustment → Viewport Update → Dependency Graph Rebuild → Preview Render
```

**Performance Considerations**:
- **Lazy Evaluation**: Only recalculates on parameter change
- **Preview Mode**: Reduced iteration count during interaction
- **Instance Culling**: Optional frustum culling for large fractals

### 3.3 Future Agent Flow (MCP Integration)
```
Natural Language Input → LLM Processing → Tool Selection → JSON Generation/Modification → 
Blender API Call → Node Update → Geometry Output → Agent Feedback
```

**Communication Pattern**:
- **Stateless Requests**: Each agent call is self-contained
- **Result Validation**: Agent receives success/error + preview image
- **Iteration Capability**: Multi-turn refinement of parameters

---

## 4. Technical Constraints & Design Decisions

### 4.1 Iteration Limits
**Constraint**: Maximum 12 iterations  
**Rationale**: Exponential growth of geometry (e.g., 4 transforms × 12 iterations = 16M instances)  
**Mitigation**: Preview mode, performance warnings, instancing-first approach

### 4.2 Transform Count
**Constraint**: Up to 8 simultaneous transforms  
**Rationale**: Balance between flexibility and node graph complexity  
**Alternative**: Support unlimited transforms via array-based structure (future enhancement)

### 4.3 Deterministic Randomness
**Decision**: Seed-based probabilistic selection  
**Implementation**: Geometry Nodes "Random Value" with seed propagation  
**Benefit**: Reproducible results across sessions and machines

### 4.4 Node Group Asset Management
**Strategy**: Single `.blend` file with versioned node groups  
**Distribution**: Blender Asset Browser integration  
**Updates**: Semantic versioning in node group metadata

---

## 5. Integration Points

### 5.1 Blender Python API
**Usage Scenarios**:
- Preset loading and application
- Batch rendering automation
- Export pipeline orchestration
- (Future) MCP server implementation

**Key Modules**:
- `bpy.data.node_groups`: Access to Geometry Nodes
- `bpy.context.object.modifiers`: Apply IFS generator to objects
- `bpy.ops.export_scene`: Format conversion operations

### 5.2 External Data Sources
**JSON Preset Library**:
- Local filesystem storage
- Optional: Git submodule for community presets
- Optional: REST API for cloud-hosted configurations

**Reference Images**:
- Mathematical diagrams for preset documentation
- Expected output renders for validation

### 5.3 MCP Protocol (Future)
**Server Implementation**:
- Python-based MCP server running alongside Blender
- Tools exposed: `generate_fractal`, `modify_preset`, `export_geometry`
- Context provision: Available presets, current scene state

**Client Expectations**:
- LLM with visual reasoning capability (for preview feedback)
- Conversational parameter refinement
- Long-term: Autonomous fractal exploration

---

## 6. System Boundaries

### In Scope
- IFS fractal generation via Geometry Nodes
- Preset management and switching
- Basic color mapping and material assignment
- Performance optimization for real-time preview
- Export to common 3D formats
- Comprehensive test suite (TDD approach)
- Automated validation and quality assurance

### Out of Scope (Current Phase)
- Non-IFS fractal types (L-systems, DLA, etc.)
- Advanced material systems (PBR, procedural shaders)
- GPU-accelerated custom solvers
- Distributed rendering

### Future Considerations
- Multi-fractal blending operations
- Fractal animation sequencing
- VR/AR preview modes
- Collaborative preset editing

---

## 7. Quality Attributes

### Performance
- **Target**: 60fps viewport interaction at 8 iterations
- **Strategy**: Instancing, delayed realization, LOD systems

### Maintainability
- **Documentation**: Inline node comments, external architecture docs
- **Modularity**: Grouped sub-networks for transforms, colors, utilities
- **Testing**: Comprehensive test suite with 80%+ coverage

### Extensibility
- **Plugin Architecture**: Clean interfaces for new transform types
- **Preset Versioning**: Schema evolution without breaking existing files

### Usability
- **Sensible Defaults**: Barnsley Fern preset loaded on startup
- **Progressive Disclosure**: Basic params exposed, advanced in collapsed panels

### Testability
- **Test-Driven Development**: Write tests before implementation
- **Unit Testing**: Fast, isolated tests for Python modules (80%+ coverage)
- **Integration Testing**: Blender API interaction validation
- **Preset Testing**: Automated schema validation for all presets
- **Performance Testing**: Benchmarks for point counts and FPS
- **Continuous Integration**: Automated test runs on commits

---

## 8. Architectural Risks & Mitigations

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|-----------|
| Geometry explosion crashes Blender | High | Medium | Hard iteration caps, memory monitoring |
| Node group complexity makes debugging difficult | Medium | High | Modular sub-groups, visual documentation |
| JSON schema changes break old presets | Medium | Medium | Versioned schema, migration scripts |
| MCP integration requires Blender API hacks | Low | Low | Clean Python layer, standard IPC |

---

## Next Steps
Refer to `/docs/development-plan.md` for milestone breakdown and implementation sequence.

