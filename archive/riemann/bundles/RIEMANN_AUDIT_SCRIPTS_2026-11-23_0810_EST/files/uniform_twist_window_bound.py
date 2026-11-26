import mpmath as mp, json
from pathlib import Path
mp.mp.dps=90
root=Path('/mnt/data/riemann_20261123_0751')

def threshold(tau,C,eta):
    Q=32*C/(eta*tau*(1-mp.power(2,-tau)))
    return mp.log(Q)/tau

cases=[]
for e_str in ('0.01','0.005','0.001'):
    eps=mp.mpf(e_str);tau=eps/2
    assert tau>0 and eps<mp.mpf(1)/52
    C=mp.mpf(1);eta=mp.mpf('.1')
    L=threshold(tau,C,eta)
    def bad_fraction(logY):
        return 32*C/(tau*(1-mp.power(2,-tau)))*mp.exp(-tau*logY)
    assert abs(bad_fraction(L)/eta-1)<mp.mpf('1e-75')
    assert bad_fraction(L-mp.mpf('.01')/tau)>eta
    assert bad_fraction(L+mp.mpf('.01')/tau)<eta
    cases.append({'epsilon':e_str,'tau':mp.nstr(tau,10),'logY_sufficient_threshold':mp.nstr(L,35),'log10Y_sufficient_threshold':mp.nstr(L/mp.log(10),35),'bad_fraction_on_threshold':mp.nstr(bad_fraction(L),20)})

# Proof of dyadic Cauchy-Schwarz derived from two mean-square inputs:
# A=sum |S_p(a)|^2 <= C a log(a) P; B(v)=sum|D_p(v)|^2 <= C (log v)/v P.
# per p and w_p in[a,b], |S_p(w_p)|^2 <= 2|S_p(a)|^2+2a int |D_p(v)|²;
# sum <= 2C a log(a) P + 2CaP*int_a^b (log v)/v dv
# <= 2C a log(2a)P + 2Ca log(2a)log2 P <4Ca log(2a)P.
# If bad threshold |S_p(w_p)|>.5w_p^(1/2+tau), contributions >a^(1+2tau)/4,
# hence bad fraction <=16C log(2a)/a^(2tau) <=32C/(tau a^tau)
# where log(2a) <=(2a)^tau/tau <=2a^tau/tau for tau<=1.
# sum over a_j=2^jY yields 32C/tau*Y^-tau/(1-2^-tau).

# For fixed positive R prior exceptional twist classes and independent union bound:
union=[]
for R in (1,2,10,100):
    # error budget per family eta/(2(R+1)); other half for zero boxes
    tau=mp.mpf('.005'); eta=mp.mpf('.1')
    family_eta=eta/(2*(R+1))
    L=threshold(tau,mp.mpf(1),family_eta)
    union.append({'number_existing_families':R,'log10Y_sufficient':mp.nstr(L/mp.log(10),15),'fraction_bad_per_family':mp.nstr(family_eta,15)})

out={'uniformity_lemma':'Assuming uniform mean-square bound on S_p(a) and D_p(v) with one C for all a in [Y,Y^K], the fraction of primes bad somewhere is <=[32 C/(tau(1-2^-tau))] Y^-tau for tau in (0,1], Y>=2. No probabilistic independence or discretization needed.','proof_steps':['Cauchy-Schwarz for each p along [a,b]','sum C a log(a) and C log(v)/v bounds','Markov on maximum point w_p to get 16C log(2a)/a^(2tau)','monotone bound log(2a)<=2a^tau/tau','sum dyadic geometric series'], 'thresholds_for_illustrative_C_1_eta_.1':cases,'illustrative_union_bound_families':union,'caveat':'The uniform mean-square inputs, zero-free box and simultaneous admissible prime existence remain deep external assumptions; threshold sizes are illustrative and not explicit effective bounds for the actual theory.'}
(root/'uniform_twist_window_bound.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
