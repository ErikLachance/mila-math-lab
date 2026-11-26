from itertools import product
from fractions import Fraction as F
from collections import Counter
from time import monotonic
start=monotonic(); C=Counter()
# Enumerate all possible valuations of the four weights, absent = None.
for a in product([None,*range(1,13)],repeat=4):
    P=[(w,v) for w,v in zip((1,2,-1,-2),a) if w>0 and v is not None]
    N=[(-w,v) for w,v in zip((1,2,-1,-2),a) if w<0 and v is not None]
    if not P or not N: continue
    c,s=min((F(q*x+p*y,p+q),F(y-x,p+q)) for p,x in P for q,y in N)
    vpos=[x+p*s for p,x in P]; vneg=[y-q*s for q,y in N]
    assert min(vpos)==min(vneg)==c and c>0
    assert s.denominator<=4 and c*s.denominator==int(c*s.denominator)
    for z in (s-F(1,7),s+F(1,7)):
        assert min([x+p*z for p,x in P]+[y-q*z for q,y in N])<c
    C['mixed_valuation_patterns']+=1
# Full inertia: quadratic tau does not affect square of cyclotomic twist.
for p in (3,5,7,11,13,17,19,23,29,31,37,41,43):
    for e in range(1,2*p):
        if 2*e%(p-1)==0:continue
        for kind in (0,1):
            values=[(pow(x,e,p)*(1 if not kind or pow(x,(p-1)//2,p)==1 else -1))%p for x in range(1,p)]
            assert any(y*y%p!=1 for y in values)
            C['full_inertia_character_cases']+=1
# Independently test diagonal coefficient invariance under infinitesimal change of basis.
# Matrices over F_p[eps]/eps^2 as pairs of constant and linear arrays.
def add(A,B,p):return tuple(tuple((a+b)%p for a,b in zip(r,s)) for r,s in zip(A,B))
def mul(A,B,p):return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(3))%p for j in range(3)) for i in range(3))
def neg(A,p):return tuple(tuple(-x%p for x in r) for r in A)
def dm(A,B,p):return (mul(A[0],B[0],p),add(mul(A[0],B[1],p),mul(A[1],B[0],p),p))
I=tuple(tuple(int(i==j) for j in range(3)) for i in range(3)); Z=tuple((0,0,0) for _ in range(3))
for p in (5,7,11):
    for lam in range(1,p):
        D=((lam,0,0),(0,1,0),(0,0,pow(lam,-1,p)))
        for a,b,c,d in product(range(3),repeat=4):
            X=((a,b,c),(d,c,a),(b,d,a)); U=((0,a,b),(0,0,c),(0,0,0))
            A=dm(dm((I,X),(D,U),p),(I,neg(X,p)),p)
            assert A[0]==D and all(A[1][i][i]==0 for i in range(3))
            C['infinitesimal_diagonal_cases']+=1
print(dict(C)); print('script_seconds',monotonic()-start)
# Check first-order normalization kills every coboundary compatible with c.
# M fixed by derivative of theta = -J M^T J.
# For odd p this space consists of diag(a,0,-a), b(E12-E23), c(E21-E32).
cb=0; surviving=0
for p in (5,7,11,13):
    for lam in range(2,p-1):
        delta=(lam-pow(lam,-1,p))%p
        D=((delta,0,0),(0,0,0),(0,0,-delta%p))
        for a,b,c in product(range(p),repeat=3):
            M=((a,b,0),(c,0,-b%p),(0,-c%p,-a%p))
            B=add(mul(M,D,p),neg(mul(D,M,p),p),p)
            assert (B[0][1]==B[1][0]==0)==(b==c==0)
            cb+=1
            if b==c==0:surviving+=1
print('normalized_coboundary_cases',cb,'surviving_diagonal_centralizer',surviving)

