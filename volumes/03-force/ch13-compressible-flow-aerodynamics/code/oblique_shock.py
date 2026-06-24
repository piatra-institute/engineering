"""Oblique-shock solver via the theta-beta-M relation.

For a given upstream Mach number M1 and flow deflection theta (radians),
solve for the shock angle beta on the weak branch (and optionally the
strong branch) using the relation

    tan(theta) = 2 cot(beta) (M1^2 sin^2 beta - 1)
                 / (M1^2 (gamma + cos 2beta) + 2)

The normal-shock relations are then applied to the normal Mach component
Mn1 = M1 sin(beta) to obtain downstream properties; the downstream Mach
number is M2 = Mn2 / sin(beta - theta).

Used in Volume III, Chapter 13.
"""

from __future__ import annotations

import math


def theta_from_beta(beta: float, m1: float, gamma: float = 1.4) -> float:
    """Deflection angle (rad) produced by a shock at angle beta (rad)."""
    g = gamma
    num = 2.0 / math.tan(beta) * (m1 * m1 * math.sin(beta) ** 2 - 1.0)
    den = m1 * m1 * (g + math.cos(2.0 * beta)) + 2.0
    return math.atan(num / den)


def max_deflection(m1: float, gamma: float = 1.4) -> tuple[float, float]:
    """Scan beta to find theta_max (rad) and the beta (rad) where it occurs."""
    mu = math.asin(1.0 / m1)
    best_theta, best_beta = -1.0, mu
    b = mu + 1e-4
    while b < math.radians(89.9):
        th = theta_from_beta(b, m1, gamma)
        if th > best_theta:
            best_theta, best_beta = th, b
        b += 1e-4
    return best_theta, best_beta


def solve_beta(m1: float, theta: float, gamma: float = 1.4,
               weak: bool = True) -> float:
    """Bisection for beta (rad) given M1 and deflection theta (rad)."""
    theta_max, beta_at_max = max_deflection(m1, gamma)
    if theta > theta_max:
        raise ValueError("Deflection exceeds theta_max; shock detaches")
    mu = math.asin(1.0 / m1)
    if weak:
        lo, hi = mu + 1e-6, beta_at_max
    else:
        lo, hi = beta_at_max, math.radians(89.999)
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        f = theta_from_beta(mid, m1, gamma) - theta
        f_lo = theta_from_beta(lo, m1, gamma) - theta
        if f == 0.0:
            return mid
        if (f < 0) == (f_lo < 0):
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


if __name__ == "__main__":
    m1 = 3.0
    theta = math.radians(15.0)
    beta_w = solve_beta(m1, theta, weak=True)
    beta_s = solve_beta(m1, theta, weak=False)
    print(f"M1={m1}, theta=15 deg:")
    print(f"  weak shock beta   = {math.degrees(beta_w):.2f} deg")
    print(f"  strong shock beta = {math.degrees(beta_s):.2f} deg")
    th_max, b_max = max_deflection(m1)
    print(f"  theta_max = {math.degrees(th_max):.2f} deg at beta = "
          f"{math.degrees(b_max):.2f} deg")
