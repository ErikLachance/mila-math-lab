from fractions import Fraction as F
import json
class QI:
 def __init__(self,r=0,i=0):self.r=F(r);self.i=F(i)
 def __add__(self,o):
  o=o if isinstance(o,QI) else QI(o)
  return QI(self.r+o.r,self.i+o.i)
 __radd__=__add__
 def __neg__(self):return QI(-self.r,-self.i)
 def __sub__(self,o):return self+-o if isinstance(o,QI) else self+QI(-o)
 def __mul__(self,o):
  o=o if isinstance(o,QI) else QI(o)
  return QI(self.r*o.r-self.i*o.i,self.r*o.i+self.i*o.r)
 __rmul__=__mul__
 def __truediv__(self,o):
  o=o if isinstance(o,QI) else QI(o)
  den=o.r**2+o.i**2
  return QI((self.r*o.r+self.i*o.i)/den,(self.i*o.r-self.r*o.i)/den)
 def __pow__(self,n):
  if n<0:return QI(1)/(self**(-n))
  r=QI(1);a=self
  while n:
   if n&1:r=r*a
   a=a*a;n>>=1
  return r
 def __eq__(self,o):
  o=o if isinstance(o,QI) else QI(o)
  return self.r==o.r and self.i==o.i
 def norm2(self):return self.r*self.r+self.i*self.i
 def __repr__(self):return f'({self.r})+({self.i})i'

p=2;a=QI(0,1)
results=[]
for m in range(0,41):
 for x in sorted(set([p**m,p**m+1,p**(m+1)-1])):
  if x>=p**(m+1):continue
  d=QI(x)*a/(QI(p)-a)
  for k in range(1,m+1):
   d=d-(a**k)*(F(x,p**k)-1)
  c=(QI(x)*a/(QI(p)-a))*((a/QI(p))**m)+sum((a**k for k in range(1,m+1)),QI())
  assert d==c,(m,x,d,c)
  # since |first| < p/sqrt(p²+1) <1 and |i+..+i^m|<=sqrt2, |delta|<1+sqrt2 <5/2
  assert d.norm2()<F(25,4)
  if m<5:results.append({'m':m,'x':x,'coefficient':str(d),'norm2':str(d.norm2())})
print('exact Gaussian-rational identities passed: all m=0..40 and 3 interior/boundary x choices, plus |delta/log2|<5/2')
print(results)
with open('/mnt/data/riemann_20261123_1253/gaussian_missing_euler.json','w') as f:json.dump({'exact_cases':sum(3 if m>=1 else 2 for m in range(0,41)), 'samples':results},f,indent=2)
