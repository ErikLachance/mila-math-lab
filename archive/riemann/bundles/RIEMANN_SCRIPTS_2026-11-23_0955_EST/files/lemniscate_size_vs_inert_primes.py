#!/usr/bin/env python3
"""Size obstruction: exact Hurwitz coefficients vs all inert-prime divisibilities."""
import runpy, math, json, contextlib, io
from sympy import primerange
with contextlib.redirect_stdout(io.StringIO()):
    base=runpy.run_path('/mnt/data/riemann_20261123_0936/lemniscate_ode_exact.py')
A=base['A'];vp=base['vp']; selected=[]
for n in [17,49,101,201,501,1001,2001]:
    an=A[n]
    lA=math.log(abs(an))
    all_p=list(primerange(2,n+1))
    inert=[p for p in all_p if p%4==3]
    actual_inert=sum(vp(an,p)*math.log(p) for p in inert)
    bound=sum((n*p//(p*p-1))*math.log(p) for p in inert)
    ratio=actual_inert/lA
    print(n,'log|A_n|',round(lA,8),'inert_actual',round(actual_inert,8),'ratio',round(ratio,6),'pred',round(bound,8))
    assert actual_inert<=lA+1e-8 and actual_inert>=bound-1e-8
    selected.append({'n':n,'log_abs_A':lA,'inert_prime_log_contribution_actual':actual_inert,'ratio_inert_to_total':ratio,'inert_prime_guaranteed_lower':bound,'inert_count':len(inert)})
with open('/mnt/data/riemann_20261123_0936/lemniscate_size_vs_inert_primes.json','w') as f:json.dump({'selected':selected,'status':'PASS','warning':'size comparison is a finite independent illustration of the factor-2 obstruction already stated in source; not RH proof'},f,indent=2)
print('PASS size-vs-divisibility cases')
