# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy", "scipy"]
# ///
"""Integrate a stiff two-component ODE with explicit RK4 (at the
largest step that remains stable) and with the implicit BDF method
from scipy.integrate.solve_ivp. Report wall-clock time, step count,
and final-value accuracy.

System:  y1' = -1000 (y1 - cos t),   y2' = -y2 + y1
         y1(0) = 0,                  y2(0) = 0
Integrated on t in [0, 10].

Used by Simulation exercise 4.
"""
from __future__ import annotations

import time

import numpy as np
from scipy.integrate import solve_ivp


def f(t: float, y: np.ndarray) -> np.ndarray:
    y1, y2 = y
    return np.array([-1000.0 * (y1 - np.cos(t)), -y2 + y1])


def rk4_step(t: float, y: np.ndarray, h: float) -> np.ndarray:
    k1 = f(t, y)
    k2 = f(t + h / 2, y + (h / 2) * k1)
    k3 = f(t + h / 2, y + (h / 2) * k2)
    k4 = f(t + h, y + h * k3)
    return y + (h / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)


def main() -> None:
    t0, tf = 0.0, 10.0
    y0 = np.zeros(2)

    # Stability of RK4 on the stiff mode requires h * |lambda| <= ~2.78
    # with lambda = -1000, so h <= ~2.78e-3. Use h = 2.5e-3.
    h_rk4 = 2.5e-3
    n_steps = int((tf - t0) / h_rk4)
    t0_clock = time.perf_counter()
    y = y0.copy()
    t = t0
    for _ in range(n_steps):
        y = rk4_step(t, y, h_rk4)
        t += h_rk4
    rk4_wall = time.perf_counter() - t0_clock
    rk4_final = y.copy()

    # BDF: implicit, A-stable, takes large steps
    t0_clock = time.perf_counter()
    sol = solve_ivp(f, (t0, tf), y0, method="BDF", rtol=1e-6, atol=1e-9)
    bdf_wall = time.perf_counter() - t0_clock
    bdf_final = sol.y[:, -1]
    bdf_steps = len(sol.t) - 1

    print(f"RK4  (explicit, h = {h_rk4:.1e}): steps = {n_steps:>6}, wall = {rk4_wall*1e3:.2f} ms")
    print(f"   final y = {rk4_final}")
    print(f"BDF  (implicit, adaptive):        steps = {bdf_steps:>6}, wall = {bdf_wall*1e3:.2f} ms")
    print(f"   final y = {bdf_final}")
    print(f"final-value difference: {np.abs(rk4_final - bdf_final)}")


if __name__ == "__main__":
    main()
