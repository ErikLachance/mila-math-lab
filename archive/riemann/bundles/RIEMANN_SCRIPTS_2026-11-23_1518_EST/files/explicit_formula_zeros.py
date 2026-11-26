import mpmath as m, json, time, sympy as s
m.mp.dps=25
start=time.monotonic()
N=200
z=[m.im(m.zetazero(i)) for i in range(1,N+1)]
xt=[m.mpf(n) for n in [2,3,10,100,1000,10000]]
def psi_sum(x):
    x=int(x)
    u=0
    for p in s.primerange(2,x+1):
        k=p
        while k<=x:
            u+=m.log(p)*(m.mpf(x)/k-1)
            k*=p
    return u
rows=[]
for x in xt:
    gv=psi_sum(x)-x*m.log(x)+(1+m.euler)*x
    T=1-m.log(1-x**(-2))/2-x*m.atanh(1/x)
    cs=[m.mpf(2)*m.sqrt(x)*sum(m.cos(t*m.log(x))/(m.mpf('.25')+t*t) for t in z[:k]) for k in [20,50,100,200]]
    reconstruction=[v+m.log(2*m.pi)-T for v in cs]
    rows.append({'x':int(x),'exact_G':m.nstr(gv,30),'T':m.nstr(T,25),'zero_partial_recon':[m.nstr(v,25) for v in reconstruction],'abs_error_200':m.nstr(abs(reconstruction[-1]-gv),12)})
res={'N':N,'last_zero_ordinate':m.nstr(z[-1],20),'seconds':time.monotonic()-start,'rows':rows}
with open('/mnt/data/riemann_run_20261123_1457/explicit_formula_zeros.json','w') as f:json.dump(res,f,indent=2)
print(json.dumps(res,indent=2))
