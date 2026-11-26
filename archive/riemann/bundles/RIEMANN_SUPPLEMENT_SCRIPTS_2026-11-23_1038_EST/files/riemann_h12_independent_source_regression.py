#!/usr/bin/env python3
"""Independent high-precision reproduction of source I.1 published smoothed prime-power values."""
from pathlib import Path
import json,hashlib
import mpmath as mp
from sympy import primerange
mp.mp.dps=65
max_x=2000000
terms=[]
for p in primerange(2,max_x+1):
    n=int(p)
    lp=mp.log(int(p))
    while n<=max_x:
        terms.append((n,lp))
        n*=int(p)
terms.sort(key=lambda x:x[0])
S1=mp.mpf(0);S2=mp.mpf(0);i=0
rows=[]
for x in [10000,100000,1000000,2000000]:
    while i<len(terms) and terms[i][0]<=x:
        n,lp=terms[i]
        S1+=lp/n;S2+=lp
        i+=1
    xx=mp.mpf(x)
    g=xx*S1-S2-xx*mp.log(xx)+(1+mp.euler)*xx
    printed={10000:1.749,100000:3.671,1000000:11.040,2000000:-12.268}[x]
    diff=float(g-printed)
    assert abs(diff)<.0008,(x,g,printed,diff)
    rows.append({'x':x,'prime_powers_included':i,'G_60_decimal':mp.nstr(g,62),'printed_Rubinstein_I1_three_decimals':printed,'difference':diff,'3_decimal_agrees':round(float(g),3)==printed})
res={'source':'Rubinstein et al, The Alpoge-Claude proof explained for zeta, v2 (2026-11-22), page 5, numerical checks G(10^4),G(10^5),G(10^6),G(2*10^6).','independent_method':'sympy.primerange, direct powers p^j and independent mpmath 65-digit accumulation of (sum log(p)/p^j,sum log(p)); no reuse of previous sieve or coefficient code.','rows':rows,'limitations':'Four sample values verify implementation of scalar G only. Do not infer RH, source (M), H12 or uniform growth.'}
out=Path('/mnt/data/riemann_current/riemann_h12_independent_source_regression.json');out.write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps(rows,indent=2))
for x in [Path(__file__),out]:print('SHA256',x.name,hashlib.sha256(x.read_bytes()).hexdigest())
