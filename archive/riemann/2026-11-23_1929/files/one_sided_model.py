import mpmath as mp, time, json
mp.mp.dps=60
start=time.monotonic(); rows=[]
for a in ['.05','.2','.45']:
 beta=mp.mpf(a); gamma=mp.mpf('14.134725'); z=mp.mpc(beta,gamma)
 H=mp.fprod(mp.sinh(z/2**j)/(z/2**j) for j in range(1,81));c=H**2
 def F(t):return 2*mp.re(c*mp.exp(z*t)+c*mp.exp(-z*t))
 for n in [100,300,1000]:
  tplus=(2*mp.pi*n-mp.arg(c))/gamma;tminus=tplus+mp.pi/gamma
  eta=beta/2
  vp=F(tplus)*mp.exp(-eta*tplus);vm=F(tminus)*mp.exp(-eta*tminus)
  assert vp>0 and vm<0
  # For phase-cancellation sample, the e^(beta t) term vanishes, so value is small.
  tz=tplus+mp.pi/(2*gamma)
  residual=F(tz)*mp.exp(-beta*tz)
  # Direct high precision numerical test is limited by phase residual (~1e-58).
  assert abs(residual)<=2*abs(c)*mp.exp(-2*beta*tz)+mp.mpf('1e-53')
  rows.append({'beta':a,'n':n,'log_positive_scaled':float(mp.log(vp)),'log_abs_negative_scaled':float(mp.log(-vm)),'cancelled_abs_scaled':float(abs(residual))})
report={'tests':len(rows),'rows':rows,'elapsed_code_seconds':time.monotonic()-start,'warning':'Hypothetical finite zero quartet, not an actual zeta zero test.'};print(json.dumps(report,indent=2));open('/mnt/data/riemann_20261123_1927/one_sided_model_result.json','w').write(json.dumps(report,indent=2))

