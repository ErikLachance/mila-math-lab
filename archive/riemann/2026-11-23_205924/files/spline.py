from fractions import Fraction as Q
from math import comb,factorial
import json,time
from pathlib import Path
import mpmath as mp
start=time.monotonic(); checks=0; rows=[]
# Kernel is sum of 2k independent uniforms [-1/(2k),1/(2k)].
for k in range(1,9):
 d=2*k-1; factor=Q(k**(2*k),factorial(d)); knots=[Q(j,k)-1 for j in range(2*k+1)]
 def poly(v,j,r):
  return factor*Q(factorial(d),factorial(d-r))*sum((-1)**i*comb(2*k,i)*(v-knots[i])**(d-r) for i in range(j+1))
 # derivatives up to d-1 agree at each knot including boundaries
 for j,t in enumerate(knots):
  for r in range(d):
   assert poly(t,j-1,r)==poly(t,j,r);checks+=1
 for r in range(d+1):
  assert poly(Q(2),2*k,r)==0;checks+=1
 # exact moments on [-1,1] by integrated truncated powers
 moments=[]
 for r in [0,1,2,4]:
  val=factor*sum((-1)**j*comb(2*k,j)*sum(Q(comb(r,l))*t**(r-l)*(1-t)**(d+l+1)/(d+l+1) for l in range(r+1)) for j,t in enumerate(knots))
  var=Q(1,6*k);expected={0:Q(1),1:Q(0),2:var,4:3*var**2-Q(1,60*k**3)}[r]
  assert val==expected,(k,r,val,expected);checks+=1;moments.append(str(val))
 rows.append(dict(k=k,smoothness=2*k-2,exact_moments=moments,largest_integer_p_with_r_strict=4*k-5))
# independent numerical complex bilateral Laplace integral, not a certified enclosure
mp.mp.dps=45; maxerr=mp.mpf(0); n=0
for k in range(1,6):
 d=2*k-1;fac=mp.mpf(k)**(2*k)/factorial(d);knots=[mp.mpf(j)/k-1 for j in range(2*k+1)]
 def den(v):return fac*mp.fsum((-1)**j*comb(2*k,j)*max(mp.mpf(0),v-t)**d for j,t in enumerate(knots))
 for s in [mp.mpc('0.5'),mp.mpc('0.3','8.5'),mp.mpc('0','14.13'),mp.mpc('-0.4','4')]:
  lhs=mp.quad(lambda v: den(v)*mp.exp(s*v),knots);u=s/(2*k);rhs=(mp.sinh(u)/u)**(2*k);err=abs(lhs-rhs);maxerr=max(maxerr,err);n+=1
  assert err<mp.mpf('1e-34')
report=dict(exact_rational_checks=checks,complex_transform_checks=n,max_transform_error=str(maxerr),rows=rows,elapsed_seconds=time.monotonic()-start)
print(json.dumps(report,indent=2));Path(__file__).with_name('spline.json').write_text(json.dumps(report,indent=2))

