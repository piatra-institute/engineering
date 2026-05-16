# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy", "scipy"]
# ///
"""A toy diet linear program, in the spirit of Stigler (1945).

Five foods, three nutritional constraints, costs and per-food nutrient
amounts loaded from data/diet_problem.csv. Solves

    min c^T x
    subject to A x >= b, x >= 0

with the HiGHS backend exposed by scipy.optimize.linprog. Prints the
optimal cost, the active constraints (binding nutrients), and the
dual variables (shadow prices). The values are illustrative; the
purpose is to exhibit a small LP whose dual carries an interpretable
shadow-price reading for each nutrient.
"""

from __future__ import annotations

import csv
import pathlib

import numpy as np
from scipy.optimize import linprog

DATA = pathlib.Path(__file__).resolve().parent.parent / "data" / "diet_problem.csv"


def load() -> tuple[list[str], np.ndarray, np.ndarray, list[str], np.ndarray]:
    """Return (food names, cost vector c, nutrient matrix A, nutrient names, requirement vector b)."""
    with DATA.open() as fh:
        rows = list(csv.reader(fh))
    header = rows[0]
    # header: food, cost_usd_per_unit, energy_kcal, protein_g, calcium_mg
    nutrient_names = header[2:]
    data_rows = rows[1:-1]
    req_row = rows[-1]
    foods = [r[0] for r in data_rows]
    c = np.array([float(r[1]) for r in data_rows])
    A = np.array([[float(v) for v in r[2:]] for r in data_rows]).T
    b = np.array([float(v) for v in req_row[2:]])
    return foods, c, A, nutrient_names, b


def main() -> None:
    foods, c, A, nutrient_names, b = load()
    # linprog minimises c^T x subject to A_ub x <= b_ub, A_eq x = b_eq.
    # We have A x >= b, so flip: -A x <= -b.
    res = linprog(
        c=c,
        A_ub=-A,
        b_ub=-b,
        bounds=[(0.0, None)] * len(c),
        method="highs",
    )
    if not res.success:
        print(f"linprog failed: {res.message}")
        return
    print("Diet LP solution")
    print()
    print(f"{'food':>20}  {'units/day':>12}")
    for name, qty in zip(foods, res.x):
        print(f"{name:>20}  {qty:>12.4f}")
    print()
    print(f"optimal daily cost: USD {res.fun:.4f}")
    print()
    # Dual variables on the inequality block (we used -A x <= -b),
    # so the shadow prices on the nutrient requirements are -res.ineqlin.marginals.
    duals = -res.ineqlin.marginals
    print("Shadow prices (USD per additional unit of nutrient required)")
    for name, mu in zip(nutrient_names, duals):
        print(f"  {name:>12}: {mu:>10.4f}")


if __name__ == "__main__":
    main()
