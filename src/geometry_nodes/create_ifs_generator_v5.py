"""Script to programmatically create the IFS_Generator node group in Blender 5.0+.

This is an updated version compatible with Blender 5.0 API changes.

Usage:
    blender --background --python src/geometry_nodes/create_ifs_generator_v5.py

See src/geometry_nodes/README.md for manual creation instructions.
"""

import bpy


def debug_node_sockets(node, name="Node"):
    """Print available sockets for debugging."""
    print(f"\n{name} ({node.bl_idname}):")
    print("  Inputs:")
    for inp in node.inputs:
        print(f"    - {inp.name} ({inp.type})")
    print("  Outputs:")
    for out in node.outputs:
        print(f"    - {out.name} ({out.type})")


def create_ifs_generator_node_group():
    """Create the IFS_Generator Geometry Nodes group for Blender 5.0+.
    
    Returns:
        bpy.types.GeometryNodeTree: The created node group
    """
    # Remove existing IFS_Generator if it exists
    if "IFS_Generator" in bpy.data.node_groups:
        bpy.data.node_groups.remove(bpy.data.node_groups["IFS_Generator"])
    
    # Create new Geometry Nodes group
    node_group = bpy.data.node_groups.new("IFS_Generator", 'GeometryNodeTree')
    
    # Create node group interface (inputs/outputs)
    create_node_group_interface(node_group)
    
    # Create nodes
    nodes = node_group.nodes
    nodes.clear()
    
    # Create Group Input and Output nodes
    group_input = nodes.new('NodeGroupInput')
    group_input.location = (-800, 0)
    group_input.name = "Group Input"
    
    group_output = nodes.new('NodeGroupOutput')
    group_output.location = (600, 0)
    group_output.name = "Group Output"
    
    # Create Points node for single point initialization (simpler for Blender 5.0)
    points = nodes.new('GeometryNodePoints')
    points.location = (-600, -100)
    points.name = "Single Point Init"
    points.inputs['Count'].default_value = 1  # Single point
    
    print(f"✓ Created Points node for single point initialization")
    
    # Create Repeat Zone nodes
    repeat_input = nodes.new('GeometryNodeRepeatInput')
    repeat_input.location = (-350, 0)
    repeat_input.name = "Repeat Input"
    
    repeat_output = nodes.new('GeometryNodeRepeatOutput')
    repeat_output.location = (350, 0)
    repeat_output.name = "Repeat Output"
    
    print(f"✓ Created Repeat Zone nodes")
    
    # Debug: Print available sockets
    debug_node_sockets(points, "Points Node")
    debug_node_sockets(repeat_input, "Repeat Input")
    debug_node_sockets(repeat_output, "Repeat Output")
    
    # Create Index node for iteration counter
    index_node = nodes.new('GeometryNodeInputIndex')
    index_node.location = (-100, -150)
    index_node.name = "Iteration Index"
    
    # Create Store Named Attribute node for iteration storage
    store_attr = nodes.new('GeometryNodeStoreNamedAttribute')
    store_attr.location = (100, 0)
    store_attr.name = "Store Iteration"
    store_attr.data_type = 'INT'
    store_attr.domain = 'POINT'
    
    # Set the attribute name using the Selection input
    # In Blender 5.0, this might be done differently
    if 'Name' in store_attr.inputs:
        store_attr.inputs['Name'].default_value = "iteration"
    elif hasattr(store_attr, 'attribute_name'):
        store_attr.attribute_name = "iteration"
    
    print(f"✓ Created Store Named Attribute node")
    debug_node_sockets(store_attr, "Store Named Attribute")
    
    # Create links
    links = node_group.links
    
    print("\n📌 Creating links...")
    
    # Try to find the right socket names by inspecting
    try:
        # Points → Repeat Input
        points_out = next((s for s in points.outputs if s.type == 'GEOMETRY'), points.outputs[0])
        repeat_in_geom = next((s for s in repeat_input.inputs if s.type == 'GEOMETRY'), None)
        
        if repeat_in_geom:
            links.new(points_out, repeat_in_geom)
            print(f"  ✓ Connected Points → Repeat Input ({points_out.name} → {repeat_in_geom.name})")
        else:
            print(f"  ⚠ Could not find geometry input on Repeat Input node")
            print(f"     Available inputs: {[s.name for s in repeat_input.inputs]}")
        
        # Group Input → Repeat Input (Iterations)
        iterations_out = next((s for s in group_input.outputs if 'Iteration' in s.name), None)
        iterations_in = next((s for s in repeat_input.inputs if 'Iteration' in s.name), None)
        
        if iterations_out and iterations_in:
            links.new(iterations_out, iterations_in)
            print(f"  ✓ Connected Iterations ({iterations_out.name} → {iterations_in.name})")
        
        # Inside Repeat Zone: Repeat Input → Store Attr
        repeat_out_geom = next((s for s in repeat_input.outputs if s.type == 'GEOMETRY'), None)
        store_in_geom = next((s for s in store_attr.inputs if s.type == 'GEOMETRY' and 'Geometry' in s.name), None)
        
        if repeat_out_geom and store_in_geom:
            links.new(repeat_out_geom, store_in_geom)
            print(f"  ✓ Connected Repeat Input → Store Attr ({repeat_out_geom.name} → {store_in_geom.name})")
        
        # Index → Store Attr (Value)
        index_out = index_node.outputs[0]
        value_in = next((s for s in store_attr.inputs if 'Value' in s.name and s.type in ['INT', 'VALUE']), None)
        
        if value_in:
            links.new(index_out, value_in)
            print(f"  ✓ Connected Index → Store Attr Value ({index_out.name} → {value_in.name})")
        
        # Store Attr → Repeat Output
        store_out_geom = next((s for s in store_attr.outputs if s.type == 'GEOMETRY'), None)
        repeat_end_geom = next((s for s in repeat_output.inputs if s.type == 'GEOMETRY'), None)
        
        if store_out_geom and repeat_end_geom:
            links.new(store_out_geom, repeat_end_geom)
            print(f"  ✓ Connected Store Attr → Repeat Output ({store_out_geom.name} → {repeat_end_geom.name})")
        
        # Repeat Output → Group Output
        final_out = next((s for s in repeat_output.outputs if s.type == 'GEOMETRY'), None)
        group_out_geom = next((s for s in group_output.inputs if s.type == 'GEOMETRY'), None)
        
        if final_out and group_out_geom:
            links.new(final_out, group_out_geom)
            print(f"  ✓ Connected Repeat Output → Group Output ({final_out.name} → {group_out_geom.name})")
        
    except Exception as e:
        print(f"  ⚠ Error creating links: {e}")
        import traceback
        traceback.print_exc()
    
    print(f"\n✓ Created IFS_Generator node group")
    print(f"  - {len(nodes)} nodes")
    print(f"  - {len(links)} connections")
    print(f"  - Phase 1.1: Repeat Zone with iteration counter")
    
    return node_group


def create_node_group_interface(node_group):
    """Create the input/output interface for IFS_Generator."""
    interface = node_group.interface
    
    # Clear existing interface items
    interface.clear()
    
    # Add input: Geometry (standard input)
    interface.new_socket(
        name="Geometry",
        in_out='INPUT',
        socket_type='NodeSocketGeometry'
    )
    
    # Add input: Iterations
    iterations = interface.new_socket(
        name="Iterations",
        in_out='INPUT',
        socket_type='NodeSocketInt'
    )
    iterations.default_value = 8
    iterations.min_value = 1
    iterations.max_value = 12
    
    # Add input: Seed
    seed = interface.new_socket(
        name="Seed",
        in_out='INPUT',
        socket_type='NodeSocketInt'
    )
    seed.default_value = 0
    
    # Add input: Instance Mesh
    interface.new_socket(
        name="Instance Mesh",
        in_out='INPUT',
        socket_type='NodeSocketGeometry'
    )
    
    # Add input: Output Mode
    output_mode = interface.new_socket(
        name="Output Mode",
        in_out='INPUT',
        socket_type='NodeSocketInt'
    )
    output_mode.default_value = 0
    output_mode.min_value = 0
    output_mode.max_value = 2
    
    # Add output: Geometry
    interface.new_socket(
        name="Geometry",
        in_out='OUTPUT',
        socket_type='NodeSocketGeometry'
    )
    
    print(f"✓ Created interface with {len([i for i in interface.items_tree if i.in_out == 'INPUT'])} inputs")


def save_blend_file():
    """Save the blend file with IFS_Generator node group."""
    from pathlib import Path
    
    script_dir = Path(__file__).parent
    blend_path = script_dir / "ifs_generator.blend"
    
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))
    print(f"✓ Saved to {blend_path}")


def main():
    """Main execution function."""
    print("=" * 60)
    print("Creating IFS_Generator Geometry Nodes Group")
    print("Phase 1.1: Basic Repeat Zone Structure")
    print(f"Blender Version: {bpy.app.version_string}")
    print("=" * 60)
    
    # Create node group
    node_group = create_ifs_generator_node_group()
    
    # Save blend file
    save_blend_file()
    
    print("=" * 60)
    print("✓ IFS_Generator creation complete!")
    print("")
    print("Next steps:")
    print("  1. Open src/geometry_nodes/ifs_generator.blend in Blender")
    print("  2. Review the node group in Geometry Nodes editor")
    print("  3. Run integration tests (if pytest available in Blender)")
    print("=" * 60)


if __name__ == "__main__":
    main()

