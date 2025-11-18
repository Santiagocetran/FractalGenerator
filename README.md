# IFS Fractal Generator (Blender Geometry Nodes)

![Project Status](https://img.shields.io/badge/status-phase%201-blue)
![Blender](https://img.shields.io/badge/blender-4.0%2B-orange)
![License](https://img.shields.io/badge/license-MIT-green)

> A modular, open Geometry Nodes implementation of an **Iterated Function System (IFS)** fractal generator for procedural 3D art, mathematical exploration, and future AI agent integration.

---

## 🎯 Purpose

This project provides a **pure Geometry Nodes** approach to generating classic and custom fractals in Blender. It's designed as:

- **Educational Tool**: Learn IFS mathematics and procedural geometry
- **Production System**: Create fractal art for games, renders, and visualization
- **Research Platform**: Experiment with novel fractal configurations
- **MCP Integration Foundation**: Future-ready for AI agent control

---

## ✨ Features

### Current (Phase 1-2)
- 🔄 **Procedural Generation**: Pure Geometry Nodes using Repeat Zone
- 🎚️ **Adjustable Parameters**: Iterations, transforms, seed, and probabilities
- 🎨 **Color Mapping**: Automatic gradients based on iteration depth
- 📦 **Preset System**: JSON-based fractal configurations
- ⚡ **Performance Optimized**: Instancing-first approach with quality modes
- 🔧 **Modular Design**: Clean separation of node logic and data

### Classic Fractals Included
- **Barnsley Fern** (organic, 4 transforms)
- **Sierpiński Triangle** (geometric, 3 transforms)
- **Menger Cube** (3D volumetric, 20 transforms)

### Planned (Phase 3-5)
- 🖥️ **UI Add-on**: Custom Blender panel for easy interaction
- 🤖 **MCP Integration**: Natural language fractal generation via AI agents
- 📤 **Export Pipeline**: Automated GLB, PLY, Alembic, USD conversion
- 🌐 **Preset Marketplace**: Community-driven fractal library

---

## 📁 Repository Layout

```
IFS-Fractal-Generator/
├── docs/                        # 📚 Complete documentation
│   ├── architecture.md          # System design and technical details
│   ├── development-plan.md      # Phased roadmap and milestones
│   ├── glossary.md             # Terminology reference
│   ├── quick-reference.md      # Fast lookup guide
│   └── diagrams/               # Mermaid architecture diagrams
│       ├── system-overview.md
│       ├── data-flow.md
│       ├── folder-structure.md
│       └── interaction-map.md
│
├── src/                         # 💾 Core implementation
│   ├── geometry_nodes/
│   │   └── ifs_generator.blend # Main node group (coming soon)
│   ├── presets/                # Fractal configurations
│   │   ├── schema.json         # JSON validation schema
│   │   ├── barnsley.json       # Barnsley Fern preset
│   │   ├── sierpinski.json     # Sierpiński Triangle preset
│   │   └── menger.json         # Menger Cube preset
│   ├── utils/                  # Python utilities (future)
│   │   ├── preset_loader.py
│   │   └── validator.py
│   └── mcp/                    # MCP integration (future)
│
├── tests/                       # 🧪 Test suite (TDD approach)
│   ├── unit/                   # Fast unit tests (no Blender)
│   ├── integration/            # Integration tests (Blender API)
│   ├── presets/               # Preset validation tests
│   ├── fixtures/              # Test data and mocks
│   └── conftest.py            # Pytest configuration
│
└── assets/                      # 🎨 Visual resources
    ├── icons/                  # UI icons
    ├── reference_images/       # Mathematical diagrams
    └── preview_renders/        # Example outputs
```

---

## 🚀 Quick Start

### Prerequisites
- **Blender 4.0+** (Geometry Nodes with Repeat Zone support)
- Basic understanding of Geometry Nodes (helpful but not required)

### Installation (Phase 1 - Manual Setup)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/IFS-Fractal-Generator.git
   cd IFS-Fractal-Generator
   ```

2. **Open Blender** and load the node group:
   - File → Open → Navigate to `src/geometry_nodes/ifs_generator.blend`
   - Or append the node group to your existing project

3. **Apply to an object**:
   - Select an object (or create a cube)
   - Add Modifier → Geometry Nodes
   - Select "IFS_Generator" node group

4. **Adjust parameters**:
   - Iterations: 6-10 (start low!)
   - Seed: Any integer
   - Select output mode: Points, Instanced, or Realized

### Using Presets

**Manual Method** (Phase 1):
1. Open preset JSON file (e.g., `src/presets/barnsley.json`)
2. Copy parameter values
3. Manually enter into node group inputs

**Automated Method** (Phase 2 - Coming Soon):
```python
from utils.preset_loader import load_preset, apply_preset

preset = load_preset("barnsley")
apply_preset(preset, bpy.data.node_groups["IFS_Generator"])
```

---

## 📖 Documentation

### For New Users
Start here to understand the project:
1. [Glossary](./docs/glossary.md) - Learn terminology
2. [Quick Reference](./docs/quick-reference.md) - Common tasks and parameters
3. [System Overview Diagrams](./docs/diagrams/system-overview.md) - Visual architecture

### For Developers
Dive into technical details:
1. [Architecture](./docs/architecture.md) - Complete system design
2. [Development Plan](./docs/development-plan.md) - Milestones and roadmap
3. [Data Flow Diagrams](./docs/diagrams/data-flow.md) - How data moves through the system
4. [Interaction Maps](./docs/diagrams/interaction-map.md) - Component communication

### Quick Links
- 📐 **[Architecture Documentation](./docs/architecture.md)** - System design
- 📅 **[Development Roadmap](./docs/development-plan.md)** - Phases and milestones
- 📊 **[Visual Diagrams](./docs/diagrams/)** - Mermaid architecture diagrams
- 📚 **[Glossary](./docs/glossary.md)** - Terms and concepts
- ⚡ **[Quick Reference](./docs/quick-reference.md)** - Fast lookup

---

## 🎨 Example Presets

### Barnsley Fern
```json
{
  "name": "Barnsley Fern",
  "iterations": 10,
  "transforms": [
    {"scale": [0.85, 0.85, 0.85], "rotation": [0, 0, 2.5], "translation": [0, 1.6, 0], "weight": 0.85},
    {"scale": [0.04, 0.04, 0.04], "rotation": [0, 0, 0], "translation": [0, 0, 0], "weight": 0.07},
    {"scale": [0.2, 0.23, 0.2], "rotation": [0, 0, -50], "translation": [0, 1.6, 0], "weight": 0.07},
    {"scale": [0.15, 0.26, 0.15], "rotation": [0, 0, 49], "translation": [0, 0.44, 0], "weight": 0.01}
  ]
}
```

### Sierpiński Triangle
```json
{
  "name": "Sierpiński Triangle",
  "iterations": 8,
  "transforms": [
    {"scale": [0.5, 0.5, 0.5], "rotation": [0, 0, 0], "translation": [-0.5, -0.433, 0], "weight": 0.33},
    {"scale": [0.5, 0.5, 0.5], "rotation": [0, 0, 0], "translation": [0.5, -0.433, 0], "weight": 0.33},
    {"scale": [0.5, 0.5, 0.5], "rotation": [0, 0, 0], "translation": [0, 0.433, 0], "weight": 0.34}
  ]
}
```

See all presets in [`src/presets/`](./src/presets/).

---

## ⚡ Performance Guidelines

### Iteration Count vs. Point Count

| Transforms | Iter 6 | Iter 8 | Iter 10 | Iter 12 |
|------------|--------|--------|---------|---------|
| 2 | 64 | 256 | 1,024 | 4,096 |
| 3 | 729 | 6,561 | 59,049 | 531,441 |
| 4 | 4,096 | 65,536 | 1,048,576 | 16,777,216 |

**Formula**: `Points = Transforms ^ Iterations`

### Recommendations
- **Interactive Preview**: 6-8 iterations, Points mode
- **High Quality**: 10-11 iterations, Instanced mode
- **Final Export**: 12 iterations, Realized mode (careful with memory!)

### Optimization Tips
- Use instancing, avoid realization until export
- Enable preview mode during parameter adjustment
- Limit iteration depth for complex transforms
- Close other Blender files to free memory

---

## 🛠️ Development

### Development Methodology: Test-Driven Development (TDD)

This project follows **TDD principles**: Write tests first, then implement features.

**Red-Green-Refactor Cycle**:
1. 🔴 **Red**: Write failing test describing desired behavior
2. 🟢 **Green**: Write minimal code to make test pass
3. ♻️ **Refactor**: Improve code while keeping tests green

**Coverage Goals**:
- Minimum: 80% overall coverage
- Critical paths (preset loading, validation): 95%+
- Integration tests: 70%+

### Current Status: Phase 1
**In Progress**: Core Geometry Nodes implementation

- [x] Project structure and documentation
- [x] TDD workflow and test infrastructure
- [ ] Unit tests for preset loading
- [ ] Repeat Zone node network
- [ ] Integration tests for node group
- [ ] Transform application logic
- [ ] Color mapping system
- [ ] Preset schema definition

See [Development Plan](./docs/development-plan.md) for complete roadmap.

### Running Tests

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run all tests
pytest tests/

# Run unit tests only (fast)
pytest tests/unit/

# Run with coverage
pytest --cov=src --cov-report=html tests/

# Install pre-commit hooks
pre-commit install
```

### Contributing

Contributions welcome! Areas of interest:
- **Test Writing**: Expand test coverage (TDD approach)
- **Node Design**: Optimize repeat zone logic
- **Preset Creation**: New fractal configurations
- **Documentation**: Tutorials and examples
- **Testing**: Validate presets across Blender versions

### Setting Up Development Environment

1. **Fork and clone** the repository
   ```bash
   git clone https://github.com/yourusername/IFS-Fractal-Generator.git
   cd IFS-Fractal-Generator
   ```

2. **Install development dependencies**
   ```bash
   pip install -r requirements-dev.txt
   ```

3. **Install pre-commit hooks**
   ```bash
   pre-commit install
   ```

4. **Run tests to verify setup**
   ```bash
   pytest tests/unit/  # Should pass (will add tests in Phase 1)
   ```

5. **Install Blender 4.0+** for integration tests

6. **Read architecture docs**: [`docs/architecture.md`](./docs/architecture.md)

7. **Check development plan**: [`docs/development-plan.md`](./docs/development-plan.md)

8. **Follow TDD workflow**:
   - Write test first (RED)
   - Implement feature (GREEN)
   - Refactor (keep GREEN)

9. **Pick a task** and open an issue to discuss

---

## 🔮 Future Vision

### Phase 3-4: UI & Performance
- Custom Blender add-on with preset browser
- Real-time parameter adjustment panel
- Performance profiling and optimization
- Batch rendering utilities

### Phase 5: MCP Integration
- Natural language fractal generation
- Conversational parameter refinement
- Automated export workflows
- Agent-driven exploration

**Example Agent Interaction**:
```
User: "Create a fern-like fractal with purple colors"
Agent: [Generates preset, applies to Blender, returns preview]
User: "Make it more compact"
Agent: [Adjusts scale parameters, updates preview]
User: "Perfect! Export as GLB"
Agent: [Exports geometry, provides download link]
```

### Phase 6: Ecosystem
- Community preset marketplace
- Cloud rendering integration
- Collaborative editing features
- Extended fractal types (L-systems, DLA)

---

## 📚 Learning Resources

### IFS Theory
- **"Fractals Everywhere"** by Michael Barnsley (the classic text)
- [Wikipedia: Iterated Function System](https://en.wikipedia.org/wiki/Iterated_function_system)
- [Chaos Game Method](https://en.wikipedia.org/wiki/Chaos_game)

### Blender Geometry Nodes
- [Official Blender Manual](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/)
- [Geometry Nodes Cookbook](https://www.youtube.com/watch?v=kMDB7c0ZiKA) (Tutorial)
- [Blender Artists Forum](https://blenderartists.org/c/geometry-nodes/68)

### MCP (Future)
- [Model Context Protocol Spec](https://modelcontextprotocol.io)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)

---

## 🤝 Community

- **Issues**: [GitHub Issues](https://github.com/yourusername/IFS-Fractal-Generator/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/IFS-Fractal-Generator/discussions)
- **Documentation**: [`docs/`](./docs/) folder

### Support
- Check [Quick Reference](./docs/quick-reference.md) for common issues
- Read [Glossary](./docs/glossary.md) for terminology
- Review [Troubleshooting](./docs/quick-reference.md#-troubleshooting) section

---

## 📜 License

This project is licensed under the **MIT License** - see LICENSE file for details.

### Third-Party Licenses
- **Blender**: GPL v3
- **Python**: PSF License
- **Mermaid.js** (for diagrams): MIT License

---

## ✨ Acknowledgments

- **Michael Barnsley**: For IFS theory and the iconic Barnsley Fern
- **Blender Foundation**: For Geometry Nodes and ongoing development
- **Anthropic**: For MCP specification enabling AI integration
- **Community Contributors**: All preset creators and documentation improvers

---

## 🗺️ Project Roadmap

| Phase | Timeline | Status | Key Deliverables |
|-------|----------|--------|------------------|
| **Phase 1**: Core Implementation | Weeks 1-3 | 🔄 In Progress | Working node group |
| **Phase 2**: Preset System | Weeks 4-5 | 🔜 Planned | 5+ JSON presets |
| **Phase 3**: Performance | Weeks 6-7 | 📋 Future | 60fps target |
| **Phase 4**: UI Layer | Weeks 8-10 | 📋 Future | Installable add-on |
| **Phase 5**: MCP Integration | Weeks 11-14 | 📋 Future | Agent workflows |
| **Phase 6**: Ecosystem | Ongoing | 💡 Concept | Community features |

---

## 📞 Contact

- **Project Lead**: [Your Name]
- **Email**: your.email@example.com
- **GitHub**: [@yourusername](https://github.com/yourusername)

---

## 🌟 Star History

If you find this project useful, please consider giving it a star! ⭐

---

**Built with ❤️ for the intersection of mathematics, art, and AI**

---

### Quick Navigation

- [📖 Full Documentation](./docs/)
- [🎯 Quick Start](#-quick-start)
- [📊 Development Plan](./docs/development-plan.md)
- [🎨 Create Your Own Preset](./docs/quick-reference.md#adding-a-new-preset)
- [🐛 Report an Issue](https://github.com/yourusername/IFS-Fractal-Generator/issues)

