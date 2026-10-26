# AirCube routing batch — 25 October 2026

Review copy. This is a partial routing update, not a fabrication release.

## Starting point

Based only on AirCube(20261025-173503).kicad_pcb, the final saved version supplied in this conversation. Source SHA-256: cdf6729b737dd80849f26f4705e13f446c8cc593865be3be4258870fd4cc0eec.

## Added connections

| Start | Destination | Net | Layer / width |
|---|---|---|---|
| U1.17 | R8.2 | /MODEM_PWRKEY_CTL | B.Cu / 0.2032 mm |
| U1.18 | R11.2 | /MODEM_RESET_CTL | B.Cu / 0.2032 mm |
| U1.20 | U4.15 | /MODEM_STATUS_3V3 | B.Cu / 0.2032 mm |
| U1.12 | U4.16 | /MODEM_CTS_3V3 | B.Cu / 0.2032 mm |
| R12.1 | R13.1 | Net-(U4-OE) | B.Cu / 0.2032 mm |
| U1.40 | inner GND planes; via at 27.25, 55.89 mm | GND | B.Cu / 0.3048 mm |
| R6.2 | inner GND planes; via at 47.325, 77.2 mm | GND | B.Cu / 0.3048 mm |
| Q2.2 | inner GND planes; via at 48.8625, 73.85 mm | GND | B.Cu / 0.3048 mm |
| R7.2 | inner GND planes; via at 52.925, 72.7 mm | GND | B.Cu / 0.3048 mm |
| Q3.2 | inner GND planes; via at 52.8625, 73.95 mm | GND | B.Cu / 0.3048 mm |
| C9.2 | inner GND planes; via at 55.2, 70.025 mm | GND | B.Cu / 0.3048 mm |

Added 85 track segments on B.Cu and six GND through vias (0.6 mm diameter, 0.3 mm drill). Signal tracks are 0.2032 mm; ground tracks are 0.3048 mm.

## Checks completed

- Compared parsed input and output: every original board item remains unchanged; only the listed copper features were appended.
- Verified all 11 requested endpoint connections geometrically.
- Checked all input and added outer-layer copper, including rotated pad shapes and vias, for different-net overlap: none found.
- Checked new tracks against other-net copper on B.Cu; checked new through vias against copper on all four layers. No new copper gap below 0.20 mm was found. Minimum measured new-copper gap in the candidate-pair audit: 0.268 mm.
- Checked added drills against represented existing drilled pads and vias. Minimum new hole-to-hole edge gap: 0.952 mm.
- Verified each added GND via is inside the saved GND copper fills on both inner layers.
- Independent geometric connectivity calculation: 243 missing connections before, 232 after. This is an estimate to compare with KiCad after zone refill, not a native DRC result.
- Visually inspected the generated bottom-copper overview and MCU/modem-control area.

## Required native verification

KiCad/kicad-cli is not installed in the editing environment. The output has been parsed and geometrically checked, but has NOT been opened, refilled, or DRC-tested in native KiCad. Project-level .kicad_pro/.kicad_dru files and the current schematic were not supplied with this batch, so their rules and schematic parity were not independently checked.

1. Keep your existing project as a backup.
2. Open this PCB in a copy of your existing project using the same project settings/rules. If needed, rename the review PCB to the project board filename inside that copied project directory.
3. Press B to refill every copper zone, then save. Existing fills were preserved, but native refill is required after editing.
4. Run the full DRC with zone refill enabled and include errors, warnings, exclusions, and unconnected items in the report.
5. Send the saved PCB and DRC report before routing the next batch. Do not send this partial board for fabrication.

## Still unfinished

- MCU +3V3 network still needs its regulator-supply connection and current-path review.
- PM_TX and PM_RX connector routing, remaining modem UART/flow-control routing, and the U4 output-enable connection remain incomplete. R12/R13 are now joined to one another; their group still needs U4 pad 10.
- Remaining SIM, RF/antenna, sensor, power, and USB routing needs completion and separate review.
- Regulator high-current paths, modem burst-current budget, decoupling/return-path placement, RF impedance/keep-outs, manufacturing rules, schematic/BOM correctness, and firmware have not been signed off.
- The earlier Q1 drain loop remains unchanged.

The edit intentionally completes a bounded control/ground batch without moving footprints, deleting existing tracks, altering power topology, or changing nets.
