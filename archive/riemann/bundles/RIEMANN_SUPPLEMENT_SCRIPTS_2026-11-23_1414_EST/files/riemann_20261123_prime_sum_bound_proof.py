"""Exact-rational certificates of elementary constant inequalities in a proof of
 sum_{p<=x} log p/(p-1) <= log x + 67/20, given psi(x) <= (6/5)x.
The bound on psi is external: Isabelle AFP Chebyshev_Prime_Bounds (Eberl, 2024).
"""
import math, json
from fractions import Fraction as F
from pathlib import Path

def exp_lower(x, degree):
    return sum((x**k)/F(math.factorial(k)) for k in range(degree+1))

# e^(9/5)>6; hence log(3+2 sqrt2)<9/5 since sqrt2<3/2
x=F(9,5); low=exp_lower(x,6)
assert low>6
# e^(7/10)>2; hence log2<7/10
low2=exp_lower(F(7,10),4)
assert low2>2
# d/dt sqrt(t)-log(t) changes from negative to positive at t=4;
# min value sqrt4 - log4 >0 since e^2 >4 (Taylor)
assert exp_lower(F(2),3)>4
# Sum f(n) <= f(2)+integral_2^infty f(t)dt <= log2/2+log(3+2sqrt2)
# < 7/20 + 9/5 = 43/20. Hence full sum <= log x +6/5+43/20 = log x+67/20.
assert F(7,20)+F(9,5)==F(43,20)
assert F(6,5)+F(43,20)==F(67,20)
assert F(67,20)<F(17,5)
# numerical sanity not a proof of the universal prime sum
N=300000
sieve=bytearray(b'\x01')*(N+1)
sieve[:2]=b'\x00\x00'
for p in range(2,int(N**0.5)+1):
    if sieve[p]:sieve[p*p:N+1:p]=b'\x00'*((N-p*p)//p+1)
prime_sum=0.0
maxdiff=(-1e20,0)
for p in range(2,N+1):
    if sieve[p]: prime_sum+=math.log(p)/(p-1)
    diff=prime_sum-math.log(p)
    if diff>maxdiff[0]:maxdiff=(diff,p)
# Note maxdiff sampled at every p not all x; between primes diff decreases.
assert maxdiff[0]<F(67,20)
res={"source":"https://isa-afp.org/entries/Chebyshev_Prime_Bounds.html", "exp_9_over_5_degree_6_lower":"%s"%low,"exp_7_over_10_degree_4_lower":"%s"%low2,"tail_constant_upper":"43/20", "psi_bound_constant":"6/5", "proved_additive_bound":"67/20", "quoted_source_bound":"17/5", "numerical_prime_check_up_to":N,"largest_sample_gap":maxdiff[0],"largest_sample_at_prime":maxdiff[1],"proof_status":"conditional on formally certified unconditional psi(x)<=1.2x; elementary steps rational except external psi theorem; not RH"}
out=Path('/mnt/data/riemann_20261123_prime_sum_bound_proof.json')
out.write_text(json.dumps(res,indent=2))
print(json.dumps(res,indent=2))
