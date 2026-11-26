#!/usr/bin/env python3
"""Exact toy p-adic valuations, gamma-window tail checks, asymptotic exponents."""
from fractions import Fraction
from math import comb, factorial, log, exp, sqrt
from scipy.stats import gamma
from scipy.optimize import minimize_scalar
import json

# Exact toy formal-group series: l(u)=u+u^(p^2)/p+u^(p^4)/p^2+...
# For a<=p^4 and a=1+(p^2-1)k, derive via Lagrange inversion.
def vp(n,p):
    assert n!=0
    n=abs(n); i=0
    while n%p==0:n//=p;i+=1
    return i

def coefficient_inverse(p,a):
    k=(a-1)//(p*p-1)
    if (a-1)%(p*p-1)!=0:return Fraction(0,1)
    if a<p**4:
        return Fraction((-1)**k*comb(a+k-1,k),a*p**k)
    if a==p**4:
        return Fraction((-1)**k*comb(a+k-1,k),a*p**k)-Fraction(1,p*p)
    raise ValueError('unsupported')

p_adic=[]
for p in [3,5,7]:
    lim=min(p**4,1+(p*p-1)*10)
    for k in range(1,11):
        a=1+k*(p*p-1)
        if a>lim:break
        coeff=coefficient_inverse(p,a)
        derivative=coeff*factorial(a)
        got=vp(derivative.numerator,p)-vp(derivative.denominator,p)
        fact_v=vp(factorial(a),p)
        naive_lower=fact_v-Fraction(a-1,p*p-1) # rational
        predicted=a*p/(p*p-1)
        p_adic.append({'p':p,'a':a,'coefficient':str(coeff) if a<=p**4 else '[large]', 'vp_derivative':got,'vp_factorial':fact_v,'naive_lower':str(naive_lower), 'target_ap/(p2-1)':round(predicted,6), 'gap_from_target':round(got-predicted,6)})

eta=max(0.8*exp(0.2),1.2*exp(-0.2));c0=log((1+eta)/(2*eta)); sigma=252
window=[]
for U in [1,2,5,10,20]:
    j=round(1.25*(sigma-2)*U)
    # gamma distribution of u^j exp[-(sigma-2)u] normalized
    shape=j+1;rate=sigma-2
    below=gamma.cdf(U,a=shape,scale=1/rate)
    above=gamma.sf(1.5*U,a=shape,scale=1/rate)
    tail=below+above
    window.append({'U':U,'j':j,'tail_probability':tail,'exp_minus_cj':exp(-0.008*j),'tail_over_exp_minus_cj':tail/exp(-0.008*j),'below':below,'above':above})

# independent elementary check for m-scaling; no premise about arithmetic proof
asymp=[]
for power in [1,2,3]:
    alpha=1/(power+1)
    exponent=power/(power+1)
    for x in [10**3,10**6]:
        m=x**alpha
        val=x/m + m**power
        asymp.append({'p':power,'x':x,'m_balance':m,'exponent':exponent,'value':val,'value_over_x_exponent':val/(x**exponent)})

result={
'eta':eta,'log_eta_cap':c0,'c0_is_greater_than_0.008':c0>0.008,
'ratio_at_sigma_252_theta0':252/(252-2),'exp_0.008':exp(0.008),
'window_checks':window,
'p_adic':p_adic,
'error_model_minimizers':asymp,
'notes':['Toy p-adic calculation uses inverse of formal log, not the entire higher-rank theta-lift machinery.', 'Gamma concentration supports only source’s analytic window localization, not arithmetic input M.', 'The stated one-sided window criterion uses positive part of G, so a two-sided Mellin bound is not interchangeable.'],
}
open('/mnt/data/riemann_runs/20261123_1047/independent_audits.json','w').write(json.dumps(result,indent=2))
print(json.dumps({'windows':window,'p3':p_adic[:10],'eta':eta,'logCap':c0,'asymp':asymp},indent=2)[:16000])
