#!/usr/bin/env python3
"""Independent finite derivative envelope and analytic grid improvement via classical von Mangoldt harmonic theorem."""
import math,json,hashlib
from pathlib import Path
N=250000
v=[0.0]*(N+1);isprime=bytearray(b'\x01')*(N+1);isprime[0]=isprime[1]=0
for p in range(2,N+1):
    if isprime[p]:
        for t in range(p*p,N+1,p):isprime[t]=0
        k=p
        while k<=N:
            v[k]=math.log(p);k*=p
A=0.; mx=(0.,0,''); gamma=.5772156649015328606
max_abs_d=0.0; at=None
for n in range(2,N+1):
    left=A-math.log(n)+gamma
    A+=v[n]/n
    right=A-math.log(n)+gamma
    for val,kind in [(left,'left'),(right,'right')]:
        if abs(val)>max_abs_d:
            max_abs_d=abs(val);at=(n,kind,val)
# All interval derivative extrema lie at endpoints, hence finite sample at each break is exhaustive modulo fp error.
Y=1000.;theta=.6
absolute_finite_M=max_abs_d+0.0001
h_old=Y**theta/((1.5*math.log(Y))**2+3*math.log(Y)+1)
h_finite=Y**theta/absolute_finite_M
result={'finite_domain':'[2,250000], exhaustive left/right derivative endpoints of each piece, computed in float64; NOT proof for all x','observed_max_abs_G_primepower_one_sided_derivative':max_abs_d,'max_at':at,'N':N,
'lemma':'By the classical unconditional von Mangoldt harmonic estimate sum_{n<=x} Lambda(n)/n = log x + O(1) (Metamath vmadivsum; Shapiro, equation 9.2.13), G\'(x)=sum Lambda(n)/n - log x+gamma = O(1) away from prime powers. G continuous at breaks, therefore globally Lipschitz beyond x0 with some absolute M0. For any Y>=x0 and 0<theta<1, a left h-net with h=Y^theta/M0 and G(nodes)<=C nodes^theta implies G(x)<=(C+1)x^theta throughout [Y,Y^(3/2)]. Number nodes O(Y^(3/2-theta)), improving elementary O(Y^(3/2-theta)*log^2Y).',
'proof_ingredients':'Classical harmonic von Mangoldt estimate; derivative of smoothed S; continuity at breaks. The explicit M0 is not evaluated analytically; numeric max in finite interval is only a diagnostic.',
'finite_Y_illustration':{'Y':Y,'theta':theta,'old_h':h_old,'finite_empirical_M':absolute_finite_M,'finite_h':h_finite,'h_ratio':h_finite/h_old},
'warning':'This is an expository sufficient criterion for the scalar statistic G only, not an estimate on G, not a bound on the arithmetic construction data, and not RH.'}
p=Path('/mnt/data/riemann_current/riemann_h12_mertens_upgrade.json');p.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2));print('SHA256 CODE',hashlib.sha256(Path(__file__).read_bytes()).hexdigest());print('SHA256 JSON',hashlib.sha256(p.read_bytes()).hexdigest())
