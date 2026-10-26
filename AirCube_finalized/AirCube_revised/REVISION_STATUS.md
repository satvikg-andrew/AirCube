# AirCube routing revision — review package complete

The revised KiCad source and manufacturing outputs are included. Read README_REVISIONS.md before ordering.

Final native KiCad 10.0.7 PCB DRC: **0 violations, 0 unconnected items, 0 schematic parity mismatches**. Full-width USB reference audit: no uncovered area after own-net pad/via transition exclusions.

Schematic ERC: **0 errors, 367 warnings** (235 standard symbol-library lookup warnings in this environment, 132 off-grid endpoints). These warnings have not been disabled or represented as resolved.

Remaining release decisions: manufacturer confirmation of 90-ohm USB and 50-ohm LTE on JLC04161H-3313; remaining generic BOM sourcing and assembly footprint/orientation approval. Hardware/firmware operation is not tested by this package. See docs/POWER.md and docs/IMPEDANCE.md.

The saved board is authoritative. Older checkpoint reports and route-plan JSON files are historical evidence, not the final manufacturing status.

## Ordering metadata correction

Fixed manufacturer: JLCPCB. Fixed stackup: JLC04161H-3313, nominal 1.6 mm order category. Copper/dielectric sum 1.5642 mm; including existing CAD solder mask, KiCad total 1.59468 mm. Regenerated native Gerber job reports 1.5947 mm. The old 1.66 mm value is removed from current source/job data. Green mask and white legend are explicit. DRC and USB audit rerun; routing and dielectric geometry unchanged.

Deliver two fully assembled PCBAs, with a single transferable off-board test kit. No extra bare boards requested. Details: manufacturing/ORDER_SPECIFICATION.md.
