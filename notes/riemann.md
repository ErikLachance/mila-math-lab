# Riemann — reproducible Möbius and Mertens computations

**Date:** 2026-11-26. **Status:** finite exact arithmetic; no new global proof.

The Möbius function mu(n) is zero for n divisible by a square of a prime and otherwise equals (-1)^k for k distinct prime factors. The Mertens function M(N)=sum_{n<=N} mu(n) is related to analytic estimates in prime number theory. Finite computations do not establish the asymptotic estimates required by RH.

## Recorded terrain runs

Two local CPU compute receipts were retrieved on 26 November 2026. These aggregates omit private identifiers and paths.

| N | M(N) | Primes <= N | mu=+1 | mu=-1 | mu=0 | Recorded algorithm wall time |
|---:|---:|---:|---:|---:|---:|---:|
| 10,000,000 | 1,037 | 664,579 | 3,040,164 | 3,039,127 | 3,920,709 | 7.655572 s |
| 100,000,000 | 1,928 | 5,761,455 | 30,397,311 | 30,395,383 | 39,207,306 | 6.099763 s |

At 10 million, two independent sieves (prime-factor sign reversal with square marking, and Euler's linear sieve) agreed on every value, with 1,219 independent trial-division checks and five Dirichlet convolution checks. The encoded array SHA-256, with index 0 included and encoding zero=0, positive=1, negative=2, was abc95800f8c11e409fff3cb15d05bdfa7d5c0fc7c2aef70bd53c341033feaff4.

At 100 million, ten workers performed a segmented sieve; an independent linear sieve matched the first million values' digest, and independent summatory recurrence checks matched all ten segment endpoints. The observed minimum was -3,448 at 76,015,339 and maximum 3,290 at 92,418,127. These extrema are recorded outputs, not independently recomputed by the public endpoint verifier. The two runs differ in methods and validation coverage; wall times are not a controlled speedup comparison.

## Independent public reproduction

The identity sum_{k=1}^N M(floor(N/k))=1 follows by summing mu*1=epsilon. Hence

$$ M(N)=1-\sum_{k=2}^{N} M(\lfloor N/k\rfloor). $$

Group consecutive k with equal quotient, memoize values and compute a base interval by the linear sieve. The public reproduction checks all reported 10-million segment endpoints and smaller powers of 10. It reproduces M(10^8)=1928. It does not check all 100 million individual Möbius values or the extrema.

## Historical analytical work

Earlier checkpoints discuss prolate spectral subspaces, constrained endpoint jets and moments, and quantitative leakage. They record a gap between finite leakage estimates and the needed coercivity or limiting argument. This material is not released as a proved theorem: normalization, uniformity, domains and the passage to an infinite-dimensional form need auditing. See the [Clay Mathematics Institute's Riemann hypothesis page](https://www.claymath.org/millennium/riemann-hypothesis/). No resolution of RH is claimed.
