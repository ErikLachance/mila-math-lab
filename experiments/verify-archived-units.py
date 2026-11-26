#!/usr/bin/env python3
"""Replay a small exact certificate from the archived Riemann exploration.

Python 3.10+, standard library only. Run from any working directory:
    python experiments/verify-archived-units.py
    python experiments/verify-archived-units.py --check

This program reads JSON data only. It imports or executes no archived scripts,
loads no pickle, performs no heuristic search, and uses no floating arithmetic.
It checks ten selected unit determinants in two supplied integer multiplication
tables, and finite linear algebra on their RECORDED local vectors over F_7.
It does not recompute the arithmetic embeddings or certify field identification,
maximality, class groups, reciprocity hypotheses, a global unit basis, or RH.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
import time


ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "archive" / "riemann"
DEFAULT_OUTPUT = ROOT / "results" / "archived-units-20261126.json"
PRIME = 7
DIMENSION = 42
ORDER_DIMENSION = 21


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def identity(n: int) -> list[list[int]]:
    return [[int(i == j) for j in range(n)] for i in range(n)]


def zero(rows: int, columns: int) -> list[list[int]]:
    return [[0] * columns for _ in range(rows)]


def checked_vector(value, n: int, label: str) -> list[int]:
    require(isinstance(value, list) and len(value) == n, f"Invalid {label} length")
    require(all(type(x) is int for x in value), f"Noninteger {label}")
    return value


def checked_matrix(value, rows: int, columns: int, label: str) -> list[list[int]]:
    require(isinstance(value, list) and len(value) == rows, f"Invalid {label} rows")
    for row in value:
        checked_vector(row, columns, label)
    return value


def multiply(a, b, modulus: int | None = None):
    require(len(a[0]) == len(b), "Incompatible matrix multiplication")
    columns = list(zip(*b))
    out = [[sum(x * y for x, y in zip(row, column)) for column in columns] for row in a]
    return [[x % modulus for x in row] for row in out] if modulus else out


def horizontal(*matrices):
    return [sum((list(matrix[i]) for matrix in matrices), []) for i in range(len(matrices[0]))]


def power(a, exponent: int):
    result = identity(len(a))
    base = a
    while exponent:
        if exponent & 1:
            result = multiply(result, base, PRIME)
        exponent >>= 1
        if exponent:
            base = multiply(base, base, PRIME)
    return result


def rank_mod7(matrix) -> int:
    """Row elimination over the exact prime field; no rational or real rank."""
    a = [[x % PRIME for x in row] for row in matrix]
    rank = 0
    for column in range(len(a[0])):
        pivot = next((i for i in range(rank, len(a)) if a[i][column]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inverse = pow(a[rank][column], -1, PRIME)
        a[rank] = [(x * inverse) % PRIME for x in a[rank]]
        for row in range(rank + 1, len(a)):
            factor = a[row][column]
            if factor:
                a[row] = [(x - factor * y) % PRIME for x, y in zip(a[row], a[rank])]
        rank += 1
        if rank == len(a):
            break
    return rank


def determinant_bareiss(matrix) -> int:
    """Fraction-free integer elimination, with row swaps and exact divisions."""
    a = [row[:] for row in matrix]
    n = len(a)
    if n == 0:
        return 1
    previous = 1
    sign = 1
    for k in range(n - 1):
        pivot_row = next((i for i in range(k, n) if a[i][k]), None)
        if pivot_row is None:
            return 0
        if pivot_row != k:
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                require(numerator % previous == 0, "Inexact Bareiss division")
                a[i][j] = numerator // previous
            a[i][k] = 0
        previous = pivot
    return sign * a[-1][-1]


def linear_combination(matrices, coefficients):
    n = len(matrices[0])
    out = zero(n, n)
    for coefficient, matrix in zip(coefficients, matrices):
        if coefficient:
            for i in range(n):
                for j in range(n):
                    out[i][j] += coefficient * matrix[i][j]
    return out


def verify_multiplication_table(data):
    """Check the supplied table defines a unital commutative integer algebra.

    No identification of this algebra with the claimed number field is made.
    Matrix-composition identities certify associativity of the supplied table.
    """
    n = ORDER_DIMENSION
    matrices = data["matrices"]
    require(isinstance(matrices, list) and len(matrices) == n, "Wrong multiplication table size")
    for matrix in matrices:
        checked_matrix(matrix, n, n, "multiplication table")
    one = checked_vector(data["one"], n, "identity coordinates")
    require(linear_combination(matrices, one) == identity(n), "Identity multiplication failed")
    require(all([sum(matrix[i][j] * one[j] for j in range(n)) for i in range(n)]
                == [int(i == k) for i in range(n)] for k, matrix in enumerate(matrices)),
            "Basis/identity compatibility failed")
    for i in range(n):
        for j in range(n):
            coefficients = [matrices[i][row][j] for row in range(n)]
            require(coefficients == [matrices[j][row][i] for row in range(n)],
                    "Multiplication table is not commutative")
            require(multiply(matrices[i], matrices[j]) == linear_combination(matrices, coefficients),
                    "Multiplication table composition identity failed")
    return matrices


def verify_case(q: int, certificate, order_data):
    matrices = verify_multiplication_table(order_data)
    units = certificate["units"]
    require(len(units) == 5, "Expected five selected units")
    indices = checked_vector(certificate["indices"], 5, "archived selection indices")
    require(len(set(indices)) == 5 and min(indices) >= 0, "Invalid archived indices")
    norm_results = []
    for index, entry in zip(indices, units):
        require(isinstance(entry, list) and len(entry) == 3, "Invalid unit record")
        vector = checked_vector(entry[0], ORDER_DIMENSION, "unit coordinates")
        recorded_norm = entry[1]
        require(type(recorded_norm) is int and abs(recorded_norm) == 1, "Invalid recorded unit norm")
        computed_norm = determinant_bareiss(linear_combination(matrices, vector))
        require(computed_norm == recorded_norm, "Selected unit determinant mismatch")
        norm_results.append({"archived_index": index, "determinant": computed_norm,
                             "maximum_absolute_coordinate": max(map(abs, vector))})

    vectors = checked_matrix(certificate["V"], 5, DIMENSION, "recorded local vectors")
    g = checked_matrix(certificate["G"], 6, 6, "local action")
    require(all(0 <= x < PRIME for row in vectors + g for x in row), "Noncanonical field representative")
    v = [list(column) for column in zip(*vectors)]
    ident = identity(DIMENSION)
    shift = [[int(j == (i + 6) % DIMENSION) for j in range(DIMENSION)] for i in range(DIMENSION)]
    action = zero(DIMENSION, DIMENSION)
    for block in range(7):
        for i in range(6):
            for j in range(6):
                action[6 * ((3 * block) % 7) + i][6 * block + j] = g[i][j]
    require(power(shift, 7) == ident, "Shift order failed")
    require(power(action, 6) == ident, "Action order failed")
    require(multiply(action, shift, PRIME) == multiply(power(shift, 3), action, PRIME),
            "Action/shift covariance failed")
    difference = [[(shift[i][j] - ident[i][j]) % PRIME for j in range(DIMENSION)] for i in range(DIMENSION)]
    derivative = zero(DIMENSION, DIMENSION)
    for k in range(1, 7):
        term = power(difference, k)
        coefficient = (-1) ** (k + 1) * pow(k, -1, PRIME)
        derivative = [[(derivative[i][j] + coefficient * term[i][j]) % PRIME
                       for j in range(DIMENSION)] for i in range(DIMENSION)]
    require(power(derivative, 7) == zero(DIMENSION, DIMENSION), "Logarithmic shift is not nilpotent")
    require(multiply(action, derivative, PRIME)
            == [[3 * x % PRIME for x in row] for row in multiply(derivative, action, PRIME)],
            "Action/logarithmic-shift covariance failed")

    orbit = horizontal(*(multiply(power(shift, k), v, PRIME) for k in range(7)))
    orbit_rank = rank_mod7(orbit)
    require(orbit_rank == 20, "Recorded-vector orbit does not have rank 20")
    require(rank_mod7(horizontal(orbit, multiply(action, orbit, PRIME))) == orbit_rank,
            "Orbit span is not stable under the recorded action")
    require(rank_mod7(horizontal(orbit, multiply(shift, orbit, PRIME))) == orbit_rank,
            "Orbit span is not stable under the shift")
    restriction_ranks = [rank_mod7(multiply(power(derivative, k), orbit, PRIME)) for k in range(8)]
    sum_ranks = [rank_mod7(horizontal(orbit, power(derivative, k))) for k in range(1, 8)]
    require(restriction_ranks == [20, 17, 14, 11, 8, 5, 2, 0], "Restriction filtration differs")
    require(restriction_ranks == certificate["ranks"], "Archived restriction ranks differ")
    require(sum_ranks == [38, 35, 32, 29, 26, 23, 20], "Ambient-sum filtration differs")
    weights = []
    action_powers = [power(action, k) for k in range(6)]
    for eigenvalue in range(1, 7):
        projector = [[sum(pow(eigenvalue, -k, PRIME) * action_powers[k][i][j] for k in range(6))
                      * pow(6, -1, PRIME) % PRIME for j in range(DIMENSION)] for i in range(DIMENSION)]
        projected = multiply(projector, orbit, PRIME)
        require(multiply(action, projected, PRIME)
                == [[eigenvalue * x % PRIME for x in row] for row in projected],
                "Weight projector is not in the named eigenspace")
        weights.append(rank_mod7(projected))
    require(weights == [3, 4, 3, 4, 3, 3] == certificate["weights"], "Weight dimensions differ")
    require(sum(weights) == orbit_rank, "Weights do not exhaust the orbit span")
    ranks = restriction_ranks + [0]
    jordan_lengths = sorted((k for k in range(1, 8)
                             for _ in range(ranks[k - 1] - 2 * ranks[k] + ranks[k + 1])), reverse=True)
    require(jordan_lengths == [7, 7, 6], "Jordan dimensions differ")
    return {"q": q, "multiplication_dimension": ORDER_DIMENSION,
            "integer_table_composition_identities_checked": ORDER_DIMENSION ** 2,
            "selected_units": norm_results, "recorded_local_vectors": len(vectors),
            "shift_orbit_columns": len(orbit[0]), "ambient_dimension_over_F7": DIMENSION,
            "orbit_rank": orbit_rank, "restriction_ranks_D_power_U": restriction_ranks,
            "sum_ranks_U_plus_image_D_power": sum_ranks,
            "weight_eigenvalues": list(range(1, 7)), "weight_dimensions": weights,
            "jordan_block_lengths_on_orbit_span": jordan_lengths,
            "identities_verified": ["S^7=I", "G^6=I", "GS=S^3G", "D^7=0", "GD=3DG",
                                     "S(U)=U", "G(U)=U"]}


def run(archive_root: Path):
    inputs = []

    def read(relative: str):
        raw = (archive_root / relative).read_bytes()
        inputs.append({"path": "archive/riemann/" + relative,
                       "sha256": hashlib.sha256(raw).hexdigest()})
        return json.loads(raw)

    minimal = read("2026-11-25_1151/files/minimal_certificate.json")
    cases = [verify_case(q, minimal[str(q)], read(f"2026-11-25_1105/files/units_wide{q}.json"))
             for q in (683, 907)]
    return {"schema_version": 1, "date": "2026-11-26", "status": "pass",
            "arithmetic": "exact integers and F_7; Python standard library; no floating point",
            "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "inputs": inputs, "selected_unit_determinants_checked": 10,
            "cases": cases,
            "scope": {
                "verified": ["The supplied integer multiplication tables satisfy unital, commutative, associative table identities.",
                             "The ten selected multiplication determinants equal their recorded values +1 or -1.",
                             "The recorded local vectors generate the reported F_7 orbit spaces, filtrations and weight dimensions."],
                "not_replayed_or_proved": ["Arithmetic evaluation of units in the claimed local embeddings.",
                                           "Equality of independently regenerated 7-adic precision levels.",
                                           "Identification or maximality of the number-field orders.",
                                           "Completeness or saturation of the global unit groups.",
                                           "Class-group, Kummer, reciprocity or global automorphy hypotheses.",
                                           "The local expansion coefficients e_loc and e8.",
                                           "Any proof of the Riemann hypothesis."]}}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive-root", type=Path, default=ARCHIVE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--check", action="store_true", help="compare with the saved report without modifying it")
    args = parser.parse_args()
    started = time.monotonic()
    report = run(args.archive_root)
    encoded = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.check:
        require(args.output.read_text(encoding="utf-8") == encoded, "Recorded replay report differs")
        verb = "verified"
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded, encoding="utf-8")
        verb = "wrote"
    print(f"PASS: {verb} {args.output}")
    print(f"elapsed_seconds={time.monotonic() - started:.3f}", file=sys.stderr)
    print(f"result_sha256={hashlib.sha256(encoded.encode()).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
