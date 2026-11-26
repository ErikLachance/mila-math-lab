#!/usr/bin/env python3
"""Independent numerical regression for Rubinstein 2026 ramp statistic I.2, not a RH proof."""
import math, json, time
from pathlib import Path
from mpmath import euler
start=time.monotonic()
N=2000000
is_prime=bytearray(b'\x01')*(N+1)
is_prime[0]=0; is_prime[1]=0
for d in range(2,math.isqrt(N)+1):
    if is_prime[d]:
        is_prime[d*d:N+1:d]=b'\x00'*(((N-d*d)//d)+1)
lambda_values=[0.0]*(N+1)
prime_power_counts=0
for p in range(2,N+1):
    if is_prime[p]:
        power=p; lp=math.log(p)
        while power<=N:
            lambda_values[power]=lp
            power*=p
            prime_power_counts+=1
queries=[10000,100000,1000000,2000000]
prefix_logn=0.0; prefix_logover=0.0
res=[]; j=0
for k in range(1,N+1):
    v=lambda_values[k];prefix_logn+=v;prefix_logover+=v/k
    if k==queries[j]:
        S=k*prefix_logover-prefix_logn
        G=S-k*math.log(k)+(1+float(euler))*k
        previous=[1.749,3.671,11.040,-12.268][j]
        res.append({'x':k,'S':S,'G':G,'reference_3dp':previous,'difference':G-previous})
        j+=1
        if j==len(queries):break
assert max(abs(z['difference']) for z in res)<0.004, 'Numerical regression failed'
# Toy oscillatory function has a pole off the critical line but is nonpositive on an infinite point sequence.
beta=0.70;theta=0.51;omega=1.4
point_log=[(2*m+1)*math.pi/omega for m in range(1,11)]
assert all(math.cos(omega*u)<-0.999999 for u in point_log)
# For long log intervals [log Y, 1.5 log Y], gamma*interval length eventually exceeds 2pi,
# hence cos attains +1 and upper bound cannot persist at all points.
for U in (20,40,80,160):
    assert omega*U/2>2*math.pi
    peaks=[2*math.pi*j/omega for j in range(math.ceil(omega*U/(2*math.pi)),math.floor(1.5*omega*U/(2*math.pi))+1)]
    assert peaks
report={'source':'Rubinstein zeta-paper v2 PDF I.2 and I.3 2026-11-22','regression':res,'n_prime_powers':prime_power_counts,'max_rounding_difference':max(abs(z['difference']) for z in res),'toy_sparse_points_conclusion':'Pointwise upper bounds on infinitely many isolated x do not exclude off-line-type oscillations; long multiplicative intervals are a genuine extra condition.','elapsed_wall_seconds':time.monotonic()-start,'status':'independent floating regression, not formal verification'}
out=Path(__file__).with_suffix('.json');out.write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
