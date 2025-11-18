# IFS_Generator Geometry Nodes

This directory contains Blender `.blend` files with the IFS Fractal Generator Geometry Nodes groups.

## Phase 1.1: Creating the IFS_Generator Node Group

### Overview

The `IFS_Generator` is the core Geometry Nodes group that implements the Iterated Function System fractal algorithm. In Phase 1.1, we're creating the basic structure with a Repeat Zone and iteration counter, without transforms yet.

### Step-by-Step Implementation Guide

#### 1. Create the Blend File and Node Group

1. Open Blender 4.0 or later
2. Create a new file
3. Switch to the Geometry Nodes workspace
4. Create a new Geometry Nodes modifier on the default cube
5. In the Geometry Nodes editor, click the "New" button to create a new node group
6. Rename the node group to **`IFS_Generator`**

#### 2. Set Up Input Interface

Configure the node group inputs (in the Group Input node or via the interface panel):

| Input Name | Type | Default | Min | Max | Description |
|------------|------|---------|-----|-----|-------------|
| `Geometry` | Geometry | - | - | - | Input geometry (standard) |
| `Iterations` | Integer | 8 | 1 | 12 | Number of IFS iterations |
| `Seed` | Integer | 0 | - | - | Random seed for deterministic results |
| `Instance Mesh` | Geometry | - | - | - | Mesh to instance at each point |
| `Output Mode` | Integer | 0 | 0 | 2 | 0=Points, 1=Instanced, 2=Realized |

**To add inputs:**
1. Select the Group Input node
2. In the properties panel (N), go to the Group tab
3. Click "+" to add new inputs
4. Set names, types, and default values as specified above
5. For `Iterations`, set min=1 and max=12 in the properties

#### 3. Initialize Single Point (Phase 1.1)

Before the Repeat Zone, we need to initialize the starting point cloud:

**Nodes to add:**
1. **Mesh Line** node (or **Points** node)
   - Set Count to 1
   - This creates a single point at the origin
   - Connect to the Repeat Zone input

**Node connections:**
```
Group Input → Mesh Line (Count=1) → Repeat Zone Input
```

#### 4. Create the Repeat Zone Structure

**Add Repeat Zone:**
1. Add → Flow → **Repeat Zone** (Blender 4.0+)
2. This creates two nodes: Repeat Input and Repeat Output
3. Set the Iterations from the Group Input:
   - Connect Group Input → Iterations to Repeat Zone → Iterations

**Basic structure:**
```
Mesh Line → Repeat Input (Iterations from Group) → [loop body] → Repeat Output → Group Output
```

#### 5. Implement Iteration Counter (Phase 1.1 Core Feature)

Inside the Repeat Zone, we need to capture the iteration index as an attribute:

**Nodes to add inside loop:**
1. **Index** node (Geometry → Read → Index)
   - This provides the loop index (0, 1, 2, ...)
2. **Store Named Attribute** node
   - Name: `iteration`
   - Data Type: Integer
   - Domain: Point
   - Connect Index → Value
   - Connect incoming geometry to Geometry input
   - Connect output to Repeat Output

**Loop body structure:**
```
Repeat Input → Store Named Attribute (name="iteration", value=Index) → Repeat Output
```

#### 6. Set Up Output (Phase 1.1)

After the Repeat Zone, connect the output to the Group Output:

**Simple pass-through for Phase 1.1:**
```
Repeat Output → Group Output (Geometry)
```

**For Output Mode switching (optional in Phase 1.1):**
1. Add **Switch** node (Utilities → Switch)
2. Connect Repeat Output → Switch input
3. Connect Group Input → Output Mode → Switch selector
4. Add paths for Points/Instanced/Realized (can be stubbed for now)
5. Connect Switch output → Group Output

#### 7. Complete Phase 1.1 Node Graph

The complete Phase 1.1 node graph should look like this:

```
┌─────────────┐
│ Group Input │
└──┬──────┬───┘
   │      │
   │      └─────────────────────────┐
   │                                │ (Iterations)
   │                                ▼
   │                      ┌─────────────────┐
   │                      │  Repeat Input   │◄─────┐
   │                      │  (Iterations)   │      │
   │                      └────────┬────────┘      │
   │                               │               │
   ▼                               ▼               │
┌────────┐                   ┌─────────┐          │
│ Mesh   │────────────────►  │  Index  │          │
│ Line   │                   └────┬────┘          │
│(Count=1)                        │               │
└────────┘                        ▼               │
                        ┌──────────────────┐      │
                        │ Store Named Attr │      │
                        │ name="iteration" │      │
                        │ domain=Point     │      │
                        └────────┬─────────┘      │
                                 │                │
                                 ▼                │
                       ┌─────────────────┐        │
                       │  Repeat Output  │────────┘
                       └────────┬────────┘
                                │
                                ▼
                       ┌─────────────┐
                       │Group Output │
                       │ (Geometry)  │
                       └─────────────┘
```

#### 8. Save the Blend File

1. Save the file as `ifs_generator.blend` in this directory
2. Ensure the node group is named exactly **`IFS_Generator`**
3. Test the node group:
   - Set Iterations to different values (1, 4, 8, 12)
   - Verify it produces points with the `iteration` attribute
   - Use the Spreadsheet editor to inspect attributes

#### 9. Verify Against Integration Tests

Once saved, the integration tests can be run:

```bash
# From project root, with Blender in PATH
blender --background src/geometry_nodes/ifs_generator.blend \
    --python-expr "import sys; sys.path.insert(0, '.'); import pytest; pytest.main(['tests/integration/test_node_group.py'])"
```

The tests in `tests/integration/test_node_group.py` will verify:
- ✓ Node group exists with correct name
- ✓ All required inputs are present with correct types
- ✓ Geometry output exists
- ✓ Node group applies without errors
- ✓ Iteration counts work for 1, 4, 8, 12
- ⚠ Iteration attribute tests (marked xfail until implementation is complete)

## Phase 1.2: Single Transform Application (Next Steps)

Phase 1.2 will add:
- Scale/Rotate/Translate node chains
- Connection of transform parameters to group inputs
- Single transform application to verify Sierpiński triangle

See `docs/development-plan.md` for details.

## Troubleshooting

### Issue: "IFS_Generator not found" in tests
- **Solution**: Ensure the node group is named exactly `IFS_Generator` (case-sensitive)
- **Solution**: Verify the .blend file is saved in `src/geometry_nodes/ifs_generator.blend`

### Issue: Tests fail with "Repeat Zone not found"
- **Solution**: Requires Blender 4.0+ for Repeat Zone support
- **Solution**: Check Blender version: Help → About Blender

### Issue: Iteration attribute not stored
- **Solution**: Verify Store Named Attribute node is inside the Repeat Zone loop
- **Solution**: Check that Domain is set to "Point" and Name is exactly "iteration"
- **Solution**: Use Spreadsheet editor (Shift+F3) to inspect geometry attributes

### Issue: Performance lag in Blender
- **Solution**: Reduce Iterations to 6 or less for interactive work
- **Solution**: Use Points output mode instead of Instanced/Realized
- **Solution**: Hide other objects in scene

## Node Organization Best Practices

Per `.cursorrules` Geometry Nodes Guidelines:

1. **Use Frames** to group related nodes:
   - Frame 1: "Initialization" (Mesh Line)
   - Frame 2: "Repeat Zone Loop" (Repeat nodes, Index, Store Attr)
   - Frame 3: "Output Processing" (Switch, modulation)

2. **Name all nodes descriptively**:
   - Not "Math.001", but "Scale Transform"
   - Not "Store Named Attribute", but "Store Iteration Index"

3. **Use Reroutes sparingly**:
   - Prefer clean direct connections
   - Only use reroutes for long-distance connections

4. **Add Annotation nodes** for complex logic:
   - Document the Repeat Zone structure
   - Explain the iteration counter logic

## References

- Architecture: `docs/architecture.md` §2.1 (Geometry Nodes Engine)
- Development Plan: `docs/development-plan.md` Phase 1.1
- Quick Reference: `docs/quick-reference.md` (Node Setup Patterns)
- Tests: `tests/integration/test_node_group.py`

---

**Status**: Phase 1.1 Implementation  
**Last Updated**: 2025-11-18  
**Blender Version**: 4.0+

