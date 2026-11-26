from itertools import product
from collections import Counter
from random import Random
from time import monotonic
T=monotonic(); C=Counter(); rng=Random(20261124)
def mm(A,B,q):return [[sum(A[i][k]*B[k][j] for k in range(3))%q for j in range(3)] for i in range(3)]
def tr(A):return sum(A[i][i] for i in range(3))
def det(A):
 a,b,c=A[0];d,e,f=A[1];g,h,i=A[2]
 return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)
for p in (5,7,11,13):
 for n in (1,2,3):
  q=p**n
  for _ in range(100):
   A=[[rng.randrange(q) for j in range(3)] for i in range(3)]
   t1=tr(A); A2=mm(A,A,q);t2=tr(A2);t3=tr(mm(A2,A,q))
   c2=sum(A[i][i]*A[j][j]-A[i][j]*A[j][i] for i in range(3) for j in range(i+1,3))
   assert (t1*t1-t2-2*c2)%q==0
   assert (t1**3-3*t1*t2+2*t3-6*det(A))%q==0
   C['newton_matrices']+=1
# Raw integral tangents of O[x]/(x^m,p^a*x^b) at x=0 into O/p^n.
# Horizontal saturation eliminates x^b. Compare raw and saturated derivation counts.
for p,n,m,a,b in product((2,3,5,7),range(1,5),range(2,5),range(1,5),range(1,5)):
 if b>=m:continue
 q=p**n
 raw=sum(1 for z in range(q) if b>1 or p**a*z%q==0)
 sat=sum(1 for z in range(q) if b>1 or z==0)
 assert raw==(q if b>1 else p**min(a,n))
 assert sat==(q if b>1 else 1)
 if raw!=sat:C['torsion_sensitive_tangent_cases']+=1
 C['tangent_count_cases']+=1
# Orbit slicing counts over algebraic closure: nonzero weights subset; normalization
# by selected negative weight. Stabilizer order gcd of support; over roots of unity
# represent roots by exact modular exponents (not finite-field point counting).
from math import gcd
weights=(-2,-1,1,2)
for bits in product((0,1),repeat=4):
 w=[d for d,b in zip(weights,bits) if b]
 if not any(d<0 for d in w) or not any(d>0 for d in w):continue
 for k in [abs(d) for d in w if d<0]:
  signatures={tuple((j*d)%k for d in w) for j in range(k)}
  g=0
  for d in w:g=gcd(g,abs(d))
  assert len(signatures)==k//g<=2
  C['slice_support_cases']+=1
# Small characteristic trace-to-charpoly obstruction (all positive power traces zero).
for p in (2,3):
 A=[[int(i==j and i<p) for j in range(3)] for i in range(3)]
 for j in range(1,10):assert tr(A)%p==0 # idempotent
 c2=sum(A[i][i]*A[j][j]-A[i][j]*A[j][i] for i in range(3) for j in range(i+1,3))
 assert (c2%p!=0 if p==2 else det(A)%p!=0)
 C['small_char_counterexamples']+=1
print(dict(C));print('script_seconds',monotonic()-T)
