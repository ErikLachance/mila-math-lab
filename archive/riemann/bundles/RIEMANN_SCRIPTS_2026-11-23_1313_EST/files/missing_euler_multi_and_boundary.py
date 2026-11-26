from fractions import Fraction as F
from sympy import primerange
import json, math

def chi4(n):
 if n%2 == 0:return 0
 return 1 if n%4==1 else -1

def ps_terms(N):
 out=[]
 for p in primerange(2,N+1):
  v=p
  while v<=N:
   out.append((p,v))
   v*=p
 return out

def direct_mod_change(x,modulus):
 out={}
 for p,n in ps_terms(x):
  a=chi4(n)
  b=a if math.gcd(n,modulus)==1 else 0
  if b!=a:
   out[p]=out.get(p,F())+F(b-a)*(F(x,n)-1)
 for p in primerange(2,modulus+1):
  if modulus%p==0 and 4%p!=0:
   a=chi4(p)
   out[p]=out.get(p,F())+F(x*a,p-a)
 return {p:v for p,v in out.items() if v}

def algebra(x,modulus):
 out={}
 for p in primerange(2,modulus+1):
  if modulus%p or 4%p==0:continue
  a=chi4(p)
  if not a:continue
  m=0;t=1
  while p*t<=x:t*=p;m+=1
  v=F(x*a,p-a)
  for k in range(1,m+1):v-=F(a**k)*(F(x,p**k)-1)
  if v:out[p]=v
 return out

report=[]
for q in [4*5,4*3,4*5*7,4*5*13,4*5**3*13,4*3*7]:
 for x in [1,2,7,19,59,100,260,500,2026,10000,50000]:
  if x>50000:continue
  d=direct_mod_change(x,q)
  c=algebra(x,q)
  assert d==c,(q,x,d,c)
  report.append({'q':q,'x':x,'extra_prime_coefficients':{str(p):str(v) for p,v in c.items()}})

# Mathematical fixed point of logarithmic drift: for each q, count distinct
# p|q, p not dividing primitive conductor 4, with chi4(p)=+1.
status=[]
for q in [20,12,140,260,6500,84]:
 splits=[p for p in primerange(2,q+1) if q%p==0 and 4%p and chi4(p)==1]
 nonsplits=[p for p in primerange(2,q+1) if q%p==0 and 4%p and chi4(p)==-1]
 status.append({'q':q,'split_primes':splits,'nonsplit_primes':nonsplits,
  'asymptotic_correction':'Delta(x) = '+str(len(splits))+'*log(x) + O_q(1)',
  'extra_zeros_at_s0':len(splits)})
# no extra correction if adding a conductor divisor to the modulus
assert algebra(100,4*2)=={}
assert algebra(100,4*4)=={}
print('EXACT multi-prime and conductor-power verification',len(report),'cases PASS')
print(json.dumps(status,indent=2))
with open('/mnt/data/riemann_20261123_1253/missing_euler_multi_and_boundary.json','w') as f:
 json.dump({'exact_cases':len(report),'statuses':status,'selected_samples':[r for r in report if r['x'] in (1,10000)]},f,indent=2)
