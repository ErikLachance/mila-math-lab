import mpmath as mp, json, math
mp.mp.dps=80
a,b=mp.mpf(1)/4,mp.mpf(3)/4
D=[mp.stieltjes(k,a)-mp.stieltjes(k,b) for k in range(9)]

def S(z):return mp.fsum([(-z)**k*D[k]/mp.factorial(k) for k in range(len(D))])
def Sp(z):return mp.fsum([(-1)**k*z**(k-1)*D[k]/mp.factorial(k-1) for k in range(1,len(D))])
def Spp(z):return mp.fsum([(-1)**k*z**(k-2)*D[k]/mp.factorial(k-2) for k in range(2,len(D))])
def κ(s):
 z=s-1
 if abs(z)<mp.mpf('0.12'):return -mp.log(4)+Sp(z)/S(z)
 beta=lambda t:mp.dirichlet(t,[0,1,0,-1])
 return mp.diff(beta,s)/beta(s)
k0=κ(mp.mpf(1));dk=Spp(0)/S(0)-(Sp(0)/S(0))**2
assert abs(S(0)/4-mp.pi/4)<mp.mpf('1e-70')
lim4=k0-dk

def F4(s):return (-κ(s)/s+k0)/(s-1)
def zeta_center(s):
 return -mp.diff(mp.zeta,s)/mp.zeta(s)/(s*(s-1))-(s-1)**(-2)+(1+mp.euler)/(s-1)
limz=1+mp.euler+mp.euler**2+2*mp.stieltjes(1)
checks=[]
for h in ['0.1','0.0001','0.00000001','0.000000000001']:
 z=mp.mpf(h);f=F4(1+z);g=zeta_center(1+z)
 checks.append({'h':h,'F4':mp.nstr(f,27),'F4_limit':mp.nstr(lim4,27),'error_F4':mp.nstr(f-lim4,12),'F_zeta':mp.nstr(g,27),'F_zeta_limit':mp.nstr(limz,27),'error_F_zeta':mp.nstr(g-limz,12)})
result={'beta_log_derivative_1':mp.nstr(k0,30),'beta_log_derivative_derivative_1':mp.nstr(dk,30),'beta_regularized_Mellin_at_1':mp.nstr(lim4,35),'zeta_regularized_Mellin_at_1':mp.nstr(limz,35),'checks':checks,'original_numerical_failure':'A naive evaluation of the Hurwitz zeta difference at s=1 and derivative-based evaluation near s=1 produce NaN and spurious large values. Resolved by Laurent series of Hurwitz zeta with generalized Stieltjes constants.'}
open('/mnt/data/riemann_20261123_1728/mellin_stable.json','w').write(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
