import math,json,time,hashlib
from pathlib import Path
N=300000
start=time.perf_counter()
sigma=[0]*(N+1)
for d in range(1,N+1):
    for j in range(d,N+1,d):
        sigma[j]+=d
H=0.0; er=math.exp(0.57721566490153286060651209)
robin_bad=[];lagarias_bad=[]
robin_nearest=(1e99,None); robin_tight_ratio=(0,None); lagarias_nearest=(1e99,None)
for n in range(1,N+1):
    H+=1.0/n
    lagbound=H+math.exp(H)*math.log(H)
    lm=lagbound-sigma[n]
    if n>1 and lm<lagarias_nearest[0]:lagarias_nearest=(lm,n)
    if lm< -2e-8:lagarias_bad.append((n,lm))
    if n>5040:
        robinbound=er*n*math.log(math.log(n))
        rm=robinbound-sigma[n]
        ratio=sigma[n]/robinbound
        if rm<robin_nearest[0]:robin_nearest=(rm,n)
        if ratio>robin_tight_ratio[0]: robin_tight_ratio=(ratio,n)
        if rm< -2e-8:robin_bad.append((n,rm))
specific=[]
for n in [1,2,3,10,5040,5041,10080,15120,30030,60060,277200,300000]:
    if n>N:continue
    h=math.fsum(1/k for k in range(1,n+1)) if n<=5041 else math.log(n)+0.5772156649015329+1/(2*n)-1/(12*n*n)+1/(120*n**4)
    specific.append({'n':n,'sigma':sigma[n],'Robin_margin':er*n*math.log(math.log(n))-sigma[n] if n>1 else None,'Lagarias_margin':h+math.exp(h)*math.log(h)-sigma[n]})
R={'limit':N,'checkedRobinIntegers':N-5040,'checkedLagariasIntegers':N,'robinViolations':robin_bad[:10],'lagariasViolations':lagarias_bad[:10], 'tightestRobinAbsoluteMargin':robin_nearest, 'maxRobinRatio':robin_tight_ratio, 'tightestLagariasMarginExcludingN1':lagarias_nearest,'samples':specific,'seconds':time.perf_counter()-start,'note':'Finite double-precision numerical falsification only, not proof; Robin n=5040 excluded by theorem.'}
p=Path('/mnt/data/riemann_20261123_1554/robin_lagarias_results.json');p.write_text(json.dumps(R,indent=2));print(json.dumps(R,indent=2))
