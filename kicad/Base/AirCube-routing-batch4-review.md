# AirCube routing batch 4 — 25 October 2026

Partial routing review copy. Press B to refill the copper zones before checking connectivity or running DRC.

## Input and result

Based on AirCube(20261025-213224).kicad_pcb. Input SHA-256: 6f9ec4fa5d3b3f02d6ec0573df3b279f339266ce042edd9fc4b612423ed8796f.

Independent connectivity estimate: 147 missing connections before, 130 after native-equivalent plane-clearance reconstruction. Native KiCad after zone refill is authoritative.

Added 173 track segments and 18 through vias (16 non-GND, two GND). Final totals are 828 track segments and 94 vias. Existing footprints, tracks, vias, net assignments and zone boundaries/settings are unchanged.

## Important: zone refill is mandatory

New signal vias pass through the inner GND layers. They need GND copper clearance around them, not a connection to GND. The old saved fill polygons were removed from the output to prevent stale fills from overlapping these vias. Zone outlines, GND net assignments and fill settings are preserved.

The board may show more unconnected items or no filled planes immediately after opening. Press B, wait for refill, then save and run DRC. The expected 130 count applies AFTER refill. Do not export fabrication outputs from the unfilled file.

The independent audit predicts the new antipads by subtracting 0.201 mm clearances around the new non-GND via copper from the input plane fills. This prediction is used for checking only; native KiCad must regenerate the actual fills using your project rules.

## Completed connections

| Start | Destination | Net | Layers | Width (mm) | Track length (mm) | Via count |
|---|---|---|---|---:|---:|---:|
| U3.29 | U4.2 | /MODEM_VDD_1V8 | B.Cu/F.Cu | 0.2032 | 4.534 | 1 |
| U3.20 | U4.6 | /MODEM_STATUS_1V8 | B.Cu/F.Cu | 0.2032 | 21.073 | 1 |
| U3.36 | U4.5 | /MODEM_CTS_1V8 | B.Cu/F.Cu | 0.2032 | 8.955 | 1 |
| U3.37 | U4.4 | /MODEM_RTS_1V8 | B.Cu/F.Cu | 0.2032 | 9.741 | 1 |
| U1.9 | J1.3 | /PM_RX | B.Cu/F.Cu | 0.2032 | 18.419 | 1 |
| U1.8 | J1.2 | /PM_TX | B.Cu/F.Cu | 0.2032 | 20.692 | 3 |
| U1.7 | U4.17 | /MODEM_RTS_3V3 | B.Cu/F.Cu | 0.2032 | 41.322 | 2 |
| R12.1 | U4.10 | Net-(U4-OE) | B.Cu/F.Cu | 0.2032 | 11.803 | 2 |
| R14.2 | D1.1 | /SIM_RST_CARD | B.Cu/F.Cu | 0.2032 | 7.728 | 1 |
| R15.2 | D2.1 | /SIM_CLK_CARD | B.Cu/F.Cu | 0.2032 | 15.109 | 1 |
| R23.2 | D3.1 | /SIM_DATA_CARD | B.Cu/F.Cu | 0.2032 | 19.829 | 1 |
| R24.2 | J2.1 | /SIM_VDD | B.Cu/F.Cu | 0.254 | 8.436 | 1 |
| U11.3 | U11.11 | GND | B.Cu | 0.1524 | 4.664 | 0 |
| U11.5 | U11.10 | GND | B.Cu | 0.1524 | 6.23 | 0 |
| U8.7 | U8.8 | +5VD | F.Cu | 0.254 | 0.641 | 0 |
| U11.3 | inner GND planes | GND | B.Cu | 0.1524 | 0.725 | 1 |
| U11.5 | inner GND planes | GND | B.Cu | 0.1524 | 1.249 | 1 |

The PM connector UART pair is now routed. SIM reset, clock, data and supply groups are now linked across layers to the card/ESD networks. These connectivity results do not constitute a full SIM signal-integrity or hardware-function sign-off.

U11 uses 0.1524 mm tracks for fine-pitch GND breakouts; the new different-net copper gaps still meet the 0.20 mm audit threshold. U8 same-net output pins are joined by a short 0.254 mm connection. This is not completion or current-capacity sign-off of the main power feed.

## Checks completed

- Verified every listed endpoint join, including both U11 ground groups reaching the predicted inner planes.
- Checked the entire modeled outer-layer copper for different-net overlaps: none found.
- New tracks checked against the copper on their own layer; new vias checked against copper on all four layers.
- No newly introduced copper clearance below 0.20 mm. Minimum measured new gap: 0.206 mm.
- All nine board/footprint rule areas included, using their board-coordinate polygon points and layer restrictions. No track/via keepout violations found.
- New drill edge-to-edge gap minimum: 0.506 mm. No new hole gap below 0.25 mm.
- New drill-to-surface-solder-pad edge gap minimum: 0.217 mm.
- Predicted new signal via to inner GND fill gap minimum: 0.201 mm.
- Parsed output and compared all original footprints/tracks/vias and zone boundary/settings data with the input. Only copper additions and cached-fill invalidation are present.
- Inspected front/back copper plots with footprint keepout outlines.

## Remaining priorities

- MCU-to-level-shifter modem TX/RX and modem-to-level-shifter TX/RX still need different breakout paths. Candidate detours for the latter were rejected.
- C8/C9 supply/decoupling placement and routes need focused review. A long supply-to-capacitor route was rejected; no footprint was moved.
- Main 3.3 V supply, modem VBAT feeds and local input/output capacitor paths require current/voltage-drop/burst-current and layout review.
- Remaining I2C buses, sensor upstream supplies and previously deferred sensor joins remain incomplete.
- Remaining USB coordinated routing, controller CC/power wiring, ground connections, RF feed/antenna keepouts, schematic/BOM/footprint/manufacturing checks, firmware and bench testing remain outstanding.

## Native verification

1. Open the review board in a copy of your existing project using the same .kicad_pro/.kicad_dru rules.
2. Press B to refill all zones, then save.
3. Run full DRC and save the report with errors, warnings, exclusions and unconnected items included.
4. Send the saved PCB and full report. Expected missing connections after refill: 130.

Native KiCad/kicad-cli is unavailable in the editing environment. No native open/refill/DRC pass is claimed. The project-rule files, schematic and manufacturer constraints were not supplied for this batch. This board is incomplete and must not be fabricated yet.
