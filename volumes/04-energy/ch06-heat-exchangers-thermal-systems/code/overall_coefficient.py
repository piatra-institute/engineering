"""Overall heat-transfer coefficient from a series thermal-resistance network.

Assemble the clean overall coefficient from the inside film, the tube-wall
conduction, and the outside film, all referred to the outside area, then add
the two fouling resistances to get the dirty coefficient. The model is the
arithmetic behind the thermal-network figure of section 6.7.

Films h in W/(m^2 K); wall k in W/(m K); radii in m; fouling R_f in
m^2 K / W; coefficients returned referred to the outside surface.
"""

from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass
class UResult:
    u_clean: float       # clean overall coefficient, outside-referred (W/m^2 K)
    u_dirty: float       # dirty overall coefficient (W/m^2 K)
    loss_fraction: float # fractional duty lost to fouling at fixed LMTD


def overall_coefficient(h_in, h_out, k_wall, r_in, r_out,
                        rf_in=0.0, rf_out=0.0, length=1.0) -> UResult:
    a_in = 2.0 * math.pi * r_in * length
    a_out = 2.0 * math.pi * r_out * length
    # all resistances referred to the outside area: U_o A_o = 1 / R_total
    r_film_in = 1.0 / (h_in * a_in)
    r_foul_in = rf_in / a_in
    r_wall = math.log(r_out / r_in) / (2.0 * math.pi * k_wall * length)
    r_foul_out = rf_out / a_out
    r_film_out = 1.0 / (h_out * a_out)

    r_clean = r_film_in + r_wall + r_film_out
    r_dirty = r_clean + r_foul_in + r_foul_out

    u_clean = 1.0 / (r_clean * a_out)
    u_dirty = 1.0 / (r_dirty * a_out)
    loss = 1.0 - u_dirty / u_clean
    return UResult(u_clean, u_dirty, loss)


if __name__ == "__main__":
    # 25 mm OD, 21 mm ID steel tube (k=50), water both sides, fouling 0.0005 each.
    res = overall_coefficient(
        h_in=3000.0, h_out=2000.0, k_wall=50.0,
        r_in=0.0105, r_out=0.0125,
        rf_in=0.0005, rf_out=0.0005,
    )
    print(f"U_clean = {res.u_clean:.0f} W/m^2 K")
    print(f"U_dirty = {res.u_dirty:.0f} W/m^2 K")
    print(f"duty lost to fouling = {100*res.loss_fraction:.1f}%")
