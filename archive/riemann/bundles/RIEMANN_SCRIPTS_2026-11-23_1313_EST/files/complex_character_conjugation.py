from mpmath import mp
from sympy import primerange
import json
mp.dps=35
q=5
ch=[0,1,mp.j,-mp.j,-1]
L=lambda s:mp.dirichlet(s,ch)
P=sum(ch[a]*mp.digamma(mp.mpf(a)/q) for a in range(1,q))
V=sum(ch[a]*mp.stieltjes(1,mp.mpf(a)/q) for a in range(1,q))
L1=-P/q
L1prime=(-V+mp.log(q)*P)/q
C1=L1prime/L1
L0=sum(ch[a]*(mp.mpf(1)/2-mp.mpf(a)/q) for a in range(1,q))
L0prime=sum(ch[a]*mp.loggamma(mp.mpf(a)/q) for a in range(1,q))-mp.log(q)*L0
C0=L0prime/L0
Ctheory=mp.log(5/mp.pi)-mp.euler+2*mp.re(C1)
Cboundary=C1-C0+mp.log(2)
print('order4 mod5 c=',mp.nstr(C1,45),'c0=',mp.nstr(C0,45))
print('C from completed L=',mp.nstr(Ctheory,40))
print('C from boundary=',mp.nstr(Cboundary,40),'residual=',mp.nstr(Ctheory-Cboundary,15))
zeros=[]
seq=[]
for p in primerange(2,10001):
 n=int(p)
 while n<=10000:
  seq.append((n,mp.log(int(p)),ch[n%q]));n*=int(p)
seq.sort()
def T(x):
 if x==1:return mp.log(2)
 x=mp.mpf(x);t=1/x
 return mp.atanh(t)+x*mp.log(1-t*t)/2
out=[]
for x in [1,2,3,5,10,100,1000,10000]:
 g=sum(l*h*(mp.mpf(x)/n-1) for n,l,h in seq if n<=x)+C1*x
 spect=g-C0+T(x)
 ratio=abs(spect)/mp.sqrt(x)
 item={'x':x,'G_re':mp.nstr(mp.re(g),28),'G_im':mp.nstr(mp.im(g),28),'spect_re':mp.nstr(mp.re(spect),28),'spect_im':mp.nstr(mp.im(spect),28),'ratio':mp.nstr(ratio,28),'slack':mp.nstr(Ctheory-ratio,20)}
 out.append(item);print(item)
with open('/mnt/data/riemann_20261123_1253/complex_character_conjugation.json','w') as f:json.dump({'c':str(C1),'c0':str(C0),'C':str(Ctheory),'boundary':str(Cboundary),'tests':out},f,indent=2)
