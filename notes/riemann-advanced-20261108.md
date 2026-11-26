# Riemann — a compact-window spectral candidate: codimension 361

Historical checkpoint: 8 November 2026. Public arithmetic recheck: 26 November 2026. **Status: analytic candidate under audit.** The numerical comparisons below have been independently reproduced with exact rational arithmetic. The original analytic interval certificate and all normalization premises have not been recovered or independently checked here.

The historical argument studies the Weil form Q on complex admissible smooth compactly supported functions on I=(-L,L), L=81/100, using the conventions recorded from [Zhu, arXiv:2608.24827v2](https://arxiv.org/abs/2608.24827v2). It takes the Slepian operator K_T with T=596 and kernel sin(T(x-y))/(pi(x-y)), and eta=17/1000. The intended conclusion is positivity on the complement of the first 361 eigenmodes. It would bound the negative index on one fixed window; it would not prove RH.

## Recorded analytic premises

The historical note states these strict bounds:

- trace(K_T)<307.34 and trace(K_T(1-K_T))<0.928;
- beta>0.16918, M<9.75369 for the high/low frequency estimates of the form without the negative pole;
- E_hi=<h,(1-K_T)h><0.000186, with h=sinh(x/2) on I.

The trace bound and variance imply the number N_eta of eigenvalues at least eta is at most trace(K_T)+trace(K_T(1-K_T))/eta, since 1<=lambda+lambda(1-lambda)/eta when lambda>=eta. In the orthogonal complement of the first 361 eigenmodes, the spectral projection P then gives ||Ph||^2<=E_hi/(1-eta). Assuming the recorded decomposition of Q, including the negative pole term -2|<f,h>|^2, one obtains

$$ Q(f)\ge ((1-\eta)\beta-\eta M-2E_{hi}/(1-\eta))\,\|f\|^2. $$

The checkpoint gives a Fourier-tail estimate for h via explicit integration and an upper bound on the oscillatory cos^2 integral. That analytic step and the bounds above still require the original rigorous interval computations or an independent reconstruction.

## What was rechecked

Using only exact fractions, the current public verifier obtains

- trace+variance/eta < 307639/850 = approximately 361.928235294 < 362;
- net lower margin > 11085943/98300000000 = approximately 0.000112776633 > 1/10000.

Thus **if the recorded analytic premises hold**, the claimed codimension-361 estimate follows with the indicated positive margin. The arithmetic recheck alone does not certify the premises, the exceptional block, the infinite-dimensional form domain, or positivity for all windows. No negative direction or counterexample to RH has been found by this test.

## Remaining scientific tasks

Recover or reconstruct certified bounds for the trace, variance, archimedean term, prime contributions and Fourier tail; audit the source normalization and the form domain. Then address the exceptional 361-dimensional block and its coupling to the complement, without assuming the coupling is small. The historical work also explores prolate leakage and moment constraints; none resolves the global positivity problem. See the [Clay Mathematics Institute RH page](https://www.claymath.org/millennium/riemann-hypothesis/).

Reproduce the final rational arithmetic with node experiments/recheck-historical.mjs. This is not a full spectral or RH certificate.
