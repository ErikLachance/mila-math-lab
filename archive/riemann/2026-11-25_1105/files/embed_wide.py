from order7 import *
q=int(sys.argv[1])
import json,itertools,math
# R=Z_7[pi,t], pi^3=7pi^2-14pi+7, t^2=-107.
import os
N=7**int(os.getenv("PREC","5"));Z=(0,)*6;one=(1,0,0,0,0,0);pi=(0,1,0,0,0,0);tt=(0,0,0,1,0,0)
def add(a,b):return tuple((x+y)%N for x,y in zip(a,b))
def sc(a,k):return tuple(x*k%N for x in a)
def sub(a,b):return add(a,sc(b,-1))
def mul(a,b):
 c=[[0]*5 for _ in range(2)]
 for i,x in enumerate(a):
  if not x:continue
  for j,y in enumerate(b):
   if y:c[(i//3+j//3)%2][i%3+j%3]+=x*y*(-q if i//3+j//3==2 else 1)
 for v in c:
  for k in (4,3):
   z=v[k];v[k-3]+=7*z;v[k-2]-=14*z;v[k-1]+=7*z
 return tuple(x%N for v in c for x in v[:3])
def pw(a,k):
 b=one
 while k:
  if k&1:b=mul(b,a)
  k//=2
  if k:a=mul(a,a)
 return b
def divpi(a):
 if a[0]%7 or a[3]%7:raise ValueError('not divisible')
 out=[]
 for i in (0,3):
  q=a[i]//7;out.extend([(a[i+1]+14*q)%N,(a[i+2]-7*q)%N,q])
 return tuple(out)
def divpis(a,k):
 for i in range(k):a=divpi(a)
 return a
def valatleast(a,k):
 try:divpis(a,k);return True
 except ValueError:return False
def ev(co,a):
 r=Z
 for b in reversed(co):r=add(mul(r,a),b)
 return r
r=json.load(open(f'/mnt/data/riemann_1105/smallgen{q}.json'));poly=r['poly'][::-1];co=[sc(one,a) for a in poly];digits=[(a,0,0,b,0,0) for a,b in itertools.product(range(7),repeat=2)];res=[d for d in digits if valatleast(ev(co,d),1)];print('residue roots',res)
# For double/triple roots use translated polynomial / pi^3 and lift simple roots.
def lift(co,a,kmax):
 for k in range(1,kmax):
  cand=[add(a,mul(pw(pi,k),d)) for d in digits];valid=[b for b in cand if valatleast(ev(co,b),k+1)]
  assert len(valid)==1,(k,len(valid),a)
  a=valid[0]
 return a
roots=[]
for a in res:
 if not valatleast(ev([sc(one,i*poly[i]) for i in range(1,8)],a),1):roots.append(lift(co,a,int(os.getenv("LIFT","10"))));continue
 cc=[]
 for k in range(8):
  t=Z
  for j in range(k,8):t=add(t,sc(pw(a,j-k),poly[j]*math.comb(j,k)))
  cc.append(divpis(mul(pw(pi,k),t),3))
 ys=[d for d in digits if valatleast(ev(cc,d),1)];print('translated residue roots',len(ys));assert len(ys)==3
 for y in ys:roots.append(add(a,mul(pi,lift(cc,y,int(os.getenv("LIFT","10"))-1))))
assert len(roots)==7 and all(valatleast(ev(co,a),10) for a in roots)
# delta: c -> c^2-2, t -> -t.  pi -> 4pi-pi^2.
pi2=add(sc(pi,4),sc(pw(pi,2),-1))
def delta(a):
 r=Z
 for i,b in enumerate(a):r=add(r,sc(mul(pw(pi2,i%3),pw(tt,i//3)),b*(-1 if i//3 else 1)))
 return r
fixed=[a for a in roots if valatleast(sub(delta(a),a),8)];assert len(fixed)==1
rr=[None]*7;rr[0]=fixed[0];rr[1]=[a for a in roots if a!=rr[0]][int(os.getenv("ROOT_CHOICE","0"))];idx=1
for _ in range(5):
 b=delta(rr[idx]);idx=idx*3%7;matches=[a for a in roots if valatleast(sub(a,b),8)];assert len(matches)==1;rr[idx]=matches[0]
assert len(set(rr))==7 and all(valatleast(sub(delta(rr[i]),rr[3*i%7]),8) for i in range(7));print('roots labeled',rr)
# Evaluate units in local field at all 7 embeddings with rational coeffs.
u=json.load(open(f'/mnt/data/riemann_1105/units_wide{q}.json'));T=s.Matrix([[s.Rational(a) for a in row] for row in u['basis']]);A=s.Matrix([[s.Rational(a) for a in row] for row in r['old_power_to_new']]);T=s.kronecker_product(A,s.eye(3))*T;c=sub(sc(one,2),pi)
def evalrat(v,a):
 den=s.ilcm(*[x.q for x in v]);den=int(den);d=den;vp=0
 while d%7==0:vp+=1;d//=7
 assert vp<=1, vp
 b=Z
 for i,x in enumerate(v):b=add(b,sc(mul(pw(a,i//3),pw(c,i%3)),int(x*den)))
 assert all(x%7**vp==0 for x in b)
 return tuple((x//7**vp*pow(d,-1,N))%N for x in b)
def classvec(a):
 assert a[0]%7==a[3]%7==0
 return s.Matrix([a[0]//7%7,a[1]%7,a[2]%7,a[3]//7%7,a[4]%7,a[5]%7])
def log(a):
 h=sub(pw(a,48),one);assert valatleast(h,1)
 return add(sub(h,sc(pw(h,2),pow(2,-1,N))),sc(pw(h,3),pow(3,-1,N)))
V=[]
for j,(v,norm,logs) in enumerate(u['units']):
 v=T*s.Matrix(v);aa=[evalrat(v,a) for a in rr];vv=s.Matrix.vstack(*[classvec(log(a)) for a in aa]);V.append(vv)
 # products of embeddings over B must equal unit norm over cubic, checked later via conjugates c automorphism
print('embedded unit count',len(V))
def mod(M):return M.applyfunc(lambda z:int(z)%7)
def rank(M):return M.cols-nullmod(M,7).cols
def shift(v):return s.Matrix.vstack(*[v[6*((i+1)%7):6*((i+1)%7)+6,0] for i in range(7)])
I=s.eye(42);S=s.Matrix.hstack(*[shift(I[:,i]) for i in range(42)]);T0=S-I;D=mod(sum((pow(k,-1,7)*(-1)**(k+1)*T0**k for k in range(1,7)),s.zeros(42)))
U=mod(s.Matrix.hstack(*[S**i*v for v in V for i in range(7)])); print('unit span rank',rank(U)); print('ranks D^i',[rank(U.row_join(D**i)) for i in range(1,8)])
locbasis=[sc(one,7),pi,pw(pi,2),sc(tt,7),mul(tt,pi),mul(tt,pw(pi,2))];G=s.Matrix.hstack(*[classvec(delta(a)) for a in locbasis]);assert mod(G**6)==s.eye(6)
GG=s.zeros(42)
for i in range(7):GG[6*i:6*i+6,6*((5*i)%7):6*((5*i)%7)+6]=G
print('covariant span closure rank',rank(U.row_join(mod(GG*U))));assert mod(GG*S-S**3*GG)==s.zeros(42)
json.dump({'V':[list(map(int,v)) for v in V],'G':[[int(z)%7 for z in row] for row in G.tolist()]},open(f'/mnt/data/riemann_1105/partial_cert{q}_{os.getenv("PREC","5")}.json','w'))
