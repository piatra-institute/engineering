"""Predict surface strain along a cantilever beam for the chapter project.

A cantilever of length L, rectangular section b x h, modulus E, loaded by a
tip force P. Returns the bending moment, top-surface bending stress, and
predicted strain at a list of gauge positions measured from the clamp, plus
the tip deflection. The project (section 3.9) compares these predictions to
measured strain-gauge readings.

SI units throughout: metres, newtons, pascals.
"""

from __future__ import annotations


def section_inertia(b, h):
    """Second moment of area of a rectangular section about its neutral axis."""
    return b * h ** 3 / 12.0


def cantilever_predictions(L, b, h, E, P, gauge_positions):
    """Return per-gauge (x, moment, stress, strain) and the tip deflection.

    x is measured from the clamped end; the moment at x for a tip load P on a
    cantilever of length L is M(x) = P (L - x).
    """
    I = section_inertia(b, h)
    y_max = h / 2.0
    rows = []
    for x in gauge_positions:
        M = P * (L - x)
        sigma = M * y_max / I          # top-surface bending stress (Pa)
        eps = sigma / E                # predicted strain
        rows.append((x, M, sigma, eps))
    delta_tip = P * L ** 3 / (3.0 * E * I)
    return rows, delta_tip


if __name__ == "__main__":
    # Aluminium coupon: 25 mm x 3 mm, 300 mm free length, E = 69 GPa.
    L = 0.300
    b = 0.025
    h = 0.003
    E = 69e9
    P = 0.500 * 9.81          # 500 g tip load -> newtons
    gauges = [0.050, 0.150, 0.250]
    rows, delta = cantilever_predictions(L, b, h, E, P, gauges)
    print(f"tip load P = {P:.3f} N, I = {section_inertia(b,h):.3e} m^4")
    print(f"{'x (mm)':>8} {'M (N.m)':>10} {'sigma (MPa)':>12} {'strain (ue)':>12}")
    for x, M, sigma, eps in rows:
        print(f"{x*1e3:8.0f} {M:10.4f} {sigma/1e6:12.2f} {eps*1e6:12.1f}")
    print(f"predicted tip deflection = {delta*1e3:.2f} mm")
