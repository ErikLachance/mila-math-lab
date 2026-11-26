"""Mertens to 100 million: parallel segmented exact sieve + independent
linear sieve and summatory Dirichlet inversion. Offline, no external I/O."""
from array import array
from functools import lru_cache
import math
import multiprocessing as mp
import hashlib
import json
import time
import traceback

N = 100_000_000
BLOCK = 10_000_000
BASE = 1_000_000
WORKERS = N//BLOCK
FLIP = bytes([0, 2, 1] + list(range(3, 256)))
VALUES = (0, 1, -1)
PRIMES = None

def segment(lo, hi, conn):
    wall = time.perf_counter()
    cpu = time.process_time()
    try:
        length = hi-lo+1
        mu = bytearray(b'\x01')*length
        for p in PRIMES:
            if p > hi:
                break
            first = (-lo)%p
            if first >= length:
                continue
            if first+p >= length:
                mu[first] = FLIP[mu[first]]
            else:
                mu[first::p] = mu[first::p].translate(FLIP)
            pp = p*p
            if pp <= hi:
                firstsq = (-lo)%pp
                if firstsq < length:
                    mu[firstsq::pp] = bytes((length-1-firstsq)//pp+1)
        pos, neg, zero = mu.count(1), mu.count(2), mu.count(0)
        m = 0
        mn = mx = 0
        imin = imax = lo-1
        for j, b in enumerate(mu, lo):
            m += VALUES[b]
            if m < mn:
                mn, imin = m, j
            if m > mx:
                mx, imax = m, j
        assert pos+neg+zero == length and m == pos-neg
        conn.send({"lo":lo,"hi":hi,"sum":m,"counts":[pos,neg,zero],
            "min":[mn,imin],"max":[mx,imax],
            "digest":hashlib.sha256(mu).hexdigest(),
            "first_million_digest":hashlib.sha256(mu[:BASE]).hexdigest() if lo==1 else None,
            "wall_s":round(time.perf_counter()-wall,6),
            "cpu_s":round(time.process_time()-cpu,6)})
    except Exception:
        conn.send({"error":traceback.format_exc(),"lo":lo,"hi":hi})
    finally:
        conn.close()

def linear_base():
    comp = bytearray(BASE+1)
    mu = bytearray(BASE+1)
    mu[1]=1
    ps=[]
    for i in range(2, BASE+1):
        if not comp[i]:
            ps.append(i); mu[i]=2
        for p in ps:
            j=i*p
            if j>BASE: break
            comp[j]=1
            if i%p==0: break
            mu[j]=FLIP[mu[i]]
    prefix=array('i',[0])*(BASE+1)
    m=0
    for i in range(1,BASE+1):
        m+=VALUES[mu[i]]
        prefix[i]=m
    return prefix, hashlib.sha256(mu[1:]).hexdigest(), len(ps)

def main():
    global PRIMES
    t0=time.perf_counter()
    pcpu=time.process_time()
    prime=bytearray(b'\x01')*(N+1)
    prime[:2]=b'\x00\x00'
    for p in range(2,math.isqrt(N)+1):
        if prime[p]:
            prime[p*p::p]=bytes((N-p*p)//p+1)
    PRIMES=array('I',(i for i,v in enumerate(prime) if v))
    del prime
    t1=time.perf_counter()

    # Fork shares immutable compact prime array. Pipes avoid large
    # result transfers and semaphore-dependent process pools.
    ctx=mp.get_context('fork')
    jobs=[]
    for lo in range(1,N+1,BLOCK):
        recv, send=ctx.Pipe(duplex=False)
        p=ctx.Process(target=segment,args=(lo,min(lo+BLOCK-1,N),send))
        p.start()
        send.close()
        jobs.append((p,recv))
    segments=[]
    for p,recv in jobs:
        result=recv.recv()
        recv.close()
        p.join()
        if p.exitcode!=0 or "error" in result:
            raise RuntimeError(str(result))
        segments.append(result)
    t2=time.perf_counter()

    # Independent verification: summing mu*1=epsilon gives
    # M(x)=1-sum_{k=2}^x M(floor(x/k)). Group equal quotients.
    prefix, base_digest, base_prime_count=linear_base()
    @lru_cache(maxsize=None)
    def mertens(x):
        if x<=BASE:
            return prefix[x]
        total=1
        l=2
        while l<=x:
            q=x//l
            r=x//q
            total-=(r-l+1)*mertens(q)
            l=r+1
        return total

    assert base_digest==segments[0]["first_million_digest"]
    assert base_prime_count==78498 and len(PRIMES)==5761455
    counts=[0,0,0]
    M=0; min_m=max_m=0; min_n=max_n=0
    checks={}
    for s in sorted(segments,key=lambda r:r["lo"]):
        lm,li=s["min"]; hm,hi=s["max"]
        if M+lm<min_m: min_m,min_n=M+lm,li
        if M+hm>max_m: max_m,max_n=M+hm,hi
        M+=s["sum"]
        for i,v in enumerate(s["counts"]): counts[i]+=v
        independent=mertens(s["hi"])
        if M!=independent: raise ArithmeticError("M mismatch at "+str(s["hi"]))
        checks[str(s["hi"])]=M
    assert checks["10000000"]==1037 and prefix[BASE]==212
    assert sum(counts)==N and counts[0]-counts[1]==M
    t3=time.perf_counter()
    print(json.dumps({"N":N,"M_N":M,"checkpoints":checks,"prime_count":len(PRIMES),
        "mu_counts":dict(zip(("positive","negative","zero"),counts)),
        "M_min":[min_m,min_n],"M_max":[max_m,max_n],
        "parallel_workers":WORKERS,"worker_cpu_s":round(sum(s["cpu_s"] for s in segments),6),
        "parent_cpu_s":round(time.process_time()-pcpu,6),
        "seconds":{"prime_sieve":round(t1-t0,6),"parallel_segments":round(t2-t1,6),
            "independent_checks":round(t3-t2,6),"total":round(t3-t0,6)},
        "independent_segment_boundary_checks":len(checks),
        "independent_base_digest_matches":True,"independent_base_values":BASE,
        "base_digest":base_digest,"recurrence_cache":mertens.cache_info()._asdict(),
        "segments":segments,"scope":"finite exact arithmetic; not a proof of RH"},
        sort_keys=True))

if __name__=="__main__":
    main()
