import json, math, time, random
from fractions import Fraction as Q
start=time.monotonic(); N=100000; Z=45; m0=120; a0=7
sieve=bytearray(b'\1')*(N+1);sieve[:2]=b'\0\0'
for p in range(2,math.isqrt(N)+1):
 if sieve[p]:sieve[p*p::p]=b'\0'*((N-p*p)//p+1)
qs=[q for q in range(Z*Z+1,N+1) if sieve[q] and q%m0==a0]
ps=[p for p in range(2,Z+1) if sieve[p]]
def leg(a,p):
 v=pow(a%p,(p-1)//2,p);return -1 if v==p-1 else v
def sf(n):
 s=1; sign=1
 for p in ps:
  j=0
  while n%p==0:n//=p;j+=1
  if j%2:
   if p==2: sign*=1 if a0%8 in (1,7) else -1
   elif m0%p==0:sign*=leg(a0,p)*(-1 if a0%4==p%4==3 else 1)
   else:s*=p;sign*=(-1 if a0%4==p%4==3 else 1)
 assert n==1
 return s,sign
def jac(q,s):
 out=1
 for p in ps:
  if s%p==0:out*=leg(q,p)
 return out
def sym(a,b):return a*b//math.gcd(a,b)**2
meta={n:sf(n) for n in range(1,Z+1)}; supports=sorted({s for s,sg in meta.values()}); pair={sym(s,t) for s in supports for t in supports}; cor={s:Q(sum(jac(q,s) for q in qs),len(qs)) for s in pair}; e=max(pair-{1},key=lambda s:abs(cor[s])); eta=max(abs(cor[s]) for s in pair-{1,e}); count=0
for q in qs:
 for n,(s,sign) in meta.items():
  assert leg(n,q)==sign*jac(q,s);count+=1
rng=random.Random(23); gramchecks=0
for i in range(100):
 a={s:0 for s in supports}; c={n:rng.randrange(-8,9) for n in meta}
 for n,(s,sign) in meta.items():a[s]+=c[n]*sign
 exact=Q(sum(sum(c[n]*leg(n,q) for n in meta)**2 for q in qs),len(qs))
 gram=sum(a[s]*a[t]*cor[sym(s,t)] for s in supports for t in supports)
 assert exact==gram
 bound=sum(x*x for x in a.values())+abs(cor[e])*sum(abs(a[s]*a.get(sym(s,e),0)) for s in supports)+eta*sum(map(abs,a.values()))**2
 assert exact<=bound;gramchecks+=1
print(json.dumps({'q_count':len(qs),'Z':Z,'m0':m0,'a0':a0,'q_limit':N,'exact_reciprocity_checks':count,'exact_grouped_gram_checks':gramchecks,'group_count':len(supports),'exception_candidate':e,'largest_abs_correlation':str(abs(cor[e])),'second_largest_abs_correlation':str(eta),'runtime_s':time.monotonic()-start},indent=2))

