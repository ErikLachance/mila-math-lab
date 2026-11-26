from fractions import Fraction
import json,math

def vp_fact(n,p):
 s=0
 while n:
  n//=p;s+=n
 return s

def ell(n,p):
 if n==0:return 0
 ans=0
 while n:
  ans+=1;n//=p
 return ans

def bound(p,N,i):
 ellN=ell(N,p);elli=ell(i,p)
 delta=ellN+elli+ellN*ellN
 a=Fraction(N+i,p*p-1)-delta
 d=p
 while d<=N:
  a+=max(Fraction(N,d)-i,0)
  d*=p*p
 return a

summary=[];records=[]
for p,k in [(3,5),(3,6),(3,7),(5,4),(5,5),(7,4)]:
 N=p**k;pos=[];pass_count=0;maxslack=-1;bad=[]
 for i in range(1,N//p+1):
  # F=(h/p)^i Z_0^(N-pi), target coefficient at Z_0^N Z_1^i equals p^(-i)
  v=vp_fact(N,p)+vp_fact(i,p)-i
  B=bound(p,N,i)
  slack=Fraction(v)-B
  if slack<0:bad.append(i)
  else:pass_count+=1
  if B>0:pos.append(i)
  if i in (1,2,3,p,p*p,N//p,N//(p*p)):
   records.append({'p':p,'N':N,'i':i,'vp':v,'bound':str(B),'slack':str(slack),'positive_bound':B>0})
 summary.append({'p':p,'N':N,'i_range':N//p,'nonnegative_bounds_count':len(pos),'largest_i_with_positive_bound':max(pos) if pos else None,'smallest_i_with_positive_bound':min(pos) if pos else None,'violations':bad[:10],'passed':pass_count})
assert all(not x['violations'] for x in summary)
res={'summary':summary,'sample_cases':records,'coefficient_proof':'In h^i, each h factor contains at least one Z1, so Z1^i forces all factors to take (Z0^p Z1) with coefficient 1; higher q terms cannot contribute. Thus target coefficient p^-i, v_p(J)=v_p(N!)+v_p(i!)-i.','class_membership':'Choose U_i=Z0^(N-p*i) and all other U_j=0. F=p^-i h^i U_i satisfies the integral-U series class exactly.'}
open('/mnt/data/riemann_20261123_1728/theta_high_i_family.json','w').write(json.dumps(res,indent=2))
print(json.dumps(summary,indent=2));print('SAMPLES',json.dumps(records[:25],indent=2))
