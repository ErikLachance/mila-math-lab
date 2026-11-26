"""Finite exact enumeration only. Check the M=1,2 ray principal-prime objects
for K=Q(sqrt(-23)), used as a sanity case for the human manuscript's (C9).
No inference of uniform interval lower bound from finite counts.
"""
import math,json
from pathlib import Path
N=200000
prime=[True]*(N+1);prime[0:2]=[False,False]
for p in range(2,math.isqrt(N)+1):
 if prime[p]:
  for q in range(p*p,N+1,p):prime[q]=False
pairs={}; rep={}
for b in range(-math.isqrt(4*N//23)-1,math.isqrt(4*N//23)+2):
 # Norm(a+bw)=(a+b/2)^2+(23/4)b^2
 B=4*N-23*b*b
 if B<0:continue
 xmax=math.isqrt(B)
 # Exact candidate a satisfies |2a+b|<=floor sqrt B
 for a in range(math.ceil((-xmax-b)/2),math.floor((xmax-b)/2)+1):
  n=a*a+a*b+6*b*b
  if 2<=n<=N and prime[n]:
   pairs.setdefault(n,[]).append((a,b))
   if n not in rep:rep[n]=(a,b)
P1=set(pairs)
P2={p for p,ab in pairs.items() if any(a%2==1 and b%2==0 for a,b in ab)}
P3={p for p,ab in pairs.items() if any(a%3==1 and b%3==0 for a,b in ab)}
for p in P2:assert p%2==1
for p in P3:assert p%3==1
numprimes=sum(prime)
threshold=[1000,10000,50000,100000,200000]
counts=[]
for u in threshold:
 pp=sum(prime[:u+1]);one=sum(n<=u for n in P1);two=sum(n<=u for n in P2);three=sum(n<=u for n in P3)
 counts.append({'X':u,'primeCount':pp,'M1Count':one,'M1DensityAmongPrimes':round(one/pp,5),'M2Count':two,'M3Count':three})
assert len(P2)<=len(P1) and len(P3)<=len(P1)
R={'discriminant':-23,'norm':'Norm(a+b*(1+sqrt(-23))/2) = a^2+a*b+6*b^2','classNumberExact':3,'heuristicM1RationalPrimeDensity':'1/(2*classNumber)=1/6 (Chebotarev heuristic; not proved by this finite count)','counts':counts,'M1RepresentationExamples':{str(p):rep[p] for p in sorted(P1)[:12]},'primalitySieveExactTo':N,'limitations':'Finite enumeration supports only elementary representability, congruence and density sanity checks. It does not prove C9 uniform in discriminant, conductor, variable h, nor a lower bound for every short interval. The ray class character of order 3 is a Hecke L-function, not a Dirichlet L-function over Q; RH for only Dirichlet L does not directly imply it.'}
Path('/mnt/data/riemann_20261123_1554/imaginary_quadratic_principal_primes.json').write_text(json.dumps(R,indent=2))
print(json.dumps(counts,indent=2))
