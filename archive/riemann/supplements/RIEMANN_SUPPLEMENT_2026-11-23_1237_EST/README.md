# Riemann Proof Watch — supplemental source-fidelity checkpoint: Jutila and exact inert-prime bridge

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_SUPPLEMENT_2026-11-23_1237_EST.md`. **Recorded time label:** 2026-11-23 12:37 EST (from the filename).

[Archive index](../../../README.md) · [Manifest](../../../manifest.json) · [Verification scope](../../../README.md#what-was-checked-during-import)


## NEW primary-source match: Jutila 1977 zero-density statement

Read Matti Jutila, **On Linnik's constant**, *Mathematica Scandinavica* 41 (1977), pp.45–62, DOI 10.7146/math.scand.a-11701, ORIGINAL journal PDF https://www.mscand.dk/article/download/11701/9717 . Inspected visually scanned PRINTED p.46 (PDF page index1), Theorem 1, lines (1.7)–(1.8). This resolves a specific attribution left `source match pending` in V17 of Jimmie Adriazola's external-input audit for the Alpöge–Claude RH formal archive (https://github.com/jimjamzola/RH-Alpoge-Reconstruction/blob/main/EXTERNAL_THEOREMS.md): for **4/5 <= alpha <=1, T>=1, epsilon>0**,

* For a **single fixed modulus q**, eq.(1.7) counts **all** Dirichlet characters modulo q: `N(alpha,T,q) <<_eps (q*T)^((2+eps)*(1-alpha))`.
* For moduli summed **q <= Q**, eq.(1.8) counts **PRIMITIVE** characters only: `N*(alpha,T,Q) <<_eps (Q^2*T)^((2+eps)*(1-alpha))`.

Both starred and unstarred definitions occur immediately above Theorem 1, on printed p.46. The bound's exponent, cutoff alpha, T>=1 and implied dependence on epsilon match the formula recorded in the reconstruction's V17. **However the actual Lean declaration signature or its caller's handling of imprimitive characters has not been read. Therefore this is a source-location and published-theorem verification ONLY, not yet a proof that the whole published theorem interface is correctly instantiated.** The other same-year Jutila work *Zero-density estimates for L-functions*, *Acta Arithmetica* 32(1977)55–62, is a distinct publication and must not be silently substituted for the verified Theorem1 eq.(1.8).

## NEW exact conductor-counting audit and adversarial transfer lemma

In modulus q, every Dirichlet character is induced uniquely from a primitive character whose conductor d divides q; missing Euler factors introduce no new zeros in the OPEN critical strip 0<Re(s)<1. Let a_d denote number of zeros for all primitive characters of conductor d in a chosen alpha>=4/5 zero-count rectangle. Then mathematically, as a finite integer identity:

`S_all(Q)=sum_{q<=Q} sum_{chi mod q} N(alpha,T,chi) = sum_{d<=Q} floor(Q/d)*a_d = sum_{k<=Q} A_prim(floor(Q/k))`

where `A_prim(U)=sum_{d<=U} a_d`. The same zero is repeated in induced imprimitive characters, even if missing Euler factors have no new interior zeros. This identity requires the usual zero multiplicities and no boundary zeros counted from the missing factors; the source rectangle alpha>=4/5 lies safely in Re(s)>0.

Independently computed exact primitive character counts `phi_star(d)=sum_{e|d}mobius(d/e)*phi(e)` and tested `sum_{d|q}phi_star(d)=phi(q)` for all q=1..500 using SymPy integers, all PASS. Example primitive chi modulo4 occurs as an induced character for **125 moduli** q<=500 (multiples of4), vs ONE conductor4 in the primitive zero-count sum. No claim chi4 actually has an off-line zero; multiplicity of the induced character is unconditional. Script `jutila_primitive_count_audit.py/.json`.

If the primitive theorem bounds `A_prim(U) <= C*(U^2*T)^a`, `a=(2+eps)(1-alpha)`, then this alone yields

`S_all(Q) <= C*(Q^2*T)^a * sum_{k<=Q} k^(−2a)`.

For `2a<1`, the last sum can grow as `Q^(1−2a)`, giving `O(Q*T^a)` rather than the primitive `O(Q^(2a)*T^a)`. For `2a=1` the loss is logarithmic, and `2a>1` it is bounded. At epsilon=1/10, exact exponent pairs (alpha,2a,loss) are (4/5,21/25,4/25), (9/10,21/50,29/50), (99/100,21/500,479/500). Exact artificial countermodel a_4=1, all other a_d=0: primitive aggregate A(Q)=1 but all-character aggregate S(Q)=floor(Q/4), linear in Q. This toy is an **exact countermodel to a careless inference from the primitive estimate**, NOT a claim actual chi4 has a zero, and NOT a contradiction of eq.(1.7), which separately handles a single fixed modulus. Script `jutila_induction_transfer.py/.json`.

**Highest-value open check:** read the precise Lean source declaration for `Jutila` or the nine `hostEx_of_zeroFreeRegion` inputs and determine which of (1.7) fixed-q all-characters and (1.8) summed primitive-characters it requires. If it uses (1.8), verify the primitive restriction or an explicit loss-proof for induction. The independent Lean formal certificate means no human source mismatch may be presumed to create a proof gap.

## NEW exact inert-prime arithmetic bridge, separate from the 11:10 q,d selector test

For prime d=3(mod4), primitive quadratic chi=Kronecker(-d, .), and `S(x)=sum_{n<=x} Lambda(n)*(x/n−1)`, `S_chi(x)=sum_{n<=x}Lambda(n)*chi(n)*(x/n−1)`, write x=a/w, a>0,w>0. Then coefficient by coefficient in `log p`,

`w*(S(x)-S_chi(x)) = 2*sum_{p inert} sum_{k odd>=1} log(p)*max(a/p^k−w,0) + log(d)*sum_{k>=1}max(a/d^k−w,0)`.

Proof: for each p^k, coefficient is `(1−chi(p)^k)`; it is zero for split primes, 2 for inert p and odd k, zero for inert even k, and 1 for ramified p=d at every k. At p=2 one must use **Kronecker** `(-d/2)`, not an undefined Legendre symbol `(2/d)` without reciprocity context. Tested d=3,7,11,19,31 and 4 distinct pairs (a,w), 20 cases, with exact `Fraction` coefficients of each independent logarithm `log p`; all PASS. Initial script falsely failed because a default dictionary stored coefficient 0 for split primes, while RHS omitted that key; normalized both dictionaries to omit zeros and reran successfully. This is a **data-structure equivalence bug**, not a mathematical counterexample. Source normalization `G(x)` and nonprincipal `G_chi(x)` has separate linear/constant terms, so this proof only checks the **arithmetic prime-power part** of the exact inert identity in Stage2, not full main inequality (M), no RH proof. Script `inert_prime_hinge_identity.py/.json`.

## Additional source scrutiny / no unproved inference

Primary author-readable working guide v2 Nov22 https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf says on first page NONE of H0–H12 is proved outright there; all are formally established elsewhere in verified Lean artifact, and the human source remains conditional. An independent human reconstruction `PROOF_DEPENDENCY_MAP.md` https://github.com/jimjamzola/RH-Alpoge-Reconstruction/blob/main/PROOF_DEPENDENCY_MAP.md maps stages 1→12 and derives an inert character prime sum exactly on Stage2, then theta-lift/automorphic/Galois machinery stages3–9, positive prime sum stage10, zero-free half-plane stage11. It describes a fixed positive character combination G_Xi bounded on arbitrarily large windows. One must not casually swap `for every window exists a potentially different Xi` with `exists a fixed Xi for arbitrarily many windows`: such a quantifier swap is invalid absent a structural reduction. The dependence map is abridged, so no flaw inferred; verify the exact source hypothesis before making a claim. Likewise, a bound for a **positive sum of components** cannot be replaced with a bound for each component without the special analytic Landau criterion. The source expressly uses that criterion; do not substitute naive cancellation heuristics.

## Next checks

Companion files recorded: all FOUR new files `jutila_primitive_count_audit.py/.json`, `jutila_induction_transfer.py/.json`, `inert_prime_hinge_identity.py/.json`. Continue source-fidelity route: inspect exact Jutila primitive use and the two exception-window clauses of Gallagher 1970; avoid recycling mesh/G estimates, 16D Fourier or prime selector toys. No independent RH proof is produced.
