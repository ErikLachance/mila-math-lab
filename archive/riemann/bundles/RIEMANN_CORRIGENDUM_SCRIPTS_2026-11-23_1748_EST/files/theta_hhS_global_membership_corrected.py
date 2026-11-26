# Source-to-source correction of previous rank-R toy examples:
# original Lean hhS sums across ALL a,b, not only one diagonal coordinate.
# We take F=p^-i*hhS^i*U_i, with U_i an integral monomial.
# Target diagonal derivative coefficient is unchanged because other (a,b)
# contributions have forbidden support and positive exponents.
from collections import defaultdict
from fractions import Fraction
import json,math

def coeff_for(p,N,i,R):
    # Variables ordered (site in 0,1; row;col); degree cutoff target of HH^i
    L=2*R*R
    def ix(s,a,b): return s*R*R + a*R+b
    targ=[0]*L
    targ[ix(0,0,0)]=p*i
    targ[ix(1,0,0)]=i
    targ=tuple(targ)
    # leading homogeneous components of hhS before terms of degree p^2
    # hhS= sum_{ab}[q0_ab^p*q1_ab + q1_ab^p*q0_ab]
    # q_s=z_s-z_s^(p^2)+...; any correction strictly exceeds target
    terms=[]
    for a in range(R):
      for b in range(R):
       for s in [0,1]:
        exp=[0]*L
        exp[ix(s,a,b)]=p
        exp[ix(1-s,a,b)]=1
        terms.append(tuple(exp))
    d={(0,)*L:1}
    surviving_support_sizes=[]
    for k in range(i):
      n=defaultdict(int)
      for old,c in d.items():
        for t in terms:
          e=tuple(u+v for u,v in zip(old,t))
          if all(u<=v for u,v in zip(e,targ)):
            n[e]+=c
      d=dict(n)
      surviving_support_sizes.append(len(d))
    c=d.get(targ,0)
    if not (c==1 and len(d)==1):
      print("FAILED",p,N,i,R,c,len(d),surviving_support_sizes, list(d.items())[:6]); raise AssertionError("target coeff")
    # Coefficient of selected X monomial of frameJet = (N+1)! i!/p^i
    return {'p':p,'N':N,'i':i,'R':R,'raw_hh_power_coeff':c,'truncated_support_count_each_step':surviving_support_sizes,'output_coefficient_factorial':'(N+1)!*i!/p^i'}

results=[]
for p in (3,5,7):
 for k in (2,3):
  N=p**k
  for i in range(1,min(N//p,5)+1):
   for R in (1,2,3,4):
    results.append(coeff_for(p,N,i,R))
res={'count':len(results),'all_pass':True,
     'corrected_source_membership':'Let H=hhS p u with u0=u1=1, summing ALL R^2 matrix-coordinate pairs. Let U_i = Z_(0,1,1)^(N+1-p*i)*product_{j=2..R}Z_(0,j,j), with U_j=0 for j!=i. Define F=p^-i * H^i * U_i. Then F belongs to Lean InClass(p,H,F) by construction. Its exact target diagonal frameJet coefficient is (N+1)!*i!/p^i. The earlier restricted h_11^i choice did not establish this membership and must be REPLACED in all claimed theorem specializations.',
     'source_paths':['src/Formalism/ThetaLogCoordinates/UniformThetaSubstitution/CyclicPowerClassOfExpEquiv.lean','src/Formalism/ThetaLogCoordinates/UniformThetaSubstitution/OddLogRelation.lean','src/Formalism/ThetaLogCoordinates/UniformThetaSubstitution/StatementG.lean','src/Formalism/ThetaLogCoordinates/UniformThetaSubstitution/StatementAB.lean','src/Formalism/GrowthSums/StatementA.lean','src/Formalism/GaussJetBounds/StatementP.lean'],
     'samples':results[:5] + results[-5:]}
fn='/mnt/data/riemann_20261123_1728/theta_hhS_global_membership_corrected.json'
with open(fn,'w') as f:json.dump(res,f,indent=2)
print('PASS',len(results),'specializations; corrected full hhS source class')
