from fractions import Fraction
import mpmath as mp,json
mp.mp.dps=90
beta=mp.mpf('0.75');theta=mp.mpf('0.6')
L=mp.log(2)
rows=[]
for k in range(1,31):
 u=mp.pi-L/2+2*mp.pi*k
 phases=[u+j*L/128 for j in range(129)]
 cosmax=max(mp.cos(t) for t in phases)
 assert cosmax<0
 # exact theoretical bound: cos(phase)<=-cos(log2/2)<0
 rows.append({'k':k,'logY':mp.nstr(u,20),'max_cos':mp.nstr(cosmax,12),'sign_pass':True})
print('all 30 dyadic windows negative; first and last',rows[0],rows[-1])
print('exact positive pole model: Mellin (s-beta)/((s-beta)^2+1) poles beta±i, beta>theta')
with open('/mnt/data/riemann_20261123_1659/landau_dyadic_counterexample.json','w') as f:json.dump(rows,f,indent=2)
