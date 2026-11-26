from fractions import Fraction
from math import factorial
import time,json,sys
sys.set_int_max_str_digits(100000)
start=time.perf_counter()
K=486
c=[Fraction(1)]
sq=[Fraction(1)]
for k in range(1,K+1):
    w=sum((sq[i]*c[k-1-i] for i in range(k)),Fraction(0))
    ck=Fraction(-2,4*k*(4*k+1))*w
    c.append(ck)
    # Use symmetric summation
    sqk=sum((2*c[i]*c[k-i] for i in range((k+1)//2)),Fraction(0))
    if k%2==0: sqk+=c[k//2]**2
    sq.append(sqk)
    if k%100==0:
        print('progress',k,round(time.perf_counter()-start,2),'s',flush=True)
n=1945
A=c[-1]*factorial(n)
assert A.denominator==1
v3=0; z=A.numerator
while z%3==0:z//=3;v3+=1
v7=0;z=A.numerator
while z%7==0:z//=7;v7+=1
r={'n':n,'A_n_integer':True,'digits':len(str(abs(A.numerator))),'v3':v3,'bound_floor3':n*3//8,'excess3_numerator':8*v3-n*3,'excess3_div8':(8*v3-n*3)/8,'v7':v7,'bound_floor7':n*7//48,'elapsed_s':time.perf_counter()-start}
print(json.dumps(r,indent=2))
with open('/mnt/data/riemann_run_20261123_1457/lemniscate_long.json','w') as f:json.dump(r,f,indent=2)
