"""Source size asymptotic guard. x=exp(t), 0<eps<1/52.
D1: log d <= x^(eps/5)*(log x)^2.
Source: y >= X' = exp(x^(eps/3)); thus log y >= x^(eps/3).
Ratio x^(eps/3)/(x^(eps/5)*(log x)^2) = exp(2eps*t/15)/t^2 -> infinity.
Consequently log(y/d) >= exp(eps*t/3) - exp(eps*t/5)*t^2 -> infinity.
"""
import math,json
r=[]
for e in [0.005,0.01,0.018]:
    t=1000.0
    while 2*e*t/15-2*math.log(t)<1.0:
        t*=2
    assert e<1/52
    # Work in log-scale; direct x=exp(t) would overflow.
    logratio=(2*e*t/15)-2*math.log(t)
    assert logratio>1
    r.append({'epsilon':e,'log_x':t,'log_of_ratio_of_exponents':logratio,'ratio':math.exp(logratio)})
print(r)
with open('/mnt/data/riemann_20261123_1446_conductor_size_comparison.json','w') as f:json.dump({'analytic_limit':'exp(2eps*t/15)/t^2 -> infinity for fixed eps>0','sample_checks':r},f,indent=2)
