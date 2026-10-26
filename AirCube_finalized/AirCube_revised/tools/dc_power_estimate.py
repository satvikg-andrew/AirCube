"""2D resistor mesh estimate of copper only, not a transient or fabrication sign-off.
Uses saved filled zones, tracks, pads and through vias. Via plating assumed 25 um.
Requires numpy, scipy, shapely. Run from project tools, optional mesh pitch mm.
"""
from parse_board import *
import numpy as np,shapely,scipy.sparse as sp
from scipy.sparse.linalg import spsolve
from scipy.sparse.csgraph import connected_components
from shapely.geometry import Point,LineString,Polygon,box
from shapely.affinity import rotate,translate
from shapely.ops import unary_union
import math,json,sys
pitch=float(sys.argv[1]) if len(sys.argv)>1 else .08
layers=['F.Cu','In1.Cu','In2.Cu','B.Cu'];rho=.00001724 # ohm mm at 20 C
thickness=[.035,.0152,.0152,.035];heights=[0,.1344,1.4146,1.549]
via_plating=.025
jobs=[('/USB_VBUS_RAW',[('J6','A4'),('J6','A9'),('J6','B4'),('J6','B9')],[('U8','1'),('U8','2')]),('+5VD',[('U8','7'),('U8','8')],[('U7','10'),('U7','11'),('U7','12')]),('+5VD',[('U8','7'),('U8','8')],[('U6','10'),('U6','11'),('U6','12')]),('/MODEM_VBAT',[('L1','1')],[('R28','1')]),('/MODEM_VBAT',[('L1','1')],[('R29','2')]),('/MODEM_VBAT_BB',[('R28','2')],[('U3','32'),('U3','33')]),('/MODEM_VBAT_RF',[('R29','1')],[('U3','52'),('U3','53')])]
ground_only='--ground' in sys.argv
if ground_only:
 modem_ground=[(p['ref'],p['num']) for p in pads if p['ref']=='U3' and p['net']=='GND']
 reg_ground=[('U7','6'),('U7','8'),('U7','15'),('U7','16'),('U7','17')]
 usb_ground=[('J6','A1'),('J6','A12'),('J6','B1'),('J6','B12')]
 jobs=[('GND',usb_ground,reg_ground),('GND',reg_ground,modem_ground)]
def padgeom(p):
 w,h=p['size'];g=Point(0,0).buffer(w/2) if p['shape']=='circle' else box(-w/2,-h/2,w/2,h/2)
 return translate(rotate(g,-p['angle'],origin=(0,0)),p['x'],p['y'])
def model(net):
 geoms={l:[] for l in layers}
 for z in all(b,'zone'):
  if val(z,'net')!=net:continue
  for f in all(z,'filled_polygon'):
   l=val(f,'layer',val(z,'layer'))
   if l in geoms:geoms[l].append(Polygon([list(map(float,q[1:])) for q in one(f,'pts')[1:]]).buffer(0))
 for t in all(b,'segment'):
  if val(t,'net')==net:geoms[val(t,'layer')].append(LineString([list(map(float,one(t,k)[1:])) for k in ['start','end']]).buffer(float(val(t,'width'))/2))
 vias=[]
 for v in all(b,'via'):
  if val(v,'net')!=net:continue
  xy=list(map(float,one(v,'at')[1:]));vias.append((xy,float(val(v,'size')),float(val(v,'drill'))))
  for l in layers:geoms[l].append(Point(xy).buffer(float(val(v,'size'))/2))
 for p in pads:
  if p['net']!=net:continue
  if p['raw'][2]=='thru_hole':vias.append(([p['x'],p['y']],min(p['size']),float(one(p['raw'],'drill')[1])))
  for l in layers:
   if l in p['layers'] or '*.Cu' in p['layers']:geoms[l].append(padgeom(p))
 gs=[unary_union(geoms[l]) for l in layers];bounds=unary_union(gs).bounds;x0=math.floor(bounds[0]/pitch)*pitch;y0=math.floor(bounds[1]/pitch)*pitch
 nx=math.ceil((bounds[2]-x0)/pitch)+1;ny=math.ceil((bounds[3]-y0)/pitch)+1
 xx,yy=np.meshgrid(x0+np.arange(nx)*pitch,y0+np.arange(ny)*pitch);points=shapely.points(xx,yy)
 ids=[];coords=[];n=0
 for l,g in enumerate(gs):
  mask=shapely.intersects(g,points);index=np.full((ny,nx),-1,dtype=np.int32);index[mask]=np.arange(n,n+mask.sum());coords.extend(zip(np.full(mask.sum(),l),xx[mask],yy[mask]));n+=mask.sum();ids.append(index)
 u=[];v=[];conductance=[]
 for l,index in enumerate(ids):
  for a,c in [(index[:,:-1],index[:,1:]),(index[:-1,:],index[1:,:])]:
   mask=(a>=0)&(c>=0);u.extend(a[mask]);v.extend(c[mask]);conductance.extend(np.full(mask.sum(),thickness[l]/rho))
 for xy,size,drill in vias:
  ix=round((xy[0]-x0)/pitch);iy=round((xy[1]-y0)/pitch)
  for l in range(3):
   a=ids[l][iy,ix];c=ids[l+1][iy,ix]
   if min(a,c)<0:continue
   resistance=rho*(heights[l+1]-heights[l])/(math.pi*drill*via_plating)
   u.append(a);v.append(c);conductance.append(1/resistance)
 u=np.array(u);v=np.array(v);g=np.array(conductance);rows=np.r_[u,v,u,v];cols=np.r_[u,v,v,u];data=np.r_[g,g,-g,-g];lap=sp.coo_matrix((data,(rows,cols)),shape=(n,n)).tocsr();labels=connected_components(lap,directed=False)[1]
 coords=np.array(coords)
 def contact(refs):
  out=[]
  for ref,num in refs:
   pp=[p for p in pads if p['ref']==ref and p['num']==num and p['net']==net]
   if not pp:raise ValueError((net,ref,num,'pad not found'))
   for p in pp:
    for l in range(4):
     if layers[l] not in p['layers'] and '*.Cu' not in p['layers']:continue
     mask=(coords[:,0]==l)&(np.abs(coords[:,1]-p['x'])<max(p['size']))&(np.abs(coords[:,2]-p['y'])<max(p['size']))
     cand=np.flatnonzero(mask);out.extend(cand[shapely.intersects(padgeom(p),shapely.points(coords[cand,1],coords[cand,2]))])
  return np.unique(out)
 return lap,labels,contact,n
results=[];cache={}
for net,src,dst in jobs:
 if net not in cache:cache[net]=model(net)
 lap,labels,contact,n=cache[net];a=contact(src);z=contact(dst);assert len(a) and len(z),(net,'no terminals')
 active=labels==labels[a[0]]
 if not (np.all(active[z]) and np.all(active[a])):
  raise RuntimeError((net,'Disconnected copper mesh: inspect geometry or reduce pitch'))
 fixed=np.r_[a,z];voltage=np.zeros(n);voltage[a]=1;free=np.flatnonzero(active);free=free[~np.isin(free,fixed)];rhs=-(lap[free]@voltage)
 voltage[free]=spsolve(lap[free][:,free],rhs);current=(lap@voltage)[a].sum();r=1/current
 result={'net':net,'from':src,'to':dst,'copper_resistance_milliohms':r*1000,'mesh_pitch_mm':pitch,'nodes':int(n)};results.append(result);print(json.dumps(result),flush=True)
print(json.dumps({'method':'2D resistor mesh, via plating assumed 25 um, room-temperature nominal copper; excludes component/contact/cable resistance and return path','results':results},indent=2))
(BASE.parent/'review'/(('dc-ground-' if ground_only else 'dc-copper-')+str(pitch)+'.json')).write_text(json.dumps(results,indent=2))
