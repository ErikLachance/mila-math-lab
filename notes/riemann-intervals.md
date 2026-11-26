# Rational enclosures for a compact-window Weil-form estimate

**Research note ML-RH-003.** Historical argument: 8 November 2026. Independent reconstruction: 26 November 2026. Not peer reviewed. This is a bound on negative directions in one fixed window, not a proof of positivity on the entire window or of RH.

## Abstract

For L=0.81 and frequency cutoff T=596, we reconstruct the rational bounds underlying the codimension-361 estimate in ML-RH-002. Unlike the previous edition, which only checked the final arithmetic, the new verifier constructs enclosures for the prime contribution, archimedean constants, trace, trace variance and negative pole tail. All decisive comparisons use exact integer fractions. The argument uses the Weil normalization and envelope/parity formulas in Zhu's preprint, equations (2)–(3), Lemmas 3.1 and 6.1; the overall note awaits independent mathematical review.

## 1. Symbol and projection

Set I=(-L,L). For smooth admissible f supported in I, use the Fourier transform F(t)=integral f(x)e^(itx) dx. The cited geometric-side Weil form has an even multiplier H(t)-P_L(t) with H(t)=Re psi(1/4+it/2)-log pi and prime comb P_L. The pole contribution is bounded below by -2|<f,h>|^2, where h(x)=sinh(x/2) on I. For complex f the same bound follows from the real/imaginary and even/odd decompositions.

The only prime powers below exp(2L) are 2,3,4,5. Their total comb amplitude is

$$ A_L=\sqrt{2}\log2+2\log3/\sqrt3+\log2+2\log5/\sqrt5.$$

The digamma series gives H(t)>=H(0)=-gamma-pi/2-3log2-log pi. The high-frequency lower bound follows from the cited envelope. Define M=A_L-H(0), beta=log(T/(2pi))-1/T-A_L. Thus the multiplier is bounded below by -M everywhere and by beta for |t|>=T.

Let K_T be the positive time-band-limiting contraction on L^2(I) with kernel sin(T(x-y))/(pi(x-y)). Parseval then yields

$$ Q(f)\ge\beta\|f\|^2-(\beta+M)\langle f,K_T f\rangle-2|\langle f,h\rangle|^2.$$

## 2. Trace variance bound

Write a=2L and X=aT. Direct integration of the kernel gives trace K_T=X/pi and

$$ V=\operatorname{tr}(K_T-K_T^2)
=\frac2{\pi^2}\left[\int_0^a\frac{\sin^2(Ts)}s\,ds
+a\int_a^\infty\frac{\sin^2(Ts)}{s^2}\,ds\right].$$

The first integral is (gamma+log(2X)-Ci(2X))/2. Integration by parts bounds |Ci(2X)| by 1/X. Splitting sin^2 into constant and oscillatory terms and integrating the latter by parts gives the second integral, including its factor a, at most 1/2+1/(2X). Hence

$$ V\le(\gamma+\log(2X)+1+2/X)/\pi^2.$$

For eta=17/1000 and each eigenvalue lambda>=eta, 1<=lambda+lambda(1-lambda)/eta. The number of such eigenvalues is therefore at most trace K_T+V/eta, strictly less than 362 by the enclosed constants below. On the complement S of the first 361 modes, <f,K_T f><=eta||f||^2.

## 3. Negative pole tail

If P_S is the orthogonal projection to S, the spectral theorem yields ||P_S h||^2<=(1-eta)^(-1)<h,(1-K_T)h>. Write A=sinh(L/2), B=cosh(L/2)/2. The Fourier transform of h on I is, up to its harmless sign convention, 2i[B sin(Lt)-t A cos(Lt)]/(t^2+1/4). Bounding the denominator below by t^4 after squaring, using 2|sin cos|<=1 and integrating the cos^2 term by parts gives

$$ E_{\rm hi}=\langle h,(1-K_T)h\rangle
\le\frac4\pi\left[A^2\left(\frac1{2T}+\frac1{2LT^2}\right)
+\frac{AB}{2T^2}+\frac{B^2}{3T^3}\right].$$

Consequently on S the coefficient lower bound for Q is (1-eta)beta-eta M-2E_hi/(1-eta).

## 4. Certified numerical comparisons

The new script uses Machin's formula and alternating arctangent series for pi; positive atanh log series with a geometric remainder and binary range reduction for logarithms; integer square-root brackets; the harmonic Euler–Maclaurin bound

$$H_n-\log n-\frac1{2n}<\gamma<H_n-\log n-\frac1{2n}+\frac1{12n^2},$$

with n=512; and positive Taylor series with geometric tails for sinh and cosh. Each comparison is made on reduced rational numbers using BigInt. Decimal displays below are rounded outward and are not the inputs to the decisive tests.

| Quantity | Certified bound (conservative) |
|---|---:|
| beta | > 0.16918 |
| M | < 9.75369 |
| trace K_T | < 307.34 |
| V | < 0.928 |
| E_hi | < 0.000186 |

The resulting index upper bound is strictly less than 307639/850=361.928235294..., so the negative index is at most 361. The lower coefficient on S is strictly greater than 11085943/98300000000=0.000112776632..., hence greater than 10^-4.

This is a reconstruction of the previously recorded fixed-window argument and numerical premises, not a certificate for the full exceptional block. It uses the cited explicit-formula conventions. The remaining directions and their coupling to the complement must still be controlled, and a single fixed L cannot establish RH, which requires positivity across all admissible supports.

## References and reproduction

Xuefeng Zhu, [Weil positivity in compact windows: a finite reduction, certified two-sided bounds, and a Landau-Widom decay law](https://arxiv.org/html/2608.24827v2), v2, 2026, especially equations (2)–(3), Lemma 3.1 and Lemma 6.1. Its claimed positivity for L=0.8 is not reproduced here. H. J. Landau and H. Widom, [Eigenvalue distribution of time and frequency limiting](https://doi.org/10.1016/0022-247X(80)90241-3), 1980, for time-band-limiting context.

Run node experiments/certificates-20261126.mjs. [Exact output](../results/certificates-20261126.json), key riemann_constants. See [ML-RH-002](riemann-advanced-20261108.md) for the earlier stage. Independent critique of the analytic inequalities and domain assumptions is invited.
