exec(open('/mnt/data/riemann_20261123_1659/derivation_val.py').read().split('runs=[]')[0])
import json,time
p=7;f={3:1,1:-1};allr={}
for name,(a,b) in [('x',({1:1},{})),('y',({},{0:1}))]:
 out=[];fails=[];minmargin=100000
 for n in range(1,701):
  a,b=D(a,b,f)
  v=allcoeff_val(a,b,p)
  expected=n//7+n//343
  if v is not None:
   minmargin=min(minmargin,v-expected)
   if v<expected:fails.append((n,v,expected))
  if n in (7,14,49,98,300,342,343,344,350,490,686,700):out.append((n,v,expected))
 assert not fails,(name,fails[:10]);allr[name]={'samples':out,'minmargin':minmargin,'all700_pass':True}
 print(name,out,flush=True)
with open('/mnt/data/riemann_20261123_1659/j1728_higher.json','w') as g:json.dump(allr,g,indent=2)
