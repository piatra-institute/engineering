"""Sensitivity propagation for the beam-deflection model.

Computes relative sensitivities S_i = (theta_i / y) dy/dtheta_i for
y_max = 5 w L^4 / (384 E I), both analytically (closed-form derivatives)
and by finite difference (1% perturbation). Propagates the parameter
intervals to a prediction interval and produces the tornado-diagram
data for figure 18.6.

Dependencies: numpy.

Run:
    python sensitivity_propagation.py
"""
from __future__ import annotations

import numpy as np


def y_max(w, L, E, I):
    return 5.0 * w * L ** 4 / (384.0 * E * I)


def analytic_sensitivities(w, L, E, I):
    """Closed-form relative sensitivities."""
    y = y_max(w, L, E, I)
    # dy/dw * w/y = 1
    S_w = 1.0
    # dy/dL * L/y = 4
    S_L = 4.0
    # dy/dE * E/y = -1
    S_E = -1.0
    # dy/dI * I/y = -1
    S_I = -1.0
    return {"w": S_w, "L": S_L, "E": S_E, "I": S_I}


def finite_diff_sensitivities(w, L, E, I, frac=0.01):
    """Relative sensitivities by symmetric finite difference."""
    y0 = y_max(w, L, E, I)
    S = {}
    for name, param in [("w", w), ("L", L), ("E", E), ("I", I)]:
        d = frac * param
        kwargs_p = dict(w=w, L=L, E=E, I=I)
        kwargs_m = dict(w=w, L=L, E=E, I=I)
        kwargs_p[name] = param + d
        kwargs_m[name] = param - d
        dy = y_max(**kwargs_p) - y_max(**kwargs_m)
        S[name] = (param / y0) * dy / (2 * d)
    return S


def main() -> None:
    # Nominal values (SI, illustrative simply supported beam)
    w_nom = 2000.0  # N/m
    L_nom = 5.0  # m
    E_nom = 200e9  # Pa (steel)
    I_nom = 8.5e-6  # m^4

    y0 = y_max(w_nom, L_nom, E_nom, I_nom)
    print(f"Nominal y_max = {y0*1000:.2f} mm")

    S_an = analytic_sensitivities(w_nom, L_nom, E_nom, I_nom)
    S_fd = finite_diff_sensitivities(w_nom, L_nom, E_nom, I_nom)

    print("\nRelative sensitivities (analytic vs finite difference):")
    print(f"  {'param':5s}  {'analytic':10s}  {'finite diff':12s}")
    for name in ("w", "L", "E", "I"):
        print(f"  {name:5s}  {S_an[name]:+10.4f}  {S_fd[name]:+12.4f}")

    # Parameter intervals (relative, half-width)
    intervals = {"w": 0.05, "L": 0.005, "E": 0.08, "I": 0.03}
    print("\nContribution to relative prediction interval (|S_i| * sigma_i):")
    contribs = {}
    for name in ("w", "L", "E", "I"):
        c = abs(S_an[name]) * intervals[name]
        contribs[name] = c
        print(f"  {name}: |{S_an[name]:+.2f}| x {intervals[name]*100:.1f}% "
              f"= {c*100:.2f}%")
    rss = np.sqrt(sum(c ** 2 for c in contribs.values()))
    print(f"\nTotal (RSS) relative interval on y_max: +/- {rss*100:.2f}%")
    ranked = sorted(contribs.items(), key=lambda kv: -kv[1])
    print(f"Dominant contributor: {ranked[0][0]} ({ranked[0][1]*100:.1f}%);")
    print(f"highest-yield reduction target: tighten {ranked[0][0]}.")


if __name__ == "__main__":
    main()
