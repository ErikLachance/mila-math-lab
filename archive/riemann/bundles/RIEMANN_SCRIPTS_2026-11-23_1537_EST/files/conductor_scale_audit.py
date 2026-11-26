#!/usr/bin/env python3
"""Independent log-scale audit of conditional asymptotic inequalities
in jimjamzola/RH-Alpoge-Reconstruction, sec16_local.tex, primesizes.
Not a reproduction of the formal Lean proof."""
import json, mpmath as mp
mp.mp.dps = 80

def highroot(eq, start):
    lo=mp.mpf(start)/2
    hi=mp.mpf(start)*2
    # choose largest positive crossing, ensure negative at lo and positive at hi
    while eq(lo)>0: lo /= 2
    while eq(hi)<0: hi *= 2
    for i in range(350):
        m=(lo+hi)/2
        if eq(m)>=0: hi=m
        else: lo=m
    return (lo+hi)/2

rows=[]
for estr in ['0.002','0.005','0.01','0.018']:
    e=mp.mpf(estr)
    # log x=t/e, so x^e=e^t.
    f1=lambda t: mp.exp(t)-9-40*t/e
    f2=lambda t: mp.mpf('0.8')*t-2*mp.log(t/e)
    f4=lambda t: mp.exp(t)-mp.exp(t/3)-(mp.mpf(808)+e)*t/e-mp.log(4)
    fd=lambda t: mp.mpf(2)*t/15-2*mp.log(t/e)
    rt1=highroot(f1,20)
    rt2=highroot(f2,30)
    rt4=highroot(f4,22)
    rtd=highroot(fd,200)
    # exact-to-precision identity vs Lambert W lower branch for a t = 2 log(t/e)
    for a,t0 in [(mp.mpf('.8'),rt2),(mp.mpf(2)/15,rtd)]:
        w=-2/a*mp.lambertw(-a*e/2,-1)
        assert abs(w-t0)<mp.mpf('1e-68')
    row={'epsilon':estr,'threshold_t_exp_bound_i':mp.nstr(rt1,18),
         'threshold_t_d_le_xeps_ii':mp.nstr(rt2,18),
         'threshold_t_size_bound_iv':mp.nstr(rt4,18),
         'threshold_t_d_lt_Xprime':mp.nstr(rtd,18),
         'sufficient_log10_x_for_iv':mp.nstr(rt4/(e*mp.log(10)),15),
         'sufficient_log10_x_for_d_lt_Xprime':mp.nstr(rtd/(e*mp.log(10)),15),
         'all_thresholds_t_ordered': bool(rt1<rtd and rt2<rtd and rt4<rtd)}
    rows.append(row)
print(json.dumps({'reference':'jimjamzola/RH-Alpoge-Reconstruction manuscript/sec16_local.tex lines 184-211, SHA 96e49a132f32d4d660ea12cc8efd9c96216229fc','variables':'t=epsilon*log(x), epsilon fixed, x>1','identity':'4*x^(808+epsilon)*exp(x^(epsilon/3))<=exp(x^epsilon) iff exp(t)-exp(t/3)-(808+epsilon)*t/epsilon-log(4)>=0','root_uniqueness':'for f4(t), f4(0)=-log4<0; f4 second derivative exp(t)-exp(t/3)/9>0 for all t>=0, so exactly one positive zero','samples':rows},indent=2))
with open('/mnt/data/riemann_run_20261123_1524/conductor_scale_audit.json','w') as f:json.dump({'samples':rows,'interpretation':'finite numerical threshold regressions with rigorous algebraic implication, not new RH proof'},f,indent=2)
