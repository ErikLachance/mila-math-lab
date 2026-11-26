import mpmath as mp, json, math
from fractions import Fraction
mp.mp.dps=75
beta=lambda s: (mp.zeta(s,mp.mpf(1)/4)-mp.zeta(s,mp.mpf(3)/4))/(4**s)
def chi20L(s):
    return beta(s)*(-mp.expm1(-s*mp.log(5)))
zeros=[]
for k in [-2,-1,0,1,2]:
    s=2j*mp.pi*k/mp.log(5)
    val=chi20L(s)
    zeros.append({'k':k,'s_real':mp.nstr(mp.re(s),9),'s_imag':mp.nstr(mp.im(s),18),'abs_L_chi20':mp.nstr(abs(val),12),'abs_beta':mp.nstr(abs(beta(s)),12)})
def divisors_sum(n):
    return sum(d+n//d if d*d!=n else d for d in range(1,math.isqrt(n)+1) if n%d==0)
cutoff=[]
for n in [1,2,12,5040,5041,5042,10080]:
    sig=divisors_sum(n);H=mp.harmonic(n)
    lag=H+mp.exp(H)*mp.log(H)
    data={'n':n,'sigma_n':sig,'lagarias_rhs':mp.nstr(lag,30),'lagarias_gap':mp.nstr(lag-sig,30)}
    if n>=2:
        rob=mp.e**mp.euler*n*mp.log(mp.log(n))
        data['robin_bound']=mp.nstr(rob,30);data['robin_gap']=mp.nstr(rob-sig,30)
    cutoff.append(data)
assert all(mp.mpf(d['abs_L_chi20'])<mp.mpf('1e-55') for d in zeros)
assert mp.mpf(cutoff[3]['robin_gap'])<0 and mp.mpf(cutoff[4]['robin_gap'])>0
assert mp.mpf(cutoff[0]['lagarias_gap'])==0
res={'imprimitive_boundary_euler_zeros':zeros,'robin_lagarias_cutoff_examples':cutoff,'conclusion':'Imprimitive Euler-factor zeros occur on Re(s)=0, not in 0<Re(s)<1. Robin strict bound fails at n=5040 but examples n>=5041 checked pass; Lagarias equality at n=1; finite checks NOT equivalent to universal RH proof.'}
with open('/mnt/data/riemann_20261123_1225/boundary_and_cutoff.json','w') as f:json.dump(res,f,indent=2)
print(json.dumps(res,indent=2))
