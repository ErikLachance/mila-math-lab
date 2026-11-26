# Riemann Proof Watch — additional append-only checkpoint, 2026-11-23 14:42 EST (America/New_York)

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_SUPPLEMENT_2026-11-23_1442_EST.md`. **Recorded time label:** 2026-11-23 14:42 EST (from the filename).

[Archive index](../../../README.md) · [Manifest](../../../manifest.json) · [Verification scope](../../../README.md#what-was-checked-during-import)


## New rigorous source-fidelity refinement: exact extremal sign characters in the RIGHT odd quadratic family

A previous pass of this same run constructed sign-prescribed *even* quadratic Dirichlet characters `chi_ell=(./ell)` with `ell = 1 mod 4` and thereby showed a uniform-conductor extreme range, but the actual Michael Rubinstein/Alpöge human guide at https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf and independent November-23 225-page manuscript (https://github.com/jimjamzola/RH-Alpoge-Reconstruction/blob/main/manuscript/sec12_loss.tex) use the **odd** real quadratic `chi_d=chi_{-d}` with `d` a prime `3 mod 4`. Simply identifying the two families would be a source-fidelity mistake. We repaired the construction **within precisely the correct odd family**:

Let y>=3, q a fixed auxiliary prime (take q=7 in experiments), and P_y the primes p<=y. For ANY prescribed signs epsilon_p in {+1,-1}, there exist INFINITELY MANY prime discriminant parameters d>y with d=3 mod 4, such that the primitive odd Dirichlet character chi_{-d} satisfies `chi_{-d}(p)=epsilon_p` for every p in P_y. Proof: at p=2, Kronecker `(-d/2)=+1` if d=7 mod 8 and -1 if d=3 mod 8. For each odd p choose any nonzero residue d mod p with `(-d/p)=epsilon_p`, possible because exactly half of nonzero residues have either sign. CRT combines these with the residue mod 8 into one reduced congruence class d=a mod N, `N=8 prod_{odd p<=y} p`, gcd(a,N)=1. Dirichlet's theorem produces infinitely many primes d in the class. d=3 or 7 mod8 ensures d=3 mod4, so -d is a negative fundamental discriminant and chi_{-d} is a primitive ODD real character. Every chosen d>y avoids the `p=d` conductor-zero exception. This is a general existence theorem requiring only CRT, Dirichlet primes in progressions, and the standard Kronecker symbol; no RH assumption.

Define the actual SOURCE-SCOPE single-weight signed-prime sum, with arithmetic exclusions p=2 and p=q (also p=d, automatically outside y), for a positive scale a and y=a/w:

`P_{chi,q}(y)/a = sum_{p^k<y; p odd, p!=q} (1-chi_{-d}(p)^k) log(p) * (1/p^k-1/y)`.

Since chi_{-d}(p)=+1 gives ZERO for all powers, while chi=-1 gives coefficient2 for odd k and0 for even k, for every such odd quadratic chi and every finite y:

`0 <= P_{chi,q}(y)/a <= 2 sum_{p^k<y; p odd,p!=q,k odd} log(p)(1/p^k-1/y)`.

***Both endpoints are SHARP*** for infinitely many d>y with d=3 mod4, by prescribing all signs +1 or all signs -1 for the finite set of primes up to y. The source's actual cell-indexed varying weights and consistency constraints are more difficult; this lemma is only for a *single common positive cell weight* and free choice of conductor, not for the original final theta-lift or H12 conditions.

## New exact computational falsification tests

Executed Python/SymPy Kronecker symbol, CRT, primality and mpmath 60-digit weighted prime-power sums, script `riemann_20261123_1441_odd_quadratic_extremes.py` and JSON report (new append-only companion ZIP). For y=10,30,100 constructed positive-pattern and negative-pattern primes d as follows:

- y=10: d+=311, d-=547; exact min0; max 0.834573317198604597571266...
- y=30: d+=10792179191, d-=238929233467; exact min0; max 2.03295976336352551149119...
- y=100: d+=60765662588513235425022835652976245831, d-=77952153794507619893681285262321432427; exact min0; max 3.92744002202365447251798...

Every prime d independently checked prime, congruent3 mod4, greater than y, satisfying *every prescribed symbol*, and each direct prime-power sum agrees with its independently constructed extremal formula to <1e-55 at 60 digits. The infinitely-many proof is number-theoretic, not inferred from the finite computations. This new pass corrects the parity/conductor scope of the earlier same-run source comparison; earlier even-character examples remain mathematically valid but not as source-faithful.

## Adversarial limitations, next experiments

The sign prescriptions may force d extremely large relative to y, so this does **not** refute conductor-bounded estimates for the H12 choice, nor show any mistake in a formally checked Lean proof. The main term in (M) includes conductor-dependent `L'/L(1,chi_{-d})`; changing chi can change this constant, so differing prime sums do NOT by themselves contradict a properly conductor-uniform expansion with correct c_chi. This is a sharp finite-window edge-case and a needed quantifier guard, not RH proof/disproof or mathematical priority claim. Existing user's signed Weil collar and 16D Fourier modes still cannot yield whole-window positivity due missing mixed/orthogonal-tail estimates; don't reattempt naive float64 eigensign extrapolation.

Sources actually used this continuation: November-22 Waterloo explanatory paper URL above; exact `sec12_loss.tex` GitHub source (read from live repository, SHA `5d1a0cec6eb545abd9fe9468f3d58ef4aa7b89e6`); mathematical facts CRT, Dirichlet theorem and Kronecker reciprocity. The actual Lean proof has been certified by external checkers, but no independent Lean compilation done here.

Next: test source's *explicit d size conditions and H12 selection uniformity*: identify whether d is polynomial/exponential in x, which can exclude the sign-adversarial CRT family; track uniform dependence on conductor in any hypothesized PNT error. If source parameters are unavailable, audit a distinct published/theoretic ingredient instead.
