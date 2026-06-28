"""LMTD-method sizing of a heat exchanger.

Given the four terminal temperatures, the heat duty, the overall coefficient,
and a correction factor, return the log-mean temperature difference and the
required heat-transfer area. The routine handles both counter-flow and
parallel-flow end-difference conventions and guards the equal-difference limit
where the log-mean expression is indeterminate.

All temperatures in degrees Celsius (differences are the same in kelvin); U in
W/(m^2 K); Q in W; area returned in m^2.
"""

from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass
class LMTDResult:
    dt1: float           # end temperature difference at end 1 (K)
    dt2: float           # end temperature difference at end 2 (K)
    lmtd: float          # log-mean temperature difference (K)
    area: float          # required heat-transfer area (m^2)


def lmtd(dt1: float, dt2: float) -> float:
    """Log-mean of two end differences, with the equal-difference limit."""
    if dt1 <= 0 or dt2 <= 0:
        raise ValueError("end temperature differences must be positive")
    if math.isclose(dt1, dt2, rel_tol=1e-9):
        return dt1
    return (dt1 - dt2) / math.log(dt1 / dt2)


def size_counterflow(t_hi, t_ho, t_ci, t_co, q, u, f=1.0) -> LMTDResult:
    """Size a counter-flow exchanger (or any geometry via correction factor f)."""
    dt1 = t_hi - t_co
    dt2 = t_ho - t_ci
    dtlm = lmtd(dt1, dt2)
    area = q / (u * f * dtlm)
    return LMTDResult(dt1, dt2, dtlm, area)


def size_parallelflow(t_hi, t_ho, t_ci, t_co, q, u) -> LMTDResult:
    """Size a parallel-flow exchanger (both fluids enter the same end)."""
    dt1 = t_hi - t_ci
    dt2 = t_ho - t_co
    dtlm = lmtd(dt1, dt2)
    area = q / (u * dtlm)
    return LMTDResult(dt1, dt2, dtlm, area)


if __name__ == "__main__":
    # 1 MW steam condenser: steam at 50 C, water 25 -> 35 C, U = 2000.
    cf = size_counterflow(50, 50, 25, 35, q=1.0e6, u=2000.0)
    print(f"LMTD = {cf.lmtd:.2f} K, area = {cf.area:.1f} m^2")
    # Same duty as parallel flow, for comparison of the area penalty.
    pf = size_parallelflow(50, 50, 25, 35, q=1.0e6, u=2000.0)
    print(f"parallel-flow area = {pf.area:.1f} m^2 "
          f"({pf.area / cf.area:.2f}x counter-flow)")
