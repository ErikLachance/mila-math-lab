import math,json
from scipy.special import gammainc,gammaincc
import mpmath as mp
mp.mp.dps=50
eta=max(.8*math.exp(.2),1.2*math.exp(-.2))
C=math.log((1+eta)/(2*eta))
assert eta<1 and C>0.008
rows=[]
for U in [1,5,10,20,40,80]:
 sigma=252.; theta=.8
 j=round(1.25*(sigma-2)*U)
 rate=sigma-2
 lo=gammainc(j+1,rate*U)
 hi=gammaincc(j+1,rate*(1.5*U))
 ratio=(sigma-theta)/(sigma-2)
 r=eta*ratio
 # shape j+1 gamma density
 rows.append({'U':U,'j':j,'tail_prob_gamma':lo+hi,'eta':eta,'eta_times_ratio':r,'r_to_j':r**j, 'log10_r_to_j':j*math.log10(r)})
print(json.dumps({'eta':eta,'log_thresh':C,'pass_sigma252_theta0':eta*(252./250.)<1,'test':rows},indent=2))
with open('/mnt/data/riemann_run_20261123_1457/landau_interval_audit.json','w') as f:json.dump({'eta':eta,'log_thresh':C,'test':rows},f,indent=2)
