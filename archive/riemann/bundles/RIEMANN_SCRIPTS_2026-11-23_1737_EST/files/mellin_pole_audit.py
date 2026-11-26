import mpmath as mp, json, math
mp.mp.dps=75

def chi4(n):
    k=n%4
    return 1 if k==1 else (-1 if k==3 else 0)
def dirbeta(s):
    return mp.dirichlet(s,[0,1,0,-1])
def kappa(s):
    return mp.diff(dirbeta,s)/dirbeta(s)
kap=kappa(mp.mpf(1));dkap=mp.diff(kappa,mp.mpf(1))

def F4(s):
    return -kappa(s)/(s*(s-1))+kap/(s-1)
limit4=kap-dkap

def zeta_center(s):
    return -mp.diff(mp.zeta,s)/mp.zeta(s)/(s*(s-1))-(s-1)**(-2)+(1+mp.euler)/(s-1)
limitZ=1+mp.euler+mp.euler**2+2*mp.stieltjes(1)

def primes(N):
    sieve=bytearray(b'\x01')*(N+1)
    sieve[:2]=b'\x00\x00'
    for i in range(2,math.isqrt(N)+1):
        if sieve[i]:sieve[i*i:N+1:i]=b'\x00'*((N-i*i)//i+1)
    return [i for i in range(N+1) if sieve[i]]
pp=primes(200000)

def euler_log_deriv(s):
    return mp.fsum([mp.log(p)*chi4(p)*mp.power(p,-s)/(1-chi4(p)*mp.power(p,-s)) for p in pp if chi4(p)])

checks=[]
for h in ['0.1','0.0001','0.00000001','0.000000000001']:
    w=mp.mpf(h)
    checks.append({'near':'1+'+h,'F4':mp.nstr(F4(1+w),25),'limit4':mp.nstr(limit4,25),'error4':mp.nstr(F4(1+w)-limit4,10),'Fzeta':mp.nstr(zeta_center(1+w),25),'limitZ':mp.nstr(limitZ,25),'errorZ':mp.nstr(zeta_center(1+w)-limitZ,10)})
series=[]
for sr,si in [('3','0'),('3','0.3'),('2.5','0.7')]:
    s=mp.mpc(mp.mpf(sr),mp.mpf(si));approx=euler_log_deriv(s);actual=-kappa(s)
    series.append({'s':str(s),'primes':len(pp),'euler_partial':mp.nstr(approx,25),'true_negative_log_derivative':mp.nstr(actual,25),'abs_diff':mp.nstr(abs(actual-approx),12),'general_absolute_tail_bound':mp.nstr((mp.log(200000)/(s.real-1)+1/(s.real-1)**2)*(200000**(1-s.real))*1.2,12)})

data={'κchi4':mp.nstr(kap,55),'κprimechi4':mp.nstr(dkap,55),'chi4_reg_limit':mp.nstr(limit4,55),'zeta_reg_limit':mp.nstr(limitZ,55),'checks':checks,'euler':series}
open('/mnt/data/riemann_20261123_1728/mellin_pole_audit.json','w').write(json.dumps(data,indent=2,ensure_ascii=False))
print(json.dumps(data,indent=2,ensure_ascii=False))
