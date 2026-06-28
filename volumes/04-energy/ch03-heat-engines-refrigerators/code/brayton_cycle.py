"""Air-standard Brayton-cycle state-point solver.

Given the compressor inlet state, the pressure ratio, and the turbine inlet
temperature, compute the four state temperatures, the net specific work, the
thermal efficiency, and the back-work ratio. Cold-air-standard assumption:
constant specific heats. Used in section 3.3 and the Brayton exercises.
"""

from __future__ import annotations

CP_AIR = 1.005      # kJ/kg.K
GAMMA = 1.4


def solve_brayton(t1, p_ratio, t3, gamma=GAMMA, cp=CP_AIR):
    """Return a dict of state temperatures and cycle performance.

    t1      compressor inlet temperature (K)
    p_ratio pressure ratio p2/p1
    t3      turbine inlet temperature (K)
    """
    exp = (gamma - 1.0) / gamma
    t2 = t1 * p_ratio ** exp                 # isentropic compression
    t4 = t3 * p_ratio ** (-exp)              # isentropic expansion

    w_comp = cp * (t2 - t1)                  # compressor work input
    w_turb = cp * (t3 - t4)                  # turbine work output
    q_in = cp * (t3 - t2)                    # combustor heat input
    w_net = w_turb - w_comp
    eta = w_net / q_in
    bwr = w_comp / w_turb                    # back-work ratio

    return {
        "T1": t1, "T2": t2, "T3": t3, "T4": t4,
        "w_comp": w_comp, "w_turb": w_turb, "q_in": q_in,
        "w_net": w_net, "eta": eta, "back_work_ratio": bwr,
    }


if __name__ == "__main__":
    # Worked example: r_p = 12, T1 = 300 K, T3 = 1400 K.
    res = solve_brayton(300.0, 12.0, 1400.0)
    for k, v in res.items():
        print(f"{k:18s} {v:8.3f}")
    # Check eta against the closed form 1 - r_p^-((g-1)/g).
    closed = 1.0 - 12.0 ** (-(GAMMA - 1.0) / GAMMA)
    print(f"closed-form eta    {closed:8.3f}")
