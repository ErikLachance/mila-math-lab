# Riemann proof watch - append-only checkpoint, 2026-11-23 17:06 EST

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_CHECKPOINT_2026-11-23_1706_EST.md`. **Recorded time label:** 2026-11-23 17:06 EST (from the filename).

[Archive index](../../README.md) · [Manifest](../../manifest.json) · [Verification scope](../../README.md#what-was-checked-during-import)

## Scientific continuity


Earlier Riemann checkpoint: 2026-11-08 15:30:58 EST. It asserts an endpoint-collar support-restricted exact-rational lower bound with L=.81, w=1/12 for Weil form, explicitly not full-window positivity or RH. Known failed/insufficient routes: 16-dimensional Galerkin positivity cannot control an infinite-dimensional complement; core/collar mixed terms swamp established small coercivity margins; crude IMS localization errors too large. Do not recycle them without new certified tail/mixed estimates.

Preceding research checkpoints: `RIEMANN_SUPPLEMENT_2026-11-23_1611_EST.md` and prior `RIEMANN_CHECKPOINT_2026-11-23_1602_EST.md` and `RIEMANN_CHECKPOINT_2026-11-23_1537_EST.md` were read. Earlier 16:11 work established limitations of direct rank-2-to-rank-3 symmetric-square transfer, exact ray-prime C9 dyadic reduction and source fidelity gap, non-Dirichlet Hecke characters for K=Q(sqrt(-23)), and elementary conductor estimates. This checkpoint does NOT falsely claim novelty for those previous results.


## Primary sources consulted directly this run

- Levent Alpoge, primary author note and October-November timeline, https://alpo.ge/remark.pdf (text inspected; web PDF screenshot of page 3 inspected). The October 9 step says D^p=0 modulo inert CM primes and describes derivative/period valuations of the form a/p+a/p^3+...-O(log a); a November step uses chains of theta lifts of length approximately sqrt(X).
- Lean FRO + Mathlib Initiative statement 2026-11-21, https://leanprover-community.github.io/blog/posts/riemann-hypothesis/ : externally certified original Lean Riemann statement and formal proof.
- Andrew Sutherland (MIT), independent verification report last UPDATED 2026-11-23 14:35 UTC, https://math.mit.edu/~drew/grh/ : 175,187 Lean modules compiled, three standard axioms, 2 independent source-to-statement comparisons, full original kernel accepts and unmodified Comparator v4.33.0 prints 'Your solution is okay!'; paranoid kernel with allocator adjustment accepted Nov 23; two slower default/canonical runs still marked running at report time. We did NOT run the 17 million line code locally.
- Andrew O'Desky, independently prepared interpretive map of the Lean project, https://andrewodesky.com/rh/ : 1,722 Lean theorem statements, 24 high-priority statements, only ~6-7 of 24 statements and 7 of 24 tier-one proofs currently reviewed, and 17 prose proofs written. This is a HUMAN/LLM-generated interpretive reconstruction, NOT equivalent to the original fully formally checked Lean proof. Its 'Landau theorem on intervals' and 'Weighted prime-sum bound' sections were read directly (including equations and dependency lists).
- Christophe Debry, 'Beyond two criteria for supersingularity: coefficients of division polynomials', arXiv:1303.5002, https://arxiv.org/abs/1303.5002 : classical coefficient-of-x^(p-1) test for supersingularity.
- McGill Peter Darmon modular forms lectures, https://www.math.mcgill.ca/darmon/courses/16-17/mf/blog.html : Hasse invariant and supersingularity.
- University of Chicago lecture note on Cartier and Hasse invariant (public draft), https://www.math.uchicago.edu/~fcale/papers/AWS.pdf ; web result only, NOT downloaded/visually analyzed; no theorem from its PDF used as independently verified.
- Background for restricted Lie p-power: https://en.wikipedia.org/wiki/Restricted_Lie_algebra (expository, not substituted for a primary proof).

## Micro-pass A: exact algebraic test of Alpoge's 10/9 inert-CM derivative idea

For p>=5 and an integral elliptic Weierstrass equation E: y^2=f(x), define the invariant derivation
 D(x)=2y, D(y)=f'(x),
 D(A(x)+B(x)y)=[2 f B'+f' B]+[2 A']y.
All computations use exact integer or F_p polynomial arithmetic with y^2=f, never float64. For j=0 take f=x^3-1 (CM by Q(sqrt(-3))); for j=1728 take f=x^3-x (CM by Q(i)). For odd p define H_p=[x^(p-1)] f^((p-1)/2) mod p. Algebraic binomial expansion gives for f=x^3-1 that H_p=0 exactly when p=2 mod3, while if p=1 mod3 then H_p=(-1)^(m-k)*binom(m,k), with m=(p-1)/2,k=(p-1)/3, nonzero mod p because 0<=k<=m<p. Similarly for f=x^3-x, H_p=0 exactly when p=3 mod4; in the split case k=m/2 and its binomial coefficient is nonzero mod p. Exclude p=2,3 as bad characteristic cases.

Independent recurrence computed D^p(x) modulo p, and for every prime 5<=p<151 (33 primes) on each of two curves (66 test cases) observed D^p(x)=H_p*2y; no x-component. Exact finite tests all passed, including zero iff inert and Hasse coefficient identity. As D^p is a derivation in characteristic p, its value on x plus relation y^2=f determines its value on y in the smooth integral domain; hence for the TESTED inert cases D^p=0 on the coordinate ring. A general proof of D^p=H_p D needs the standard Hasse/restricted-Lie identity beyond these finite computations; do not promote the regression to a proof for all curves/all primes. The H_p zero/congruence statements themselves follow from the explicit binomial expansions for all p>=5.

Program `hasse_derivation.py` and machine-readable `hasse_derivation_results.json` saved locally.

## Micro-pass B: quantitative integral derivative valuations and a falsified shortcut

For the integral recurrence (without reducing mod p) and coefficientwise v_p(D^a x), v_p(D^a y), at inert p=5 of j=0 curve, all 700 evaluations (2 generators times a=1..350) satisfy the stronger TESTED bound
 v_5(D^a generator) >= floor(a/5)+floor(a/125).
At a=125, exact minimum coefficient valuation is 26 for x and y, compared with first-level floor(a/5)=25. At a=250, it is 52 vs 50. At p=7 inert on j=1728, a=1..700 for x and y (1400 tests) satisfy
 v_7(D^a generator) >= floor(a/7)+floor(a/343).
At a=343, valuation is 50, versus floor(343/7)=49. At a=686, valuation is 100 versus 98. This matches the shape of a/p+a/p^3 in author's reported inert-CM theta differentiation, but only for generators of two tiny coordinate rings and finite a. It is NOT a global general formal-group theorem, not a normalized theta-period divisibility theorem and not proof of RH.

The easy fact D^p maps the integral coordinate ring into p times itself implies only v_p(D^a f)>=floor(a/p) (under good integral normalization). It CANNOT by itself imply the additional a/p^3. Counterexample: free Z_p module with basis e_0...e_{p-1}, linear operator T(e_i)=e_{i+1} for i<p-1, T(e_{p-1})=p e_0. Then T^p=p I. Yet the minimal coefficient valuation of T^a is exactly floor(a/p) for all a. For a=p k this falls behind a/p+a/p^3-C log a by k/p^2-C log(pk), which diverges for fixed C. This is an algebraically rigorous obstruction to using only first-level mod-p nilpotence; it is not a counterexample to the theta result because T is an arbitrary linear operator, not a geometric elliptic derivation. Additional higher-height structure is essential.

Programs `derivation_val.py`, `deriv_long_test.py`, `higher_divisibility_regression.py`, `j1728_higher.py` with JSON outputs.

## Micro-pass C: self-contained exact quantitative audit of Landau high-derivative concentration

O'Desky's source 'Landau theorem on intervals' requires: for logarithmic interval I_U=[U,(3/2)U], find fixed sigma>2,A and each U>=1 a k>=U such that
 integral_{u outside I_U, u>0} u^k exp((2-sigma)u)/k! du <= A/sigma^k.
The following explicit choice independently proves this IN THE SPECIFIC lambda=3/2 case: q=1000, sigma=1002, A=1, m=floor(1250 U), k=m-1. For U>=1, m>=1249U, k>=U. The integral equals q^{-m} times the tail of X~Gamma(shape=m,rate=q) outside [U,1.5U]. Chernoff's bound gives each tail <=exp(-m h(r)), h(r)=r-1-ln(r), with r=qU/m for left and 1.5qU/m for right. Here r_left<=1000/1249<801/1000, so h(r_left)>=(1-r_left)^2/2>13/750. Right r>=6/5, so h(r)>=h(6/5)>13/750, the last by the alternating upper truncation ln(1+t)<=t-t^2/2+t^3/3 for t=1/5. Thus P(X outside)<=2 exp(-1249U*13/750)<2 exp(-21U). Since ln(1+2/q)<=2/q and m-1<1250U, one has q(q/sigma)^(m-1)>=1000 exp(-2.5U), and 2 exp(-21U)<=1000 exp(-2.5U) for U>=1. Hence q^-m P <=sigma^-k, exactly as needed. This is a proof of this isolated gamma-concentration sublemma under stated normalization, NOT independent proof of the complete Landau theorem or the arithmetic interval bound.

As falsification checks, high-precision mpmath computed ratio [actual tail integral]/sigma^-k at U=1,7/5,2,9/2,10, all far below one (base-10 logs approx -12.77,-16.25,-21.43,-42.88,-89.87). Rational inequalities in script asserted exactly. Program `landau_gamma_concentration.py/.json`.

## Micro-pass D: why logarithmically expanding good intervals are indispensable

The same Landau theorem assumes upper control on arbitrarily large FULL intervals [Y,Y^lambda], lambda>1. It is NOT safe to weaken this to dyadic intervals [Y,2Y]. Rigorous toy counterexample: for beta=3/4>theta=3/5 let G(x)=x^beta cos(log x). Its Mellin transform for Re(s)>beta is (s-beta)/[(s-beta)^2+1], with genuine poles at beta +/- i. Let U_k=pi-(log2)/2+2*pi*k and Y_k=exp(U_k). Throughout x in [Y_k,2Y_k], log x lies in [pi-log2/2, pi+log2/2] modulo 2pi, so cos(log x)<0. Thus G(x)<=0<=x^theta on every one of infinitely many arbitrarily remote FULL DYADIC intervals despite the right-half-plane poles. This does NOT contradict the published theorem because [Y,Y^lambda] has logarithmic length (lambda-1)logY->infinity, eventually containing an arbitrarily large positive peak of cos. Independent mpmath falsification sampled 129 points in each of 30 successive dyadic intervals: all cos values negative. The proof is analytic, not just numerical. Program `landau_dyadic_counterexample.py/.json`. This extends prior run's sparse point-sampling warning to a stronger FULL fixed-ratio interval counterexample.

## Micro-pass E: character weights in the analytic-to-counting chain

O'Desky writes coset targets lambda(h)=4c on distinguished H0 and 3c on each other coset, c=1/(3o+1), with o=[H:H0]. Exact algebra: 4c+(o-1)*3c=1, so these are normalized masses. For any nontrivial character of cyclic quotient H/H0, sum_h lambda(h) chi(h)=(4c-3c)+3c sum_h chi(h)=c>0 by character orthogonality. For trivial character the coefficient is 1. This explains positivity in the weighted smoothed prime sums and absence of pole-residue cancellation in Landau step; it does not prove that arithmetic construction realizes those exact approximate masses. Code used exact finite-field primitive o-th roots, for o=2..63, 62 orders and 2015 characters, all coefficients matched mod suitable auxiliary primes. Script `coset_fourier_exact.py/.json`.

## Micro-pass F: why sqrt(X) from the author is structurally plausible yet not a solved bridge

The new O'Desky mapping reports two characteristic arithmetic errors of sizes x/m and m (up to x^epsilon factors), choosing x^(1/2-eps/16)<=m<=2 x^(1/2-eps/16). Pure algebra shows max(x/m,m) is minimized by m=sqrt(x); with this choice m=x^(1/2-eps/16), x/m=x^(1/2+eps/16), and m is smaller by x^(eps/8) in scale. This explains the half exponent mentioned in Alpoge's note as a BALANCING heuristic in the interpreted source. It does NOT independently establish existence of the automorphic theta chains, uniform arithmetic data or the claimed interval upper bound; these are the hard inputs. The exact link between X in the author note and x in O'Desky's write-up is NOT independently proven here.

## Status, adversarial limits, next high-information experiment

The original RH and all Dirichlet GRH are externally certified in the released Lean proof by community checkers, but we have NOT produced a new independent complete proof or run the 17-million-line kernel locally. Do NOT conflate incompleteness of O'Desky's interpretive prose, or of the separate jimjamzola human reconstruction, with hidden extra axioms or `sorry` in the verified original Lean archive. Do NOT turn finite Hasse experiments or simple gamma lemma into RH. The p-adic higher divisibility a/p^3 needs general height-two formal group proof with period normalization; converting it into theta-determinant multiplicity and the main long-interval character estimate remains an open reconstruction problem for us. Prior gap (C9) on ray-class dyadic primes and (G3) rank-three input in alternative human manuscript remain unfilled in that exposition; do not reuse an incompatible rank-two theorem.

Next experiment: derive a complete formal-group/Honda height-two argument for the second-scale p-adic derivative valuation bound, checking precision loss, denominators and transition from coordinate functions to theta sections; compare exactly against original Lean theorem's assumptions. Independently audit O'Desky's 'Compatible arithmetic data on intervals' and arithmetic existence of cyclic quotient/coset masses, NOT just formal Fourier identities.

**Status:** No new proof/disproof.
