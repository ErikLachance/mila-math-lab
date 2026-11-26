"""Independent reproducibility checks. Python 3.10+, standard library only."""
import argparse
import hashlib
import itertools
import json
import math
import random
import struct
from array import array
from collections import Counter
from fractions import Fraction
from functools import lru_cache


def sat_check():
    # Literal i denotes bit i-1; positive clauses have ordinary Boolean semantics.
    clauses = [(i, i + 1, -(i + 2)) for i in range(1, 17)]
    def literal(x, l):
        return bool(x & (1 << (abs(l) - 1))) == (l > 0)
    values = bytes(all(any(literal(x, l) for l in clause) for clause in clauses)
                   for x in range(1 << 18))
    compact = bytes(((x | (x >> 1) | ~(x >> 2)) & 65535) == 65535
                    for x in range(1 << 18))
    assert values == compact and sum(values) == 10945
    uint32_digest = hashlib.sha256(b"".join(struct.pack("<I", v) for v in values)).hexdigest()
    assert uint32_digest == "5af5b258801a1138709617d3dceb6c4a669ea2b1139f4fea366e7f4b2259657d"
    return {"variables": 18, "clauses": 16, "assignments": len(values),
            "satisfying": sum(values), "unsatisfying": len(values)-sum(values),
            "boolean_byte_sha256": hashlib.sha256(values).hexdigest(),
            "uint32_le_sha256": uint32_digest}


def independent_sets_check():
    rng = random.Random(20261126)
    tested = 0
    fib = [0, 1]
    for _ in range(15):
        fib.append(sum(fib[-2:]))
    for n in range(2, 13):
        edges = list(itertools.combinations(range(n), 2))
        cases = [(edges, n+1), ([(i,i+1) for i in range(n-1)], fib[n+2]),
                 ([(0,i) for i in range(1,n)], 2**(n-1)+1)]
        cases += [([e for e in edges if rng.randrange(3)==0], None) for _ in range(15)]
        for graph, expected in cases:
            masks = [(1 << u)|(1 << v) for u,v in graph]
            count1 = sum(all(x & e != e for e in masks) for x in range(1 << n))
            count2 = 0
            for bits in itertools.product((False,True), repeat=n):
                if all(not bits[u] or not bits[v] for u,v in graph):
                    count2 += 1
            assert count1 == count2 and count1 > 0
            if expected is not None:
                assert count1 == expected
            tested += 1
    return {"graphs": tested, "all_agree": True, "seed": 20261126,
            "scope": "new deterministic replication, not the historical random sample"}


def beal_check():
    def signatures(threshold):
        out=[]
        for x in range(3, int(3/threshold)+1):
            for y in range(x, int(2/(threshold-Fraction(1,x)))+1):
                rem=threshold-Fraction(1,x)-Fraction(1,y)
                if rem <= 0:
                    raise ValueError("enumeration threshold too small")
                for z in range(y, int(1/rem)+1):
                    assert Fraction(1,x)+Fraction(1,y)+Fraction(1,z)>=threshold
                    out.append((x,y,z))
        return out
    a=signatures(Fraction(71,105)); b=signatures(Fraction(89,132))
    assert len(a)==115 and len(b)==143
    assert Counter((x,y) for x,y,z in a)=={(3,3):103,(3,4):7,(3,5):3,(4,4):2}
    # Fixed base regression; the general argument is in the accompanying note.
    for base,target in [(3,5),(5,3)]:
        lhs={target**k for k in range(3,60)}
        assert not any(2**m+base**n in lhs for m in range(3,60) for n in range(3,60))
    c=23**5; radical=2*3*109*23
    assert 2+109*3**10==c and c**71>radical**105
    return {"threshold_71_105_count":len(a),"threshold_89_132_count":len(b),
            "fixed_base_exponents":[3,59],"fixed_base_matches":0,
            "abc_obstruction":{"c":c,"radical":radical,"exact_inequality":True}}


def mertens_check(n=100_000_000):
    # Euler's linear sieve on a base interval, then exact quotient grouping.
    base=min(n,1_000_000)
    mu=array('b',[0])*(base+1); mu[1]=1
    composite=bytearray(base+1); primes=[]
    for i in range(2,base+1):
        if not composite[i]:
            primes.append(i); mu[i]=-1
        for p in primes:
            j=i*p
            if j>base: break
            composite[j]=1
            if i%p==0: break
            mu[j]=-mu[i]
    prefix=array('i',[0])*(base+1)
    for i in range(1,base+1): prefix[i]=prefix[i-1]+mu[i]
    @lru_cache(maxsize=None)
    def M(x):
        if x<=base: return prefix[x]
        result=1; left=2
        while left<=x:
            q=x//left; right=x//q
            result-=(right-left+1)*M(q); left=right+1
        return result
    expected={1:1,10:-1,100:1,1000:2,10000:-23,100000:-48,
              1000000:212,10000000:1037,20000000:-953,30000000:-1157,
              40000000:-333,50000000:-908,60000000:1267,70000000:-1270,
              80000000:1088,90000000:2050,100000000:1928}
    checks={str(k):M(k) for k in expected if k<=n}
    assert all(v==expected[int(k)] for k,v in checks.items())
    return {"base":base,"N":n,"M_N":M(n),"checkpoints":checks,
            "scope":"endpoint verification, not a pointwise independent sieve through N"}


if __name__ == '__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--limit',type=int,default=100_000_000)
    args=p.parse_args()
    if not 1<=args.limit<=100_000_000: p.error('limit must be in 1..100000000')
    print(json.dumps({"sat":sat_check(),"independent_sets":independent_sets_check(),
                      "beal":beal_check(),"mertens":mertens_check(args.limit)},indent=2,sort_keys=True))
