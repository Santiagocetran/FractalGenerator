# Data Flow Diagrams

## 1. Core IFS Generation Flow

This diagram shows how data flows through the geometry generation pipeline.

```mermaid
flowchart TD
    Start([User Initiates Generation]) --> Input[Collect Input Parameters]
    
    Input --> InputData{Input Sources}
    InputData -->|Manual| Sliders[UI Sliders/Fields]
    InputData -->|Preset| JSON[Load JSON Preset]
    
    Sliders --> Validate
    JSON --> Parse[Parse JSON]
    Parse --> Validate[Validate Parameters]
    
    Validate -->|Invalid| Error[Display Error Message]
    Validate -->|Valid| Init[Initialize Point Cloud]
    
    Init --> IterLoop{Iteration Counter}
    
    subgraph "Repeat Zone Loop"
        IterLoop -->|i < Max Iterations| Transform[Apply Transform Set]
        Transform --> Branch{For Each Transform}
        
        Branch --> T1[Transform 1: Scale/Rot/Trans]
        Branch --> T2[Transform 2: Scale/Rot/Trans]
        Branch --> T3[Transform 3: Scale/Rot/Trans]
        Branch --> T4[Transform N: Scale/Rot/Trans]
        
        T1 --> Weight1{Weight Check}
        T2 --> Weight2{Weight Check}
        T3 --> Weight3{Weight Check}
        T4 --> WeightN{Weight Check}
        
        Weight1 -->|Random < Weight| Apply1[Apply Transform 1]
        Weight2 -->|Random < Weight| Apply2[Apply Transform 2]
        Weight3 -->|Random < Weight| Apply3[Apply Transform 3]
        WeightN -->|Random < Weight| ApplyN[Apply Transform N]
        
        Weight1 -->|Skip| Merge
        Weight2 -->|Skip| Merge
        Weight3 -->|Skip| Merge
        WeightN -->|Skip| Merge
        
        Apply1 --> Merge[Merge All Points]
        Apply2 --> Merge
        Apply3 --> Merge
        ApplyN --> Merge
        
        Merge --> Capture[Capture Iteration Attribute]
        Capture --> Increment[Increment Counter]
        Increment --> IterLoop
    end
    
    IterLoop -->|i >= Max Iterations| Output[Generate Output]
    
    Output --> Mode{Output Mode}
    Mode -->|Points| Points[Point Cloud Output]
    Mode -->|Instanced| Instance[Instance on Points]
    Mode -->|Realized| Realize[Realize Instances]
    
    Instance --> ColorMap
    Realize --> ColorMap
    Points --> ColorMap[Apply Color Ramp]
    
    ColorMap --> Material[Assign Material]
    Material --> Final([Final Geometry Output])
    
    Error --> End([End])
    Final --> End
    
    style IterLoop fill:#4CAF50
    style Transform fill:#4CAF50
    style Merge fill:#4CAF50
    style JSON fill:#2196F3
```

---

## 2. Preset Loading Flow

Detailed flow of how JSON presets are loaded and applied.

```mermaid
sequenceDiagram
    actor User
    participant UI as Blender UI
    participant Loader as Preset Loader
    participant Validator as Schema Validator
    participant Parser as JSON Parser
    participant API as Blender API
    participant Nodes as Geometry Nodes
    participant DG as Dependency Graph
    
    User->>UI: Select Preset
    UI->>Loader: Load Preset File
    Loader->>Parser: Read JSON
    Parser->>Parser: Parse Structure
    
    alt JSON Parse Error
        Parser-->>Loader: Error: Malformed JSON
        Loader-->>UI: Display Error
        UI-->>User: Show Error Message
    else JSON Valid
        Parser->>Validator: Validate Schema
        
        alt Schema Invalid
            Validator-->>Loader: Error: Schema Mismatch
            Loader-->>UI: Display Error
            UI-->>User: Show Error Message
        else Schema Valid
            Validator->>API: Apply Parameters
            
            loop For Each Parameter
                API->>Nodes: Set Input Value
                Nodes->>Nodes: Update Socket
            end
            
            Nodes->>DG: Mark Dirty
            DG->>DG: Rebuild Graph
            DG->>UI: Update Viewport
            UI-->>User: Display Result
        end
    end
```

---

## 3. Parameter Update Flow (Real-Time Interaction)

Shows the flow when user adjusts parameters in real-time.

```mermaid
flowchart TD
    Start([User Adjusts Parameter]) --> Detect[Detect Value Change]
    
    Detect --> Check{Is Interactive Mode?}
    Check -->|Yes| Preview[Use Preview Settings]
    Check -->|No| Full[Use Full Settings]
    
    Preview --> ReduceIter[Reduce Iteration Count]
    ReduceIter --> Update
    Full --> Update[Update Node Input]
    
    Update --> Propagate[Propagate Through Node Tree]
    
    Propagate --> Eval[Dependency Graph Evaluation]
    
    Eval --> Cache{Result Cached?}
    Cache -->|Yes| Load[Load from Cache]
    Cache -->|No| Compute[Compute Geometry]
    
    Compute --> Store[Store in Cache]
    Store --> Render
    Load --> Render[Render to Viewport]
    
    Render --> Display[Display Result]
    
    Display --> Monitor{Still Interacting?}
    Monitor -->|Yes| Wait[Wait for Change]
    Monitor -->|No| Finalize[Switch to Full Quality]
    
    Wait --> Detect
    Finalize --> Full
    
    Display --> End([End])
    
    style Compute fill:#FF9800
    style Eval fill:#4CAF50
    style Cache fill:#2196F3
```

---

## 4. Transform Application Logic Flow

Detailed view of how transforms are applied within a single iteration.

```mermaid
flowchart LR
    Start([Iteration N Begins]) --> Input[Input Point Cloud]
    
    Input --> Duplicate[Duplicate for Each Transform]
    
    subgraph "Transform Processing"
        Duplicate --> Split[Split by Transform Count]
        
        Split --> Branch1[Branch 1]
        Split --> Branch2[Branch 2]
        Split --> Branch3[Branch 3]
        Split --> BranchN[Branch N]
        
        Branch1 --> Rand1[Generate Random Value]
        Branch2 --> Rand2[Generate Random Value]
        Branch3 --> Rand3[Generate Random Value]
        BranchN --> RandN[Generate Random Value]
        
        Rand1 --> Comp1{Compare with Weight}
        Rand2 --> Comp2{Compare with Weight}
        Rand3 --> Comp3{Compare with Weight}
        RandN --> CompN{Compare with Weight}
        
        Comp1 -->|Pass| Apply1[Scale/Rotate/Translate]
        Comp2 -->|Pass| Apply2[Scale/Rotate/Translate]
        Comp3 -->|Pass| Apply3[Scale/Rotate/Translate]
        CompN -->|Pass| ApplyN[Scale/Rotate/Translate]
        
        Comp1 -->|Fail| Discard1[Discard Points]
        Comp2 -->|Fail| Discard2[Discard Points]
        Comp3 -->|Fail| Discard3[Discard Points]
        CompN -->|Fail| DiscardN[Discard Points]
        
        Apply1 --> Attr1[Add Iteration Attribute]
        Apply2 --> Attr2[Add Iteration Attribute]
        Apply3 --> Attr3[Add Iteration Attribute]
        ApplyN --> AttrN[Add Iteration Attribute]
    end
    
    Attr1 --> Merge[Merge Geometry]
    Attr2 --> Merge
    Attr3 --> Merge
    AttrN --> Merge
    
    Merge --> Output([Output to Next Iteration])
    
    style Apply1 fill:#4CAF50
    style Apply2 fill:#4CAF50
    style Apply3 fill:#4CAF50
    style ApplyN fill:#4CAF50
    style Merge fill:#FF9800
```

---

## 5. Color Mapping Flow

How iteration depth is converted to color gradients.

```mermaid
flowchart TD
    Start([Geometry with Iteration Attribute]) --> Read[Read Iteration Index]
    
    Read --> Normalize[Normalize to 0-1 Range]
    Normalize --> Formula["Value = Index / Max Iterations"]
    
    Formula --> ColorRamp{Color Ramp Type}
    
    ColorRamp -->|Preset| PresetPalette[Use Preset Colors]
    ColorRamp -->|Custom| CustomPalette[Use Custom Gradient]
    
    PresetPalette --> Interp
    CustomPalette --> Interp[Interpolate Color]
    
    Interp --> RGB[Generate RGB Values]
    RGB --> Store[Store as Vertex Color]
    
    Store --> Material{Has Material?}
    Material -->|Yes| Apply[Apply to Material Input]
    Material -->|No| Default[Use Default Material]
    
    Apply --> Output
    Default --> Output([Final Colored Geometry])
    
    style ColorRamp fill:#4CAF50
    style Interp fill:#4CAF50
    style RGB fill:#FF9800
```

---

## 6. Export Pipeline Flow

Data flow for exporting fractals to various formats.

```mermaid
flowchart TD
    Start([User Initiates Export]) --> Check{Geometry Ready?}
    
    Check -->|No| Error1[Display Error]
    Check -->|Yes| Select[Select Export Format]
    
    Select --> Format{Format Type}
    
    Format -->|GLB/GLTF| PrepGLB[Prepare for GLB]
    Format -->|PLY| PrepPLY[Prepare Point Cloud]
    Format -->|Alembic| PrepABC[Prepare Animation]
    Format -->|USD| PrepUSD[Prepare USD Structure]
    
    PrepGLB --> Realize1[Realize Instances]
    PrepPLY --> Keep[Keep as Points]
    PrepABC --> Realize2[Realize Instances]
    PrepUSD --> Hierarchy[Build Hierarchy]
    
    Realize1 --> OptGLB{Optimize?}
    OptGLB -->|Yes| Decimate[Decimate Mesh]
    OptGLB -->|No| ExportGLB
    
    Decimate --> ExportGLB[Export GLB]
    Keep --> ExportPLY[Export PLY]
    Realize2 --> ExportABC[Export Alembic]
    Hierarchy --> ExportUSD[Export USD]
    
    ExportGLB --> Validate
    ExportPLY --> Validate
    ExportABC --> Validate
    ExportUSD --> Validate[Validate Output]
    
    Validate -->|Valid| Success[Show Success Message]
    Validate -->|Invalid| Error2[Show Error]
    
    Success --> Open{Open After Export?}
    Open -->|Yes| Launch[Launch External Viewer]
    Open -->|No| Done
    
    Launch --> Done
    Error1 --> Done
    Error2 --> Done([End])
    
    style Realize1 fill:#FF9800
    style Realize2 fill:#FF9800
    style Validate fill:#4CAF50
```

---

## 7. Future: MCP Agent Interaction Flow

Planned data flow for AI agent-driven fractal generation.

```mermaid
sequenceDiagram
    actor User
    participant Agent as AI Agent
    participant MCP as MCP Server
    participant Blender as Blender API
    participant Nodes as Geometry Nodes
    participant Render as Render Engine
    
    User->>Agent: "Create a fern-like fractal"
    Agent->>Agent: Parse Intent
    Agent->>MCP: Call generate_fractal tool
    
    MCP->>MCP: Generate JSON Preset
    MCP->>MCP: Validate Schema
    
    alt Invalid Parameters
        MCP-->>Agent: Error Response
        Agent-->>User: Request Clarification
        User->>Agent: Provide Details
        Agent->>MCP: Retry with Updated Params
    end
    
    MCP->>Blender: Apply Preset via API
    Blender->>Nodes: Update Node Group
    Nodes->>Nodes: Evaluate Geometry
    Nodes->>Render: Request Preview
    Render->>Render: Generate Image
    Render-->>MCP: Return Preview Image
    
    MCP-->>Agent: Success + Preview
    Agent-->>User: Show Result + Description
    
    User->>Agent: "Make it more compact"
    Agent->>MCP: Call modify_parameters tool
    
    MCP->>MCP: Adjust Scale Values
    MCP->>Blender: Update Parameters
    Blender->>Nodes: Recalculate
    Nodes->>Render: New Preview
    Render-->>MCP: Updated Image
    MCP-->>Agent: Success + New Preview
    Agent-->>User: Show Updated Result
    
    User->>Agent: "Export as GLB"
    Agent->>MCP: Call export_geometry tool
    MCP->>Blender: Trigger Export
    Blender->>Blender: Realize and Export
    Blender-->>MCP: Export Complete
    MCP-->>Agent: File Path
    Agent-->>User: Download Link
    
    Note over Agent,Render: All interactions maintain context<br/>for multi-turn refinement
```

---

## Data Flow Summary

| Flow Type | Complexity | Performance Impact | Caching Possible |
|-----------|------------|-------------------|------------------|
| Core Generation | High | High (exponential) | Partial |
| Preset Loading | Low | Minimal | Full |
| Parameter Update | Medium | Medium | Yes |
| Transform Logic | High | High | No |
| Color Mapping | Low | Low | Yes |
| Export Pipeline | Medium | Medium | No |
| MCP Interaction | Medium | Low (async) | Yes |

---

## Performance Considerations

- **Bottleneck**: Transform application and merge operations in repeat zone
- **Optimization Strategy**: Minimize point count via probabilistic culling
- **Caching**: Dependency graph caches unchanged subtrees
- **Future**: GPU compute shaders for transform operations

