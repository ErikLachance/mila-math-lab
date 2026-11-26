import numpy as np
import sympy as s
from itertools import product
from time import monotonic
start=monotonic(); p=7
# finite matrix arithmetic
I=np.eye(3,dtype=np.int64); Z=np.zeros_like(I)
def E(i,j,n=3):
 a=np.zeros((n,n),dtype=np.int64);a[i,j]=1;return a
U=E(0,1)+E(1,2); L=E(2,0); V=E(0,2)
def comm(x,y):return (x@y-y@x)%7
n=0
for a,b,c,e,v in product(range(1,7),range(1,7),range(1,7),range(7),range(7)):
 X=a*L+b*U;q=a*b*b%7
 assert np.array_equal(np.linalg.matrix_power(X,7)%7,q*q*X%7)
 B=comm(X,comm(X,V));assert np.array_equal(B,(a*b*U-2*a*a*L)%7)
 J=(c*q*q*X+e*v*B)%7
 good=J[2,0]==0
 assert good == ((c*q*q-2*e*v*a)%7==0)
 if good:
  assert e and v and np.array_equal(J,(3*c*q*q*b*4*U)%7)
 n+=1
print('local theta coefficient cases',n)
# j=2: x^7 vanishes mod t^5; the same coefficient is forced zero.
j2=0
for a,b,v,e in product(range(1,7),range(1,7),range(1,7),range(7)):
 X=a*L+b*U;J=e*v*comm(X,comm(X,V))%7
 assert (J[2,0]==0)==(e==0)
 j2+=1
print('j2 necessary e=0 cases',j2)
# tame fixed inertia: all upper unipotent coefficients in each degree independent.
D=np.diag([2,1,4]);Di=np.diag([4,1,2]);fixed=0
for a,b,c in product(range(7),repeat=3):
 W=I+a*E(0,1)+b*E(0,2)+c*E(1,2)
 if np.array_equal(D@W@Di%7,W):fixed+=1;assert a==b==c==0
assert fixed==1;print('tame fixed matrices',fixed,'of',7**3)
# UT4 selector: explicit cyclic semidirect product of order 7^4.
I4=np.eye(4,dtype=np.int64);A=I4+E(0,1,4)+E(1,2,4)
Ai=np.linalg.matrix_power(A,6)%7;B=E(2,3,4)
assert np.array_equal(np.linalg.matrix_power(A,7)%7,I4)
T=lambda W:(A@W@Ai-W)%7
assert np.array_equal(T(T(B)),E(0,3,4));assert not np.any(T(T(T(B))))
assert not np.any(sum((np.linalg.matrix_power(A,k)@B@np.linalg.matrix_power(Ai,k) for k in range(7)))%7)
words=set()
for k,u,v,w in product(range(7),repeat=4):
 M=np.linalg.matrix_power(A,k)@(I4+u*B+v*T(B)+w*T(T(B)))%7
 words.add(tuple(M.ravel()));assert np.array_equal(np.linalg.matrix_power(M,7)%7,I4)
assert len(words)==2401;print('UT4 quotient distinct words',len(words))
# Field and independent local unit computation
z,x,t=s.symbols('z x t');f=z**3+z**2-2*z-1
P=s.resultant(f,(x-z)**2+79,z);print('field polynomial',P)
assert s.discriminant(f,z)==49 and f.subs(z,2)==7
assert s.factor(P,modulus=7)==(x**2+3*x-1)**3
assert s.legendre_symbol(-79,7)==-1
vec=[]
for a in (z,z*z-2):
 assert s.resultant(f,a,z)==1
 r=s.rem(a**48,f,z,domain=s.GF(7)); h=s.Poly(r.subs(z,t+2)-1,t,modulus=7).as_expr()
 log=s.Poly(s.rem(h-4*h*h,t**3,t,domain=s.GF(7)),t,modulus=7)
 vec.append([int(log.nth(1))%7,int(log.nth(2))%7])
assert vec==[[3,1],[5,5]];assert int(s.Matrix(vec).det())%7==3
# all 49 linear combinations, multiplicatively in the truncated real residue ring
out=set()
r=[s.rem(a**48,f,z,domain=s.GF(7)) for a in (z,z*z-2)]
for i,j in product(range(7),repeat=2):
 v=s.Poly(s.rem(r[0]**i*r[1]**j,f,z,domain=s.GF(7)),z,modulus=7)
 out.add(tuple(int(v.nth(k))%7 for k in range(3)))
assert len(out)==49
print('local unit log vectors',vec,'det=3; distinct unit combinations',len(out))
print('elapsed script seconds',round(monotonic()-start,4))

