from fractions import Fraction
from collections import defaultdict
import json
import sympy as sp

def powers(x):
    for p in sp.primerange(1,x+1):
        n=int(p);k=1
        while n<=x:
            yield int(p),k,n
            n*=int(p);k+=1

def test(d,a,w):
    x=Fraction(a,1)/w
    left=defaultdict(Fraction);right=defaultdict(Fraction)
    inert_terms=ram_terms=0
    for p,k,n in powers(x.numerator//x.denominator):
        chi=int(sp.kronecker_symbol(-d,p))
        weight=max(Fraction(0),Fraction(a,n)-w)
        left[p]+=(1-chi**k)*weight
        if chi==-1 and k%2==1:
            right[p]+=2*weight;inert_terms+=1
        if chi==0:
            assert p==d
            right[p]+=weight;ram_terms+=1
    left={p:v for p,v in left.items() if v}
    right={p:v for p,v in right.items() if v}
    assert left==right,(d,a,w,left,right)
    return {'d':d,'a':a,'w':str(w),'x':str(x),'inert_terms':inert_terms,'ramified_terms':ram_terms,'nonzero_log_p_coefficients':sum(c!=0 for c in left.values()),'coefficient_equality':True}
vals=[]
for d in [3,7,11,19,31]:
    for a,w in [(2,Fraction(1)),(13,Fraction(1,3)),(100,Fraction(1,7)),(1000,Fraction(2,3))]:
        vals.append(test(d,a,w))
# Include the p=2 splitting rule by Kronecker: d=3 (-3/2)=-1, d=7 (-7/2)=1.
assert int(sp.kronecker_symbol(-3,2))==-1 and int(sp.kronecker_symbol(-7,2))==1
result={'source_identity':'For quadratic chi=Kronecker(-d,.), d prime =3(mod4): w[S(x)-S_chi(x)] = 2 sum_{inert p} sum_{odd k} log(p)*max(a/p^k-w,0) + log(d)*sum_{k>=1}max(a/d^k-w,0), where x=a/w, S(x)=sum_{n<=x}Lambda(n)(x/n-1).','status':'Exact rational equality of every log(p) coefficient; excludes separate analytic/linear normalizations in G and G_chi; NOT proof of (M) or RH.','tests':vals}
with open('/mnt/data/riemann_20261123_1225/inert_prime_hinge_identity.json','w') as f:json.dump(result,f,indent=2)
print('PASS',len(vals),'cases, all exact Fraction coefficients agree, d and p=2 handling verified')
