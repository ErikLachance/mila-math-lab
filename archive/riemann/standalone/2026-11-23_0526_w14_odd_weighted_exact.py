#!/usr/bin/env python3
"""Certified rational odd-parity Weil lower bound on width-1/14 endpoint collars,
conditional on the standard signed Weil explicit formula & its form-domain extension.
NOT a Riemann hypothesis proof; no test of general full-window positivity.
"""
from fractions import Fraction as F
from math import isqrt,factorial
from time import monotonic
import json
from pathlib import Path
start=monotonic()
L=F(81,100);w=F(1,14);v=1/L
DLO=F(1056,100000);DHI=F(1057,100000)
PILO=F(314159,100000);PIHI=F(314160,100000)
H0=-F(269,50); C5=F(18,25); SU=F(5,12)
N=400; CELLS=480; S=10**10; PBINS=256; ROOT_SCALE=10**8

# Exact rational checks of every external constant.
def arctan_bracket(z,n):
 t=sum(((-1)**k*z**(2*k+1)/F(2*k+1) for k in range(n)),F(0)); rem=z**(2*n+1)/F(2*n+1)
 return (t,t+rem) if n%2==0 else (t-rem,t)
a0,a1=arctan_bracket(F(1,5),10);b0,b1=arctan_bracket(F(1,239),4)
assert PILO<16*a0-4*b1 < 16*a1-4*b0<PIHI
def log_bracket(z,n):
 y=(z-1)/(z+1); t=y; out=F(0)
 for k in range(n):out+=2*t/F(2*k+1);t*=y*y
 return out,out+2*t/(F(2*n+1)*(1-y*y))
ln5lo,ln5hi=log_bracket(F(5),100)
assert DLO<2*L-ln5hi<2*L-ln5lo<DHI
ln2lo,ln2hi=log_bracket(F(2),40);lnpilo,lnpihi=log_bracket(PIHI,100)
gamma_hi=sum((F(1,i) for i in range(1,65)),F(0))-6*ln2lo-F(1,128)+F(1,12*64**2)
assert -gamma_hi-PIHI/2-3*ln2hi-lnpihi>H0
assert F(2236,1000)**2<5 and ln5hi/F(2236,1000)<C5
x=L/2; su=sum((x**(2*k+1)/factorial(2*k+1) for k in range(6)),F(0))+(x**13/factorial(13))/(1-x*x/F(14*15))
assert su<SU

def sqrt_up(z):
 if z==0:return F(0)
 n=isqrt(z.numerator*ROOT_SCALE**2//z.denominator)+1
 q=F(n,ROOT_SCALE); assert q*q>z
 return q

def hpos_lower(t):
 # Exact floor each positive finite digamma summand to scale 1/S.
 num=t.numerator;den=t.denominator;u=num*num
 ans=0
 for n in range(N):
  a=4*n+1
  ans+=(S*16*u)//(a*(den*den*a*a+4*u))
 return F(ans,S)

# Rational lower of L^2 integral_0^v t² H(t)dt:
# H=H0 + positive increasing series; sample t²*[H-H0] from left.
I2=L*L*(H0*v**3/3 + (v/F(CELLS))*sum(((v*F(i,CELLS))**2 * hpos_lower(v*F(i,CELLS)) for i in range(CELLS)),F(0)))
print('I2 weighted lower',float(I2),flush=True)
Ts=[F(k,2) for k in range(40,73)]
terms=[]
for T in Ts:
  h=H0+hpos_lower(T)
  if T<=v:continue
  I1=H0*(T-v)+(T-v)*sum((hpos_lower(v+(T-v)*F(i,CELLS)) for i in range(CELLS)),F(0))/CELLS
  # The effective cap mass on symmetric [-T,T] is 2M [T - 2v/3].
  a=T-F(2,3)*v
  I=I2+I1
  assert I<a*h, 'increasing H and cap imply average < endpoint'
  terms.append((T,h,I,a))
print('number of candidates',len(terms),flush=True)

worst=(F(1000),None,None)
used_T={}
for j in range(PBINS):
  pL=F(j,PBINS);pR=F(j+1,PBINS)
  cap=(sqrt_up(DHI*pR)+sqrt_up((w-DLO)*(1-pL)))**2/PILO
  cap=min(cap,w/PILO)
  best=(F(-1000),None)
  for T,h,I,a in terms:
    if 2*cap*a>=1:continue
    result=h+2*cap*(I-a*h)
    if result>best[0]:best=(result,T)
  assert best[1] is not None
  qlow=best[0]-C5*pR-4*w*SU**2
  if qlow<worst[0]:worst=(qlow,j,best[1])
  used_T[str(best[1])]=used_T.get(str(best[1]),0)+1
print('worst conservative exact rational lower display',float(worst[0]),'pbin',worst[1],'T',worst[2],flush=True)
print('all > 1/50?',worst[0]>F(1,50),'all > 1/25?',worst[0]>F(1,25),flush=True)
report={'date':'2026-11-23','L':'81/100','w':'1/14','parity':'odd only',
        'kind':'rational fraction interval sufficient positive Weil form restricted support; conditional on correct signed form',
        'worst_bound_float_display':float(worst[0]), 'p_bin':worst[1],'T':str(worst[2]),
        'passes_Q_gt_1_over_50':worst[0]>F(1,50),'passes_Q_gt_1_over_25':worst[0]>F(1,25),
        'cutoff_frequency':used_T,'grid_p':PBINS,'grid_integral':CELLS,'digamma_terms':N,
        'runtime_seconds':monotonic()-start,'status':'NOT RH proof, odd only and restricted support'}
Path(__file__).with_suffix('.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
