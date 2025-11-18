# Component Interaction Maps

## 1. User Workflow Sequence

Complete sequence of a typical user session.

```mermaid
sequenceDiagram
    actor User
    participant Blender as Blender Application
    participant UI as Add-on UI Panel
    participant Loader as Preset Loader
    participant Nodes as Geometry Nodes
    participant Viewport as 3D Viewport
    
    User->>Blender: Launch Blender
    Blender->>UI: Load Add-on
    UI->>UI: Initialize Panel
    
    User->>UI: Click "Add Fractal"
    UI->>Loader: Request Default Preset
    Loader->>Loader: Load barnsley.json
    Loader->>Nodes: Create Node Group
    Nodes->>Nodes: Initialize with Preset
    
    Nodes->>Viewport: Generate Preview
    Viewport-->>User: Display Fractal (6 iterations)
    
    User->>UI: Adjust Iterations Slider (10)
    UI->>Nodes: Update Iterations Input
    Nodes->>Nodes: Recalculate Geometry
    Nodes->>Viewport: Update Display
    Viewport-->>User: Show Updated Fractal
    
    User->>UI: Change Preset to "Sierpiński"
    UI->>Loader: Load sierpinski.json
    Loader->>Nodes: Apply New Parameters
    Nodes->>Viewport: Regenerate
    Viewport-->>User: Display New Fractal
    
    User->>UI: Adjust Color Ramp
    UI->>Nodes: Update Color Params
    Nodes->>Viewport: Update Colors
    Viewport-->>User: Show Recolored Result
    
    User->>UI: Click "Export GLB"
    UI->>Nodes: Realize Instances
    Nodes->>Blender: Export Geometry
    Blender->>Blender: Write GLB File
    Blender-->>UI: Export Complete
    UI-->>User: Show Success Message
```

---

## 2. Preset Loading Interaction

Detailed interaction during preset loading.

```mermaid
sequenceDiagram
    participant UI as User Interface
    participant Validator as Schema Validator
    participant Loader as Preset Loader
    participant FileSystem as File System
    participant Parser as JSON Parser
    participant NodeAPI as Node API
    participant NodeGroup as Node Group
    
    UI->>FileSystem: Request Preset List
    FileSystem-->>UI: Return Available Presets
    
    UI->>Loader: Load Preset "barnsley"
    Loader->>FileSystem: Read barnsley.json
    FileSystem-->>Loader: Return File Contents
    
    Loader->>Parser: Parse JSON String
    Parser->>Parser: Validate JSON Syntax
    
    alt Invalid JSON
        Parser-->>Loader: Syntax Error
        Loader-->>UI: Display Error Dialog
    else Valid JSON
        Parser-->>Loader: Return Data Structure
        
        Loader->>Validator: Validate Schema
        Validator->>Validator: Check Required Fields
        Validator->>Validator: Validate Data Types
        Validator->>Validator: Check Constraints
        
        alt Schema Invalid
            Validator-->>Loader: Validation Errors
            Loader-->>UI: Display Error Details
        else Schema Valid
            Validator-->>Loader: Validation Success
            
            Loader->>NodeAPI: Access Node Group
            
            loop For Each Parameter
                Loader->>NodeAPI: Set Input Value
                NodeAPI->>NodeGroup: Update Socket
            end
            
            NodeGroup->>NodeGroup: Trigger Evaluation
            NodeGroup-->>NodeAPI: Evaluation Complete
            NodeAPI-->>Loader: Update Success
            Loader-->>UI: Display Success
        end
    end
```

---

## 3. Real-Time Parameter Adjustment

How the system responds to live parameter changes.

```mermaid
sequenceDiagram
    participant User
    participant UI as UI Slider
    participant EventLoop as Blender Event Loop
    participant Props as Property System
    participant DepGraph as Dependency Graph
    participant Nodes as Node Tree
    participant Viewport as Viewport Renderer
    
    User->>UI: Drag Slider
    
    loop During Drag
        UI->>EventLoop: Value Changed Event
        EventLoop->>Props: Update Property
        Props->>Props: Mark Dirty
        Props->>DepGraph: Tag for Update
        DepGraph->>DepGraph: Schedule Rebuild
        
        Note over DepGraph: Debounce rapid changes
        
        DepGraph->>Nodes: Evaluate Node Tree
        Nodes->>Nodes: Execute Geometry Logic
        Nodes-->>DepGraph: Return Geometry
        
        DepGraph->>Viewport: Queue Redraw
        Viewport->>Viewport: Render New Geometry
        Viewport-->>User: Display Update (20-60ms)
    end
    
    User->>UI: Release Slider
    UI->>EventLoop: Final Value Event
    EventLoop->>Props: Confirm Final Value
    Props->>DepGraph: Force Full Evaluation
    DepGraph->>Nodes: Full Quality Pass
    Nodes-->>Viewport: Final Geometry
    Viewport-->>User: High Quality Display
```

---

## 4. Node Group Internal Communication

How nodes communicate within the IFS generator.

```mermaid
graph TD
    Input[Input Sockets] --> Control{Control Flow}
    
    Control --> Init[Initialize]
    Init --> StartPoint[Single Start Point]
    
    StartPoint --> RepeatZone[Repeat Zone Node]
    
    subgraph "Repeat Zone Internal"
        RepeatZone --> IterCheck{Iteration < Max?}
        
        IterCheck -->|Yes| Split[Split to Transforms]
        
        Split --> T1[Transform Branch 1]
        Split --> T2[Transform Branch 2]
        Split --> T3[Transform Branch 3]
        Split --> T4[Transform Branch 4]
        
        T1 --> Weight1{Check Weight}
        T2 --> Weight2{Check Weight}
        T3 --> Weight3{Check Weight}
        T4 --> Weight4{Check Weight}
        
        Weight1 -->|Pass| Apply1[Apply Transform]
        Weight2 -->|Pass| Apply2[Apply Transform]
        Weight3 -->|Pass| Apply3[Apply Transform]
        Weight4 -->|Pass| Apply4[Apply Transform]
        
        Weight1 -->|Fail| Merge
        Weight2 -->|Fail| Merge
        Weight3 -->|Fail| Merge
        Weight4 -->|Fail| Merge
        
        Apply1 --> Merge[Join Geometry]
        Apply2 --> Merge
        Apply3 --> Merge
        Apply4 --> Merge
        
        Merge --> Capture[Capture Attributes]
        Capture --> Increment[Increment Counter]
        Increment --> IterCheck
    end
    
    IterCheck -->|No| Output[Output Socket]
    Output --> Post[Post Processing]
    
    Post --> ColorMap[Color Mapping]
    ColorMap --> Instance{Output Mode}
    
    Instance -->|Points| PointOut[Points Output]
    Instance -->|Instanced| InstOut[Instance Output]
    Instance -->|Realized| RealOut[Realized Output]
    
    PointOut --> Final[Final Geometry]
    InstOut --> Final
    RealOut --> Final
    
    style RepeatZone fill:#4CAF50
    style Merge fill:#FF9800
    style Final fill:#2196F3
```

---

## 5. Future: MCP Agent Workflow

Planned interaction pattern with AI agents.

```mermaid
sequenceDiagram
    actor User
    participant Agent as AI Agent (Claude)
    participant MCP as MCP Server
    participant Tools as Tool Functions
    participant Blender as Blender API
    participant Nodes as Geometry Nodes
    participant Storage as File System
    
    User->>Agent: "Create a tree-like fractal with 5 branches"
    
    Agent->>Agent: Analyze Request
    Agent->>Agent: Identify Tool: generate_fractal
    
    Agent->>MCP: Call generate_fractal(description="tree-like, 5 branches")
    MCP->>Tools: Execute generate_fractal
    
    Tools->>Tools: Generate JSON Preset
    Note over Tools: Uses LLM context for<br/>reasonable defaults
    
    Tools->>Tools: Validate Against Schema
    
    alt Invalid Schema
        Tools-->>MCP: Error Response
        MCP-->>Agent: Tool Error
        Agent->>Agent: Adjust Parameters
        Agent->>MCP: Retry with Corrections
    else Valid Schema
        Tools->>Storage: Save Temporary Preset
        Tools->>Blender: Apply Preset
        Blender->>Nodes: Create/Update Node Group
        Nodes->>Nodes: Generate Geometry
        Nodes->>Blender: Render Preview
        Blender->>Storage: Save Preview Image
        Storage-->>Tools: Image Path
        Tools-->>MCP: Success + Image Path
        MCP-->>Agent: Result + Preview
        Agent-->>User: Show Result + Description
    end
    
    User->>Agent: "Make the branches thinner"
    
    Agent->>MCP: Call modify_parameters(param="scale", adjustment="decrease", factor=0.7)
    MCP->>Tools: Execute modify_parameters
    
    Tools->>Storage: Load Current Preset
    Tools->>Tools: Adjust Scale Values
    Tools->>Blender: Update Parameters
    Blender->>Nodes: Recalculate
    Nodes->>Blender: New Preview
    Blender->>Storage: Save Updated Preview
    Storage-->>MCP: New Image Path
    MCP-->>Agent: Success + New Image
    Agent-->>User: Show Updated Result
    
    User->>Agent: "Perfect! Save this as 'My Tree'"
    
    Agent->>MCP: Call save_preset(name="My Tree")
    MCP->>Tools: Execute save_preset
    Tools->>Storage: Save to Presets Folder
    Storage-->>Tools: Save Confirmed
    Tools-->>MCP: Success
    MCP-->>Agent: Preset Saved
    Agent-->>User: "Saved successfully as 'My Tree'"
```

---

## 6. Multi-User Collaboration (Future Concept)

Conceptual interaction for shared fractal editing.

```mermaid
sequenceDiagram
    actor UserA as User A
    actor UserB as User B
    participant SyncServer as Sync Server
    participant BlenderA as Blender A
    participant BlenderB as Blender B
    participant Storage as Shared Storage
    
    UserA->>BlenderA: Create Fractal
    BlenderA->>BlenderA: Generate Geometry
    UserA->>BlenderA: Click "Share"
    
    BlenderA->>Storage: Upload Preset JSON
    Storage->>SyncServer: Register New Preset
    SyncServer->>SyncServer: Generate Share Link
    SyncServer-->>BlenderA: Return Link
    BlenderA-->>UserA: Display Share Link
    
    UserA->>UserB: Send Link
    UserB->>SyncServer: Access Link
    SyncServer->>Storage: Request Preset
    Storage-->>SyncServer: Return Preset Data
    SyncServer-->>UserB: Provide Download
    
    UserB->>BlenderB: Import Shared Preset
    BlenderB->>BlenderB: Load and Display
    BlenderB-->>UserB: Show Fractal
    
    UserB->>BlenderB: Modify Parameters
    BlenderB->>BlenderB: Update Geometry
    UserB->>BlenderB: Save as Variant
    
    BlenderB->>Storage: Upload Variant
    Storage->>SyncServer: Notify Variant Created
    SyncServer->>BlenderA: Send Notification
    BlenderA-->>UserA: "User B created a variant"
    
    UserA->>BlenderA: View Variant
    BlenderA->>Storage: Download Variant
    Storage-->>BlenderA: Variant Data
    BlenderA-->>UserA: Display Side-by-Side
```

---

## 7. Batch Processing Workflow

Interaction for generating multiple fractal variations.

```mermaid
sequenceDiagram
    participant User
    participant Script as Batch Script
    participant Loader as Preset Loader
    participant Blender as Blender (Background)
    participant Renderer as Render Engine
    participant Storage as Output Folder
    
    User->>Script: Run batch_generate.py
    Script->>Script: Parse Configuration
    
    loop For Each Preset
        Script->>Loader: Load Preset N
        Loader->>Blender: Apply to Scene
        Blender->>Blender: Generate Geometry
        
        loop For Each Iteration Count
            Blender->>Blender: Set Iterations
            Blender->>Renderer: Render Frame
            Renderer->>Renderer: Execute Render
            Renderer->>Storage: Save Image
            Storage-->>Script: Confirm Save
        end
        
        loop For Each Camera Angle
            Blender->>Blender: Set Camera Position
            Blender->>Renderer: Render Frame
            Renderer->>Storage: Save Image
        end
        
        Script->>Blender: Export Geometry
        Blender->>Storage: Save GLB/PLY
    end
    
    Script->>Script: Generate Index HTML
    Script->>Storage: Save Gallery Page
    Script-->>User: Batch Complete (N renders)
```

---

## 8. Error Handling Flow

How errors propagate through the system.

```mermaid
graph TD
    Start[User Action] --> Validate{Input Valid?}
    
    Validate -->|No| UIError[Display UI Error]
    Validate -->|Yes| Execute[Execute Operation]
    
    Execute --> Check{Operation Success?}
    
    Check -->|Error: JSON| JSONError[JSON Parse Error]
    Check -->|Error: Schema| SchemaError[Schema Validation Error]
    Check -->|Error: Node| NodeError[Node Evaluation Error]
    Check -->|Error: Memory| MemError[Out of Memory Error]
    Check -->|Success| Success[Complete]
    
    JSONError --> Log[Log Error Details]
    SchemaError --> Log
    NodeError --> Log
    MemError --> Log
    UIError --> Log
    
    Log --> UserNotify{Severity}
    
    UserNotify -->|Critical| Modal[Show Modal Dialog]
    UserNotify -->|Warning| Toast[Show Toast Notification]
    UserNotify -->|Info| Console[Log to Console]
    
    Modal --> Recovery{Recoverable?}
    Recovery -->|Yes| Suggest[Suggest Fix]
    Recovery -->|No| Abort[Abort Operation]
    
    Suggest --> Retry{User Retry?}
    Retry -->|Yes| Start
    Retry -->|No| End
    
    Toast --> End
    Console --> End
    Abort --> End
    Success --> End([End])
    
    style JSONError fill:#F44336
    style SchemaError fill:#F44336
    style NodeError fill:#F44336
    style MemError fill:#F44336
    style Success fill:#4CAF50
```

---

## Interaction Patterns Summary

| Pattern | Complexity | User Involvement | Automation Level |
|---------|------------|------------------|------------------|
| Manual Preset Load | Low | High | None |
| Parameter Adjustment | Low | Continuous | Real-time feedback |
| Agent Generation | Medium | Initial + Refinement | High |
| Batch Processing | High | Initial Setup | Full |
| Collaborative Edit | High | Multi-user | Synchronized |
| Error Recovery | Variable | Context-dependent | Semi-automatic |

---

## Design Principles

### Responsiveness
- All interactions provide immediate feedback
- Long operations show progress indicators
- Preview mode enables real-time parameter tuning

### Predictability
- Clear state changes with visual confirmation
- Undo/redo support for all modifications
- Validation before destructive operations

### Extensibility
- Plugin architecture for new interaction modes
- MCP layer enables novel workflows
- Clear API boundaries for custom scripts

### Resilience
- Graceful degradation on errors
- Automatic recovery where possible
- Clear error messages with actionable suggestions

