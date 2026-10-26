# AirCube routing revision — read before ordering

This ZIP contains the revised KiCad 10 project in `Base/`, generated manufacturing files in `manufacturing/`, and the review evidence in `review/`. Open `Base/AirCube.kicad_pro`. The fixed manufacturer, construction, two-PCBA delivery requirement and shared test kit are specified in `manufacturing/ORDER_SPECIFICATION.md`.

**Status: ready for the manufacturer's design/assembly review, not an unconditional approval to fabricate.** The saved board passes native KiCad DRC with zero violations, zero unconnected items and zero schematic parity mismatches. Schematic ERC has zero errors, with the warnings detailed below. Hardware operation has not been tested.

## Changes actually made

- Completed `/MODEM_RX_3V3` between the level translator and MCU-side connection. Added a 0.1524 mm route, approximately 62.19 mm long, with four through vias; avoided the In2 power pours and protected USB reference corridors. This is a low-speed UART connection, not an impedance-controlled signal.
- Removed the reported dangling SDA branches, unused RTS branch/via, duplicate short RX segments and tiny RX stubs.
- Added a 0.508/0.254 mm output via at X56.85/Y77.90 beside U8's existing via, with short 0.3 mm connections to output pins 7/8.
- Added an explicit 0.4 mm +5VD bridge between the output-side and regulator-side copper, using F/B layers and two additional through vias. Route length is 35.39 mm. This makes the physical copper path independently continuous in the resistance mesh rather than relying on the logical net/zone result alone.
- Added small ground-reference patches on In1 near D9 and on In2 near the modem USB transition. The filled-copper audit now finds no uncovered trace area for all eight routed USB net sections after own-net pad/via transition exclusions. It does not exclude a different signal's clearance simply because it is near an ESD part.
- Trimmed acute pour tips with small, layer-specific copper-pour keepouts. These allow tracks, pads, vias and footprints; they only prevent pour refill at those tips. No DRC severity was relaxed for these changes.
- Added project-local footprint copies for portability. These were recovered from the supplied board, not independently requalified against every manufacturer's drawing. Refreshed J3 from that local copy; its pad coordinates and sizes were checked unchanged.
- Added exact power-part procurement fields to both schematic and PCB. Kept C38/C39 DNP. Generated the BOM, placement, four copper Gerbers and drill files from the revised source.

- Corrected the inconsistent overall thickness metadata to the sum of the existing stackup, including its solder-mask model; made green mask/white legend explicit; regenerated the manufacturing outputs. No routing or dielectric dimensions changed in this metadata correction. See `review/thickness-correction.json`.

## Before authorizing production

1. Send the source and outputs to NOSO/manufacturer for their requested review. Ask them to confirm **JLC04161H-3313**, 90 ohm differential USB and 50 ohm LTE against the actual finished copper, dielectric and solder mask. See `docs/IMPEDANCE.md`. An impedance-class name and a clean DRC are not an impedance guarantee.
2. Have assembly resolve the remaining generic BOM entries to exact purchasable parts and approve package orientation, polarities, paste and footprint compatibility. The eight power components now have exact MPNs; other blank MPN fields remain visible in the BOM. Check the board's small finished drills and clearances against the chosen service. Confirm the simulator/calculator tolerance is not being mistaken for the manufacturer's production tolerance.
3. Use the specified LTE-only supply assumptions and 5 V/3 A source/cable. Disable EGPRS/2G in firmware before network attachment. This ZIP contains the supplied hardware project; it does not add or validate the assignment's ESP-IDF firmware, HTTPS delivery, video or hardware logs.

## Files and validation

- `review/final-native-drc.json`: authoritative final PCB check; no exclusions were added. Existing ignored categories: missing courtyard, track endpoint centering, tuning profile geometry and symbol-footprint filter mismatch. Other enabled checks passed.
- `review/final-usb-reference.txt`: geometric filled-ground check, full trace width minus own-net transitions. Not a field solver, return-current simulation or USB eye test.
- `review/schematic-erc.json`: **zero errors, 367 warnings** in this environment: 235 standard symbol-library lookup warnings and 132 off-grid endpoints. The schematic retains its cached symbol definitions. Off-grid endpoints were not moved during this routing repair. A fresh ERC should also be run with the normal KiCad 10 symbol libraries installed.
- `docs/POWER.md`: estimated supply losses, current assumptions, capacitor checks and bench tests.
- `manufacturing/assembly/`: BOM and placement in millimetres. C38/C39 are excluded as DNP. Placement uses native KiCad coordinates/orientations; assembly must apply its normal bottom-side rotation convention.
- `manufacturing/gerbers/`: F, In1, In2, B copper, front/back mask, silk, paste, outline and job file.
- `manufacturing/drill/`: separate plated/non-plated Excellon files, maps and drill report.
- `review/plots/`: saved-board copper plots and independently parsed Gerber views. Some decorative fonts are unavailable here, but those texts are on Dwgs.User, not production silkscreen.
- `review/revision-manifest.json`: hashes tying the saved source, reports and manufacturing files to this package.

Older checkpoint reports are retained as history; use the **final** reports for this revision. Copper resistance/impedance scripts are estimates, not manufacturing acceptance tests. Do not reroute from archived intermediate plans; the saved KiCad board is the deliverable.
