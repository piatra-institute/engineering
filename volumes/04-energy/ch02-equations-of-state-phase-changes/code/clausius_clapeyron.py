#!/usr/bin/env python3
"""Clausius-Clapeyron saturation-pressure correlation.

The integrated Clausius-Clapeyron equation, under the approximations that
the vapour is an ideal gas and that v_g >> v_f, gives

    ln(p2 / p1) = -(h_fg / R_s) * (1/T2 - 1/T1),

a two-point correlation that predicts the saturation pressure at one
temperature from its value at another. The routine also fits a straight
line to a set of (T, p_sat) points in the ln(p) versus 1/T plane and
recovers h_fg from the slope.
"""

import math


def p_sat_two_point(T2, T1, p1, h_fg, R_s):
    """Saturation pressure at T2 from the value p1 at T1 [SI: K, Pa, J/kg]."""
    return p1 * math.exp(-(h_fg / R_s) * (1.0 / T2 - 1.0 / T1))


def fit_latent_heat(T_list, p_list, R_s):
    """Least-squares slope of ln(p) vs 1/T; returns h_fg = -slope * R_s."""
    x = [1.0 / T for T in T_list]
    y = [math.log(p) for p in p_list]
    n = len(x)
    xbar = sum(x) / n
    ybar = sum(y) / n
    sxx = sum((xi - xbar) ** 2 for xi in x)
    sxy = sum((xi - xbar) * (yi - ybar) for xi, yi in zip(x, y))
    slope = sxy / sxx
    return -slope * R_s


if __name__ == "__main__":
    R_s_water = 461.5  # J/(kg K) for steam
    h_fg_100 = 2257e3  # J/kg at 100 C

    # predict p_sat at 150 C from the 100 C anchor
    p150 = p_sat_two_point(423.15, 373.15, 101.325e3, h_fg_100, R_s_water)
    print(f"CC prediction p_sat(150 C) = {p150/1e3:.1f} kPa "
          f"(steam table ~ 476 kPa)")

    # recover h_fg from a small data set
    T = [373.15, 423.15, 473.15, 523.15]
    p = [101.3e3, 476.2e3, 1555e3, 3976e3]
    h_fg = fit_latent_heat(T, p, R_s_water)
    print(f"fitted h_fg = {h_fg/1e3:.0f} kJ/kg "
          f"(effective average over the range)")
