from mpmath import mp
import json
mp.dps=90
beta=mp.mpf('0.75'); theta=mp.mpf('0.6')
C=mp.pi/3
c=mp.exp(C)
records=[]
for n in range(0,9):
    U=mp.pi+2*mp.pi*n
    values=[mp.cos(U+C*mp.mpf(k)/100) for k in range(101)]
    # exact sign follows cos(pi+t)=-cos(t), cos t >=1/2 on 0<=t<=pi/3
    upper=max(values)
    records.append({'n':n,'U':mp.nstr(U,20),'log_width':mp.nstr(C,20),'Y':mp.nstr(mp.exp(U),18),'c':mp.nstr(c,18),'max_cos_on_samples':mp.nstr(upper,18),'all_values_negative':all(v<0 for v in values)})
# Direct integral for Re(s)>beta; comparison to meromorphic continuation
s=mp.mpf('1.5')+mp.mpf('.2')*1j
integral=mp.quad(lambda u:mp.e**((beta-s)*u)*mp.cos(u),[0,mp.inf])
closed=(s-beta)/((s-beta)**2+1)
# poles at beta+/-i. Residues 1/2 at each pole since F=(1/2)[1/(s-beta-i)+1/(s-beta+i)]
report={'definition':'g(u)=exp(beta*u)*cos(u), G(x)=g(log x)=x**beta*cos(log x), beta=3/4>theta=3/5','claim':'For infinitely many Y_n=exp(pi+2*pi*n), every x in [Y_n,exp(pi/3)*Y_n] has G(x)<=0<=x^theta, yet Mellin F(s) has poles at s=beta+/-i. Thus replacing [Y,Y**alpha] fixed alpha>1 by [Y,c*Y] fixed c>1 invalidates general one-sided criterion. This is a toy Mellin function, not zeta G and not RH counterexample.','alpha_not_fixed':'log(c*Y)/log Y=1+log(c)/log(Y) -> 1','analytic_cos_sign':'cos(pi+t)=-cos(t)<=-1/2 for 0<=t<=pi/3, proves sign for every real x, not only samples','beta':str(beta),'theta':str(theta),'multiplicative_width_c':mp.nstr(c,35),'poles':['3/4+i','3/4-i'],'residue_at_each':'1/2','integral_numeric':str(integral),'closed_numeric':str(closed),'absolute_error':mp.nstr(abs(integral-closed),12),'sample_windows':records}
with open('/mnt/data/riemann_20261123_sparse_countermodel.json','w') as f:json.dump(report,f,indent=2)
assert all(r['all_values_negative'] for r in records)
assert abs(integral-closed)<mp.mpf('1e-75')
print('Toy countermodel PASS, sample windows',len(records),'c=',mp.nstr(c,15),'numeric transform error',mp.nstr(abs(integral-closed),8),'poles beta+/-i')
