"""
Paris-Erdogan crack-growth integrator for the Bjork-Shiley
convexo-concave (BSCC) outlet-strut weld toe.

Vol VI Ch 12 sec 12.7; Failure-analysis exercises.

Mechanics:
- Cyclic bending stress at the weld toe, amplitude depends on
  valve size (chord radius) and opening angle.
- Stress intensity range Delta K = Y * Delta sigma * sqrt(pi * a)
  with geometric factor Y = 1.12 for an edge-cracked plate.
- Paris-Erdogan: da/dN = C (Delta K)^m, with C and m for Haynes-25
  (cobalt-chromium-tungsten) from the literature.
- Integrate cycle-by-cycle from initial flaw size a0 to fracture
  critical size a_c, where K = K_IC.

The model reproduces the qualitative size-dependence of the
fracture rate observed by Blot et al. (2005): larger valves with
70-degree opening angle have higher cyclic stress, smaller a_c
relative to strut leg, and shorter fatigue life.

References:
- paper:v6c12-paris-erdogan-1963
- paper:v6c12-vanderlugt-strut-fracture-1993
- paper:v6c12-blot-bjork-shiley-2005
"""

from __future__ import annotations
import math


# Material parameters (Haynes-25 / L-605), illustrative values from
# the literature; carry one significant figure.
C_PARIS = 1.5e-12             # m/cycle / (MPa sqrt(m))^m
M_PARIS = 3.2                 # exponent
K_IC = 60.0                   # MPa sqrt(m), fracture toughness

# Geometric factor for an edge crack at a weld toe; standard value.
Y_GEOM = 1.12


def stress_amplitude_mpa(valve_size_mm: float,
                         opening_angle_deg: float) -> float:
    """
    Heuristic stress-amplitude estimator: larger valves and larger
    opening angles produce a larger moment arm and therefore higher
    cyclic stress at the outlet-strut weld toe.

    This is not the Shiley engineering analysis; it is an
    order-of-magnitude reconstruction used for the pedagogical
    crack-growth integration.
    """
    base = 80.0    # MPa; nominal cyclic amplitude at 27 mm, 60 deg
    size_factor = (valve_size_mm / 27.0) ** 1.5
    angle_factor = 1.0 + 0.6 * (opening_angle_deg - 60.0) / 10.0
    return base * size_factor * angle_factor


def critical_crack_length_m(stress_amp_mpa: float) -> float:
    """K_IC = Y * sigma * sqrt(pi * a_c) gives a_c."""
    return (K_IC / (Y_GEOM * stress_amp_mpa)) ** 2 / math.pi


def cycles_to_failure(a0_m: float, stress_amp_mpa: float,
                       da_max_m: float = 1e-7) -> int:
    """
    Cycle-by-cycle Paris-Erdogan integration from initial flaw a0
    to critical a_c. Returns the cycle count.
    """
    a = a0_m
    N = 0
    a_c = critical_crack_length_m(stress_amp_mpa)
    while a < a_c:
        dK = Y_GEOM * stress_amp_mpa * math.sqrt(math.pi * a)
        da_dN = C_PARIS * (dK ** M_PARIS)
        # Adaptive step: cap delta a at da_max
        step = max(1, int(min(da_max_m / da_dN, 1e6)))
        a += da_dN * step
        N += step
        if N > 1e12:
            break
    return N


def fracture_rate_per_year(a0_m: float, stress_amp_mpa: float,
                            cycles_per_year: float = 36e6) -> float:
    """Hazard rate, cycles_to_failure inverted to per-year."""
    Nf = cycles_to_failure(a0_m, stress_amp_mpa)
    return cycles_per_year / Nf if Nf > 0 else float("inf")


def main() -> None:
    a0 = 50e-6      # 50 micrometre initial flaw at weld toe
    cycles_per_year = 36e6   # ~70 bpm

    print(f"{'size(mm)':>10} {'angle(deg)':>12} {'sigma(MPa)':>12} "
          f"{'a_c(mm)':>10} {'Nf':>14} {'hazard/yr':>12}")
    for size in (23, 25, 27, 29, 31, 33):
        for angle in (60, 70):
            sigma = stress_amplitude_mpa(size, angle)
            a_c = critical_crack_length_m(sigma)
            Nf = cycles_to_failure(a0, sigma)
            haz = cycles_per_year / Nf if Nf > 0 else float("inf")
            print(f"{size:>10} {angle:>12} {sigma:>12.1f} "
                  f"{a_c * 1e3:>10.3f} {Nf:>14d} {haz:>12.4f}")


if __name__ == "__main__":
    main()
