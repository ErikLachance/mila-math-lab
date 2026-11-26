# A Carleman obstruction at a spatial interface in the Weil form

**ML-RH-004.** Historical argument: 8 November 2026. Reconstruction and review: 26 November 2026. Not peer reviewed.

## Abstract

A narrow added spatial strip does not force the entire cross-interface L2 coupling of the Weil form to tend to zero. Its archimedean component has a scale-invariant Carleman singularity. We reconstruct the lower bound pi/2 for the supremum of the absolute mixed form on normalized smooth functions on opposite sides of a touching interface. This rules out a small-norm estimate for the full unweighted cross block, not the positivity of the Weil form.

## 1. Off-diagonal kernel

Fix b=0.8 and a positive strip width e. Write C=(-b,b), E=(-b-e,-b) union (b,b+e). Work with the geometric-side normalization in [Zhu, arXiv:2608.24827v2](https://arxiv.org/html/2608.24827v2), particularly equations (2),(3),(9) and the parity discussion in Section 6. Let B denote the polarized quadratic form, normalized so B(f,f)=Q(f). Consider real smooth functions with disjoint supports on either side of b.

Gauss's integral for the digamma function gives the archimedean multiplier H(t)=Re psi(1/4+it/2)-log pi. Inverting its cosine term off the diagonal gives the kernel

$$
K(s)=-\frac{\exp(-|s|/2)}{1-\exp(-2|s|)}.
$$

The constant and diagonal distribution terms contribute nothing between disjoint supports. For s>0 tending to zero, Taylor expansion gives K(s)=-1/(2s)-1/4+O(s). At an interface write x=b-r, y=b+t, with r,t>0. The leading cross kernel is therefore -1/[2(r+t)].

## 2. Carleman norm

Define C_0 on positive half-line functions by

$$
(C_0g)(r)=\int_0^\infty\frac{g(t)}{r+t}\,dt.
$$

The weighted Schur bound with weight r^(-1/2) gives ||C_0||<=pi, because integral_0^infty t^(-1/2)/(r+t) dt=pi r^(-1/2). For T>0 let f_T(r)=r^(-1/2)/sqrt(2T) on [exp(-T),exp(T)] and zero elsewhere. Its norm is one. The logarithmic change of variables gives

$$
\langle f_T,C_0 f_T\rangle=\int_0^{2T}\frac{1-s/(2T)}{\cosh(s/2)}\,ds\longrightarrow\pi.
$$

Dominated convergence proves the limit, and smooth compactly supported approximations yield the same supremum because C_0 is bounded. Thus its operator norm is exactly pi.

## 3. Scaling at the interface

For normalized smooth compactly supported F,G on (0,infty), let f_epsilon(x)=epsilon^(-1/2) F((b-x)/epsilon) on the core side and g_epsilon(y)=epsilon^(-1/2) G((y-b)/epsilon) on the strip side, zero elsewhere. For sufficiently small epsilon their supports are contained in C and E respectively. Their norms stay one. Substituting the scaled variables into the off-diagonal integral gives

$$
\lim_{\epsilon\to0}B_{\rm arch}(f_\epsilon,g_\epsilon)
=-\tfrac12\langle F,C_0G\rangle.
$$

Indeed the factor epsilon from the Jacobian and normalization cancels the inverse-distance singularity, while the bounded remainder tends to zero. The prime shifts have distances at least log 2, and are absent in this cross term once the supports are sufficiently close to the same interface. The pole is a finite-rank smooth-kernel contribution; each rescaled moment is O(sqrt(epsilon)), so its mixed term tends to zero.

Taking smooth approximations to the norm witnesses from section 2, then rescaling them inside an arbitrarily narrow but fixed strip, proves

$$
\sup_{\|f\|_2=\|g\|_2=1,\ f\in C_c^\infty(C),\ g\in C_c^\infty(E)}|B(f,g)|\ge \pi/2.
$$

If the full mixed block admits a bounded L2 realization, its operator norm is therefore at least pi/2 for every positive strip width. The proof needs only the supremum over smooth tests; it does not assert existence of that bounded realization.

## 4. What is ruled out, and what is not

A strategy that requires the full unweighted L2 mixed block to be o(1) as the strip shrinks cannot work in this spatial decomposition. The conclusion does not establish any negative direction of Q. In particular, the high-frequency diagonal energies of interface-concentrated functions need not remain small. A valid Schur-complement or coercivity method must retain the corresponding form-domain information and use estimates relative to the diagonal energies rather than only the unweighted mixed norm.

This obstruction is separate from the spectral projection argument of ML-RH-003: a spatial core/strip split is not the same as a spectral low/high-mode split. Nothing here rules out that latter strategy or proves or disproves RH.

## 5. Numerical illustration and sources

The companion script computes six floating-point approximations of the logarithmic Carleman witness integral and five near-interface kernel remainders. They illustrate convergence to pi and -1/4 respectively; they are not rigorous interval certificates and do not enter the analytic proof.

Source normalization and Gauss integral: Xuefeng Zhu, [Weil positivity in compact windows](https://arxiv.org/html/2608.24827v2), v2, 2 September 2026. Its claimed positivity certificate is not reproduced here. Historical source note dated 8 November 2026. The reconstructed proof is subject to independent review; no novelty claim is made.

**Reproduce the illustrations:** node experiments/frontier-20261126.mjs; [results](../results/frontier-20261126.json), key carleman. See [ML-RH-003](riemann-intervals.md).
