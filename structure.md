IFS-Fractal-Generator/
├── README.md # concise intro & usage notes
├── docs/
│ └── IFS_Fractal_Generator.md # the main design document (you already have this)
├── src/
│ ├── init.py # Blender add-on entry point (future)
│ ├── geometry_nodes/ # node group definitions, JSON or .blend assets
│ │ └── ifs_generator.blend
│ ├── presets/ # preset configurations (e.g., Barnsley, Sierpiński)
│ │ ├── barnsley.json
│ │ ├── sierpinski.json
│ │ └── menger.json
│ ├── utils/ # helpers for transforms, colors, random seeds
│ │ └── init.py
│ └── mcp/ # placeholder for future Model Context Protocol integration
│ └── README.md
└── assets/
├── icons/
├── reference_images/
└── preview_renders/