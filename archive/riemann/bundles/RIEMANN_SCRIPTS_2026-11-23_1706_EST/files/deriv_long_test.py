exec(open('/mnt/data/riemann_20261123_1659/derivation_val.py').read().split('runs=[]')[0])
import json
f={3:1,0:-1};p=5
allr={}
for name,(a,b) in [('x',({1:1},{})),('y',({},{0:1}))]:
 out=[]
 for n in range(1,251):
  a,b=D(a,b,f)
  if n%5==0:
   v=allcoeff_val(a,b,p);out.append((n,v,n//p))
  if n%50==0:print(name,n,'maxdegree',max(list(a)+list(b),default=0),flush=True)
 allr[name]=out
print(json.dumps({k:v for k,v in allr.items()},indent=2))
with open('/mnt/data/riemann_20261123_1659/deriv_long.json','w') as s:json.dump(allr,s)
