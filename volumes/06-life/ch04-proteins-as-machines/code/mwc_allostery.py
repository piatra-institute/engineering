# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy"]
# ///
"""Two-state MWC (Monod-Wyman-Changeux) allosteric model.

A homotetramer exists in two conformations R (relaxed, high affinity)
and T (tense, low affinity). The allosteric equilibrium constant in
the absence of ligand is L = [T0] / [R0]. Ligand binds R with
dissociation constant KR and T with dissociation constant KT > KR.

The fractional saturation is
    Y(x) = ( x(1+x)^(n-1) + L c x (1 + c x)^(n-1) )
         / ( (1+x)^n + L (1 + c x)^n )
where x = [L]/KR and c = KR/KT.

Engineering reading: large L makes the basal state T-dominated and
the ligand-binding curve sigmoidal. Small c (large KT/KR ratio) makes
T effectively non-binding and shifts the apparent KD. The model
captures haemoglobin's cooperative oxygen binding with L ~ 9000 and
c ~ 0.014, giving a Hill coefficient of ~2.8.
"""

from __future__ import annotations

import math


def mwc_saturation(x: float, n: int, L: float, c: float) -> float:
    r_term = x * (1 + x) ** (n - 1)
    t_term = L * c * x * (1 + c * x) ** (n - 1)
    denom = (1 + x) ** n + L * (1 + c * x) ** n
    return (r_term + t_term) / denom


def hill_coefficient(L: float, c: float, n: int) -> float:
    # Numerical estimate of nH at the midpoint of the saturation curve.
    target = 0.5
    lo, hi = 1e-4, 1e4
    for _ in range(80):
        mid = math.sqrt(lo * hi)
        if mwc_saturation(mid, n, L, c) < target:
            lo = mid
        else:
            hi = mid
    x50 = math.sqrt(lo * hi)
    eps = 0.01
    y_minus = mwc_saturation(x50 * (1 - eps), n, L, c)
    y_plus = mwc_saturation(x50 * (1 + eps), n, L, c)
    slope = (math.log(y_plus / (1 - y_plus)) - math.log(y_minus / (1 - y_minus))) / (
        math.log(x50 * (1 + eps)) - math.log(x50 * (1 - eps))
    )
    return slope


def main() -> None:
    print(f"{'L':>7} {'c':>7} {'n':>3} {'n_Hill':>8}")
    for L in [1, 100, 1000, 9000, 100000]:
        for c in [1.0, 0.1, 0.014, 0.001]:
            n_hill = hill_coefficient(L=L, c=c, n=4)
            print(f"{L:7d} {c:7.3f} {4:3d} {n_hill:8.2f}")
    print()
    print("Haemoglobin parameters (L ~ 9000, c ~ 0.014, n = 4) reproduce")
    print("the observed Hill coefficient near 2.8.")


if __name__ == "__main__":
    main()
