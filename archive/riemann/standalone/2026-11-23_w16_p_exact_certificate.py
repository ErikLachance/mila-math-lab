#!/usr/bin/env python3
"""All-rational positivity lower bound for signed Weil form on two 1/16 endpoint collars.
Conditional on the standard explicit Weil formula; no RH input or float decisions.
"""
from fractions import Fraction as F
from math import isqrt,factorial
import time,json
start=time.monotonic()
L=F(81,100);w=F(1,16);DLO=F(1056,100000);DHI=F(1057,100000)
PILO=F(314159,100000);PIHI=F(314160,100000)
H0=-F(269,50);C5=F(18,25);SU=F(5,12)
A=F(25); N=320; M=512; S=10**10; PBINS=128
# Lower digamma symbol H via H(0)> -269/50 and series of positive terms.
# H(t) increasing for t>=0; left Riemann sum gives integral lower.
q=A.denominator*M; u=A.numerator
summed=0
for i in range(M):
 p=u*i; pp=p*p
 for n in range(N):
  a=4*n+1
  summed += (S*16*pp)//(a*(q*q*a*a+4*pp))
I=A*(H0+F(summed,M*S))
q=A.denominator;u=A.numerator;pp=u*u
h=H0+F(sum((S*16*pp)//(a*(q*q*a*a+4*pp)) for a in (4*n+1 for n in range(N))),S)
assert I>0 and h>0
# verify delta bounds: delta=1.62-log5 with atanh series and positive tail
# log5=2sum_{k>=0} (2/3)^(2k+1)/(2k+1)
y=F(2,3);term=y;lo=F(0)
for k in range(100):
 lo+=2*term/(2*k+1)
 term*=y*y
up=lo+2*term/((2*100+1)*(1-y*y))
assert F(81,50)-up>DLO and F(81,50)-lo<DHI
# pi coarse bounds can be proved by Machin alternating sums with exact rational terms.
def atan_int(x,N):
 ss=sum(((-1)**k*x**(2*k+1)/F(2*k+1) for k in range(N)),F(0))
 rr=x**(2*N+1)/F(2*N+1)
 return (ss,ss+rr) if N%2==0 else (ss-rr,ss)
a,b=atan_int(F(1,5),10);c,d=atan_int(F(1,239),4)
assert PILO < 16*a-4*d and 16*b-4*c < PIHI
# sqrt F rational rounded UP with exact integer inequality
ROOT_SCALE=10**7
def sqrt_upper(z):
 if not z:return F(0)
 t=isqrt(z.numerator*ROOT_SCALE*ROOT_SCALE//z.denominator)+1
 assert F(t*t,ROOT_SCALE*ROOT_SCALE)>z
 return F(t,ROOT_SCALE)

worst=(F(100),None)
for j in range(PBINS):
 a=F(j,PBINS);b=F(j+1,PBINS)
 s1=sqrt_upper(DHI*b)
 s2=sqrt_upper((w-DLO)*(1-a))
 mupper=min((s1+s2)**2/PILO,w/PILO)
 assert 2*mupper*A<1
 # All quantities positive where required. Since I-A*h<0, using upper M is safe.
 assert I-A*h<0
 arch=h+2*mupper*(I-A*h)
 qlb=arch-C5*b-4*w*SU*SU
 if qlb<worst[0]:worst=(qlb,j)
print('I lower:',float(I),'H(25) lower:',float(h))
print('worst p interval:',worst[1],PBINS,'lower Q:',float(worst[0]),'pass 0.05?',worst[0]>F(1,20))
assert worst[0]>F(1,20)
report={'L':'81/100','w':'1/16','T0':25,'digamma_terms':N,'quad_bins':M,'p_bins':PBINS,'integer_floor_scale':S,'sqrt_scale':ROOT_SCALE,'worst_p_bin':worst[1], 'Qlower_decimal':float(worst[0]),'rigorous_Q_gt_1_over_20':worst[0]>F(1,20),'work_s':time.monotonic()-start}
with open('/mnt/data/riemann_research_20261123/w16_p_exact_certificate.json','w') as f:json.dump(report,f,indent=2)
print(json.dumps(report,indent=2))
