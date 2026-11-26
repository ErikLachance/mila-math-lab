"""Independent exact Mobius/Mertens sieves; no external I/O."""
import math
import time
import json
import hashlib

N = 10_000_000
t0 = time.perf_counter()

# Encoding: 0 = zero, 1 = +1, 2 = -1.
# Method A: Eratosthenes primes, flip signs for each distinct prime,
# then set all multiples of a prime square to zero.
isprime = bytearray(b'\x01') * (N + 1)
isprime[0:2] = b'\x00\x00'
for p in range(2, math.isqrt(N) + 1):
    if isprime[p]:
        isprime[p*p::p] = bytes((N-p*p)//p + 1)
mu_a = bytearray(b'\x01') * (N + 1)
mu_a[0] = 0
flip = bytes([0, 2, 1] + list(range(3, 256)))
prime_count = 0
for p in range(2, N + 1):
    if isprime[p]:
        prime_count += 1
        mu_a[p::p] = mu_a[p::p].translate(flip)
        if p*p <= N:
            mu_a[p*p::p*p] = bytes(N//(p*p))
del isprime
t1 = time.perf_counter()

# Method B: Euler's linear sieve, each composite generated once.
# mu(i*p)=0 if p divides i; otherwise mu(i*p)=-mu(i).
mu_b = bytearray(N + 1)
mu_b[1] = 1
composite = bytearray(N + 1)
primes = []
for i in range(2, N + 1):
    if not composite[i]:
        primes.append(i)
        mu_b[i] = 2
    for p in primes:
        j = i*p
        if j > N:
            break
        composite[j] = 1
        if i % p == 0:
            mu_b[j] = 0
            break
        mu_b[j] = flip[mu_b[i]]
t2 = time.perf_counter()
if mu_a != mu_b or len(primes) != prime_count:
    raise ArithmeticError("Independent sieves disagree")
del composite, primes

# Exact summatory statistics and normalized extrema for n >= 1000.
values = (0, 1, -1)
checkpoints = {10**k for k in range(8)}
M = 0
min_m = max_m = 0
min_n = max_n = 1
best_abs, best_n = 0, 1000
samples = {}
for i in range(1, N + 1):
    M += values[mu_a[i]]
    if i in checkpoints:
        samples[str(i)] = M
    if M < min_m:
        min_m, min_n = M, i
    if M > max_m:
        max_m, max_n = M, i
    if i >= 1000 and M*M*best_n > best_abs*best_abs*i:
        best_abs, best_n = abs(M), i

# Independent trial division of deterministic sample points, including
# boundary points and prime squares. No random state or dependencies.
def trial_mu(n):
    sign = 1
    d = 2
    while d*d <= n:
        if n % d == 0:
            n //= d
            if n % d == 0:
                return 0
            sign = -sign
        d = 3 if d == 2 else d+2
    if n > 1:
        sign = -sign
    return sign

points = {1, 2, 3, 4, 6, 9, 16, 25, N-1, N}
points.update(i*i for i in range(2, 3163, 17))
x = 20261126
for _ in range(1024):
    x = (1664525*x + 1013904223) & 0xffffffff
    points.add(1 + x % N)
for n in sorted(points):
    if values[mu_a[n]] != trial_mu(n):
        raise ArithmeticError("Trial division mismatch at %d" % n)

# Dirichlet convolution mu*1=epsilon, summed up to k:
# sum mu(d)*floor(k/d)=1. Group equal quotients, use exact counts.
identities = {}
for k in (1, 10, 1000, 100000, N):
    total = 0
    lo = 1
    while lo <= k:
        q = k//lo
        hi = k//q
        total += q*(mu_a.count(1, lo, hi+1)-mu_a.count(2, lo, hi+1))
        lo = hi+1
    if total != 1:
        raise ArithmeticError("Dirichlet convolution mismatch at %d" % k)
    identities[str(k)] = total

pos, neg, zero = mu_a.count(1), mu_a.count(2), mu_a.count(0)-1
if pos+neg+zero != N or pos-neg != M:
    raise ArithmeticError("Count invariant mismatch")
t3 = time.perf_counter()
print(json.dumps({
    "N": N, "M_N": M, "M_checkpoints": samples,
    "prime_count": prime_count,
    "mu_counts": {"positive": pos, "negative": neg, "zero": zero},
    "M_min": [min_m, min_n], "M_max": [max_m, max_n],
    "max_abs_M_over_sqrt_n_from_1000": {"abs_M":best_abs,"n":best_n,"ratio":best_abs/math.sqrt(best_n)},
    "full_agreement": True, "compared_values": N,
    "trial_division_points":len(points), "dirichlet_identities": identities,
    "mu_encoding_sha256": hashlib.sha256(mu_a).hexdigest(),
    "seconds": {"eratosthenes":round(t1-t0,6),"euler":round(t2-t1,6),"checks_and_statistics":round(t3-t2,6),"total":round(t3-t0,6)},
    "cpu_threads_used_by_algorithm": 1,
    "scope": "finite exact integer calculation, not RH proof"
}, sort_keys=True))
