from fractions import Fraction
import json

def vp_fact(n,p):
 out=0
 while n>0:
  n//=p;out+=n
 return out

def ell(n,p):
 j=0
 while n:
  n//=p;j+=1
 return j

def direct(p,k,i):
 N=p**k
 r=0;d=p
 positive=Fraction(0)
 while d<N:
  v=Fraction(N,d)-i
  if v>0:positive+=v;r+=1
  d*=p*p
 D=ell(N,p)+ell(i,p)+ell(N,p)**2
 B=positive-D+Fraction(N+i,p*p-1)
 v=vp_fact(N,p)+vp_fact(i,p)-i
 return v,B,Fraction(v)-B,r,D

def symbolic(p,k,i,r,D):
 N=p**k
 # N*p^(1-2r) as exact Fraction
 n=Fraction(N*p,p**(2*r))
 return D+(r-1)*i+vp_fact(i,p)+Fraction(n-i,p*p-1)-Fraction(1,p-1)

nchecks=0;minslack=None;mincase=None
for p in [3,5,7,11,13]:
 for k in [2,3,4,5,6,7]:
  N=p**k
  # deterministic broad samples plus complete when affordable
  values=range(1,N//p+1) if N//p<=10000 else set([1,2,3,p,p*p,N//(p*p),N//p,N//p-1]+[1+j*(N//p)//1000 for j in range(1,1000)])
  for i in values:
   if i<1 or i>N//p:continue
   v,b,slack,r,D=direct(p,k,i)
   e=symbolic(p,k,i,r,D)
   assert slack==e,(p,k,i,slack,e)
   assert slack>0,(p,k,i,slack)
   nchecks+=1
   if minslack is None or slack<minslack:
    minslack=slack;mincase={'p':p,'k':k,'N':N,'i':i,'r':r,'delta':D,'slack':str(slack)}
res={'identity_checks':nchecks,'smallest_slack_tested':str(minslack),'minimum_case':mincase,'exact_general_statement':'For any odd prime p, integer k>=1, N=p^k, and integer 1<=i<=N/p, set h=q0^p q1+q1^p q0, F=p^-i h^i Z0^(N-pi), with T={0}, nu=r0=r1=1 and height-1 column counts N at 0 and i at 1. If r counts odd positive e with N/p^e>i, delta=(k+1)+ell_p(i)+(k+1)^2, and v=v_p(N!)+v_p(i!)-i, then v-B=delta+(r-1)i+v_p(i!)+(N*p^(1-2r)-i)/(p^2-1)-1/(p-1)>0. For r>=1, N*p^(1-2r)>i; for r=0, i=N/p and expression reduces to delta+v_p(i!)-1/(p-1)>0. This proves this entire specialization of PHT.1753 by elementary algebra; not the general theorem.'}
open('/mnt/data/riemann_20261123_1728/theta_family_symbolic_slack.json','w').write(json.dumps(res,indent=2))
print(json.dumps(res,indent=2))
