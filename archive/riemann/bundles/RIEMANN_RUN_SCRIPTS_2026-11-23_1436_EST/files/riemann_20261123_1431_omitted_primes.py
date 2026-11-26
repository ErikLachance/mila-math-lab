import math,json

def chi(p,d):
 if d==3: return 0 if p==3 else (1 if p%3==1 else -1)
 if d==4: return 0 if p==2 else (1 if p%4==1 else -1)

def finite(p,c,y):
 v=p;k=1;t=0.0
 while v<y:
  t+=(1-c**k)*math.log(p)*(1/v-1/y)
  if v>y//p:break
  v*=p;k+=1
 return t

def asymptotic(p,c):return math.log(p)*(1/(p-1)-c/(p-c))
results=[]
for d in (3,4):
 for p in (2,3,5,7,11,101):
  c=chi(p,d);infty=asymptotic(p,c)
  xs={str(y):finite(p,c,y) for y in (100,1000,1000000)}
  assert all(0<=v<=infty+1e-14 for v in xs.values()),(d,p,c,xs,infty)
  assert infty<=2*math.log(p)/(p-1)+1e-12
  results.append({'d':d,'p':p,'chi':c,'correction_limit':infty,'finite':xs,'crude_upper':2*math.log(p)/(p-1)})
print(json.dumps(results,indent=2))
open('/mnt/data/riemann_20261123_1431_omitted_primes.json','w').write(json.dumps(results,indent=2))
