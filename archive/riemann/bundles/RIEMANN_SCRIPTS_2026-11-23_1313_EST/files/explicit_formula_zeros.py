from mpmath import mp
from sympy import primerange
import json
mp.dps=45
xs=[2,10,100,1000,10000]
maxx=max(xs)
seq=[]
for p in primerange(2,maxx+1):
    n=int(p)
    while n<=maxx:
        seq.append((n,mp.log(int(p))))
        n*=int(p)
seq.sort()
actual={x:sum(l*(mp.mpf(x)/n-1) for n,l in seq if n<=x)-x*mp.log(x)+(1+mp.euler)*x for x in xs}
zer=[]
for k in range(1,81):
    z=mp.zetazero(k)
    zer.append(z)
triv={x:mp.nsum(lambda k:mp.power(x,-2*k)/(2*k*(2*k+1)),[1,mp.inf]) for x in xs}
res=[]
for K in [2,5,10,20,40,80]:
    for x in xs:
        Z=2*mp.re(sum(mp.power(x,z)/(z*(z-1)) for z in zer[:K]))
        pred=mp.log(2*mp.pi)-Z-triv[x]
        res.append({'K':K,'x':x,'actual':mp.nstr(actual[x],25),'pred':mp.nstr(pred,25),'error':mp.nstr(pred-actual[x],13)})
for K in [2,10,40,80]:
    print('K',K,[(r['x'],r['error']) for r in res if r['K']==K])
print('triv2',mp.nstr(triv[2],25),'triv10',mp.nstr(triv[10],25))
with open('/mnt/data/riemann_20261123_1253/explicit_formula_zeros.json','w') as f:json.dump(res,f,indent=2)
