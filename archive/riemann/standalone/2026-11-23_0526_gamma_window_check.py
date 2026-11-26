#!/usr/bin/env python3
"""Independent Chernoff audit for Rubinstein Part II section 1 derivative localization."""
import math, json, time
from mpmath import mp
mp.dps=70
start=time.monotonic()
a=2.0
cases=[]
for U in [20,40,80,160,320,640]:
    j=round(1.25*a*U)
    k=j+1
    r_low=a*U/k;r_high=a*1.5*U/k
    assert r_low<1<r_high
    rate=lambda r:r-1-math.log(r)
    bound=math.exp(-k*rate(r_low))+math.exp(-k*rate(r_high))
    actual=float((mp.gammainc(k,0,a*U)+mp.gammainc(k,a*1.5*U,mp.inf))/mp.gamma(k))
    assert 0<actual<bound
    cases.append({'U':U,'j':j,'k':k,'relative_low':r_low,'relative_high':r_high,'actual_gamma_mass_outside':actual,'chernoff_bound_outside':bound})
# Bad j choice centers peak at left endpoint: demonstrates need to tune j not choose it arbitrarily.
U=160;j=round(a*U);k=j+1
bad=float((mp.gammainc(k,0,a*U)+mp.gammainc(k,a*1.5*U,mp.inf))/mp.gamma(k))
assert bad>0.4
rep={'source':'Rubinstein zeta v2 Part II section 1, screenshot p31 (Gamma kernel high derivatives)','rate_formula':'P(U outside [u,1.5u]) <= exp(-k*(r_low-1-ln r_low))+exp(-k*(r_high-1-ln r_high)), k=j+1, r_low=a*u/k, r_high=1.5*a*u/k, a=sigma-2','cases':cases,'wrong_j_equal_aU_tail_probability':bad,'elapsed_seconds':time.monotonic()-start,'scope':'rigorous elementary Chernoff inequalities; decimal evaluations are diagnostics, not a recheck of the whole RH proof'}
open(__file__.replace('.py','.json'),'w').write(json.dumps(rep,indent=2))
print(json.dumps(rep,indent=2))
