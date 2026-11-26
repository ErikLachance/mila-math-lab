from fractions import Fraction
from sympy import primerange,isprime
import json,random

def chi(a,p):
 if a%p==0:return 0
 return 1 if pow(a%p,(p-1)//2,p)==1 else -1

q,d=11,1319
assert isprime(q) and isprime(d)
N=10000
# Exact formal equality per n, regardless Λ(n) or x; test n over 1..N.
counts={0:0,2:0,4:0}
factor_examples=[]
for n in range(1,N+1):
 a,b=chi(n,q),chi(n,d)
 c=(1+a)*(1-b)
 assert c==1+a-b-a*b
 counts[c]+=1
 if len(factor_examples)<25 and c==4 and isprime(n):factor_examples.append(n)

# Independent right-hand side coefficient values via Fourier character expansion, then
# finite weighted sum. Use rational weights before attaching real logarithmic Λ(n).
xs=[20,30,70,100,1319,4000,10000]
results=[]
for x in xs:
 lhs={};rhs={}
 for p in primerange(2,x+1):
  u=p
  while u<=x:
   w=Fraction(x,u)-1
   if w:
    lhs[p]=lhs.get(p,0)+w*(1+chi(u,q))*(1-chi(u,d))
    rhs[p]=rhs.get(p,0)+w*(1+chi(u,q)-chi(u,d)-chi(u,q)*chi(u,d))
   u*=p
 assert lhs==rhs
 result={'x':x,'nonzero_prime_coefficients':sum(1 for v in lhs.values() if v),'first_positive_prime_coefficients':list(p for p,v in lhs.items() if v)[:12]}
 results.append(result)

# Separate adversarial sign tests: chi_d(2)=1 and chi_d(p)=1 when p odd, p|(d+1).
for p in [2,3,5,11]:assert chi(p,d)==1
non_split=[p for p in primerange(2,100) if chi(p,d)==-1]
report={'toy_q':q,'toy_d':d,'qdivides_dplus1':(d+1)%q==0,'all_n_character_weight_counts':counts,'first_allows_weight4_prime_numbers':factor_examples,'rational_prime_power_weight_identity':results,'first_inert_primes_below_100':non_split,'tested_range':N,'scope':'finite algebraic sanity check, not RH'}
print(json.dumps(report,indent=2))
with open('/mnt/data/riemann_runs/20261123_1047/twist_identity.json','w') as f:json.dump(report,f,indent=2)
