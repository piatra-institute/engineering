"""Half-wave dipole radiation pattern, directivity, and beamwidth.

Evaluate the normalised E-plane field pattern of a centre-fed half-wave dipole,
F(theta) = cos((pi/2) cos theta) / sin theta, find its half-power beamwidth by
root-finding, and integrate the radiated power numerically to recover the peak
directivity of 1.64. The pattern is drawn in figure fig-dipole-pattern.

Angles in radians inside the routines; the demo prints degrees and dBi.
"""

from __future__ import annotations

import math


def pattern(theta: float) -> float:
    """Normalised field pattern; the value at the null poles is taken as 0."""
    s = math.sin(theta)
    if abs(s) < 1.0e-9:
        return 0.0
    return math.cos(0.5 * math.pi * math.cos(theta)) / s


def directivity(n: int = 20000) -> float:
    """Peak directivity by numerical integration of |F|^2 over the sphere.

    D = 2 |F_max|^2 / integral_0^pi |F(theta)|^2 sin theta d theta,
    with F_max = 1 at theta = pi/2 for the half-wave dipole.
    """
    total = 0.0
    dth = math.pi / n
    for i in range(1, n):
        th = i * dth
        total += pattern(th) ** 2 * math.sin(th) * dth
    return 2.0 / total


def half_power_beamwidth_deg(n: int = 200000) -> float:
    """Angular width between the two half-power (|F|^2 = 0.5) points, degrees."""
    target = 1.0 / math.sqrt(2.0)   # field at half power
    # scan from broadside (pi/2) toward the axis (0) for the first crossing
    prev = math.pi / 2.0
    for i in range(1, n):
        th = (math.pi / 2.0) * (1.0 - i / n)
        if pattern(th) < target:
            theta_hp = 0.5 * (th + prev)
            return 2.0 * math.degrees(math.pi / 2.0 - theta_hp)
        prev = th
    return float("nan")


if __name__ == "__main__":
    d = directivity()
    print(f"directivity   = {d:.3f} ({10*math.log10(d):.2f} dBi)")
    print(f"HPBW (E-plane)= {half_power_beamwidth_deg():.1f} deg")
