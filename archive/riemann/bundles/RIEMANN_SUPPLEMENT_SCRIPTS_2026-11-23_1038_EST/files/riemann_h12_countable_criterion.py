#!/usr/bin/env python3
"""Independent exact integer check of countable rational exponent H12 grid criterion geometry."""
from pathlib import Path
import json,hashlib

def h_max(a,j):
    # theta_j=1/2+1/j=(j+2)/(2j); h^(4j)<=8^(2j)*a^(3j+2)
    target=8**(2*j)*a**(3*j+2)
    lo=1;hi=2
    while hi**(4*j)<=target:lo=hi;hi*=2
    while hi-lo>1:
        h=(lo+hi)//2
        if h**(4*j)<=target:lo=h
        else:hi=h
    assert lo**(4*j)<=target<(lo+1)**(4*j)
    return lo

def grid(m,j):
    nodes=[m*m];end=m**3
    while nodes[-1]<end:
        a=nodes[-1]
        h=h_max(a,j)
        b=min(a+h,end)
        assert (b-a)**(4*j)<=8**(2*j)*a**(3*j+2)
        nodes.append(b)
    assert nodes[0]==m*m and nodes[-1]==m*m*m
    return nodes

rows=[]
for j,m in [(3,30),(4,100),(10,1000),(100,1000),(100,10000)]:
    g=grid(m,j)
    rows.append({'j':j,'theta':f'({j+2})/(2*{j})','m':m,'start':g[0],'end':g[-1],'steps':len(g)-1,'max_gap':max(b-a for a,b in zip(g[:-1],g[1:])),'all_bigint_checks':'PASS'})
report={'statement':'RH iff for every integer j>=3, there exists finite C_j>=0 and arbitrarily large integers m such that G(n)<=C_j*n^theta_j at every integer node n of the grid for theta_j=1/2+1/j on [m^2,m^3].','proof':'RH => G(x)=O(sqrt(x)) from source explicit formula, so yes. Converse: for each j, exact grid h^(4j)<=8^(2j) a^(3j+2) ensures G(x)<=(C_j+1)x^theta_j for all real x in [m^2,m^3]. Given any tau>1/2 choose j so theta_j<tau, then m large enough that (C_j+1)*(m^2)^(theta_j-tau)<=1. Thus G(x)<=x^tau on arbitrarily far-out [m^2,m^3]. Source one-sided Landau interval lemma implies no zeta zeros with Re>tau; take tau down to half and functional equation to deduce RH. No hidden extension to arbitrary leading constants required.','notes':'This is strictly a conditional restatement and not a proof, since it supplies no uniform C_j or arithmetic G values for arbitrarily large m. It reduces quantifiers to countable j and integer grid nodes but still an infinite unproved arithmetic condition. Source Part II sections 4-5 are pointwise in x and permits auxiliary q,d to vary with x; a weakened H12 need only establish pointwise hypotheses at those nodes WITH constants uniform in m and x. This does not follow from finite testing.','finite_exact_integer_tests':rows}
out=Path('/mnt/data/riemann_current/riemann_h12_countable_criterion.json')
out.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(rows,indent=2))
for p in [Path(__file__),out]:print('SHA256',p.name,hashlib.sha256(p.read_bytes()).hexdigest())
