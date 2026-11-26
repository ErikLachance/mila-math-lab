#!/usr/bin/env python3
"""Rational p/q grid even-parity Fourier/pole bound at width 1/14.
All arithmetic decisions exact Fraction; hypothesis: standard signed Weil form
on smooth even compactly supported functions in two endpoint collars.
This is NOT a proof of whole-interval Weil positivity or RH.
"""
from fractions import Fraction as F
from math import isqrt,factorial
from time import monotonic
from pathlib import Path
import json
start=monotonic()
L=F(81,100); w=F(1,14); tau=F(7,10)
DLO=F(1056,100000);DHI=F(1057,100000);PILO=F(314159,100000);PIHI=F(314160,100000)
H0_LO=-F(269,50);H0_HI=-F(537,100);C5=F(18,25)
N=400;K=512;S=10**10;R=10**8;PB=128;QB=128

def lgbr(z,n):
 y=(z-1)/(z+1);v=y;s=F(0)
 for j in range(n):s+=2*v/(2*j+1);v*=y*y
 return s,s+2*v/((2*n+1)*(1-y*y))
def at(z,n):
 v=sum(((-1)**j*z**(2*j+1)/(2*j+1) for j in range(n)),F(0));r=z**(2*n+1)/(2*n+1)
 return (v,v+r) if n%2==0 else (v-r,v)
alpha,beta=at(F(1,5),10);c,d=at(F(1,239),4)
assert PILO<16*alpha-4*d and 16*beta-4*c<PIHI
ln2lo,ln2hi=lgbr(F(2),40);lnpilo,lnpihi=lgbr(PIHI,100)
log5lo,log5hi=lgbr(F(5),100)
assert DLO<2*L-log5hi<2*L-log5lo<DHI
harm=sum((F(1,j) for j in range(1,65)),F(0))
gamma_hi=harm-6*ln2lo-F(1,128)+F(1,12*64**2)
gamma_lo=harm-6*ln2hi-F(1,128)+F(1,12*64**2)-F(1,120*64**4)
assert -gamma_hi-PIHI/2-3*ln2hi-lnpihi>H0_LO
assert -gamma_lo-PILO/2-3*ln2lo-lnpilo<H0_HI
assert log5hi/F(2236,1000)<C5 and F(2236,1000)**2<5
x=L/2
from math import factorial
hyper=sum((x**(2*j+1)/factorial(2*j+1) for j in range(6)),F(0))+(x**13/factorial(13))/(1-x*x/F(14*15))
assert hyper<F(5,12)

def sqlo(z):
 if z==0:return F(0)
 n=isqrt(z.numerator*R*R//z.denominator);v=F(n,R);assert v*v<=z;return v

def squp(z):
 if z==0:return F(0)
 n=isqrt(z.numerator*R*R//z.denominator)+1;v=F(n,R);assert v*v>z;return v

def plus_lo(t):
 u=t.numerator*t.numerator;v=t.denominator*t.denominator
 return F(sum((S*16*u)//(a*(v*a*a+4*u)) for a in (4*j+1 for j in range(N))),S)

def plus_up(t):
 # positive finite 400-term digamma bound rounded UP + series tail <= t²/(8*(N-1)²)
 u=t.numerator*t.numerator;v=t.denominator*t.denominator
 ans=F(sum(((S*16*u)//(a*(v*a*a+4*u))+1) for a in (4*j+1 for j in range(N))),S)
 return ans + t*t/F(8*(N-1)**2)

upper_tau=tau*H0_HI + tau*sum((plus_up(tau*F(i+1,K)) for i in range(K)),F(0))/K
print('I(tau) upper',float(upper_tau),flush=True)
Ts=[F(j,2) for j in range(40,67)]
coeff=[]
for T in Ts:
 h=H0_LO+plus_lo(T)
 I=H0_LO*T + T*sum((plus_lo(T*F(i,K)) for i in range(K)),F(0))/K
 assert I<T*h and tau*h>upper_tau
 coeff.append((T,h,I,tau*h-upper_tau))

sqrtw=squp(2*w);D=sqrtw*L*L*(tau*tau/2+F(11,80))
qmax=2*w*F(11,10)**2
worst=(F(100),None,None,None)
fail_counts=0
for pidx in range(PB):
 p0=F(pidx,PB);p1=F(pidx+1,PB)
 mu=min((squp(DHI*p1)+squp((w-DLO)*(1-p0)))**2/PILO,w/PILO)
 ml=(sqlo(DLO*p0)+sqlo((w-DHI)*(1-p1)))**2/PIHI
 for qidx in range(QB):
  q0=qmax*F(qidx,QB);q1=qmax*F(qidx+1,QB)
  lowcap=(squp(q1)+D)**2/(2*PILO)
  improvement=max(F(0),ml-lowcap)
  best=(F(-100),None)
  for T,h,I,diff in coeff:
   if 2*mu*T>=1:continue
   lower=h+2*mu*(I-T*h)+2*improvement*diff+2*q0-C5*p1
   if lower>best[0]:best=(lower,T)
  if best[1] is None:fail_counts+=1;continue
  if best[0]<worst[0]:worst=(best[0],pidx,qidx,best[1])
print('worst=',float(worst[0]),'p',worst[1],'q',worst[2],'T',worst[3], 'fails',fail_counts,'Q>0',worst[0]>0,flush=True)
rep={'L':'81/100','w':'1/14','parity':'even','result_type':'conditional exact rational grid sufficient certificate','Qpositive':worst[0]>0 and fail_counts==0,'worst_display':float(worst[0]),'worst_pbin':worst[1],'worst_qbin':worst[2],'cutoff':str(worst[3]),'fail_bins':fail_counts,'p_bins':PB,'q_bins':QB,'runtime_s':monotonic()-start}
Path(__file__).with_suffix('.json').write_text(json.dumps(rep,indent=2))
print(json.dumps(rep,indent=2))
