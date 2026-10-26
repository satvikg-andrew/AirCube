# AirCube — completed PCB routing

Open **AirCube.kicad_pro** with **KiCad 10.0.7 or compatible**. The saved PCB includes refilled copper zones.

## Verified results

The uploaded PCB had 28 missing connections. The returned PCB has:

- **0 unconnected items**;
- **0 reported DRC errors or warnings** under the unchanged project rules;
- **0 schematic-parity issues** and **0 footprint errors**;
- the same 119 footprints and unchanged pad numbers, net assignments, pad sizes and copper-layer assignments;
- byte-identical schematic and project settings.

The native reports are `review/DRC.json` and `review/DRC.rpt`. `review/change-verification.json` records the comparison and checksums. The four pre-existing ignored check categories are listed in the native report; no rules were relaxed and no new exclusions were added.

## Changes

Completed the remaining power, LTE RF, MCU USB, modem service USB and modem receive routing. Local revisions also reconnect the control, I2C, debug, shield and ground paths affected by the new routing. Redundant and dangling copper was removed.

R32 and R33, the modem USB zero-ohm links, were moved toward the modem by exchanging their positions with the R9/R10 I2C pull-ups. Their pad-net assignments are unchanged. These four references are on B.Fab for assembly identification. All other footprint placements are preserved.

Power distribution includes 0.8 mm inner-layer 5 V links and a 0.6 mm 3.3 V replacement link. Short escapes and control branches use narrower copper where required. The original stack-up and ground-zone definitions are retained; both inner layers now also contain routed signals/power, with the ground copper refilled around them.

Added through-vias use 0.508 mm copper diameter / 0.254 mm drills and are tented on both sides. The manufacturing audit found **no added via drills intersecting SMD lands**. Existing exposed-pad thermal-hole structures remain as supplied.

## Electrical qualification still required

**This file is a completed routing deliverable for engineering review, not hardware test evidence or production sign-off.**

The LTE feed uses 0.17 mm F.Cu traces. New USB data routing uses outer-layer traces, with uncoupled sections and multiple layer transitions. Neither 50-ohm RF nor 90-ohm USB differential impedance has been certified by a field solver or the selected fabricator. USB skew, return paths and signal integrity still require review against the actual manufactured stack-up. DRC does not establish those properties.

Modem transmit-burst voltage sag, regulator ripple/temperature, sensor operation, cellular connectivity and USB operation require bench testing. The schematic was preserved and checked for PCB parity; this routing work is not an independent schematic electrical sign-off.

Have the required NOSO/fabricator design review include these items before ordering. Generate new fabrication outputs from this revision after that review; the older Gerbers in the uploaded archive were not reused.

## Repeat the native checks

```sh
kicad-cli pcb drc --refill-zones --schematic-parity --format json -o review/recheck.json AirCube.kicad_pcb
```

The preview images are native copper/silkscreen plots; the back image is mirrored to show the underside.

Reference design guidance: [Quectel BG95 hardware design](https://quectel.com/content/uploads/2024/02/Quectel_BG95_Series_Hardware_Design_V1.3-2.pdf) and [Espressif ESP32-S3 PCB layout guidance](https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32s3/pcb-layout-design.html).
