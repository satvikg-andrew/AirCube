# AirCube cellular/PM2.5 placement checkpoint

**UNROUTED. NOT READY TO ORDER OR FABRICATE.** This package corrects placement and project portability. It is not a completed electrical, RF, mechanical, manufacturing, firmware, or hardware validation release.

## Verification

Checked with native KiCad 10.0.7 against the included project rules and official 10.0.7 libraries:

| Check | Result |
| --- | --- |
| Placement DRC violations (including warnings) | 0 |
| Unconnected DRC reports, separately reported by KiCad | 331; routing is still required |
| PCB/schematic parity issues | 0 |
| Schematic ERC errors | 0 |
| Schematic warnings | 132 existing off-grid endpoint warnings |
| Schematic connectivity comparison | All 156 net names and reference/pin memberships unchanged |
| Footprint pad-object containment | All 558 checked; no objects outside the rounded board or intersecting thermal cutouts |
| Fabrication body-graphic containment | No checked body graphics outside the board or intersecting cutouts |

The containment check is a separate conservative 2-D check, including paste-only pad objects. It supplements native DRC; it does not validate enclosure fit, part heights, solder joints, SIM-lid opening, antenna cables, or connector mating. The 331 unconnected reports are errors in a completed-board DRC, not waived connections. The 132 schematic warnings remain visible; no schematic wires were snapped automatically.

Reports, a geometry check, netlist comparison, and front/back placement maps are in `placement-review/`. The PCB remains the inherited two-copper-layer project at this checkpoint. No manufacturing stackup or controlled-impedance dimensions have been approved.

## Changes and reasons

- Repositioned all electrical parts onto the original 45 mm x 45 mm board, preserving its outline, sensor isolation slots, three mounting holes, and fiducial positions. Parts are distributed over both sides. Existing sensor positions are preserved. Placement is a starting point for routing, not a guarantee that every high-current or RF route is complete or optimized.
- Separated the front-side BG95 from the back-side S3 module's plated ground pads. Opposite-side placement does not isolate through-hole copper. Regulator thermal pads and connector holes were also checked against the opposite side.
- Regrouped each buck regulator with its inductor, input/output capacitors, feedback and soft-start parts. Actual switching loops, return currents, feedback routing, rail widths and copper heating still require routing review.
- Created project-local U1/U6/U7 footprint variants with 0.30 mm thermal drills and 0.60 mm copper pads, replacing twenty 0.20 mm drills that violated the existing 0.254 mm minimum-hole rule. Signal land positions are unchanged. The nominal annular ring is 0.15 mm. This is a manufacturing geometry choice, not relaxation of the drill rule. Confirm finished-hole tolerances, via treatment, paste/solder-wicking behavior and assembly acceptance with the selected fabricator before release.
- Replaced U8's provisional generic lead pattern with a TPS22975 DSG land pattern: 0.50 x 0.25 mm peripheral lands at x = +/-0.95 mm, 0.50 mm pitch, and a 0.90 x 1.60 mm grounded exposed pad. Included 0.07 mm NSMD expansion and two 0.90 x 0.70 mm paste windows centered at y = +/-0.45 mm. This follows the TI DSG0008A example board/stencil geometry; copper routing and thermal grounding remain unfinished.
- Removed the obsolete H2 antenna copper-pour exclusion. Replaced the old board-wide upper copper-pour exclusion with two local sensor-island exclusions, leaving space for the cellular RF ground reference. When changing to a four-layer stackup, review those exclusions on every copper layer. No ground planes have been poured yet.
- Enabled courtyard-overlap and through/nonplated-hole-in-courtyard errors. Set minimum copper-to-board-edge clearance to 0.25 mm. Electrical clearance and hole rules were not weakened, and no new DRC exclusions were added.
- Moved component values to fabrication layers. Kept 95 reference labels on production silk; 22 dense references remain on fabrication layers, listed in `silkscreen-labels.json`. Retained original decorative artwork on documentation layers rather than copper/mask/silk. The old misplaced Boot legend is also on a documentation layer.
- Recovered embedded `custom_IC` and `SAMC21_breakout-rescue` symbols into project-local libraries. Preserved the individually edited LED symbol variants, including their existing pin definitions. Relinked 22 inherited footprint instances to their recovered project copies. Schematic footprint fields match the PCB, including the four new manufacturing variants. Native netlist comparison confirms unchanged connectivity.

The LED, switch and connector positions changed. The board outline and holes alone do not establish compatibility with existing light pipes or case openings. SW1 is RESET; SW2 is BOOT. Both are on the back. The SPS30 connector J1 is on the front; SIM J2 and debug/service headers J4/J5 are on the back. Use footprint pin numbers and the schematic to identify connector orientation, not an assumed left-to-right view of an image.

## Remaining work before production review

1. Select the fabricator/assembler and its actual stackup; a four-layer layout with a continuous ground reference is the proposed next step. Establish copper, drill, mask, via and impedance constraints before routing.
2. Route and review the buck switching loops and ground returns, VBAT star branches and modem burst-current paths. Calculate losses, voltage droop, capacitor effective capacitance, regulator stability with the complete load capacitance, startup/inrush, and USB-C available-current behavior. Verify thermals and current limits for the final parts and operating modes.
3. Route the LTE feed/matching network with a continuous 50-ohm reference, ground stitching and suitable transitions. Route USB as the appropriate differential pair. Review the BG95 USB service header/cable as a high-speed path; the header arrangement is not a validated high-speed USB implementation. Route SIM signals and confirm ESD placement against contact locations and return paths. Placement may need adjustment as these routes are completed.
4. Freeze exact purchasable MPNs, ratings and assembly orientations for every part. Select the BG95 SKU, US-supported LTE-M/NB-IoT SIM/provider, LTE antenna and S3 external BLE antenna, with correct connectors and bands. The S3-WROOM-1U needs an external antenna for BLE. Verify the PM sensor harness pinout and connector mating. This package does not establish availability or carrier certification.
5. Check the real enclosure, LED visibility, part heights on both sides, SIM insertion/lid travel, header access, antenna cable bends and SPS30 airflow/mounting. The external SPS30 is not included as a 3-D model.
6. Resolve/review the 132 off-grid schematic warnings carefully while preserving connectivity. Complete final schematic/datasheet and footprint/pinout review. Re-run ERC, DRC, schematic parity and manufacturing checks after every material change. A clean placement DRC alone does not prove a working circuit.
7. Produce the final BOM, pick-and-place, gerbers, drill files, assembly drawings and reviewed fabrication package. No fabrication outputs from the old design are included here.
8. Finish ESP-IDF C firmware, build/flash instructions, modem/SIM/HTTPS retry handling, PM2.5 and existing sensor operation, LED behavior and power management. Then fabricate, bring up and record real cellular PM2.5 logs/video. None of those hardware results are claimed by this checkpoint.

## Primary references for the footprint/layout work

- TI TPS22975 datasheet, DSG0008A example board layout and stencil design: https://www.ti.com/lit/ds/symlink/tps22975.pdf
- TI TPS6213x datasheet, layout and thermal guidance: https://www.ti.com/lit/ds/symlink/tps62130.pdf
- Espressif S3-WROOM-1/1U module datasheet: https://documentation.espressif.com/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf
- Espressif PCB layout guidance: https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32s3/pcb-layout-design.html

Original AirCube attribution and repository licensing remain applicable. Keep this checkpoint's design notes separate from the final build/test evidence so an unfinished board is not presented as validated hardware.
