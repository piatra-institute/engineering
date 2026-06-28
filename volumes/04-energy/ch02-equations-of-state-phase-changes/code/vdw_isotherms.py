#!/usr/bin/env python3
"""Plot reduced van der Waals isotherms and locate the coexistence line.

The reduced van der Waals equation is

    p_r = 8 T_r / (3 v_r - 1) - 3 / v_r**2,

which depends on no substance constants once pressure, volume, and
temperature are scaled by their critical values. Below T_r = 1 the
isotherm develops a non-monotonic loop; the Maxwell equal-area
construction finds the saturation pressure p_sat by requiring that the
two lobes the horizontal coexistence line cuts from the loop have equal
area, equivalently that the integral of p dv between the two roots equals
p_sat (v_g - v_f).

Requires numpy. Plotting is optional (matplotlib).
"""

import numpy as np

try:
    from numpy import trapezoid as _trap
except ImportError:  # older numpy
    from numpy import trapz as _trap


def p_reduced(v_r, T_r):
    return 8.0 * T_r / (3.0 * v_r - 1.0) - 3.0 / v_r**2


def maxwell_saturation(T_r, n=20000):
    """Return (p_sat, v_f, v_g) by the equal-area construction at T_r < 1."""
    v = np.linspace(0.42, 6.0, n)
    p = p_reduced(v, T_r)

    def area_balance(p_sat):
        # the three roots of p_reduced(v_r) = p_sat bracket the loop;
        # integrate p - p_sat between the outer two roots, which the
        # equal-area rule drives to zero.
        crossings = np.where(np.diff(np.sign(p - p_sat)))[0]
        if len(crossings) < 2:
            return None
        v_lo = v[crossings[0]]
        v_hi = v[crossings[-1]]
        mask = (v >= v_lo) & (v <= v_hi)
        return _trap(p[mask] - p_sat, v[mask]), v_lo, v_hi

    # bisection on p_sat between the loop min and max pressures
    p_min = p[(v > 0.5) & (v < 6.0)].min()
    p_max = p[(v > 0.5) & (v < 1.5)].max()
    lo, hi = max(p_min, 0.01), p_max
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        res = area_balance(mid)
        if res is None:
            hi = mid
            continue
        bal, v_f, v_g = res
        if bal > 0:
            lo = mid
        else:
            hi = mid
    return mid, v_f, v_g


if __name__ == "__main__":
    for T_r in (0.85, 0.90, 0.95):
        p_sat, v_f, v_g = maxwell_saturation(T_r)
        print(f"T_r={T_r}: p_sat={p_sat:.4f}, v_f={v_f:.3f}, v_g={v_g:.3f}")
