from sympy import primerange,legendre_symbol,isprime
from sympy.ntheory.modular import crt
from math import log
import json

def build(Y,sign):
 ps=list(primerange(1,Y+1));mods=[8];res=[1 if sign==1 else 5]
 for p in ps:
  if p==2:continue
  a=next(a for a in range(1,p) if legendre_symbol(a,p)==sign)
  mods.append(p);res.append(a)
 a,Q=crt(mods,res);a=int(a);Q=int(Q)
 k=1
 while not isprime(a+k*Q): k+=1
 ell=a+k*Q
 assert ell%4==1
 assert all((pow(p,(ell-1)//2,ell)==1 if sign==1 else pow(p,(ell-1)//2,ell)==ell-1) for p in ps)
 S=0.0;individual=[]
 for p in ps:
  n=p;j=1
  while n<=Y:
   v=1-sign**j
   if n<Y and v: S+=v*log(p)*(1/n-1/Y)
   individual.append((p,j,n,v))
   n*=p;j+=1
 return {'Y':Y,'sign':sign,'ell':str(ell),'ell_digits':len(str(ell)),'progression':str(Q),'prime_count':len(ps),'signed_prime_power_sum':S,'positive_prime_powers':len([v for p,j,n,v in individual if v>0 and n<Y]),'neglected_even_power_count':len([v for p,j,n,v in individual if j%2==0])}

out=[build(Y,sign) for Y in [10,30,100] for sign in [1,-1]]
print(json.dumps(out,indent=2))
open('/mnt/data/riemann_20261123_1431_extreme_quadratic.json','w').write(json.dumps(out,indent=2))
