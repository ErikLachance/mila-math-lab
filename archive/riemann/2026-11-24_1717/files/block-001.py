from itertools import product
from collections import Counter
from fractions import Fraction as F
from time import monotonic
import sympy as s
T=monotonic(); C=Counter()
J=s.Matrix([[0,0,1],[0,1,0],[1,0,0]]); I=s.eye(3)
def sharp(A): return J*A.T*J
def tr(A): return s.trace(A)
a,b,c,d,e,f,g=s.symbols('a b c d e f g')
A=s.Matrix([[a,b,c],[d,e,b],[f,d,g]])
B=A-sharp(A); D=a-g
assert B==s.diag(D,0,-D)
P=[(B*B+D*B)/(2*D**2),I-B*B/D**2,(B*B-D*B)/(2*D**2)]
for i in range(3):
 for j in range(3):
  assert s.simplify(P[i]*P[j]-(P[i] if i==j else s.zeros(3)))==s.zeros(3)
  C['symbolic_projector_products']+=1
assert s.simplify(sum(P,s.zeros(3))-I)==s.zeros(3)
assert s.simplify(tr(B*B)/2-D**2)==0
X=s.Matrix(3,3,s.symbols('x:9')); Y=s.Matrix(3,3,s.symbols('y:9')); Z=s.Matrix(3,3,s.symbols('z:9'))
# For every primitive invariant weight pattern and choices of matrix entries,
# reflect entries as necessary to obtain a directed cycle.
for ws in [(0,),(1,-1),(2,-2),(1,1,-2),(-1,-1,2)]:
 slots=[[(i,j) for i,j in product(range(3),repeat=2) if j-i==w] for w in ws]
 for pairs in product(*slots):
  Ms=[X,Y,Z][:len(ws)]; want=s.prod(M[i,j] for M,(i,j) in zip(Ms,pairs))
  found=False
  for refl in product([0,1],repeat=len(ws)):
   ij=[(2-j,2-i) if r else (i,j) for (i,j),r in zip(pairs,refl)]
   if not all(ij[t][1]==ij[(t+1)%len(ws)][0] for t in range(len(ws))): continue
   expr=I
   for M,(i,j),r in zip(Ms,ij,refl): expr=expr*P[i]*(sharp(M) if r else M)
   assert s.simplify(tr(expr)-want)==0
   found=True; break
  assert found
  C['symbolic_invariant_monomials']+=1
# Exhaustive bounded exponent tests of the elementary Hilbert basis proof.
for u,v,w,z in product(range(13),repeat=4):
 if u+2*v!=w+2*z: continue
 m=min(u,w); u-=m; w-=m
 m=min(v,z); v-=m; z-=m
 assert (u==v==w==z==0) or (v==w==0 and u==2*z) or (u==z==0 and w==2*v)
 C['zero_weight_count_vectors']+=1
# Type II theta relation (symbolic), and two possible extensions on c.
p,q,r,t=s.symbols('p q r t'); U=s.Matrix([[p,q],[r,t]]); J2=s.Matrix([[0,1],[1,0]]); E=s.diag(1,-1)
assert s.simplify(J2*U.inv().T*J2-E*U*E/U.det())==s.zeros(2)
C['symbolic_corner_identity']+=1
# Negative control: drop g1 normalization, keep c normalization. A near-identity
# J-isometry conjugates a diagonal marked A to a non-normalized matrix.
N=s.Matrix([[0,1,0],[0,0,-1],[0,0,0]])
assert sharp(N)==-N and N**3==s.zeros(3)
for p0 in (5,7,11):
 R=I+p0*N+s.Rational(p0*p0,2)*N*N
 assert sharp(R)*R==I
 M=R*s.diag(2,1,s.Rational(1,2))*R.inv()
 assert M-sharp(M)!=s.diag(M[0,0]-M[2,2],0,M[2,2]-M[0,0])
 C['missing_normalization_negative_controls']+=1
# Saturated cotangent dual: size of Hom(O/pi^n,O/pi^k) is q^min(n,k).
# Direct counting of possible images of cyclic generator for small rings.
for p0,n,k in product((2,3,5),range(1,5),range(1,5)):
 count=sum((p0**n*x)%(p0**k)==0 for x in range(p0**k))
 assert count==p0**min(n,k)
 C['cyclic_dual_counts']+=1
# Marked g1 numerical arithmetic: primitive residue generator exists; the square
# is nontrivial for all exponents satisfying (ell-1) not dividing 2e.
for ell in list(s.primerange(3,150)):
 h=int(s.primitive_root(ell))
 for e0 in range(1,2*(ell-1)+1):
  if 2*e0%(ell-1)==0: continue
  for sign in (-1,1):
   assert pow(sign*pow(h,e0,ell),2,ell)!=1
   C['marked_residual_checks']+=1
print(dict(C)); print('script_seconds',monotonic()-T)
# Tangent normalization: [X,B] diagonal implies X offdiagonal zero when D!=0.
xx=s.Matrix(3,3,s.symbols('u:9')); comm=xx*B-B*xx
for i,j in product(range(3),repeat=2):
 if i!=j:
  assert s.simplify(comm[i,j]-(B[j,j]-B[i,i])*xx[i,j])==0
  assert B[j,j]-B[i,i] != 0
  C['tangent_offdiag_identities']+=1
# Type II off-diagonal adjoint decomposition.
Jalt=s.Matrix([[0,1],[-1,0]]); v=s.Matrix(s.symbols('v:2')); w=s.Matrix(1,2,s.symbols('w:2')); u=Jalt*w.T
vp=-J2*w.T; up=-Jalt*J2*v
assert vp==-E*u and up==-E*v
assert vp+up==-E*(v+u) and vp-up==E*(v-u)
assert s.simplify(Jalt*U.inv().T-U*Jalt/U.det())==s.zeros(2)
C['symbolic_typeII_offdiagonal_decomposition']+=1
print('final_counts',dict(C)); print('total_script_seconds',monotonic()-T)
