"""Kremser-equation absorber sizing for linear equilibrium y* = m x.

Given the absorption factor A = L / (m G), the number of theoretical
stages N, and the inlet gas composition, the Kremser equation returns
the fractional solute recovery. The script also inverts for the stages
needed to hit a target recovery.

Usage:
    python kremser_absorber.py
"""

from __future__ import annotations
from math import log


def recovery(A: float, N: int) -> float:
    """Fraction of entering solute absorbed, lean solvent (x0 = 0)."""
    if abs(A - 1.0) < 1e-9:
        return N / (N + 1.0)
    return (A ** (N + 1) - A) / (A ** (N + 1) - 1.0)


def stages_for_recovery(A: float, target: float) -> float:
    """Theoretical stages to reach a target fractional recovery."""
    if abs(A - 1.0) < 1e-9:
        return target / (1.0 - target)
    # invert the Kremser equation for N (lean-solvent form)
    num = log((1.0 - target / A) / (1.0 - target))
    return num / log(A) - 1.0


if __name__ == "__main__":
    A = 1.5
    print(f"recovery at N=5    : {recovery(A, 5):.3f}")
    print(f"stages for 95%     : {stages_for_recovery(A, 0.95):.2f}")
