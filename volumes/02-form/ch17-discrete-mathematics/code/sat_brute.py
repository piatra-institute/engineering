# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Brute-force SAT solver and 3-CNF random-instance generator.

Reference: SAT background in section 17.4. The brute-force solver
enumerates all 2^n assignments and is the canonical pedagogical
baseline against which a CDCL solver (MiniSat, Kissat, CaDiCaL) is
benchmarked. The simulation exercise in section 17.9 uses this
script to verify the exponential-in-n running time empirically.

Run: uv run code/sat_brute.py
"""

from __future__ import annotations

import random
import time

Clause = tuple[int, ...]  # positive literal i = variable i, negative -i
CNF = list[Clause]


def random_3cnf(n: int, m: int, seed: int = 0) -> CNF:
    """m clauses of width 3 over n variables, indices 1..n."""
    rng = random.Random(seed)
    instance: CNF = []
    while len(instance) < m:
        vars_ = rng.sample(range(1, n + 1), 3)
        clause = tuple(v if rng.random() < 0.5 else -v for v in vars_)
        instance.append(clause)
    return instance


def evaluate(cnf: CNF, assignment: list[bool]) -> bool:
    for clause in cnf:
        satisfied = False
        for lit in clause:
            var = abs(lit)
            value = assignment[var - 1]
            if (lit > 0 and value) or (lit < 0 and not value):
                satisfied = True
                break
        if not satisfied:
            return False
    return True


def solve_brute(cnf: CNF, n: int) -> list[bool] | None:
    for mask in range(2**n):
        assignment = [(mask >> i) & 1 == 1 for i in range(n)]
        if evaluate(cnf, assignment):
            return assignment
    return None


def benchmark() -> None:
    print(f"{'n':>4}  {'m':>5}  {'sat?':>5}  {'time (s)':>10}")
    for n in (10, 15, 20, 22):
        m = round(4.25 * n)  # near 3-SAT phase-transition density
        cnf = random_3cnf(n, m, seed=2026)
        t0 = time.time()
        result = solve_brute(cnf, n)
        elapsed = time.time() - t0
        verdict = "SAT" if result is not None else "UNSAT"
        print(f"{n:>4}  {m:>5}  {verdict:>5}  {elapsed:>10.3f}")


if __name__ == "__main__":
    benchmark()
