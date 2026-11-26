#!/usr/bin/env python3
"""Analytic bridge check: Dirichlet character mod 20 induced by primitive mod 4.
Illustrates nonzero finite Euler factors for Re(s)>0; not GRH proof.
"""
import mpmath as mp,json
from pathlib import Path
mp.mp.dps=75

def chi4(n):
    return 0 if n%2==0 else (1 if n%4==1 else -1)
def chi20(n):
    return 0 if n%5==0 else chi4(n)
def beta(s):
    return mp.power(4,-s)*(mp.zeta(s,mp.mpf(1)/4)-mp.zeta(s,mp.mpf(3)/4))
def L20(s):
    return mp.power(20,-s)*sum(chi20(a)*mp.zeta(s,mp.mpf(a)/20) for a in range(1,21))
res=[]
for s in [mp.mpc('0.65','1.25'),mp.mpc('1.75','-4'),mp.mpc('2','0'),mp.mpc('0','0'),mp.mpc('0','5.2')]:
    b=beta(s);factor=1-mp.power(5,-s);l=L20(s)
    err=abs(l-b*factor)
    assert err < mp.mpf('1e-62'),(s,err)
    res.append({'s':str(s),'beta_mod4':str(mp.nstr(b,30)),'euler_factor':str(mp.nstr(factor,30)),'L_mod20':str(mp.nstr(l,30)),'abs_error':str(mp.nstr(err,8))})
assert abs(L20(mp.mpf('0'))) < mp.mpf('1e-60')
# Elementary theorem: for sigma>0, |chi(p)*p^{-s}|<=p^{-sigma}<1.
# At sigma=0 there can be zeros: s=0 gives factor zero and a spurious imprimitive zero.
report={'formula':'L(s,chi20) = beta(s)*(1 - 5^{-s}); chi20 induced mod20 from primitive mod4','analytic_condition':'If Re(s)>0 then |5^{-s}|<1, so added Euler factor is nonzero. At s=0 the factor vanishes.','exact_character_table':[{'a':a,'chi4':chi4(a),'chi20':chi20(a)} for a in range(1,21)],'numerical_tests':res,'claim_scope':'Bridge for one explicit imprimitive character and general finite-factor inequality; not an RH or GRH proof.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(report,indent=2,ensure_ascii=False))
print(json.dumps(report,indent=2,ensure_ascii=False)[:4500])
