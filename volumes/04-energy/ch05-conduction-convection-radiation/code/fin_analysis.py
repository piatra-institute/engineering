"""Straight-fin temperature distribution, heat rate, and efficiency.

A rectangular straight fin of length L, cross-section A_c, perimeter P, made of
a material of conductivity k, with a uniform convection coefficient h on its
surface and an insulated tip. Section 5.5 gives the governing parameter
m = sqrt(h P / (k A_c)) and the dimensionless group mL that decides whether a
fin earns its material.

SI units throughout: metres, watts, kelvin.
"""

from __future__ import annotations

import math


def fin_parameter(h, perimeter, k, area_c):
    """m = sqrt(h P / (k A_c)), the inverse decay length of the fin."""
    return math.sqrt(h * perimeter / (k * area_c))


def fin_tip_excess(theta_base, m, length):
    """Tip excess temperature for an insulated-tip fin: theta_b / cosh(mL)."""
    return theta_base / math.cosh(m * length)


def fin_heat_rate(h, perimeter, k, area_c, theta_base, length):
    """Heat dissipated by an insulated-tip fin.

    q_fin = sqrt(h P k A_c) * theta_base * tanh(mL).
    """
    m = fin_parameter(h, perimeter, k, area_c)
    return math.sqrt(h * perimeter * k * area_c) * theta_base * math.tanh(m * length)


def fin_efficiency(h, perimeter, k, area_c, length):
    """Fin efficiency: actual heat rate over the rate if the whole fin sat at
    the base temperature. For an insulated-tip fin this is tanh(mL)/(mL).
    """
    m = fin_parameter(h, perimeter, k, area_c)
    return math.tanh(m * length) / (m * length)


def fin_temperature_profile(theta_base, m, length, n=21):
    """Excess temperature along the fin, insulated tip.

    Returns (x, theta) pairs, theta = theta_b cosh(m(L-x)) / cosh(mL).
    """
    pts = []
    for i in range(n):
        x = length * i / (n - 1)
        theta = theta_base * math.cosh(m * (length - x)) / math.cosh(m * length)
        pts.append((x, theta))
    return pts


if __name__ == "__main__":
    # Aluminium fin from the exercises: 50 mm long, 1 mm x 10 mm section.
    k = 237.0
    h = 20.0
    width, thick = 0.010, 0.001
    area_c = width * thick
    perimeter = 2.0 * (width + thick)
    length = 0.050
    theta_b = 60.0  # 80 C base, 20 C air

    m = fin_parameter(h, perimeter, k, area_c)
    print(f"m = {m:.2f} 1/m, mL = {m * length:.3f}")
    print(f"tip excess = {fin_tip_excess(theta_b, m, length):.1f} K")
    print(f"heat rate = {fin_heat_rate(h, perimeter, k, area_c, theta_b, length):.2f} W")
    print(f"efficiency = {fin_efficiency(h, perimeter, k, area_c, length):.3f}")
