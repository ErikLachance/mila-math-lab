import math, json
from pathlib import Path
N=300000
isprime=bytearray(b'\x01')*(N+1);isprime[0:2]=b'\x00\x00'
for p in range(2,int(N**0.5)+1):
 if isprime[p]:isprime[p*p:N+1:p]=b'\x00'*(((N-p*p)//p)+1)
ll=[0.0]*(N+1);weighted=[0.0]*(N+1)
for p in range(2,N+1):
 if isprime[p]:
  m=p
  while m<=N:
   ll[m]=math.log(p)
   m*=p
  weighted[p]=math.log(p)/(p-1)
psi=0.; F=0.; worst_psi=(0,0);worstF=(-1e100,0)
for n in range(2,N+1):
 psi+=ll[n];F+=weighted[n]
 ratio=psi/n
 if ratio>worst_psi[0]:worst_psi=(ratio,n)
 diff=F-math.log(n)
 if diff>worstF[0]:worstF=(diff,n)
 assert psi<1.2*n+1e-8
 assert F<math.log(n)+67/20
r={'maxN':N,'max_psi_over_x':worst_psi,'max_prime_sum_minus_logx':worstF,'independent_checks':N-1,'numeric_only':True}
Path('/mnt/data/riemann_20261123_prime_sum_independent_regression.json').write_text(json.dumps(r,indent=2))
print(r)
