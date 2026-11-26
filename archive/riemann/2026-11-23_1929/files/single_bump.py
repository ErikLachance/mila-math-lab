import mpmath as mp, json, time
from fractions import Fraction
mp.mp.dps=65
start=time.monotonic()
def H(z,N):
    return mp.fprod(mp.sinh(z/mp.mpf(2)**j)/(z/mp.mpf(2)**j) if z else 1 for j in range(1,N+1))
# for |z| <= R, a_j R <= 1: |sinh(w)/w-1| <= |w|^2 (from power series).
# tail product absolute error <= exp(R^2*sum a_j^2)-1 <= 2 R^2*4^-N/3 when tail sum <= 1/2.
checks=0; max_rel=mp.mpf(0)
for R in [1,2,4,8,16,32]:
    for N in [12,20,30]:
        b=Fraction(R*R,3*4**N); assert b < Fraction(1,2)
        for beta in [mp.mpf('0.05'),mp.mpf('0.2'),mp.mpf('0.49')]:
            for gamma in [mp.mpf('0.1'),mp.mpf('0.5'),mp.mpf('0.95')*R]:
                z=mp.mpc(beta,gamma)
                if abs(z)>R: continue
                p=H(z,N); q=H(z,100); assert p!=0
                rel=abs(q/p-1); bound=mp.mpf(2*b.numerator)/b.denominator
                assert rel <= bound
                max_rel=max(max_rel,rel/bound);checks+=1
# finite quartet off-line model. Real-even transform ensures conjugation/reflection. Choose t phases aligning leading exponential.
quartet=[]
for beta in [mp.mpf('0.05'),mp.mpf('0.2'),mp.mpf('0.45')]:
    gamma=mp.mpf('14.134725'); z=mp.mpc(beta,gamma); c=H(z,80)**2
    zs=[z,mp.conj(z),-z,-mp.conj(z)]
    for n in [30,100,300]:
        t=(2*mp.pi*n-mp.arg(c))/gamma
        f=mp.fsum([H(zz,80)**2*mp.exp(t*zz) for zz in zs])
        exact=2*mp.re(c*mp.exp(z*t)+c*mp.exp(-z*t));assert abs(f-exact)<mp.mpf('1e-55')*max(1,abs(f))
        quartet.append({'beta_offset':str(beta),'t':float(t),'observed_log_abs_over_t':float(mp.log(abs(f))/t),'phase_aligned_ratio_to_exp':float(mp.re(f)*mp.exp(-beta*t))})
report={'product_tail_numeric_checks':checks,'largest_fraction_of_analytic_tail_bound':float(max_rel),'quartet_phase_aligned_checks':quartet,'elapsed_code_seconds':time.monotonic()-start,'warning':'mpmath numerical falsification only; analytic proof separate. Quartet is hypothetical, not zeta zeros.'}
print(json.dumps(report,indent=2));open('/mnt/data/riemann_20261123_1927/single_bump_result.json','w').write(json.dumps(report,indent=2))

