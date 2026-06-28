"""NTU-effectiveness rating of a heat exchanger.

Given the area, the overall coefficient, the two heat-capacity rates, and the
two inlet temperatures, return the effectiveness, the heat-transfer rate, and
the two outlet temperatures. Effectiveness relations are provided for
counter-flow, parallel-flow, cross-flow (both unmixed), and the phase-change
limit C_r -> 0.

C = m_dot * c_p in W/K; U in W/(m^2 K); A in m^2; temperatures in degrees C.
"""

from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass
class RatingResult:
    ntu: float
    c_r: float
    eff: float           # effectiveness
    q: float             # heat-transfer rate (W)
    t_ho: float          # hot outlet (C)
    t_co: float          # cold outlet (C)


def eps_counterflow(ntu: float, c_r: float) -> float:
    if math.isclose(c_r, 1.0, rel_tol=1e-9):
        return ntu / (1.0 + ntu)
    num = 1.0 - math.exp(-ntu * (1.0 - c_r))
    den = 1.0 - c_r * math.exp(-ntu * (1.0 - c_r))
    return num / den


def eps_parallelflow(ntu: float, c_r: float) -> float:
    return (1.0 - math.exp(-ntu * (1.0 + c_r))) / (1.0 + c_r)


def eps_crossflow_unmixed(ntu: float, c_r: float) -> float:
    if c_r == 0.0:
        return 1.0 - math.exp(-ntu)
    expo = (math.exp(-c_r * ntu**0.78) - 1.0) * ntu**0.22 / c_r
    return 1.0 - math.exp(expo)


def eps_phase_change(ntu: float, c_r: float = 0.0) -> float:
    # condenser or evaporator: one stream at constant temperature.
    return 1.0 - math.exp(-ntu)


_RELATIONS = {
    "counterflow": eps_counterflow,
    "parallelflow": eps_parallelflow,
    "crossflow": eps_crossflow_unmixed,
    "phase_change": eps_phase_change,
}


def rate(u, a, c_hot, c_cold, t_hi, t_ci, geometry="counterflow") -> RatingResult:
    c_min = min(c_hot, c_cold)
    c_max = max(c_hot, c_cold)
    c_r = c_min / c_max
    ntu = u * a / c_min
    eff = _RELATIONS[geometry](ntu, c_r)
    q_max = c_min * (t_hi - t_ci)
    q = eff * q_max
    t_ho = t_hi - q / c_hot
    t_co = t_ci + q / c_cold
    return RatingResult(ntu, c_r, eff, q, t_ho, t_co)


if __name__ == "__main__":
    # Air-cooled oil exchanger: A = 200 m^2, U = 50, oil C = 5*2100 = 10500 W/K,
    # air C = 20*1005 = 20100 W/K, oil in 140 C, air in 30 C.
    r = rate(u=50.0, a=200.0, c_hot=10500.0, c_cold=20100.0,
             t_hi=140.0, t_ci=30.0, geometry="crossflow")
    print(f"NTU = {r.ntu:.3f}, C_r = {r.c_r:.3f}, eff = {r.eff:.3f}")
    print(f"Q = {r.q/1e3:.1f} kW, oil out = {r.t_ho:.1f} C, air out = {r.t_co:.1f} C")
