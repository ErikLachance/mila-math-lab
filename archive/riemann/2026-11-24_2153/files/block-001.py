from fractions import Fraction as F
from math import factorial, isqrt
from itertools import product
from time import monotonic
import sympy as s
start=monotonic()
x=s.symbols('x'); P=s.Poly(s.cyclotomic_poly(21,x),x)
D=3**6*7**10
assert abs(int(P.discriminant()))==D
B=F(400,314)**6*F(factorial(12),12**12)*(isqrt(D)+1)
assert B<105
small=[]
for q in s.primerange(2,105):
    m=21
    while m%q==0: m//=q
    f=int(s.n_order(q,m)) if m>1 else 1
    if q**f<105: small.append((int(q),f,int(q**f)))
assert small==[(2,6,64),(7,1,7),(43,1,43)]
for q,a in [(2,1-x**3-x**9),(7,1-x+x**3),(43,1+x-x**3)]:
    n=abs(int(P.resultant(s.Poly(a,x))))
    f=next(f for v,f,norm in small if v==q)
    mat=s.Matrix(12,12,lambda i,j:s.Poly(s.rem(a*x**j,P.as_expr(),x),x).nth(i))
    assert n==abs(int(mat.det()))==q**f
    print('principal prime norm',n,'generator',a)
# Character congruences: chi|I = omega^(e+(p-1)/2 * bit), hence chi^2 never omega.
count=0
for p in s.primerange(5,150):
    for e in range(1,2*(p-1)):
        if 2*e%(p-1)==0: continue
        for bit,w in product((0,1),(-2,2)):
            assert (w*(e+bit*(p-1)//2)-1)%(p-1)!=0
            count+=1
# Polarization and matrix products: theta differential preserves upper/lower weights.
J=s.zeros(3)
for i in range(3):J[i,2-i]=1
for i,j in product(range(3),repeat=2):
    A=s.zeros(3);A[i,j]=1; T=-J*A.T*J
    assert all(T[a,b]==0 or b-a==j-i for a,b in product(range(3),repeat=2))
for i,j,k,l in product(range(3),repeat=4):
    if i<j and k<l and j==k: assert (i,l)==(0,2)
print('exact character cases',count,'prime norm certificate',small,'rational Minkowski upper bound',float(B),'script seconds',monotonic()-start)

