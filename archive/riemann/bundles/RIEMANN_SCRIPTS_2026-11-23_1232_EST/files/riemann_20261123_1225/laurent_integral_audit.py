import math,json,mpmath as mp
import sympy as sy
mp.mp.dps=60
Ns=[100,1000,10000,100000,1000000]
checks=[]
for N in Ns:
    term=mp.mpf(0);psi=mp.mpf(0);powercount=0
    for p in sy.primerange(1,N+1):
        lp=mp.log(p);v=p
        while v<=N:
            psi+=lp;term+=lp/v;powercount+=1
            v*=p
    integrated=term-psi/N-mp.log(N)
    const=-1-mp.euler
    exact_finite_identity_from_step_function=True
    checks.append({'N':N,'prime_powers':powercount,'psi':mp.nstr(psi,20),'finite_integral':mp.nstr(integrated,23),'limiting_value':mp.nstr(const,23),'error_vs_asymptotic':mp.nstr(integrated-const,20),'dirichlet_partial_sum_minus_log':mp.nstr(term-mp.log(N),23)})
# Analytic: for Re(s)>1 integral = -zeta'/[s zeta]-1/(s-1), extend to s=1 using zero-free region.
# zeta=1/u+gamma + O(u); -zeta'/zeta =1/u-gamma +O(u); division by (1+u) produces -1-gamma.
for e in ['0.1','0.01','0.001','0.0001','0.00001']:
    s=1+mp.mpf(e)
    Mellin= -mp.diff(mp.zeta,s)/(s*mp.zeta(s))-1/(s-1)
    checks.append({'s':mp.nstr(s,9),'meromorphic_Mellin':mp.nstr(Mellin,22),'limit_minus_1_minus_gamma':mp.nstr(Mellin+1+mp.euler,17)})
result={'analytic_identity_for_Re_s_gt_1':"integral_1^infty (psi(x)-x) x^(-s-1) dx = -zeta'(s)/(s*zeta(s))-1/(s-1)", 'extension_note':'Taking s->1+ requires an integrable PNT remainder bound, not mere pointwise convergence; Laurent expansion gives -1-gamma.', 'finite_step_integral_exact_identity':'integral_1^X (psi(u)-u)/u^2 du = sum_{n<=X}Lambda(n)/n - psi(X)/X - log(X)', 'checks':checks, 'status':'Exact finite identity; numerical evaluations not proof of PNT remainder or RH.'}
with open('/mnt/data/riemann_20261123_1225/laurent_integral_audit.json','w') as f:json.dump(result,f,indent=2)
print(json.dumps(result,indent=2))
