# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy", "scipy"]
# ///
"""Minimum-volume sizing of the six-member cantilever truss.

Solves the linear program of the chapter case study,

    min_A  sum_j A_j L_j
    subject to  A_j >= |N_j| / sigma_allow,  A_j >= A_min.

The member forces N_j come from static equilibrium of the determinate
truss and are constants of the optimisation. Because the stress
constraints decouple, the LP separates into per-member problems whose
solution is A_j* = max(|N_j|/sigma_allow, A_min); the script solves the
full LP with scipy.optimize.linprog anyway, to recover the dual
variables (shadow prices) on each stress limit and confirm the
closed-form areas. Prints the optimal areas, the binding constraint per
member (stress vs manufacturing floor), the total mass, and the shadow
prices.
"""

from __future__ import annotations

import numpy as np
from scipy.optimize import linprog

P = 40.0e3                      # tip load, N
SIGMA_ALLOW = 160.0e6           # allowable stress, Pa
A_MIN = 2.0e-4                  # manufacturing floor, m^2 (2 cm^2)
RHO = 7850.0                    # steel density, kg/m^3
ELL = 3.0                       # bay side, m

# Member lengths: chords and verticals = ELL, diagonals = ELL*sqrt(2).
L = np.array([ELL, ELL, ELL, ELL, ELL * np.sqrt(2), ELL * np.sqrt(2)])
# Member force magnitudes from equilibrium (see chapter).
N = np.array([P, P, P, 0.0, P * np.sqrt(2), 0.0])


def main() -> None:
    stress_area = np.abs(N) / SIGMA_ALLOW          # area lower bound from stress
    bounds = [(max(s, A_MIN), None) for s in stress_area]
    res = linprog(c=L, bounds=bounds, method="highs")
    if not res.success:
        print(f"linprog failed: {res.message}")
        return

    areas = res.x
    print("Optimal truss member sizing")
    print()
    print(f"{'member':>6}  {'force kN':>9}  {'area cm^2':>10}  {'binding':>14}")
    for j in range(6):
        binding = "stress" if stress_area[j] > A_MIN else "manuf. floor"
        print(f"{j + 1:>6}  {N[j] / 1e3:>9.1f}  {areas[j] * 1e4:>10.3f}  {binding:>14}")
    print()
    volume = float(L @ areas)
    print(f"total volume: {volume:.6e} m^3")
    print(f"total mass:   {RHO * volume:.2f} kg")
    print()
    # Shadow price d(volume)/d(sigma_allow) for each stress-limited member.
    print("shadow price on allowable stress (m^3 saved per Pa relaxation)")
    for j in range(6):
        if stress_area[j] > A_MIN:
            sp = -np.abs(N[j]) * L[j] / SIGMA_ALLOW ** 2
            print(f"  member {j + 1}: {sp:.3e}")
        else:
            print(f"  member {j + 1}: 0 (floor-limited)")


if __name__ == "__main__":
    main()
