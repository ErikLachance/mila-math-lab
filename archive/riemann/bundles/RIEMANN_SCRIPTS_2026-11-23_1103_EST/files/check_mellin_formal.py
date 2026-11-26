from math import log, isqrt, factorial
from fractions import Fraction
from collections import defaultdict
import json
import mpmath as mp
mp.mp.dps=50
N=100000
is_prime=bytearray([1])*(N+1);is_prime[0]=is_prime[1]=0
for p in range(2,isqrt(N)+1):
    if is_prime[p]:
        for k in range(p*p,N+1,p):is_prime[k]=0
prime_powers=[]
for p in range(2,N+1):
    if is_prime[p]:
        k=p
        while k<=N:
            prime_powers.append((k,p))
            k*=p
rows=[]
for s in [2,3,4]:
    a=mp.fsum(mp.log(p)/mp.mpf(k)**s for k,p in prime_powers)
    exact=-mp.diff(mp.zeta,s)/mp.zeta(s)
    residual=exact-a
    upper=mp.mpf(N)**(1-s)*(mp.log(N)/(s-1)+1/mp.mpf(s-1)**2)
    rows.append({'s':s,'N':N,'prime_power_terms':len(prime_powers), 'finite_sum':mp.nstr(a,25),'zeta_log_derivative':mp.nstr(exact,25),'positive_tail':mp.nstr(residual,18),'naive_integral_tail_upper':mp.nstr(upper,18),'tail_less_than_upper':bool(0<residual<upper)})
# Independent exact formal inverse test at p=3, deg 81
p=3;D=81

def mul(A,B):
    C={}
    for i,ai in A.items():
        for j,bj in B.items():
            if i+j<=D:C[i+j]=C.get(i+j,Fraction(0,1))+ai*bj
    return {i:v for i,v in C.items() if v}

def power(A,m):
    C={0:Fraction(1,1)}
    for i in range(m):C=mul(C,A)
    return C
# Extract U from Lagrange inverse as above (only terms deg 1 mod8)
from math import comb
U={1:Fraction(1,1)}
for k in range(1,11):
    a=1+8*k
    q=Fraction((-1)**k*comb(a+k-1,k), a*3**k)
    if a==81:q-=Fraction(1,9)
    U[a]=q
A=power(U,9);B=power(U,81)
recon=dict(U)
for degree,v in A.items():recon[degree]=recon.get(degree,Fraction(0,1))+v/3
for degree,v in B.items():recon[degree]=recon.get(degree,Fraction(0,1))+v/9
failures=[(i,str(c)) for i,c in recon.items() if c != (Fraction(1,1) if i==1 else Fraction(0,1))]
result={'mellin_prime_powers':rows,'formal_inverse':{'p':3,'max_degree':D,'nonzero_coefficients':len(U),'composition_l_of_U_equals_z_to_order_D':not failures,'failures':failures}}
with open('/mnt/data/riemann_runs/20261123_1047/check_mellin_formal.json','w') as f:json.dump(result,f,indent=2)
print(json.dumps(result,indent=2))
