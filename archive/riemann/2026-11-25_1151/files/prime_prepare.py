import numpy as np,sympy as s,mpmath as mp,random,sys,json,time,itertools as it,math,os
from fractions import Fraction as F
from pathlib import Path
from sympy.matrices.normalforms import hermite_normal_form as hnf
q=int(sys.argv[1]);start=time.monotonic();n=21;mp.mp.dps=100
f=Path(f'units_wide{q}.json');d=json.loads(f.read_text());g=json.loads(Path(f'smallgen{q}.json').read_text());M=[s.Matrix(a) for a in d['matrices']];one=s.Matrix(d['one']);T=s.kronecker_product(s.Matrix(g['old_power_to_new']),s.eye(3))*s.Matrix(d['basis']);x=s.symbols('x');P=s.Poly.from_list(g['poly'],x);C=s.Poly(x**3+x**2-2*x-1,x);roots=[mp.mpc(str(s.re(z)),str(s.im(z))) for z in P.nroots(n=85,maxsteps=1000) if s.im(z)>=0];cs=[mp.mpf(str(z)) for z in C.nroots(n=85)];rows=[]
for a in roots:
 for c in cs:
  row=[a**i*c**j for i in range(7) for j in range(3)];rows.append([mp.re(z)*(1 if not a.imag else mp.sqrt(2)) for z in row]);
  if a.imag:rows.append([mp.im(z)*mp.sqrt(2) for z in row])
E=mp.matrix(rows)*mp.matrix([[mp.mpf(int(z.p))/int(z.q) for z in row] for row in T.tolist()]);mats=np.array([m.tolist() for m in M],dtype=np.int64);assert np.max(np.abs(mats))<100
I=s.eye(n); on=np.array(one,dtype=np.int64).ravel();units=d['units'];known={tuple(u[0]) for u in units};seen=set();count=0;small=0;rels=0;skipped=0;primecache={};powercache={};pivot={};history=[];cert=[];rng=random.Random(q+10000)
def mat(v):return sum((int(z)*m for z,m in zip(v,M) if z),s.zeros(n))
def mm(v):return np.tensordot(v,mats,axes=1)
def mul(a,b,p):return mm(a)@b%p
def powv(a,k,p):
 b=on.copy()
 while k:
  if k&1:b=mul(b,a,p)
  k//=2
  if k:a=mul(a,a,p)
 return b

def rref(A,p):
 A=A.copy()%p;r=0; piv=[]
 for j in range(A.shape[1]):
  if r==len(A):break
  ids=np.flatnonzero(A[r:,j]);
  if not len(ids):continue
  k=int(ids[0])+r;A[[r,k]]=A[[k,r]];A[r]=A[r]*pow(int(A[r,j]),-1,p)%p
  a=A[:,j].copy();a[r]=0;A=(A-a[:,None]*A[r])%p;piv.append(j);r+=1
 return A,piv

def primeparts(p):
 if p in primecache:return primecache[p]
 assert p not in (7,q)
 eye=np.eye(n,dtype=np.int64);Frob=np.column_stack([powv(e,p,p) for e in eye]);R,pi=rref(Frob-eye,p);fixed=[]
 for j in range(n):
  if j in pi:continue
  v=eye[j].copy()
  for i,k in enumerate(pi):v[k]=-R[i,j]%p
  fixed.append(v)
 es=[on.copy()]
 for a in fixed:
  if len(es)==len(fixed):break
  parts=[(on-powv((a-r*on)%p,p-1,p))%p for r in range(p)];parts=[v for v in parts if np.any(v)]
  es=[w for e in es for v in parts if np.any(w:=mul(e,v,p))]
 assert len(es)==len(fixed) and np.all(sum(es)%p==on%p)
 for i,e in enumerate(es):
  assert np.array_equal(mul(e,e,p),e)
  assert all(not np.any(mul(e,b,p)) for b in es[:i])
 out=[]
 for i,e in enumerate(es):
  deg=len(rref(mm(e),p)[1]);B=mat((on-e)%p);H=hnf((p*I).row_join(B));assert abs(int(H.det()))==p**deg
  out.append((deg,B,H))
 assert sum(z[0] for z in out)==n
 primecache[p]=out;print('prime',p,'residue degrees',[a[0] for a in out],flush=True);return out

def valuation(v,p,i,kmax,B,H):
 # membership in P^k via (p^k, b^k) for P=(p,b), unramified p.
 for k in range(1,kmax+1):
  key=(p,i,k)
  if key not in powercache:
   h=H if k==1 else hnf((p**k*I).row_join(B**k));assert abs(int(h.det()))==p**(k*primecache[p][i][0]);powercache[key]=h.inv()
  if any(z.q!=1 for z in powercache[key]*v):return k-1
 return kmax

def factors(v,A,norm):
 out={}
 for p,e in s.factorint(norm).items():
  p=int(p);e=int(e)
  if p<=97 and p not in (7,q):
   total=0
   for i,(deg,B,H) in enumerate(primeparts(p)):
    if deg>e:continue
    k=valuation(v,p,i,e//deg,B,H);total+=k*deg
    if k:out[('prime',p,i)]=k
   assert total==e,(p,e,total)
  else:
   H=hnf((p**e*I).row_join(A));assert abs(int(H.det()))==p**e
   out[('primary',p,tuple(H))]=1
 return out

def add(v,why,rel=None):
 v=tuple(map(int,v));v=min(v,tuple(-z for z in v));
 if v in known or tuple(-z for z in v) in known or list(v)==list(one) or list(-s.Matrix(v))==list(one):return
 A=mat(v);norm=int(A.det(method='domain-ge'));assert abs(norm)==1
 known.add(v);units.append((list(v),norm,[]));cert.append({'unit':list(v),'norm':norm,'why':why,'relation':rel});print('unit',len(units),why,'maxcoeff',max(map(abs,v)),flush=True)

def save():
 d['units']=units;Path(f'units_rel{q}.json').write_text(json.dumps(d));Path(f'relations{q}.json').write_text(json.dumps(cert))
def axpy(a,b,c):
 for k,v in b.items():
  w=a.get(k,F(0))+c*v
  if w:a[k]=w
  else:a.pop(k,None)

def relation(v,A,norm,fac):
 global rels,skipped
 j=len(history);history.append((v,A,norm));r={k:F(z) for k,z in fac.items()};w={j:F(1)}
 while r:
  k=min(r);a=r[k]
  if k not in pivot:
   pivot[k]=({k:z/a for k,z in r.items()},{k:z/a for k,z in w.items()});return
  u,b=pivot[k];axpy(r,u,-a);axpy(w,b,-a)
 rels+=1;l=math.lcm(*(z.denominator for z in w.values()));co={j:int(z*l) for j,z in w.items()};g=math.gcd(*co.values());co={j:z//g for j,z in co.items()}
 if sum(map(abs,co.values()))>80:skipped+=1;return
 # Check product of absolute norms as a separate necessary condition.
 assert math.prod(history[j][2]**z for j,z in co.items() if z>0)==math.prod(history[j][2]**(-z) for j,z in co.items() if z<0)
 a=one;b=one
 for j,z in co.items():
  v,A,N=history[j]
  if z>0:a=A**z*a
  else:b=A**(-z)*b
 B=mat(b);u=B.inv()*a;assert all(z.q==1 for z in u) and B*u==a
 add(u,f'factor relation {len(co)} terms',[(list(map(int,history[j][0])),z,history[j][2]) for j,z in co.items()])

def test(v):
 global count,small
 v=tuple(map(int,v));v=min(v,tuple(-z for z in v));
 if v in seen:return
 seen.add(v);count+=1
 A=mat(v);norm=abs(int(A.det(method='domain-ge')))
 if norm==1:add(v,'direct');return
 if norm==0 or norm>10**8:return
 small+=1;fac=factors(s.Matrix(v),A,norm);relation(s.Matrix(v),A,norm,fac)

def reduce(H,w):
 a=w[:3]+[z for z in w[3:] for _ in range(2)];weights=[mp.exp(z) for z in a];EH=E*mp.matrix(H.tolist());A=s.Matrix([[int(mp.nint(EH[j,i]*weights[j]*10**22)) for j in range(n)] for i in range(n)])
 try:L,U=A.lll_transform(delta=s.Rational(3,4));assert abs(U.det())==1 and L==U*A
 except (AssertionError,ValueError):return
 V=H*U.T
 for i in range(6):test(V[:,i])
 for i,j in it.combinations(range(6),2):
  test(V[:,i]+V[:,j]);test(V[:,i]-V[:,j])

# Persist idempotent decompositions once for later batches.
import pickle
cachefile=Path(f'primeparts{q}.pkl')
if cachefile.exists():primecache.update(pickle.loads(cachefile.read_bytes()))
targets=[I]
for p in [2,3,5,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]:
 for deg,B,H in primeparts(p):
  if deg<=2 and p**deg<=1000:targets.append(H)
 cachefile.write_bytes(pickle.dumps(primecache))
print('target ideals',len(targets),flush=True)
