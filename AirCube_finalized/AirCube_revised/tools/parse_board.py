import re,json,math,collections
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]/'Base'
def parse(p):
 t=re.findall(r'"(?:\\.|[^"\\])*"|[^\s()]+|[()]',Path(p).read_text());root=[];stack=[root]
 for x in t:
  if x=='(':a=[];stack[-1].append(a);stack.append(a)
  elif x==')':stack.pop()
  else:stack[-1].append(json.loads(x) if x.startswith('"') else x)
 return root[0]
def all(n,k):return [v for v in n if isinstance(v,list) and v and v[0]==k]
def one(n,k,d=None):return next(iter(all(n,k)),d or [k])
def val(n,k,d=''):return one(n,k,[k,d])[1]
def props(n):return {p[1]:p[2] for p in all(n,'property')}
def tf(f,xy):
 at=list(map(float,one(f,'at')[1:]));a=math.radians(at[2] if len(at)>2 else 0);x,y=map(float,xy[:2]);return at[0]+x*math.cos(a)+y*math.sin(a),at[1]-x*math.sin(a)+y*math.cos(a)
b=parse(BASE/'AirCube.kicad_pcb');s=parse(BASE/'AirCube.kicad_sch');fps=all(b,'footprint');pads=[]
for f in fps:
 for p in all(f,'pad'):
  x,y=tf(f,one(p,'at')[1:]);pa=one(p,'at');pads.append(dict(ref=props(f).get('Reference'),num=p[1],x=x,y=y,size=list(map(float,one(p,'size')[1:])),angle=float(pa[3]) if len(pa)>3 else 0,net=val(p,'net'),layers=one(p,'layers')[1:],shape=p[3],raw=p))
if __name__=='__main__':
 print('COUNTS',collections.Counter(n[0] for n in b if isinstance(n,list)))
 for f in fps:
  r=props(f).get('Reference');print(r,props(f).get('Value'),one(f,'at')[1:],val(f,'layer'),f[1])
 print('NET WIDTHS')
 for net in sorted(set(val(x,'net') for x in all(b,'segment'))):
  if 'USB' not in net and net not in ['+5VD','/MODEM_VBAT','/MODEM_VBAT_RF']:continue
  ls=collections.defaultdict(float)
  for x in all(b,'segment'):
   if val(x,'net')==net:ls[(val(x,'width'),val(x,'layer'))]+=math.dist(*[list(map(float,one(x,k)[1:])) for k in ['start','end']])
  vs=[v for v in all(b,'via') if val(v,'net')==net];print(net,dict(ls),'VIAS',len(vs))
