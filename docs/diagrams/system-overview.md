# System Overview Diagrams

## 1. High-Level System Architecture

This diagram shows the major components of the IFS Fractal Generator and their relationships.

```mermaid
graph TB
    subgraph "User Interaction Layer"
        A[User Input]
        B[Blender UI]
        C[Future: MCP Agent]
    end
    
    subgraph "Configuration Layer"
        D[JSON Presets]
        E[Preset Loader]
        F[Schema Validator]
    end
    
    subgraph "Core Engine"
        G[Geometry Nodes Group]
        H[IFS Algorithm]
        I[Repeat Zone]
        J[Transform System]
    end
    
    subgraph "Output Layer"
        K[Point Cloud]
        L[Instanced Geometry]
        M[Realized Mesh]
        N[Export Pipeline]
    end
    
    subgraph "Asset Management"
        O[Node Group Asset]
        P[Instance Meshes]
        Q[Material Library]
    end
    
    A --> B
    A --> C
    B --> E
    C --> E
    D --> F
    F --> E
    E --> G
    G --> H
    H --> I
    I --> J
    J --> K
    K --> L
    L --> M
    M --> N
    O --> G
    P --> G
    Q --> M
    
    style G fill:#4CAF50
    style H fill:#4CAF50
    style I fill:#4CAF50
    style D fill:#2196F3
    style E fill:#2196F3
    style C fill:#FF9800
```

---

## 2. Component Interaction Overview

This diagram illustrates how different system components communicate and depend on each other.

```mermaid
graph LR
    subgraph "Frontend"
        UI[Blender Interface]
        VP[Viewport]
    end
    
    subgraph "Business Logic"
        PC[Preset Controller]
        PM[Parameter Manager]
        VM[Validation Module]
    end
    
    subgraph "Core Engine"
        GN[Geometry Nodes]
        DG[Dependency Graph]
    end
    
    subgraph "Data Storage"
        JP[JSON Presets]
        BF[Blend Files]
        AS[Asset Library]
    end
    
    subgraph "Future: AI Layer"
        MCP[MCP Server]
        LLM[Language Model]
    end
    
    UI -->|User Actions| PC
    PC -->|Load Preset| JP
    PC -->|Validate| VM
    VM -->|Apply Params| PM
    PM -->|Update Inputs| GN
    GN -->|Evaluate| DG
    DG -->|Render| VP
    VP -->|Feedback| UI
    
    MCP -.->|Future| PC
    LLM -.->|Future| MCP
    
    BF --> AS
    AS --> GN
    
    style GN fill:#4CAF50
    style MCP fill:#FF9800,stroke-dasharray: 5 5
    style LLM fill:#FF9800,stroke-dasharray: 5 5
```

---

## 3. Technology Stack

Visual representation of the technology layers.

```mermaid
graph TB
    subgraph "Presentation Layer"
        T1[Blender UI/Panels]
        T2[Viewport Renderer]
        T3[Custom Add-on Interface]
    end
    
    subgraph "Application Layer"
        T4[Python Scripts]
        T5[Blender Python API]
        T6[Preset Management]
    end
    
    subgraph "Core Layer"
        T7[Geometry Nodes Engine]
        T8[Repeat Zone Logic]
        T9[Transform Operators]
    end
    
    subgraph "Data Layer"
        T10[JSON Configuration]
        T11[Blend File Assets]
        T12[Attribute Storage]
    end
    
    subgraph "Future Integration Layer"
        T13[MCP Protocol]
        T14[REST API]
        T15[Export Adapters]
    end
    
    T1 --> T4
    T2 --> T5
    T3 --> T4
    T4 --> T5
    T5 --> T7
    T6 --> T10
    T7 --> T8
    T8 --> T9
    T9 --> T12
    T10 --> T6
    T11 --> T7
    
    T13 -.->|Future| T5
    T14 -.->|Future| T6
    T15 -.->|Future| T5
    
    style T7 fill:#4CAF50
    style T8 fill:#4CAF50
    style T9 fill:#4CAF50
    style T13 fill:#FF9800,stroke-dasharray: 5 5
    style T14 fill:#FF9800,stroke-dasharray: 5 5
    style T15 fill:#FF9800,stroke-dasharray: 5 5
```

---

## 4. Deployment Architecture (Future State)

Shows how the system could be deployed with MCP integration.

```mermaid
graph TB
    subgraph "User Environment"
        U1[Claude Desktop/AI Client]
        U2[Blender Application]
    end
    
    subgraph "Local Services"
        L1[MCP Server Process]
        L2[File Watcher]
        L3[Render Queue]
    end
    
    subgraph "Storage"
        S1[Local Preset Library]
        S2[Asset Cache]
        S3[Render Output]
    end
    
    subgraph "Optional: Cloud Services"
        C1[Preset Repository]
        C2[Render Farm]
        C3[Asset CDN]
    end
    
    U1 <-->|MCP Protocol| L1
    L1 <-->|Python API| U2
    U2 --> L2
    L2 --> S1
    U2 --> S2
    U2 --> S3
    L3 --> U2
    
    S1 -.->|Sync| C1
    L3 -.->|Submit| C2
    S2 -.->|Fetch| C3
    
    style L1 fill:#FF9800
    style U2 fill:#4CAF50
    style C1 fill:#9E9E9E,stroke-dasharray: 5 5
    style C2 fill:#9E9E9E,stroke-dasharray: 5 5
    style C3 fill:#9E9E9E,stroke-dasharray: 5 5
```

---

## 5. Module Dependency Graph

Shows internal module dependencies within the project.

```mermaid
graph TD
    subgraph "Core Modules"
        M1[ifs_generator.blend]
        M2[node_utils]
        M3[transform_logic]
    end
    
    subgraph "Preset Modules"
        M4[preset_schema]
        M5[preset_loader]
        M6[preset_validator]
    end
    
    subgraph "UI Modules"
        M7[addon_init]
        M8[panel_ui]
        M9[operator_handlers]
    end
    
    subgraph "Utility Modules"
        M10[math_utils]
        M11[color_utils]
        M12[export_utils]
    end
    
    subgraph "Future Modules"
        M13[mcp_server]
        M14[agent_tools]
        M15[api_bridge]
    end
    
    M1 --> M2
    M2 --> M3
    M3 --> M10
    
    M5 --> M4
    M5 --> M6
    M6 --> M4
    
    M7 --> M8
    M7 --> M9
    M8 --> M5
    M9 --> M5
    M9 --> M1
    
    M3 --> M11
    M9 --> M12
    
    M13 -.-> M15
    M14 -.-> M15
    M15 -.-> M5
    M15 -.-> M9
    
    style M1 fill:#4CAF50
    style M13 fill:#FF9800,stroke-dasharray: 5 5
    style M14 fill:#FF9800,stroke-dasharray: 5 5
    style M15 fill:#FF9800,stroke-dasharray: 5 5
```

---

## Legend

- **Green**: Core geometry system (already implemented/in progress)
- **Blue**: Configuration and data management
- **Orange**: Future MCP/AI integration features
- **Gray**: Optional cloud services
- **Dashed Lines**: Planned but not yet implemented
- **Solid Lines**: Implemented or in active development

---

## Notes

- All diagrams represent both current state and planned architecture
- Dashed components indicate future phases (see `/docs/development-plan.md`)
- Core geometry nodes remain independent of future extensions
- MCP integration is non-invasive and can be added without modifying core engine

