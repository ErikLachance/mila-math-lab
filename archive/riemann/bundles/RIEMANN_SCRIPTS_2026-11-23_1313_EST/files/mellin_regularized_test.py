from sympy import primerange, primepi
from mpmath import mp
import json
mp.dps=70
GAM=mp.euler
# Primitive real quadratic character modulo 4: 1 for 1 mod 4, -1 for 3 mod 4.
def chi4(n):
    return 0 if n%2==0 else (1 if n%4==1 else -1)
def L4(s):
    return mp.dirichlet(s,[0,1,0,-1])
L1= L4(1)
c=mp.dirichlet(1,[0,1,0,-1],1)/L1
cp=mp.diff(lambda s: mp.diff(L4,s)/L4(s),1)
ref1=1+GAM+2*mp.stieltjes(1)+GAM**2
ref4=c-cp
prime_powers=[]
for p in primerange(2,1000001):
    n=int(p)
    while n<=1000000:
        prime_powers.append((n,mp.log(int(p)),chi4(int(n))))
        n*=int(p)
prime_powers.sort()
results=[]
for X in [100,1000,10000,100000,1000000]:
    logX=mp.log(X)
    m1=mp.mpf(0);m4=mp.mpf(0)
    for n,l,chi in prime_powers:
        if n>X:break
        t=l*((logX-mp.log(n)-1)/n+mp.mpf(1)/X)
        m1+=t;m4+=chi*t
    m1+=-logX**2/2 +(1+GAM)*logX
    m4+=c*logX
    results.append(dict(X=X, I1=mp.nstr(m1,35),I4=mp.nstr(m4,35),error1=mp.nstr(m1-ref1,20),error4=mp.nstr(m4-ref4,20)))
print('L4 1',mp.nstr(L1,35),' expected pi/4',mp.nstr(mp.pi/4,35))
print('c',mp.nstr(c,35),'cprime',mp.nstr(cp,35))
print('zeta-reg-value',mp.nstr(ref1,35),'chi4-reg-value',mp.nstr(ref4,35))
for r in results:print(r)
with open('/mnt/data/riemann_20261123_1253/mellin_regularized_test.json','w') as f:json.dump(dict(ref1=str(ref1),ref4=str(ref4),c=str(c),cp=str(cp),results=results),f,indent=2)
