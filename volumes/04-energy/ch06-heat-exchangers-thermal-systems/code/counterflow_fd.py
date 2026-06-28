"""One-dimensional finite-difference solver for a counter-flow heat exchanger.

March the two coupled energy balances along the exchanger length and compare the
converged outlet temperatures against the closed-form LMTD prediction. The hot
stream flows in +x; the cold stream flows in -x (counter-current). The grid
sweeps are repeated until the cold profile stops moving, because the cold inlet
boundary condition sits at the far end.

C = m_dot * c_p in W/K; U in W/(m^2 K); total area A in m^2.
"""

from __future__ import annotations

import math


def solve_counterflow(u, area, c_hot, c_cold, t_hi, t_ci, n=200, iters=400):
    da = area / n
    th = [t_hi] * (n + 1)   # hot temperature at node faces, hot enters at node 0
    tc = [t_ci] * (n + 1)   # cold temperature, cold enters at node n
    for _ in range(iters):
        # march hot forward (0 -> n)
        for i in range(n):
            dq = u * da * (th[i] - tc[i])
            th[i + 1] = th[i] - dq / c_hot
        # march cold backward (n -> 0)
        tc[n] = t_ci
        for i in range(n, 0, -1):
            dq = u * da * (th[i] - tc[i])
            tc[i - 1] = tc[i] + dq / c_cold
    t_ho = th[n]
    t_co = tc[0]
    return t_ho, t_co


def lmtd_outlets(u, area, c_hot, c_cold, t_hi, t_ci):
    """Closed-form counter-flow outlets via the effectiveness relation."""
    c_min, c_max = min(c_hot, c_cold), max(c_hot, c_cold)
    c_r = c_min / c_max
    ntu = u * area / c_min
    if math.isclose(c_r, 1.0):
        eff = ntu / (1 + ntu)
    else:
        eff = ((1 - math.exp(-ntu * (1 - c_r)))
               / (1 - c_r * math.exp(-ntu * (1 - c_r))))
    q = eff * c_min * (t_hi - t_ci)
    return t_hi - q / c_hot, t_ci + q / c_cold


if __name__ == "__main__":
    args = dict(u=1500.0, area=3.0, c_hot=8400.0, c_cold=16800.0,
                t_hi=80.0, t_ci=20.0)
    th_fd, tc_fd = solve_counterflow(**args)
    th_lm, tc_lm = lmtd_outlets(**args)
    print(f"finite-difference: hot out {th_fd:.2f} C, cold out {tc_fd:.2f} C")
    print(f"closed form:       hot out {th_lm:.2f} C, cold out {tc_lm:.2f} C")
