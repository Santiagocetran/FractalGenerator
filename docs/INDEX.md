# Documentation Index - Visual Navigation

Quick visual guide to navigate the IFS Fractal Generator documentation.

---

## 📖 Documentation Tree

```
📁 docs/
│
├── 📄 INDEX.md (this file)
│   └── Quick visual navigation
│
├── 📄 README.md
│   └── Documentation hub, reading guides, navigation
│
├── 📄 DOCUMENTATION_SUMMARY.md
│   └── Complete overview of all deliverables
│
├── 📄 architecture.md ⭐
│   ├── § 1. Project Overview
│   ├── § 2. Core Architecture Components
│   ├── § 3. Data Flow Architecture
│   ├── § 4. Technical Constraints
│   ├── § 5. Integration Points
│   ├── § 6. System Boundaries
│   ├── § 7. Quality Attributes
│   └── § 8. Architectural Risks
│
├── 📄 development-plan.md ⭐
│   ├── Phase 1: Core Geometry Nodes (3 weeks)
│   ├── Phase 2: Preset System (2 weeks)
│   ├── Phase 3: Performance (2 weeks)
│   ├── Phase 4: UI Layer (3 weeks)
│   ├── Phase 5: MCP Integration (4 weeks)
│   ├── Phase 6: Ecosystem (ongoing)
│   └── Timeline & Success Metrics
│
├── 📄 glossary.md
│   ├── Mathematical Concepts (13 terms)
│   ├── Blender Terms (10 terms)
│   ├── Project-Specific (12 terms)
│   ├── Technical Terms (8 terms)
│   ├── File/Folder Terms (11 terms)
│   ├── UI/UX Terms (4 terms)
│   ├── Performance Terms (7 terms)
│   ├── Future Concepts (6 terms)
│   └── Acronyms (20)
│
├── 📄 quick-reference.md
│   ├── Common Tasks
│   ├── Parameter Ranges
│   ├── Color Palettes
│   ├── Node Patterns
│   ├── Troubleshooting
│   ├── Performance Benchmarks
│   ├── Code Snippets
│   └── Tips & Tricks
│
└── 📁 diagrams/
    │
    ├── 📄 system-overview.md ⭐
    │   ├── 🔷 High-Level System Architecture
    │   ├── 🔷 Component Interaction Overview
    │   ├── 🔷 Technology Stack
    │   ├── 🔷 Deployment Architecture
    │   └── 🔷 Module Dependency Graph
    │
    ├── 📄 data-flow.md ⭐
    │   ├── 🔷 Core IFS Generation Flow
    │   ├── 🔷 Preset Loading Flow
    │   ├── 🔷 Parameter Update Flow
    │   ├── 🔷 Transform Application Logic
    │   ├── 🔷 Color Mapping Flow
    │   ├── 🔷 Export Pipeline Flow
    │   └── 🔷 MCP Agent Interaction Flow
    │
    ├── 📄 folder-structure.md
    │   ├── 🔷 Current Repository Structure
    │   ├── 🔷 Folder Organization by Function
    │   ├── 🔷 File Dependency Map
    │   ├── 🔷 Preset Organization Hierarchy
    │   ├── 🔷 Asset Organization Structure
    │   ├── 🔷 Documentation Structure
    │   └── 🔷 Module Import Structure
    │
    └── 📄 interaction-map.md
        ├── 🔷 User Workflow Sequence
        ├── 🔷 Preset Loading Interaction
        ├── 🔷 Real-Time Parameter Adjustment
        ├── 🔷 Node Group Internal Communication
        ├── 🔷 MCP Agent Workflow
        ├── 🔷 Multi-User Collaboration
        ├── 🔷 Batch Processing Workflow
        └── 🔷 Error Handling Flow

⭐ = Start here
🔷 = Mermaid diagram
```

---

## 🎯 Reading Paths by Goal

### Path 1: "I want to understand the project" (30 min)

```
1. /README.md (root)
   └─> Project overview
   
2. docs/architecture.md §1
   └─> System purpose and design
   
3. docs/diagrams/system-overview.md
   └─> Visual architecture
   
4. docs/glossary.md
   └─> Reference as needed
```

### Path 2: "I want to start developing" (45 min)

```
1. docs/README.md
   └─> Documentation orientation
   
2. docs/development-plan.md Phase 1
   └─> Current tasks
   
3. docs/diagrams/data-flow.md §1-4
   └─> Implementation flows
   
4. docs/quick-reference.md
   └─> Parameters and patterns
```

### Path 3: "I want to create presets" (20 min)

```
1. docs/quick-reference.md §1
   └─> Adding a new preset
   
2. docs/glossary.md
   └─> Understand terminology
   
3. docs/architecture.md §2.2
   └─> Preset system details
```

### Path 4: "I want to work on MCP integration" (60 min)

```
1. docs/architecture.md §2.3, §3.3
   └─> MCP architecture
   
2. docs/development-plan.md Phase 5
   └─> MCP milestones
   
3. docs/diagrams/data-flow.md §7
   └─> Agent interaction flow
   
4. docs/diagrams/interaction-map.md §5
   └─> MCP workflow sequence
```

### Path 5: "I want to understand performance" (30 min)

```
1. docs/architecture.md §4
   └─> Technical constraints
   
2. docs/quick-reference.md §6
   └─> Performance benchmarks
   
3. docs/development-plan.md Phase 3
   └─> Optimization approach
```

---

## 📊 Content Matrix

| Document | Conceptual | Technical | Visual | Practical |
|----------|-----------|-----------|--------|-----------|
| architecture.md | ████████░░ 80% | ████████░░ 80% | ███░░░░░░░ 30% | ████░░░░░░ 40% |
| development-plan.md | ██████░░░░ 60% | ████░░░░░░ 40% | ██░░░░░░░░ 20% | ████████░░ 80% |
| glossary.md | ██████████ 100% | ████░░░░░░ 40% | ░░░░░░░░░░ 0% | ████░░░░░░ 40% |
| quick-reference.md | ██░░░░░░░░ 20% | ████████░░ 80% | ░░░░░░░░░░ 0% | ██████████ 100% |
| system-overview.md | ████████░░ 80% | ██████░░░░ 60% | ██████████ 100% | ██░░░░░░░░ 20% |
| data-flow.md | ████░░░░░░ 40% | ████████░░ 80% | ██████████ 100% | ██████░░░░ 60% |
| folder-structure.md | ██░░░░░░░░ 20% | ████░░░░░░ 40% | ██████████ 100% | ████████░░ 80% |
| interaction-map.md | ████░░░░░░ 40% | ████████░░ 80% | ██████████ 100% | ████████░░ 80% |

---

## 🔍 Quick Lookup

### By Topic

| Topic | Primary Document | Secondary References |
|-------|------------------|---------------------|
| **IFS Algorithm** | architecture.md §2.1 | data-flow.md §1, glossary.md |
| **Geometry Nodes** | architecture.md §2.1 | interaction-map.md §4, glossary.md |
| **Preset System** | architecture.md §2.2 | data-flow.md §2, quick-reference.md |
| **MCP Integration** | architecture.md §2.3 | development-plan.md Phase 5, data-flow.md §7 |
| **Performance** | architecture.md §4.1 | development-plan.md Phase 3, quick-reference.md §6 |
| **Data Flow** | architecture.md §3 | data-flow.md (all), interaction-map.md |
| **File Structure** | folder-structure.md §1 | architecture.md §5.2 |
| **Development Phases** | development-plan.md | architecture.md §8 |
| **Parameters** | quick-reference.md §2 | architecture.md §2.2, glossary.md |
| **Troubleshooting** | quick-reference.md §5 | interaction-map.md §8 |

### By Question

| Question | Answer Location |
|----------|-----------------|
| What is this project? | README.md, architecture.md §1 |
| How does IFS work? | glossary.md "IFS", data-flow.md §1 |
| What technologies are used? | system-overview.md §3, architecture.md §5 |
| What's the development timeline? | development-plan.md Timeline Summary |
| How do I create a preset? | quick-reference.md §1, architecture.md §2.2 |
| What are valid parameter ranges? | quick-reference.md §2 |
| How does the node graph work? | interaction-map.md §4, data-flow.md §1 |
| What's planned for the future? | development-plan.md Phases 4-6, architecture.md §2.3 |
| How do I optimize performance? | quick-reference.md §5, development-plan.md Phase 3 |
| What risks exist? | architecture.md §8, development-plan.md Risk Management |

---

## 📐 Diagram Quick Reference

### Architecture Diagrams (5 total)
```
system-overview.md:
├─ §1 High-Level System (13 components, 4 layers)
├─ §2 Component Interaction (5 groups, data flow)
├─ §3 Technology Stack (5 layers, dependencies)
├─ §4 Deployment Architecture (future state)
└─ §5 Module Dependencies (15 modules)
```

### Data Flow Diagrams (7 total)
```
data-flow.md:
├─ §1 Core Generation (complete pipeline)
├─ §2 Preset Loading (sequence)
├─ §3 Parameter Update (real-time)
├─ §4 Transform Logic (iteration detail)
├─ §5 Color Mapping (attribute to visual)
├─ §6 Export Pipeline (format conversion)
└─ §7 MCP Agent (future, sequence)
```

### Structure Diagrams (7 total)
```
folder-structure.md:
├─ §1 Repository Structure (file tree)
├─ §2 Functional Organization (categories)
├─ §3 File Dependencies (imports)
├─ §4 Preset Hierarchy (JSON structure)
├─ §5 Asset Organization (media files)
├─ §6 Documentation Structure (docs layout)
└─ §7 Module Imports (Python)
```

### Interaction Diagrams (8 total)
```
interaction-map.md:
├─ §1 User Workflow (complete session)
├─ §2 Preset Loading (detailed sequence)
├─ §3 Parameter Adjustment (event loop)
├─ §4 Node Communication (internal flow)
├─ §5 MCP Workflow (agent interaction)
├─ §6 Collaboration (future, multi-user)
├─ §7 Batch Processing (automation)
└─ §8 Error Handling (recovery)
```

---

## 🎓 Learning Sequence

### Beginner (Never used Geometry Nodes)
```
Day 1: README.md + glossary.md (basics)
Day 2: system-overview.md (visual understanding)
Day 3: quick-reference.md (hands-on examples)
```

### Intermediate (Some GN experience)
```
Week 1: architecture.md + development-plan.md Phase 1-2
Week 2: All data-flow diagrams + quick-reference patterns
Week 3: Start implementation with Phase 1 milestones
```

### Advanced (Ready to contribute)
```
Session 1: Full architecture.md (2 hours)
Session 2: All diagrams (3 hours)
Session 3: Development plan + risk analysis (1 hour)
Session 4: Pick Phase 1 milestone and start coding
```

---

## 🔗 External Links

From documentation to external resources:

### Blender
- [Official Geometry Nodes Manual](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/)
- [Blender Python API](https://docs.blender.org/api/current/)
- [Blender Artists Forum](https://blenderartists.org/)

### Mathematics
- [Fractals Everywhere](https://archive.org/details/fractalseverywhe00barn) (Barnsley)
- [Wikipedia: IFS](https://en.wikipedia.org/wiki/Iterated_function_system)
- [Chaos Game](https://en.wikipedia.org/wiki/Chaos_game)

### MCP
- [Model Context Protocol](https://modelcontextprotocol.io)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)

### Tools
- [JSON Schema](https://json-schema.org/)
- [Mermaid Live Editor](https://mermaid.live)

---

## 📱 Mobile-Friendly Quick Access

### Most Viewed Files (Bookmark These)

1. **Quick Reference** - `docs/quick-reference.md`
   - Common tasks, parameters, troubleshooting

2. **Glossary** - `docs/glossary.md`
   - Terminology lookup

3. **Core Flow** - `docs/diagrams/data-flow.md` §1
   - How generation works

4. **Development Tasks** - `docs/development-plan.md`
   - What to work on next

5. **System Architecture** - `docs/architecture.md` §1-2
   - High-level understanding

---

## 🎯 Success Indicators

You'll know the documentation is working when:

- ✅ New contributors can understand the system in < 1 hour
- ✅ Developers reference quick-reference.md frequently
- ✅ Diagrams are shared in discussions
- ✅ Glossary eliminates terminology confusion
- ✅ Development plan guides implementation
- ✅ No "where do I find X?" questions

---

## 🔄 Documentation Versions

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-11-11 | Initial complete documentation |

---

## 📞 Documentation Feedback

Found something unclear? Want more detail on a topic?

- Open an issue with label `documentation`
- Suggest improvements via pull request
- Reference specific sections (e.g., "architecture.md §3.2")

---

**Happy Exploring! 🚀**

*This index is designed for both sequential reading and random access. Jump in wherever makes sense for your goals.*

---

**Quick Start**: Begin with [README.md](../README.md) → [architecture.md](./architecture.md) § 1 → [development-plan.md](./development-plan.md) Phase 1

