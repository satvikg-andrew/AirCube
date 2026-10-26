# Power path estimates and assembly choices

These are pre-fabrication estimates, not measured results. The board has not been powered or tested here.

## Power components

| References | Selected manufacturer part | Relevant checks |
|---|---|---|
| L1, L2 | Coilcraft XAL4020-222MEC | 2.2 uH, ±20%, 38.7 milliohm maximum DCR at 25 C; typical 5.6 A saturation at 30% inductance drop, 4 A at 20 C rise. Same XAL4020 footprint family. |
| C18, C26 | TDK C3225X7R1C226K250AC | 22 uF, 16 V, X7R, ±10%, 1210. DC-bias plot indicates only a few percent loss around 3.3–3.8 V. A conservative screening allowance of 5% bias loss plus tolerance and 15% temperature reduction gives about 16 uF. ESR is milliohm-scale around resonance; actual filter/transient performance still needs bench verification. |
| C33, C34 | KEMET T520B107M006ATE040 | 100 uF polymer tantalum, ±20%, 6.3 V, 40 milliohm ESR at 100 kHz/25 C, B/3528 case. Budget 80 uF minimum before application derating. The 3.792 V rail uses about 60% of rated voltage; check polarity. |
| R28, R29 | Vishay WFZ080500000ZE66 | 0805 metal-foil jumpers, maximum 0.5 milliohm. Selected to avoid an unspecified ordinary zero-ohm resistor becoming a supply bottleneck. This rating does not imply the PCB itself can carry the jumper's full published current. |

MPNs are recorded in the schematic, PCB and BOM. Assembly must confirm stock and footprints; do not substitute solely by nominal inductance/capacitance or “0 ohm”. C38/C39 remain DNP pending actual antenna matching measurements. Generic decouplers and other blank BOM MPNs still need procurement review, including effective capacitance at their operating bias.

U7 is TPS62130 with 374k/100k feedback: nominal Vout = 0.8 × (1 + 374/100) = **3.792 V**. U6 is fixed-output TPS62132. These are buck converters; their inductor DCR and switch losses are part of the regulated conversion stage. Do not subtract those losses from output voltage a second time as if the regulator had no feedback. They do consume input headroom and power.

## Copper resistance

`tools/dc_power_estimate.py` constructs a 2D sheet-resistor mesh of saved filled copper, tracks and pads, with plated via/through-hole links. It uses nominal 35 um outer/15.2 um inner copper at 20 C, copper resistivity 1.724e-5 ohm mm and **assumed 25 um hole plating**. Via lengths are approximate. It omits solder/contact resistance, exact corner/annular current distribution and component internals. Rectangular pad approximation and mesh discretization introduce error; it is not a guaranteed upper bound. A 0.508/0.254 mm via's whole-board barrel is about 1.35 milliohm at these assumptions.

| Positive path | Approximate resistance at 20 C |
|---|---:|
| J6 VBUS pads → U8 input pins 1/2 | 20.2 milliohm |
| U8 output pins 7/8 → U7 input pads | 38.9 milliohm |
| U8 output pins 7/8 → U6 input pads | 33.8 milliohm |
| L1 output → R28 input | 24.3 milliohm |
| L1 output → R29 input | 10.3 milliohm |
| R28 output → modem BB pads | 4.1 milliohm |
| R29 output → modem RF pads | 1.5 milliohm |

Raw mesh results for 0.03 and 0.06 mm pitches are in `review/dc-copper-*.json`; these positive-path estimates differ by roughly 3% or less. The 0.06 mm ground mesh estimates about 11.2 milliohm between USB ground and U7 grounds, and 1.45 milliohm between U7 ground and the modem's ground pads. Ground estimates have not been mesh-converged separately. Actual module internal ground distribution is not modelled.

### Example current and drop budget

Design operation is **LTE Cat-M1/NB-IoT only**. Reserve 1 A at 3.792 V for the modem supply as a conservative LTE allocation; also assess a 2 A transient as headroom, not as a claim of tested performance. At assumed 85% modem-converter efficiency and 4.5 V input, 1 A modem output needs about **0.99 A input**. Allowing 0.65 A on 3.3 V for the MCU/sensors/LED and 85% conversion, plus 0.10 A at 5 V for the SPS30/circuit overhead, gives about **1.65 A total at 4.5 V**. A 2 A modem-output scenario approaches **2.65 A**. Use a genuine **5 V/3 A supply and suitable cable**; do not assume an ordinary USB host port can supply this. USB-C advertised/negotiated current must be respected.

For a conservative common 5 V path estimate, combine 20.2 + 38.9 milliohm copper, about 11.2 milliohm ground return and **30 milliohm switch allowance**: approximately **100 milliohm** before cable/connector contacts. This allowance is deliberately above U8's 16 milliohm typical figure; its actual limits depend on bias/temperature. At 1.65 A that is about **0.17 V**; at 2.65 A about **0.27 V**. Hot copper, cable resistance and connector drop must be added. Check the actual voltage at both regulator inputs, especially under low-line and transmit loading.

For a deliberately pessimistic single-branch 1 A allocation, BB path copper + jumper + return is about **30.3 milliohm**, or **30 mV**; RF is about **13.7 milliohm**, or **14 mV**. The common output-plane portions are shared when both branches draw current, so do not apply independent one-branch numbers as an exact simultaneous-load solution. Copper resistance rises about 26% from 20 C to 85 C. Add modelling/contact margin. At 2 A, the BB static estimate is roughly 61 mV at 20 C, before temperature/margin.

Static resistance is only one part of burst droop. With 80 uF minimum local capacitance, an uncompensated 1 A step for 10 us gives about **0.125 V capacitive droop**, plus about **0.040 V ESR step** at the nominal specified ESR. This illustrates why regulator response and interconnect inductance must be scoped; 100 uF does not by itself guarantee millisecond burst support. Check hot/cold ESR and effective capacitance as part of assembly qualification.

## LTE-only configuration and bench acceptance

Before attachment, configure and read back the BG95-M3 LTE-only search mode, for example `AT+QCFG="nwscanmode",3` followed by `AT+QCFG="nwscanmode"`, following the exact modem firmware's Quectel manual and applying any required restart/effect setting. Confirm the returned mode is 3. **This hardware ZIP does not implement or prove that firmware configuration.** EGPRS/2G burst operation is not approved by this budget.

Bring up with current limiting, confirm rails and absence of shorts first, then connect the correct antennas before RF transmission. Scope directly across modem VBAT_BB/GND and VBAT_RF/GND at the module using a short ground spring. Exercise startup, attachment, poor-signal retries and repeated HTTPS uploads while the ESP32, LED and SPS30 are active. Log minimum rail voltages, current and reset causes. Confirm the exact module's operating limits (BG95-M3 supply minimum 3.3 V) with margin; also inspect regulator input sag, thermal behaviour and inductor current/saturation. Capture USB enumeration/service operation and sensor readings. Physical tests are required before claiming the assignment works.

## Off-board procurement

Include the Sensirion SPS30, a correctly wired **five-position 1.5 mm JST-ZH mating cable for J1**, an LTE 50-ohm U.FL antenna covering the selected carrier's bands, a separate 2.4 GHz U.FL antenna for ESP32-S3-WROOM-1U BLE, and an activated compatible nano-SIM/data plan. Verify SPS30 end connector and UART-mode selection against its datasheet; do not assume a same-size cable is pin-for-pin correct. Antenna part numbers must be selected for the actual enclosure/carrier; none is falsely marked as validated here. Include a 5 V/3 A supply/cable, UART adapter and appropriate modem service adapter in bring-up equipment.

Sources: [TI TPS62130](https://www.ti.com/lit/ds/symlink/tps62130.pdf), [TI TPS22975](https://www.ti.com/lit/ds/symlink/tps22975.pdf), [Coilcraft XAL4020-222](https://www.coilcraft.com/en-us/products/power/shielded-inductors/molded-inductor/xal/xal40xx/xal4020-222/), [TDK characterization](https://product.tdk.com/en/system/files/dam/doc/product/capacitor/ceramic/mlcc/charasheet/c3225x7r1c226k250ac.pdf), [KEMET specification](https://search.kemet.com/download/specsheet/T520B107M006ATE040), [Vishay WFZ](https://www.vishay.com/docs/30432/wfz-jumper.pdf), [Quectel BG95 hardware design](https://images.quectel.com/python/2023/04/Quectel_BG95_Series_Hardware_Design_V1.5.pdf), [Quectel network-search introduction](https://quectel.com/content/uploads/2024/02/Quectel_BG95BG77BG600L_Series_Network_Searching_Scheme_Introduction_V2.0-1.pdf).
