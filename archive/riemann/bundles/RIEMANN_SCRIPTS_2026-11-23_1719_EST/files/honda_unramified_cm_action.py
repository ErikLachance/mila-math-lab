import json
from math import gcd

def finite_field(p):
    D=next(d for d in range(2,p) if pow(d,(p-1)//2,p)==p-1)
    def mul(a,b):return ((a[0]*b[0]+D*a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
    def powe(a,n):
        r=(1,0)
        while n:
            if n&1:r=mul(r,a)
            a=mul(a,a);n//=2
        return r
    def prime_divs(n):
        out=[];i=2
        while i*i<=n:
            if n%i==0:
                out.append(i)
                while n%i==0:n//=i
            i+=1
        if n>1:out.append(n)
        return out
    n=p+1
    roots=[]
    for a in range(p):
        for b in range(p):
            w=(a,b)
            if w==(0,0) or b==0:continue
            if powe(w,n)!=(1,0):continue
            if any(powe(w,n//d)==(1,0) for d in prime_divs(n)):continue
            assert powe(w,p)==powe(w,n-1)
            assert powe(w,p*p)==w
            assert powe(w,p)!=w
            roots.append(w)
    assert len(roots)>0
    return {'p':p,'D_nonsquare':D,'primitive_order':n,'count_primitive_(p+1)-roots':len(roots),'example_w':roots[0],'w_p_frobenius_conjugate':powe(roots[0],p),'w_p_squared_identity':True,'sigma_w_minus_w_residue_nonzero':True}
rows=[finite_field(p) for p in [3,5,7,11,13,17,19,23,31]]
with open('/mnt/data/riemann_20261123_1659/honda_unramified_cm_action.json','w') as f:json.dump({'pass':True,'data':rows},f,indent=2)
print(*rows,sep='\n')
