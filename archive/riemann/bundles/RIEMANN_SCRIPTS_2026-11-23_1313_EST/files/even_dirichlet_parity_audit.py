from mpmath import mp
from sympy import primerange
import json
mp.dps=65
q=5;char=[0,1,-1,-1,1]
L=lambda s:mp.dirichlet(s,char)
L0=L(0);L0p=mp.dirichlet(0,char,1);H=lambda s:mp.power(5,-s)*(mp.zeta(s,mp.mpf(1)/5)-mp.zeta(s,mp.mpf(2)/5)-mp.zeta(s,mp.mpf(3)/5)+mp.zeta(s,mp.mpf(4)/5))
L0pp=mp.diff(H,mp.mpf(0),2)
d=L0pp/(2*L0p)
c=mp.dirichlet(1,char,1)/L(1)
K0=1+d
K1=mp.log(q/mp.pi)-mp.euler-2*mp.log(2)+2*c
K2=c-d-mp.log(2)
print('even quadratic character modulo 5')
for name,val in [('L0',L0),('L0prime',L0p),('L0doubleprime',L0pp),('d',d),('c',c),('K0',K0),('K1',K1),('K2',K2),('difference',K1-K2)]:print(name,mp.nstr(val,40))
def T(x):
 x=mp.mpf(x)
 if x==1:return 1-mp.log(2)
 return mp.nsum(lambda k:mp.power(x,-2*k)/(2*k*(2*k+1)),[1,mp.inf])
maxx=100000
seq=[]
for p in primerange(2,maxx+1):
 n=int(p)
 while n<=maxx:
  seq.append((n,mp.log(int(p)),char[n%q]));n*=int(p)
seq.sort()
res=[]
for x in [1,2,3,4,5,6,10,100,1000,10000,100000]:
 g= sum(l*h*(mp.mpf(x)/n-1) for n,l,h in seq if n<=x)+c*x
 spectral=g-mp.log(x)-K0+T(x)
 ratio=abs(spectral)/mp.sqrt(x)
 r={'x':x,'G5':mp.nstr(g,30),'spectral':mp.nstr(spectral,30),'ratio':mp.nstr(ratio,30),'slack':mp.nstr(K1-ratio,20)}
 res.append(r);print(r)
with open('/mnt/data/riemann_20261123_1253/even_dirichlet_parity_audit.json','w') as f:json.dump({'L0':str(L0),'L0p':str(L0p),'L0pp':str(L0pp),'d':str(d),'c':str(c),'C5':str(K1),'C5b':str(K2),'results':res},f,indent=2)
