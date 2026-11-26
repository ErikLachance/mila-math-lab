"""Falsification-only finite numerical check of RH consequence Robin inequality.
No implication in the reverse direction from a finite prefix.
"""
import math, json
N=200000
sigma=[0]*(N+1)
for d in range(1,N+1):
    for n in range(d,N+1,d): sigma[n]+=d
GAMMA=0.57721566490153286060651209008240243
ratio=lambda n:sigma[n]/(math.exp(GAMMA)*n*math.log(math.log(n)))
violations=[n for n in range(5041,N+1) if ratio(n)>=1]
record=sorted(range(5041,N+1),key=ratio,reverse=True)[:12]
near={str(n):{'sigma':sigma[n],'robin_ratio':ratio(n),'difference':math.exp(GAMMA)*n*math.log(math.log(n))-sigma[n]} for n in [5040,5041,10080,27720,55440,110880,166320,200000]}
assert not violations
print(json.dumps({'N':N,'candidate_violations_above_5040':violations,'max_ratio_at':record,'near':near},indent=2))
