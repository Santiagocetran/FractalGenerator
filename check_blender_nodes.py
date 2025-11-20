"""Check what geometry nodes are available in this Blender version."""

import bpy

print("=" * 60)
print(f"Blender Version: {bpy.app.version_string}")
print("=" * 60)

# Get all available geometry node types
print("\nAvailable Geometry Node Types:")
print("-" * 60)

node_types = []
for item in dir(bpy.types):
    if item.startswith('GeometryNode'):
        node_types.append(item)

# Sort and display
for node_type in sorted(node_types):
    print(f"  {node_type}")

print("\n" + "=" * 60)
print("Searching for Repeat/Loop related nodes:")
print("-" * 60)

repeat_nodes = [n for n in node_types if 'repeat' in n.lower() or 'loop' in n.lower() or 'iterate' in n.lower()]
if repeat_nodes:
    for node in repeat_nodes:
        print(f"  ✓ {node}")
else:
    print("  ⚠ No repeat/loop nodes found")

print("=" * 60)

