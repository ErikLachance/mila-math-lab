from sympy import primerange
from mpmath import mp
import json
mp.dps=60
C=2+mp.euler-mp.log(4*mp.pi)
def T(x):
    x=mp.mpf(x)
    if x==1:return 1-mp.log(2)
    return 1-mp.log(1-1/x**2)/2 - x*mp.atanh(1/x)
xs=[1,2,3,10,100,1000,10000,100000]
seq=[]
for p in primerange(2,max(xs)+1):
    n=int(p)
    while n<=max(xs):seq.append((n,mp.log(int(p))));n*=int(p)
seq.sort()
out=[]
for x in xs:
    g=sum(l*(mp.mpf(x)/n-1) for n,l in seq if n<=x)-x*mp.log(x)+(1+mp.euler)*x
    spectral=g-mp.log(2*mp.pi)+T(x)
    ratio=abs(spectral)/mp.sqrt(x)
    out.append({'x':x,'G1':mp.nstr(g,25),'T':mp.nstr(T(x),25),'spectral':mp.nstr(spectral,25),'ratio':mp.nstr(ratio,25),'slack':mp.nstr(C-ratio,25)})
Z80=2*sum(1/(mp.im(mp.zetazero(k))**2+mp.mpf(1)/4) for k in range(1,81))
print('C = 2 + EulerGamma - ln(4*pi) =',mp.nstr(C,45))
print('C80=',mp.nstr(Z80,45),'tail_unestimated=',mp.nstr(C-Z80,25))
for r in out:print(r)
with open('/mnt/data/riemann_20261123_1253/sharp_rh_smoothed_bound.json','w') as f:json.dump({'C':str(C),'C80':str(Z80),'results':out},f,indent=2)
