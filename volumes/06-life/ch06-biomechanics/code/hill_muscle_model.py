# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy>=1.26"]
# ///
"""Hill three-element muscle model: force-length, force-velocity, force-time.

The Hill model represents skeletal muscle as a contractile element
in parallel with a passive elastic element, in series with a tendon
elastic element. The contractile element's force depends on its
length (force-length, FL) and shortening velocity (force-velocity,
FV) and on the activation level a(t) (between 0 and 1).

Force is computed as:

    F_total(L, v, a) = a * F_0 * f_L(L/L_0) * f_V(v / v_max) + F_pe(L/L_0)

where f_L is the FL relation, f_V the FV relation, and F_pe the
passive parallel elastic force.

References:
  - Hill (1938). Proc. R. Soc. B 126, 136--195.
  - Zajac (1989). Muscle and tendon: properties, models, scaling, and
    application to biomechanics and motor control.
  - Winter (2009), chapter on muscle mechanics.

Run: uv run hill_muscle_model.py
"""
from __future__ import annotations
import math


def force_length(L_over_L0: float, width: float = 0.4) -> float:
    """Active force-length: Gaussian centred on L/L_0 = 1."""
    return math.exp(-((L_over_L0 - 1.0) ** 2) / (2 * (width / 2.355) ** 2))


def passive_force(L_over_L0: float, k_pe: float = 4.0) -> float:
    """Passive parallel-elastic force, normalised by F_0."""
    if L_over_L0 <= 1.0:
        return 0.0
    return k_pe * (L_over_L0 - 1.0) ** 2


def force_velocity(v_over_vmax: float, a_F0: float = 0.25, b_vmax: float = 0.25) -> float:
    """Hill force-velocity. v > 0 = shortening (concentric), v < 0 = eccentric."""
    if v_over_vmax >= 0:
        # Concentric: (F + a)(v + b) = (F_0 + a) b
        # Solve for F: F = (F_0 + a) b / (v + b) - a
        F = (1.0 + a_F0) * b_vmax / (v_over_vmax + b_vmax) - a_F0
        return max(F, 0.0)
    # Eccentric: empirical fit rising to F_ecc_max ~ 1.5 F_0
    F_ecc_max = 1.5
    k = 6.0
    return 1.0 + (F_ecc_max - 1.0) * (1.0 - math.exp(k * v_over_vmax))


def total_force(L_over_L0: float, v_over_vmax: float, activation: float = 1.0) -> float:
    """Total muscle force normalised by F_0."""
    active = activation * force_length(L_over_L0) * force_velocity(v_over_vmax)
    return active + passive_force(L_over_L0)


def calf_estimate() -> None:
    """Estimate peak gastrocnemius force during push-off."""
    # Gastrocnemius: PCSA ~ 50 cm^2, specific tension 0.3 MPa
    PCSA_cm2 = 50.0
    specific_tension_Pa = 0.3e6
    F0 = specific_tension_Pa * PCSA_cm2 * 1e-4  # N
    print(f"Gastrocnemius F_0 (isometric peak) = {F0:.0f} N")
    # During push-off the muscle is shortening at moderate velocity, ~0.3 v_max,
    # and at length near L_0.
    f_norm = total_force(1.0, 0.3, activation=0.9)
    print(f"At L/L0=1.0, v/vmax=0.3, a=0.9: F/F_0 = {f_norm:.2f}, F = {f_norm*F0:.0f} N")


def main() -> None:
    print("=== Force-length curve ===")
    for L in [0.5, 0.7, 0.85, 1.0, 1.15, 1.3, 1.5]:
        print(f"  L/L_0 = {L:.2f}: f_L = {force_length(L):.3f}, "
              f"f_pe = {passive_force(L):.3f}")
    print("\n=== Force-velocity curve ===")
    for v in [-0.5, -0.2, 0.0, 0.1, 0.3, 0.5, 0.7, 1.0]:
        print(f"  v/v_max = {v:+.2f}: f_V = {force_velocity(v):.3f}")
    print()
    calf_estimate()


if __name__ == "__main__":
    main()
