"""
Combined-uncertainty calculation for a multi-link traceability chain.

Demonstrates the quadrature-combination rule for independent
uncertainties and identifies the chain configuration in which one
link dominates the total.

Supports Volume I, Chapter 3, Simulation exercise on chain
uncertainties.

Dependencies:
  numpy

Usage:
  python chain_uncertainty.py
"""

import math


def combined_uncertainty(uncertainties: list[float]) -> float:
    """Quadrature combination of independent standard uncertainties."""
    return math.sqrt(sum(u * u for u in uncertainties))


def fraction_from_dominant(uncertainties: list[float]) -> float:
    """Fraction of u_c^2 contributed by the largest link."""
    u_max2 = max(u * u for u in uncertainties)
    u_c2 = sum(u * u for u in uncertainties)
    return u_max2 / u_c2


def main() -> None:
    cases = {
        "equal links (5 x 0.5)": [0.5] * 5,
        "one dominant (2.0, 0.1, 0.1, 0.1, 0.1)": [2.0, 0.1, 0.1, 0.1, 0.1],
        "two moderate, three small (1.0, 1.0, 0.2, 0.2, 0.2)":
            [1.0, 1.0, 0.2, 0.2, 0.2],
        "two strong, three negligible (1.5, 1.5, 0.05, 0.05, 0.05)":
            [1.5, 1.5, 0.05, 0.05, 0.05],
    }

    print(f"{'configuration':<55} {'u_c':>8} {'dominant frac':>14}")
    print("-" * 80)
    for name, links in cases.items():
        u_c = combined_uncertainty(links)
        frac = fraction_from_dominant(links)
        print(f"{name:<55} {u_c:8.4f} {frac:14.4f}")


if __name__ == "__main__":
    main()
