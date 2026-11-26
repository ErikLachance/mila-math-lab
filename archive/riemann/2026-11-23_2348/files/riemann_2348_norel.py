from itertools import product, combinations
from collections import defaultdict
from math import gcd, isqrt
from fractions import Fraction as F
import time,json
start=time.monotonic()
# A sorted triple a<b<c has a primitive relation with some anchor and |i|,|j|<=L iff
# the two adjacent gaps after division by their gcd are each <=L (anchor middle).
# Endpoint anchor can only impose the stronger sum<=L.
def bad(a,b,c,L):
    u,v=b-a,c-b; g=gcd(u,v)
    return max(u//g,v//g)<=L
checks=0; small_base_counter=None; triples=0; density_checks=0
for S in range(2,5):
 for d in range(2,7):
  layers=defaultdict(list)
  for v in product(range(d),repeat=S): layers[sum(x*x for x in v)].append(v)
  assert sum(map(len,layers.values()))==d**S
  assert max(map(len,layers.values()))*(S*(d-1)**2+1)>=d**S
  # exact Chebyshev test with population variance and radius 2 sigma, avoid square roots
  mean=F(S*sum(i*i for i in range(d)),d)
  var=S*(F(sum(i**4 for i in range(d)),d)-F(sum(i*i for i in range(d)),d)**2)
  central=[(k,v) for k,v in layers.items() if (k-mean)**2<=4*var]
  assert sum(len(v) for k,v in central)*4>=3*d**S
  density_checks+=1
  for L in range(1,6):
   B=max(d, (2*L-1)*(d-1)+1) if L>=2 else 2*(d-1)+1
   # L=1 primitive coefficients may be opposite and sum 2, hence separate base.
   for k,vecs in layers.items():
    vals=sorted(sum(x*B**i for i,x in enumerate(v)) for v in vecs)
    assert len(set(vals))==len(vecs)
    for a,b,c in combinations(vals,3):
     assert not bad(a,b,c,L),(S,d,L,B,k,a,b,c)
     triples+=1
    if small_base_counter is None:
     xs=sorted(sum(x*d**i for i,x in enumerate(v)) for v in vecs)
     for a,b,c in combinations(xs,3):
      if bad(a,b,c,L): small_base_counter=[S,d,L,k,a,b,c];break
    checks+=1
# Independently brute-force all anchor/coefficient choices in small interval.
anchor_checks=0
for L in range(1,7):
 for a,b,c in combinations(range(18),3):
  vals=(a,b,c); brute=False
  for x,y,z in [(a,b,c),(b,a,c),(c,a,b)]:
   for i in range(-L,L+1):
    for j in range(-L,L+1):
     if i and j and i!=j and j*(y-x)==i*(z-x): brute=True
  assert brute==bad(a,b,c,L)
  anchor_checks+=1
print(json.dumps(dict(shell_checks=checks,triple_checks=triples,central_mass_checks=density_checks,anchor_checks=anchor_checks,small_base_counter=small_base_counter,runtime_seconds=time.monotonic()-start),indent=2))

