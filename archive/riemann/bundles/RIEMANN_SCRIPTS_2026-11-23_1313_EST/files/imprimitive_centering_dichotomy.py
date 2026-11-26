from fractions import Fraction
import math,json
# For primitive chi_* and an extra modulus prime ell with a=chi_*(ell) in {-1,1},
# exact coefficient of log ell in (G_imprimitive - G_primitive).
def m_for(x,p):
 m=0;t=1
 while p*t<=x:t*=p;m+=1
 return m

def direct(x,p,a):
 m=m_for(x,p)
 C=Fraction(a,p-a)*x
 return C-sum(Fraction(a**k,1)*(Fraction(x,p**k)-1) for k in range(1,m+1))

def closed(x,p,a):
 m=m_for(x,p)
 geom=Fraction(a,p-a)*x*Fraction(a**m,p**m)
 return geom+sum(Fraction(a**k,1) for k in range(1,m+1))

report={}
for p,a in [(5,1),(3,-1),(7,-1),(11,1)]:
 count=0;maxcorr=Fraction(0,1);maxspread=Fraction(0,1)
 for m in range(0,41):
  for x in sorted(set([p**m,max(1,p**m+1),2*p**m,p**(m+1)-1])):
   if x>=p**(m+1):continue
   q1=direct(Fraction(x),p,a)
   q2=closed(Fraction(x),p,a)
   assert q1==q2,(p,a,m,x)
   count+=1
   if a==-1:
    # |x*a/(p-a)*(a/p)^m|< p/(p+1); |sum_{k<=m}(-1)^k|<=1
    assert abs(q2)<Fraction(p,p+1)+1
   else:
    # log p * m is log x + O(log p), x p^-m in [1,p)
    assert q2-m>0 and q2-m<=Fraction(p,p-1)
 report[f'p{p}_a{a}']={'exact_cases':count,'first5':[(x,str(closed(Fraction(x),p,a))) for x in [1,p,p**2,p**3,p**4]]}
print(json.dumps(report,indent=2))
with open('/mnt/data/riemann_20261123_1253/imprimitive_centering_dichotomy.json','w') as f:json.dump(report,f,indent=2)
