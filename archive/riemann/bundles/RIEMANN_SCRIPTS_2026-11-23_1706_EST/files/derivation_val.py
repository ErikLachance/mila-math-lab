import json

def deriv(a):return {i-1:i*c for i,c in a.items() if i and c}
def pmul(a,b):
 o={}
 for i,c in a.items():
  for j,v in b.items():o[i+j]=o.get(i+j,0)+c*v
 return {i:c for i,c in o.items() if c}
def add(a,b):
 o=a.copy()
 for i,c in b.items():o[i]=o.get(i,0)+c
 return {i:c for i,c in o.items() if c}
def D(A,B,f):return add(pmul({0:2},pmul(f,deriv(B))),pmul(deriv(f),B)),pmul({0:2},deriv(A))
def valuation(v,p):
 if v==0:return None
 v=abs(v);k=0
 while v%p==0:v//=p;k+=1
 return k

def allcoeff_val(A,B,p):
 t=[valuation(v,p) for v in list(A.values())+list(B.values()) if v]
 return min(t) if t else None

runs=[]
for label,f,p in [('j0_inert5',{3:1,0:-1},5),('j0_split7',{3:1,0:-1},7),('j1728_inert7',{3:1,1:-1},7),('j1728_split5',{3:1,1:-1},5)]:
 for item,initial in [('x',({1:1},{})),('y',({},{0:1}))]:
  a,b=initial
  hist=[]
  for n in range(1,81):
   a,b=D(a,b,f);v=allcoeff_val(a,b,p)
   hist.append({'n':n,'valuation':v,'guarantee':n//p if 'inert' in label else 0})
   if 'inert' in label:assert v is None or v>=n//p,(label,item,n,v)
  runs.append({'curve':label,'element':item,'selected': [h for h in hist if h['n']%p==0 or h['n'] in (p*p-1,p*p,p*p+1)],'all_pass':True,'maxval':max(h['valuation'] for h in hist if h['valuation'] is not None)})
print(json.dumps(runs,indent=2)[:9000])
with open('/mnt/data/riemann_20261123_1659/derivation_val.json','w') as h:json.dump(runs,h,indent=2)
