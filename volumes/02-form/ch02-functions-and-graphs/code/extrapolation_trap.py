# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
Quantify the linear-extrapolation trap on an exponential process.

Given a doubling-process count sampled over a short fitted window,
this script fits a straight line through the windowed samples and
compares the linear projection of a threshold-crossing time against
the true exponential crossing time. It reproduces the arithmetic of
the failure-section estimation block: a process that doubles on a
fixed cadence, fitted linearly over an early window, projects a
threshold crossing that is wrong by a large factor.

Supports Volume II, Chapter 2, failure section (linear extrapolation
of an exponential) and the extrapolation-trap figure
(fig:vol02:ch02:extrapolation-trap).

Usage:
  python extrapolation_trap.py <N0> <double_time> <window_end> \
      <threshold>

  python extrapolation_trap.py 100 3 7 4000

All arguments share the same time unit (e.g. days). The output prints
the fitted linear slope, the linear-projected crossing time, the true
exponential crossing time, and the ratio between them.
"""

from __future__ import annotations

import math
import sys


def true_count(n0: float, double_time: float, t: float) -> float:
    """Exponential count under a fixed doubling cadence."""
    return n0 * 2.0 ** (t / double_time)


def linear_fit_through_window(
    n0: float, double_time: float, window_end: float, n_samples: int = 8
) -> tuple[float, float]:
    """Least-squares line through evenly spaced windowed samples.

    Returns (slope, intercept).
    """
    ts = [window_end * i / (n_samples - 1) for i in range(n_samples)]
    ys = [true_count(n0, double_time, t) for t in ts]
    mean_t = sum(ts) / len(ts)
    mean_y = sum(ys) / len(ys)
    s_tt = sum((t - mean_t) ** 2 for t in ts)
    s_ty = sum((t - mean_t) * (y - mean_y) for t, y in zip(ts, ys))
    slope = s_ty / s_tt
    intercept = mean_y - slope * mean_t
    return slope, intercept


def main() -> int:
    if len(sys.argv) != 5:
        print(__doc__)
        return 2
    n0 = float(sys.argv[1])
    double_time = float(sys.argv[2])
    window_end = float(sys.argv[3])
    threshold = float(sys.argv[4])

    slope, intercept = linear_fit_through_window(
        n0, double_time, window_end
    )
    # Linear projection of the threshold crossing.
    t_linear = (threshold - intercept) / slope
    # True exponential crossing: N0 * 2^(t/T) = threshold.
    t_true = double_time * math.log2(threshold / n0)
    ratio = t_linear / t_true

    print(f"fitted linear slope   : {slope:.3g} per unit time")
    print(f"linear crossing time  : {t_linear:.3g}")
    print(f"true crossing time    : {t_true:.3g}")
    print(f"linear / true ratio   : {ratio:.3g}")
    print(
        "The linear extrapolation overstates the time to threshold "
        f"by a factor of about {ratio:.1f}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
