from fractions import Fraction
import json

def vf(n,p):
 z=0
 while n:
  n//=p;z+=n
 return z

def ell(n,p):
 o=0
 while n:
  n//=p;o+=1
 return o

def test(p,k,i):
 N=p**k; en=ell(N,p);ei=ell(i,p)
 # 1x1 comparison Delta_old
 delta_old=en+ei+en*en
 # r0=r1=2, one height2 column at site 0 plus N height1 columns at0, i height1 at1.
 delta_2=en*en+2*en+4+4*ei
 positives=Fraction(0)
 power=p
 while power < N:
  positives+=max(Fraction(N,power)-i,0)
  power*=p*p
 B_old=positives-delta_old+Fraction(N+i,p*p-1)
 B2=positives-delta_2+Fraction(N+2+i,p*p-1)
 v=vf(N+1,p)+vf(i,p)-i
 assert vf(N+1,p)==vf(N,p)
 assert B_old-B2==delta_2-delta_old-Fraction(2,p*p-1)
 assert v>=B2
 return {'p':p,'N':N,'i':i,'v':v,'B_2x2':str(B2),'slack':str(Fraction(v)-B2),'B_2x2_positive':B2>0,'improvement_v_over_B1':str(Fraction(v)-B_old),'bound_degradation_B1_minus_B2':str(B_old-B2)}

cases=[];counts=[]
for p,k in [(3,3),(3,4),(3,5),(5,3),(5,4),(7,3),(7,4)]:
 N=p**k
 q=[]
 for i in range(1,N//p+1):q.append(test(p,k,i))
 counts.append({'p':p,'N':N,'checked':len(q),'positive_B2':sum(x['B_2x2_positive'] for x in q),'failures':0})
 for ii in sorted({1,2,3,p,max(1,N//(p*p)),N//p}):
  if ii<=N//p:cases.append(q[ii-1])
res={'counts':counts,'cases':cases,'analytic_proof':'For p odd, h=sum_(s,a,b) q_(s,a,b)^p q_(s+1,a,b), r0=r1=2. Site0: N height1 columns with I=1 and one height2 column with I(1)=1,I(2)=2. Site1: i height1 columns with I=1. T={0}. Let F=p^-i h^i (Z_(0,1,1))^(N+1-pi)*Z_(0,2,2). The target X monomial X_(0,1,1)^(N+1) X_(0,2,2) X_(1,1,1)^i in J_F has exact coefficient (N+1)! i! /p^i; other determinant branch vanishes by Z multidegree. v=vp(N!)+vp(i!)-i. Delta2-Delta1=ell(N)+4+3ell(i), and dQ2-dQ1=2, so B2=B1-(ell(N)+4+3ell(i)-2/(p^2-1)) < B1. The previous universally proven 1x1 slack ensures v>B2 for all odd p,k,i. This checks an honest size-2 determinant but a tightly controlled F and X coefficient, NOT arbitrary high-rank minors or global theta class membership.'}
open('/mnt/data/riemann_20261123_1728/theta_2x2_minor_family.json','w').write(json.dumps(res,indent=2))
print(json.dumps(counts,indent=2))
print('SAMPLES',json.dumps(cases[:10],indent=2))
