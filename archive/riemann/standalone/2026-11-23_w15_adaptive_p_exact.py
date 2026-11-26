#!/usr/bin/env python3
"""All-rational bin-grid Weil positivity test on two width-1/15 endpoint collars.
A finite max over legal monotone digamma tangents avoids a global cutoff loss.
"""
from fractions import Fraction as F
from math import isqrt
import time,json
start=time.monotonic()
L=F(81,100);w=F(1,15);DLO=F(1056,100000);DHI=F(1057,100000)
PILO=F(314159,100000);PIHI=F(314160,100000)
H0=-F(269,50);C5=F(18,25);SU=F(5,12)
N=400; M=768; S=10**10; PBINS=256; ROOT_SCALE=10**8
cutoffs=[F(47,2),F(24),F(25),F(26),F(27),F(28),F(29),F(30),F(32),F(36),F(40)]
# Derive DLO<D=2L-log5<DHI with rational atanh series.
y=F(2,3);term=y;loglo=F(0)
for k in range(100):loglo+=2*term/(2*k+1);term*=y*y
loghi=loglo+2*term/((201)*(1-y*y))
assert 2*L-loghi>DLO and 2*L-loglo<DHI
# Derive PILO<pi<PIHI using exact Machin arctan alternating remainder.
def at(x,N):
 ss=sum(((-1)**k*x**(2*k+1)/(2*k+1) for k in range(N)),F(0))
 rr=x**(2*N+1)/(2*N+1)
 return (ss,ss+rr) if N%2==0 else (ss-rr,ss)
a,b=at(F(1,5),10);c,d=at(F(1,239),4)
assert PILO<16*a-4*d and 16*b-4*c<PIHI
# Independently verify ALL three coarse constants used by the certificate.
def log_bracket(z,N):
    y=(z-1)/(z+1);v=F(0);term=y
    for k in range(N):
        v+=2*term/(2*k+1);term*=y*y
    return v,v+2*term/((2*N+1)*(1-y*y))
ln2lo,ln2hi=log_bracket(F(2),40)
lnpi_lo,lnpi_hi=log_bracket(PIHI,100)
gamma_hi=sum((F(1,i) for i in range(1,65)),F(0))-6*ln2lo-F(1,128)+F(1,12*64**2)
H0_rigor_lower=-gamma_hi-PIHI/2-3*ln2hi-lnpi_hi
assert H0_rigor_lower>H0
sqrt5lo=F(2236,1000)
assert sqrt5lo*sqrt5lo<5
assert loghi/sqrt5lo<C5
from math import factorial
x=F(81,200)
sinh_partial=sum((x**(2*k+1)/factorial(2*k+1) for k in range(6)),F(0))
sinh_bound=sinh_partial+(x**13/factorial(13))/(1-x*x/F(14*15))
assert sinh_bound<SU

def root_up(z):
 if z==0:return F(0)
 k=isqrt((z.numerator*ROOT_SCALE**2)//z.denominator)+1
 result=F(k,ROOT_SCALE)
 assert result*result>z
 return result

info=[]
for T in cutoffs:
 pp=T.numerator;qq=T.denominator*M
 tot=0
 for i in range(M):
  p=pp*i;u=p*p
  for n in range(N):
   an=4*n+1
   tot+=(S*16*u)//(an*(qq*qq*an*an+4*u))
 I=T*(H0+F(tot,M*S))
 u=pp*pp;qq=T.denominator
 tot=sum((S*16*u)//(an*(qq*qq*an*an+4*u)) for an in (4*n+1 for n in range(N)))
 h=H0+F(tot,S)
 assert I>0 and h>0 and I-T*h<0
 info.append((T,I,h))
 print('T=',float(T),'I=',float(I),'h=',float(h),flush=True)

worst=(F(100),None,None)
for j in range(PBINS):
 pa=F(j,PBINS);pb=F(j+1,PBINS)
 ss=root_up(DHI*pb)+root_up((w-DLO)*(1-pa))
 mu=min(ss*ss/PILO,w/PILO)
 best=(F(-100),None)
 for T,I,h in info:
  if 2*mu*T>=1:continue
  a=h+2*mu*(I-T*h)
  if a>best[0]:best=(a,T)
 assert best[1] is not None
 qlower=best[0]-C5*pb-4*w*SU**2
 if qlower<worst[0]:worst=(qlower,j,best[1])
print('worst=',float(worst[0]),'bin=',worst[1],'cut=',worst[2], 'Q positive',worst[0]>0,'Qgt0.001',worst[0]>F(1,1000),flush=True)
output={'L':'81/100','w':'1/15','P':PBINS,'N':N,'M':M,'grid_cutoffs':list(map(str,cutoffs)),'worst_lower':str(float(worst[0])),'worst_bin':worst[1],'selected_cutoff_at_worst':str(worst[2]),'Q_positive':worst[0]>0,'elapsed_sec':time.monotonic()-start}
with open('/mnt/data/riemann_research_20261123/w15_adaptive_p_exact.json','w') as f:json.dump(output,f,indent=2)
print(json.dumps(output,indent=2))
