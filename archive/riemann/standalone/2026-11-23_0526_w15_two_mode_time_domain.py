#!/usr/bin/env python3
"""Independent small Galerkin cross-check of signed Weil form using time-domain kernel."""
import mpmath as mp, json,time
from pathlib import Path
start=time.monotonic();mp.mp.dps=60
L=mp.mpf(81)/100;w=mp.mpf(1)/15;s=mp.log(5);c5=s/mp.sqrt(5)
h0=mp.digamma(mp.mpf(1)/4)-mp.log(mp.pi)
K=lambda u:mp.exp(u/2)/mp.sinh(u)
d=2*L-w
# Normalized indicators on the left and right collars.
arch_diag=h0+mp.quad(lambda t:K(t)*t/w,[0,w])+mp.quad(lambda t:K(t),[w,1,10,100,mp.inf])
arch_cross= -mp.mpf('.5')*(mp.quad(lambda t:K(t)*(t-(d-w))/w,[d-w,d])
                   +mp.quad(lambda t:K(t)*((d+w)-t)/w,[d,d+w]))
# Normalize each basis vector by sqrt(w): end-to-end direct pole integrals.
def av(u,v):return (2*(mp.sinh(v/2)-mp.sinh(u/2)))/mp.sqrt(w)
def bv(u,v):return (2*(mp.cosh(v/2)-mp.cosh(u/2)))/mp.sqrt(w)
aL=av(-L,-L+w); aR=av(L-w,L)
bL=bv(-L,-L+w); bR=bv(L-w,L)
assert abs(aL-aR)<mp.mpf('1e-55') and abs(bL+bR)<mp.mpf('1e-55')
pole_diag=2*(aL*aL-bL*bL)
pole_cross=2*(aL*aR-bL*bR)
overlap= max(mp.mpf(0),w-abs(s-d))/w
prime_cross=-c5*overlap
D=arch_diag+pole_diag
X=arch_cross+pole_cross+prime_cross
lowest=D-abs(X)
highest=D+abs(X)
# Finite-section all-functions certificate claimed >1/60. Test only these 2 indicators.
assert lowest>mp.mpf(1)/60
rep={'L':str(L),'w':str(w),'source':'Suzuki 2606.09096v4 Weil form and Zhu 2608.24827v2 signed pole','arch_diagonal':mp.nstr(arch_diag,30),'arch_cross':mp.nstr(arch_cross,30),'pole_diag':mp.nstr(pole_diag,30),'pole_cross':mp.nstr(pole_cross,30),'prime5_overlap':mp.nstr(overlap,30),'prime5_offdiag':mp.nstr(prime_cross,30),'full_diagonal':mp.nstr(D,30),'full_offdiagonal':mp.nstr(X,30),'smallest_2by2_eigenvalue':mp.nstr(lowest,30),'largest_2by2_eigenvalue':mp.nstr(highest,30),'claim_check_smallest_gt_1_over_60':True,'elapsed_seconds':time.monotonic()-start,'scope':'independent two-mode numerical cross-check only; discontinuous indicator functions; NOT rigorous global positivity or RH proof'}
Path(__file__).with_suffix('.json').write_text(json.dumps(rep,indent=2))
print(json.dumps(rep,indent=2))
