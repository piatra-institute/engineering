# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy"]
# ///
"""Sweep polynomial degree p; report Vandermonde conditioning in three bases.

Reproduces the numbers behind Figure 9.5 (vol02/ch09).
"""

from __future__ import annotations

import numpy as np


def vandermonde(x: np.ndarray, p: int) -> np.ndarray:
    return np.vander(x, N=p + 1, increasing=True)


def chebyshev_design(x: np.ndarray, p: int) -> np.ndarray:
    # Build T_0, T_1, ..., T_p evaluated at x in [-1, 1] by recurrence.
    m = x.size
    T = np.zeros((m, p + 1))
    T[:, 0] = 1.0
    if p >= 1:
        T[:, 1] = x
    for k in range(2, p + 1):
        T[:, k] = 2.0 * x * T[:, k - 1] - T[:, k - 2]
    return T


def main() -> None:
    m = 100
    x01 = np.linspace(0.0, 1.0, m)
    xpm = np.linspace(-1.0, 1.0, m)

    print(f"{'p':>3} {'kappa mono[0,1]':>16} {'kappa mono[-1,1]':>17} {'kappa Cheb[-1,1]':>18}")
    for p in range(1, 13):
        Va = vandermonde(x01, p)
        Vb = vandermonde(xpm, p)
        Tc = chebyshev_design(xpm, p)
        ka = np.linalg.cond(Va)
        kb = np.linalg.cond(Vb)
        kc = np.linalg.cond(Tc)
        print(f"{p:>3} {ka:>16.3e} {kb:>17.3e} {kc:>18.3e}")


if __name__ == "__main__":
    main()
