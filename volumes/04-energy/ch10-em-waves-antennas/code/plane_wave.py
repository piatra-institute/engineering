"""Plane-wave field relations and energy transport in a linear medium.

Given the peak electric-field amplitude of a sinusoidal plane wave, return the
peak magnetic-field amplitude, the wave impedance, the time-averaged Poynting
flux (intensity), the time-averaged energy density, and the radiation pressure
on a perfectly absorbing and on a perfectly reflecting surface. The relations
are the working content of section 10.2.

SI units throughout: E0 in V/m, results in tesla, ohm, W/m^2, J/m^3, Pa.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

MU0 = 4.0e-7 * math.pi            # vacuum permeability, H/m
C0 = 299_792_458.0                # speed of light in vacuum, m/s
EPS0 = 1.0 / (MU0 * C0 * C0)      # vacuum permittivity, F/m


@dataclass
class PlaneWave:
    B0: float           # peak magnetic field, tesla
    impedance: float    # wave impedance eta, ohm
    intensity: float    # time-averaged Poynting flux, W/m^2
    energy_density: float   # time-averaged energy density, J/m^3
    pressure_absorb: float  # radiation pressure, absorbing surface, Pa
    pressure_reflect: float # radiation pressure, reflecting surface, Pa


def plane_wave(E0: float, eps_r: float = 1.0, mu_r: float = 1.0) -> PlaneWave:
    eps = eps_r * EPS0
    mu = mu_r * MU0
    v = 1.0 / math.sqrt(mu * eps)          # phase speed in the medium
    eta = math.sqrt(mu / eps)              # wave impedance
    B0 = E0 / v
    intensity = 0.5 * E0 * E0 / eta        # <S> = E0^2 / (2 eta)
    energy_density = 0.5 * eps * E0 * E0    # equal split E and B; sum = eps E0^2 / 2
    pressure_absorb = intensity / v
    pressure_reflect = 2.0 * intensity / v
    return PlaneWave(B0, eta, intensity, energy_density,
                     pressure_absorb, pressure_reflect)


if __name__ == "__main__":
    w = plane_wave(500.0)   # exercise 1: 500 V/m in vacuum
    print(f"B0           = {w.B0:.3e} T")
    print(f"eta          = {w.impedance:.1f} ohm")
    print(f"intensity    = {w.intensity:.1f} W/m^2")
    print(f"u (avg)      = {w.energy_density:.3e} J/m^3")
    print(f"P (absorb)   = {w.pressure_absorb:.3e} Pa")
    print(f"P (reflect)  = {w.pressure_reflect:.3e} Pa")
