import mpmath as mp,json,math
from fractions import Fraction
mp.mp.dps=75
q=120;sigma=122
results=[]
for u in [1,1.01,1.1,1.25,1.5,2,3,5,10,20,100]:
 U=mp.mpf(str(u));m=int(mp.floor(150*U));k=m-1
 PL=mp.gammainc(m,0,q*U,regularized=True)
 PR=mp.gammainc(m,q*mp.mpf(3)/2*U,mp.inf,regularized=True)
 p=PL+PR
 ratio=p/mp.mpf(q)*mp.power(mp.mpf(sigma)/q,k)
 bound=mp.exp(-mp.mpf(31)*U/375)/60
 assert ratio<=bound and ratio<1 and k>=U
 results.append({'U':str(u),'m':m,'k':k,'log10_actual_ratio':mp.nstr(mp.log10(ratio),14),'log10_certified_upper':mp.nstr(mp.log10(bound),14),'pass':True})
assert Fraction(120,149)<Fraction(81,100)
assert Fraction(361,20000)>Fraction(13,750)
assert Fraction(149*13,750)-Fraction(5,2)==Fraction(31,375)
res={'fixed_lambda':'3/2','q':q,'sigma':sigma,'A':1,'k_formula':'floor(150U)-1','full_U_range':'all real U>=1','rigorous_bound':'[integral outside U..1.5U u^k exp((2-sigma)u)/k!du]*sigma^k <= (1/60)*exp(-31U/375) < 1','proof':'m=floor(150U)>=149U; k=m-1>=U; gamma rate120 shape m; lower threshold ratio<=120/149<0.81, upper ratio>=1.2; both h(r)=r-1-log r at least13/750; Ptail<=2exp(-149*13U/750); factor sigma^k*120^-m <=(1/120)*exp(5U/2); combine.','regressions':results}
open('/mnt/data/riemann_20261123_1728/landau_kernel_sigma122.json','w').write(json.dumps(res,indent=2))
print(json.dumps(res,indent=2))
