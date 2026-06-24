"""Equilibrium branches of the bead on a rotating hoop.

For each rotation speed, lists the equilibrium angles and labels each as
stable or unstable by the sign of the second derivative of the effective
potential U_eff(theta) = m g R (1 - cos theta) - (1/2) m R^2 Omega^2
sin^2(theta). The data backs the pitchfork-bifurcation figure.

Run:
    python hoop_bifurcation.py
writes data/hoop_equilibria.csv.
"""

from __future__ import annotations
import csv
import math
from pathlib import Path

G = 9.81
R = 0.030  # 30 mm hoop, matching the chapter's estimation exercise


def effective_curvature(theta, omega):
    """Second derivative of U_eff at theta, per unit m (sign is all we need)."""
    # U_eff' = m R [ g sin th - R Omega^2 sin th cos th ]
    # U_eff'' / (m R) = g cos th - R Omega^2 cos(2 th)
    return G * math.cos(theta) - R * omega * omega * math.cos(2 * theta)


def equilibria(omega):
    """Return list of (theta_rad, stable_bool)."""
    eqs = [0.0, math.pi]
    # off-axis equilibria exist when R Omega^2 > g
    if R * omega * omega > G:
        tc = math.acos(G / (R * omega * omega))
        eqs += [tc, -tc]
    return [(th, effective_curvature(th, omega) > 0.0) for th in eqs]


def main():
    omega_crit = math.sqrt(G / R)
    out = Path(__file__).resolve().parent.parent / "data"
    out.mkdir(exist_ok=True)
    path = out / "hoop_equilibria.csv"
    with path.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["omega_rad_s", "omega_over_crit",
                    "theta_eq_deg", "stable"])
        for frac in (0.5, 0.8, 1.0, 1.2, 1.5, 2.0):
            omega = frac * omega_crit
            for th, stable in equilibria(omega):
                w.writerow([f"{omega:.4f}", f"{frac:.2f}",
                            f"{math.degrees(th):.3f}",
                            int(stable)])
    print(f"critical omega = {omega_crit:.3f} rad/s "
          f"({omega_crit * 60 / (2 * math.pi):.1f} rev/min)")
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
