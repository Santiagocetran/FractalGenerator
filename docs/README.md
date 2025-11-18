# Documentation Index

Welcome to the **IFS Fractal Generator** documentation. This folder contains comprehensive technical documentation, architecture diagrams, and development planning materials.

---

## 📚 Documentation Structure

### Core Documentation

| Document | Purpose | Audience |
|----------|---------|----------|
| [`architecture.md`](./architecture.md) | System architecture, component design, and technical decisions | Developers, Contributors |
| [`development-plan.md`](./development-plan.md) | Phased roadmap, milestones, and implementation strategy | Project Managers, Developers |
| [`glossary.md`](./glossary.md) | Terminology reference for project-specific concepts | All Users |

### Visual Diagrams

Located in [`diagrams/`](./diagrams/)

| Document | Purpose | Key Diagrams |
|----------|---------|--------------|
| [`system-overview.md`](./diagrams/system-overview.md) | High-level architecture visualization | Component relationships, technology stack, deployment |
| [`data-flow.md`](./diagrams/data-flow.md) | How data moves through the system | Generation flow, preset loading, parameter updates |
| [`folder-structure.md`](./diagrams/folder-structure.md) | Repository organization and navigation | File hierarchy, dependencies, module structure |
| [`interaction-map.md`](./diagrams/interaction-map.md) | Component communication patterns | Sequence diagrams, user workflows, error handling |

---

## 🎯 Quick Navigation

### I want to...

#### Understand the Project
- **Learn what this project does**: Start with [`../README.md`](../README.md)
- **See the big picture**: Read [`architecture.md`](./architecture.md) § 1-2
- **Understand terminology**: Check [`glossary.md`](./glossary.md)

#### Start Development
- **See what to build first**: Review [`development-plan.md`](./development-plan.md) Phase 1
- **Understand folder layout**: View [`diagrams/folder-structure.md`](./diagrams/folder-structure.md)
- **Know where to put files**: Check "Navigation Guide" in folder-structure docs

#### Contribute to the Project
- **Add a new preset**: See [`development-plan.md`](./development-plan.md) Phase 2.2
- **Extend node logic**: Review [`architecture.md`](./architecture.md) § 2.1
- **Work on MCP integration**: Start with [`development-plan.md`](./development-plan.md) Phase 5

#### Visualize System Behavior
- **How presets are loaded**: [`diagrams/data-flow.md`](./diagrams/data-flow.md) § 2
- **User interaction flow**: [`diagrams/interaction-map.md`](./diagrams/interaction-map.md) § 1
- **Component relationships**: [`diagrams/system-overview.md`](./diagrams/system-overview.md) § 1-2

---

## 📖 Reading Guide

### For New Contributors

**30-Minute Orientation**:
1. Read `architecture.md` § 1 (Overview) — 5 min
2. Skim `diagrams/system-overview.md` — 5 min
3. Review `development-plan.md` phases 1-2 — 10 min
4. Explore `diagrams/folder-structure.md` — 5 min
5. Reference `glossary.md` as needed — 5 min

**Deep Dive (2-3 hours)**:
1. Complete architecture document
2. All diagram files (review each Mermaid diagram)
3. Full development plan with milestone details
4. Explore actual code in `/src/` referencing documentation

### For Technical Decision-Makers

**Focus Areas**:
- `architecture.md` § 3-4 (Data Flow & Constraints)
- `architecture.md` § 8 (Architectural Risks)
- `development-plan.md` Timeline & Success Metrics
- `diagrams/system-overview.md` § 4 (Deployment)

### For UI/UX Designers

**Focus Areas**:
- `development-plan.md` Phase 4 (UI Layer)
- `diagrams/interaction-map.md` § 1 (User Workflow)
- `diagrams/interaction-map.md` § 3 (Real-Time Interaction)
- `architecture.md` § 7 (Quality Attributes: Usability)

### For AI/MCP Integrators

**Focus Areas**:
- `architecture.md` § 2.3 (MCP Integration Layer)
- `architecture.md` § 3.3 (Agent Flow)
- `development-plan.md` Phase 5 (MCP Integration)
- `diagrams/interaction-map.md` § 5 (MCP Agent Workflow)
- `diagrams/data-flow.md` § 7 (Future Agent Flow)

---

## 🔄 Documentation Maintenance

### Versioning
- Documentation reflects current state + planned features
- Dashed lines in diagrams indicate future/planned components
- Phase status in development plan updated regularly

### Updating Guidelines

**When to Update**:
- Architecture changes (new components, modified flows)
- Milestone completion (mark todos as done in dev plan)
- API changes (update sequence diagrams)
- New risks identified (add to architecture § 8)

**Who Updates**:
- Core contributors: All sections
- Feature developers: Relevant sections only
- Documentation lead: Consistency review

**Update Process**:
1. Make changes in feature branch
2. Update relevant diagrams (maintain Mermaid syntax)
3. Cross-reference between documents
4. Validate all Mermaid renders correctly
5. Submit PR with "docs:" prefix

---

## 🛠️ Working with Mermaid Diagrams

### Viewing Diagrams

**Option 1: GitHub** (recommended)
- View any `.md` file directly on GitHub
- Mermaid diagrams render automatically

**Option 2: VS Code**
- Install "Markdown Preview Mermaid Support" extension
- Use Markdown preview pane (Ctrl+Shift+V)

**Option 3: Online**
- Copy Mermaid code to [mermaid.live](https://mermaid.live)
- Edit and export as needed

### Editing Diagrams

**Syntax Validation**:
```bash
# Install mermaid CLI
npm install -g @mermaid-js/mermaid-cli

# Validate diagram
mmdc -i docs/diagrams/system-overview.md -o /tmp/test.png
```

**Best Practices**:
- Keep diagrams focused (one concept per diagram)
- Use consistent color scheme (see legend in system-overview.md)
- Include legends for complex diagrams
- Comment complex Mermaid logic

---

## 🔗 Related Resources

### External Documentation
- [Blender Geometry Nodes Manual](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/index.html)
- [Model Context Protocol Spec](https://spec.modelcontextprotocol.io/)
- [JSON Schema Reference](https://json-schema.org/)

### Project Resources
- **Source Code**: `/src/`
- **Presets**: `/src/presets/`
- **Assets**: `/assets/`
- **Examples**: `/examples/` (future)

### Community
- **Issues**: [GitHub Issues](https://github.com/yourusername/IFS-Fractal-Generator/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/IFS-Fractal-Generator/discussions)
- **Contributing**: See `CONTRIBUTING.md` (future)

---

## 📝 Documentation TODO

### Short Term
- [ ] Add glossary.md with IFS terminology
- [ ] Create getting-started guide for users
- [ ] Document preset JSON schema thoroughly
- [ ] Add troubleshooting section

### Medium Term
- [ ] API reference for Python utilities
- [ ] Node group interface documentation
- [ ] Performance tuning guide
- [ ] Video tutorial scripts

### Long Term
- [ ] MCP integration guide
- [ ] Advanced techniques documentation
- [ ] Community preset guidelines
- [ ] Internationalization strategy

---

## 📄 License

This documentation is part of the IFS Fractal Generator project.  
See the main LICENSE file for terms.

---

## ✨ Credits

**Documentation Authors**: Project Contributors  
**Diagrams**: Mermaid.js  
**Inspiration**: Mathematical beauty of fractal geometry  

---

**Last Updated**: 2025-11-11  
**Documentation Version**: 1.0  
**Project Status**: Phase 1 (Core Implementation)

