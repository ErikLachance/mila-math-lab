import json,math,time
from collections import defaultdict

def vmod(z,p,M):
    if z%p: return 0
    if z==0: return M
    v=0
    while z%p==0 and v<M:
        z//=p;v+=1
    return v

def deriv(A,B,fcoeff,mod):
    # f(x)= sum_j fcoeff[j] x^j; D A=2A' y, D(By)=2f B'+f' B
    C=defaultdict(int)
    E=defaultdict(int)
    for k,b in B.items():
        if k:
            for j,fj in fcoeff.items():
                C[j+k-1]+=(2*k*fj*b)
        for j,fj in fcoeff.items():
            if j: C[j+k-1]+=j*fj*b
    for k,a in A.items():
        if k: E[k-1]+=2*k*a
    return ({k:v%mod for k,v in C.items() if v%mod}, {k:v%mod for k,v in E.items() if v%mod})

def test(p,f,upto,degree):
    M=upto//p+upto//(p**3)+6
    mod=p**M
    bad=[];mins=[];cases=0;floorhits=0
    for branch in ('A','B'):
        for d in range(degree+1):
            A,B=({d:1},{}) if branch=='A' else ({},{d:1})
            for a in range(1,upto+1):
                A,B=deriv(A,B,f,mod)
                w=min([vmod(x,p,M) for x in list(A.values())+list(B.values())] or [M])
                t=a//p+a//(p**3)
                cases+=1
                if w==t: floorhits+=1
                if w<t and len(bad)<60:
                    bad.append({'branch':branch,'d':d,'a':a,'minimum_val':w,'target':t})
                if a in (p,p*p,p**3,2*p**3,upto):
                    mins.append({'branch':branch,'d':d,'a':a,'v':w,'target':t})
    return {'p':p,'polynomial':f,'upto':upto,'degree':degree,'cases':cases,'hits_at_bound':floorhits,'violations':bad,'checkpoints':mins,'precision':M}

t0=time.time();tests=[test(5,{3:1,0:-1},260,15),test(7,{3:1,1:-1},350,10)]
res={'elapsed_wall_seconds':time.time()-t0,'tests':tests}
with open('/mnt/data/riemann_20261123_1728/derivation_extension.json','w') as h:json.dump(res,h,indent=2)
for t in tests:print(t['p'], 'tests',t['cases'],'bad',t['violations'][:12],'hits',t['hits_at_bound'],'atN', [x for x in t['checkpoints'] if x['a']==t['p']**3][:8])
print('elapsed',res['elapsed_wall_seconds'])
