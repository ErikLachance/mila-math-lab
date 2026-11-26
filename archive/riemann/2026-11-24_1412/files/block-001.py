from sympy import Poly, symbols, cyclotomic_poly, resultant, gcd, factor_list, ZZ, Matrix
from fractions import Fraction as F
from itertools import product
from collections import Counter
from time import monotonic
x,z=symbols('x z'); C=Counter(); start=monotonic()
# Gelfand-Tsetlin patterns for GL3; exact coordinate weight bounds and dimension.
for a in range(-5,9):
 for b in range(-5,a+1):
  for c in range(-5,b+1):
   count=0; mins=[a+1]*3; maxs=[c-1]*3
   for u in range(b,a+1):
    for v in range(c,b+1):
     for w in range(v,u+1):
      mu=(w,u+v-w,a+b+c-u-v)
      assert sum(mu)==a+b+c and all(c<=j<=a for j in mu)
      for k,j in enumerate(mu):mins[k]=min(mins[k],j);maxs[k]=max(maxs[k],j)
      count+=1; C['GT_patterns']+=1
   assert count==(a-b+1)*(a-c+2)*(b-c+1)//2 and mins==[c]*3 and maxs==[a]*3
   C['GL3_weights']+=1
# Exact minimum of ellipse target (when a+1/a>=4): derivative at c=-1 >=0.
for q in range(5,401):
 for e in range(1,5):
  a=q**e; A=F(a)+F(1,a); B=F(a)-F(1,a)
  assert A>=4
  # Compare A-1 > sqrt(q)+1+1/sqrt(q) by squaring positive sides.
  assert A-2>0 and (A-2)**2>q+2+F(1,q)
  # rank two, after cancelling constant 1
  assert B**2>4*q
  for j in range(-10,11):
   t=F(j,10)
   assert (1+A*t)**2+B**2*(1-t*t)-(A-1)**2==(t+1)*(2*A+4*(t-1))>=0
   C['ellipse_exact']+=1
  C['separation_q_e']+=1
# General resultant with target factors repeated. Work in ZZ[x].
# For each q,e, z primitive n-th roots, scaled target q^e*t=1? precisely
# a*(1+a/z+z/a) = a + a*a/z + z.
# z^2+(a-x)z+a*a=0, resultant with Phi_n(z).
for q,e,n in product((7,11,13),(1,2),range(1,11)):
 a=q**e; Q=Poly(resultant(cyclotomic_poly(n,z),z*z+(a-x)*z+a*a,z),x,domain=ZZ).monic().set_domain(ZZ)
 for k in (1,2,3):
  # synthetic actual eigenvalues in [-2,2], repeated traces allowed.
  P0=Poly((x-a)**2*(x+a)*(x*x+a*a),x,domain=ZZ)
  assert gcd(P0,Q).degree()==0
  P=P0*Q**k*Poly(x-100*a*a,x,domain=ZZ)
  # Remove all copies of shared irreducible factors, not merely one gcd.
  Fp=P; removed=0
  while True:
   g=gcd(Fp,Q)
   if g.degree()==0:break
   Fp=Fp.exquo(g); removed+=g.degree()
  assert Fp==P0*Poly(x-100*a*a,x,domain=ZZ) and removed==k*Q.degree()
  R=int(resultant(Q.as_expr(),P0.as_expr(),x)); assert R!=0
  # independent product over known P0 factors, including repeated trace
  R2=int(resultant(Q.as_expr(),(x-a),x))**2*int(resultant(Q.as_expr(),x+a,x))*int(resultant(Q.as_expr(),x*x+a*a,x))
  if R!=R2: C['sympy_sign_disagreement']+=1
  assert abs(R)==abs(R2), (q,e,n,k,R,R2)
  if k==1:
   # Sylvester determinant with descending coefficients and no degree swap.
   m,d=Q.degree(),P0.degree(); u=Q.all_coeffs(); v=P0.all_coeffs()
   rows=[[0]*j+u+[0]*(d-1-j) for j in range(d)]
   rows += [[0]*j+v+[0]*(m-1-j) for j in range(m)]
   S=Matrix(rows).det(method='bareiss')
   assert abs(S)==abs(R)
   if m==1: assert S==P0.eval(-Q.nth(0))
   C['sylvester_crosscheck']+=1
  # Roots of P0 modulus <=a; roots of Q modulus <=a+a*a+1.
  assert abs(R)<=(a*a+2*a+1)**(Q.degree()*P0.degree())
  C['resultant_and_pollution']+=1
  if k>1:
   assert gcd(P.exquo(gcd(P,Q)),Q).degree()>0
   C['one_gcd_failure']+=1
print(dict(C)); print('script_seconds',monotonic()-start)

