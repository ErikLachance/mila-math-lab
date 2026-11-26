"""Finite countermodel for swapping the quantifiers in DesignExists.
The formal argument is in checkpoint; these enumerations test finite surrogates.
"""
import json
from fractions import Fraction
records = []
for cutoff in [2, 3, 5, 8, 13, 21, 34, 55]:
    K = list(range(cutoff + 1))
    families = list(range(cutoff + 1))
    large = lambda m,k: m >= k
    forall_K_exists_family = all(any(large(f,k) for f in families) for k in K)
    exists_family_forall_K = any(all(large(f,k) for k in K) for f in families)
    # finite sets make both true if cap==maximum K. Remove one-step extreme.
    if cutoff >= 2:
        families_n = list(range(cutoff))
        false_model = {
            'all_K_thresholds_met': all(any(large(f,k) for f in families_n) for k in range(cutoff)),
            'one_f_meets_all_unbounded_K': any(all(large(f,k) for k in range(cutoff + 1)) for f in families_n),
        }
    else: false_model = None
    # independent analytical zero-free region only: sigma=3/4 satisfies when T >= e^(4c)-3
    for c in [Fraction(1,10), Fraction(1,2), Fraction(3,2)]:
        # choose T huge using integer ceiling approximations in real math proof
        import math
        t = max(0., math.exp(4*float(c)) - 3.) + 100.
        region = Fraction(3,4) <= 1 - float(c)/math.log(t+3)
        records.append({'cutoff':cutoff,'c':str(c),'T':t,'zeta_region_allows_sigma_0p75_at_T':region})
    assert forall_K_exists_family and exists_family_forall_K
    assert false_model['all_K_thresholds_met'] is True
    assert false_model['one_f_meets_all_unbounded_K'] is False
    assert records[-1]['zeta_region_allows_sigma_0p75_at_T']
print(json.dumps({'total_checks':len(records),'finite_quantifier_model':'all pass','observations':records}, indent=2))
