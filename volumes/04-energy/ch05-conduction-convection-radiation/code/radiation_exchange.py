"""Radiative exchange: Stefan-Boltzmann, two-surface networks, and the
linearised radiation coefficient.

Section 5.4 develops the net radiative heat flow between surfaces. This module
covers the blackbody emissive power, the small-body-in-large-enclosure case,
the two-large-parallel-plates case, and the linearised coefficient used when
radiation and convection are combined at room temperature.

SI units throughout: watts, square metres, kelvin (absolute).
"""

from __future__ import annotations

SIGMA = 5.670e-8  # Stefan-Boltzmann constant, W/(m^2.K^4)


def blackbody_emissive_power(temperature):
    """Total blackbody emissive power E_b = sigma T^4 (T in kelvin)."""
    return SIGMA * temperature ** 4


def small_body_in_enclosure(emissivity, area, t_body, t_surround):
    """Net radiative heat loss from a small convex body in a large enclosure.

    q = epsilon A sigma (T_body^4 - T_surround^4), temperatures in kelvin.
    """
    return emissivity * area * SIGMA * (t_body ** 4 - t_surround ** 4)


def parallel_plates(area, eps1, eps2, t1, t2):
    """Net radiative exchange between two large parallel plates.

    q = A sigma (T1^4 - T2^4) / (1/eps1 + 1/eps2 - 1).
    """
    denom = 1.0 / eps1 + 1.0 / eps2 - 1.0
    return area * SIGMA * (t1 ** 4 - t2 ** 4) / denom


def linearised_coefficient(emissivity, t1, t2):
    """Linearised radiation coefficient h_rad = 4 eps sigma T_avg^3.

    Valid for small temperature differences; T_avg is the arithmetic mean of
    the two absolute temperatures.
    """
    t_avg = 0.5 * (t1 + t2)
    return 4.0 * emissivity * SIGMA * t_avg ** 3


def two_surface_network(area1, area2, eps1, eps2, view_factor, t1, t2):
    """General two-surface enclosure exchange with surface and space resistances.

    q = sigma (T1^4 - T2^4) / [ (1-eps1)/(eps1 A1) + 1/(A1 F12)
                                 + (1-eps2)/(eps2 A2) ].
    """
    r = ((1.0 - eps1) / (eps1 * area1)
         + 1.0 / (area1 * view_factor)
         + (1.0 - eps2) / (eps2 * area2))
    return SIGMA * (t1 ** 4 - t2 ** 4) / r


if __name__ == "__main__":
    for t in (300.0, 1000.0, 5800.0):
        print(f"E_b({t:.0f} K) = {blackbody_emissive_power(t):.3e} W/m^2")

    # Person losing heat to cold walls (the exercises): 32 C skin, 15 C walls.
    q = small_body_in_enclosure(0.95, 1.7, 305.15, 288.15)
    print(f"radiative loss from person = {q:.0f} W")

    # Linearised coefficient at room temperature.
    h_rad = linearised_coefficient(0.9, 300.0, 300.0)
    print(f"h_rad at 300 K = {h_rad:.2f} W/(m^2.K)")

    # Thermos vacuum gap: two silvered surfaces, eps = 0.05.
    q_gap = parallel_plates(0.025, 0.05, 0.05, 360.0, 295.0)
    print(f"thermos vacuum-gap radiation = {q_gap:.2f} W")
