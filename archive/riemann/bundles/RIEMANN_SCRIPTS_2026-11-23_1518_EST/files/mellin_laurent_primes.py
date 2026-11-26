import math,mpmath as mp,json,time
from sympy import primerange
T0=time.perf_counter()
X=[10000,100000,1000000,2000000]
maxx=max(X)
pp=[]
for p in primerange(2,maxx+1):
 k=p
 while k<=maxx:
  pp.append((k,math.log(p)))
  if k>maxx//p: break
  k*=p
pp.sort()
row=[]
for x in X:
 contrib=[lamb*(x/n-1.) for n,lamb in pp if n<=x]
 s=math.fsum(contrib)
 G=s-x*math.log(x)+(1+float(mp.euler))*x
 alt=x*math.fsum(lamb/n for n,lamb in pp if n<=x)-math.fsum(lamb for n,lamb in pp if n<=x)-x*math.log(x)+(1+float(mp.euler))*x
 row.append({'x':x,'G':G,'G_alternate':alt,'difference':G-alt})
mp.mp.dps=90
g=mp.euler;g1=mp.stieltjes(1)
laurent_constant=1+g+g*g+2*g1
near=[]
for k in [5,10,15,20,30]:
 h=mp.mpf(10)**(-k)
 s=1+h
 F=(-mp.diff(mp.zeta,s)/mp.zeta(s))/(s*(s-1))-1/((s-1)**2)+(1+g)/(s-1)
 near.append({'h_exponent':-k,'value':mp.nstr(F,28),'deviation':mp.nstr(F-laurent_constant,12)})
constant=2+g-mp.log(4*mp.pi)
partial=[]
for N in [5,15,40,100]:
 # RH-side computation: summing ±positive imaginary zeros as pairs; no proof that all zeros lie on line
 a=mp.mpf(0)
 for j in range(1,N+1):
  gamma=mp.im(mp.zetazero(j))
  a+=2/(gamma**2+mp.mpf('0.25'))
 partial.append({'N_pairs':N,'sum':mp.nstr(a,25),'remaining':mp.nstr(constant-a,16)})
res={'all_prime_powers_to':maxx,'prime_power_count':len(pp),'G':row,'F_at_1_exact_identity':'1+gamma+gamma^2+2*gamma_1','F_at_1_value':mp.nstr(laurent_constant,32),'s_to_1_plus':near,'positive_RH_weight_constant':mp.nstr(constant,32),'partial_sums_nontrivial_zeros':partial,'runtime_s':time.perf_counter()-T0}
print(json.dumps(res,indent=2))
with open('/mnt/data/riemann_run_20261123_1457/mellin_laurent_primes.json','w') as f:json.dump(res,f,indent=2)
