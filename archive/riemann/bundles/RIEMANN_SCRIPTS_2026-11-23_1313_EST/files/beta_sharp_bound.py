from mpmath import mp
from sympy import primerange
import json
mp.dps=55
chi=[0,1,0,-1]
L=lambda s:mp.dirichlet(s,chi)
C1=mp.dirichlet(1,chi,1)/L(1)
C0=mp.dirichlet(0,chi,1)/L(0)
Csharp=mp.log(4/mp.pi)-mp.euler+2*C1
Cvia=C1-C0+mp.log(2)
print('L0',mp.nstr(L(0),25),'L1',mp.nstr(L(1),25))
print('C1',mp.nstr(C1,45),'C0',mp.nstr(C0,45))
print('Csharp',mp.nstr(Csharp,45),'Cvia',mp.nstr(Cvia,45),'diff',mp.nstr(Csharp-Cvia,12))
def Triv(x):
    x=mp.mpf(x)
    if x==1:return mp.log(2)
    t=1/x
    return mp.atanh(t)+(x/2)*mp.log(1-t*t)
xs=[1,2,3,10,100,275,1000,10000,100000]
pp=[]
for p in primerange(2,max(xs)+1):
 n=int(p)
 while n<=max(xs):
  h=0 if n%2==0 else (1 if n%4==1 else -1)
  pp.append((n,mp.log(int(p)),h));n*=int(p)
pp.sort()
out=[]
for x in xs:
 S=sum(l*h*(mp.mpf(x)/n-1) for n,l,h in pp if n<=x)
 G=S+C1*x
 spec=G-C0+Triv(x)
 ratio=abs(spec)/mp.sqrt(x)
 out.append({'x':x,'G4':mp.nstr(G,28),'T4':mp.nstr(Triv(x),28),'spectral':mp.nstr(spec,28),'ratio':mp.nstr(ratio,28),'slack':mp.nstr(Csharp-ratio,28)})
for x in out:print(x)
tab=['6.02094890469759665490251152161','10.2437703041665545521377574791','12.9880980123124225074531097896','16.3426071045872221949768614835','18.2919931961235348385260042776','21.4506113439834604972009483863','23.2783765204595315318195588863','25.7287564250887275672650886743','28.3596343430253277856516079418','29.6563840145931527218099069682']
zeros=[]
for j,s in enumerate(tab):
 t=mp.mpf(s)
 z=mp.findroot(L,(mp.mpc('0.50',t-mp.mpf('.00001')),mp.mpc('0.50',t+mp.mpf('.00001'))),solver='secant',tol=mp.mpf('1e-44'),maxsteps=35)
 zeros.append(z)
 print('root',j+1,mp.nstr(z,34),'residual',mp.nstr(abs(L(z)),5))
part=2*sum(1/(mp.im(z)**2+mp.mpf(1)/4) for z in zeros)
print('first10 C',mp.nstr(part,35),'remaining POS under GRH',mp.nstr(Csharp-part,20))
for x in [2,10,100,1000,10000]:
 approx=2*mp.sqrt(x)*sum(mp.cos(mp.im(z)*mp.log(x))/(mp.im(z)**2+mp.mpf(1)/4) for z in zeros)
 actual=mp.mpf(next(a['spectral'] for a in out if a['x']==x))
 print('10 zeros x',x,'approx',mp.nstr(approx,20),'actual',mp.nstr(actual,20),'diff',mp.nstr(approx-actual,12))
res={'C1':str(C1),'C0':str(C0),'Csharp':str(Csharp),'Cvia':str(Cvia),'values':out,'zeros':[str(z) for z in zeros],'first10C':str(part)}
with open('/mnt/data/riemann_20261123_1253/beta_sharp_bound.json','w') as f:json.dump(res,f,indent=2)
