"""Diffraction and resolution calculators.

Single-slit Fraunhofer intensity, the circular-aperture Airy resolution
limit, and the diffraction-grating equation. Wavelengths and lengths in
metres unless stated; angles returned in radians. Reproduces the resolution
numbers quoted in the wave-optics section.
"""

from __future__ import annotations

import math

AIRY_FACTOR = 1.22  # first zero of J1, divided by pi, times 2


def single_slit_intensity(theta: float, a: float, wavelength: float) -> float:
    """Relative intensity I/I0 of a single slit of width a at angle theta."""
    beta = math.pi * a * math.sin(theta) / wavelength
    if abs(beta) < 1e-12:
        return 1.0
    return (math.sin(beta) / beta) ** 2


def single_slit_first_min(a: float, wavelength: float) -> float:
    """Angle of the first diffraction minimum: sin(theta) = lambda / a."""
    return math.asin(wavelength / a)


def rayleigh_limit(diameter: float, wavelength: float) -> float:
    """Angular resolution (rad) of a circular aperture, 1.22 lambda / D."""
    return AIRY_FACTOR * wavelength / diameter


def grating_orders(period: float, wavelength: float) -> list[tuple[int, float]]:
    """Return (order, angle_rad) pairs that the grating can diffract."""
    m_max = int(period / wavelength)
    out = []
    for m in range(-m_max, m_max + 1):
        s = m * wavelength / period
        if -1.0 <= s <= 1.0:
            out.append((m, math.asin(s)))
    return out


if __name__ == "__main__":
    lam = 550e-9
    theta = rayleigh_limit(diameter=0.200, wavelength=lam)
    print(f"200 mm aperture at 550 nm: {theta*1e6:.2f} urad "
          f"= {math.degrees(theta)*3600:.2f} arcsec")
    print("grating d = 1.667 um at 550 nm orders:")
    for m, ang in grating_orders(period=1.667e-6, wavelength=lam):
        print(f"  m = {m:+d}: {math.degrees(ang):6.2f} deg")
