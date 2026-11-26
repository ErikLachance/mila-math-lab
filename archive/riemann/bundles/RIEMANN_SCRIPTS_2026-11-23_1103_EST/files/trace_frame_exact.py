#!/usr/bin/env python3
"""Exact prime-root counting audit of Rubinstein III.8, Lemma T1, using p+1 MUBs in C^p.
This tests the finite Hilbert-space skeleton, NOT deep automorphic trace hypotheses.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product
import json

def mod_poly_norm2(phase_list, p):
    cnt=Counter(v%p for v in phase_list)
    corr=[sum(cnt[j]*cnt[(j-r)%p] for j in range(p)) for r in range(p)]
    # All polynomial coefficients after reducing z^(p-1)=-sum_(j0..p-2) z^j.
    assert len(corr)==p
    if any(corr[j]!=corr[-1] for j in range(1,p-1)):
        raise ValueError(('non-rational Gauss abs-squared',p,phase_list,corr))
    value=corr[0]-corr[-1]
    assert value>=0
    return value

report=[]
for p in [3,5,7]:
    # Basis labels: C (computational), A(a) for each quadratic phase a.
    columns=[('C',b) for b in range(p)] + [('A',a,b) for a in range(p) for b in range(p)]
    assert len(columns)==p*(p+1)
    observed=Counter()
    for i,j in product(range(len(columns)),repeat=2):
        u=columns[i];v=columns[j]
        if u[0]=='C' and v[0]=='C':
            norm=F(1 if u[1]==v[1] else 0)
        elif u[0]=='C' or v[0]=='C':
            norm=F(1,p)
        else:
            _,a,b=u;_,c,d=v
            phases=[((c-a)*x*x+(d-b)*x)%p for x in range(p)]
            norm=F(mod_poly_norm2(phases,p),p*p)
        expected=F(1) if i==j else (F(0) if (u[0]==v[0] and (u[0]=='C' or u[1]==v[1])) else F(1,p))
        assert norm==expected, (u,v,norm,expected)
        observed[str(norm)]+=1
    # By finite-field Gaussian orthogonality, each basis contributes I_p:
    # Q=sum_w B_w B_w^*=(p+1)I_p.
    D=F(p);S=F(len(columns));Dstar=D;kappa=F(1,p+1)
    assert 0<kappa<=F(1,4) and Dstar<=kappa*S
    trQ=S;trQ2=F((p+1)**2*p)
    assert trQ2==trQ**2/D
    assert trQ2 <=(1+5*kappa)*trQ**2/D
    # Diag Gram K_ii=1, offdiag squared <=d_i d_j / Dstar =1/p.
    assert sum(F(key)*val for key,val in observed.items())==trQ2
    report.append(dict(p=p,D=p,W=len(columns),S=int(S),kappa=str(kappa),cross_abs2_counts=dict(observed),trQ=int(trQ),trQ2=int(trQ2),bound_trQ2=str((1+5*kappa)*trQ**2/D),status='EXACT INTEGER PASS'))

with open('/mnt/data/riemann_runs/20261123_1047/trace_frame_exact.json','w') as f:json.dump(report,f,indent=2)
print(json.dumps(report,indent=2))
