# AirCube routing checkpoint 8 — JLCPCB planning configuration

Status: routing incomplete. Expected 74 -> 68 unconnected after native zone refill. No fabrication release or native KiCad DRC claim.

Open AirCube.kicad_pro, open the PCB, press B to refill zones, save, then run DRC with schematic parity enabled. Return the saved PCB and full DRC report before the next routing iteration. This package contains the project, unchanged schematic, and project-local custom libraries.

## Manufacturing decision
Target: JLCPCB, four-layer nominal 1.6 mm JLC04161H-3313, 1 oz outer / 0.5 oz nominal inner copper, ENIG. Both inner copper layers remain GND reference planes. No new inner-layer signal tracks.

The PCB physical stackup has been updated using the current published values: F.Cu 0.035 mm; 3313 prepreg 0.0994 mm; In1.Cu 0.0152 mm; core dielectric 1.265 mm; In2.Cu 0.0152 mm; 3313 prepreg 0.0994 mm; B.Cu 0.035 mm. Prepreg Dk 4.1, core Dk 4.6; soldermask Dk 3.8 and above-trace thickness 0.01524 mm are planning parameters. The retained dielectric loss tangent 0.02 is an estimate, not a verified material certificate. The exact finished stack and impedance model must be confirmed against the fabrication quote. Thickness is nominal, not a tolerance guarantee.

Reference: https://jlcpcb.com/impedance (current published stackups/parameters).

Targets for the pending controlled-impedance routing: LTE 50 ohm single-ended and USB 90 ohm differential. Neither route is claimed complete or impedance-verified in this checkpoint. Do not substitute generic 0.2 mm USB or LTE widths as a verified impedance design. Trace widths, pair spacing, mask and nearby copper must be included in the final calculation/fab review.

## Routing changes
- Added the MCU-to-level-shifter modem TX connection.
- Added the button's 3.3 V supply and USB modem VBUS protection-device link.
- Removed 22 B.Cu ground-loop segments around U11 that prevented signal escape.
- Replaced the loops with a shared short ground return through a 0.6 mm / 0.3 mm via. Geometric connectivity confirms U11 ground pins 3, 5, 10 and 11 all retain plane connectivity.
- Added U11's short connection to its local decoupling capacitor, its supply feed, and USB-C CC1.
- All existing footprints and original vias are unchanged. Existing tracks are unchanged except the 22 explicitly removed ground-loop segments. Saved zone-fill caches were cleared for mandatory native refill around new signal vias; zone definitions are unchanged.

## Rules and geometric checks
The supplied project specifies 0.1524 mm default clearance, 0.14986 mm global minimum clearance and 0.1524 mm minimum trace width. New routes use at least 0.1524 mm net clearance with routing margin. Existing wider clearances were not reduced by moving existing copper. Board-edge checking uses 0.25 mm; new drill-edge separation checking uses 0.25 mm. New through vias remain 0.6 mm diameter / 0.3 mm drill.

Geometric audit: no different-net copper overlaps, new clearance failures, rule-area violations, board-edge violations or new drill-spacing violations. Minimum new copper gap: 0.16077 mm. Minimum new drill-edge spacing: 0.26569 mm. These checks do not replace native DRC, ERC, schematic parity, assembly/DFM checks, current-budget verification or hardware testing.

## Before ordering
Complete all remaining connections and review power paths, decoupling placement, modem burst-current delivery, SIM protection, USB routing and RF return paths. Validate native DRC/ERC and regenerate BOM, placement and fab files from the final design. Old fab outputs are intentionally excluded from this working package.

JLCPCB is the target, subject to the final BOM stock/assembly quote and delivery estimate to Pittsburgh. Global sourcing can exceed the assignment timeline. Obtain NOSO review and payment arrangements for the complete production/shipping and sensor/modem/SIM requirements before placing an order. No order has been placed and no email has been sent.
