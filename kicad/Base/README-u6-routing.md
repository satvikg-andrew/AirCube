# AirCube U6 regulator and regulator-input-link checkpoint

**PARTIALLY ROUTED. NOT A FABRICATION RELEASE OR A POWERED HARDWARE TEST RESULT.**

This continues the U7 routing checkpoint. Component values, footprint identities, pad/net assignments, schematic, project rules and provisional physical stackup are unchanged. It adds 70 track segments and 12 vias; the current board has 142 track segments and 23 added routing vias in total, in addition to the thermal through pads already in footprints.

## What changed

- Routed U6's fixed 3.3 V TPS62132 local circuit: three SW pins to L2, VIN pins and local C20/C25 bypass, EN tied to the input supply, direct ground/exposed-pad ties, grounded fixed-output FB pin, C28 soft-start, and the filtered output to C26/C22. PG remains intentionally unconnected.
- Main SW, input and output links use 0.80, 0.60 and 1.00 mm copper respectively, with short 0.25 mm IC-land escapes. These are routing dimensions, not proof of current/thermal capability.
- Routed a separate 0.20 mm capacitor-referenced VOS line with two outer-layer transitions. FSW is tied to the quiet output branch. The sense route is approximately 13.4 mm and still needs final analog/transient review.
- Connected TP2 using a 0.80 mm output power stub from C26. Future 3.3 V load distribution should branch from the output power copper, not the thin VOS/FSW sense wiring.
- Joined the U7 and U6 +5VD input networks using outer-layer copper and four 0.80/0.40 mm through vias. The approximately 33.3 mm, 0.60 mm link goes around the S3's through-board ground-pad array and existing sense routing. No inner-layer power or signal tracks were added.
- Preserved U7's prior track and via objects. C18/L2 silkscreen reference fields were moved/rotated to clear new C22 placement; C25's reference is on its fabrication layer. No U7 component placement changed.

## Four capacitor placement refinements

| Part | New position | Rotation | Purpose |
| --- | --- | --- | --- |
| C20 | 35.70, 66.50 mm | 0 degrees | Bulk input bypass near U6 VIN |
| C25 | 35.85, 69.00 mm | 0 degrees | Local AVIN bypass |
| C22 | 26.50, 65.40 mm | 0 degrees | Additional output bypass near L2 |
| C28 | 35.50, 71.00 mm | 0 degrees | Local soft-start routing |

Values and pad assignments did not change. Earlier placement maps are historical.

## Verification

Native KiCad 10.0.7 after zone refill:

- 0 main DRC violations, including warnings.
- 273 separately reported unconnected items, down from 298. These remain errors for a finished board.
- 0 schematic-to-PCB parity issues.
- Native physical-connectivity traversal confirms all pads in U6's five local nets are connected, and all pads in U7's seven local nets remain connected.
- Native connectivity also confirms C12's +5VD pad and C20's +5VD pad are physically joined.
- Both inner GND zones retain a single continuous filled region. Sensor thermal exclusions remain on all four copper layers.
- Independent comparison confirms unchanged global component values and pad/net assignments, and exactly the four capacitor placement changes listed above.
- New drill openings clear the outer SMD-pad bounding boxes expanded by 0.05 mm. Checked footprint pads and fabrication body graphics remain inside the board and clear of its thermal cutouts. These are geometric checks, not assembler DFM approval.

A trace-only DC calculation for the new input link assumes 35 um copper at 20 C. It gives roughly 27 mOhm, or 27 mV drop at 1 A. Actual via, source/cable and other routing loss is excluded, as are temperature and transient effects. This is not a completed power budget or current rating. Details are in `u6-routing-review/input-link-dc-estimate.json`.

The copper preview overlays front copper in red and back copper in blue. Opposite-side pads may overlap visually. Use the native layer view for inspection.

TI reference for pin connections and local routing guidance: TPS6213x datasheet, pin functions and Section 11: https://www.ti.com/lit/gpn/TPS62131 . The fixed-output FB connection, direct ground ties, local bypass and capacitor-referenced sense routing follow that guidance; circuit performance has not been measured.

## Still unfinished

The USB-C/raw-input/load-switch power path is not yet routed into the regulator input network. The MCU and other 3.3 V loads, LED/PM 5 V loads, modem VBAT_BB/VBAT_RF distribution, U7 MCU enable connection, and most remaining signals are still unrouted. Both regulators' local routing being connected does not mean either has been powered or tested.

Next: complete the USB power path, then connect the MCU supply/boot/reset circuitry and modem supply branches. Final MPNs, effective capacitance, full-load stability, USB-C current/inrush behavior, cable/source droop, transmit bursts, thermal behavior, mechanical fit, manufacturing stackup, RF/USB impedance geometry, firmware and real hardware evidence remain to be completed/reviewed.

## Install

1. Close all KiCad windows and back up the current PCB outside the repository.
2. Extract this ZIP. Copy its `Base` contents into `C:\Users\satvi\Downloads\AirCube-cellular\kicad\Base`, replacing the PCB and keeping all existing project, schematic and local libraries.
3. Open `AirCube.kicad_pro`, then PCB Editor. Press B to refill zones. Run Inspect > Design Rules Checker > Run DRC. Expected here: 0 main violations, 273 unconnected reports.
4. U6 is at X=32 mm, Y=69 mm on F.Cu. The new +5VD link uses front/back routing around the left edge of the power-stage area. Both inner layers remain GND references.

## Save a real Git checkpoint

In PowerShell at the repository root, review `git status --short`. This explicit file list also captures any still-uncommitted earlier placement/ground-plane/U7 design files while excluding history, lock files, local preferences and backup PCBs:

```powershell
git add -- kicad/Base/AirCube.kicad_pcb kicad/Base/AirCube.kicad_sch kicad/Base/AirCube.kicad_pro kicad/Base/fp-lib-table kicad/Base/sym-lib-table "kicad/Base/*.kicad_sym" kicad/Base/AirCube_Recovered.pretty "kicad/Base/README-*.md" kicad/Base/placement-review kicad/Base/ground-plane-review kicad/Base/u7-routing-review kicad/Base/u6-routing-review
git diff --cached --stat
git commit -m "Route local power stages and join regulator inputs"
git push
```

Review the staged file list before committing. This is a partial-design checkpoint, not a production release.
