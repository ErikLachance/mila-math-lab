#!/usr/bin/env python3
"""Exact toy obstruction: sparse sample bounds cannot replace full logarithmic windows.
G_beta,omega(x)=x^beta*cos(omega log x) has Mellin poles at beta +/- i omega.
Does not assert existence of zeta zero outside critical line."""
import json, mpmath as mp
mp.mp.dps=60
beta=mp.mpf('0.75'); theta=mp.mpf('0.6'); omega=mp.mpf('3')
s=mp.mpc('1.35','0.2')
formula=(s-beta)/((s-beta)**2+omega**2)
numeric=mp.quad(lambda t:mp.exp(-(s-beta)*t)*mp.cos(omega*t), [0, 20, 40, 80, mp.inf])
assert abs(formula-numeric)<mp.mpf('1e-40')
zeros=[];peaks=[]
for k in range(1,16):
    u=(mp.pi/2+2*mp.pi*k)/omega
    peak_log=2*mp.pi*k/omega
    # y_k=cos zero while peak F=exp(beta*peak_log) > exp(theta*peak_log)
    zeros.append(float(mp.cos(omega*u)))
    peaks.append(float(mp.exp((beta-theta)*peak_log)))
assert max(map(abs,zeros))<1e-50
assert all(p>1 for p in peaks)
# A log interval [logY,1.5logY] of length .5logY contains a cos=1 peak when .5logY>=2pi/omega.
Y0log=4*mp.pi/omega
report={'model':'G(x)=x^beta*cos(omega*log(x)), x>1','beta':str(beta),'theta':str(theta),'omega':str(omega),
 'Mellin_formula':'(s-beta)/((s-beta)^2+omega^2), Re(s)>beta',
 'Mellin_poles':'beta +/- i omega',
 'numerical_Mellin_regression_abs_error':mp.nstr(abs(numeric-formula),10),
 'sample_zeros_count':len(zeros),'max_sample_cos_abs':max(map(abs,zeros)),
 'peak_growth_F_over_x_theta_first':peaks[0], 'peak_growth_F_over_x_theta_last':peaks[-1],
 'logY_sufficient_for_all_[Y,Y^1.5]_to_contain_period_peak':mp.nstr(Y0log,17),
 'logical_warning':'Sparse pointwise sample is insufficient for Landau-style window criterion; all-x uniform long window is essential. Toy poles are not zeta zeros.'}
print(json.dumps(report,indent=2))
with open('/mnt/data/riemann_run_20261123_1524/sparse_window_adversary.json','w') as f:json.dump(report,f,indent=2)
