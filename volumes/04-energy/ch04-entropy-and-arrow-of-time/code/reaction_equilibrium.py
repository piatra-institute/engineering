"""Temperature dependence of a reaction equilibrium constant.

Given standard enthalpy and entropy of reaction (treated as temperature
independent over a moderate range), compute the standard Gibbs free energy,
the equilibrium constant, and the crossover temperature where the reaction
direction flips. Reproduces the water-gas-shift numbers used in the chapter.

Energies in J/mol; entropies in J/(mol K).
"""

from __future__ import annotations

import math

R = 8.314462618  # J/(mol K)


def gibbs(delta_h: float, delta_s: float, temperature: float) -> float:
    """Standard Gibbs free energy of reaction at temperature T (J/mol)."""
    return delta_h - temperature * delta_s


def equilibrium_constant(delta_h: float, delta_s: float, temperature: float) -> float:
    """Equilibrium constant K_eq = exp(-Delta G / RT)."""
    return math.exp(-gibbs(delta_h, delta_s, temperature) / (R * temperature))


def crossover_temperature(delta_h: float, delta_s: float) -> float:
    """Temperature at which Delta G = 0, i.e. T* = Delta H / Delta S.

    Returns NaN when Delta S is zero (no crossover).
    """
    if delta_s == 0.0:
        return float("nan")
    return delta_h / delta_s


def vant_hoff_slope(delta_h: float, temperature: float) -> float:
    """d ln K / dT = Delta H / (R T^2), the van't Hoff relation."""
    return delta_h / (R * temperature * temperature)


def main() -> None:
    # water-gas-shift: CO + H2O <=> CO2 + H2
    dh = -41.2e3       # J/mol
    ds = -42.1         # J/(mol K)
    for T in (298.15, 400.0, 673.15, 978.0, 1200.0):
        k = equilibrium_constant(dh, ds, T)
        g = gibbs(dh, ds, T) / 1000.0
        print(f"T={T:7.1f} K  dG={g:8.2f} kJ/mol  K_eq={k:.3e}")
    print(f"crossover T* = {crossover_temperature(dh, ds):.1f} K")


if __name__ == "__main__":
    main()
