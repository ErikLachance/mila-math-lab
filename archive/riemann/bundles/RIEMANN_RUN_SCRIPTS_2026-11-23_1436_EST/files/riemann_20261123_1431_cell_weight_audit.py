import json, math
from fractions import Fraction

def primes_upto(n):
    a=bytearray(b'\x01')*(n+1);a[:2]=b'\x00\x00'
    for p in range(2,math.isqrt(n)+1):
        if a[p]:a[p*p:n+1:p]=b'\x00'*((n-p*p)//p+1)
    return [i for i in range(n+1) if a[i]]

def chi3(p):return 0 if p==3 else (1 if p%3==1 else -1)

def terms(n):
    out=[]
    for p in primes_upto(n):
        k=1;v=p
        while v<=n:
            out.append((v,p,k,math.log(p),chi3(p)**k))
            if v>n//p:break
            v*=p;k+=1
    return sorted(out)

arr=terms(10000)
weights=[{1:Fraction(1,10000),-1:Fraction(1,100),0:Fraction(1,100)},
         {1:Fraction(1,100),-1:Fraction(1,10000),0:Fraction(1,100)}]
res=[]
for wi in weights:
    v=0.;count=0
    for x,p,k,lp,c in arr:
        ch=1-c;w=wi[c]
        if ch and Fraction(1,x)>w:
            v+=ch*lp*(1/x-float(w));count+=1
    # independent 'integral': integral Psi_c(u)/u^2 computed from a step sum of each class;
    # coefficients arise by exchanging finite sum/integral.
    integ=0.;numclass={str(c):0 for c in [-1,0,1]}
    for c in [-1,0,1]:
        Y=Fraction(1,1)/wi[c]
        coeff=0.
        for x,p,k,lp,z in arr:
            if z!=c or x>Y:continue
            coeff+=(1-c)*lp*(1/x-1/float(Y));numclass[str(c)]+=1
        integ+=coeff
    assert abs(v-integ)<1e-11
    M= math.log(1)-1-0.5772156649015328606+0.36828161597014784-\
         sum(math.log(float(wi[c])) for c in [-1,0,1])/3
    res.append({"w_plus":str(wi[1]),"w_minus":str(wi[-1]),"w_zero":str(wi[0]),"P":v,"M_geometric_unweighted_3cells":M,"difference":v-M,"terms_in_each_cell":numclass,"independent_finite_integral":integ})
print(json.dumps(res,indent=2))
with open('/mnt/data/riemann_20261123_1431_cell_weight_audit.json','w') as f:json.dump(res,f,indent=2)
