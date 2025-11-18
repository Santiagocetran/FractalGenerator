# Blender 5.0 Compatibility Notes

## Issue: API Changes in Blender 5.0

Blender 5.0 has significant changes to the Geometry Nodes API, particularly around Repeat Zones.

### What Changed

1. **Mesh Line Node**: `mode = 'POINTS'` no longer exists
   - Solution: Use `GeometryNodePoints` instead

2. **Repeat Zone Connections**: Geometry is not directly connected via named inputs
   - The Repeat Input/Output nodes use a custom item system
   - Empty string `''` sockets are the geometry pass-through

###

 Current Status

✅ **Working**:
- Node group interface created (Iterations, Seed, Instance Mesh, Output Mode)
- Points node for single point initialization
- Repeat Zone nodes created
- Store Named Attribute node created
- Most connections work

⚠️ **Partial**:
- Repeat Zone geometry flow needs manual connection in Blender GUI
- The script creates 4/5 connections automatically

### Manual Steps Required (Blender 5.0)

After running the creation script, open Blender and:

1. Open `src/geometry_nodes/ifs_generator.blend`
2. Go to Geometry Nodes editor
3. Select the `IFS_Generator` node group
4. **Manually connect**:
   - `Points` node → `Repeat Input` (the empty socket)
   - `Repeat Input` → `Store Named Attribute` Geometry input

### Recommended Workflow for Blender 5.0

**Option 1: Use the Script + Manual Finishing**
```bash
# Run script to create most of the setup
blender --background --python src/geometry_nodes/create_ifs_generator_v5.py

# Then open in GUI to finish connections
blender src/geometry_nodes/ifs_generator.blend
```

**Option 2: Full Manual Creation**
Follow the step-by-step guide in `src/geometry_nodes/README.md`

### Testing with Blender 5.0

The integration tests were written for Blender 4.x API. They may need updates for Blender 5.0:

```python
# Blender 4.x
modifier["Input_2"] = iterations

# Blender 5.0 - TBD, API may have changed
# Need to investigate new modifier input access method
```

### Node Group Structure (Phase 1.1)

```
Points (Count=1)
        ↓
[To be manually connected to Repeat Input empty socket]
        ↓
Repeat Input → Store Named Attribute (iteration) → Repeat Output
                        ↑
                   Index Node
        ↓
Group Output
```

### Files Updated for Blender 5.0

1. `src/geometry_nodes/create_ifs_generator_v5.py` - New Blender 5.0 compatible version
   - Uses `GeometryNodePoints` instead of `MeshLine`
   - Debug output to show socket names
   - Attempts smart socket matching

2. `src/geometry_nodes/create_ifs_generator.py` - Original (Blender 4.x)
   - Uses `MeshLine` with `POINTS` mode
   - Direct socket name connections

### Recommendation

For now, **manually create the node group** using the guide in `src/geometry_nodes/README.md`. This ensures compatibility and allows you to understand the node structure better.

Once Blender 5.0's Geometry Nodes API stabilizes and documentation is available, we can update the script to be fully automated again.

### Future Work

- [ ] Research Blender 5.0 Repeat Zone API
- [ ] Update script for full automation in Blender 5.0
- [ ] Update integration tests for Blender 5.0 compatibility
- [ ] Test on both Blender 4.x and 5.0

---

**Blender Version Tested**: 5.0.0 (hash a37564c4df7a)  
**Date**: 2025-11-18  
**Status**: Partially automated - manual finishing required

