# MAVRIC-Electrical
The repository for the E-Team. Includes designs and documentation.

# Team Structure
Team Lead: ? @?

Members:
 * ?
 * ?
 * ?
 * ?

# Folder Structure:

```
|> Electrical
|  |> Design Documents // The system diagrams, datasheets, etc.
|  `> Implmentation    // KiCad deigns, simulation data, etc.
|
|> Firmware
|  |> Design Documents // The system diagrams, datasheets, etc.
|  `> Implmentation    // The code
|     `> [Catkin Worksapce]
|
`> Base Station
   |> ?                // We still need to decide more about this
```

# Milestones [Proposed]
|                     | Milestone 1 | Milestone 2 | Milestone 3 | Milestone 4 |
|:--------------------|:-----------:|:-----------:|:-----------:|:-----------:|
| Name                |Drive System |      ?      |      ?      |      ?      |
| Due Date            |  Sept. 17   |      ?      |      ?      |      ?      |
| Primary Team Member |      ?      |      ?      |      ?      |      ?      |

## Milestone 1:  [Drive System](https://github.com/m2i/MAVRIC-Electrical/milestone/2)
Description: Control of the drive system. Includes basic forward, backward, and turn maneuvers as well as heading and position feedback to the controller.

Notes: Phoenix will need to have at least serial comms, but we should finalize a communications stack before we get too far on this. We can simulate a Rocket system by hooking everything up on a local network. If we go with a network-bridge solution like the Rocket, we will most likely use sockets. Sockets will give us the flexibility to open up multiple 'channels' to and from Phoenix.
### Tasks
 * Establish basic connectivity with the rover
   * Most likely either Sockets or Serial.
   * Requires a master Control Board and Drive Control Board
 * Define control parameters
   * Open Loop: (`Output Power`, `Left/Right Output Ratio`)
   * Open Loop Direct: (`Left Output Power`, `Right Output Power`)
   * Closed Loop: (`Velocity`, `Turn Radius`)
   * Closed Loop Direct: (`Left Velocity`, `Right Velocity`)
 * Implement Control Nodes
   * `/mavric/master-control/control-interface`
   * `/mavric/drive-control/control-interface`
   * `/mavric/drive-control/*` [any PID or other subsystems]
 * Implement sensing
   * GPS
   * Compass

### Deliverables
 * System architecture document with drive system finalized
   * ROS architecture
   * Electrical architecture
 * Video of Phoenix Driving in the Howe atrium
 * Description of control systems and sensors in place, including safety systems
   * Communication setup
   * Control Parameters chosen
   * Hartbeat signal
   * Positioning
   * Heading

## Milestone 2: ?
Description: ?

Notes: 
### Tasks
 * ?
 * ?
 * ?

### Deliverables
 * ?
 * ?
 * ?

## Milestone 3: ?
Description: ?

Notes: 
### Tasks
 * ?
 * ?
 * ?

### Deliverables
 * ?
 * ?
 * ?
 
## Milestone 4: ?
Description: ?

Notes: 
### Tasks
 * ?
 * ?
 * ?

### Deliverables
 * ?
 * ?
 * ?
