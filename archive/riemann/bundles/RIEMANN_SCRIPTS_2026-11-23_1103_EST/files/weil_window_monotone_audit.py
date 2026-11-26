#!/usr/bin/env python3
"""Monotonicity falsification of unsafe global margin extrapolations: NOT a new RH proof."""
from fractions import Fraction as F
import json, math
L0=F(4,5)         # 0.8
L1=F(81,100)      # 0.81
upper_at_L0=F(227,10**19)  # 2.27e-17, NOT 2.27e-18
lower_at_L0=F(89,10**19)   # 8.9e-18
finite_even_L1=F(1,10**14)
finite_odd_L1=F(1,10**13)
assert L0<L1 and lower_at_L0<upper_at_L0<finite_even_L1
ratio=finite_even_L1/upper_at_L0
# Source reported 16-dimensional compression positive; cannot infer its bound for all test functions.
assert ratio>F(400)
# The exact upper bound implies there exists a test f supported in L0 with Q(f)/||f||² <= bound
# up to arbitrary epsilon (infimum property), and the same f is admissible in L1.
# Thus any asserted Q >= 1e-14||f||² on the entire L1 support domain contradicts that upper bound.
Tstar=2*math.pi*math.exp(2*float(L1))
shannon=2*float(L1)*Tstar/math.pi
r={
 'source':'https://arxiv.org/html/2608.24827v2 (September 2026 v2); report L=.8 upper 2.27e-17 even real, lower 8.9e-18 all parity',
 'window_inclusion':'C_c(-0.8,0.8) is a subset of C_c(-0.81,0.81), so lambda_even*(0.81)<=lambda_even*(0.8)',
 'exact_upper_lambda_even_L081':str(upper_at_L0),
 'invalid_possible_extrapolated_global_margin':str(finite_even_L1),
 'exact_ratio_wrong_margin_to_upper':str(ratio),
 'conclusion':'A claimed full-window >=1e-14 at L=.81 would contradict the independent, unconditional L=.8 upper bound. The recorded 8-even finite Fourier span lower bound is NOT a full-window claim and remains compatible.',
 'heuristic_Tstar_at_L081':Tstar,
 'heuristic_time_bandwidth_count':shannon,
 'warning':'Empirical resolution Tstar and Shannon count are heuristics and NOT a finite-dimensional completeness certificate.',
 'status':'EXACT RATIONAL COMPARISON PASS; mathematical implication conditional on correctness and matching normalization of source certificate'
}
with open('/mnt/data/riemann_runs/20261123_1047/weil_window_monotone_audit.json','w') as f:json.dump(r,f,indent=2)
print(json.dumps(r,indent=2))
