import mpmath as mp, json, time
mp.mp.dps=65
start=time.monotonic()
# Analytic transform: integral_n^infty (x/n-1) x^{-s-1} dx = n^{-s}/(s(s-1)).
records=[]
for n in [2,3,4,5,11]:
 for s in [mp.mpc('2.5','0.7'),mp.mpc('1.4','0.15'),mp.mpc('3.75','-2.3')]:
  actual=mp.quad(lambda t:(mp.e**t/n-1)*mp.e**(-s*t),[mp.log(n),mp.log(n)+2,mp.log(n)+20,mp.inf])
  target=mp.power(n,-s)/(s*(s-1))
  err=abs(actual-target)
  assert err <mp.mpf('1e-55'),(n,str(s),str(err))
  records.append({'n':n,'s':str(s),'error':mp.nstr(err,7)})
# Pole subtraction at s=1 can be checked symbolically using elementary Laurent series:
# (1/h-gamma+O(h)) * 1/(h(1+h)) = 1/h^2 -(1+gamma)/h +O(1).
# for L'/L at a zero rho, residue is -ord/(rho*(rho-1)).
rho=mp.mpc(mp.mpf(3)/5,1)
res=-1/(rho*(rho-1))
assert res!=0
out={'numerical_integral_matches':len(records),'max_error':max(x['error'] for x in records),
     'example_residue':str(res),'elapsed_s':time.monotonic()-start}
with open('/mnt/data/riemann_research_20261123/mellin_pole_checks.json','w') as f:json.dump(out,f,indent=2)
print(json.dumps(out,indent=2))
