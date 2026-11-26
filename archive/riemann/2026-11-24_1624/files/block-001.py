from fractions import Fraction as F
from itertools import product
from collections import Counter
from time import monotonic
from math import gcd
T=monotonic(); C=Counter()
# Strict width and product=1, use q=b^(3m), x_j=k_j/(3m).
for b,m in product(range(2,9),range(1,13)):
 d=3*m; q=b**d; upper=F(b**(2*m))+2*F(b)**(-m)
 other=2*F(b**m)+F(b)**(-2*m)
 assert upper>=other
 powers={k:F(b)**k for k in range(-2*m,2*m+1)}
 for i,j in product(range(-2*m,2*m+1),repeat=2):
  k=-i-j
  if k not in powers or max(i,j,k)-min(i,j,k)>d: continue
  assert powers[i]+powers[j]+powers[k]<=upper
  C['width_polytope_exact']+=1
 # Lower target bound valid even with arbitrary complex phases.
 assert upper < q-1-F(1,q)
 C['integer_cube_separation']+=1
# q^(1/3)>7/4 for q>=7; rational inequality gives upper < reverse triangle.
for q in range(7,10001):
 assert q*4**3>7**3
 assert F(4*q+8,7)<q-1-F(1,q)
 C['all_q_rational_bound']+=1
# Previously assumed symmetric exponent box is not implied by width 1 and determinant 1.
a=(F(1024),F(1,32),F(1,32)); q=2**16
assert a[0]*a[1]*a[2]==1 and a[0]/a[1]<q
assert sum(a)>256+1+F(1,256)
C['prior_box_counterexample']+=1
# Hodge to highest weight, two embeddings, exact Weyl dimension.
for e in range(1,101):
 J=(e+1,1,1-e); lam=tuple(J[i]-(2-i) for i in range(3))
 assert lam==(e-1,0,1-e)
 a,b,c=lam; D=(a-b+1)*(a-c+2)*(b-c+1)//2
 assert D==e**3
 C['exact_weight_and_dimension']+=1
# Count GL3 over prime residue rings from formula, not direct enumeration.
for p,f,n in product((2,3,5,7,11,13),(1,2),range(1,9)):
 Q=p**f
 gl=Q**(9*(n-1))*(Q**3-1)*(Q**3-Q)*(Q**3-Q**2)
 assert gl<=Q**(9*n)
 C['level_index_cases']+=1
# Separate growth exponents: N^18 (e+1)^7 <= [N(e+1)]^18.
for N,e in product(range(1,101),repeat=2):
 assert N**18*(e+1)**7 <= (N*(e+1))**18
 assert N**8*(e+1)**2 <= (N*(e+1))**18
 C['combined_exponent_bounds']+=1
print(dict(C)); print('script_seconds',monotonic()-T)

