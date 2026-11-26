from fractions import Fraction
import mpmath as mp
import json
mp.mp.dps=65
L=mp.mpf(81)/100
w=mp.mpf(1)/40
A=mp.mpf(15)/4
T=mp.pi/(2*w)
H=lambda t: mp.re(mp.digamma(mp.mpf(1)/4 + 1j*t/2))-mp.log(mp.pi)
H0=H(0)
low_crude=mp.log(10)-1-(mp.mpf(87)/(80*mp.pi))
low_exact_integral=(2*w/mp.pi)*mp.quad(H,[0,A,6,20,T])
const_arith=mp.log(5)/mp.sqrt(5)
const_pole=4*w*mp.sinh(L/2)**2
certified_rational=Fraction(71,80)-Fraction(3,4)-Fraction(1,40)
# endpoint shift support n5: s=ln 5 in (2L-2w,2L), all others n<=5 do not intersect the collars
prime_shifts={str(n):str(mp.log(n)) for n in [2,3,4,5]}
delta=2*L-mp.log(5)
assert 0 < delta < w
assert 2*(L-w)>mp.log(4)
assert H0 > -6
assert low_crude > mp.mpf(71)/80
assert low_exact_integral > low_crude
assert const_arith < mp.mpf(3)/4
assert const_pole < w
assert certified_rational == Fraction(9,80)
# exact finite analog spectral test: disjoint matched endpoint subintervals, each basis vector normalized.
# The prime-5 compression acts as -c times an exchange matrix; independent of overlap delta>0.
import numpy as np
for N in [1,2,4,8,16,32]:
    c=float(const_arith)
    M=np.zeros((2*N,2*N))
    for j in range(N):
        M[j,N+j]=M[N+j,j]=-c
    eig=np.linalg.eigvalsh(M)
    assert np.max(np.abs(np.abs(eig)-c)) < 2e-15
report={
  'date':'2026-11-23', 'purpose':'independent support-collar positivity lower bound; not RH proof',
  'L':str(L),'w':str(w),'E':['(-0.81,-0.785)','(0.785,0.81)'],
  'A':str(A),'T':str(T),'H0':str(H0),'arch_bathtub_actual_integral':str(low_exact_integral),
  'arch_crude_lower':str(low_crude),'arch_rational_lower':'71/80',
  'prime5_overlap_delta':str(delta),'prime_shifts':prime_shifts,
  'prime5_coefficient':str(const_arith),'prime5_rational_upper':'3/4',
  'negative_odd_pole_bound':str(const_pole),'pole_rational_upper':'1/40',
  'Q_norm_lower_simple':'9/80', 'scope':'smooth complex test functions supported in E, using source Weil formula and Zhu high digamma lower t>=15/4',
  'spectrum_test_N':[1,2,4,8,16,32], 'spectrum_test':'PASS, prime5 active-pair exchange matrix has eigenvalues +-log(5)/sqrt(5)',
  'caveats':'Fourier bathtub yields an analytically justified lower bound under H monotonicity; must verify complex signed pole decomposition. This does not extend to arbitrary f in full window.'
}
with open('/mnt/data/riemann_research_20261123/collar_bound_report.json','w') as f:json.dump(report,f,indent=2)
for k,v in report.items():print(k,':',v)
