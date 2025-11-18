# IFS Fractal Generator: Development Plan

## Overview
This document outlines the phased development approach for the IFS Fractal Generator project, from core node implementation to advanced MCP integration and ecosystem expansion.

---

## Development Approach

**Methodology**: Test-Driven Development (TDD)

All development follows the Red-Green-Refactor cycle:
1. **Red**: Write failing test describing desired behavior
2. **Green**: Implement minimal code to make test pass
3. **Refactor**: Improve code quality while keeping tests green

**Coverage Goals**:
- Minimum: 80% overall coverage
- Critical paths (preset loading, validation): 95%+
- Integration tests: 70%+

## Development Phases

### Phase 1: Core Geometry Nodes Implementation
**Goal**: Build functional IFS generator with single preset  
**Duration**: 2-3 weeks  
**Status**: 🔄 In Progress  
**Testing**: TDD approach with pytest

#### Milestones

##### 1.1 Basic Repeat Zone Structure
- [ ] Write tests for node group interface (TDD)
- [ ] Create node group with input/output interface
- [ ] Write tests for iteration counter
- [ ] Implement Repeat Zone with iteration counter
- [ ] Set up point cloud initialization (single starting point)
- [ ] Test basic iteration without transforms

**Success Criteria**: Loop executes N times, outputs point count = N, all tests pass

##### 1.2 Single Transform Application
- [ ] Add Scale/Rotate/Translate node chain
- [ ] Connect transform parameters to group inputs
- [ ] Verify geometric transformation correctness
- [ ] Test with simple shapes (cube, sphere)

**Success Criteria**: Sierpiński triangle appears with 3 transforms at 0.5 scale

##### 1.3 Multi-Transform System
- [ ] Duplicate transform chain for 4-8 parallel branches
- [ ] Implement probabilistic selection (Random Value + Compare)
- [ ] Add weight normalization logic
- [ ] Test Barnsley Fern parameters

**Success Criteria**: Fern structure visible with correct proportions

##### 1.4 Color & Output Modulation
- [ ] Capture iteration index as attribute
- [ ] Build Color Ramp mapping system
- [ ] Add output mode switching (Points/Instanced/Realized)
- [ ] Implement instance mesh input

**Success Criteria**: Color gradient visible, mesh instancing works

#### Deliverables
- `ifs_generator.blend` with functional node group
- Test suite with 80%+ coverage
- Integration tests for node group
- Screenshot documentation of node graph
- Basic usage instructions in README

#### Technical Challenges
- **Challenge**: Repeat Zone state management complexity  
  **Solution**: Use Named Attributes for iteration tracking
  
- **Challenge**: Probabilistic branching in pure nodes  
  **Solution**: Random Value seeded by iteration + point index

---

### Phase 2: Preset System & Validation
**Goal**: JSON-based configuration with 3-5 working presets  
**Duration**: 1-2 weeks  
**Status**: 🔜 Planned

#### Milestones

##### 2.1 JSON Schema Design
- [ ] Define complete preset structure (see architecture.md)
- [ ] Create JSON schema file for validation
- [ ] Document required vs. optional fields
- [ ] Design versioning strategy

**Success Criteria**: Schema validates against example presets

##### 2.2 Preset Implementation
- [ ] Create `barnsley.json` (Barnsley Fern)
- [ ] Create `sierpinski.json` (Triangle)
- [ ] Create `menger.json` (Cube)
- [ ] Create `tree_01.json` (Experimental organic)
- [ ] Add reference images for each

**Success Criteria**: Each preset produces expected fractal form

##### 2.3 Python Preset Loader
- [ ] Write unit tests for preset loading (TDD)
- [ ] Implement load_preset() function
- [ ] Write tests for schema validation
- [ ] Implement validate_preset() function
- [ ] Write tests for error handling
- [ ] Add error handling for malformed files
- [ ] Write integration tests for node group application
- [ ] Implement apply_preset() function
- [ ] Achieve 90%+ test coverage for preset module

**Success Criteria**: All tests pass, preset loads correctly, 90%+ coverage

#### Deliverables
- 3-5 validated JSON presets
- `preset_loader.py` utility script with 90%+ test coverage
- Comprehensive test suite for preset validation
- Automated tests for all existing presets
- Preset gallery in `/assets/preview_renders/`

#### Technical Challenges
- **Challenge**: Mapping JSON to node inputs programmatically  
  **Solution**: Consistent naming convention, reflection-based assignment
  
- **Challenge**: Preset compatibility across Blender versions  
  **Solution**: Minimal API surface, fallback handling

---

### Phase 3: Performance Optimization
**Goal**: Smooth 60fps interaction at 8-10 iterations  
**Duration**: 1-2 weeks  
**Status**: 🔜 Planned

#### Milestones

##### 3.1 Profiling & Baseline
- [ ] Measure frame time at various iteration counts
- [ ] Identify bottleneck nodes (typically merge operations)
- [ ] Document memory usage per iteration
- [ ] Create performance test preset (worst-case scenario)

**Success Criteria**: Data-driven understanding of performance limits

##### 3.2 Instancing Optimization
- [ ] Ensure instances not realized until necessary
- [ ] Implement LOD (Level of Detail) switching
- [ ] Add frustum culling for large fractals
- [ ] Test viewport vs. render performance

**Success Criteria**: 2x performance improvement in viewport

##### 3.3 Preview/Final Mode
- [ ] Add `Preview Iterations` slider (defaults to 6)
- [ ] Add `Final Iterations` slider (defaults to 10-12)
- [ ] Automatic switching based on viewport interaction
- [ ] Warning UI for high iteration counts

**Success Criteria**: No viewport lag during parameter adjustment

#### Deliverables
- Performance optimization documentation
- Benchmarking results table
- User guidelines for iteration limits

#### Technical Challenges
- **Challenge**: Blender's dependency graph rebuilds entire tree on change  
  **Solution**: Minimize node connections, use driver tricks
  
- **Challenge**: Instance realization unavoidable for some outputs  
  **Solution**: Clear mode separation, export-time realization only

---

### Phase 4: UI & User Experience
**Goal**: Polished interface for non-technical users  
**Duration**: 2-3 weeks  
**Status**: 📋 Future

#### Milestones

##### 4.1 Blender Add-on Wrapper
- [ ] Create add-on structure (`__init__.py`, register/unregister)
- [ ] Custom panel in N-panel sidebar
- [ ] Preset dropdown menu
- [ ] One-click fractal addition to scene

**Success Criteria**: Add-on installable via Blender preferences

##### 4.2 Interactive Parameter Controls
- [ ] Sliders for common parameters (iterations, seed)
- [ ] Transform editor (visual grid for 8 transforms)
- [ ] Color palette picker
- [ ] Live preview toggle

**Success Criteria**: All parameters adjustable without node editor

##### 4.3 Preset Management UI
- [ ] Import/export preset buttons
- [ ] Save current configuration as new preset
- [ ] Delete/rename preset operations
- [ ] Community preset browser (local only, phase 1)

**Success Criteria**: Complete preset lifecycle within Blender UI

#### Deliverables
- Installable `.zip` add-on
- Video tutorial (2-5 minutes)
- Updated README with UI screenshots

#### Technical Challenges
- **Challenge**: Blender UI API quirks and limitations  
  **Solution**: Reference official add-on examples, community patterns
  
- **Challenge**: Keeping UI in sync with node group state  
  **Solution**: Property callbacks, careful event handling

---

### Phase 5: MCP Integration
**Goal**: Natural language fractal generation via agent  
**Duration**: 3-4 weeks  
**Status**: 📋 Future

#### Milestones

##### 5.1 MCP Server Foundation
- [ ] Python MCP server setup (using official SDK)
- [ ] Tool definitions: `generate_fractal`, `list_presets`, `modify_parameters`
- [ ] Blender API bridge (server runs in background, calls Blender)
- [ ] Testing with Claude Desktop or compatible client

**Success Criteria**: Agent can list presets and describe them

##### 5.2 Preset Generation Tool
- [ ] `generate_fractal` tool accepts natural language description
- [ ] LLM generates valid JSON preset from description
- [ ] Validation and application to active scene
- [ ] Return preview image to agent

**Success Criteria**: "Create a fern-like fractal" produces working result

##### 5.3 Parameter Refinement Loop
- [ ] `modify_parameters` tool for iterative adjustments
- [ ] Multi-turn conversation support
- [ ] Visual feedback (screenshot) after each change
- [ ] Preset saving from conversation

**Success Criteria**: Agent can refine fractal through 5+ interactions

##### 5.4 Advanced Agent Workflows
- [ ] Batch generation ("create 10 tree variations")
- [ ] Animation sequencing (keyframe iteration count)
- [ ] Export automation (GLB, PLY, etc.)
- [ ] Preset comparison ("which is more compact?")

**Success Criteria**: Complex multi-step workflows via natural language

#### Deliverables
- MCP server implementation (`/src/mcp/server.py`)
- Agent prompt templates and examples
- Integration documentation
- Demo video with Claude Desktop

#### Technical Challenges
- **Challenge**: Blender not designed for headless API control  
  **Solution**: Use `bpy` in background mode, or run server in Blender's Python
  
- **Challenge**: Describing visual concepts to LLM  
  **Solution**: Rich context (reference images, mathematical descriptions)
  
- **Challenge**: LLM hallucinating invalid parameters  
  **Solution**: Strict JSON schema validation, error feedback loop

---

### Phase 6: Ecosystem Expansion
**Goal**: Community features and advanced capabilities  
**Duration**: Ongoing  
**Status**: 💡 Conceptual

#### Potential Features

##### 6.1 Preset Marketplace
- [ ] Cloud-hosted preset library
- [ ] Rating and commenting system
- [ ] Auto-update mechanism
- [ ] Creator attribution

##### 6.2 Advanced Fractal Types
- [ ] L-system integration
- [ ] Strange attractor support
- [ ] Hybrid IFS/DLA systems
- [ ] Parametric curve fractals

##### 6.3 Rendering Enhancements
- [ ] Procedural shader presets
- [ ] HDRI lighting setups
- [ ] Camera animation templates
- [ ] Post-processing filters

##### 6.4 Collaboration Features
- [ ] Preset versioning (Git-like)
- [ ] Blend file merging
- [ ] Shared workspaces
- [ ] Live co-editing (exploratory)

---

## Risk Management

### Critical Path Items
1. **Repeat Zone complexity**: Could block Phase 1  
   - Mitigation: Prototype early, consult Blender docs/forums
   
2. **Performance limitations**: Could delay Phase 3  
   - Mitigation: Set realistic iteration caps, progressive enhancement
   
3. **MCP protocol instability**: Could delay Phase 5  
   - Mitigation: Build clean abstraction layer, stay updated with spec

### Dependency Management
- **Blender Version**: Target 4.0+, test on 4.2 LTS
- **Python Version**: 3.10+ (Blender bundled)
- **MCP SDK**: Pin specific version, monitor updates

---

## Success Metrics

### Phase 1-2 (Core + Presets)
- [ ] 3 fractals render correctly
- [ ] Zero crashes in normal usage
- [ ] GitHub repository has clear README

### Phase 3-4 (Performance + UI)
- [ ] 60fps at 8 iterations confirmed
- [ ] 5 non-technical users can use add-on without help
- [ ] Tutorial video reaches 100+ views

### Phase 5 (MCP)
- [ ] Agent successfully generates 10 novel fractals
- [ ] 90%+ of agent-generated presets are valid
- [ ] Community adopts at least 3 agent-created presets

---

## Timeline Summary

| Phase | Duration | Cumulative Time | Key Deliverable |
|-------|----------|-----------------|-----------------|
| 1. Core Implementation | 3 weeks | 3 weeks | Working node group |
| 2. Preset System | 2 weeks | 5 weeks | 5 JSON presets |
| 3. Performance | 2 weeks | 7 weeks | 60fps target |
| 4. UI Layer | 3 weeks | 10 weeks | Installable add-on |
| 5. MCP Integration | 4 weeks | 14 weeks | Agent interaction |
| 6. Ecosystem | Ongoing | N/A | Community features |

**Target for MVP (Phase 1-3)**: 7 weeks  
**Target for Public Release (Phase 1-4)**: 10 weeks  
**Target for MCP Demo (Phase 1-5)**: 14 weeks

---

## Next Actions
1. Begin Phase 1.1 (Repeat Zone structure)
2. Set up Git repository with initial structure
3. Create project board for task tracking
4. Identify Blender node reference materials

For technical architecture details, see `/docs/architecture.md`.  
For visual system diagrams, see `/docs/diagrams/`.

