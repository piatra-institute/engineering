"""Transmission-line impedance, reflection, and standing-wave quantities.

Routines for the daily arithmetic of section 10.4: reflection coefficient from
a load, VSWR from the reflection coefficient, reflected and delivered power
fractions, and the input impedance of a lossless line of given electrical
length. Complex impedances are handled throughout.

Impedances in ohm, lengths and wavelengths in the same units, results
dimensionless except where noted.
"""

from __future__ import annotations

import cmath
import math


def reflection_coefficient(z_load: complex, z0: float = 50.0) -> complex:
    """Voltage reflection coefficient Gamma at the load."""
    return (z_load - z0) / (z_load + z0)


def vswr(gamma: complex) -> float:
    """Voltage standing wave ratio from the reflection coefficient."""
    g = abs(gamma)
    if g >= 1.0:
        return math.inf
    return (1.0 + g) / (1.0 - g)


def reflected_power_fraction(gamma: complex) -> float:
    """Fraction of incident power reflected, |Gamma|^2."""
    return abs(gamma) ** 2


def delivered_power_fraction(gamma: complex) -> float:
    """Fraction of incident power delivered to the load, 1 - |Gamma|^2."""
    return 1.0 - abs(gamma) ** 2


def input_impedance(z_load: complex, length_over_lambda: float,
                    z0: float = 50.0) -> complex:
    """Input impedance of a lossless line, length in wavelengths."""
    beta_l = 2.0 * math.pi * length_over_lambda
    t = cmath.tan(beta_l)
    return z0 * (z_load + 1j * z0 * t) / (z0 + 1j * z_load * t)


def return_loss_db(gamma: complex) -> float:
    """Return loss in dB, -20 log10 |Gamma| (positive number)."""
    g = abs(gamma)
    if g == 0.0:
        return math.inf
    return -20.0 * math.log10(g)


if __name__ == "__main__":
    # exercise 4: 50-ohm line into a 75-ohm load
    g = reflection_coefficient(75.0, 50.0)
    print(f"|Gamma|        = {abs(g):.4f}")
    print(f"VSWR           = {vswr(g):.3f}")
    print(f"reflected      = {100*reflected_power_fraction(g):.2f} %")
    print(f"delivered      = {100*delivered_power_fraction(g):.2f} %")
    print(f"return loss    = {return_loss_db(g):.2f} dB")
    # quarter-wave transformer check: Zin = Z0^2 / ZL at length lambda/4
    print(f"Zin (lambda/4) = {input_impedance(75.0, 0.25, 50.0):.2f} ohm")
