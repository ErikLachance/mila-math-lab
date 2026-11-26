#!/usr/bin/env python3
"""Exact finite checks for Boolean relation degree; Python 3.10+, standard library.

Run from any directory:
    python experiments/boolean-degree-20261126.py
    python experiments/boolean-degree-20261126.py --check

Coordinates are little endian. A point is its binary integer, an ANF monomial
is the mask of its variables, and truth-table bit x is the value at point x.
All arithmetic is in F_2. No floating-point calculation enters a check.

The evaluation-matrix implementation and the exhaustive multiplier formula
use different representations: direct monomial evaluations versus truth-table
multiplication followed by the Boolean Mobius transform. Finite agreement is
evidence about this implementation, not a proof of an infinite-family claim.
"""

from __future__ import annotations

import argparse
from collections import Counter
from functools import lru_cache
import hashlib
from itertools import combinations
import json
from math import comb
from pathlib import Path
import random
import sys
import time


SEED = 20261126
DEFAULT_OUTPUT = Path(__file__).resolve().parents[1] / "results/boolean-degree-20261126.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def bits(value: int):
    while value:
        low = value & -value
        yield low.bit_length() - 1
        value ^= low


@lru_cache(maxsize=None)
def monomials(n: int) -> tuple[int, ...]:
    return tuple(sorted(range(1 << n), key=lambda m: (m.bit_count(), m)))


def evaluate_anf(coefficients: int, point: int) -> int:
    return sum((point & mask) == mask for mask in bits(coefficients)) & 1


def anf_from_truth(truth: int, n: int) -> int:
    """In-place subset Mobius transform of the complete truth table."""
    values = [(truth >> x) & 1 for x in range(1 << n)]
    for coordinate in range(n):
        bit = 1 << coordinate
        for mask in range(1 << n):
            if mask & bit:
                values[mask] ^= values[mask ^ bit]
    return sum(value << mask for mask, value in enumerate(values))


def anf_degree(coefficients: int) -> int:
    # Degree -1 is used internally for the zero polynomial.
    return max((mask.bit_count() for mask in bits(coefficients)), default=-1)


@lru_cache(maxsize=65536)
def minimum_relation(n: int, points: tuple[int, ...]) -> tuple[int | None, int]:
    """First linear dependence of evaluation columns ordered by total degree.

    Returns (minimum degree, ANF coefficient bitset). None means no relation,
    possible only for the full cube. The empty set is allowed internally for
    algebraic immunity and has the constant relation 1 of degree zero.
    """
    require(len(set(points)) == len(points), "Repeated point")
    require(all(0 <= point < 1 << n for point in points), "Point outside cube")
    basis: dict[int, tuple[int, int]] = {}
    for mask in monomials(n):
        column = sum(((point & mask) == mask) << row
                     for row, point in enumerate(points))
        relation = 1 << mask
        while column:
            pivot = column.bit_length() - 1
            previous = basis.get(pivot)
            if previous is None:
                basis[pivot] = (column, relation)
                break
            column ^= previous[0]
            relation ^= previous[1]
        if not column:
            require(relation != 0, "Trivial dependence")
            require(anf_degree(relation) == mask.bit_count(), "Wrong witness degree")
            require(all(evaluate_anf(relation, point) == 0 for point in points),
                    "Invalid evaluation-kernel witness")
            return mask.bit_count(), relation
    require(len(points) == 1 << n, "Missing relation on a proper subset")
    return None, 0


def finite_min(values) -> int | None:
    finite = [value for value in values if value is not None]
    return min(finite) if finite else None


def graph_points(n: int, truth: int) -> tuple[int, ...]:
    return tuple(x | (((truth >> x) & 1) << n) for x in range(1 << n))


def algebraic_immunity(n: int, truth: int) -> int:
    ones = tuple(x for x in range(1 << n) if (truth >> x) & 1)
    zeros = tuple(x for x in range(1 << n) if not (truth >> x) & 1)
    result = finite_min((minimum_relation(n, ones)[0], minimum_relation(n, zeros)[0]))
    require(result is not None, "Algebraic immunity cannot be infinite")
    return result


def product(factors: list[tuple[int, tuple[int, ...]]]) -> tuple[int, tuple[int, ...]]:
    points = [0]
    dimension = 0
    for n, factor_points in factors:
        points = [left | (right << dimension) for left in points for right in factor_points]
        dimension += n
    return dimension, tuple(sorted(points))


class Transcript:
    def __init__(self):
        self.count = 0
        self.hasher = hashlib.sha256()

    def add(self, value) -> None:
        self.hasher.update(json.dumps(value, sort_keys=True, separators=(",", ":")).encode())
        self.hasher.update(b"\n")
        self.count += 1

    def summary(self) -> dict:
        return {"cases": self.count, "transcript_sha256": self.hasher.hexdigest()}


def histogram(counter: Counter) -> list[dict]:
    return [{"algebraic_immunity": ai, "graph_relation_degree": degree, "count": count}
            for (ai, degree), count in sorted(counter.items())]


def exhaustive_graph_formula() -> dict:
    transcript = Transcript()
    by_arity = []
    multipliers = 0
    for n in range(4):
        table_count = 1 << (1 << n)
        coefficients = [anf_from_truth(truth, n) for truth in range(table_count)]
        degrees = [anf_degree(anf) for anf in coefficients]
        counts = Counter()
        for truth in range(table_count):
            direct, _ = minimum_relation(n + 1, graph_points(n, truth))
            formula = min(max(1 + degrees[b], degrees[truth & b])
                          for b in range(1, table_count))
            ai_rank = algebraic_immunity(n, truth)
            ai_enumerated = min(degrees[b] for b in range(1, table_count)
                                if truth & b == 0 or (truth ^ (table_count - 1)) & b == 0)
            require(direct == formula, f"Graph formula failed: n={n}, h={truth}")
            require(ai_rank == ai_enumerated, "Algebraic immunity implementations disagree")
            require(ai_rank <= direct <= ai_rank + 1, "AI bounds failed")
            counts[(ai_rank, direct)] += 1
            transcript.add([n, truth, direct, formula, ai_rank, ai_enumerated])
            multipliers += table_count - 1
        by_arity.append({"input_variables": n, "functions": table_count,
                         "degree_pairs": histogram(counts)})
    return {**transcript.summary(), "nonzero_multiplier_evaluations": multipliers,
            "arities": by_arity}


def check_product_case(factors, transcript: Transcript) -> None:
    require(all(points for _, points in factors), "Empty factors are outside the product claim")
    n, points = product(factors)
    expected = finite_min(minimum_relation(k, values)[0] for k, values in factors)
    actual, _ = minimum_relation(n, points)
    require(actual == expected, f"Product formula failed: dimensions {[k for k, _ in factors]}")
    transcript.add({"factors": [[k, list(values)] for k, values in factors],
                    "product_dimension": n, "product_points": len(points),
                    "expected_degree": expected, "actual_degree": actual})


def product_checks() -> dict:
    small = [(n, tuple(bits(mask))) for n in range(3)
             for mask in range(1, 1 << (1 << n))]
    exhaustive = Transcript()
    for left in small:
        for right in small:
            check_product_case([left, right], exhaustive)

    free = Transcript()
    for factor in small:
        for free_dimension in range(5):
            check_product_case([factor, (free_dimension, tuple(range(1 << free_dimension)))], free)

    larger = Transcript()
    rng = random.Random(SEED)
    for _ in range(64):
        factors = []
        for _ in range(rng.choice((2, 3))):
            n = rng.choice((1, 2, 3))
            mask = rng.randrange(1, 1 << (1 << n))
            factors.append((n, tuple(bits(mask))))
        check_product_case(factors, larger)
    for truth in (0x17, 0x69, 0x96, 0xE8):
        factor = (4, graph_points(3, truth))
        for repetitions in (2, 3):
            check_product_case([factor] * repetitions, larger)
    strict_factor = (6, graph_points(5, 0x17543756))
    check_product_case([strict_factor, strict_factor], larger)
    return {"all_nonempty_subsets_dimensions_0_to_2": exhaustive.summary(),
            "free_coordinates_0_to_4": free.summary(),
            "seeded_and_structured_larger_products": larger.summary(), "seed": SEED}


def balanced_checks() -> dict:
    transcript = Transcript()
    counts = Counter()
    for support in combinations(range(16), 8):
        truth = sum(1 << point for point in support)
        ai = algebraic_immunity(4, truth)
        degree, _ = minimum_relation(5, graph_points(4, truth))
        require(ai <= degree <= ai + 1, "Balanced four-input AI bound failed")
        counts[(ai, degree)] += 1
        transcript.add([truth, ai, degree])

    truth = 0x17543756
    points = graph_points(5, truth)
    ai = algebraic_immunity(5, truth)
    degree, witness = minimum_relation(6, points)
    require(truth.bit_count() == 16 and ai == 2 and degree == 3, "Strict balanced example failed")
    # A transparent quadratic annihilator: x0*x1 is zero wherever h=1.
    require(all(not (point & 3) == 3 for point in range(32) if (truth >> point) & 1),
            "Named quadratic annihilator failed")

    structured_truth = 0
    for point in range(32):
        a, b, c, d, e = [(point >> coordinate) & 1 for coordinate in range(5)]
        f = b ^ c ^ d ^ (b & c) ^ (b & d) ^ (c & d)
        value = ((1 ^ a) & f) ^ (a & (1 ^ b) & e)
        structured_truth |= value << point
    structured_ai = algebraic_immunity(5, structured_truth)
    structured_degree, structured_witness = minimum_relation(6, graph_points(5, structured_truth))
    require(structured_truth == 0x37761554 and structured_truth.bit_count() == 16,
            "Structured example is not the stated balanced function")
    require(structured_ai == 2 and structured_degree == 3, "Structured strict example failed")
    require(all(not (point & 3) == 3 for point in range(32)
                if (structured_truth >> point) & 1), "Structured annihilator failed")
    return {"all_balanced_four_input_functions": {**transcript.summary(),
                "degree_pairs": histogram(counts)},
            "balanced_five_input_strict_example": {
                "input_variables": 5, "truth_table_hex": hex(truth),
                "one_set": list(bits(truth)),
                "function_anf_monomial_masks": list(bits(anf_from_truth(truth, 5))),
                "algebraic_immunity": ai, "graph_relation_degree": degree,
                "quadratic_annihilator_monomial_mask": 3,
                "graph_rank_through_degree_2": sum(comb(6, k) for k in range(3)),
                "graph_relation_monomial_masks": list(bits(witness))},
            "balanced_five_input_structured_strict_example": {
                "input_variables": 5, "coordinate_names": ["a", "b", "c", "d", "e"],
                "formula_over_F2": "f=b+c+d+bc+bd+cd; h=(1+a)f+a(1+b)e",
                "truth_table_hex": hex(structured_truth),
                "one_set": list(bits(structured_truth)),
                "function_anf_monomial_masks": list(bits(anf_from_truth(structured_truth, 5))),
                "algebraic_immunity": structured_ai, "graph_relation_degree": structured_degree,
                "quadratic_annihilator_monomial_mask": 3,
                "graph_rank_through_degree_2": sum(comb(6, k) for k in range(3)),
                "graph_relation_monomial_masks": list(bits(structured_witness))}}


def threshold_checks() -> dict:
    transcript = Transcript()
    cases = []
    for n in range(1, 9):
        for threshold in range(1, n + 1):
            truth = sum((x.bit_count() >= threshold) << x for x in range(1 << n))
            degree, witness = minimum_relation(n + 1, graph_points(n, truth))
            ai = algebraic_immunity(n, truth)
            expected_ai = min(threshold, n - threshold + 1)
            expected = threshold if n == 2 * threshold - 1 else expected_ai + 1
            require(ai == expected_ai, f"Threshold AI formula failed: {n}, {threshold}")
            require(degree == expected, f"Threshold graph formula failed: {n}, {threshold}")
            record = {"input_variables": n, "threshold": threshold,
                      "algebraic_immunity": ai, "graph_relation_degree": degree,
                      "full_rank_through_degree": degree - 1,
                      "rank_at_that_degree": sum(comb(n + 1, k) for k in range(degree)),
                      "witness_monomial_masks": list(bits(witness))}
            transcript.add(record)
            cases.append(record)

    majorities = []
    evaluation_count = 0
    for n in range(1, 14, 2):
        threshold = (n + 1) // 2
        first = (1 << threshold) - 1
        # A = product(first t variables), C = product(1+x_i), B = A+C.
        # In characteristic two A cancels the top monomial in C.
        b_masks = list(range(first))
        q_masks = [first] + [(1 << n) | mask for mask in b_masks]
        q = sum(1 << mask for mask in q_masks)
        require(anf_degree(q) == threshold, "Majority witness has wrong degree")
        for x in range(1 << n):
            point = x | ((x.bit_count() >= threshold) << n)
            require(evaluate_anf(q, point) == 0, f"Majority witness failed: n={n}, x={x}")
        evaluation_count += 1 << n
        majorities.append({"input_variables": n, "threshold": threshold,
                           "witness_degree": threshold, "witness_terms": len(q_masks),
                           "graph_points_checked": 1 << n,
                           "witness_monomial_masks": sorted(q_masks),
                           "lower_degree_rank_computed": n <= 7})
    return {**transcript.summary(), "thresholds": cases,
            "odd_majority_expanded_witnesses": majorities,
            "majority_graph_evaluations": evaluation_count,
            "scope": "Ranks certify thresholds through n=8. For n=9,11,13 only the explicit upper-bound witness is evaluated; the lower bound requires the analytic proof."}


def run() -> dict:
    return {"schema_version": 1, "status": "pass", "date": "2026-11-26",
            "arithmetic": "exact GF(2); Python integers; no floating point",
            "conventions": {"coordinates": "little endian",
                            "truth_table_bit_x": "function value at point x",
                            "monomial_mask": "bit i selects variable x_i; 0 is constant 1",
                            "infinite_relation_degree": None,
                            "internal_zero_polynomial_degree": -1},
            "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "graph_formula_and_algebraic_immunity": exhaustive_graph_formula(),
            "cartesian_products": product_checks(),
            "balanced_functions": balanced_checks(),
            "threshold_functions": threshold_checks(),
            "limitations": [
                "Finite checks do not prove the Cartesian-product or threshold formulas for all dimensions.",
                "The n=13 majority calculation verifies an explicit degree-seven relation on all 8192 graph points; it does not independently compute the rank of all degree-six monomials.",
                "Boolean relation degree is not a general Boolean-circuit lower bound and gives no P-versus-NP separation.",
                "No literature novelty is claimed."]}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--check", action="store_true", help="compare to the recorded JSON without modifying it")
    arguments = parser.parse_args()
    started = time.monotonic()
    report = run()
    encoded = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if arguments.check:
        require(arguments.output.read_text(encoding="utf-8") == encoded,
                f"Recorded result differs: {arguments.output}")
        action = "verified"
    else:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        arguments.output.write_text(encoded, encoding="utf-8")
        action = "wrote"
    print(f"PASS: {action} {arguments.output}")
    print(f"elapsed_seconds={time.monotonic() - started:.3f}", file=sys.stderr)
    print(f"result_sha256={hashlib.sha256(encoded.encode()).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
