"""Buckingham-Pi: compute dimensionless groups for a set of variables.

Given a list of variables and their dimensions in (M, L, T, K, Theta)
SI base units (mass, length, time, current, temperature), computes a
maximal set of independent dimensionless products by finding the null
space of the dimension matrix.

Demonstrates on:
  - the simple pendulum (T, L, g, m): one group, T sqrt(g/L)
  - the simply supported beam (y, w, L, E, I): two groups
  - the cooling cup (k, h, c, rho, L): one group, the Biot number

Dependencies: numpy, sympy (for rational null space).

Run:
    python dimensional_analysis.py
"""
from __future__ import annotations

from sympy import Matrix


# Dimension columns: (M, L, T, I, Theta)
PROBLEMS = {
    "pendulum (period, length, gravity, mass)": {
        "T": (0, 0, 1, 0, 0),
        "L": (0, 1, 0, 0, 0),
        "g": (0, 1, -2, 0, 0),
        "m": (1, 0, 0, 0, 0),
    },
    "beam deflection (y, w, L, E, I)": {
        "y": (0, 1, 0, 0, 0),
        "w": (1, 0, -2, 0, 0),    # force / length: kg / s^2
        "L": (0, 1, 0, 0, 0),
        "E": (1, -1, -2, 0, 0),   # Pa: kg / (m s^2)
        "I": (0, 4, 0, 0, 0),     # m^4
    },
    "cooling (h, k, c, rho, L)": {
        "h": (1, 0, -3, 0, -1),   # W / (m^2 K): kg / (s^3 K)
        "k": (1, 1, -3, 0, -1),   # W / (m K)
        "c": (0, 2, -2, 0, -1),   # J / (kg K): m^2 / (s^2 K)
        "rho": (1, -3, 0, 0, 0),
        "L": (0, 1, 0, 0, 0),
    },
}


def pi_groups(variables: dict[str, tuple]) -> None:
    names = list(variables.keys())
    M = Matrix([list(variables[n]) for n in names]).T  # rows = dims, cols = variables
    ns = M.nullspace()
    print(f"  rank of dimension matrix: {M.rank()}")
    print(f"  number of independent dimensionless groups: {len(ns)}")
    for i, v in enumerate(ns):
        terms = []
        for n, exp in zip(names, v):
            exp = exp.simplify()
            if exp == 0:
                continue
            if exp == 1:
                terms.append(n)
            else:
                terms.append(f"{n}^({exp})")
        if not terms:
            terms = ["(trivial)"]
        print(f"  Pi_{i+1} = {' * '.join(terms)}")


def main() -> None:
    for label, variables in PROBLEMS.items():
        print(f"\nProblem: {label}")
        pi_groups(variables)
    print("\nReading: the number of dimensionless groups equals (number of variables) -")
    print("(rank of dimension matrix). For the pendulum this is 4 - 3 = 1; the single")
    print("group T sqrt(g/L) is the dimensionless period. Mass m drops out: this is the")
    print("structural argument that the period is mass-independent, independent of any data.")


if __name__ == "__main__":
    main()
