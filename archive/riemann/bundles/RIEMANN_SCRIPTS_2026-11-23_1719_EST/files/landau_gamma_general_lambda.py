from fractions import Fraction as F
import math,json

def ceil(x):return -(-x.numerator//x.denominator)
def floor(x):return x.numerator//x.denominator
rows=[]
for lam in [F(1001,1000),F(101,100),F(11,10),F(3,2),F(2),F(10)]:
    lam0=min(lam,F(3,2))
    delta=(lam0-1)/(lam0+1)
    q=ceil(F(1000)/(delta*delta))
    sigma=q+2
    for U in [F(1),F(3,2),F(2),F(10),F(100)]:
        mu=(1+lam0)*U/2
        m=floor(q*mu);k=m-1
        left=F(q)*U/m
        right=F(q)*lam0*U/m
        assert 0<left<=1-delta/2
        assert right>=1+delta
        assert k>=U
        assert m>=q*mu/2
        assert F(q)*delta*delta>=1000
        assert (q>=3 and mu>=1)
        rows.append({'lambda':str(lam),'restricted_lambda':str(lam0),'delta':str(delta),'q':q,'sigma':sigma,'U':str(U),'m':m,'k':k,'left_r':float(left),'right_r':float(right),'conservative_log_tail_ratio_bound':float(math.log(2/q)-60.5*float(mu))})
with open('/mnt/data/riemann_20261123_1659/landau_gamma_general_lambda.json','w') as f:json.dump({'pass':True,'cases':len(rows),'rows':rows},f,indent=2)
print('PASS',len(rows),'exact rational inequality tests, largest q=',max(r['q'] for r in rows),'largest m=',max(r['m'] for r in rows));print(*rows[:4],sep='\n')
