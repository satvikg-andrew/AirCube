"""Preliminary closed-form screening, NOT a controlled-impedance sign-off.
Hammerstad-Jensen single microstrip, finite copper thickness. USB value is
relative width sensitivity calibrated to the supplied JLC calculator result.
Mask, etched trapezoid, local ground voids and pad/via discontinuities omitted.
"""
import math,json,pathlib
h=.0994;t=.035;er=4.1;gap=.127

def z_single(w):
 u=w/h;tn=t/h
 du1=tn/math.pi*math.log(1+4*math.e/tn*math.tanh(math.sqrt(6.517*u))**2)
 du=du1*(1+1/math.cosh(math.sqrt(er-1)))/2;u+=du
 a=1+math.log((u**4+(u/52)**2)/(u**4+.432))/49+math.log(1+(u/18.1)**3)/18.7
 bb=.564*((er-.9)/(er+3))**.053
 ee=(er+1)/2+(er-1)/2*(1+10/u)**(-a*bb)
 f=6+(2*math.pi-6)*math.exp(-(30.666/u)**.7528)
 return 376.730313668/(2*math.pi)*math.log(f/u+math.sqrt(1+(2/u)**2))/math.sqrt(ee)
anchor=.123444
r={'stackup':'JLC04161H-3313','outer_dielectric_mm':h,'copper_mm':t,'dielectric_constant':er,'usb_gap_mm':gap,'usb_actual_width_mm':.13,'jlc_screenshot_90ohm_width_mm':anchor,'width_difference_percent':100*(.13/anchor-1),'usb_calibrated_width_sensitivity_estimate_ohms':90*z_single(.13)/z_single(anchor),'rf_actual_width_mm':.17,'rf_unmasked_isolated_microstrip_screen_ohms':z_single(.17),'limitations':'Preliminary only. USB is a ratio calibrated to user-supplied JLC screenshot, not a coupled-line field solution. RF omits solder mask and coplanar copper. Fabricator must confirm both targets against actual finished construction.'}
p=pathlib.Path(__file__).resolve().parents[1]/'review/impedance-screen.json';p.write_text(json.dumps(r,indent=2));print(json.dumps(r,indent=2))
