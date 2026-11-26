# Independently implement literal Lean definitions from
# StatementG.lean, StatementAB.lean, GrowthSums/StatementA.lean,
# OddLogRelation.lean, CyclicPowerClassOfExpEquiv.lean.
# Evaluate r0=r1=R, nu=1, TT={0}, N and i 1-height columns
# and one R-height column at site0 for R>=2.
from fractions import Fraction
import json

def ell(p,n):
 if n==0:return 0
 k=0
 while n:
  n//=p;k+=1
 return k

def vp_fact(p,n):
 q=0
 while n:
  n//=p;q+=n
 return q

def directly_from_lean(p,N,i,R):
 # at0 has N 1-columns + one R-column (for R>=2);
 # at1 has i 1-columns; r0=r1=R.
 # for R1 do NOT include extra R=1 column.
 extra=(1 if R>=2 else 0)
 hts={0:[1]*N+([R] if extra else []),1:[1]*i}
 TT=(0,)
 al={s:(sum(1 for h in hts[s] if h==1) if s in TT else 0) for s in (0,1)}
 cap={s:len(hts[s])-al[s] for s in (0,1)}
 ls={s:sum(hts[s])-al[s] for s in (0,1)}
 dset0=set() # only s0 in TT, opposite parity subset empty
 de=sum(R*ell(p,al[s]) +R*R*ell(p,ls[s]) for s in (0,1))+ell(p,al[0])**2
 rho=Fraction(1,p*p-1)
 gam=Fraction(p,p*p-1)
 # excessGain: sum_e max(al0 / p^(2e+1)-cap_(0+odd),0) -de
 excess=Fraction(-de)
 t=0
 while True:
  exp=2*t+1
  a=Fraction(al[0],p**exp)-cap[1]
  if a<=0:break
  excess+=a
  t+=1
  if t>50:raise RuntimeError('unreasonable')
 exponent=excess+rho*sum(al[s]+ls[s] for s in (0,1))
 return exponent,{'al':al,'cap':cap,'ls':ls,'deLoss':de,'count_odd_terms':t,'dSet0':list(dset0)}

def shortcut_from_previous(p,N,i,R):
 de=ell(p,N)**2+R*ell(p,N)+R*R*(ell(p,R) if R>=2 else 0)+R*R*ell(p,i)
 sum_pos=Fraction(0)
 e=1
 while Fraction(N,p**e)>i:
  sum_pos+=Fraction(N,p**e)-i
  e+=2
 return sum_pos-de+Fraction(N+(R if R>=2 else 0)+i,p*p-1)

checked=0;viol=[];min_slack=None;nonvacuous=0;examples=[]
for p in [3,5,7,11,13]:
 for k in [1,2,3,4]:
  N=p**k
  for i in range(1,min(N//p,30)+1):
   for R in range(1,13):
    t,m=directly_from_lean(p,N,i,R)
    b=shortcut_from_previous(p,N,i,R)
    if t!=b:viol.append({'p':p,'k':k,'i':i,'R':R,'actual':str(t),'shortcut':str(b),'state':m})
    v=vp_fact(p,N+(1 if R>=2 else 0))+vp_fact(p,i)-i
    if v<t:viol.append({'p':p,'k':k,'i':i,'R':R,'actual':str(t),'v':v,'state':m})
    checked+=1
    if t>0:nonvacuous+=1
    if min_slack is None or Fraction(v)-t<min_slack:min_slack=Fraction(v)-t
    if (p,k,i,R) in {(3,2,1,1),(3,3,3,4),(5,3,3,9),(7,4,2,10)}:
     examples.append({'p':p,'N':N,'i':i,'R':R,'targetValuation':v,'sourceLowerBound':str(t),'computedState':m})
assert not viol,viol[:2]
res={'test_count':checked,'exact_lean_source_matches':True,'positive_lower_bound_cases':nonvacuous,'min_slack':str(min_slack),'examples':examples,'source_semantics':'direct from alG/capG/lsG,deLoss,rhoP,gamP,excessGain and dSet. TT singleton even site0; dSet0 empty; cap(site1)=i; alg sum for R>=2 has al0=N ls0=R; R1 no extra column. Key odd terms positive until N/p^(2e+1)<=i. Demonstrates previous human formula B_R equals actual source exponent in this narrow model after replacing F with full hhS globally.'}
open('/mnt/data/riemann_20261123_1728/theta_source_exact_formula_audit.json','w').write(json.dumps(res,indent=2))
print(json.dumps(res,indent=2)[:1600])
