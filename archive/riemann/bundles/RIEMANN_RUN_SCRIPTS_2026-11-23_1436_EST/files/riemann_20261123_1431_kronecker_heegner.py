import json,time
import mpmath as mp
from sympy import legendre_symbol
mp.mp.dps=65

def cchi(d):
    c0=mp.mpf('0');c1=mp.mpf('0')
    for a in range(1,d):
        c=int(legendre_symbol(a,d))
        if not c:continue
        t=mp.mpf(a)/d
        c0-=c*mp.digamma(t)
        c1-=c*mp.stieltjes(1,t)
    return c1/c0-mp.log(d),c0/d

def lhs(d):
    root=mp.sqrt(d)
    r=mp.exp(-mp.pi*root)
    res=mp.log(4*mp.pi)+mp.log(root/2)-mp.pi*root/6
    for n in range(1,100):
        e=(-1)**n*r**n
        res+=4*mp.log(1-e)
        if abs(e)<mp.mpf('1e-70'):break
    return res
out=[]
for d in [7,11,19]:
    t=time.time();c,L=cchi(d)
    Left=lhs(d);Right=mp.euler+mp.log(2*mp.pi/mp.sqrt(d))-c
    err=Left-Right
    assert abs(err)<mp.mpf('1e-55'),(d,err)
    out.append({'d':d,'class_number':1,'L_1':mp.nstr(L,40),'logder_1':mp.nstr(c,40),'eta_side':mp.nstr(Left,40),'analytic_side':mp.nstr(Right,40),'abs_error':mp.nstr(abs(err),8),'seconds':round(time.time()-t,3)})
print(json.dumps(out,indent=2))
open('/mnt/data/riemann_20261123_1431_kronecker_heegner.json','w').write(json.dumps(out,indent=2))
