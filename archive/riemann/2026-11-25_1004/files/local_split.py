import numpy as np, sympy as s, math,sys,time
from itertools import product
start=time.monotonic()
for q0 in map(int,sys.argv[1:]):
 N=7*q0;res={i*i%q0 for i in range(1,q0)};eta=lambda a:1 if a%q0 in res else -1
 H=[a for a in range(1,N) if math.gcd(a,N)==1 and (a%7,eta(a)) in [(1,1),(6,-1)]]
 g=2; C=[[(pow(g,j,N)*a)%N for a in H] for j in range(6)]; assert len(set(sum(C,[])))==6*(q0-1)
 ex=[4,1,0,2,5,6];e=[1,-2,-3,-1,2,3];assert all((e[(l-1)%6]-3*e[l])%7==0 for l in range(6));assert all(e[j]+e[j+3]==0 for j in range(3))
 # Witness nontrivial Kummer class in full cyclotomic field
 for k in range(1,100):
  ell=k*N+1
  if not s.isprime(ell):continue
  z=pow(int(s.primitive_root(ell)),k,ell)
  us=[math.prod((1-pow(z,a,ell))%ell for a in c)%ell for c in C]
  al=math.prod(pow(u,v,ell) for u,v in zip(us,e))%ell
  w=pow(al,(ell-1)//7,ell)
  if w!=1:break
 assert w!=1
 print('q',q0,'witness prime',ell,'alpha power',w,flush=True)
 mod=49;v=np.zeros(N,dtype=np.int64);v[0]=1
 for j in range(6):
  for a in C[j]*ex[j]:v=(v-np.roll(v,a))%mod
 def mul(a,b):
  c=np.convolve(a,b);c[:N-1]+=c[N:];return c[:N]%mod
 def power(a,n):
  b=np.zeros(N,dtype=np.int64);b[0]=1
  while n:
   if n&1:b=mul(b,a)
   n//=2
   if n:a=mul(a,a)
  return b
 def reduce_pi(w):
  mat=np.zeros((q0,7),dtype=np.int64); iq=pow(7,-1,q0);i7=pow(q0,-1,7)
  assert (iq*7+i7*q0)%N==1
  for j,k in enumerate(w):mat[iq*j%q0,i7*j%7]=k
  mat[:q0-1,:]-=mat[q0-1,:];mat=mat[:q0-1,:];mat[:,:6]-=mat[:,6,None];mat=mat[:,:6]%mod
  pi=np.zeros_like(mat)
  for j in range(6):
   for k in range(j+1):pi[:,k]+=math.comb(j,k)*mat[:,j]
  return pi%mod
 def val(pi):return min((j+(6 if n%7==0 else 0) for i,j in product(range(q0-1),range(6)) if (n:=pi[i,j])!=0),default=12)
 al48=power(v,48);w=al48.copy();w[0]=(w[0]-1)%mod;pi=reduce_pi(w);vv=val(pi);print('initial valuation lower bound across factors',vv,flush=True);assert vv>=7 and not np.any(pi%7)
 c=(-pi[:,1]//7)%7
 def frob(a):
  b=np.zeros(q0,dtype=np.int64)
  for i,x in enumerate(a):b[7*i%q0]=x
  return (b[:q0-1]-b[q0-1])%7
 assert np.array_equal(frob(c),(-c)%7)
 a=(-4*c)%7;assert np.array_equal((frob(a)-a)%7,c)
 y=np.zeros(N,dtype=np.int64);y[0]=1
 for i,x in enumerate(a):y[(7*i+q0)%N]+=x;y[7*i%N]-=x
 pi=reduce_pi((al48-power(y%49,7))%49);vv=val(pi);print('corrected valuation lower bound',vv,'ord_q(7)',s.n_order(7,q0),'q-1 prime to7?',(q0-1)%7!=0,'elapsed',time.monotonic()-start,flush=True);assert vv>=8 and (q0-1)%7!=0
