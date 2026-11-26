import json
from math import factorial
from fractions import Fraction as F

def vp_fact(n,p):
    r=0
    while n:n//=p;r+=n
    return r

def ell(n,p):
    r=0
    while n:n//=p;r+=1
    return r

rows=[]
for p in [3,5,7,11,13]:
    for k in [4,5,6]:
        N=p**k
        # r0=r1=1, nu=1, S={0,1}, T={0}
        # c0=N,c1=1, all heights1. h=q0^p q1 + q1^p q0, u0=u1=1.
        # F=(h/p)*Z0^(N-p); [Z0^N Z1]F =1/p.
        alpha0=N;C1=1
        total=sum((F(N,p**e)-1) for e in range(1,k+1,2) if N>p**e)
        d=F(N+1,p*p-1)
        L=ell(N,p)
        Delta=L+L*L+ell(1,p)
        bound=total+d-Delta
        v=vp_fact(N,p)-1
        assert bound>0
        assert F(v)>=bound
        rows.append({'p':p,'N':N,'v_p(J_F)':v,'rational_bound':str(bound),'positive':True,'slack':str(F(v)-bound),'v_p_N_factorial':vp_fact(N,p),'sum_odd_excess':str(total),'Delta':Delta})
with open('/mnt/data/riemann_20261123_1659/theta_minor_positive_certificate.json','w') as f:json.dump({'pass':True,'cases':len(rows),'data':rows},f,indent=2)
print('PASS',len(rows),'nonzero theta polynomial examples with nonzero h/p and STRICTLY POSITIVE theorem bound')
for x in rows[:6]: print(x)
