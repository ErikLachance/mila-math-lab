import numpy as np,sympy as s,mpmath as mp,random,sys,json,time,itertools as it
from pathlib import Path
from sympy.matrices.normalforms import hermite_normal_form as hnf
q=int(sys.argv[1]);start=time.monotonic();n=21;mp.mp.dps=100
f=Path(f'units_weight{q}.json');d=json.loads(f.read_text());g=json.loads(Path(f'smallgen{q}.json').read_text());M=[s.Matrix(a) for a in d['matrices']];one=s.Matrix(d['one']);T=s.kronecker_product(s.Matrix(g['old_power_to_new']),s.eye(3))*s.Matrix(d['basis']);x=s.symbols('x');P=s.Poly.from_list(g['poly'],x);C=s.Poly(x**3+x**2-2*x-1,x);roots=[mp.mpc(str(s.re(z)),str(s.im(z))) for z in P.nroots(n=85,maxsteps=1000) if s.im(z)>=0];cs=[mp.mpf(str(z)) for z in C.nroots(n=85)];rows=[]
for a in roots:
 for c in cs:
  row=[a**i*c**j for i in range(7) for j in range(3)];rows.append([mp.re(z)*(1 if not a.imag else mp.sqrt(2)) for z in row]);
  if a.imag:rows.append([mp.im(z)*mp.sqrt(2) for z in row])
E=mp.matrix(rows)*mp.matrix([[mp.mpf(int(z.p))/int(z.q) for z in row] for row in T.tolist()]);mats=np.array([m.tolist() for m in M],dtype=np.int64);assert np.max(np.abs(mats))<100
# weighted LLL only proposes candidates; exact integral norm/HNF verifies them.
units=d['units']; known={tuple(u[0]) for u in units};seen=set();cache={};count=0;coll=0;small=0;rng=random.Random(q+5000)
def add(v,why):
 v=tuple(map(int,v));v=min(v,tuple(-z for z in v));
 if v in known or tuple(-z for z in v) in known or list(v)==list(one) or list(-s.Matrix(v))==list(one):return
 A=sum((z*m for z,m in zip(v,M) if z),s.zeros(n)); norm=int(A.det(method='domain-ge'));assert abs(norm)==1
 known.add(v);units.append((list(v),norm,[]));print('unit',len(units),why,'maxcoeff',max(map(abs,v)),flush=True);save()
def save():
 d['units']=units;Path(f'units_wide{q}.json').write_text(json.dumps(d))
def test(v):
 global count,small,coll
 v=tuple(map(int,v));v=min(v,tuple(-z for z in v));
 if v in seen:return
 seen.add(v);count+=1
 A=sum((z*m for z,m in zip(v,M) if z),s.zeros(n));norm=abs(int(A.det(method='domain-ge')))
 if norm==1:add(v,'direct');return
 if norm==0 or norm>10**7:return
 small+=1;H=hnf(A);key=tuple(H)
 if key in cache:
  old=cache[key];w=old.inv()*s.Matrix(v);assert all(z.q==1 for z in w);coll+=1;add(w,f'ideal norm {norm}')
 else:cache[key]=A
rounds=0;limit=int(sys.argv[2]);
while time.monotonic()-start<limit:
 # log weights are sampled jointly across conjugate pairs (positive-definite real lattice).
 w=[rng.uniform(-6,6) for _ in range(12)];w += []
 a=w[:3]+[z for z in w[3:] for _ in range(2)];weights=[mp.exp(z) for z in a]
 A=s.Matrix([[int(mp.nint(E[j,i]*weights[j]*10**22)) for j in range(n)] for i in range(n)])
 try:L,U=A.lll_transform(delta=s.Rational(3,4));assert abs(U.det())==1 and L==U*A
 except (AssertionError,ValueError):continue
 rounds+=1
 for i in range(5):test(U.row(i))
 for i,j in it.combinations(range(5),2):
  test(U.row(i)+U.row(j));test(U.row(i)-U.row(j))
 if rounds%5==0:print('round',rounds,'tested',count,'small',small,'coll',coll,'units',len(units),'seconds',time.monotonic()-start,flush=True)
save();print('FINAL',rounds,count,small,coll,len(units),'seconds',time.monotonic()-start,flush=True)
