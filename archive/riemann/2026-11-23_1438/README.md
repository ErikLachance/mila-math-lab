# Riemann Proof Watch - append-only research checkpoint, 2026-11-23 14:38 EST

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_CHECKPOINT_2026-11-23_1438_EST.md`. **Recorded time label:** 2026-11-23 14:38 EST (from the filename).

[Archive index](../../README.md) · [Manifest](../../manifest.json) · [Verification scope](../../README.md#what-was-checked-during-import)

**Status:** Partial research checkpoint, not a new RH proof. This checkpoint records several separate tests and derivations.

## Scientific continuity

Earlier Riemann checkpoint: `2026-11-08 15:30:58 EST -- W12 rational support certificate`: a claimed exact-rational positive signed Weil quadratic form only on two endpoint collars of L=.81 with w=1/12, **not** a proof of positivity on whole (-L,L), and not RH. Earlier finite Fourier 16D block, codimension <=14 estimate, mixed core/collar coupling, incomplete Schur/IMS estimates, and known false float64 sign changes are not to be repeated as conclusive. The source-to-code argument and all prior finite certificates are not independently peer reviewed.

Also read relevant research checkpoints, particularly `RIEMANN_SUPPLEMENT_2026-11-23_1420_EST.md` and `RIEMANN_SUPPLEMENT_2026-11-23_1414_EST.md`; earlier in the day they already derived the Laurent identity `integral_1^infty (psi(u)-u) du/u^2 = -1-EulerGamma`, H12 quantifier guards, gamma-Chernoff window analysis, a conductor-*uniform missing Euler factor bound*, and a warning that a working human manuscript is NOT a full independent conventional proof. This run does **not** re-claim those as new.


## Actual new research passes - analytic bridge to the 2026 Alpoge-Claude main inequality (M)

**Source fidelity:** Michael Rubinstein's November 22 v2 human explanation https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf gives a positive-part prime-power sum P (excluding p=2 and an auxiliary q), and its main term M involving `-1-EulerGamma + L'/L(1,chi_d) - geometric_mean(log weights)`. The source itself explicitly says inequality (M) and 13 H0-H12 prerequisites have NOT all been proved in this human-readable draft; this does not impugn the separately verified Lean formalization. An attempted web PDF screenshot gave `Cache miss`, so no unverified PDF-page-specific typography claim is made. A later public human reconstruction was read instead as *plain TeX* at https://github.com/jimjamzola/RH-Alpoge-Reconstruction .

### New pass A - finite exact and asymptotic quadratic-character prime-sum identity

For a fixed real nonprincipal Dirichlet character chi, `a>0, w>0, y=a/w>=1`, define the ALL-prime reference model:

`S_chi(y) = sum_{p^k<=y} (1-chi(p)^k) log(p) * (1/p^k-1/y)`.

At equality p^k=y the term is zero; `S>=0` for quadratic chi. Put `psi_chi(t)=sum_{p^k<=t} chi(p)^k log p`. Finite Stieltjes/Abel summation gives the EXACT identity for every y>=1:

`S_chi(y)=integral_1^y (psi(t)-psi_chi(t))/t^2 dt`.

For a fixed nonprincipal character, using classical (unconditional) PNT with zero-free-region error and Dirichlet PNT in progressions, the two improper integrals converge, and Laurent expansions of `-zeta'/zeta` and `-L'/L` at 1 give the rigorous asymptotic:

`S_chi(y)= log(y)-1-EulerGamma + (L'/L)(1,chi) + R_chi(y)`,

`R_chi(y)= integral_y^infty (psi_chi(t)-psi(t)+t)/t^2 dt`.

Therefore multiplying by a, the exact constants become `a*(log(a)-log(w)-1-EulerGamma + L'/L(1,chi))`, precisely the structure of the M term for **uniform** weights and **ALL** primes. It does NOT license the original weighted-cell (M) formula for arbitrary cell allocations, and does NOT automatically permit omitted primes 2,q or nonuniform conductors. This is the decisive limit of this pass.

Independent executable check `riemann_20261123_1431_prime_bridge.py`: reconstructs all prime powers <=1,000,000, checks two independent finite sum implementations, max discrepancy 2.8e-13. Computes `L'/L(1,chi_-3)=0.3682816159701478426...` and `L'/L(1,chi_-4)=0.2456095847773141724...` via Hurwitz generalized Stieltjes regularization. A naive direct difference of two Hurwitz zeta values *at the pole s=1* returned `nan`, so that evaluation was REJECTED and repaired; false numerics are not presented as valid. Residual S - [log y -1-gamma+cchi] for y=1e6: chi=trivial baseline +1.10404e-5, chi_-3 +2.71935e-5, chi_-4 +2.98908e-5. Numeric convergence is falsification-only; the proof is the analytic identity plus cited PNT facts.

### New pass B - exact finite transport identity independent of limiting PNT

For 1<X<Y and either fixed quadratic character, `D_chi(y)=S_chi(y)-log(y)` satisfies **unconditionally**

`D_chi(Y)-D_chi(X)=integral_X^Y [psi(t)-psi_chi(t)-t]/t^2 dt`.

This follows by differentiating between prime-power thresholds (S is continuous through each threshold) or subtracting exact finite identities; it needs no asymptotic, no RH and no assumption about cchi. Script `riemann_20261123_1431_error_transport.py` evaluated 12 channel/interval pairs, including chi_-3 and chi_-4 on X=100,1000,10000,100000 to Y=10X. Two independent implementations (prime-power sum difference vs stepwise exact interval integral in double precision) agree within 2.8e-14. The deliberate 'primes-only' approximation **omitting p^k with k>=2** gave persistent nonvanishing errors (~0.753 at y=1e6 for trivial character, ~0.447 for chi_-3, ~0.455 for chi_-4), so prime powers must not be discarded.

### New pass C - cell-weight correlation is not determined by geometric mean

For arbitrary positive cell weights w_c, the EXACT finite identity is

`P_cell = a * sum_c integral_1^(a/w_c) Psi_c(t)/t^2 dt`, where `Psi_c(t)=sum_{p^k<=t:cell(p^k)=c} (1-chi(p)^k) log p`, with an empty integral when a/w_c<=1. This is a finite interchange, valid without PNT. Replacing the cell distribution by equal-density average is **not** justified unless one proves arithmetic equidistribution sufficiently uniform in the growing moduli and shifting cell weights.

Toy computational falsification, NOT the actual automorphic cell assignment: four synthetic cells at a=1, d=3 (quadratic chi), exclude p=2 and auxiliary q=7 exactly as in the source prime scope; weights (1e-4,1e-2,1e-2,1e-2) permuted between cells. All have the SAME geometric mean, so the naive M-like comparison is identical =4.54752868355. Nevertheless the exact positive-part sums are respectively 2.53448523567 when small weight sits on chi=+1 (inactive), 7.02848766867 when small weight sits on chi=-1 (active), 2.58424867180 when small weight sits on chi=0, and 2.53448523567 when the small weight sits in an empty cell. No 'error in Lean' is inferred, since the actual construction restricts cell layout strongly. `riemann_20261123_1431_fourcell_source_scope.py/json`. The earlier three-cell variant is also archived but is less source-fidelitous and should not be cited as the main regression.

### New pass D - conductor-*varying* character sign patterns and sharp finite envelope

**Rigorous elementary lemma:** For any finite set S of rational primes and any prescribed signs eps_p in {+1,-1}, there are infinitely many PRIME conductors ell congruent 1 mod 4 such that the quadratic primitive character chi_ell(p)=(p/ell)=eps_p for every p in S. Proof: choose ell congruent 1 or 5 mod 8 to prescribe the symbol of 2; for each odd p choose a residue or nonresidue r_p mod p; CRT combines these and Dirichlet's theorem on primes in arithmetic progressions supplies infinitely many primes ell. Quadratic reciprocity gives (p/ell)=(ell/p). No RH or generic uniform PNT in q is involved.

In particular, for every cutoff y, infinitely many quadratic primitive characters with conductors ell>y have chi_ell(p)=+1 for every p<=y, so `S_chi_ell(y)=0` EXACTLY (all prime powers vanish). Also characters with chi_ell(p)=-1 for every p<=y exist, making the odd-power contribution maximal. For the uniform-weight source scope excluding p=2 and a fixed q=7, and prime conductor ell>y, the SHARP CHARACTER-UNIFORM ENVELOPE is

`0 <= P^odd,q_chi_ell(y)/a <= 2*sum_{p^k<y, p notin {2,q}, k odd} log(p)*(1/p^k-1/y)`.

Both endpoints are attained by infinitely many prime ell (not all intermediate values). In fact all even k terms vanish when chi(p)=+/-1, while odd k have coefficients 0 or 2. Numeric examples for y=100 with q=7 give upper endpoint 3.92744002202, lower endpoint 0. For all-primes y=100, plus-pattern prime ell=46111359278910368495062042946635121401 yields S=0, minus-pattern prime ell=87995321176219449974135873673999044717 yields S=5.3126629909954. Full residue, primality, Legendre tests for cutoffs 10,30,100 PASS with SymPy; exact proof relies on CRT, reciprocity and Dirichlet. These are formal finite-scale limitations: fixed-character `S=logy+constant+o(1)` is NOT uniform across conductor growing with y. Thus the key H12 demand for suitable *simultaneously good* auxiliary primes at EVERY point of large windows cannot be replaced by arbitrary-character PNT. `riemann_20261123_1431_adversarial_quadratic.py`, `..._extreme_quadratic.py`, `..._sharp_uniform_envelope.py` and JSON.

### New pass E - missing fixed Euler-factor contributions cannot be silently dropped

The loss from deleting a single prime p from the ALL-primes S is the finite nonnegative sum `E_p(y)=sum_{p^k<y} (1-chi(p)^k)log(p)*(1/p^k-1/y)`. It has exact nonnegative limit as y grows

`E_p(infty)=log(p)*[1/(p-1)-chi(p)/(p-chi(p))] <= 2log(p)/(p-1)`.

For chi_-3 at p=2 the limit is `(4/3)log2=0.92419624`; for chi_-4 at p=2 the limit is `log2=0.69314718`. Thus omitting p=2 changes the constant term, not an o(1) error; deleting a large auxiliary q costs at most `2log(q)/(q-1)` if real quadratic chi. Script `riemann_20261123_1431_omitted_primes.py/json` tested 12 (character, prime) pairs at y=100,1000,1e6; all finite values lie between 0 and the analytic limit. The theorem follows by a simple geometric series; numerical tests are not the proof.

### New pass F - independent classical CM constant source audit, class-number >1

Read *plain TeX* `manuscript/sec15_heights.tex` in independent human reconstruction https://github.com/jimjamzola/RH-Alpoge-Reconstruction/blob/main/manuscript/sec15_heights.tex (blob `87e3cb0f78d0a42cb33b1afb05b8a9ef5724970f`). It cites Kronecker's first limit formula to assert, for prime d>3, d congruent 3 mod4:

`(1/h) sum_classes log(A(Lambda_C)/pi) = EulerGamma + log(2pi/sqrt(d)) - L'/L(1,chi_-d)`.

Tested independently with high-precision mpmath for Heegner class-number-1 d=7,11,19 (binary eta product at tau=(1+i sqrt(d))/2; character log-derivative via generalized Stieltjes). Each sides agree to about 60 digits. Further class-number >1 test enumerated all reduced primitive binary quadratic forms and computed the modular eta product for every class: d=23 (h=3), d=31(h=3), d=47(h=5), d=59(h=3). Left averaged log(A/pi) and right above agree within 1.4e-60 at 60-digit precision. For example d=23, both sides 1.2694665713847508242755...; d=47, both sides 1.1311780498095989622157... This is independent NUMERICAL source-fidelity testing of signs, factor 2, class averaging and normalization; NOT a formal proof of Kronecker or a new analytic ingredient. Scripts `riemann_20261123_1431_kronecker_heegner.py` and `..._kronecker_multiclass.py/json`. Reference to formal RH argument itself remains indirect.

## External status verified this run

- Lean and Mathlib communities' Nov21 statement https://leanprover-community.github.io/blog/posts/riemann-hypothesis/ says it independently certified both the RH statement and its formal proof under standard axioms; I did NOT myself compile 17 million Lean lines.
- MIT Andrew Sutherland public verification dashboard https://math.mit.edu/~drew/grh/ (web search preview as of Nov22; independent updated reporting dated Nov23), multiple kernel, independent checker and comparator passes. Some longer checks still running; do not claim all checks finished.
- Clay Mathematics Institute https://www.claymath.org/millennium/Riemann-Hypothesis/ currently says `Unsolved`; formal verification vs official mathematical/prize acceptance are different stages.
- Waterloo working draft v2 Nov22 https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf says it reduces (M) to 13 stated hypotheses and does not itself prove (M). An attempted PDF screenshot on the web tool failed `Cache miss` and no page-specific visual inference was made.

## Adversarial limitations and next highest-value angle

No result in this run proves or disproves RH independently. No numerical convergence or toy cell example is a proof of the full (M) inequality. The sharp envelope for *arbitrary* quadratic characters highlights why H12's conductor, character, compatibility and window quantifiers matter; it is NOT a counterexample to a source with highly constrained simultaneous auxiliary primes. Fixed-conductor PNT must not be silently promoted to conductor-growing uniformity. The Kronecker tests audit a conventional classical factor only; the automorphic theta-lift, integral lattices, nondegeneracy, Bessel period and Sha/cohomology inputs remain the difficult heart. The old signed Weil method's mixed form and domain issues remain unclosed. The human reconstruction may have gaps but the formal Lean proof has passed strong independent external checks.

**Next experiment:** explicitly map the local prime-sign CRT counterfamilies to which H12 compatibility constraints exclude them, and verify whether its required arithmetic constants are uniform in the exponentially growing d. In the 225-page independent manuscript `sec12_loss.tex` and `sec15_heights.tex`, audit a *different* named published input (not the Kronecker factor already checked), e.g. a small-rank Hecke nondegeneracy toy or the lambda1 vs CM-period identity with strict normalization, then test with exact rational/interval tools and avoid speculative accusations. Consider a reproducible extraction of the original Lean statements for (M) once feasible; a human draft is not sufficient to attribute an error to Lean.


