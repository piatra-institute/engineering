"""Transient simulation of a series RLC circuit by trapezoidal integration.

State variables are the capacitor voltage v_C and the inductor current i_L,
the two energy-storage quantities that cannot change instantaneously. The
state-space form is

    dv_C/dt = i_L / C
    di_L/dt = (V_s - R i_L - v_C) / L

integrated with the trapezoidal rule, which is A-stable and second-order
accurate. The analytical step response is included for comparison so the
reader can watch the truncation error grow with step size.

Units: ohms, henries, farads, volts, seconds.
"""

from __future__ import annotations

import math

import numpy as np


def step_response_numeric(R, L, C, Vs, t_end, dt):
    """Trapezoidal-rule integration of the series RLC step response."""
    n = int(round(t_end / dt))
    t = np.linspace(0.0, n * dt, n + 1)
    vC = np.zeros(n + 1)
    iL = np.zeros(n + 1)
    # trapezoidal update solves a 2x2 linear system each step
    a = dt / (2.0 * C)
    b = dt / (2.0 * L)
    for k in range(n):
        # implicit system for (vC[k+1], iL[k+1])
        # vC1 - a iL1 = vC0 + a iL0
        # iL1 + b R iL1 + b vC1 = iL0 + b(Vs - R iL0 - vC0) + b Vs ... assemble:
        rhs1 = vC[k] + a * iL[k]
        rhs2 = iL[k] + b * (Vs - R * iL[k] - vC[k]) + b * Vs
        M = np.array([[1.0, -a], [b, 1.0 + b * R]])
        rhs = np.array([rhs1, rhs2])
        vC[k + 1], iL[k + 1] = np.linalg.solve(M, rhs)
    return t, vC, iL


def step_response_analytic(R, L, C, Vs, t):
    """Closed-form capacitor-voltage step response, all damping regimes."""
    wn = 1.0 / math.sqrt(L * C)
    zeta = (R / 2.0) * math.sqrt(C / L)
    t = np.asarray(t, dtype=float)
    if zeta < 1.0:
        wd = wn * math.sqrt(1.0 - zeta * zeta)
        phi = math.acos(zeta)
        env = np.exp(-zeta * wn * t) / math.sqrt(1.0 - zeta * zeta)
        return Vs * (1.0 - env * np.sin(wd * t + phi))
    if abs(zeta - 1.0) < 1e-12:
        return Vs * (1.0 - (1.0 + wn * t) * np.exp(-wn * t))
    s1 = -wn * (zeta - math.sqrt(zeta * zeta - 1.0))
    s2 = -wn * (zeta + math.sqrt(zeta * zeta - 1.0))
    return Vs * (1.0 - (s2 * np.exp(s1 * t) - s1 * np.exp(s2 * t)) / (s2 - s1))


if __name__ == "__main__":
    R, L, C, Vs = 10.0, 1e-3, 1e-7, 5.0
    wn = 1.0 / math.sqrt(L * C)
    t, vC, _ = step_response_numeric(R, L, C, Vs, t_end=6.0 / (0.5 * wn), dt=1e-7)
    va = step_response_analytic(R, L, C, Vs, t)
    err = np.max(np.abs(vC - va))
    print(f"omega_n = {wn:.3e} rad/s, max abs error = {err:.3e} V")
