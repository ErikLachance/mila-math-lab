import numpy as np,json,time
from scipy.special import digamma
from scipy.integrate import quad
from scipy.optimize import minimize_scalar
from math import log,pi,sqrt,sinh
s=time.monotonic()
L=.81;delta=2*L-log(5); c5=log(5)/sqrt(5)
H=lambda t:digamma(.25+.5j*t).real-log(pi)
record=[]
for w in [1/24,1/20,1/16,1/14,1/13,1/12,1/11,1/10,1/9,1/8,1/7]:
 if w<delta or 2*L-2*w<=log(4):continue
 pole=4*w*sinh(L/2)**2
 def val(p):
  M=(sqrt(delta*p)+sqrt((w-delta)*(1-p)))**2/pi
  if M==0:return np.inf
  T=1/(2*M)
  v=2*M*quad(H,0,T,epsabs=1e-9,limit=200)[0]-c5*p-pole
  return v
 sol=minimize_scalar(val,method='bounded',bounds=(0,1),options={'xatol':1e-12})
 res={'w':w,'p':sol.x,'lower':sol.fun,'p0':val(0.),'p1':val(1.),'p_uniform':val(delta/w)}
 record.append(res)
 print(res,flush=True)
with open('/mnt/data/riemann_research_20261123/collar_p_optimization.json','w') as f:json.dump({'results':record,'elapsed_s':time.monotonic()-s},f,indent=2)
