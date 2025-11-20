"""Manual node group creation script with explicit saving.

This script creates the IFS_Generator node group and ensures it's properly saved.
"""

import bpy


def create_minimal_ifs_generator():
    """Create a minimal IFS_Generator node group that actually saves."""
    
    # Clear everything first
    bpy.ops.wm.read_factory_settings(use_empty=True)
    
    # Remove existing if present
    if "IFS_Generator" in bpy.data.node_groups:
        bpy.data.node_groups.remove(bpy.data.node_groups["IFS_Generator"])
    
    # Create new node group
    node_group = bpy.data.node_groups.new("IFS_Generator", 'GeometryNodeTree')
    
    print(f"✓ Created node group: {node_group.name}")
    
    # Mark as asset or fake user to ensure it saves
    node_group.use_fake_user = True
    
    # Create interface
    tree = node_group.interface
    tree.clear()
    
    # Inputs
    tree.new_socket(name="Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    iter_input = tree.new_socket(name="Iterations", in_out='INPUT', socket_type='NodeSocketInt')
    iter_input.default_value = 8
    iter_input.min_value = 1
    iter_input.max_value = 12
    
    tree.new_socket(name="Seed", in_out='INPUT', socket_type='NodeSocketInt')
    tree.new_socket(name="Instance Mesh", in_out='INPUT', socket_type='NodeSocketGeometry')
    
    mode_input = tree.new_socket(name="Output Mode", in_out='INPUT', socket_type='NodeSocketInt')
    mode_input.default_value = 0
    mode_input.min_value = 0
    mode_input.max_value = 2
    
    # Output
    tree.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    
    print(f"✓ Created interface with {len([s for s in tree.items_tree if s.in_out == 'INPUT'])} inputs")
    
    # Create nodes
    nodes = node_group.nodes
    nodes.clear()
    
    # Group Input
    group_input = nodes.new('NodeGroupInput')
    group_input.location = (-400, 0)
    
    # Group Output  
    group_output = nodes.new('NodeGroupOutput')
    group_output.location = (400, 0)
    
    # For now, just pass through geometry (Phase 1.1 stub)
    # Points node
    points = nodes.new('GeometryNodePoints')
    points.location = (-200, 0)
    points.inputs['Count'].default_value = 1
    
    # Simple passthrough for now
    node_group.links.new(points.outputs[0], group_output.inputs[0])
    
    print(f"✓ Created {len(nodes)} nodes with {len(node_group.links)} links")
    
    # Create a test object with the modifier
    bpy.ops.mesh.primitive_cube_add()
    cube = bpy.context.active_object
    cube.name = "IFS_Test_Cube"
    
    # Add modifier
    mod = cube.modifiers.new(name="IFS_Generator", type='NODES')
    mod.node_group = node_group
    
    print(f"✓ Applied node group to test cube")
    
    return node_group


def main():
    print("=" * 60)
    print("Creating IFS_Generator Node Group (Minimal Version)")
    print("=" * 60)
    
    node_group = create_minimal_ifs_generator()
    
    # Save the file
    from pathlib import Path
    script_dir = Path(__file__).parent
    blend_path = script_dir / "ifs_generator.blend"
    
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))
    print(f"✓ Saved to {blend_path}")
    
    # Verify it saved
    print("\nVerification:")
    print(f"  - Node group exists: {'IFS_Generator' in bpy.data.node_groups}")
    print(f"  - Has fake user: {node_group.use_fake_user}")
    print(f"  - Node count: {len(node_group.nodes)}")
    print(f"  - Objects in scene: {len(bpy.data.objects)}")
    
    print("=" * 60)
    print("✓ Complete! Node group should now be saved.")
    print("\nTo use:")
    print("  1. Open: blender src/geometry_nodes/ifs_generator.blend")
    print("  2. You should see a cube with IFS_Generator modifier")
    print("  3. The node group is also available for other objects")
    print("=" * 60)


if __name__ == "__main__":
    main()

