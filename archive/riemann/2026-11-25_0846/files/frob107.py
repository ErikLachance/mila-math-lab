from order107 import *
import mpmath as mp,itertools,json
mp.mp.dps=90
B,M,one,d=saturate(structure(P),[7,107,373599001,47447980890086283233],s.eye(7)[:,0]);roots=P.nroots(n=75,maxsteps=500);roots=[mp.mpc(str(s.re(z)),str(s.im(z))) for z in roots if s.im(z)>=0]
rows=[]
for a in roots:
 row=[a**i for i in range(7)];rows.append([mp.re(z)*(1 if a.imag==0 else mp.sqrt(2)) for z in row])
 if a.imag!=0:rows.append([mp.im(z)*mp.sqrt(2) for z in row])
E=mp.matrix(rows)*mp.matrix([[mp.mpf(str(v.p))/int(v.q) for v in row] for row in B.tolist()]);scale=10**30
A=s.Matrix([[int(mp.nint(E[j,i]*scale)) for j in range(7)] for i in range(7)]);LL,U=A.lll_transform();assert abs(U.det())==1
M=change(M,U.T);one=U.T.inv()*one;B=B*U.T
r=json.load(open('riemann_smallgen_run11.json'));T=s.Matrix([[s.Rational(x) for x in row] for row in r['old_power_to_new']])*B
poly=s.Poly.from_list(r['poly'],x);print('small poly',poly.as_expr())
# evaluate at the simple mod7 root 1 and the two other residue roots, using F49=F7[t]/(t^2+107)
def ev(v,a):
 den=int(s.ilcm(*[x.q for x in v]));assert den%7
 z=s.Poly(sum(int(z*den)*x**i for i,z in enumerate(v)),x);return int(z.eval(a))*pow(den,-1,7)%7
Q=s.Poly(x**2-x-3,x)
candidates=[];tested=0
for k in range(1,6):
 for inds in itertools.combinations(range(7),k):
  for signs in itertools.product([-2,-1,1,2],repeat=k-1):
   v=s.zeros(7,1)
   for j,c in zip(inds,(1,)+signs):v[j]=c
   vv=T*v
   if ev(vv,1):continue
   den=int(s.ilcm(*[x.q for x in vv]));pol=s.Poly(sum(int(z*den)*x**i for i,z in enumerate(vv)),x)
   if all(int(a)%7==0 for a in pol.rem(Q).all_coeffs()):continue
   tested+=1;norm=abs(int(lin(M,v).det()));nn=norm;exp=0
   while nn and nn%7==0:nn//=7;exp+=1
   if nn==1 and exp%7:
    candidates.append((exp,list(map(int,v)),[str(z) for z in vv]));print('found',candidates[-1], 'tested',tested,flush=True)
    if exp==1:break
  if candidates and candidates[-1][0]==1:break
 if candidates and candidates[-1][0]==1:break
print('count',len(candidates),'tested',tested)
if candidates:json.dump(min(candidates),open('frob_element.json','w'))

