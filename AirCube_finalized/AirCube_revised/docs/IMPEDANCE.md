# Impedance record and manufacturer request

Selected construction: JLC04161H-3313, nominal 1.6 mm ordering category, approximately 1.56 mm copper/dielectric construction, outer copper 0.035 mm, inner copper 0.0152 mm, outer-to-inner dielectric 0.0994 mm, core 1.265 mm. Nominal prepreg Dk 4.1. The supplied correct calculator screenshot is retained at `review/JLC3313-user-calculator.png`. Do not substitute the earlier 3313A screenshot/geometry.

| Circuit | Saved routing | Reference | Intended impedance |
|---|---|---|---|
| USB | 0.130 mm width, 0.127 mm nominal pair gap | In1 under F; In2 ground corridors under B | 90 ohm differential |
| LTE feed | 0.170 mm width on F | In1 GND | 50 ohm single-ended |

The supplied JLC calculator screenshot gives **4.86 mil = 0.123444 mm width**, with **5 mil = 0.127 mm spacing**, for 90 ohm USB on 3313. Actual 0.130 mm width is 5.31% wider. Width percentage is not impedance percentage. The screenshot's 0.5% field is a calculator setting; it is not evidence of a 0.5% production guarantee.

`tools/impedance_screen.py` records a preliminary width-sensitivity estimate: about **87.9 ohm USB**, calibrated to that 90-ohm screenshot result. It is not a coupled-line field solution. The isolated, unmasked Hammerstad-Jensen microstrip screen gives about **50.7 ohm for the 0.170 mm LTE feed**. Both are plausible screening results, but neither includes all finished-board effects. Solder mask, etch trapezoid, actual copper thickness, nearby coplanar copper, finite ground corridors, pads and vias matter. No claim of manufacturer approval is made and these estimates should not be used as coupon acceptance limits.

Routing widths were retained instead of making an unsupported impedance retune. Ask the fabricator to return the calculated impedances and tolerance for the saved geometry, or their required artwork adjustments, before production approval. If dimensions change, update the source, refill, rerun DRC/reference checks and regenerate every manufacturing output.

Suggested request to manufacturer (not sent):

> Please review this four-layer AirCube source and outputs using JLC04161H-3313. Confirm 90-ohm differential USB for 0.130 mm traces and nominal 0.127 mm gap on both outer layers, referencing the adjacent ground layer/corridors. Confirm 50-ohm LTE for the 0.170 mm F.Cu feed over In1 GND. Include your finished copper, prepreg thickness/Dk, mask and etch assumptions, required production tolerance, and any geometry changes. Please also approve the minimum drills/annular rings/clearances, outline slots and assembly orientations before we authorize manufacture.

Sources: [JLC controlled-impedance stackups](https://jlcpcb.com/impedance); supplied calculator screenshot; [Qucs microstrip model documentation](https://qucs.sourceforge.net/tech/node75.html). The screening script is an engineering estimate, separate from JLC's calculator.

## Corrected thickness metadata

The specified copper and dielectric layers sum to **1.5642 mm**. The existing KiCad solder-mask model adds **0.01524 mm per face**, giving **1.59468 mm** total in KiCad, rounded by the native Gerber job writer to **1.5947 mm**. The general thickness field has been corrected from 1.66 mm to that model total. The routing, copper thicknesses and dielectric dimensions were not changed. Order JLCPCB's **nominal 1.6 mm category with exact stackup JLC04161H-3313**; the CAD mask-inclusive value is not an alternate factory stackup. See manufacturing/ORDER_SPECIFICATION.md.
