from mpmath import mp
from sympy import primerange
import json, math
mp.dps=70
Q=200000
lamb=[0.0]*(Q+1)
for p in primerange(2,Q+1):
    n=int(p)
    while n<=Q:
        lamb[n]=math.log(int(p));n*=int(p)
c=float(mp.dirichlet(1,[0,1,0,-1],1)/mp.dirichlet(1,[0,1,0,-1]));gamma=float(mp.euler)
A=B=Ac=Bc=0.0
prev0=prev4=None;sign0=sign4=0;cross0=[];cross4=[];neg0=neg4=0
samples={10,25,100,500,1000,5000,10000,20000,50000,100000,200000}
values={}
for x in range(1,Q+1):
    v=lamb[x];h=0 if x%2==0 else (1 if x%4==1 else -1)
    A+=v/x;B+=v;Ac+=h*v/x;Bc+=h*v
    z=x*(A-math.log(x)+1+gamma)-B
    y=x*(Ac+c)-Bc
    if z<0:neg0+=1
    if y<0:neg4+=1
    sz=1 if z>0 else (-1 if z<0 else 0)
    sy=1 if y>0 else (-1 if y<0 else 0)
    if prev0 is not None and sz!=prev0 and sz and prev0:
        if len(cross0)<20:cross0.append(x)
        sign0+=1
    if prev4 is not None and sy!=prev4 and sy and prev4:
        if len(cross4)<20:cross4.append(x)
        sign4+=1
    prev0=sz;prev4=sy
    if x in samples:values[x]={'G1':z,'G4':y}
print('sign changes 1',sign0,'4',sign4,'negative counts',neg0,neg4)
print('first crossings 1',cross0,'4',cross4)
print(values)
# At s=2 full Mellin transform of centered sum, compared with direct finite-cutoff integral.
# M_G1(2)=-(zeta_prime/zeta)/(2*1) -1+1+gamma = -(zeta_prime/zeta)/2+gamma
# M_G4(2)=-(L4_prime/L4)/(2*1)+c
s=mp.mpf(2)
M1_exact=-mp.diff(mp.zeta,s)/(mp.zeta(s)*s*(s-1)) -1/(s-1)**2+(1+mp.euler)/(s-1)
M4_exact=-mp.dirichlet(s,[0,1,0,-1],1)/(mp.dirichlet(s,[0,1,0,-1])*s*(s-1)) + mp.mpf(c)/(s-1)
# precision for c use the mp value not float
M4_exact=-mp.dirichlet(s,[0,1,0,-1],1)/(mp.dirichlet(s,[0,1,0,-1])*s*(s-1)) + mp.dirichlet(1,[0,1,0,-1],1)/mp.dirichlet(1,[0,1,0,-1])/(s-1)
print('s2 theoretical full M1=',mp.nstr(M1_exact,25),'M4=',mp.nstr(M4_exact,25))
res={'sign_changes_G1':sign0,'sign_changes_G4':sign4,'negative_integer_points_G1':neg0,'negative_integer_points_G4':neg4,'cross_G1':cross0,'cross_G4':cross4,'samples':values,'M1_s2':str(M1_exact),'M4_s2':str(M4_exact)}
open('/mnt/data/riemann_20261123_1253/centered_sign_and_mellin.json','w').write(json.dumps(res,indent=2))
