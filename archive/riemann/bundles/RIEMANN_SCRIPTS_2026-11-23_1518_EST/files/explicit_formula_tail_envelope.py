import mpmath as m, json, sympy as s, time
m.mp.dps=25
N=100
t0=time.monotonic()
zeros=[m.im(m.zetazero(k)) for k in range(1,N+1)]
C=2+m.euler-m.log(4*m.pi)
partial=sum(2/(m.mpf('.25')+t*t) for t in zeros)
tail=C-partial
assert tail>0
rows=[]
for n in [2,3,10,100,1000,10000]:
    x=m.mpf(n)
    S=m.mpf('0')
    for p in s.primerange(2,n+1):
        pk=p
        while pk<=n:
            S+=m.log(p)*(x/pk-1);pk*=p
    G=S-x*m.log(x)+(1+m.euler)*x
    T=1-m.log(1-x**(-2))/2-x*m.atanh(1/x)
    sumz=2*m.sqrt(x)*sum(m.cos(t*m.log(x))/(m.mpf('.25')+t*t) for t in zeros)
    estimate=m.log(2*m.pi)-T+sumz
    err=abs(G-estimate)
    bound=m.sqrt(x)*tail
    assert err<bound
    rows.append(dict(x=n,G=m.nstr(G,18),partial_reconstruction=m.nstr(estimate,18),abs_error=m.nstr(err,12),tail_bound=m.nstr(bound,12),fraction_of_bound=m.nstr(err/bound,12)))
data={'N':N,'C':m.nstr(C,25),'weight_partial':m.nstr(partial,25),'tail_weight_exact_identity_using_verified_zeros':m.nstr(tail,25),'elapsed_seconds':time.monotonic()-t0,'rows':rows,'note':'conditional on RH and properly certified first N zeros; actual numerics mpmath ordinates, not certified, so only falsification regression'}
with open('/mnt/data/riemann_run_20261123_1457/explicit_formula_tail_envelope.json','w') as f:json.dump(data,f,indent=2)
print(json.dumps(data,indent=2))
