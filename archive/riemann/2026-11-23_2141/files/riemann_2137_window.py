import math, json, time
from scipy.special import gammainc,gammaincc
start=time.monotonic(); checks=0; cases=[]
# For X gamma(n,rate), P(X <= n*l/rate) <= exp(-n*(l-1-log(l))) for l<1, similarly upper r>1.
for lam in [1.01,1.05,1.1,1.25,1.5,2,4]:
 a=1.; theta=.1; mid=(1+lam)/2; l=(1+1/mid)/2; r=(1+lam/mid)/2
 c=min(l-1-math.log(l),r-1-math.log(r));sigma=a+2*(a-theta)/c+1
 assert math.log((sigma-theta)/(sigma-a))<c
 for U in [1,10,100,1000,10000]:
  n=round((sigma-a)*mid*U)+1;rate=sigma-a
  low=rate*U/n;high=rate*lam*U/n
  if low<1 and high>1:
   tail=gammainc(n,rate*U)+gammaincc(n,rate*lam*U)
   bound=math.exp(-n*(low-1-math.log(low)))+math.exp(-n*(high-1-math.log(high)))
   assert tail<=bound+1e-12;checks+=1
 cases.append({'lambda':lam,'c':c,'sigma':sigma})
# Toy meromorphic transforms, simple poles with positive real residue vs conjugate pair. No claim about actual zero locations.
for sigma in [10.,30.,100.]:
 for j in [50,100,200]:
  z=.2;g=.3;d=sigma-z
  # normalized Taylor coefficient for F=1/(s-.2)+1/(s-(.1+2i))+1/(s-(.1-2i))
  v=1+2*((d/complex(sigma-.1,2))**(j+1)).real
  err=2*(d/abs(complex(sigma-.1,2)))**(j+1)
  assert v>0 or err>=1
  assert abs(v-1)<=err+1e-12;checks+=1
  # shift to imaginary coordinate of nearest non-real pole: one pole dominates the analytic remainder
  z0=complex(sigma,2);d=sigma-.3
  r=d/complex(sigma-.3,4);v=1+r**(j+1);assert abs(v-1)<=abs(r)**(j+1)+1e-12;checks+=1
out={'checks':checks,'parameters':cases,'elapsed_s':time.monotonic()-start};print(json.dumps(out,indent=2));open('/mnt/data/riemann_2137_window.json','w').write(json.dumps(out,indent=2))

