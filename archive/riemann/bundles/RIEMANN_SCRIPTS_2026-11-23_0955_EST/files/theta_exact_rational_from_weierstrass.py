#!/usr/bin/env python3
"""Exact rational theta normalized coefficients from Weierstrass ODE g2=4,g3=0."""
from fractions import Fraction as F
import json, math
K=180
B=[F(1),F(1,5)]
for k in range(2,K+1):
    den=(4*k-2)*(4*k-3)-12
    assert den!=0
    B.append(F(6)*sum(B[j]*B[k-j] for j in range(1,k))/den)
# log((sigma(u)/u)^2) via second derivative = -2(wp(u)-u^-2): series x=u^4
S=[F(0)]+[-2*B[k]/((4*k-1)*(4*k)) for k in range(1,K+1)]
E=[F(1)]
for n in range(1,K+1):
    E.append(sum(j*S[j]*E[n-j] for j in range(1,n+1))/n)
Fcoeff=[sum(B[j]*E[k-j] for j in range(k+1)) for k in range(K+1)]
r=[F(math.factorial(4*k),16**k)*Fcoeff[k] for k in range(K+1)]
expected={1:F(1,4),2:F(17,16),3:F(-111,64),4:F(12513,256),5:F(-146079,1024)}
assert all(r[k]==v for k,v in expected.items())
# published denominators: r_k denominator divides 4^k
assert all((4**k*r[k]).denominator==1 for k in range(K+1))

def vp_fraction(fr,p):
    assert fr !=0
    a=abs(fr.numerator); b=fr.denominator
    ans=0
    while a%p==0:a//=p;ans+=1
    while b%p==0:b//=p;ans-=1
    return ans
assert vp_fraction(r[30],3)==14,('r30 v3',vp_fraction(r[30],3))
print('EXACT R k1..5', [str(r[i]) for i in range(1,6)])
print('EXACT v3(r30)',vp_fraction(r[30],3),'digits num',len(str(abs(r[30].numerator))),'den',r[30].denominator)
print('r20..r30 v3',[vp_fraction(r[i],3) for i in range(20,31)])
res={'ODE':'wp_dd=6*wp^2-2; wp=u^-2 + sum_{k>=1} B_k*u^(4k-2); B_1=1/5; B_k=6 sum B_j B_(k-j)/((4k-2)*(4k-3)-12)','formal_sigma':'sigma(u)=u exp(S(u)); S_second=-(wp-u^-2); theta/T0=sigma(u)^2 wp(u)','max_k':K,'all_denominators_divide_4_pow_k':True,'first_values':[str(r[i]) for i in range(6)],'v3_r30':vp_fraction(r[30],3),'v3_r20_r40':{str(i):vp_fraction(r[i],3) for i in range(20,41)},'r30_numerator_digits':len(str(abs(r[30].numerator))),'r30_denominator':str(r[30].denominator),'warning':'Exact equality of theta and sigma/wp is quoted from Rubinstein Theorem Le6; this script independently computes consequences of that equality and ODE, but does NOT re-prove the theta-sigma identity nor prove the RH.'}
with open('/mnt/data/riemann_20261123_0936/theta_exact_rational_from_weierstrass.json','w') as f:json.dump(res,f,indent=2)
print('PASS',K,'exact rational coefficient and denominator claims; r30 v3 14 reproduced')
