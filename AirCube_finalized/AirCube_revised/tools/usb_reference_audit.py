from parse_board import *
from shapely.geometry import Point,LineString,Polygon,box
from shapely.ops import unary_union
from shapely.affinity import rotate,translate
planes={l:unary_union([Polygon([tuple(map(float,p[1:])) for p in one(f,'pts')[1:]]).buffer(0) for z in all(b,'zone') if val(z,'net')=='GND' for f in all(z,'filled_polygon') if val(f,'layer',val(z,'layer'))==l]) for l in ['In1.Cu','In2.Cu']}
usb=sorted(set(val(x,'net') for x in all(b,'segment') if ('USB_D' in val(x,'net') or 'USB_DP' in val(x,'net') or 'USB_DM' in val(x,'net'))))
for net in usb:
 allowances=[]
 for v in all(b,'via'):
  if val(v,'net')==net:allowances.append(Point(list(map(float,one(v,'at')[1:]))).buffer(float(val(v,'size'))/2+.21))
 for p in pads:
  if p['net']!=net:continue
  w,h=p['size'];g=rotate(box(-w/2,-h/2,w/2,h/2),-p['angle'],origin=(0,0));allowances.append(translate(g,p['x'],p['y']).buffer(.21))
 allowed=unary_union(allowances);gaps=[];missingarea=0;total=0
 for x in all(b,'segment'):
  if val(x,'net')!=net:continue
  line=LineString([list(map(float,one(x,k)[1:])) for k in ['start','end']]);ref='In1.Cu' if val(x,'layer')=='F.Cu' else 'In2.Cu';g=line.buffer(float(val(x,'width'))/2);diff=g.difference(planes[ref]).difference(allowed);missingarea+=diff.area;total+=line.length
  if diff.area>.0001:gaps.append((round(diff.area,4),one(x,'start')[1:],one(x,'end')[1:]))
 print(net,'len',round(total,3),'unexplained area',round(missingarea,5),'gaps',gaps[:5])
