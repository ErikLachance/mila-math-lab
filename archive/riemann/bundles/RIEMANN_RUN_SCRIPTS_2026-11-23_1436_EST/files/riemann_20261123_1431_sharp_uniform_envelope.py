import json, math
from sympy import primerange
out=[]
for Y in [10,30,100,1000,10000]:
 terms=[]
 for p in primerange(2,Y+1):
  v=p;k=1
  while v<=Y:
   if v<Y and p not in (2,7):
    terms.append((p,k,v,math.log(p)*(1/v-1/Y)))
   if v>Y//p:break
   v*=p;k+=1
 maximum=2*sum(coef for p,k,v,coef in terms if k%2==1)
 unweighted=sum(coef for p,k,v,coef in terms)
 # every odd-prime Legendre symbol choice +/- is achievable for a prime conductor > Y.
 out.append({'Y':Y,'source_odd_prime_exclusion_q':7,'minimum':0.0,'maximum':maximum,'unweighted_reference':unweighted,'ratio_max_to_unweighted':maximum/unweighted,'odd_power_terms':sum(k%2 for p,k,v,coef in terms),'even_power_terms':sum(k%2==0 for p,k,v,coef in terms)})
print(json.dumps(out,indent=2))
open('/mnt/data/riemann_20261123_1431_sharp_uniform_envelope.json','w').write(json.dumps(out,indent=2))
