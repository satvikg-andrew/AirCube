# Fixed manufacturing and delivery specification

Project: AirCube NOSO take-home. The saved KiCad project and regenerated outputs in this ZIP are the design authority. This is a manufacturing-review package; factory impedance, sourcing and DFM acceptance remain outstanding.

## Manufacturer, construction and finish

- Manufacturer/assembly service: **JLCPCB / JLCPCB assembly**.
- Required stackup: **JLC04161H-3313**, four copper layers, **nominal 1.6 mm order category**. Do not substitute 3313A, 7628, another stackup, or another manufacturer without prior approval.
- Preserve the supplied 45.1 x 45.1 mm outline, internal isolation slots, mounting holes and component placement.
- Outer copper: nominal 0.035 mm per layer. Inner copper: 0.0152 mm per layer. Outer prepregs: 0.0994 mm each; core: 1.265 mm.
- Copper + dielectric sum: **1.5642 mm**. Existing CAD solder-mask model: 0.01524 mm on each face. KiCad total: **1.59468 mm including that mask model**. Native Gerber job rounds this to **1.5947 mm**. These describe one construction; they are not alternate thickness choices. The previous 1.66 mm scalar has been corrected. Order using the nominal 1.6 mm category and exact stackup code; do not adjust the core or prepregs to force a rounded category value.
- ENIG; green solder mask, white legend, both sides; lead-free assembly.
- Via tenting as exported. No resin filling/capping is specified; assembler must review exposed-pad vias and stencil apertures for solder wicking. Flag any process issue before production rather than changing the board.
- USB target 90 ohm differential: 0.130 mm tracks, nominal 0.127 mm pair gap, adjacent inner ground reference/corridors. LTE target 50 ohm: 0.170 mm F.Cu feed over In1 GND. Factory calculation/acceptance is required; do not silently change the artwork, stackup or reference arrangement.

## Assembly and delivery

**Deliver two identical, fully assembled PCBAs. Do not deliver a bare-board kit.** Populate both sides, including the through-hole headers/connectors requiring manual soldering, following the populated BOM and placement files. C38/C39 remain DNP. Board-only mounting holes, fiducials and logos are not purchased components.

Two assembled boards provide one development unit and one comparison/spare unit, avoiding a second fabrication cycle if an assembly fault or bring-up damage affects the first board. No extra bare boards are requested. If the service requires a larger minimum PCB fabrication lot, include that minimum cost in the quote and retain/recycle unused bare boards; only two assembled boards need shipping.

Required inspection: bare-board electrical test and assembled-board visual/AOI inspection, with hidden-joint inspection appropriate for the module/QFN packages. Check shorts, polarity and orientation. Firmware programming and complete functional testing will be performed during user bring-up; do not represent an unprogrammed PCBA as functionally validated.

The BOM contains generic entries as well as specified MPNs. Complete their purchasing codes using the existing packages and electrical requirements, and return the purchasing BOM before order placement. Preserve the selected MCU, BG95-M3 family, regulators, load switch and exact L1/L2/C18/C26/C33/C34/R28/R29 MPNs. No PCB redesign or component-footprint substitution is authorized by this document. Identify any sourcing/process conflict before placing the order.

## One shared off-board bring-up kit

One kit is sufficient for sequential testing of the two PCBAs:

- Sensirion SPS30, with a correctly pinned five-position 1.5 mm JST-ZH mating cable for J1.
- LTE U.FL antenna covering the selected BG95-M3/carrier bands.
- Separate 2.4 GHz U.FL antenna for ESP32-S3-WROOM-1U BLE.
- One compatible activated nano-SIM/data plan for LTE Cat-M1/NB-IoT at the test location.
- 5 V/3 A USB-C supply and suitable cable.
- 3.3 V UART programming/debug adapter and correctly wired modem USB-service adapter/cable.

The external sensor, antennas and SIM can move between the development and spare boards. The modem budget assumes LTE-only operation with EGPRS/2G disabled; firmware must enforce/read back this configuration before attachment. Respect USB-C source current advertisement.

## Files to use

- `Base/AirCube.kicad_pro`, `.kicad_sch`, `.kicad_pcb`: source.
- `manufacturing/gerbers/`: four copper, mask, paste, legend, outline, job.
- `manufacturing/drill/`: plated/non-plated Excellon, maps, report.
- `manufacturing/assembly/AirCube-BOM.csv` and `AirCube-placement.csv`: assembly data, mm.
- `review/final-native-drc.json`, `final-usb-reference.txt`, `schematic-erc.json`: checks.
- `docs/POWER.md`, `docs/IMPEDANCE.md`: engineering assumptions and outstanding factory checks.

Return a quote identifying PCB minimum lot cost, exactly two assembled PCBAs, components, the shared kit, inspection, shipping and lead times. Shipping address/phone will be supplied in the email. The quote and factory review are required before production release; the fixed construction is not permission to bypass a genuine manufacturing or electrical issue.
