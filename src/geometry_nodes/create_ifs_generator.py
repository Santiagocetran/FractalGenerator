"""Script to programmatically create the IFS_Generator node group in Blender.

This script creates the Phase 1.1 implementation of IFS_Generator with:
- Basic input interface (Iterations, Seed, Instance Mesh, Output Mode)
- Single point initialization
- Repeat Zone with iteration counter
- Iteration attribute storage

Usage:
    Run this script inside Blender's Python environment:
    
    blender --python src/geometry_nodes/create_ifs_generator.py
    
    Or from Blender's Text Editor:
    1. Open this file in Blender Text Editor
    2. Click "Run Script"

The script will create/update the IFS_Generator node group and save it to
src/geometry_nodes/ifs_generator.blend

See src/geometry_nodes/README.md for manual creation instructions.
"""

import bpy


def create_ifs_generator_node_group():
    """Create the IFS_Generator Geometry Nodes group.
    
    Implements Phase 1.1 specification:
    - Repeat Zone structure with iteration counter
    - Single point initialization
    - Iteration attribute storage on point domain
    
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
    group_output.location = (400, 0)
    group_output.name = "Group Output"
    
    # Create Mesh Line node for single point initialization
    # Note: In Blender 5.0+, use 'OFFSET' mode with count=1 for single point
    mesh_line = nodes.new('GeometryNodeMeshLine')
    mesh_line.location = (-600, -100)
    mesh_line.name = "Single Point Init"
    mesh_line.mode = 'OFFSET'  # Changed from 'POINTS' for Blender 5.0 compatibility
    mesh_line.inputs['Count'].default_value = 1  # Single point
    # Set offset to zero to create point at origin
    mesh_line.inputs['Offset'].default_value = (0.0, 0.0, 0.0)
    
    # Create Repeat Zone nodes
    repeat_input = nodes.new('GeometryNodeRepeatInput')
    repeat_input.location = (-400, 0)
    repeat_input.name = "Repeat Input"
    
    repeat_output = nodes.new('GeometryNodeRepeatOutput')
    repeat_output.location = (200, 0)
    repeat_output.name = "Repeat Output"
    
    # Create Index node for iteration counter
    index_node = nodes.new('GeometryNodeInputIndex')
    index_node.location = (-200, -150)
    index_node.name = "Iteration Index"
    
    # Create Store Named Attribute node for iteration storage
    store_attr = nodes.new('GeometryNodeStoreNamedAttribute')
    store_attr.location = (0, 0)
    store_attr.name = "Store Iteration"
    store_attr.data_type = 'INT'
    store_attr.domain = 'POINT'
    store_attr.inputs['Name'].default_value = "iteration"
    
    # Create links
    links = node_group.links
    
    # Group Input → Mesh Line (single point)
    links.new(mesh_line.outputs['Mesh'], repeat_input.inputs['Geometry'])
    
    # Group Input → Repeat Input (Iterations)
    links.new(group_input.outputs['Iterations'], repeat_input.inputs['Iterations'])
    
    # Inside Repeat Zone: Geometry → Store Attr → Output
    links.new(repeat_input.outputs['Geometry'], store_attr.inputs['Geometry'])
    
    # Index → Store Attr (Value)
    links.new(index_node.outputs['Index'], store_attr.inputs['Value'])
    
    # Store Attr → Repeat Output
    links.new(store_attr.outputs['Geometry'], repeat_output.inputs['Geometry'])
    
    # Repeat Output → Group Output
    links.new(repeat_output.outputs['Geometry'], group_output.inputs['Geometry'])
    
    # Organize with frames (optional, for visual clarity)
    create_node_frames(node_group)
    
    print(f"✓ Created IFS_Generator node group")
    print(f"  - {len(nodes)} nodes")
    print(f"  - {len(links)} connections")
    print(f"  - Phase 1.1: Repeat Zone with iteration counter")
    
    return node_group


def create_node_group_interface(node_group):
    """Create the input/output interface for IFS_Generator.
    
    Inputs:
    - Geometry (standard)
    - Iterations (Int, 1-12)
    - Seed (Int)
    - Instance Mesh (Geometry)
    - Output Mode (Int, 0-2)
    
    Outputs:
    - Geometry
    """
    interface = node_group.interface
    
    # Clear existing interface items (except default Geometry in/out)
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
    output_mode.default_value = 0  # 0=Points, 1=Instanced, 2=Realized
    output_mode.min_value = 0
    output_mode.max_value = 2
    
    # Add output: Geometry
    interface.new_socket(
        name="Geometry",
        in_out='OUTPUT',
        socket_type='NodeSocketGeometry'
    )
    
    print(f"✓ Created interface with {len([i for i in interface.items_tree if i.in_out == 'INPUT'])} inputs")


def create_node_frames(node_group):
    """Create organizational frames for node groups.
    
    Improves readability per .cursorrules guidelines.
    """
    nodes = node_group.nodes
    
    # Frame 1: Initialization
    init_frame = nodes.new('NodeFrame')
    init_frame.label = "Phase 1.1: Single Point Initialization"
    init_frame.name = "Initialization Frame"
    
    # Frame 2: Repeat Zone
    repeat_frame = nodes.new('NodeFrame')
    repeat_frame.label = "Phase 1.1: Repeat Zone with Iteration Counter"
    repeat_frame.name = "Repeat Zone Frame"
    
    # Assign nodes to frames
    if "Single Point Init" in nodes:
        nodes["Single Point Init"].parent = init_frame
    
    if "Repeat Input" in nodes:
        nodes["Repeat Input"].parent = repeat_frame
    if "Repeat Output" in nodes:
        nodes["Repeat Output"].parent = repeat_frame
    if "Iteration Index" in nodes:
        nodes["Iteration Index"].parent = repeat_frame
    if "Store Iteration" in nodes:
        nodes["Store Iteration"].parent = repeat_frame


def save_blend_file():
    """Save the blend file with IFS_Generator node group."""
    import os
    from pathlib import Path
    
    # Determine save path
    script_dir = Path(__file__).parent
    blend_path = script_dir / "ifs_generator.blend"
    
    # Save
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))
    print(f"✓ Saved to {blend_path}")


def main():
    """Main execution function."""
    print("=" * 60)
    print("Creating IFS_Generator Geometry Nodes Group")
    print("Phase 1.1: Basic Repeat Zone Structure")
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
    print("  3. Run integration tests:")
    print("     blender --background --python-expr \"import pytest; pytest.main(['tests/integration/'])\"")
    print("=" * 60)


if __name__ == "__main__":
    main()

