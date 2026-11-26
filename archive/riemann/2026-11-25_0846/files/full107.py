import re,json,itertools,time
from pathlib import Path
import numpy as np
import sympy as sy
start=time.monotonic()
p=7
I=np.eye(42,dtype=np.int64)
def h(*a):return np.hstack(a)%p
def rref(a):
 a=np.array(a,dtype=np.int64).copy()%p;i=0;piv=[]
 for j in range(a.shape[1]):
  idx=np.flatnonzero(a[i:,j]);
  if not len(idx):continue
  k=i+idx[0];a[[i,k]]=a[[k,i]];a[i]=a[i]*pow(int(a[i,j]),-1,p)%p
  c=a[:,j].copy();c[i]=0;a=(a-c[:,None]*a[i])%p
  piv.append(j);i+=1
  if i==a.shape[0]:break
 return a,piv
def rank(a):return len(rref(a)[1])
def base(a):return a[:,rref(a)[1]]
def null(a):
 b,piv=rref(a);free=[j for j in range(a.shape[1]) if j not in piv];r=np.zeros((a.shape[1],len(free)),dtype=np.int64)
 for i,j in enumerate(free):
  r[j,i]=1;r[piv,i]=-b[:len(piv),j]%p
 return r
def mp(a,k):return np.linalg.matrix_power(a,k)%p # k<=6, entries small
# exact product with mod reduction each step (avoid overflow in larger powers)
def mp(a,k):
 b=np.eye(a.shape[0],dtype=np.int64)
 for _ in range(k):b=b@a%p
 return b
def solve(a,b):
 aug,piv=rref(h(a,b));assert piv==list(range(a.shape[1]));return aug[:a.shape[1],-b.shape[1]:]
def proj(G,w):return sum((pow(w,-j,p)*mp(G,j) for j in range(6)),np.zeros_like(G))*6%p
# Arithmetic check independent of the large degree-12 class number: the degree-6 CM field F has real cubic class number 1.
# primitive odd characters eta,eta*omega^2,eta*omega^4 evaluated in Z[z]/(z^2+z+1).
z=sy.symbols('z');m=107*7
eta=lambda a:int(sy.legendre_symbol(a%107,107))
logs={pow(3,j,7):j for j in range(6)}
num0=sum(a*eta(a) for a in range(1,107))
num2=sy.rem(sum(a*eta(a)*z**(logs[a%7]%3) for a in range(1,m) if a%7 and a%107),z*z+z+1,z)
num4=sy.rem(num2.subs(z,z*z),z*z+z+1,z)
prod=sy.rem(num2*num4,z*z+z+1,z)
Bprod=sy.Rational(num0,107)*prod/m**2
print('F class factors',num0,num2,num4,prod,'B product',Bprod)
# Relative formula h^- = -Q*w/8 product B, w=2; unit index Q=1 or 2.
assert Bprod.is_Rational and Bprod<0
print('h_F candidates',[-Bprod*sy.Rational(q,4) for q in (1,2)])
# Fresh exact Frattini character computation for F via Kummer over L.
# even characters of L, omit trivial for units, add trivial for S-unit,
# omega torsion, theta class. For Hom character gamma, mirror omega/gamma.
chars=[(e,j) for e in (0,1) for j in range(6)]
kummer=[c for c in chars if sum(c)%2==0]+[(0,1),(1,2)]
from collections import Counter
cnt=Counter((e,(1-j)%6) for e,j in kummer)
assert {c:n for c,n in cnt.items() if c[1]%2==0}=={(0,0):1,(1,0):1,(1,2):1,(1,4):1}
print('Kummer dimensions F',[(c,cnt[c]) for c in chars if c[1]%2==0])
S0=np.roll(I,-6,axis=0)
results=[]
for fname in ['cert1.json','cert2.json']:
 cert=json.loads(Path(fname).read_text())
 V=np.array(cert['V'],dtype=np.int64).T;g=np.array(cert['G'],dtype=np.int64)
 G=np.zeros_like(I)
 # S0 sends slot i to i-1; both conventions yield same multiplier 3.
 for j in range(7):G[(3*j%7)*6:(3*j%7+1)*6,j*6:(j+1)*6]=g
 U=base(h(*[mp(S0,i)@V for i in range(7)]))
 assert rank(U)==20 and rank(h(U,G@U))==20 and rank(h(U,S0@U))==20
 assert np.array_equal(mp(G,6),I) and np.array_equal(G@S0%7,mp(S0,3)@G%7)
 local={w:np.vstack((null(g-w*np.eye(6,dtype=np.int64)),np.zeros((36,1),dtype=np.int64))) for w in range(1,7)}
 assert all(v.shape==(42,1) for v in local.values())
 for k in range(1,7):
  S=mp(S0,k);T=(S-I)%7;D=sum(((-1)**(j+1)*pow(j,-1,p)*mp(T,j) for j in range(1,7)),np.zeros_like(I))%p
  assert not np.any(mp(D,7)) and np.array_equal(G@D%7,3*D@G%7)
  R1=base(h(U,D));R3=base(h(U,mp(D,3)));R4=base(h(U,mp(D,4)))
  assert [rank(base(h(U,mp(D,i)))) for i in range(1,8)]==[38,35,32,29,26,23,20]
  # Recover the weight-theta fixed line directly in full quotient, rather than M4 preimage.
  K=null(h(D,-U))[:42];K=proj(G,3)@K%p
  X0=next(K[:,i:i+1] for i in range(K.shape[1]) if rank(h(R1,K[:,i:i+1]))==39)
  assert rank(h(U,D@X0))==20 and rank(h(U,G@X0-3*X0))==20
  for l in range(7):
   Sl=mp(S0,l);G_l=Sl@G@mp(S0,(-l)%7)%p
   ys={w:Sl@v%p for w,v in local.items()}
   basis=h(X0,*[mp(D,j)@ys[w] for w in (1,6,5) for j in range(7)])
   assert rank(h(U,basis))==42
   weights=[3]+[w*pow(3,j,7)%7 for w in (1,6,5) for j in range(7)]
   assert rank(h(U,G_l@basis-basis*np.array(weights)))==20
   d1=mp(D,1)@ys[1]%7;d2=mp(D,2)@ys[5]%7
   b3=h(R3,X0,d1,d2);assert rank(b3)==35
   c=solve(b3,ys[3])[-3:,0];assert c[0] and c[2] and not np.any((b3@solve(b3,ys[3])-ys[3])%7)
   b4=h(R4,mp(D,2)@ys[1],mp(D,3)@ys[5]);assert rank(b4)==31
   e=solve(b4,ys[2])[-2:,0];assert not np.any((b4@solve(b4,ys[2])-ys[2])%7)
   
   full=h(U,basis);assert rank(full)==42
   # for each local eigenline, expand in full module, verify exact residual
   ex={}
   for w in range(1,7):
    cf=solve(full,ys[w])[-22:,0];assert not np.any((full@solve(full,ys[w])-ys[w])%7)
    assert all(not cc or weights[j]==w for j,cc in enumerate(cf))
    ex[w]=[(('X0' if j==0 else f'D^{(j-1)%7}y{(1,6,5)[(j-1)//7]}'),int(cc)) for j,cc in enumerate(cf) if cc]
   results.append((fname,k,l,c.tolist(),e.tolist(),ex))
 print(fname,'checked 42 simultaneous generator/place choices')
print('total cases',len(results),'elapsed',time.monotonic()-start)
Path('/mnt/data/riemann_0846/full_report.json').write_text(json.dumps(results,indent=2))

