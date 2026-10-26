# AirCube routing batch 2 — 25 October 2026

Partial routing review copy, not a fabrication release.

## Source and scope

Based on AirCube(20261025-210502).kicad_pcb. Input SHA-256: d4e619b322b30bb12d415412c5f5909b06eda7a17142dc0bf0cbec17d00a08ad.

Added 34 connections: local sensor supply/ground wiring, SIM resistor/filter wiring, three SIM ESD-to-card connections, four SIM ground returns, and local RGB LED chain/supply/ground connections. Thermal-isolation copper-pour exclusions were preserved.

## Connection list

| Start | Destination | Net | Layer | Width (mm) | Track length (mm) |
|---|---|---|---|---:|---:|
| U2.8 | U2.9 | GND | F.Cu | 0.2032 | 1.121 |
| C15.2 | U2.3 | GND | F.Cu | 0.254 | 1.883 |
| C15.2 | C14.2 | GND | F.Cu | 0.254 | 1.7 |
| U5.2 | C23.2 | GND | B.Cu | 0.254 | 4.342 |
| C23.2 | C5.2 | GND | B.Cu | 0.254 | 2.871 |
| U10.4 | U10.5 | GND | F.Cu | 0.2032 | 0.991 |
| U10.4 | C32.2 | GND | F.Cu | 0.254 | 3.867 |
| U2.4 | C15.1 | +1V8 | F.Cu | 0.254 | 1.895 |
| C15.1 | C14.1 | +1V8 | F.Cu | 0.254 | 1.6 |
| U2.5 | U2.7 | +3V3 | F.Cu | 0.254 | 3.114 |
| U5.1 | U5.3 | +3V3 | B.Cu | 0.254 | 3.622 |
| U5.1 | C5.1 | +3V3 | B.Cu | 0.3048 | 8.15 |
| U10.1 | C32.1 | +3V3 | F.Cu | 0.254 | 1.611 |
| R14.2 | C7.1 | /SIM_RST_CARD | F.Cu | 0.2032 | 1.65 |
| R15.2 | C10.1 | /SIM_CLK_CARD | F.Cu | 0.2032 | 1.65 |
| R23.2 | C6.1 | /SIM_DATA_CARD | F.Cu | 0.2032 | 1.65 |
| R23.2 | R24.1 | /SIM_DATA_CARD | F.Cu | 0.2032 | 2.613 |
| R24.2 | C11.1 | /SIM_VDD | F.Cu | 0.254 | 1.774 |
| D1.1 | J2.2 | /SIM_RST_CARD | B.Cu | 0.2032 | 2.694 |
| D2.1 | J2.3 | /SIM_CLK_CARD | B.Cu | 0.2032 | 2.633 |
| D3.1 | J2.7 | /SIM_DATA_CARD | B.Cu | 0.2032 | 2.436 |
| C7.2 | C10.2 | GND | F.Cu | 0.254 | 1.75 |
| C10.2 | C6.2 | GND | F.Cu | 0.254 | 1.75 |
| C6.2 | C11.2 | GND | F.Cu | 0.254 | 1.65 |
| LED1.3 | LED2.1 | Net-(LED1-DOUT) | F.Cu | 0.2032 | 2.485 |
| LED2.3 | LED3.1 | Net-(LED2-DOUT) | F.Cu | 0.2032 | 2.485 |
| LED1.2 | LED2.2 | +5VD | F.Cu | 0.3048 | 3.768 |
| LED2.2 | LED3.2 | +5VD | F.Cu | 0.3048 | 3.768 |
| LED1.4 | LED2.4 | GND | F.Cu | 0.254 | 3.685 |
| LED2.4 | LED3.4 | GND | F.Cu | 0.254 | 3.685 |
| C11.2 | inner GND planes; via 66.875, 60.1 mm | GND | F.Cu | 0.3048 | 0.75 |
| D1.2 | inner GND planes; via 57.65, 51.9 mm | GND | B.Cu | 0.3048 | 0.783 |
| D2.2 | inner GND planes; via 55.05, 51.9 mm | GND | B.Cu | 0.3048 | 0.824 |
| D3.2 | inner GND planes; via 52.45, 51.9 mm | GND | B.Cu | 0.3048 | 0.866 |

## Validation performed

- All original parsed board items were preserved unchanged. Only 146 track segments and four GND vias were added. The output totals 477 track segments and 37 vias.
- Each listed connection was geometrically verified.
- Entire modeled outer-layer copper checked for different-net overlap: none found. Added through vias checked against all four copper layers.
- No newly introduced different-net copper gap below 0.20 mm. Minimum measured gap among audited new-feature candidate pairs: 0.279 mm.
- Added drills checked against modeled drilled pads and vias: no new drill-gap issue below 0.25 mm; minimum measured new drill edge gap 2.300 mm.
- Each added GND via (0.6 mm diameter, 0.3 mm drill) lies inside the saved copper fill on both inner GND planes.
- Independent connectivity calculation: 232 missing connections before; 198 after. Native KiCad results after refill are authoritative.
- Generated front- and back-copper views inspected. No component moves, existing track deletions, net changes, or copper-zone edits.

## Connections intentionally left for a different routing solution

- U2 pad 3 to the U2 pad 8/9 GND group remains incomplete. A long single-layer detour was rejected.
- U5 pad 5 to C23 pad 1 remains incomplete. Ground-return routing was prioritized; the remaining bottom-layer path for this output would be too long.
- Local sensor supplies are not yet joined to every upstream supply source. Local LED supply/ground groups still need their connections to the wider networks.
- SIM card nets still need the remaining modem-to-card/filter links and SIM supply connection; this batch does not complete the SIM interface.
- Previous remaining tasks still apply: MCU regulator supply, modem burst-current path review, PM UART, modem UART/flow control, OE, USB, RF, remaining sensor buses, schematic/BOM/manufacturing review, firmware and hardware bring-up.

## Required next check

Native KiCad is unavailable in the editing environment. This is a geometric audit, not a native DRC pass, schematic parity check, RF review, current-capacity sign-off, or production approval.

1. Preserve a backup of your current project.
2. Open this PCB in a copy of the same project with its existing .kicad_pro/.kicad_dru rules. Rename the review board to the project board filename inside that copied project if needed.
3. Press B to refill all zones and save.
4. Run the complete DRC, including errors, warnings, exclusions and unconnected items.
5. Send the saved PCB and full DRC report for review. Expected missing connection count is 198. Do not fabricate this incomplete layout.
