import json
import mpmath as mp
mp.mp.dps = 90

def I(v):
    return v-1-mp.log(v)

def experiment(alpha,beta,theta,sigma,Uvalues):
    alpha=mp.mpf(alpha); beta=mp.mpf(beta); theta=mp.mpf(theta); sigma=mp.mpf(sigma)
    h=(alpha-1)/mp.log(alpha)
    a=1/h; b=alpha/h
    kappa=min(I(a),I(b))
    lam=sigma-beta; q=sigma-theta
    logratio=mp.log(q/lam)
    records=[]
    for U0 in Uvalues:
        U=mp.mpf(U0)
        n=int(mp.nint(lam*h*U)); j=n-1
        low=mp.gammainc(n,0,lam*U)/mp.gamma(n)
        high=mp.gammainc(n,lam*alpha*U,mp.inf)/mp.gamma(n)
        tail=low+high
        aa=lam*U/n;bb=lam*alpha*U/n
        cher=mp.exp(-n*I(aa))+mp.exp(-n*I(bb))
        # normalized external bound: (q/lambda)**(j+1)*P_out
        excess=(q/lam)**n*tail
        records.append({'U':str(U0),'n':n,'j':j,'P_tail':mp.nstr(tail,20), 'Chernoff_bound':mp.nstr(cher,20), 'tail_ratio_P_over_bound':mp.nstr(tail/cher,15), 'relative_external_contribution':mp.nstr(excess,20), 'Chernoff_pass':bool(tail<=cher)})
    return {'alpha':str(alpha),'beta':str(beta),'theta':str(theta),'sigma':str(sigma),'h':mp.nstr(h,35),'a':mp.nstr(a,35),'b':mp.nstr(b,35),'I_left':mp.nstr(I(a),35),'I_right':mp.nstr(I(b),35),'kappa':mp.nstr(kappa,35),'log_ratio':mp.nstr(logratio,35),'strict_asymptotic_margin':mp.nstr(kappa-logratio,35),'criterion_pass':bool(kappa>logratio),'records':records}

result={'theorem':'Generalized sparse-window one-sided Mellin criterion, conditional on standard Chebyshev bound and meromorphic F: any fixed width alpha>1, centered h=(alpha-1)/log alpha gives positive Chernoff gap; choose sigma large for kappa>log((sigma-theta)/(sigma-beta)). This is proof-optimization, NOT RH proof.', 'runs':[]}
for params in [('1.5','2','0.6','252'),('1.5','2','0.6','100'),('1.5','1.1','0.6','40'),('1.02','2','0.6','60000'),('1.5','2','0.6','30')]:
    result['runs'].append(experiment(*params,Uvalues=[1,2,5,10,20,40,80,160]))
with open('/mnt/data/riemann_20261123_interval_gamma_audit.json','w') as f:
    json.dump(result,f,indent=2)
for r in result['runs']:
    print('alpha',r['alpha'],'B',r['beta'],'theta',r['theta'],'sigma',r['sigma'],'h',r['h'],'kappa',r['kappa'],'logratio',r['log_ratio'],'pass',r['criterion_pass'])
    print('U 1,20,80,160',[v['relative_external_contribution'] for v in [r['records'][0],r['records'][4],r['records'][6],r['records'][7]]])
assert all(z['Chernoff_pass'] for r in result['runs'] for z in r['records'])
print('PASS: all Chernoff inequalities checked numerically at 90-digit precision; assertions are NOT formal interval certificates')
