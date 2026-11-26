from riemann_order_run11 import *
import mpmath as mp,itertools,json
mp.mp.dps=100
B,M,one,d=saturate(structure(P),[2,7,79,38737,13513109],s.eye(7)[:,0]);roots=P.nroots(n=85,maxsteps=500); roots=[mp.mpc(str(s.re(z)),str(s.im(z))) for z in roots if s.im(z)>=0]
rows=[]
for a in roots:
 row=[a**i for i in range(7)]; rows.append([mp.re(z)*(1 if a.imag==0 else mp.sqrt(2)) for z in row]);
 if a.imag!=0:rows.append([mp.im(z)*mp.sqrt(2) for z in row])
E=mp.matrix(rows)*mp.matrix([[mp.mpf(str(v.p))/int(v.q) for v in row] for row in B.tolist()]);scale=10**35
A=s.Matrix([[int(mp.nint(E[j,i]*scale)) for j in range(7)] for i in range(7)]);L,U=A.lll_transform();assert abs(U.det())==1
M=change(M,U.T);one=U.T.inv()*one;B=B*U.T
print('short integral basis',B.tolist())
res=[]
for k in (1,2,3):
 for inds in itertools.combinations(range(7),k):
  for signs in itertools.product([-1,1],repeat=k-1):
   v=s.zeros(7,1)
   for i,sgn in zip(inds,(1,)+signs):v[i]=sgn
   N=lin(M,v); ps=[one]
   for _ in range(6):ps.append(N*ps[-1])
   S=s.Matrix.hstack(*ps);ind=abs(int(S.det()))
   if not ind or ind%7==0:continue
   poly=s.Poly(N.charpoly(x).as_expr(),x);assert poly.is_irreducible and poly.discriminant()==d*ind**2
   res.append((max(abs(int(z)) for z in poly.all_coeffs()),ind,poly,S,v))
print('7-maximal primitive generators',len(res));a,ind,poly,S,v=min(res,key=lambda z:(z[0],z[1]));print('best',poly.as_expr(),'index',ind,'coordinates',list(v),'mod7 factors',s.factor_list(poly,modulus=7));print('power-basis-to-old-B', (S.inv()*B.inv()).tolist())
json.dump({'poly':[int(z) for z in poly.all_coeffs()], 'old_power_to_new':[[str(z) for z in row] for row in (S.inv()*B.inv()).tolist()]},open('/mnt/data/riemann_smallgen_run11.json','w'))

