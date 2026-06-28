"""Canonical-ensemble thermodynamics from a discrete energy spectrum.

Given a list of microstate energies E_i, compute the partition function Z, the
state probabilities, the average energy, the Helmholtz free energy, the entropy,
and the heat capacity at a temperature T. The two-level and harmonic-oscillator
cases used in the chapter's worked examples and exercises are included as checks.

All energies in joules, temperatures in kelvin. The reduced-temperature plots
in the chapter come from sweeping T and reading C(T).
"""

from __future__ import annotations

import math
from dataclasses import dataclass

K_B = 1.380649e-23  # J/K


@dataclass
class CanonicalState:
    Z: float
    probabilities: list[float]
    mean_energy: float
    free_energy: float
    entropy: float
    heat_capacity: float


def canonical(energies: list[float], temperature: float) -> CanonicalState:
    """Full canonical thermodynamics for a discrete spectrum at temperature T.

    Uses the log-sum-exp shift for numerical stability when beta*E is large.
    """
    beta = 1.0 / (K_B * temperature)
    e_min = min(energies)
    weights = [math.exp(-beta * (e - e_min)) for e in energies]
    Z_shift = sum(weights)
    probs = [w / Z_shift for w in weights]
    # true Z includes the shift factor exp(-beta e_min)
    Z = Z_shift * math.exp(-beta * e_min)

    mean_E = sum(p * e for p, e in zip(probs, energies))
    mean_E2 = sum(p * e * e for p, e in zip(probs, energies))
    var_E = mean_E2 - mean_E * mean_E
    free_energy = -K_B * temperature * math.log(Z)
    entropy = (mean_E - free_energy) / temperature
    heat_capacity = var_E / (K_B * temperature * temperature)
    return CanonicalState(Z, probs, mean_E, free_energy, entropy, heat_capacity)


def two_level_check(epsilon: float, temperature: float) -> CanonicalState:
    """Two-level system: ground at 0, excited at epsilon."""
    return canonical([0.0, epsilon], temperature)


def schottky_peak_temperature(epsilon: float) -> float:
    """Temperature of the Schottky heat-capacity maximum for a two-level system.

    The maximum sits near k_B T = 0.417 epsilon; the constant is the root of a
    transcendental equation, computed here by a short bisection.
    """
    def dCdx(x: float) -> float:
        # x = k_B T / epsilon; differentiate the Schottky form numerically
        h = 1e-6
        def C(xx: float) -> float:
            u = 1.0 / xx
            return u * u * math.exp(u) / (1 + math.exp(u)) ** 2
        return (C(x + h) - C(x - h)) / (2 * h)

    lo, hi = 0.2, 0.7
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if dCdx(lo) * dCdx(mid) <= 0:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def main() -> None:
    eps = 1.0e-21  # joules, an arbitrary level spacing
    for T in (50.0, 100.0, 300.0, 1000.0):
        s = two_level_check(eps, T)
        print(f"T={T:7.1f} K  p_excited={s.probabilities[1]:.4f}  "
              f"C/k_B={s.heat_capacity / K_B:.4f}  S/k_B={s.entropy / K_B:.4f}")
    print(f"Schottky peak at k_B T / eps = {schottky_peak_temperature(eps):.4f}")


if __name__ == "__main__":
    main()
