from fractions import Fraction as F
import json
rows=[]
for p in [3,5,7,11,13,17]:
    for k in range(2,9):
        N=p**k
        r=k//2
        L=k+1
        Delta=L+L*L+1
        t=sum(F(N,p**e)-1 for e in range(1,k+1,2) if N>p**e)
        B=t+F(N+1,p*p-1)-Delta
        vf=(N-1)//(p-1)-1
        slack=F(vf)-B
        if k%2==0:
            target=F(r+L+L*L)-F(2,p*p-1)
        else:
            target=F(r+Delta)-F(1,p-1)
        assert slack==target,(p,k,slack,target)
        rows.append({'p':p,'k':k,'N':N,'v':vf,'B':str(B),'slack':str(slack),'asymptotic_slope':'N/(p-1) on both sides'})
with open('/mnt/data/riemann_20261123_1659/theta_minor_asymptotic_slope.json','w') as f:json.dump({'pass':True,'cases':len(rows),'rows':rows},f,indent=2)
print('PASS',len(rows),'symbolic slope regression cases');print(rows[:2])
