import math,json
import mpmath as mp
from sympy import legendre_symbol
mp.mp.dps=60

def forms(D):
 R=[]
 for a in range(1,math.isqrt(abs(D)//3)+3):
  for b in range(-a,a+1):
   if (b*b-D)%(4*a):continue
   c=(b*b-D)//(4*a)
   if a>c or math.gcd(a,math.gcd(abs(b),c))!=1:continue
   if (abs(b)==a or a==c) and b<0:continue
   R.append((a,b,c))
 return R

def chis(d):
 A0=A1=mp.mpf(0)
 for a in range(1,d):
  u=int(legendre_symbol(a,d))
  t=mp.mpf(a)/d
  A0-=u*mp.digamma(t)
  A1-=u*mp.stieltjes(1,t)
 return A1/A0-mp.log(d)

def logArea(f,d):
 a,b,c=f
 t=mp.mpc(-mp.mpf(b)/(2*a),mp.sqrt(d)/(2*a))
 q=mp.exp(2*mp.pi*1j*t)
 val=mp.log(4*mp.pi)+mp.log(t.imag)+mp.log(abs(q))/6
 for n in range(1,150):
  val+=4*mp.log(abs(1-q**n))
  if abs(q)**n < mp.mpf('1e-75'): break
 return val
out=[]
for d in [23,31,47,59]:
 f=forms(-d)
 vals=[logArea(form,d) for form in f]
 mean=sum(vals)/len(vals)
 c=chis(d)
 RHS=mp.euler+mp.log(2*mp.pi/mp.sqrt(d))-c
 err=abs(mean-RHS)
 assert err<mp.mpf('1e-48'),(d,f,err)
 out.append({'d':d,'h':len(f),'forms':[list(x) for x in f],'computed_avg':mp.nstr(mean,40),'formula':mp.nstr(RHS,40),'log_derivative':mp.nstr(c,40),'abs_error':mp.nstr(err,8)})
print(json.dumps(out,indent=2))
open('/mnt/data/riemann_20261123_1431_kronecker_multiclass.json','w').write(json.dumps(out,indent=2))
