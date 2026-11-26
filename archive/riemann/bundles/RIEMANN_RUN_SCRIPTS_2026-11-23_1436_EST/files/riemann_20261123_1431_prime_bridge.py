import math,json
import mpmath as mp
mp.mp.dps=75

def chi(p,q):
    if q==4:return 0 if p%2==0 else (1 if p%4==1 else -1)
    if q==3:return 0 if p%3==0 else (1 if p%3==1 else -1)
    raise ValueError(q)

def sieve(n):
    a=bytearray(b'\x01')*(n+1);a[:2]=b'\x00\x00'
    for p in range(2,math.isqrt(n)+1):
        if a[p]: a[p*p:n+1:p]=b'\x00'*((n-p*p)//p+1)
    return [i for i in range(n+1) if a[i]]

def logLder(q):
    a,b=(mp.mpf(1)/4,mp.mpf(3)/4) if q==4 else (mp.mpf(1)/3,mp.mpf(2)/3)
    num=-mp.stieltjes(1,a)+mp.stieltjes(1,b)
    den=mp.digamma(b)-mp.digamma(a)
    return num/den-mp.log(q)

N=[100,1000,10000,100000,1000000];maximum=max(N)
terms=[]
for p in sieve(maximum):
    v=p;k=1
    while v<=maximum:
        terms.append((v,p,k,math.log(p)))
        if v>maximum//p:break
        v*=p;k+=1
terms.sort()
constants={q:float(logLder(q)) for q in (3,4)}
result={"logLder":{"q3":str(logLder(3)),"q4":str(logLder(4))},"table":[],"independent_summation_max_diff":0.0}
for n in N:
    row={"y":n,"channels":{}}
    for q in (0,3,4):
        a=b=0.0;direct=0.0;count=0
        for val,p,k,logp in terms:
            if val>n:break
            ch=1 if q==0 else 1-chi(p,q)**k
            a+=ch*logp/val
            b+=ch*logp
            direct+=ch*logp*max(1/val-1/n,0)
            if val<n and ch:count+=1
        s=a-b/n
        assert abs(s-direct)<1e-10,(n,q,s,direct)
        result['independent_summation_max_diff']=max(result['independent_summation_max_diff'],abs(s-direct))
        main=math.log(n)-1-float(mp.euler)+(constants[q] if q else 0)
        row['channels'][str(q)]={"sum":s,"main":main,"residual":s-main,"active_terms":count}
    result['table'].append(row)
print(json.dumps(result,indent=2))
with open('/mnt/data/riemann_20261123_1431_prime_bridge.json','w') as f:json.dump(result,f,indent=2)
