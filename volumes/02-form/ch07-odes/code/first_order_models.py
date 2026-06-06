"""
First-order linear ODE models across domains: mixing tank, Newton
cooling, RC charge, RL current. Each is the same equation

    y' + y / tau = q / tau

with a different physical reading of y, tau, and the target value.

Supports:
  - Volume II, Chapter 7, section 7.2 (first-order linear ODEs)
  - The mixing-tank, Newton-cooling, and RL worked examples
  - The Newton-cooling forensic time-of-death worked example (7.10)

Dependencies:
  numpy

Usage:
  python first_order_models.py

Output:
  Closed-form trajectories sampled on a grid, the time constants, the
  steady states, and the forensic time-of-death inversion.
"""

import math


def first_order_step(y0: float, y_inf: float, tau: float, t: float) -> float:
    """Closed-form first-order step response: y(t) = y_inf + (y0 - y_inf) e^{-t/tau}."""
    return y_inf + (y0 - y_inf) * math.exp(-t / tau)


def mixing_tank() -> None:
    """Brine tank: V=200 L, Q=4 L/min, c_in=20 g/L, c0=5 g/L."""
    V, Q, c_in, c0 = 200.0, 4.0, 20.0, 5.0
    tau = V / Q                 # residence time, minutes
    m0 = c0 * V                 # initial salt mass, grams
    m_inf = c_in * V            # steady-state salt mass, grams
    print(f"mixing tank: tau = {tau:.1f} min, m0 = {m0:.0f} g, "
          f"m_inf = {m_inf:.0f} g")
    for t in (0.0, 25.0, 50.0, 100.0, 250.0):
        m = first_order_step(m0, m_inf, tau, t)
        print(f"  t = {t:6.1f} min   m = {m:8.1f} g   c = {m / V:6.2f} g/L")


def newton_cooling() -> None:
    """Coffee mug: m=0.3 kg, cp=4200, A=0.025 m^2, h=12 W/m^2/K, T0=90 C, Tinf=20 C."""
    m, cp, A, h = 0.30, 4200.0, 0.025, 12.0
    T0, T_inf = 90.0, 20.0
    tau = m * cp / (h * A)      # seconds
    print(f"\nnewton cooling: tau = {tau:.0f} s = {tau / 60:.1f} min")
    for minutes in (0, 10, 30, 49, 70):
        T = first_order_step(T0, T_inf, tau, minutes * 60.0)
        print(f"  t = {minutes:3d} min   T = {T:5.1f} C")


def forensic_time_of_death() -> None:
    """Two readings 1 h apart recover tau and elapsed time since death."""
    T_inf, T0 = 20.0, 37.0
    T1, T2 = 30.0, 27.0
    theta0, theta1, theta2 = T0 - T_inf, T1 - T_inf, T2 - T_inf
    tau = -1.0 / math.log(theta2 / theta1)      # hours
    t1 = -tau * math.log(theta1 / theta0)        # hours before discovery
    print(f"\nforensic: tau = {tau:.2f} h, elapsed since death = {t1:.2f} h")


if __name__ == "__main__":
    mixing_tank()
    newton_cooling()
    forensic_time_of_death()
