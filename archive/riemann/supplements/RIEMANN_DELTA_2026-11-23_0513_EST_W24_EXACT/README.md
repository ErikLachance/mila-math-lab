# Riemann research: third append-only delta — 2026-11-23 05:13 EST, America/Toronto

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_DELTA_2026-11-23_0513_EST_W24_EXACT.md`. **Recorded time label:** 2026-11-23 05:13 EST (from the filename).

[Archive index](../../../README.md) · [Manifest](../../../manifest.json) · [Verification scope](../../../README.md#what-was-checked-during-import)


## New exact-rational restricted-support theorem (conditional only on source formula and high-precision arithmetic code correctness)

Let L=81/100 and w=1/24; E_w=(-L,-L+w) ∪ (L-w,L). Then for EVERY smooth compactly supported complex f in E_w, the **complete signed Weil form** satisfies

    Q_W(f) > (1/100) ||f||_2^2.

This is only positivity on the two outer collars, NOT positivity over the whole (-0.81,0.81), and not an original proof of RH. It is narrower than the previously journaled w=1/12 certificate, but unlike the earlier optimization its proof is a short independent spectral-density bound with a reproducible *exact rational* certificate. It improves the same-run independent elementary w=1/40 result to a wider w=1/24.

Detailed proof framework:
- Fourier F(t)=∫f(x)e^(itx) dx, normalized density rho=|F(t)|²/(2π||f||²), nonnegative with integral1. By Cauchy-Schwarz, rho≤w/π because support measure2w. H(t)=Re ψ(1/4+it/2)−lnπ is even and increasing for t≥0: from the elementary digamma series,

  H(t)=H(0)+Σ_{n≥0} t²/[a_n(4a_n²+t²)], a_n=n+1/4.

  The series is termwise nonnegative and each term increases in t. H(0)=−EulerGamma−π/2−3ln2−lnπ >−269/50, certified by rational Euler-Maclaurin, Machin π, and atanh log bounds.
- For T0=3769/100 (a rational just below the exact cap cutoff T*=π/(2w)=12π), the generalized bathtub inequality gives

  ∫_R H(t)rho(t)dt ≥ (2w/π) ∫_0^T0 H(t)dt + (1−2w T0/π) H(T0).

  The second coefficient is nonnegative since T0<T*. A derivation splits inside/outside ±T0: use rho≤w/π against H(t)−H(T0)≤0 in the interval, and outside H≥H(T0).
- Lower-integrate H on [0,T0] with 1024 left Riemann bins (H monotone); truncate its entirely nonnegative digamma series after1200 terms. Each bin/term is evaluated with integer floor at scale 10^12: t_i=T0*i/1024=p/q,

  term_i,n =16p² / [(4n+1)(q²(4n+1)²+4p²)] >= floor(10^12 * term)/10^12,

  with zero floating-point input for decisions. Thus the exact output is a mathematical lower bound for the archimedean energy, not a heuristic quadrature. Rational bounds on π are obtained by Machin arctangent alternating series; log2, logπ, log5 via atanh positive series with geometric remainder; gamma upper via Euler–Maclaurin and harmonic sum H64.
- The arithmetic shift terms n=2,3,4 vanish by support geometry (self-shifts ≥ln2>w and endpoint gap >ln4). Only n=5 survives since log5<2L=1.62. Its most negative contribution is >=-c5||f||² with c5=ln5/√5. Exact rational logarithm upper and sqrt5 lower give c5<18/25=.72.
- Signed pole +2|<f,cosh(x/2)>|² −2|<f,sinh(x/2)>|² >=−4w sinh²(L/2)||f||²; exact rational series verifies sinh(81/200)<5/12.
- Final certified rational lower from the program (decimals just for orientation): arch >0.7596008050, c5<0.719762831, negative pole >−0.028865253, hence Q/||f||²>0.01097272260>0.01. Each strict inequality was asserted using Python `fractions.Fraction`; floats were generated *only* after all decisions to print approximate diagnostics. The program asserts 1/100, 1/150, 1/200, etc., but NOT 1/80.

Recorded local files: `/mnt/data/riemann_research_20261123/w24_exact_bathtub.py` and `w24_exact_bathtub_report.json`; it imports `/mnt/data/riemann_research_20261123/w25_exact_bathtub.py`. The w25 script independently certified Q>1/300 for wider-than-w40 but narrower-than-w24 support, based on Zhu's high-t lower envelope and a low-frequency rational digamma series. First run of w25 code *failed at JSON serialization* due Python's 4300-digit integer-to-string limit after all mathematical assertions; fixed report to use numerator bit_length, rerun successfully, and then the w24 run completed with exact pass. This is not a mathematical failure and was not hidden.

**Rigor scope and adversarial caveats**: Certifies a bound only for f in C_c^∞(E_w), assuming the published exact signed Weil formula and the digamma identity. We independently verified from Zhu's Lemma6.1 (https://arxiv.org/html/2608.24827v2) the odd pole is negative and checked exact algebra of term t²/[a_n(4a_n²+t²)]. No claim to have formally verified the source-to-Python proof in Lean or peer reviewed the inequality. The lower bound uses normal Weil Q normalization; check against a second independent implementation before publication. Since the H symbol is even, the bathtub comparison is valid for complex f with asymmetric rho; do NOT silently assume rho is even. The n=5 signed autocorrelation charge is estimated by −ln5/√5, not the too-conservative −2ln5/√5. The upper frequency cutoff T* = π/(2w) has correct Fourier normalizations.

## Distinct formal-proof cross-check and new agenda

Original primary sources opened in this delta: https://leanprover-community.github.io/blog/posts/riemann-hypothesis/ (joint official 2026-11-21 certification), https://math.mit.edu/~drew/grh/ (MIT independent checks, arithmetic Robin/Lagarias consequences), https://mrubinst.github.io/grh-lean-verification/ (Waterloo independent full module and nanoda checks), https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/ (human working draft version2 dated 2026-11-22, 265p, explicitly says the main inequality M and thirteen other classical hypotheses are NOT proved outright in the readable draft, even though Lean full proof checks), and primary math articles Suzuki https://arxiv.org/html/2606.09096v4 and Zhu https://arxiv.org/html/2608.24827v2. Clay official https://www.claymath.org/millennium/riemann-hypothesis/ still marks RH 'Unsolved' at retrieval, distinct from Lean community full confidence and formal certification.

New conceptual consequence to audit: if accepted formal RH holds, Weil positivity Q>=0 on all compactly supported smooth f follows by established Weil criterion, *but not by our numerical scripts*. For each fixed L, Suzuki's compact H^log form-domain embedding plus the density O(T logT) of zeta zeros relative to exponential-type Fourier transforms plausibly yields strict positive λ(L)>0 (nonconstructive): if a ground vector had Q=0, approximation by smooth functions and positivity of every zero-side term would force Fourier transform to vanish at all critical ordinates; exponential-type Fourier transforms cannot have O(TlogT) zeros unless identically zero. Write this domain extension with full details, including multiplicities, before asserting as standalone lemma. The existing local collar margin remains a genuinely quantitative, independent claim, not derived from accepting formal RH.

Next: independent symbolic checking of the w24 certificate formulas and more aggressive width or asymmetry; audit the formal RH proof's exact `everyCharacter` top dependency and mathematical bridge, the Waterloo thirteen-claim outline, and any peer rebuttal with specific kernel counterexample.
