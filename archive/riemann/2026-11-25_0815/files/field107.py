from math import gcd
from time import monotonic
import sympy as s
start=monotonic();q=107;N=q*7
eta=lambda a:int(s.legendre_symbol(a%q,q))
g=next(a for a in range(1,N) if a%7==5 and eta(a)==1)
H=[a for a in range(1,N) if gcd(a,N)==1 and (a%7,eta(a)) in [(1,1),(6,-1)]]
assert len(H)==q-1
C=[[(pow(g,j,N)*a)%N for a in H] for j in range(6)]
assert len(set(sum(C,[])))==6*(q-1)
ex=[4,1,0,2,5,6];r=pow(g,5,7)
# The exponents are an eigenvector modulo constants (Norm u=1).
assert len(set((ex[(j-1)%6]-r*ex[j])%7 for j in range(6)))==1
assert all(ex[j]+ex[j+3]==6 for j in range(3))
factors=[a for j in range(6) for a in C[j]*ex[j]]
v=[1]+[0]*(N-1);ram=[(6 if a%7==0 else -1)*(q-1 if a%q==0 else -1) for a in range(N)];tr=[]
for k in range(1,4):
 for a in factors:
  w=v[-a:]+v[:-a];v=[x-y for x,y in zip(v,w)]
 t=sum(x*y for x,y in zip(v,ram));assert t%(q-1)==0;tr.append(t//(q-1))
P1=tr[0];P2=tr[1]+6;P3=tr[2]+3*tr[0];assert (P1**2-P2)%2==0;c2=(P1**2-P2)//2;assert (P3-P1*P2+c2*P1)%3==0;c3=(P3-P1*P2+c2*P1)//3
z,X=s.symbols('z X');Q=z**3-P1*z*z+c2*z-c3;assert s.Poly(Q,z).is_irreducible
checks=[]
for k in range(1,40):
 ell=k*N+1
 if not s.isprime(ell):continue
 gg=int(s.primitive_root(ell));zz=pow(gg,k,ell);us=[]
 for group in C:
  v0=1
  for a in group:v0=v0*(1-pow(zz,a,ell))%ell
  us.append(v0)
 vals=[]
 for j in range(6):
  v0=1
  for i in range(6):v0=v0*pow(us[(i+j)%6],ex[i],ell)%ell
  vals.append(v0)
 assert all(vals[j]*vals[j+3]%ell==1 for j in range(3))
 assert all(((w:= (v0+pow(v0,-1,ell))%ell)**3-P1*w*w+c2*w-c3)%ell==0 for v0 in vals)
 checks.append((ell,vals[0],pow(vals[0],(ell-1)//7,ell)))
 if len(checks)>=5:break
assert any(t[2]!=1 for t in checks)
P=s.Poly(Q.subs(z,z**7-7*z**5+14*z**3-7*z),z);assert P.degree()==21
R=s.Poly(s.resultant(P.as_expr(),(X-z)**2+q,z),X);assert R.degree()==42 and s.gcd(R,R.diff()).degree()==0
print('q',q,'g',g,'traces',tr,'Q',Q,'checks',checks,'R maximum digits',max(len(str(abs(c))) for c in R.all_coeffs()),'elapsed',monotonic()-start)
open('/mnt/data/riemann_0815/field107_result.txt','w').write(f'q={q}, g={g}\ntraces={tr}\nQ={Q}\nchecks={checks}\nR={R.as_expr()}\n')

