from itertools import product
from collections import Counter
from time import monotonic
import sympy as s
T=monotonic(); C=Counter()
# Check exact two-sided flag extraction on all fixed-diagonal matrices mod 5.
p=5; a=(2,1,3); b=(3,1,2)
D=s.diag(*a); I=s.eye(3)
# simple integer arithmetic avoids expensive symbolic loop
def mm(A,B): return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(3))%p for j in range(3)) for i in range(3))
def diag(v): return tuple(tuple(v[i]%p if i==j else 0 for j in range(3)) for i in range(3))
def minus(A,x): return tuple(tuple((A[i][j]-(x if i==j else 0))%p for j in range(3)) for i in range(3))
Z=diag((0,0,0)); M=diag(a); P=mm(minus(M,a[1]),minus(M,a[2])); Q=mm(minus(M,a[0]),minus(M,a[1]))
for vals in product(range(p),repeat=6):
 u,v,w,r,t,z=vals; B=((b[0],u,v),(w,b[1],r),(t,z,b[2]))
 test=mm(minus(B,b[0]),P)==Z and mm(Q,minus(B,b[2]))==Z
 assert test==(w==t==z==0)
 C['flag_extraction']+=1
 if test:C['upper_triangular_survivors']+=1
# Universal triple-product identity for independent upper triangular factors.
xs=s.symbols('x:9'); a1,a2,a3,b1,b2,b3,c1,c2,c3=s.symbols('a1 a2 a3 b1 b2 b3 c1 c2 c3')
A=s.Matrix([[a1,xs[0],xs[1]],[0,a2,xs[2]],[0,0,a3]])
B=s.Matrix([[b1,xs[3],xs[4]],[0,b2,xs[5]],[0,0,b3]])
D=s.Matrix([[c1,xs[6],xs[7]],[0,c2,xs[8]],[0,0,c3]])
assert (A-a1*I)*(B-b2*I)*(D-c3*I)==s.zeros(3); C['symbolic_triple_identity']+=1
# Same ordered eigencharacters without triple constraint: lower-triangular extension.
A=s.diag(2,1,s.Rational(1,2)); B=s.Matrix([[3,0,0],[1,1,0],[0,0,s.Rational(1,3)]])
assert B.charpoly().as_expr()==s.diag(3,1,s.Rational(1,3)).charpoly().as_expr()
assert (B-3*I)*(A-I)*(A-s.Rational(1,2)*I)!=s.zeros(3); C['charpoly_only_counterexample']+=1
# Residual trace ambiguity at ell=5,e=1, and other primes/exponents.
for ell in list(s.primerange(5,100)):
 for e in range(1,ell):
  if 2*e%(ell-1)==0:continue
  eq=True
  for u in range(1,ell):
   q=pow(u,(ell-1)//2,ell); t=(pow(u,e,ell)+pow(u,-e,ell))%ell
   eq &= (q*t-t)%ell==0; C['quadratic_trace_residue_checks']+=1
  assert eq==(2*e%(ell-1)==(ell-1)//2)
  if eq:C['ambiguous_exponents']+=1
assert s.Rational(2)+s.Rational(1,2)!=-s.Rational(2)-s.Rational(1,2)
# Torsion trace ring: y=(1+x)+(1+x)^(-1)-2 = x^2/(1+x).
# Exact truncation over F_p; powers y^j have distinct leading degree 2j.
for p in (5,7,11):
 N=80; y=[0]*N
 for i in range(2,N): y[i]=(-1)**(i-2)%p
 a=[1]+[0]*(N-1)
 for j in range(1,40):
  a=[sum(a[k]*y[i-k] for k in range(i+1))%p for i in range(N)]
  assert next(i for i,v in enumerate(a) if v)==2*j and a[2*j]==1
  C['torsion_trace_leading_terms']+=1
print(dict(C));print('script_seconds',monotonic()-T)
