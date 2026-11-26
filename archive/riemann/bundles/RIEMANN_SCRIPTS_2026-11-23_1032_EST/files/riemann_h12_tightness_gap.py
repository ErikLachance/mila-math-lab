#!/usr/bin/env python3
"""High-precision adversarial test: one-sided interpolation envelope sharp in a prime-power-free gap."""
import math,json,hashlib
from pathlib import Path
import mpmath as mp
mp.mp.dps=85
N=20000
lam_primes={}
powers={}
for p in range(2,N+1):
    if all(p % d for d in range(2,math.isqrt(p)+1)):
        q=p
        while q<=N:
            powers[q]=p
            q*=p
active=sorted(powers)
starts=[(b-a,a,b) for a,b in zip(active[:-1],active[1:]) if a>10000]
starts.sort(reverse=True)
rows=[]
for gap,a,b in starts[:8]:
    coeff_a=mp.fsum([mp.log(powers[n])/n for n in active if n<a])
    coeff_b=mp.fsum([mp.log(powers[n]) for n in active if n<a])
    # no contribution from n=a or n=b at boundary; in gap S linear
    def G(x):
        return x*coeff_a-coeff_b-x*mp.log(x)+(1+mp.euler)*x
    x=mp.mpf(a+b)/2;t=mp.mpf('0.5')
    D=t*(mp.mpf(a)*mp.log(a)+mp.mpf(b)*mp.log(b))-x*mp.log(x)
    interpol=(G(a)+G(b))/2+D
    residual=G(x)-interpol
    upper=mp.mpf(gap)**2/(8*a)
    ratio=D/upper
    assert abs(residual)<mp.mpf('1e-65')
    assert 0<D<upper
    rows.append({'gap':gap,'a':a,'b':b,'D':mp.nstr(D,30),'h2_over_8a':mp.nstr(upper,30),'D_to_upper_ratio':mp.nstr(ratio,30),'midpoint_interpolation_error':mp.nstr(residual,9)})
result={'theorem':'For adjacent prime powers a<b with no prime-power strictly between, S(x)=sum Lambda(n)/n*(x-n)_+ is affine on [a,b]. Thus G(x)=chord(G(a),G(b))+D(a,b;x) EXACTLY, and at the midpoint D/((b-a)^2/(8a)) tends 1 as h/a tends 0. The interpolation upper-bound defect is therefore genuinely needed, not a numerical artifact.','verification':rows,'limits':'Tightness of a convexity envelope is not RH progress and does not imply ability to check endpoint upper bounds for arbitrarily large scales.'}
out=Path('/mnt/data/riemann_current/riemann_h12_tightness_gap.json');out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(rows[:5],indent=2))
for p in [Path(__file__),out]: print('SHA256',p.name,hashlib.sha256(p.read_bytes()).hexdigest())
