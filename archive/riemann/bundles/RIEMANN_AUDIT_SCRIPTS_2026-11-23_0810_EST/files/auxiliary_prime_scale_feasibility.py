import math, json
import mpmath as mp
from pathlib import Path
from math import comb
mp.mp.dps=80
root=Path('/mnt/data/riemann_20261123_0751')

def sieve(n):
    a=bytearray(b'\x01')*(n+1);a[:2]=b'\x00\x00'
    for i in range(2,math.isqrt(n)+1):
        if a[i]:a[i*i::i]=b'\x00'*((n-i*i)//i+1)
    return [i for i in range(n+1) if a[i]]

P=sieve(2000)
prod=1
bounds_checked=0
last=1
for n in range(2,2001):
    if n in P: prod*=n
    m=(n+1)//2
    # For n=2m (resp 2m-1), all primes >m up to n divide binom(n,floor n/2)
    b=comb(n,n//2)
    ratio=math.prod(p for p in P if m<p<=n)
    assert b%ratio==0,(n,m,b,ratio)
    # Recurrence P(n)<=2^n * P(ceil(n/2)), via interval primes
    halfprod=math.prod(p for p in P if p<=m)
    assert prod <=2**n*halfprod
    # bound theta(n) <= (2n + ceil(log2(n))) log 2
    # compare integer primorial against 2^(2n+ceil(log2(n))) in exact integers
    upper=2**(2*n+(n-1).bit_length())
    assert prod <= upper
    bounds_checked+=1

# Conditions for mean-square theorem stage2 m0=16*M*q*P(z), log q<=z:
# log m0<=log(16M)+z+(2z+ceil(log2(z)))*log2
# for z>=20, ceil(log2(z))<=z/4, gives <=log(16M)+(1+9/4 log2)z <4z if fixed M and z large.
margin=4-(1+mp.mpf(9)/4*mp.log(2))
assert margin>0

def root_for_inequality(alpha, ln_ratio, log_W_factor):
    # solve alpha*W - log_W_factor*log(W) > ln_ratio on increasing large branch
    hi=(log_W_factor+1)/alpha
    while alpha*hi-log_W_factor*mp.log(hi)<=ln_ratio:hi*=2
    lo=hi/2
    for _ in range(320):
        mid=(lo+hi)/2
        if alpha*mid-log_W_factor*mp.log(mid)>ln_ratio:hi=mid
        else:lo=mid
    return hi

def root_for_q_greater_T(eps,K):
    # 0.5*exp(eps*W/5)>400*K*W; logarithmically: eps*W/5 - log W > log(800*K)
    alpha=eps/5; rhs=mp.log(800*K)
    lo=5/alpha
    # To avoid small-W branch, look only large W > 5/eps.
    while alpha*lo-mp.log(lo)<=rhs:lo*=2
    hi=lo
    lo=hi/2
    for i in range(320):
        mid=(hi+lo)/2
        if alpha*mid-mp.log(mid)>rhs:hi=mid
        else:lo=mid
    assert alpha*hi-mp.log(hi)>rhs or mp.almosteq(alpha*hi-mp.log(hi),rhs)
    return hi

cases=[]
for eps_str in ('.01','.005','.001'):
    eps=mp.mpf(eps_str)
    K=3
    W=root_for_q_greater_T(eps,K)
    # Stage-1 hypothesis with fixed example modulus M=1000: z >= (W^2/4) log(8M).
    W_stage1=root_for_inequality(eps/5,mp.log(mp.log(8000)/4),2)
    W_both=max(W,W_stage1)
    z=mp.exp(eps*W/5)
    # threshold for first-stage mean square modulus m0=8M fixed. For M=1000, log U=z>=W^2 log(8M)/4.
    mm=mp.mpf(1000)
    need=z/(W*W*mp.log(8*mm)/4)
    cases.append({'epsilon':eps_str,'K':K,'logY_at_q_greater_T_threshold':mp.nstr(W,27),'log10Y':mp.nstr(W/mp.log(10),27),'z_at_threshold':mp.nstr(z,27),'q_gt_T_inequality_ratio_at_threshold':mp.nstr(z/(800*K*W),12),'first_stage_mean_square_condition_ratio_for_M_1000':mp.nstr(need,15),'log10Y_stage1_threshold_M1000':mp.nstr(W_stage1/mp.log(10),24),'log10Y_both_suffices_in_example':mp.nstr(W_both/mp.log(10),24)})

# independent threshold for q>T and stage-1 m0 may be higher/lower; do not assert simultaneous at same W without proof.
out={'elementary_primorial_lemma':'For each integer N>=2, P(N)=prod_{prime p<=N} p <=2^N P(ceil(N/2)). Iterate to theta(N)<= (2N+ceil(log2N))ln2. This follows since each p in (ceil(N/2),N] divides binom(N,floor N/2), and binom<=2^N.','exact_integer_N_checked':bounds_checked,'stage2_bound':'log m0<=log(16 M)+z+(2z+ceil(log2 z))ln2 for q<=exp(z); for z>=20, <=log(16M)+(1+(9/4)ln2)z. Thus log m0<=4z eventually for fixed M, with positive coefficient margin.', 'coefficient_margin_4_minus_1_minus_9over4log2':mp.nstr(margin,40),'q_gt_T_large_branch_thresholds':cases,'limitations':'No proof that either prime q or d exists in the required short exponential interval/progression, no zero-density or uniform character bounds; estimates are elementary necessary feasibility, not sufficient. q>T thresholds may be astronomically large and do not on their own ensure all other hypotheses.'}
(root/'auxiliary_prime_scale_feasibility.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
