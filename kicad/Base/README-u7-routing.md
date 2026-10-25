# AirCube U7 local power-stage routing checkpoint

**PARTIALLY ROUTED. NOT READY TO FABRICATE OR POWER-TEST AS A COMPLETE BOARD.**

This continues the four-layer ground-plane checkpoint. The schematic, component values, footprint libraries, project design rules and provisional 1.66 mm stackup are unchanged.

## What is routed

U7 is the adjustable TPS62130 modem regulator. The existing 374 kOhm / 100 kOhm divider corresponds to a nominal 3.792 V setpoint with the nominal 0.8 V feedback reference. This is a calculated setpoint, not a measured voltage.

- Joined U7 SW pins 1/2/3 and connected them directly to L1 using a short front-side 0.80 mm power link, with 0.25 mm IC-land escapes.
- Joined VIN pins 10/11/12, routed C12 and C13 locally, and connected the additional C21 input bypass. Main input connections use 0.60 mm traces; pin escapes are 0.25 mm.
- Connected L1's filtered output to C18 using a 1.00 mm trace.
- Directly tied U7 AGND/PGND pins 6/15/16 to the exposed ground pad; also grounded DEF pin 8. The existing thermal through pads connect to the inner GND planes. Added local capacitor/divider ground vias.
- Routed the R25 enable pull-down and C19 soft-start circuit. PG pin 4 remains intentionally unconnected.
- Routed FB and the R26/R27 divider. VOS is taken separately from C18's output land, using a 0.20 mm quiet route on the outer layers with two transitions. The divider supply and FSW selection connect to that quiet output sense branch. Most of the sense route is on the back with In2.Cu as its ground reference. This route is approximately 13.4 mm from capacitor land to VOS pin and still requires analog/transient review before manufacturing.
- Connected TP3 as a low-current voltage-test spur.

**Future modem power distribution must originate from the C18 output node, with suitably sized copper. The 0.20 mm VOS/divider/FSW and 0.25 mm TP3 sense routes are not modem power feeds.** Preserve the separate capacitor sense takeoff when routing the heavy BB/RF branches. Those branches have not been routed in this checkpoint.

## Placement refinement

Moved/rotated exactly three existing capacitors, without changing their values or pad assignments:

| Part | New board position | Rotation | Reason |
| --- | --- | --- | --- |
| C12 | 35.70, 55.50 mm | 0 degrees | Local bulk input bypass near PVIN |
| C13 | 35.85, 58.00 mm | 0 degrees | Shorten the AVIN bypass connection |
| C21 | 35.50, 51.50 mm | 0 degrees | Make room for the local input arrangement; retain extra +5VD bypass |

All other footprint positions are preserved. C12/C21 reference labels were repositioned; C13 retains its fabrication-layer reference. Earlier placement maps are historical and do not show these three refinements.

## Checks performed

Native KiCad 10.0.7 after zone refill:

- 0 reported DRC violations, including warnings, in the main violations section.
- 298 separately reported unconnected items, down from 326. They remain errors for a finished board.
- 0 schematic-to-PCB parity issues.
- Native physical-connectivity graph traversal confirms that all local pad objects belong to one connected island within each of the seven local circuit nets: +5VD, GND, SW, FB, SS/TR, MODEM_SUPPLY_EN and MODEM_VBAT.
- All component values and pad/net assignments match the preceding ground-plane checkpoint. Exactly C12/C13/C21 changed placement.
- Added 72 track segments and 11 through vias. No inner-layer signal tracks were added. Inner layers remain GND planes.
- Independent checks found no footprint pad objects or checked fabrication body graphics outside the board or intersecting thermal cutouts. All eleven new via drill openings clear outer SMD-pad bounding boxes expanded by 0.05 mm. These checks do not replace assembler DFM review.

`u7-routing-review/` contains the native DRC report, connectivity verification, route-by-route geometry, via/containment checks and a copper preview. The preview superimposes front copper in red and back copper in blue; overlapping artwork from opposite sides does not imply a short.

TI reference: TPS6213x datasheet, Section 11 layout guidance and Figure 11-1: https://www.ti.com/lit/gpn/TPS62131 . Local input bypass, direct ground-pad ties, and capacitor-referenced sensing informed this routing. Datasheet reference does not constitute manufacturer approval of this PCB.

## Still unfinished

U7 is not yet connected to the USB-derived input supply or MCU enable signal. Modem VBAT_BB/VBAT_RF distribution, their bypass/bulk capacitors, and the remainder of the board are still unrouted. The U6 3.3 V regulator is the next power-stage routing task.

No hardware startup, output accuracy, load-step response, stability, EMI, current capability or thermal performance has been measured. Final capacitor MPNs/effective capacitance, complete output loading, regulator stability, input-current/inrush strategy, modem transmit bursts, rail loss and fabricator constraints still require review. Manufacturer stackup and controlled-impedance RF/USB geometry remain unfinalized. Existing schematic off-grid warnings remain unchanged. The broader BOM, mechanical, firmware, fabrication and real-hardware evidence work remains outstanding.

## Install and inspect

1. Close all KiCad windows and back up the current PCB outside the repository.
2. Extract this ZIP and copy the contents of its `Base` folder into `C:\Users\satvi\Downloads\AirCube-cellular\kicad\Base`, accepting replacement of the PCB. Retain the existing schematic, project and local libraries.
3. Open `AirCube.kicad_pro`, then PCB Editor. Press B to refill zones and run Inspect > Design Rules Checker > Run DRC. Expect 0 main violations and 298 unconnected reports in this environment.
4. U7 is at X=32 mm, Y=58 mm, on F.Cu. Inspect F.Cu and B.Cu routing; In1.Cu/In2.Cu remain ground references. The thin unrouted lines elsewhere are expected at this checkpoint.

## Record the design checkpoint in Git

In PowerShell at the repository root, first run `git status --short`. If the previous placement and ground-plane files are still uncommitted, stage the full intended current design set below; the list deliberately excludes lock files, local preferences, history and backup PCBs.

```powershell
git add -- kicad/Base/AirCube.kicad_pcb kicad/Base/AirCube.kicad_sch kicad/Base/AirCube.kicad_pro kicad/Base/fp-lib-table kicad/Base/sym-lib-table "kicad/Base/*.kicad_sym" kicad/Base/AirCube_Recovered.pretty "kicad/Base/README-*.md" kicad/Base/placement-review kicad/Base/ground-plane-review kicad/Base/u7-routing-review
git diff --cached --stat
git commit -m "Update cellular PCB placement and route local modem regulator"
git push
```

Review the staged file list before committing. This is a partial-design commit, not a production-release commit.
