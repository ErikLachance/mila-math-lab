from math import comb,factorial
from fractions import Fraction as F
from collections import defaultdict
import json

def mul(A,B,lim):
    C=defaultdict(int)
    for (a,b),x in A.items():
        for (c,d),y in B.items():
            if a+b+c+d<=lim: C[(a+c,b+d)]+=x*y
    return {k:v for k,v in C.items() if v}
def add(A,B):
    C=defaultdict(int,A)
    for k,v in B.items():C[k]+=v
    return {k:v for k,v in C.items() if v}
def power(A,n,lim):
    B={(0,0):1}
    for _ in range(n):B=mul(B,A,lim)
    return B

def val(n,p):
    if n==0:return None
    r=0
    while n%p==0:n//=p;r+=1
    return r

def ell(n,p):
    if n==0:return 0
    j=0
    while n:
        j+=1;n//=p
    return j

def bound(N0,N1,p,T):
    c=[N0,N1]
    a=[c[s] if s in T else 0 for s in range(2)]
    C=[c[s]-a[s] for s in range(2)]
    L=C[:]  # all columns height one
    delta=sum(ell(a[s],p)+ell(L[s],p) for s in range(2)) + sum(ell(a[s],p)**2 for s in T)
    total=F(N0+N1,p*p-1)-delta
    for s in T:
        aa=a[s];cc=C[1-s]
        if aa==0:continue
        e_min=3 if 1-s in T else 1
        if cc==0:
            total+=F(aa,p**e_min) / (1-F(1,p*p))
        else:
            e=e_min
            while aa>cc*p**e:
                total+=F(aa,p**e)-cc
                e+=2
    return total

results=[]
for p,lim in [(3,38),(5,44)]:
    N=p*p
    q0={(1,0):1,(N,0):-1}
    q1={(0,1):1,(0,N):-1}
    h=add(mul(power(q0,p,lim),q1,lim),mul(power(q1,p,lim),q0,lim))
    hf={(0,0):1}
    checks=0
    min_margin=None
    worst=None
    nontriv_margin=None
    nontriv_worst=None
    positive_bound_cases=0
    for i in range(0,6):
        if i>0:hf=mul(hf,h,lim)
        if not hf:break
        for (a,b),hcoef in hf.items():
            for u0 in range(0,6):
                for u1 in range(0,6):
                    N0=a+u0;N1=b+u1
                    if N0+N1>lim:continue
                    val_b=val(factorial(N0)*factorial(N1)*hcoef,p)-i
                    for T in [(),(0,),(1,),(0,1)]:
                        q=bound(N0,N1,p,T)
                        margin=F(val_b)-q
                        checks+=1
                        if q>0:positive_bound_cases+=1
                        if i>=1 and (nontriv_margin is None or margin<nontriv_margin):
                            nontriv_margin=margin;nontriv_worst={"p":p,"i":i,"N0":N0,"N1":N1,"T":T,"v":val_b,"bound":str(q),"slack":str(margin)}
                        if min_margin is None or margin<min_margin:
                            min_margin=margin;worst={'p':p,'i':i,'N0':N0,'N1':N1,'u0':u0,'u1':u1,'T':T,'hcoef':hcoef,'v_p_coefficient':val_b,'lower_bound':str(q),'slack':str(margin)}
                        assert margin>=0,(p,i,N0,N1,T,val_b,q)
    results.append({'p':p,'nonzero_cases_tested':checks,'worst':worst,'nontriv_worst':nontriv_worst,'positive_bound_cases':positive_bound_cases,'all_pass':True})
with open('/mnt/data/riemann_20261123_1659/theta_minor_toy_exact.json','w') as f:json.dump(results,f,indent=2)
print(*results,sep='\n')
