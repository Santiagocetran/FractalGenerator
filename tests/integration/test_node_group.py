"""Integration tests for IFS_Generator Geometry Nodes group.

These tests validate the node group interface and basic behavior when run
inside Blender's Python environment. Tests are skipped if bpy is unavailable.

Phase 1.1 Focus:
- Node group interface (inputs/outputs)
- Repeat Zone iteration counter
- Single point initialization
- Basic iteration behavior (no transforms yet)

To run these tests:
    blender --background --python-expr "import pytest; pytest.main(['tests/integration/'])"

See docs/development-plan.md Phase 1.1 for implementation details.
"""

import pytest

# Skip all tests in this module if bpy (Blender Python API) is not available
bpy = pytest.importorskip("bpy")


@pytest.fixture
def clean_scene():
    """Provide a clean Blender scene for each test.
    
    Resets to factory defaults before and after each test to ensure
    test isolation and prevent state leakage.
    """
    bpy.ops.wm.read_factory_settings(use_empty=True)
    yield bpy.context.scene
    bpy.ops.wm.read_factory_settings(use_empty=True)


@pytest.fixture
def ifs_node_group():
    """Provide the IFS_Generator node group.
    
    Returns:
        bpy.types.GeometryNodeTree: The IFS_Generator node group
        
    Raises:
        AssertionError: If IFS_Generator node group is not found
        
    Note:
        This fixture assumes the IFS_Generator node group exists in
        bpy.data.node_groups, typically loaded from
        src/geometry_nodes/ifs_generator.blend
    """
    node_group = bpy.data.node_groups.get("IFS_Generator")
    assert node_group is not None, (
        "IFS_Generator node group not found. "
        "Ensure src/geometry_nodes/ifs_generator.blend is loaded "
        "with the IFS_Generator node group defined."
    )
    return node_group


class TestNodeGroupInterface:
    """Test the IFS_Generator node group interface definition.
    
    Validates that all required inputs and outputs exist with correct
    types and constraints per architecture.md §2.1.
    """

    def test_node_group_exists(self, ifs_node_group):
        """Test that IFS_Generator node group exists and is accessible."""
        assert ifs_node_group is not None
        assert ifs_node_group.name == "IFS_Generator"
        assert ifs_node_group.type == 'GEOMETRY'

    def test_iterations_input_exists(self, ifs_node_group):
        """Test that Iterations input exists with correct type and constraints.
        
        Per architecture.md §4.1: Max iterations = 12 (hard cap)
        """
        iterations_input = ifs_node_group.interface.items_tree.get("Iterations")
        assert iterations_input is not None, "Iterations input not found"
        
        # Check input type is Integer
        assert iterations_input.socket_type == 'NodeSocketInt', (
            f"Iterations should be Integer, got {iterations_input.socket_type}"
        )
        
        # Check constraints (min=1, max=12 per architecture.md §4.1)
        # Note: Accessing min_value/max_value depends on Blender version
        # This is a basic existence check; detailed constraint validation
        # may require accessing the input socket properties

    def test_seed_input_exists(self, ifs_node_group):
        """Test that Seed input exists with correct type."""
        seed_input = ifs_node_group.interface.items_tree.get("Seed")
        assert seed_input is not None, "Seed input not found"
        assert seed_input.socket_type == 'NodeSocketInt', (
            f"Seed should be Integer, got {seed_input.socket_type}"
        )

    def test_instance_mesh_input_exists(self, ifs_node_group):
        """Test that Instance Mesh input exists with correct type."""
        instance_mesh_input = ifs_node_group.interface.items_tree.get("Instance Mesh")
        assert instance_mesh_input is not None, "Instance Mesh input not found"
        assert instance_mesh_input.socket_type == 'NodeSocketGeometry', (
            f"Instance Mesh should be Geometry, got {instance_mesh_input.socket_type}"
        )

    def test_output_mode_input_exists(self, ifs_node_group):
        """Test that Output Mode input exists.
        
        Output Mode should allow switching between Points/Instanced/Realized.
        Implementation may vary (Int, Menu, or custom solution).
        """
        # Output Mode may be implemented as Int, String, or Menu
        # Accept any of these for Phase 1.1
        output_mode_input = ifs_node_group.interface.items_tree.get("Output Mode")
        assert output_mode_input is not None, "Output Mode input not found"
        
        # Accept Int, String, or Menu socket types
        valid_types = ['NodeSocketInt', 'NodeSocketString', 'NodeSocketMenu']
        assert output_mode_input.socket_type in valid_types, (
            f"Output Mode should be Int/String/Menu, got {output_mode_input.socket_type}"
        )

    def test_geometry_output_exists(self, ifs_node_group):
        """Test that Geometry output exists."""
        # Find output socket (typically named "Geometry")
        geometry_output = None
        for item in ifs_node_group.interface.items_tree:
            if item.in_out == 'OUTPUT' and item.socket_type == 'NodeSocketGeometry':
                geometry_output = item
                break
        
        assert geometry_output is not None, (
            "Geometry output not found in node group"
        )


class TestBasicNodeGroupBehavior:
    """Test basic node group behavior in a scene context.
    
    Phase 1.1: Tests without transforms, focusing on iteration counter
    and single-point initialization.
    """

    def test_node_group_applies_without_error(self, clean_scene, ifs_node_group):
        """Test that applying IFS_Generator to an object doesn't error.
        
        Smoke test: Create a cube, add Geometry Nodes modifier,
        assign IFS_Generator, and ensure no exceptions are raised.
        """
        # Create a simple cube object
        bpy.ops.mesh.primitive_cube_add()
        obj = bpy.context.active_object
        
        # Add Geometry Nodes modifier
        modifier = obj.modifiers.new(name="GeometryNodes", type='NODES')
        
        # Assign IFS_Generator node group
        modifier.node_group = ifs_node_group
        
        # Try to evaluate (force dependency graph update)
        try:
            # Update the dependency graph
            depsgraph = bpy.context.evaluated_depsgraph_get()
            obj_eval = obj.evaluated_get(depsgraph)
            
            # If we get here without exception, test passes
            assert True
        except Exception as e:
            pytest.fail(f"Node group evaluation raised exception: {e}")

    def test_node_group_with_iterations_one(self, clean_scene, ifs_node_group):
        """Test node group with Iterations=1.
        
        With no transforms and Iterations=1, expect basic point output.
        """
        # Create object with IFS_Generator
        bpy.ops.mesh.primitive_cube_add()
        obj = bpy.context.active_object
        
        modifier = obj.modifiers.new(name="GeometryNodes", type='NODES')
        modifier.node_group = ifs_node_group
        
        # Set Iterations to 1
        modifier["Input_2"] = 1  # Iterations input (index may vary)
        
        # Evaluate
        depsgraph = bpy.context.evaluated_depsgraph_get()
        obj_eval = obj.evaluated_get(depsgraph)
        
        # Basic check: object should have geometry
        assert obj_eval.data is not None


class TestIterationBehavior:
    """Test Repeat Zone iteration counter behavior.
    
    Phase 1.1: Validate iteration counting and attribute storage
    without transforms applied.
    
    TODO Phase 1.2+: Add tests for transform application.
    """

    @pytest.mark.parametrize("iterations", [1, 4, 8, 12])
    def test_iteration_count_range(self, clean_scene, ifs_node_group, iterations):
        """Test that various iteration counts work within valid range.
        
        Per architecture.md §4.1: Valid iterations are 1-12.
        This test ensures the node group handles different iteration
        counts without error.
        """
        # Create object with IFS_Generator
        bpy.ops.mesh.primitive_cube_add()
        obj = bpy.context.active_object
        
        modifier = obj.modifiers.new(name="GeometryNodes", type='NODES')
        modifier.node_group = ifs_node_group
        
        # Set Iterations parameter
        # Note: Input index may vary; this assumes Iterations is second input (index 2)
        modifier["Input_2"] = iterations
        
        # Evaluate without errors
        try:
            depsgraph = bpy.context.evaluated_depsgraph_get()
            obj_eval = obj.evaluated_get(depsgraph)
            assert obj_eval.data is not None
        except Exception as e:
            pytest.fail(
                f"Node group failed with Iterations={iterations}: {e}"
            )

    @pytest.mark.xfail(reason="Phase 1.1: Implementation in progress")
    def test_iteration_attribute_exists(self, clean_scene, ifs_node_group):
        """Test that iteration attribute is stored on point domain.
        
        The Repeat Zone should capture the iteration index and store it
        as a named attribute called 'iteration' on each point.
        
        TODO: Implement once Repeat Zone with attribute capture is complete.
        """
        # Create object with IFS_Generator
        bpy.ops.mesh.primitive_cube_add()
        obj = bpy.context.active_object
        
        modifier = obj.modifiers.new(name="GeometryNodes", type='NODES')
        modifier.node_group = ifs_node_group
        modifier["Input_2"] = 5  # 5 iterations
        
        # Evaluate and get geometry
        depsgraph = bpy.context.evaluated_depsgraph_get()
        obj_eval = obj.evaluated_get(depsgraph)
        
        # Check for 'iteration' attribute
        mesh_eval = obj_eval.data
        assert "iteration" in mesh_eval.attributes, (
            "'iteration' attribute not found on point domain"
        )

    @pytest.mark.xfail(reason="Phase 1.1: Implementation in progress")
    def test_iteration_attribute_range(self, clean_scene, ifs_node_group):
        """Test that iteration attribute spans expected range [0, N-1].
        
        For N iterations, the iteration attribute should range from 0 to N-1.
        
        TODO: Implement once Repeat Zone with attribute capture is complete.
        """
        iterations = 8
        
        # Create object with IFS_Generator
        bpy.ops.mesh.primitive_cube_add()
        obj = bpy.context.active_object
        
        modifier = obj.modifiers.new(name="GeometryNodes", type='NODES')
        modifier.node_group = ifs_node_group
        modifier["Input_2"] = iterations
        
        # Evaluate and get geometry
        depsgraph = bpy.context.evaluated_depsgraph_get()
        obj_eval = obj.evaluated_get(depsgraph)
        
        # Get iteration attribute values
        mesh_eval = obj_eval.data
        iteration_attr = mesh_eval.attributes["iteration"]
        
        # Check range
        values = [iteration_attr.data[i].value for i in range(len(iteration_attr.data))]
        assert min(values) == 0, f"Expected min iteration=0, got {min(values)}"
        assert max(values) == iterations - 1, (
            f"Expected max iteration={iterations-1}, got {max(values)}"
        )


# Phase 1.2+ Placeholder Tests
class TestTransformApplication:
    """Placeholder for Phase 1.2 Single Transform Application tests.
    
    TODO Phase 1.2: Implement tests for Scale/Rotate/Translate application.
    """

    @pytest.mark.skip(reason="Phase 1.2: Not implemented yet")
    def test_single_transform_applied(self):
        """Test that a single transform is correctly applied to points.
        
        Phase 1.2 will implement Scale/Rotate/Translate node chains.
        """
        pass

    @pytest.mark.skip(reason="Phase 1.2: Not implemented yet")
    def test_sierpinski_triangle_basic(self):
        """Test Sierpiński triangle with 3 transforms at 0.5 scale.
        
        Success criteria for Phase 1.2 per development-plan.md.
        """
        pass

