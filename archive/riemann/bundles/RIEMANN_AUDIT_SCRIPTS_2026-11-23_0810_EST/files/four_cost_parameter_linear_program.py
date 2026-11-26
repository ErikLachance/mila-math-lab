from fractions import Fraction as Q
import json
from pathlib import Path

root=Path('/mnt/data/riemann_20261123_0751')

def terms(a,b,c):
    return [1-a, 1+a-b, a, b-2*c]

def best_with_c_cap(cap):
    if cap<=Q(1,4):
        c=cap;a=(1+2*c)/3;b=(2+4*c)/3;t=(2-2*c)/3
    else:
        # Any b in [1,2*c+1/2] works at a=1/2
        c=cap;a=Q(1,2);b=(1+a+2*c)/2;t=Q(1,2)
    assert max(terms(a,b,c))==t
    return a,b,c,t

results=[]
for cap in (Q(0),Q(1,16),Q(1,8),Q(1,5),Q(1,4),Q(1,2),Q(1),Q(2)):
    a,b,c,t=best_with_c_cap(cap)
    # Rigorous dual inequalities for all nonnegative a,b and c <= cap:
    # t >= a and t >= 1-a implies t>=1/2.
    # from 1-a<=t, 1+a-b<=t, b-2c<=t:
    # b >= 1+a-t and b <= t+2c => 1+a-2c<=2t; using a>=1-t => 2-2c<=3t.
    cert=max(Q(1,2),(Q(2)-2*cap)/3)
    assert cert==t,(cap,cert,t)
    results.append({'c_upper':str(cap),'a':str(a),'b':str(b),'c':str(c),'optimal_t':str(t),'four_term_exponents':[str(x) for x in terms(a,b,c)],'dual_lower_bound':'max(1/2,(2-2*c_upper)/3)'})

# Anisotropic per-step height cost m^r gives replacing a by r*a in objective.
# If other terms made negligible, minimum max(1-a,r*a)=r/(r+1)
for r in (1,2,3,4,10):
    a=Q(1,r+1);t=Q(r,r+1)
    assert max(1-a,r*a)==t

# Test approximate over bounded exact grid at several caps, never grid as proof.
for cap in (Q(0),Q(1,8),Q(1,4),Q(1,2)):
    t=best_with_c_cap(cap)[3]
    grid=Q(1,16)
    vals=[]
    for ai in range(0,17):
        a=ai*grid
        for bi in range(0,65):
            b=bi*grid
            vals.append(max(terms(a,b,cap)))
    assert min(vals)>=t

out={'formal_optimization':'Let m=x^a,k=x^b,n=x^c; four losses have exponents 1-a,1+a-b,a,b-2c. Under 0<=c<=C and a,b>=0, optimum t=max(1/2,(2-2C)/3). Proof lower bounds: max(a,1-a)>=1/2; if all four exponents<=t then 1-a<=t=>a>=1-t, and b>=1+a-t, b<=t+2c so 2-2c<=3t. Explicit optimizers are given.', 'cases':results,'warning':'Unconstrained toy exponent algebra only; physical choices have significant number-theoretic, field, height and integrality restrictions, so this does not prove (M).'}
(root/'four_cost_parameter_linear_program.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
