from certified_bump import Q,log_bound,invsqrt,primes_to,roundout
from pathlib import Path
from math import isqrt
from functools import lru_cache
import json,time
start=time.monotonic();base=Path(__file__).parent
@lru_cache(None)
def h(s):
    w2=s*s/4;term=Q(1);total=term
    for k in range(1,49):term*=w2/(2*k*(2*k+1));total+=term
    first=term*w2/(98*99);r=w2/(100*101);assert r<1
    return roundout(total,total+first/(1-r))
def k(n,x):
    l,u=log_bound(Q(n,x));mx=max(abs(l),abs(u));mn=0 if l<=0<=u else min(abs(l),abs(u))
    return max(Q(0),1-mx),max(Q(0),1-mn)
# square-root weighted discrepancy D(x)=x A-W(x), before small trivial-zero correction.
def disc(x):
    root=isqrt(x);assert root*root==x
    a,b=h(Q(1,2));lo=x*a*a;hi=x*b*b;count=0
    for p in primes_to(3*x):
        n=p
        while n<=3*x:
            if 3*n>=x:
                kl,kh=k(n,x)
                if kh:
                    ll,lh=log_bound(Q(p));sl,sh=invsqrt(n)
                    l,u=roundout(root*ll*sl*kl,root*lh*sh*kh);lo-=u;hi-=l;count+=1
            n*=p
    return lo,hi,count
rows=[]
for m in range(2,41):
    x=m*m;l,u,c=disc(x)
    # conservative Lipschitz bound |D(x)-D(y)|<64|x-y| (analytic proof separate)
    assert u-l<Q(1,10**6)
    rows.append(dict(m=m,x=x,lower=str(l),upper=str(u),lower_scaled=float(l/m),upper_scaled=float(u/m),primepowers=c))
for a,b in zip(rows,rows[1:]):
    d=max(abs(Q(a['lower'])-Q(b['upper'])),abs(Q(a['upper'])-Q(b['lower'])))
    assert d<=64*(b['x']-a['x'])
res=dict(square_samples=len(rows),consecutive_lipschitz_regressions=len(rows)-1,total_primepower_terms=sum(r['primepowers'] for r in rows),min_scaled=min(r['lower_scaled'] for r in rows),max_scaled=max(r['upper_scaled'] for r in rows),max_width=max(float(Q(r['upper'])-Q(r['lower'])) for r in rows),elapsed_code_seconds=time.monotonic()-start,rows=rows)
(base/'triangle_square.json').write_text(json.dumps(res,indent=2));print(json.dumps({k:v for k,v in res.items() if k!='rows'},indent=2))

