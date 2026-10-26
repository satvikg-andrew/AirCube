# AirCube routing batch 3 — 25 October 2026

Partial routing review copy. Native KiCad DRC and complete electrical/manufacturing review are still required.

## Input and result

Based on AirCube(20261025-211209).kicad_pcb. Source SHA-256: 67e211c4ca28d7f35480658b0fc1902440ed7cd300804aa3e00b3ec52eeb70a3.

Geometric missing-connection count: 198 before, 147 after (51 fewer). The final board contains 656 tracks and 76 vias. Added 39 GND through vias, each 0.6 mm diameter / 0.3 mm drill. There were 180 staged new track segments; replacing two old stubs with one replacement track produces a net increase of 179 tracks.

## Completed work

- Modem-side SIM supply, reset, data and clock connections to their local resistor/filter networks. The F.Cu filter networks still need the remaining cross-layer links to the SIM socket/ESD networks; the interface is not fully routed.
- All 29 GND pads of U3 now reach the saved inner GND planes. One perimeter ground pad reaches the planes through its adjacent grounded pad; the others have short local via returns, including the modem interior ground lands.
- Ground returns for modem supply capacitors C33-C37, C8, R13, U4, the LED chain, and U8.
- R12 pad 2 to C8 pad 1 local 1.8 V connection. This group still needs its remaining modem/translator supply connections.
- Local user-button/resistor wiring and ties between matching U8 input-power pins. These are local same-net joins, not completion or sign-off of the board main power path.

## C3 via correction

The existing C3 GND via at (45.9, 56.8) partly occupied the front-side modem GND solder land. This was electrically GND-to-GND but placed a drill in the solder-pad area. It was moved to (44.975, 57.5), retaining its UUID, size and net. Two obsolete tracks to the old location were removed and one replacement B.Cu GND track added from C3 pad 2. C3/U1 grounding and the modem pad grounding were independently rechecked after this edit.

All source board items other than that via position and the two obsolete GND track stubs are unchanged. Footprints and copper-zone data are identical to the input.

## Endpoint additions and returns

The list records routing operations; an extra return can reinforce a group that already reaches GND, so its row count does not equal the number of removed missing connections.

| Start | Destination | Net | Layer | Width (mm) | Track length (mm) |
|---|---|---|---|---:|---:|
| U3.46 | R15.1 | /SIM_CLK_MODEM | F.Cu | 0.2032 | 4.206 |
| U3.45 | R23.1 | /SIM_DATA_MODEM | F.Cu | 0.2032 | 3.958 |
| U3.43 | R24.2 | /SIM_VDD | F.Cu | 0.254 | 6.013 |
| U3.44 | R14.1 | /SIM_RST_MODEM | F.Cu | 0.2032 | 9.272 |
| R12.2 | C8.1 | /MODEM_VDD_1V8 | B.Cu | 0.254 | 8.12 |
| R19.1 | R20.1 | /USER_BUTTON | F.Cu | 0.2032 | 4.013 |
| R20.2 | S3.1 | Net-(R20-Pad2) | F.Cu | 0.2032 | 5.875 |
| S3.1 | S3.2 | Net-(R20-Pad2) | F.Cu | 0.2032 | 3.65 |
| S3.3 | S3.4 | +3V3 | F.Cu | 0.3048 | 3.65 |
| U8.1 | U8.2 | /USB_VBUS_RAW | F.Cu | 0.4572 | 0.641 |
| U8.2 | U8.3 | /USB_VBUS_RAW | F.Cu | 0.4572 | 0.641 |
| U8.3 | U8.4 | /USB_VBUS_RAW | F.Cu | 0.4572 | 0.641 |
| U3.3 | inner GND planes; via 38.45, 56.5 mm | GND | F.Cu | 0.3048 | 1.0 |
| U3.31 | inner GND planes; via 55.65, 74.1 mm | GND | F.Cu | 0.3048 | 1.0 |
| U3.47 | inner GND planes; via 56.75, 56.5 mm | GND | F.Cu | 0.3048 | 1.0 |
| U3.48 | inner GND planes; via 56.75, 55.7 mm | GND | F.Cu | 0.3048 | 1.124 |
| U3.50 | inner GND planes; via 55.65, 52.1 mm | GND | F.Cu | 0.3048 | 1.0 |
| U3.54 | inner GND planes; via 50.75, 52.1 mm | GND | F.Cu | 0.3048 | 1.207 |
| U3.55 | inner GND planes; via 50.15, 52.1 mm | GND | F.Cu | 0.3048 | 1.0 |
| U3.58 | inner GND planes; via 44.95, 53.9 mm | GND | F.Cu | 0.3048 | 1.207 |
| U3.61 | inner GND planes; via 42.15, 52.1 mm | GND | F.Cu | 0.3048 | 1.0 |
| U3.62 | inner GND planes; via 40.25, 53.0 mm | GND | F.Cu | 0.3048 | 0.9 |
| U3.67 | inner GND planes; via 41.65, 66.55 mm | GND | F.Cu | 0.3048 | 1.041 |
| U3.68 | inner GND planes; via 41.65, 68.25 mm | GND | F.Cu | 0.3048 | 1.041 |
| U3.69 | inner GND planes; via 45.05, 71.95 mm | GND | F.Cu | 0.3048 | 1.224 |
| U3.70 | inner GND planes; via 48.45, 72.25 mm | GND | F.Cu | 0.3048 | 1.249 |
| U3.71 | inner GND planes; via 48.65, 70.95 mm | GND | F.Cu | 0.3048 | 1.273 |
| U3.72 | inner GND planes; via 51.55, 72.95 mm | GND | F.Cu | 0.3048 | 1.549 |
| U3.73 | inner GND planes; via 55.35, 68.25 mm | GND | F.Cu | 0.3048 | 1.041 |
| U3.74 | inner GND planes; via 55.35, 66.55 mm | GND | F.Cu | 0.3048 | 1.041 |
| U3.79 | inner GND planes; via 51.95, 56.35 mm | GND | F.Cu | 0.3048 | 1.141 |
| U3.80 | inner GND planes; via 49.35, 55.45 mm | GND | F.Cu | 0.3048 | 1.041 |
| U3.81 | inner GND planes; via 47.65, 55.45 mm | GND | F.Cu | 0.3048 | 1.041 |
| U3.82 | inner GND planes; via 45.05, 56.55 mm | GND | F.Cu | 0.3048 | 1.183 |
| U3.89 | inner GND planes; via 45.05, 70.45 mm | GND | F.Cu | 0.3048 | 1.349 |
| U3.90 | inner GND planes; via 47.65, 69.05 mm | GND | F.Cu | 0.3048 | 1.041 |
| U3.91 | inner GND planes; via 49.35, 69.05 mm | GND | F.Cu | 0.3048 | 1.041 |
| U3.100 | inner GND planes; via 50.05, 57.35 mm | GND | F.Cu | 0.3048 | 0.99 |
| U3.101 | inner GND planes; via 47.85, 58.95 mm | GND | F.Cu | 0.3048 | 1.266 |
| U3.102 | inner GND planes; via 45.05, 58.05 mm | GND | F.Cu | 0.3048 | 1.141 |
| C33.2 | inner GND planes; via 64.14, 76.6 mm | GND | F.Cu | 0.3048 | 1.721 |
| C34.2 | inner GND planes; via 50.44, 49.0 mm | GND | F.Cu | 0.3048 | 1.18 |
| C35.2 | inner GND planes; via 56.8, 47.925 mm | GND | F.Cu | 0.3048 | 0.85 |
| C36.2 | inner GND planes; via 55.1, 47.925 mm | GND | F.Cu | 0.3048 | 0.85 |
| C37.2 | inner GND planes; via 53.4, 47.925 mm | GND | F.Cu | 0.3048 | 0.85 |
| C8.2 | inner GND planes; via 65.6, 70.525 mm | GND | B.Cu | 0.3048 | 1.016 |
| R13.2 | inner GND planes; via 65.225, 81.5 mm | GND | B.Cu | 0.3048 | 1.016 |
| U4.11 | inner GND planes; via 61.5625, 71.375 mm | GND | B.Cu | 0.3048 | 1.39 |
| LED2.4 | inner GND planes; via 40.175, 44.325 mm | GND | F.Cu | 0.3048 | 0.771 |
| U8.5 | inner GND planes; via 56.75, 79.65 mm | GND | F.Cu | 0.3048 | 0.824 |
| U8.9 | inner GND planes; via 55.1, 79.7 mm | GND | F.Cu | 0.3048 | 1.566 |
| U3.58 | U3.59 | GND | F.Cu | 0.3048 | 1.2 |

## Checks performed

- Reparsed the final output independently after the C3 correction.
- Audited modeled copper on all layers for different-net overlap: none found.
- Audited all newly added and moved copper against other-net copper. No new gap below 0.20 mm; minimum measured new copper gap 0.208 mm.
- Added/moved drill-to-drill spacing checked: minimum hole-edge gap 0.255 mm; none below the 0.25 mm audit threshold. Manufacturer and project rules remain authoritative.
- New/moved drill edges are at least 0.20 mm from every represented surface-pad edge, avoiding drilled overlap of component solder lands.
- Verified all listed endpoint joins and ground returns, all 29 modem GND pads, and preserved zone/footprint data.
- Inspected front- and back-copper plots, including the relocated C3 via.

## Required KiCad check

1. Keep a backup and open this review PCB inside a copy of your existing project, using the same .kicad_pro/.kicad_dru rules.
2. Press B to refill every copper zone; save.
3. Run full DRC, retaining errors, warnings, exclusions and unconnected items.
4. Send the saved PCB and full report. Expected missing-connection count: 147. A matching number alone is not a DRC pass.

KiCad/kicad-cli is unavailable in the editing environment. No native KiCad open, refill, or DRC pass is claimed. Project-rule files, schematic, BOM, and manufacturer stackup/rules were not provided for this batch.

## Still outstanding

- Main MCU and modem supply paths, high-current trace/via sizing, transmit-burst budget and complete decoupling/layout review.
- Remaining modem UART/flow-control/OE and PM sensor UART routing.
- Remaining SIM filter-to-socket cross-layer joins; full SIM ESD placement/path review.
- U4 pad 2 to C8 pad 1 and U4 pad 19 to C9 pad 1: no acceptable single-layer route found in this batch.
- R19 ground return and U11 fine-pitch ground breakouts: require a different route/escape solution. U8 output-pin tie also remains incomplete.
- Two sensor connections flagged in batch 2, remaining sensor buses and upstream supplies.
- USB coordinated differential routing, RF feed/impedance/antenna keep-outs, remaining ground connections, schematic/BOM/footprint/manufacturing checks, firmware, and physical bring-up.

This partial board must not be sent for fabrication yet.
