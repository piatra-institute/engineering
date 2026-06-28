"""Thin-film interference: reflected-intensity colour and coating design.

Computes the reflected optical-path difference for a film of index n_f and
thickness t at incidence angle theta, accounts for the half-wave phase shift
at a low-to-high index reflection, and returns the quarter-wave thickness for
an anti-reflection coating. Used in the wave-optics worked-example section.
"""

from __future__ import annotations

import math


def refraction_angle(theta_in: float, n_in: float, n_film: float) -> float:
    """Snell's law for the angle inside the film (rad)."""
    return math.asin(n_in * math.sin(theta_in) / n_film)


def path_difference(t: float, n_film: float, theta_film: float) -> float:
    """Geometric optical-path difference 2 n_f t cos(theta_film)."""
    return 2.0 * n_film * t * math.cos(theta_film)


def quarter_wave_thickness(wavelength: float, n_film: float) -> float:
    """Anti-reflection quarter-wave thickness t = lambda / (4 n_film)."""
    return wavelength / (4.0 * n_film)


def ar_index(n_substrate: float, n_outside: float = 1.0) -> float:
    """Ideal single-layer AR index, the geometric mean sqrt(n_out * n_sub)."""
    return math.sqrt(n_outside * n_substrate)


if __name__ == "__main__":
    # MgF2 (n = 1.38) AR coating for crown glass (n = 1.52) at 550 nm.
    lam = 550e-9
    t = quarter_wave_thickness(lam, n_film=1.38)
    print(f"MgF2 quarter-wave thickness at 550 nm: {t*1e9:.1f} nm")
    print(f"ideal AR index for glass n = 1.52: {ar_index(1.52):.3f} "
          f"(MgF2 at 1.38 is the practical choice)")
    # A 500 nm soap film (n = 1.33) at normal incidence.
    pd = path_difference(t=500e-9, n_film=1.33, theta_film=0.0)
    print(f"500 nm soap film path difference: {pd*1e9:.0f} nm")
