from mpmath import mp
from sympy import primerange
import json
mp.dps=50
cases=[(3,[0,1,-1],1),(4,[0,1,0,-1],1),(5,[0,1,-1,-1,1],0),(8,[0,1,0,-1,0,-1,0,1],0)]
seq=[]
for p in primerange(2,1001):
 n=int(p)
 while n<=1000:seq.append((n,mp.log(int(p))));n*=int(p)
seq.sort()
out=[]
for q,char,parity in cases:
 L=lambda s:mp.dirichlet(s,char)
 c=mp.dirichlet(1,char,1)/L(1)
 Ctheory=mp.log(q/mp.pi)-mp.euler+2*c-(2*mp.log(2) if parity==0 else 0)
 if parity:
  K0=mp.dirichlet(0,char,1)/L(0)
  T=lambda x:mp.log(2) if x==1 else mp.atanh(1/mp.mpf(x))+(mp.mpf(x)/2)*mp.log(1-1/mp.mpf(x)**2)
 else:
  H=lambda s:mp.power(q,-s)*sum(int(char[a])*mp.zeta(s,mp.mpf(a)/q) for a in range(1,q) if char[a])
  first=mp.diff(H,0)
  d=mp.diff(H,0,2)/(2*first)
  K0=1+d
  T=lambda x:1-mp.log(2) if x==1 else mp.nsum(lambda k:mp.power(x,-2*k)/(2*k*(2*k+1)),[1,mp.inf])
 calc=[]
 for x in [1,2,3,10,100,1000]:
  G=sum(l*char[n%q]*(mp.mpf(x)/n-1) for n,l in seq if n<=x)+x*c
  spect=G-(K0 if parity else mp.log(x)+K0)+T(x)
  ratio=abs(spect)/mp.sqrt(x)
  calc.append({'x':x,'signed':mp.nstr(spect,20),'norm':mp.nstr(ratio,20),'pass_numeric':bool(ratio<Ctheory+mp.mpf('1e-35'))})
 print('q',q,'parity',parity,'C',mp.nstr(Ctheory,25),'x1_difference',mp.nstr(Ctheory-mp.mpf(calc[0]['norm']),6),'all_pass',all(a['pass_numeric'] for a in calc))
 out.append({'q':q,'parity':parity,'C':str(Ctheory),'K0':str(K0),'tests':calc})
with open('/mnt/data/riemann_20261123_1253/quadratic_char_parity_general.json','w') as f:json.dump(out,f,indent=2)
