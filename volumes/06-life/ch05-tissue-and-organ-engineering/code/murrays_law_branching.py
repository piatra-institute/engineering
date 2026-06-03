# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy>=1.26"]
# ///
"""Murray's-law branching geometry: radius ratios and angles.

Murray's law (Murray 1926) sets the diameter relation at a vascular
bifurcation by minimising the sum of metabolic maintenance cost
(proportional to volume) and Poiseuille pumping work (inversely
proportional to d^4). The resulting cubed-radius constraint:

    d_parent^3 = d_1^3 + d_2^3

For a symmetric bifurcation (d_1 = d_2 = d_d):
    d_d / d_parent = 2^(-1/3) approx 0.794

Each subsequent symmetric bifurcation reduces the diameter by the
same factor. The optimal bifurcation angle for symmetric branching
is theta ~ 37.5 degrees on each side.

Run: uv run murrays_law_branching.py
"""
from __future__ import annotations
import math


def symmetric_ratio() -> float:
    return 2.0 ** (-1.0 / 3.0)


def asymmetric_ratio(alpha: float) -> tuple[float, float]:
    """Return (d_1/d_p, d_2/d_p) when the flow split is alpha : (1 - alpha)."""
    # flow scales with d^3, so d_1^3 = alpha * d_p^3
    return alpha ** (1.0 / 3.0), (1.0 - alpha) ** (1.0 / 3.0)


def symmetric_angle() -> float:
    """Optimal half-angle (degrees) for a symmetric bifurcation."""
    # cos(2 theta) = 2^(4/3) / 2 - 1 = 2^(1/3) - 1
    cos2theta = 2.0 ** (1.0 / 3.0) - 1.0
    return 0.5 * math.degrees(math.acos(cos2theta))


def hierarchy_table(d_root: float, n_generations: int):
    ratio = symmetric_ratio()
    print(f"{'gen':>4} {'d (um)':>12} {'d/d_root':>12} {'n vessels':>12}")
    d = d_root
    for g in range(n_generations + 1):
        n = 2 ** g
        print(f"{g:>4} {d * 1e6:12.2f} {d / d_root:12.4f} {n:12d}")
        d *= ratio


def main():
    print(f"symmetric daughter/parent ratio = {symmetric_ratio():.4f}")
    print(f"symmetric optimal bifurcation half-angle = {symmetric_angle():.2f} deg")
    print()
    print("asymmetric examples (flow split alpha : 1-alpha):")
    print(f"{'alpha':>8} {'d1/d_p':>10} {'d2/d_p':>10}")
    for alpha in [0.5, 0.6, 0.7, 0.8, 0.9, 0.95]:
        r1, r2 = asymmetric_ratio(alpha)
        print(f"{alpha:8.2f} {r1:10.4f} {r2:10.4f}")
    print()
    print("hierarchy: aorta (25 mm) to capillary (8 um) requires")
    print("how many symmetric bifurcations?")
    n = 0
    d = 25e-3
    while d > 8e-6:
        n += 1
        d *= symmetric_ratio()
    print(f"  n = {n} symmetric bifurcations (lower bound; real tree mixes")
    print(f"  symmetric and asymmetric branching)")
    print()
    print("eight-generation symmetric tree from a 4 mm root:")
    hierarchy_table(d_root=4e-3, n_generations=8)


if __name__ == "__main__":
    main()
