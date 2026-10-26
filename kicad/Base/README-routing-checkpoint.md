# AirCube routing checkpoint — incomplete; do not fabricate

This is an intermediate PCB, not the completed routing requested. Open Base/AirCube.kicad_pro and its PCB with KiCad 10.0.7 or compatible. The PCB has saved, refilled zones. Full native DRC reports are in review/.

## Verified results

- Uploaded PCB after native zone refill: 30 unconnected items (the old checkpoint note estimated 37).
- Returned PCB: 28 unconnected items, all still errors for a finished board.
- Other native DRC violations: 0, including warnings, with KiCad 10 libraries installed.
- Schematic-to-PCB parity issues: 0.
- All original footprints, placements, pad net assignments, tracks and vias are preserved. No schematic, project-rule, stackup or ground-plane definition changes were made. No DRC rules were relaxed or suppressed.

## Retained routing

- MCU_DEBUG_RX: ESP32 U1 pin 36 to debug header J4 pin 3. 0.1524 mm tracks, eight tented 0.508/0.254 mm through vias. The route is long (111.34 mm of surface trace) and should be optimized during the next layout revision; no signal-integrity sign-off is claimed.
- USB_D+: U1 pin 14 to R21 pin 1. A 2.3503 mm, 0.1524 mm-wide B.Cu connection, no vias. This is only a short local escape; the complete differential USB path remains unfinished and is not impedance-verified.

The attempted redundant-ground cleanup, RF relocation, USB D- candidates and other trial routes were reverted. They are not in this PCB.

## Remaining work

Power distribution, the modem RX connection, RF matching/feed routing, and the USB paths remain incomplete. The current placement and existing copper block several straightforward escape paths. Finishing these requires local placement/routing revisions plus review of modem burst-current delivery, RF return paths and USB pair geometry. A clean main DRC section does not establish these electrical properties.

The schematic ERC has not been signed off. Hardware operation, modem current transients, RF performance and firmware behavior have not been tested by this routing work. No fabrication outputs, BOM or assembly files in this package should be inferred; none are provided.

## Unconnected items by net

- +5VD: 4
- /LTE_RF_ANT: 2
- /LTE_RF_MODEM: 2
- /MCU_USB_DM_CONN: 3
- /MCU_USB_DP_CONN: 3
- /MODEM_RX_3V3: 1
- /MODEM_USB_DM_HOST: 2
- /MODEM_USB_DP_HOST: 2
- /MODEM_USB_VBUS: 1
- /MODEM_VBAT: 2
- /USB_D-: 1
- /USB_VBUS_RAW: 2
- Net-(U3-USB_DM): 1
- Net-(U3-USB_DP): 1
- Net-(U3-VBUS): 1

These counts are KiCad missing-connection reports, not counts of all individual disconnected pads. Resolve all of them and complete electrical/assembly review before ordering.
