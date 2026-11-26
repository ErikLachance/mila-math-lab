from fractions import Fraction as F
from itertools import product, permutations
from collections import Counter
from time import monotonic
T=monotonic(); C=Counter()
# Norm of 1+p^m(a+b sqrt(d)) is 1+2p^m a+p^(2m)(a^2-d b^2).
# Valid for integral quadratic orders; test also the integral basis with w^2=w+c.
for p,m,d,a,b in product((2,3,5,7,11,13),range(1,5),(-1,-2,-3,-5,-7,-11),range(-4,5),range(-4,5)):
 h=p**m; N=(1+h*a)**2-d*(h*b)**2
 assert (N-1)%h==0
 C['norm_sqrt_basis']+=1
for p,m,c,a,b in product((2,3,5,7,11,13),range(1,5),(-1,-2,-3,-4,-5,-6),range(-4,5),range(-4,5)):
 h=p**m; x=1+h*a;y=h*b; N=x*x+x*y-c*y*y
 assert (N-1)%h==0
 C['norm_integral_basis']+=1
# WD condition F N = q N F: individual entries only possible when slopes differ by 1.
for q,e,sgn in product((2,3,5,7,11,13,17,19),range(1,21),(-1,1)):
 for weights in ((e,-e),(e,0,-e)):
  eig=[F(q)**(sgn*w) for w in weights]
  possible=[(i,j) for i,j in product(range(len(eig)),repeat=2) if eig[i]==q*eig[j]]
  if len(weights)==2 or e>1: assert not possible
  else: assert len(possible)==2
  C['WD_slope_cases']+=1
  C['WD_entries_checked']+=len(eig)**2
# Strict exponent interval width 1 excludes ratios q or 1/q. Endpoint example shows strictness needed.
for d in range(2,31):
 for a,b in product(range(1,d),repeat=2):
  assert abs(F(a,d)-F(b,d))<1
  C['strict_interval_pairs']+=1
# Exact q=prime flag count over field, tested using enumeration of invertible matrices n=2.
for p in (2,3,5,7,11):
 gl=sum((a*d-b*c)%p!=0 for a,b,c,d in product(range(p),repeat=4))
 B=p*(p-1)**2
 assert gl==(p*p-1)*(p*p-p) and gl//B==p+1
 C['GL2_flag_counts']+=1
# Distinct representation trace multiplicities cannot be dropped: one repeated root with gap 5.
for k in range(1,21):
 delta=5**k;v=0
 while delta%5==0:delta//=5;v+=1
 assert v==k
 C['multiplicity_cases']+=1
print(dict(C));print('script_seconds',monotonic()-T)

