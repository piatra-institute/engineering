#!/usr/bin/env python3
"""Projectile trajectory under three force models: no drag, linear drag,
quadratic drag. Integrates the planar equations of motion with RK4 and
writes a comparison table.

Equations (per unit mass, with drag coefficients folded into k):
    no drag:        a = (0, -g)
    linear drag:    a = (0, -g) - (k_lin/m) * v
    quadratic drag: a = (0, -g) - (k_quad/m) * |v| * v

The quadratic model is the correct one for a sports ball in air at
Reynolds numbers of order 1e4 to 1e5; linear drag is shown only to make
the contrast with the creeping-flow regime explicit.
"""
from __future__ import annotations

import math

G = 9.81          # m/s^2
M = 0.057         # kg, a tennis ball
K_LIN = 0.02      # N.s/m, illustrative linear-drag constant
K_QUAD = 0.0013   # N.s^2/m^2, ~ 0.5 rho Cd A for a tennis ball


def accel(state, model):
    """Return (ax, ay) for the chosen drag model. state = (x, y, vx, vy)."""
    _, _, vx, vy = state
    speed = math.hypot(vx, vy)
    if model == "none":
        return 0.0, -G
    if model == "linear":
        return -(K_LIN / M) * vx, -G - (K_LIN / M) * vy
    if model == "quadratic":
        return -(K_QUAD / M) * speed * vx, -G - (K_QUAD / M) * speed * vy
    raise ValueError(f"unknown model: {model}")


def rk4_step(state, dt, model):
    def deriv(s):
        _, _, vx, vy = s
        ax, ay = accel(s, model)
        return (vx, vy, ax, ay)

    def add(s, k, scale):
        return tuple(si + scale * ki for si, ki in zip(s, k))

    k1 = deriv(state)
    k2 = deriv(add(state, k1, dt / 2))
    k3 = deriv(add(state, k2, dt / 2))
    k4 = deriv(add(state, k3, dt))
    return tuple(
        s + (dt / 6) * (a + 2 * b + 2 * c + d)
        for s, a, b, c, d in zip(state, k1, k2, k3, k4)
    )


def simulate(v0, theta_deg, model, dt=0.001):
    """Integrate until the projectile returns to the ground (y <= 0)."""
    th = math.radians(theta_deg)
    state = (0.0, 0.0, v0 * math.cos(th), v0 * math.sin(th))
    traj = [state]
    while True:
        nxt = rk4_step(state, dt, model)
        if nxt[1] <= 0.0 and nxt[3] < 0.0:
            traj.append(nxt)
            break
        state = nxt
        traj.append(state)
    return traj


def summary(traj):
    xs = [s[0] for s in traj]
    ys = [s[1] for s in traj]
    rng = xs[-1]
    apex = max(ys)
    tof = (len(traj) - 1) * 0.001
    return rng, apex, tof


if __name__ == "__main__":
    print(f"{'model':>10} {'range/m':>9} {'apex/m':>8} {'time/s':>8}")
    for model in ("none", "linear", "quadratic"):
        traj = simulate(v0=30.0, theta_deg=45.0, model=model)
        rng, apex, tof = summary(traj)
        print(f"{model:>10} {rng:9.2f} {apex:8.2f} {tof:8.3f}")
