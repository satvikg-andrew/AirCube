# AirCube four-layer ground-reference checkpoint

UNROUTED. NOT READY FOR FABRICATION.

This update starts from the uploaded `AirCube(6).kicad_pcb`. It retains the user's four-layer, provisional 1.66 mm physical stackup. Manufacturer dielectric thicknesses, material properties and copper weights are not finalized; controlled-impedance trace dimensions have not been assigned.

## Changes

- Added a filled GND zone to In1.Cu and a filled GND zone to In2.Cu. Each is a single continuous region of approximately 1702.60 mm². Both zones explicitly belong to the GND net.
- Set zone clearance to 0.20 mm, minimum fill width to 0.20 mm, and isolated-island removal to always. Ground pad connections use solid copper. The existing 0.25 mm copper-to-board-edge rule remains in force. Solid ground connections improve continuity but require assembly heat capacity to be considered for through-hole ground pins.
- Applied both sensor thermal copper-pour exclusions to exactly F.Cu, In1.Cu, In2.Cu and B.Cu. Removed the extraneous User.1 documentation-layer selection from the old exclusion definitions. Copper stays out of the two sensor thermal islands. The blank areas near the upper corners are intentional.
- Preserved all 125 footprint placements, footprint identities, pad geometry and pad-to-net assignments. Added no tracks or new vias. No schematic or project-rule changes are included in this update.

## Verification

Native KiCad 10.0.7, after filling and saving zones:

- 0 DRC violations in the main violations section.
- 326 separately reported unconnected items, reduced from 331. They remain errors for a finished board.
- 0 schematic-to-PCB parity issues against the previously supplied matching schematic and libraries.
- Independent comparison confirms unchanged component placements, pad geometry and net assignments.
- Each inner GND zone has one filled contour; sample points on both sensor islands contain no filled ground copper.

The reduction of five unconnected reports comes from connecting existing plated GND pads through the planes. It does not mean only five individual pins are connected, nor that all surface-mount ground pads are connected. Those pads still need appropriate tracks or vias. Through-hole GND pads connect the two planes; no claim of completed ground stitching, validated RF return paths or current-carrying performance is made.

`ground-plane-review/` contains the native DRC report, structured results, comparison details and a preview of the In1.Cu fill. The preview depicts the copper layer, not the finished assembly.

## Install

1. Close PCB Editor, Schematic Editor and the KiCad project manager.
2. Back up the current `kicad/Base/AirCube.kicad_pcb` outside the repository.
3. Extract this ZIP. Copy the contents of its `Base` folder into your repository's `kicad/Base`, replacing the PCB when prompted. This ZIP contains only the updated PCB, this note and the new review folder. Retain all existing schematic, project and local-library files from the placement checkpoint.
4. Open `kicad/Base/AirCube.kicad_pro`, then PCB Editor.
5. Press B to refill zones if needed. Run Inspect > Design Rules Checker > Run DRC. Expected here: 0 main DRC violations and 326 unconnected reports. Different library versions may produce comparison warnings requiring investigation.

The earlier `README-placement-review.md` and its reports describe the historical placement checkpoint. This note supersedes its two-layer/no-poured-planes status.

## Next design work

Route the U7 modem regulator and U6 3.3 V regulator with their input/output loops, ground returns and feedback paths reviewed against the TI layout guidance. Complete the power budget, USB-C source-current/inrush strategy, modem transmit-burst voltage-drop and capacitance/stability checks. Then route the remaining rails, sensors, UARTs, SIM and other signals. Select the actual fabrication stackup before assigning LTE/USB controlled-impedance geometry. Add and verify the required ground vias/stitching as routing progresses.

All outstanding BOM, mechanical, manufacturing, firmware and real-hardware testing work from the placement checkpoint remains outstanding. Do not send this checkpoint as an order-ready design.
