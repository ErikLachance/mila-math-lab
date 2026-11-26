from math import gcd
from time import monotonic
from itertools import product
import sympy as s
start=monotonic(); N=553; p=7; g=5
eta=lambda a: int(s.legendre_symbol(a%79,79))
H=[a for a in range(1,N) if gcd(a,N)==1 and (a%7,eta(a)) in [(1,1),(6,-1)]]
assert len(H)==78 and eta(g)==1
C=[[(pow(g,j,N)*a)%N for a in H] for j in range(6)]
assert len(set(sum(C,[])))==468
r=pow(g,5,7); assert r==3
ex=[pow(pow(r,-1,7),j,7) for j in range(6)]
assert ex==[1,5,4,6,2,3] and all(ex[j]+ex[(j+3)%6]==7 for j in range(6))
ex=[4,1,0,2,5,6] # signed [1,-2,-3,-1,2,3] plus 3; same Kummer class
factors=[a for j in range(6) for a in C[j]*ex[j]]
# integer group ring Z[C553]; evaluation at zeta is ring homomorphism
v=[1]+[0]*(N-1)
ram=[(6 if a%7==0 else -1)*(78 if a%79==0 else -1) for a in range(N)]
tr=[]
for k in range(1,4):
 for a in factors:
  w=v[-a:]+v[:-a];v=[x-y for x,y in zip(v,w)]
 t=sum(x*y for x,y in zip(v,ram)); assert t%78==0
 tr.append(t//78)
print('trace alpha powers:',tr)
P1=tr[0];P2=tr[1]+6;P3=tr[2]+3*tr[0]
assert (P1**2-P2)%2==0
c2=(P1**2-P2)//2
assert (P3-P1*P2+c2*P1)%3==0
c3=(P3-P1*P2+c2*P1)//3
z=s.symbols('z'); Q=z**3-P1*z*z+c2*z-c3
print('cubic Q:',Q);print('digits',*[len(str(abs(x))) for x in [P1,c2,c3]])
assert s.Poly(Q,z).is_irreducible
# independent modular checks, six conjugate evaluations at primes 1 mod 553
for q in (1107,2213,3319,4425,6637,7743,11061,13273,16591):
 if not s.isprime(q):continue
 gg=int(s.primitive_root(q)); zz=pow(gg,(q-1)//N,q)
 us=[]
 for j in range(6):
  prod0=1
  for a in C[j]:prod0=prod0*(1-pow(zz,a,q))%q
  us.append(prod0)
 al=[]
 for k in range(6):
  prod0=1
  for j in range(6):prod0=prod0*pow(us[(j+k)%6],ex[j],q)%q
  al.append(prod0)
 assert all(al[j]*al[(j+3)%6]%q==1 for j in range(6))
 assert all(sum(pow(x,k,q) for x in al)%q==tr[k-1]%q for k in range(1,4))
 roots=[(x+pow(x,-1,q))%q for x in al[:3]]
 assert s.Poly(s.prod(z-x for x in roots)-Q,z,modulus=q).is_zero
 if q==3319:
  print('q3319 alphas:',al,'powers:',[pow(x,(q-1)//7,q) for x in al]); assert pow(al[0],(q-1)//7,q)!=1
 print('independent prime check',q)
# local seventh power test in unramified degree39 extension Q7(zeta79) (ord79(7)=?)
print('ord79(7)',s.n_order(7,79))
print('P7 cubic composition defines degree21 field',s.expand(Q.subs(z,z**7-7*z**5+14*z**3-7*z)).as_poly().degree())
print('elapsed',monotonic()-start)
# Independent local splitting certificate, exact ring mod 49.
# Full cyclotomic extension at 7 has unramified zeta79 part, deg78;
# each element reduced to basis zeta79^i*(zeta7-1)^j, i<78,j<6.
import numpy as np
from math import comb
m=49
v=np.zeros(N,dtype=np.int64);v[0]=1
for a in factors:v=(v-np.roll(v,a))%m
def mul(a,b):
 c=np.convolve(a,b); c[:N-1]+=c[N:]; return c[:N]%m
def power(a,n):
 b=np.zeros(N,dtype=np.int64);b[0]=1
 while n:
  if n&1:b=mul(b,a)
  a=mul(a,a);n//=2
 return b
# residue F49 in L; therefore 48 power removes residue.
w=power(v,48);w[0]=(w[0]-1)%m
mat=np.zeros((79,7),dtype=np.int64)
for a,k in enumerate(w):mat[34*a%79,4*a%7]=k
mat[:78,:]-=mat[78,:];mat=mat[:78,:];mat[:,:6]-=mat[:,6,None];mat=mat[:,:6]%m
pi=np.zeros_like(mat)
for j in range(6):
 for k in range(j+1):pi[:,k]+=comb(j,k)*mat[:,j]
pi%=m
minval=min((j+(6 if n%7==0 else 0) for i,j in product(range(78),range(6)) if (n:=pi[i,j])!=0),default=12)
print('local min valuation alpha^48-1 (mod pi^12):',minval)
print('nonzero coefficient counts by pi exponent:',np.count_nonzero(pi,axis=0).tolist())
# U1^7 can start at valuation 7. Correct the insufficient U8 test.
assert minval>=7 and all(n%7==0 for n in pi.ravel())
c=(-pi[:,1]//7)%7 # 7/pi^6=-1 mod pi
# residue of alpha^48-1 divided by pi^7, with basis zeta79.
def frob(a):
 b=np.zeros(79,dtype=np.int64)
 for i,x in enumerate(a):b[7*i%79]=x
 return (b[:78]-b[78])%7
assert np.array_equal(frob(c),(-c)%7)
a=(-4*c)%7 # a^7-a=c when c^7=-c
assert np.array_equal((frob(a)-a)%7,c)
y=np.zeros(N,dtype=np.int64);y[0]=1
for i,x in enumerate(a):
 y[(7*i+79)%N]+=x;y[7*i%N]-=x
w=(power(v,48)-power(y%49,7))%49
mat=np.zeros((79,7),dtype=np.int64)
for j,k in enumerate(w):mat[34*j%79,4*j%7]=k
mat[:78,:]-=mat[78,:];mat=mat[:78,:];mat[:,:6]-=mat[:,6,None];mat=mat[:,:6]%49
pi=np.zeros_like(mat)
for j in range(6):
 for k in range(j+1):pi[:,k]+=comb(j,k)*mat[:,j]
pi%=49
minval=min((j+(6 if n%7==0 else 0) for i,j in product(range(78),range(6)) if (n:=pi[i,j])!=0),default=12)
print('corrected valuation alpha^48-y^7:',minval)
assert minval>=8
print('certified split: U8=U2^7, gcd(48,7)=1 and local extension degree39 prime to7')
# Find small rational primes split in F but inert at every prime in E/F.
from math import lcm
for q in list(s.primerange(2,150)):
 if q in (7,79) or q%7 not in (1,6) or eta(q)!=1:continue
 m=int(q); v=np.zeros(N,dtype=np.int64);v[0]=1
 for a in factors:v=(v-np.roll(v,a))%m
 f=lcm(int(s.n_order(q,7)),int(s.n_order(q,79)))
 w=power(v,(q**f-1)//7);w[0]=(w[0]-1)%m
 mat=np.zeros((79,7),dtype=np.int64)
 for i,k in enumerate(w):mat[34*i%79,4*i%7]=k
 mat[:78,:]-=mat[78,:];mat=mat[:78,:];mat[:,:6]-=mat[:,6,None]
 nontriv=bool(np.any(mat[:,:6]%m))
 print('q split F',q,'residue degree in M',f,'Frobenius nontrivial?',nontriv)

