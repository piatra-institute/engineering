"""Manometer path-tracing helper for the configurations in Section 10.3.

The discipline of manometry is to trace the hydrostatic path from one
terminal of the instrument to the other, adding rho*g*dz on every
descent and subtracting it on every rise. This helper does the tracing
for the three standard configurations and verifies the reductions used
in the chapter. Run with:

    uv run volumes/03-force/ch10-fluid-statics/code/manometer.py
"""

G = 9.81
RHO_HG = 13600.0     # mercury
RHO_WATER = 1000.0
RHO_AIR = 1.2


def open_utube_gauge(delta_h, rho_manom=RHO_HG, rho_fluid=RHO_AIR):
    """Gauge pressure (Pa) at the connection, neglecting nothing: the light
    process column is carried explicitly so the approximation can be judged."""
    return (rho_manom - rho_fluid) * G * delta_h


def differential(delta_h, rho_manom=RHO_HG, rho_process=RHO_WATER):
    """Pressure difference p1 - p2 (Pa) across a differential manometer."""
    return (rho_manom - rho_process) * G * delta_h


def inclined_gain(theta_deg):
    """Displacement amplification of an inclined leg versus a vertical one."""
    import math
    return 1.0 / math.sin(math.radians(theta_deg))


if __name__ == "__main__":
    # 120 mm mercury reading, open-end, gas line (rho ~ air)
    p = open_utube_gauge(0.120)
    print(f"Open U-tube, 120 mm Hg: p_gauge = {p:.0f} Pa = {p/1000:.2f} kPa")
    p_approx = RHO_HG * G * 0.120
    print(f"  neglecting the gas column gives {p_approx/1000:.2f} kPa "
          f"(error {100*(p_approx-p)/p:.3f} %)")

    dp = differential(0.050)
    print(f"\nDifferential, 50 mm Hg over water: dp = {dp/1000:.2f} kPa")

    print(f"\nInclined manometer at 5 deg amplifies by {inclined_gain(5):.1f}x")
