exec(open('/mnt/data/riemann_20261123_1659/derivation_val.py').read().split('runs=[]')[0])
import json
f={3:1,0:-1};p=5
all_records={};ok=True
for name,(a,b) in [('x',({1:1},{})),('y',({},{0:1}))]:
 records=[];lowest_margin=10000
 for n in range(1,351):
  a,b=D(a,b,f)
  v=allcoeff_val(a,b,p)
  target=n//5+n//125
  if v is not None:
   lowest_margin=min(lowest_margin,v-target)
   if v<target:
    ok=False
    print('FAIL',name,n,v,target,flush=True)
  if n in (5,7,25,50,100,120,124,125,126,150,200,250,275,300,325,350):records.append([n,v,target])
 all_records[name]={'selected':records,'all350_pass':ok,'min_margin':lowest_margin}
print(json.dumps(all_records,indent=2));assert ok
with open('/mnt/data/riemann_20261123_1659/higher_divisibility_regression.json','w') as fp:json.dump(all_records,fp,indent=2)
