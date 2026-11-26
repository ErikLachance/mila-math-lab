from math import gcd,isqrt,factorial
from itertools import product
from time import monotonic
import sympy as s
import numpy as np
start=monotonic()
def vp(a,p):
    assert a
    k=0
    while a%p==0: a//=p;k+=1
    return k
def teich(a,p,k):
    x=a%p
    for n in range(1,k):
        m=p**n
        choices=[x+j*m for j in range(p) if pow(x+j*m,p-1,m*p)==1]
        assert len(choices)==1
        x=choices[0]
    assert x==pow(a,p**(k-1),p**k)
    return x
def odd_factors(p,d,k):
    M=p**k; T={a:teich(a,p,k) for a in range(1,p)}
    out={}
    for b in (0,1):
        for j in range(p-1):
            if (b+j)%2==0:continue
            f=(d if b else 1)*(p if j else 1)
            terms=[a*(int(s.kronecker_symbol(-d,a)) if b else 1)*(pow(T[a%p],j,M) if j else 1) for a in range(1,f+1) if gcd(a,f)==1]
            n=sum(terms)%M
            assert n
            out[b,j]=(n,vp(n,p)-int(f%p==0))
    return out
for p,d in ((7,79),(37,3)):
    a=odd_factors(p,d,4); b=odd_factors(p,d,5)
    assert {j:v for j,(n,v) in a.items()}=={j:v for j,(n,v) in b.items()}
    assert all(b[j][0]%(p**4)==n for j,(n,v) in a.items())
    assert 1+sum(v for n,v in a.values())==1
    print('p,d',p,d,'nonzero valuations',[(j,n,v) for j,(n,v) in a.items() if v], 'all factors',len(a))
    if p==7: print('all p7 factors',a)
forms=[]
for a in range(1,isqrt(79//3)+1):
    for b in range(-a,a+1):
        if (b*b+79)%(4*a):continue
        c=(b*b+79)//(4*a)
        if a>c or ((abs(b)==a or a==c) and b<0) or gcd(gcd(a,b),c)>1:continue
        forms.append((a,b,c))
assert len(forms)==5
print('reduced forms -79',forms)
assert s.bernoulli(32)==-s.Rational(7709321041217,510)
assert [k for k in range(2,36,2) if s.numer(s.bernoulli(k))%37==0]==[32]
q=149; z=pow(int(s.primitive_root(q)),4,q); V=1
for c in range(1,19):V=V*pow((pow(z,c,q)-pow(z,-c,q))%q,c**4,q)%q
assert pow(z,37,q)==1 and z!=1 and pow(V,4,q)!=1
print('Vandiver p37 k32 certificate',q,z,V,pow(V,4,q))
# Check the nonzero character scalar of a genuine integral Stickelberger element
# (sigma_b-b)theta on eta*omega^4 (the component excluded in p7).
p=7;m=553;M=p**4;T={a:teich(a,p,4) for a in range(1,p)}
def ch(a,j):return int(s.kronecker_symbol(-79,a))*pow(T[a%p],j,M)%M
for j in (2,4):
    # b=5 is coprime to 553, compute via floor coefficients, inverse character.
    val=sum(((a*5)%m-5*a)//m*ch(a,-j) for a in range(1,m) if gcd(a,m)==1)%p
    print('Stickelberger mod7 for eta omega^'+str(j),val)
    assert (val!=0)==(j==4)
# Exact matrix exponential identities in F7[t]/(t^7)
p=7;I=np.eye(3,dtype=np.int64);J=np.fliplr(I); count=0;checks=0
for A,B in product(range(1,p),repeat=2):
    N=np.array([[0,B,0],[0,0,B],[A,0,0]],dtype=np.int64)
    P=[I]
    for k in range(1,8):P.append(P[-1]@N%p)
    assert np.array_equal(P[3],A*B*B*I%p) and np.any(P[7])
    assert np.array_equal(-J@N.T@J%p,-N%p)
    E={u:[pow(u,k,p)*pow(factorial(k),-1,p)*P[k]%p for k in range(7)] for u in range(p)}
    for u,v in product(range(p),repeat=2):
        for k in range(7):
            assert np.array_equal(sum((E[u][i]@E[v][k-i] for i in range(k+1)),np.zeros((3,3),dtype=np.int64))%p,E[(u+v)%p][k]);checks+=1
        count+=1
    for a,eta,u in product(range(1,p),(-1,1),range(p)):
        chi=a*a%p;D=np.diag([chi,1,pow(chi,-1,p)]);Di=np.diag([pow(chi,-1,p),1,chi])
        for k in range(7):
            X=E[u][k] if eta==1 else J@E[-u%p][k].T@J
            assert np.array_equal(D@X@Di%p,E[eta*chi*u%p][k]);checks+=1
print('truncated exponential products',count,'coefficient checks incl covariance',checks,'mixed matrices',36,'seconds',monotonic()-start)
