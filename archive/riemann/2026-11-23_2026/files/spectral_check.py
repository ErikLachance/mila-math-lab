from pathlib import Path
from fractions import Fraction as Q
import json,time,mpmath as mp
from certified_bump import primes_to,log_bound,kb,run,H_real
from math import isqrt
start=time.monotonic();mp.mp.dps=45
base=Path(__file__).parent;report=json.loads((base/'certified_bump.json').read_text())
T=200;gam=[];i=1
while True:
    z=mp.zetazero(i)
    if mp.im(z)>T:break
    gam.append(mp.im(z));i+=1

def H(y):return mp.fprod(mp.sinc(y/mp.mpf(2)**j) for j in range(1,81))
vals=[(y,H(y)**2) for y in gam]
# N_+(u)<=u^2 for u>=200 (from HSW); strip bound |H|^2<=3*2^56/y^14.
# Dyadic bands: both signs, N_+(2^(j+1)T)<=4*(2^j T)^2.
rows=[]
for row in report['rows']:
    x=row['x'];root=isqrt(x)
    est=2*mp.fsum(c*mp.cos(y*mp.log(x)) for y,c in vals)
    tail=Q(24*root*2**56,T**12)*(1/(1-Q(1,2**12)))
    L=mp.mpf(Q(row['lower_exact']).numerator)/Q(row['lower_exact']).denominator;U=mp.mpf(Q(row['upper_exact']).numerator)/Q(row['upper_exact']).denominator
    tf=mp.mpf(tail.numerator)/tail.denominator
    assert L-tf<=est<=U+tf
    # stronger observed, not required for proof
    inside=L<=est<=U
    rows.append(dict(x=x,spectral_estimate=str(est),analytic_tail_bound=str(tf),inside_arithmetic_interval=inside))
# Independent trial division prime list verification, for largest arithmetic search.
lim=8*1024
trial=[n for n in range(2,lim+1) if all(n%d for d in range(2,isqrt(n)+1))]
assert trial==primes_to(lim)
# Cross-check interval enclosures for actual log values using arbitrary precision, not proof.
for n in range(1,lim+1,17):
    l,h=log_bound(Q(n,1024));v=mp.log(mp.mpf(n)/1024)
    assert mp.mpf(l.numerator)/l.denominator<=v<=mp.mpf(h.numerator)/h.denominator
out=dict(zeros_below_T=len(gam),next_zero=str(z),T=T,prime_count=len(trial),trial_division_checked=lim-1,log_numeric_checks=len(range(1,lim+1,17)),rows=rows,elapsed_code_seconds=time.monotonic()-start,warning='mpmath zero ordinates and finite product are not interval certified; tail bound analytic; independent numeric regression only.')
(base/'spectral_check.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))

