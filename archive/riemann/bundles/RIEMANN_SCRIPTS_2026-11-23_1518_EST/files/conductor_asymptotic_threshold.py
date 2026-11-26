import math,json
rows=[]
for eps in [0.005,0.01,0.018]:
 def f(t): return 2*eps*t/15 - 2*math.log(t)
 lo=1000;hi=1000000
 assert f(lo)<0 and f(hi)>0
 for _ in range(100):
  mid=(lo+hi)/2
  if f(mid)>0: hi=mid
  else:lo=mid
 tcrit=(lo+hi)/2
 def calc(t):return math.exp(min(700,f(t)))
 rows.append({'epsilon':eps,'critical_log_x_large_root':tcrit,'critical_log10_x':tcrit/math.log(10), 'ratio_at_t10000':calc(10000),'ratio_at_t40000':calc(40000),'ratio_at_t60000':calc(60000),'test_f_below':f(tcrit-0.001),'test_f_above':f(tcrit+0.001)})
res={'equivalence':'log(Xprime/d) >= exp(eps*t/5)*(exp(2eps*t/15)-t*t), t=log x; eventual Xprime/d greater than 4 if ratio >1 beyond asymptotic threshold','thresholds':rows}
print(json.dumps(res,indent=2))
with open('/mnt/data/riemann_run_20261123_1457/conductor_asymptotic_threshold.json','w') as f:json.dump(res,f,indent=2)
