#!/usr/bin/env python3
"""Independent analytic-class-number / gamma sum evaluation of L'/L(1,chi_1319).
Uses functional equation of real primitive odd quadratic character and Hurwitz zeta at zero.
No dependence on RH or the paper's numeric quoted constant."""
import json
from mpmath import mp
from sympy import legendre_symbol
from pathlib import Path
mp.dps=60
d=1319
chis=[int(legendre_symbol(a,d)) for a in range(1,d)]
assert sum(chis)==0
assert int(legendre_symbol(d-1,d))==-1
sum_weighted_a=sum((a*chi for a,chi in enumerate(chis,1)))
L0=mp.mpf(-sum_weighted_a)/d
assert L0>0 and int(L0)==L0
Z=mp.fsum(mp.mpf(chis[a-1])*mp.loggamma(mp.mpf(a)/d) for a in range(1,d) if chis[a-1])
r1=mp.euler+mp.log(2*mp.pi)-Z/L0
paper=mp.mpf('-1.520227887516')
assert abs(r1-paper)<mp.mpf('1e-11')
# Conjugate pair reflection loggamma(a/d)-loggamma(1-a/d) -> exploiting chi(-1)=-1
Zpair=mp.fsum(mp.loggamma(mp.mpf(a)/d)-mp.loggamma(mp.mpf(d-a)/d) if chis[a-1]==1 else -mp.loggamma(mp.mpf(a)/d)+mp.loggamma(mp.mpf(d-a)/d) for a in range(1,(d+1)//2))
assert abs(Zpair-Z)<mp.mpf('1e-50')
res={'d':d,'chi_parity':'odd (-1)','L0_exact_integer':int(L0),'sum_a_chi':sum_weighted_a,'Lprime_over_L_at_1':mp.nstr(r1,55),'paper_12digit_value':str(paper),'difference_to_paper':mp.nstr(r1-paper,25),'analytical_formula':'For primitive real odd quadratic chi of conductor d and root number +1: Lprime(1)/L(1)=EulerGamma+log(2*pi)-[sum_{a=1}^{d-1}chi(a)logGamma(a/d)]/L(0,chi), L(0,chi)=-(1/d)sum_{a=1}^{d-1}a chi(a). Uses Hurwitz zeta at zero and functional equation, no RH.','independent_reflection_sum':'PAIRWISE CHECK PASS (60-digit loggamma)','status':'PASS','caveats':'d=1319 quadratic character Legendre modulo d, fundamental discriminant -d; finite gamma evaluations mpmath, formula analytically exact, high-precision numeric is not a Lean certificate'}
Path('/mnt/data/riemann_20261123_0908/dirichlet_logderivative_gamma.json').write_text(json.dumps(res,indent=2))
print(json.dumps(res,indent=2))
