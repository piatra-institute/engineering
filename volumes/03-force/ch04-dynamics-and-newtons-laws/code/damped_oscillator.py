#!/usr/bin/env python3
"""Free response of a damped harmonic oscillator m x'' + c x' + k x = 0
in the three damping regimes (underdamped, critical, overdamped).

Uses the closed-form solutions rather than numerical integration so that
the regime boundaries are exact. Writes a sampled table for plotting.
"""
from __future__ import annotations

import math

M = 1.0       # kg
K = 100.0     # N/m
W0 = math.sqrt(K / M)   # undamped natural angular frequency


def response(t, zeta, x0=1.0, v0=0.0):
    """Displacement at time t for damping ratio zeta, x(0)=x0, x'(0)=v0."""
    if zeta < 1.0:                      # underdamped
        wd = W0 * math.sqrt(1.0 - zeta**2)
        a = x0
        b = (v0 + zeta * W0 * x0) / wd
        return math.exp(-zeta * W0 * t) * (a * math.cos(wd * t) + b * math.sin(wd * t))
    if abs(zeta - 1.0) < 1e-12:         # critically damped
        return (x0 + (v0 + W0 * x0) * t) * math.exp(-W0 * t)
    # overdamped
    s = W0 * math.sqrt(zeta**2 - 1.0)
    l1, l2 = -zeta * W0 + s, -zeta * W0 - s
    a = (v0 - l2 * x0) / (l1 - l2)
    b = x0 - a
    return a * math.exp(l1 * t) + b * math.exp(l2 * t)


def settling_time(zeta, tol=0.02, t_max=10.0, dt=1e-3):
    """Time after which |x| stays below tol (2% band) of the initial value."""
    t, last_out = 0.0, 0.0
    while t < t_max:
        if abs(response(t, zeta)) > tol:
            last_out = t
        t += dt
    return last_out


if __name__ == "__main__":
    print(f"natural frequency omega_0 = {W0:.3f} rad/s")
    print(f"{'zeta':>6} {'regime':>14} {'2% settle/s':>12}")
    for zeta, name in ((0.1, "underdamped"), (1.0, "critical"), (2.0, "overdamped")):
        print(f"{zeta:6.1f} {name:>14} {settling_time(zeta):12.3f}")
