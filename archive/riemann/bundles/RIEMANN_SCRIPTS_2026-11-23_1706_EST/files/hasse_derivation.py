from math import comb
import json

def mul_mod_poly(pairs,p):
    return {i:c%p for i,c in pairs.items() if c%p}

def derivative(a,p):
    return mul_mod_poly({i-1: (i*c)%p for i,c in a.items() if i>0},p)

def product(a,b,p):
    z={}
    for i,x in a.items():
        for j,y in b.items():
            z[i+j]=(z.get(i+j,0)+x*y)%p
    return mul_mod_poly(z,p)

def add(a,b,p):
    c=a.copy()
    for i,v in b.items():c[i]=(c.get(i,0)+v)%p
    return mul_mod_poly(c,p)

def apply_D(A,B,f,p):
    # D(x)=2y, D(y)=f'(x). Multiplication reduction y^2=f(x).
    return add(product({0:2},product(f,derivative(B,p),p),p),product(derivative(f,p),B,p),p),product({0:2},derivative(A,p),p)

def H(f,p):
    q={0:1}
    for _ in range((p-1)//2):q=product(q,f,p)
    return q.get(p-1,0)

def trial(f,p):
    a,b={1:1},{}
    for _ in range(p):a,b=apply_D(a,b,f,p)
    h=H(f,p)
    assert not a and not (set(b)-{0}), (p,a,b)
    # D^p = b0/2 *D via x, 2 invertible
    c=(b.get(0,0)*pow(2,-1,p))%p
    return dict(p=p,hasse=h,dp_coefficient=c,match_hasse=c==h,zero_equivalence=(c==0)==(h==0))

primes=[]
for p in range(5,151):
    if all(p%q for q in range(2,int(p**0.5)+1)):primes.append(p)
results={}
for name,f in [('j0',{3:1,0:-1}),('j1728',{3:1,1:-1})]:
    rs=[trial(f,p) for p in primes]
    for r in rs:
        p=r['p']; expect=(p%3==2) if name=='j0' else (p%4==3)
        assert (r['dp_coefficient']==0)==expect,(name,r,expect)
        assert r['match_hasse'],(name,r)
    results[name]=rs
print('TESTS',sum(map(len,results.values())),'SUCCESS; first ten each')
print(json.dumps({k:v[:10] for k,v in results.items()},indent=2))
with open('/mnt/data/riemann_20261123_1659/hasse_derivation_results.json','w') as f:json.dump(results,f,indent=2)
