from fractions import Fraction
import json

def vp_fact(n,p):
 v=0
 while n:
  n//=p;v+=n
 return v

def ell(n,p):
 k=0
 while n:
  n//=p;k+=1
 return k

def bound(p,N,i,r):
 E=ell(N,p)
 delta=E**2+r*E+r*r*(ell(r,p)+ell(i,p))
 s=Fraction(N+r+i,p*p-1)-delta
 d=p
 while d<N:
  s+=max(Fraction(N,d)-i,0)
  d*=p*p
 return s,delta
count=0;pos=0;minimum=None;sample=[]
for p in [3,5,7,11]:
 for k in [2,3,4,5]:
  N=p**k
  I=range(1,min(N//p,70)+1)
  for i in I:
   v=vp_fact(N+1,p)+vp_fact(i,p)-i
   b1,D1=bound(p,N,i,1)
   assert v>=b1
   for r in range(2,15):
    b,delta=bound(p,N,i,r)
    loss=delta-D1-Fraction(r-1,p*p-1) # WAIT dQ_r -dQ_1 = r not r-1, since base r=1 high column site0 => dQ=N+1+i
    # general comparison with 1x1 base (no tall column): B_r-B_1 = -(delta-D1)+r/(p^2-1)
    assert b<b1
    assert v>b
    count+=1
    if b>0:pos+=1
    d=Fraction(v)-b
    if minimum is None or d<minimum[0]:minimum=(d,p,k,N,i,r)
    if (p,k,i,r) in {(3,5,1,3),(5,4,1,4),(7,4,3,9),(11,4,2,12)}:
     sample.append({'p':p,'N':N,'i':i,'rank':r,'vp':v,'theorem_bound':str(b),'slack':str(d),'delta':delta})
res={'cases_checked':count,'positive_lower_bound_cases':pos,'min_slack_case':{'slack':str(minimum[0]),'p':minimum[1],'k':minimum[2],'N':minimum[3],'i':minimum[4],'rank':minimum[5]},'examples':sample,'general_identity':'For rank R>=2 choose r0=r1=R, one R-by-R determinant at s0, N height1 columns at s0, i height1 at s1. T={0}; F=p^-i h^i Z_(0,1,1)^(N+1-pi) product_{j=2..R} Z_(0,j,j). Selected diagonal X-monomial coefficient J_F=(N+1)! i! /p^i. Delta_R=ell(N)^2+R ell(N)+R^2(ell(R)+ell(i)), d_Q=N+R+i, and positive-sum part same as 1x1. Comparing previous rank1 no-tall-column result: B_R=B_1-(Delta_R-Delta_1)+R/(p^2-1) < B_1, since Delta_R-Delta_1=(R-1)ell(N)+R^2 ell(R)+(R^2-1)ell(i)>R/(p^2-1). Thus v_p(J_F)>B_R universally for all odd primes p, k>=1, i<=p^(k-1), R>=2. This is a single selected diagonal coefficient for a determinant of arbitrary rank; it does NOT certify arbitrary matrix coefficients or source-global theta membership.'}
open('/mnt/data/riemann_20261123_1728/theta_rank_r_minor_family.json','w').write(json.dumps(res,indent=2))
print(json.dumps(res,indent=2))
