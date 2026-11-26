import json
from split_controls import deriv
cases=[(7,{3:1,0:-1},'j0 split'),(13,{3:1,0:-1},'j0 split'),(5,{3:1,1:-1},'j1728 split'),(13,{3:1,1:-1},'j1728 split'),(5,{3:1,0:-1},'j0 inert'),(7,{3:1,1:-1},'j1728 inert')]
out=[]
for p,f,name in cases:
 A,B={1:1},{}
 records=[]
 for a in range(1,p*p+1):
  A,B=deriv(A,B,f,p)
  if a in [p,p*p]:
   records.append({'a':a,'A':A,'B':B,'nonzero':bool(A or B)})
 if 'split' in name:
  assert all(t['nonzero'] for t in records)
 else:
  assert not any(t['nonzero'] for t in records)
 out.append({'prime':p,'curve':name,'records':records})
print('cases=',len(out),'all assertions passed')
open('/mnt/data/riemann_20261123_1728/split_ordinary_pcurvature.json','w').write(json.dumps(out,indent=2))
