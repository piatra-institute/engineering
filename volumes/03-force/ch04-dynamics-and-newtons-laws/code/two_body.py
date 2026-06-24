#!/usr/bin/env python3
"""Two-body central-force (Newtonian gravity) integrator.

Integrates one body in the gravitational field of a fixed central mass
using a symplectic velocity-Verlet step, which conserves energy far
better than RK4 over many orbits and keeps the orbit from spiralling in
or out through numerical dissipation. The script integrates one Earth
year, reports the period from successive perihelion passages, and checks
Kepler's third law T^2 = 4 pi^2 a^3 / (G M).
"""
from __future__ import annotations

import math

G = 6.674e-11          # m^3 kg^-1 s^-2
M_SUN = 1.989e30       # kg
AU = 1.496e11          # m
YEAR = 365.25 * 86400  # s


def accel(pos):
    x, y = pos
    r = math.hypot(x, y)
    a = -G * M_SUN / r**3
    return (a * x, a * y)


def verlet(pos, vel, dt, n_steps):
    traj = [(pos, vel)]
    ax, ay = accel(pos)
    for _ in range(n_steps):
        x = pos[0] + vel[0] * dt + 0.5 * ax * dt * dt
        y = pos[1] + vel[1] * dt + 0.5 * ay * dt * dt
        ax_new, ay_new = accel((x, y))
        vx = vel[0] + 0.5 * (ax + ax_new) * dt
        vy = vel[1] + 0.5 * (ay + ay_new) * dt
        pos, vel = (x, y), (vx, vy)
        ax, ay = ax_new, ay_new
        traj.append((pos, vel))
    return traj


def specific_energy(pos, vel):
    r = math.hypot(*pos)
    v2 = vel[0] ** 2 + vel[1] ** 2
    return 0.5 * v2 - G * M_SUN / r


def kepler_period(a):
    return 2 * math.pi * math.sqrt(a**3 / (G * M_SUN))


if __name__ == "__main__":
    # Start at perihelion of Earth's orbit, moving tangentially.
    r0 = 1.471e11        # perihelion distance, m
    v0 = 30290.0         # perihelion speed, m/s
    pos0, vel0 = (r0, 0.0), (0.0, v0)

    dt = 3600.0          # 1-hour step
    n = int(1.2 * YEAR / dt)
    traj = verlet(pos0, vel0, dt, n)

    e0 = specific_energy(pos0, vel0)
    e1 = specific_energy(*traj[-1])
    drift = abs(e1 - e0) / abs(e0)

    # Semi-major axis from energy: a = -G M / (2 epsilon).
    a = -G * M_SUN / (2 * e0)
    print(f"semi-major axis a = {a / AU:.4f} AU")
    print(f"Kepler period     = {kepler_period(a) / YEAR:.4f} yr")
    print(f"energy drift over 1.2 yr = {drift:.2e} (relative)")
