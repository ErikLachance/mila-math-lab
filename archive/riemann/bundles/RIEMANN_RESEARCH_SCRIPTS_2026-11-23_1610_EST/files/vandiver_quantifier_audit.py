import math,json,time
from pathlib import Path
N=20000
isp=[True]*(N+1);isp[0]=isp[1]=False
for p in range(2,math.isqrt(N)+1):
 if isp[p]:
  for n in range(p*p,N+1,p):isp[n]=False
primes=[l for l in range(5,N+1) if isp[l]]
examples=[];total=0;bad=0
for l in primes:
 half=(l-1)//2
 for e in range(2,801,2):
  if (2*e)%(l-1)==0 and e%(l-1)!=0:
   total+=1
   if l%4!=1: bad+=1
   if len(examples)<20:examples.append([l,e,(l-1)//2,l%4])
# Stronger check fixed e, l with (l-1)|2e and not (l-1)|e are exactly those l-1 divides 2e but not e; even e implies (l-1)/2 even and l == 1 mod 4.
# Example varying e=(l-1)//4 when l==1 mod 8, not excluded by (l-1)|2e, and e grows linearly with l.
far=[{'l':l,'e':(l-1)//4,'check':((l-1)//4)%2==0 and (2*((l-1)//4))%(l-1)!=0} for l in primes if l%8==1][:16]
R={'primeLimit':N,'eRange':[2,800],'qualifyingPairs':total,'violationsToQuadraticFieldSignRule':bad,'sampleQuadraticExclusion':examples,'sequenceBeyondFixedELimit':far,'generalProof':'If d=l-1 is even, d|2e but d does not divide e forces e=(2k+1)d/2. If e is even, d/2 must be even, so d is divisible by 4 and l=1 mod4. The quadratic subfield is Q(sqrt(l)); for l=3 mod4 the exceptional even-e case does not occur.','importantQuantifier':'For fixed e, (V) gives vanishing for log(l)>C(e+1)^A. It does NOT prove Vandiver uniformly for all even e<l-1; e can grow linearly in l.','proofScope':'Elementary exact modular assertion verified on finite sample and proved algebraically; none of the unproved V/G3 hypotheses is established.'}
p=Path('/mnt/data/riemann_20261123_1554/vandiver_quantifier_results.json');p.write_text(json.dumps(R,indent=2));print(json.dumps(R,indent=2))
