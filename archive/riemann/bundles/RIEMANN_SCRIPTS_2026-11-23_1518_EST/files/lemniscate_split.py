from fractions import Fraction
from sympy import primerange
import math,json
K=50
b=[Fraction(1)]
for k in range(1,K+1):
 r=k-1
 b.append(-Fraction(2,(4*k)*(4*k+1))*sum((b[i]*b[j]*b[r-i-j] for i in range(k) for j in range(k-i)),Fraction(0)))
A=[int(v*math.factorial(4*k+1)) for k,v in enumerate(b)]
def vp(z,p):
 c=0
 while z and z%p==0: z//=p;c+=1
 return c
fails=[];observed={'inert':0,'split':0}
for k in range(1,K+1):
 n=4*k+1
 for p in primerange(3,n+1):
  group='inert' if p%4==3 else 'split'
  observed[group]+=1
  val=vp(A[k],p); bound=n*p//(p*p-1)
  if val<bound: fails.append({'k':k,'n':n,'p':p,'group':group,'value':val,'naive_bound':bound})
print(json.dumps({'verified_exact_coefficient_prefix':A[:5], 'tested':observed,'fail_inert':sum(1 for x in fails if x['group']=='inert'),'fail_split':sum(1 for x in fails if x['group']=='split'),'first_split_failures':fails[:15]},indent=2))
with open('/mnt/data/riemann_run_20261123_1457/lemniscate_split.json','w') as f:json.dump({'tested':observed,'failures':fails},f,indent=2)
