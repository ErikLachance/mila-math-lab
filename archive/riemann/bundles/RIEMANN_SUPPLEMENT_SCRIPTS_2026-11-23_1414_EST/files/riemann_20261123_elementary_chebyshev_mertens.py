"""Self-contained elementary proof (written in accompanying checkpoint) of
sum_{prime p<=x} log p/(p-1) < log x + 63/20 (x>=2).
No prime number theorem, RH, or unverified numerical bound needed.
Exact rational finite exponential lower sums verify the only rational log comparisons.
"""
from fractions import Fraction as F
from math import factorial, log, isqrt
import json
from pathlib import Path

def expo_lower(t,N):return sum((t**k)/factorial(k) for k in range(N+1))
assert expo_lower(F(7,10),4)>2 # log2 < 7/10
assert expo_lower(F(11,10),5)>3 # log3 < 11/10
assert expo_lower(F(2,1),3)>4 # log4 <2
# For n>=2: psi(n)-psi(ceil(n/2)) <= log binomial(n,floor(n/2))
# from divisibility of n choose floor(n/2) by product of prime powers in the interval.
# Therefore, by induction psi(n)<=2n log2, even and odd cases.
# f(t)=log t/[t(t-1)] is decreasing t>=2. log t<=sqrt(t) on t>=4.
# Sum all integers f(n) for n>=2 < (2/3)log2+(7/6)log3.
log_bound = F(2,3)*F(7,10)+F(7,6)*F(11,10)
assert log_bound==F(7,4)
# Mertens splitting: F(x)=sum_{n<=x} Lambda(n)/n + tail.
# By log N!=sum_{m<=N}Lambda(m)floor(N/m),
# sum Lambda(n)/n <= log(N!)/N+psi(N)/N <= log N + 2log2.
# omitted p powers tail <=sum_{p>=2} logp/(p(p-1)) <=sum_{n>=2} f(n)< 7/4.
assert F(7,5)+F(7,4)==F(63,20)<F(17,5)
# Independent exhaustive finite spot check of the combinatorial recursion divisibility.
# Use integer v_p binomial and prime-power counts, no floats.
from math import comb
sampleN=250
for N in range(2,sampleN+1):
 m=(N+1)//2
 # Check product of prime powers r in (m,N] divides binomial(N,N//2).
 r=1
 for p in range(2,N+1):
  if any(p%d==0 for d in range(2,isqrt(p)+1)):continue
  k=p
  while k<=N:
   if k>m:r*=p
   k*=p
 assert comb(N,N//2)%r==0,(N,r,comb(N,N//2))
 # The binomial central bound for odd N is <=2^(N-1).
 if N%2:assert comb(N,N//2)<=2**(N-1)
 else:assert comb(N,N//2)<=2**N
r={'theorem':'For every real x>=2, sum_{p<=x} log(p)/(p-1) < log(x)+63/20, hence source log(x)+17/5',
'proof':'prime power divisibility of central binomial + induction psi(N)<=2N log2; factorial von Mangoldt identity; missing prime-power tail <(2/3)log2+(7/6)log3<7/4; rational exp lower bounds',
'exp_7over10_degree4':str(expo_lower(F(7,10),4)),
'exp_11over10_degree5':str(expo_lower(F(11,10),5)),
'exp_2_degree3':str(expo_lower(F(2,1),3)),
'sharper_constant':'63/20','original_constant':'17/5',
'integer_binomial_divisibility_cases_tested':sampleN-1,
'mathematical_status':'unconditional elementary argument; finite tests are regression, not proof of all N',
'riemann_status':'does not prove or disprove RH/GRH'}
Path('/mnt/data/riemann_20261123_elementary_chebyshev_mertens.json').write_text(json.dumps(r,indent=2))
print(json.dumps(r,indent=2))
