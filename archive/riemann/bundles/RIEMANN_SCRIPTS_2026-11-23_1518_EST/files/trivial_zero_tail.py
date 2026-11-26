import mpmath as mp,json
mp.mp.dps=90
out=[]
for xx in ['1.5','2','3','10','100','10000']:
 x=mp.mpf(xx); z=1/x
 closed=1-mp.log1p(-z*z)/2-mp.atanh(z)/z
 direct=mp.fsum([z**(2*k)/(2*k*(2*k+1)) for k in range(1,351)])
 lo=z*z/6; hi=lo/(1-z*z)
 out.append({'x':xx,'T_closed':mp.nstr(closed,30),'T_series':mp.nstr(direct,30),'difference':mp.nstr(closed-direct,12),'lower_ge':closed>=lo,'upper_le':closed<=hi,'first_term':mp.nstr(lo,12),'bound_hi':mp.nstr(hi,12)})
print(json.dumps({'formula':'sum_(k>=1) x^(-2k)/(2k*(2k+1)) = 1 - .5 log(1-x^-2) - x atanh(x^-1)','sign':'Each trivial zero -2k gives a NEGATIVE term of this positive tail in G(x) contour expansion','out':out},indent=2))
with open('/mnt/data/riemann_run_20261123_1457/trivial_zero_tail.json','w') as f:json.dump({'out':out},f,indent=2)
