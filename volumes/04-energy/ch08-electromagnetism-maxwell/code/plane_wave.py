"""Plane electromagnetic wave: field amplitudes, energy density, and the
time-averaged Poynting vector.

Given an irradiance (intensity) in W/m^2 this recovers the peak electric
and magnetic field amplitudes for a plane wave in vacuum, and conversely.
Used in Section 8.6 and the calculation exercise on solar irradiance.
"""

import numpy as np

EPS0 = 8.8541878128e-12   # F/m
MU0 = 4.0e-7 * np.pi      # H/m
C = 1.0 / np.sqrt(EPS0 * MU0)  # m/s


def fields_from_intensity(intensity):
    """Peak E and B from time-averaged intensity <S> = 0.5 eps0 c E0^2."""
    e0 = np.sqrt(2.0 * intensity / (EPS0 * C))
    b0 = e0 / C
    return e0, b0


def intensity_from_e0(e0):
    return 0.5 * EPS0 * C * e0 ** 2


def energy_density(e0):
    """Time-averaged total energy density for a plane wave (ue = um)."""
    ue = 0.25 * EPS0 * e0 ** 2  # time average of 0.5 eps0 E^2
    return 2.0 * ue


def radiation_pressure_absorbing(intensity):
    return intensity / C


if __name__ == "__main__":
    for name, S in [("solar constant (top of atmosphere)", 1361.0),
                    ("clear-day surface", 1000.0)]:
        e0, b0 = fields_from_intensity(S)
        print(f"{name}: S = {S:.0f} W/m^2")
        print(f"  peak E0 = {e0:7.1f} V/m, peak B0 = {b0*1e9:7.2f} nT")
        print(f"  energy density <u> = {energy_density(e0)*1e6:.3f} uJ/m^3")
        print(f"  radiation pressure (absorbing) = "
              f"{radiation_pressure_absorbing(S)*1e6:.3f} uPa")
