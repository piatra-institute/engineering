"""Mohr's circle for a 2D stress state.

Given the in-plane stress components (sigma_xx, sigma_yy, sigma_xy), return the
principal stresses, the principal-axis orientation, and the maximum in-plane
shear stress. The construction is the analytic backbone of the graphical
Mohr's circle in section 3.5.

All stresses in consistent units (e.g. MPa). Angles returned in degrees.
"""

from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass
class MohrResult:
    sigma_1: float        # larger principal stress
    sigma_2: float        # smaller principal stress
    theta_p_deg: float    # orientation of sigma_1 axis, degrees CCW from x
    tau_max: float        # maximum in-plane shear stress
    center: float         # circle center on the sigma axis
    radius: float         # circle radius (= tau_max)


def mohr_circle(sigma_xx: float, sigma_yy: float, sigma_xy: float) -> MohrResult:
    center = 0.5 * (sigma_xx + sigma_yy)
    radius = math.hypot(0.5 * (sigma_xx - sigma_yy), sigma_xy)
    sigma_1 = center + radius
    sigma_2 = center - radius
    # tan(2 theta_p) = 2 sigma_xy / (sigma_xx - sigma_yy); atan2 picks the branch
    theta_p_deg = 0.5 * math.degrees(
        math.atan2(2.0 * sigma_xy, sigma_xx - sigma_yy)
    )
    return MohrResult(sigma_1, sigma_2, theta_p_deg, radius, center, radius)


def transform(sigma_xx: float, sigma_yy: float, sigma_xy: float,
              theta_deg: float) -> tuple[float, float, float]:
    """Stress components after rotating the axes CCW by theta_deg."""
    t = math.radians(theta_deg)
    avg = 0.5 * (sigma_xx + sigma_yy)
    dif = 0.5 * (sigma_xx - sigma_yy)
    c, s = math.cos(2 * t), math.sin(2 * t)
    sxx = avg + dif * c + sigma_xy * s
    syy = avg - dif * c - sigma_xy * s
    sxy = -dif * s + sigma_xy * c
    return sxx, syy, sxy


if __name__ == "__main__":
    # Three textbook checks.
    cases = [
        ("worked example", 80.0, 40.0, 30.0),   # sec 3.5 / fig mohr-circle
        ("uniaxial",       100.0, 0.0, 0.0),     # sigma_1=100, sigma_2=0, tau=50
        ("pure shear",     0.0, 0.0, 50.0),      # sigma_1=+50, sigma_2=-50
    ]
    for name, sxx, syy, sxy in cases:
        r = mohr_circle(sxx, syy, sxy)
        print(f"{name:16s}  s1={r.sigma_1:7.2f}  s2={r.sigma_2:7.2f}  "
              f"theta_p={r.theta_p_deg:6.2f} deg  tau_max={r.tau_max:7.2f}")
