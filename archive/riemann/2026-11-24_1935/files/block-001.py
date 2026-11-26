from itertools import product
from collections import Counter
from math import comb
from time import monotonic
start=monotonic(); counts=Counter()
def comps(n,k):
 if k==1:
  yield (n,); return
 for i in range(n+1):
  for tail in comps(n-i,k-1):yield (i,)+tail
for n in range(1,7):
 for mult in comps(n,5):
  w=tuple(v for v,c in zip((-2,-1,0,1,2),mult) for _ in range(c))
  basis=[x for d in (1,2,3) for x in comps(d,n) if sum(a*b for a,b in zip(x,w))==0]
  minimal=[x for x in basis if not any(y!=x and all(a>=b for a,b in zip(x,y)) for y in basis)]
  d,b,z,a,c=mult
  assert len(minimal)==z+a*b+c*d+comb(a+1,2)*d+comb(b+1,2)*c
  counts['weight_configurations']+=1
  for degree in range(1,9):
   for x in comps(degree,n):
    if sum(i*j for i,j in zip(x,w)):continue
    assert any(all(i>=j for i,j in zip(x,y)) for y in minimal)
    counts['balanced_monomials']+=1
# Matrix entries are polynomials of degree <=1 for this finite subgroup.
# D^j (I+t(a E12+b E32)); multiplication is valid since N*N'=0.
for p in (5,7,11,13,17,19):
 for lam in range(2,p-1):
  order=next(i for i in range(1,p) if pow(lam,i,p)==1)
  for j,a,b in product(range(order),range(p),range(p)):
   di=(pow(lam,j,p),1,pow(lam,-j,p))
   # exact trace of finite-group element equals diagonal reduction
   assert (sum(di)%p)==(di[0]+1+di[2])%p
   # product of (1,2) and (3,2) has t^2 coefficient a*b
   if a*b%p:counts['nonconstant_balanced_products']+=1
   counts['finite_group_elements']+=1
  # verify all pairwise products of N matrices zero using actual matrix multiplication
  for a,b,c,d in product(range(p),repeat=4):
   N=((0,a,0),(0,0,0),(0,b,0)); M=((0,c,0),(0,0,0),(0,d,0))
   assert all(sum(N[i][k]*M[k][j] for k in range(3))%p==0 for i in range(3) for j in range(3))
   counts['nilpotent_products']+=1
  break # one lambda per p for exhaustive N products
# Inertia residual eigenvalue degeneracy on squares: order of u^e on squares.
for p in (5,7,11,13,17,19,23,29,31,37,41,43):
 for e in range(1,2*(p-1)):
  if 2*e%(p-1)==0:continue
  values={pow(u,2*e,p) for u in range(1,p)}
  separates=any(v not in (1,p-1) for v in values)
  assert separates==(4*e%(p-1)!=0)
  counts['inertia_cases']+=1
  if not separates:counts['square_subgroup_exceptions']+=1
print(dict(counts));print('script_seconds',monotonic()-start)
# Compare finite invariant subspace of homogeneous monomial quotients
# k[x,y,z]/((xy)^a,z^b), with weights +1,-1,0.
# Direct standard-monomial enumeration vs product bound.
for a,b in product(range(1,13),repeat=2):
 standard=[(i,j,k) for i,j,k in product(range(a+2),range(a+2),range(b+2)) if i==j and not(i>=a and j>=a) and k<b]
 assert len(standard)==a*b
 counts['monomial_quotient_cases']+=1
 assert max(i+j+k for i,j,k in standard)==2*(a-1)+b-1
print('extended',dict(counts));print('total_seconds',monotonic()-start)
# Exact translation inverse on polynomial coefficient rings with zero divisors.
from random import Random
rng=Random(1935)
for p,n,d in product((2,3,5,7),range(1,4),range(1,21)):
 q=p**n
 a=[rng.randrange(q) for i in range(d+1)]
 b=[sum(a[i]*comb(i,j) for i in range(j,d+1))%q for j in range(d+1)]
 c=[sum(b[i]*comb(i,j)*(-1)**(i-j) for i in range(j,d+1))%q for j in range(d+1)]
 assert c==a
 counts['formal_translation_tests']+=1
print('final',dict(counts));print('final_seconds',monotonic()-start)

