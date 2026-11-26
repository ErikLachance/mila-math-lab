from fractions import Fraction as F
from math import lcm, gcd
from itertools import product
from collections import Counter
from time import monotonic
from sympy import primerange, factorint
start=monotonic()
# Exact characters on generators of CRT factors; at 2 use -1,5.
# Entries (Npsi, sign exponent, 5 exponent, odd local generator exponents).
examples=[(1,F(0),F(0),{}),(3,F(0),F(0),{3:F(1,2)}),(5,F(0),F(0),{5:F(1,4)}),(7,F(0),F(0),{7:F(1,6)}),(7,F(0),F(0),{7:F(1,3)}),(9,F(0),F(0),{3:F(1,6)}),(13,F(0),F(0),{13:F(1,12)}),(15,F(0),F(0),{3:F(1,2),5:F(1,4)}),(8,F(1,2),F(1,2),{}),(16,F(0),F(1,4),{}),(21,F(0),F(0),{3:F(1,2),7:F(1,3)}),(35,F(0),F(0),{5:F(1,4),7:F(1,6)})]
def v2(n):return (n&-n).bit_length()-1
def order(a,m):
 assert gcd(a,m)==1
 k=1; b=a%m
 while b!=1:b=b*a%m;k+=1
 return k
def prime_to(d,p):
 while d%p==0:d//=p
 return d
def c2(s,b):return v2(b.denominator)+2 if b else (2 if s else 0)
# q,d prime with source congruences; B is a fixed superset of required odd primes
q,d=59,71; counts=Counter(); distinct=0; tests=0; wrong_r1=0; low2_checks=0
for Npsi,sign,five,odd in examples:
 o=lcm(sign.denominator,five.denominator,*[f.denominator for f in odd.values()])
 pK=next(p for p in primerange(7,100) if p%4==3 and Npsi%p)
 assert pK in (7,11) # both class numbers are 1
 p1=next(p for p in primerange(3,100) if (p-1)%prime_to(o,2)==0 and gcd(p,2*Npsi*pK)==1)
 B={3}|(set(factorint(o*Npsi*pK*p1))-{2})
 assert all(p in B for p in odd) and q not in B and d not in B
 for nu in range(2,6):
  M=max(2**nu,five.denominator); keys=sorted(set(odd)|{q,d}); chars=set()
  for a,b,c,j in product(range(M),range(2),range(2),range(o)):
   vals=tuple((j*odd.get(k,F(0))+ (F(b,2) if k==q else F(c,2) if k==d else 0))%1 for k in keys)
   chars.add((j*sign%1,(F(a,M)+j*five)%1,vals))
  distinct+=len(chars)
  for s,f,vals in chars:
   loc=dict(zip(keys,vals));  # compute odd-factor -1 via group order below
   odd_group_orders={3:6 if Npsi==9 else 2,5:4,7:6,13:12,q:q-1,d:d-1}
   parity=(s+sum((x*(odd_group_orders[k]//2) for k,x in loc.items()),F(0)))%1
   full=lcm(s.denominator,f.denominator,*[x.denominator for x in vals]); c=c2(s,f)
   for p in (3,5,7,11,13,17,19,23,29,31,37,59,71):
    star=lcm(prime_to(s.denominator,p),prime_to(f.denominator,p),*[prime_to(x.denominator,p) for k,x in loc.items() if k!=p]); one=lcm(*[prime_to(x.denominator,p) for x in vals]);
    assert one>0 and gcd(p,one)==1 and lcm(prime_to(o,p),2)%one==0
    f0=order(p,lcm(4,one)); R=16*o*(p*Npsi)**2*4**v2(pow(p,f0)-1)
    for r in range(1,9):
     if parity!=F(r%2,2):continue
     tests+=1
     if p not in B and 2*r%(p-1):
      counts['I']+=1; assert full%p!=0 and loc.get(p,F(0)).denominator<=2
     elif r>=2 and star%2==0:counts['II']+=1
     elif p not in B:
      assert r>=2 and p not in (q,d) and p not in odd and full%2==1 and full==star
      counts['Z' if full==1 else 'III']+=1
     elif r==1 and 2**c>=R:counts['V']+=1
     elif r==1:
      counts['small_2_conductor']+=1
      # Degree bound from bounded conductor at 2, fixed psi and 2 quadratic factors.
      assert full<=4*o*2**c; low2_checks+=1
      if loc[q] or loc[d]:wrong_r1+=1
     else:
      counts['fixed_tower']+=1
      assert s==f==loc[q]==loc[d]==0 and all(k in odd or x==0 for k,x in loc.items())
      assert o%full==0
# synthetic large 2-conductor branch: actual R can be much greater than 2^10.
for p in (3,5,7,11,13):
 R=16*p*p*4**v2(p**order(p,4)-1)
 c=(R-1).bit_length()
 assert 2**(c-1)<R<=2**c
 # Actual psi trivial, phi=odd q-quadratic times even 2-character,
 # p fixed exceptional (p=3 or 7 for trivial psi); extra p illustrate threshold only.
 assert c2(F(0),F(1,2**(c-2)))==c
 assert c2(F(0),F(1,2**(c-3)))==c-1
 counts['V_threshold_tests']+=1
print(dict(distinct_chars=distinct,classified=tests,counts=dict(counts),low2_checks=low2_checks,low2_with_q_or_d=wrong_r1,seconds=monotonic()-start))

