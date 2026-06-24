#!/usr/bin/env python3
"""Single-degree-of-freedom oscillator response.

Free and forced response of  m x'' + c x' + k x = F(t)  by direct
time integration (RK4), plus the closed-form steady-state amplitude and
phase of the forced response. Used to generate the free-decay and
frequency-response figures of the Vibrations chapter and to check the
hand calculations in the worked examples.

Run:  python3 sdof_response.py
"""

import numpy as np


def sdof_params(m, k, zeta):
    """Return (omega_n, c) for given mass, stiffness, damping ratio."""
    omega_n = np.sqrt(k / m)
    c = 2.0 * zeta * m * omega_n
    return omega_n, c


def rk4_free(m, c, k, x0, v0, t_end, dt):
    """Integrate the free response from (x0, v0) with RK4."""
    n = int(round(t_end / dt))
    t = np.linspace(0.0, n * dt, n + 1)
    x = np.zeros(n + 1)
    v = np.zeros(n + 1)
    x[0], v[0] = x0, v0

    def deriv(xi, vi):
        # x' = v ;  v' = -(c v + k x)/m
        return vi, -(c * vi + k * xi) / m

    for i in range(n):
        k1x, k1v = deriv(x[i], v[i])
        k2x, k2v = deriv(x[i] + 0.5 * dt * k1x, v[i] + 0.5 * dt * k1v)
        k3x, k3v = deriv(x[i] + 0.5 * dt * k2x, v[i] + 0.5 * dt * k2v)
        k4x, k4v = deriv(x[i] + dt * k3x, v[i] + dt * k3v)
        x[i + 1] = x[i] + (dt / 6.0) * (k1x + 2 * k2x + 2 * k3x + k4x)
        v[i + 1] = v[i] + (dt / 6.0) * (k1v + 2 * k2v + 2 * k3v + k4v)
    return t, x, v


def steady_state(m, c, k, F0, omega):
    """Closed-form steady-state amplitude X and phase lag phi (radians)."""
    omega_n = np.sqrt(k / m)
    zeta = c / (2.0 * m * omega_n)
    r = omega / omega_n
    denom = np.sqrt((1.0 - r ** 2) ** 2 + (2.0 * zeta * r) ** 2)
    X = (F0 / k) / denom
    phi = np.arctan2(2.0 * zeta * r, 1.0 - r ** 2)
    return X, phi


def log_decrement(peaks):
    """Logarithmic decrement from a run of successive same-sign peaks."""
    peaks = np.asarray(peaks, dtype=float)
    # delta over n cycles, averaged
    ratios = np.log(peaks[:-1] / peaks[1:])
    return float(np.mean(ratios))


def zeta_from_decrement(delta):
    """Recover the damping ratio from the logarithmic decrement."""
    return delta / np.sqrt(4.0 * np.pi ** 2 + delta ** 2)


if __name__ == "__main__":
    # Worked-example check: m = 5 kg, k = 500 N/m, zeta = 0.05.
    m, k, zeta = 5.0, 500.0, 0.05
    omega_n, c = sdof_params(m, k, zeta)
    omega_d = omega_n * np.sqrt(1.0 - zeta ** 2)
    print(f"omega_n = {omega_n:.4f} rad/s   f_n = {omega_n/(2*np.pi):.4f} Hz")
    print(f"c       = {c:.4f} N.s/m")
    print(f"omega_d = {omega_d:.4f} rad/s")

    # Forced at resonance, F0 = 50 N: amplitude should be (F0/k)/(2 zeta).
    X, phi = steady_state(m, c, k, F0=50.0, omega=omega_n)
    print(f"resonant X = {X*1e3:.3f} mm   phase = {np.degrees(phi):.1f} deg")

    # Free decay, extract zeta back from the simulated peaks.
    t, x, v = rk4_free(m, c, k, x0=0.01, v0=0.0, t_end=20.0, dt=1e-3)
    # crude peak finder: local maxima above zero
    pk = x[1:-1][(x[1:-1] > x[:-2]) & (x[1:-1] > x[2:]) & (x[1:-1] > 0)]
    delta = log_decrement(pk[:8])
    print(f"recovered delta = {delta:.4f}   zeta = {zeta_from_decrement(delta):.4f}")
