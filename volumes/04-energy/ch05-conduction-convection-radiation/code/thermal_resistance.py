"""Series and parallel thermal-resistance networks for plane and tube walls.

Builds the resistance chain of a composite wall or insulated pipe and returns
the overall U-value (or heat-loss rate per metre for a pipe), plus the interface
temperatures. The same electrical analogy used in section 5.1: resistances in
series add, the heat flow is the temperature difference divided by the total
resistance, and the temperature drop across each element is the heat flow times
that element's resistance.

SI units throughout: metres, watts, kelvin, W/(m.K) for conductivity.
"""

from __future__ import annotations

import math


def film_resistance(h, area=1.0):
    """Convective film resistance 1/(h A) for a plane surface of given area."""
    return 1.0 / (h * area)


def plane_layer_resistance(thickness, k, area=1.0):
    """Conductive resistance L/(k A) of a flat layer."""
    return thickness / (k * area)


def composite_wall_u(layers, h_inner, h_outer):
    """Overall U-value of a flat composite wall (per unit area).

    layers: list of (thickness_m, conductivity_W_mK) tuples, ordered inner
    to outer. Returns U in W/(m^2.K).
    """
    r_total = film_resistance(h_inner) + film_resistance(h_outer)
    for thickness, k in layers:
        r_total += plane_layer_resistance(thickness, k)
    return 1.0 / r_total


def composite_wall_profile(layers, h_inner, h_outer, t_inner, t_outer):
    """Interface temperatures through a composite wall at steady state.

    Returns a list of (label, temperature) from indoor air to outdoor air.
    """
    resistances = [("indoor film", film_resistance(h_inner))]
    for i, (thickness, k) in enumerate(layers):
        resistances.append((f"layer {i + 1}", plane_layer_resistance(thickness, k)))
    resistances.append(("outdoor film", film_resistance(h_outer)))

    r_total = sum(r for _, r in resistances)
    q = (t_inner - t_outer) / r_total  # heat flux per unit area

    profile = [("indoor air", t_inner)]
    t = t_inner
    for label, r in resistances:
        t -= q * r
        profile.append((f"after {label}", t))
    profile[-1] = ("outdoor air", t_outer)
    return q, profile


def cylinder_resistance(r_inner, r_outer, k, length=1.0):
    """Radial conductive resistance of a tube wall, per the ln(r2/r1) form."""
    return math.log(r_outer / r_inner) / (2.0 * math.pi * k * length)


def cylinder_film_resistance(h, radius, length=1.0):
    """Convective film resistance at a cylindrical surface of given radius."""
    return 1.0 / (h * 2.0 * math.pi * radius * length)


def insulated_pipe_loss(r_pipe_inner, r_pipe_outer, k_pipe, k_ins,
                        ins_thickness, h_inner, h_outer, dt):
    """Heat-loss rate per metre from an insulated pipe.

    Returns watts per metre for the given inside-to-outside temperature
    difference dt (kelvin).
    """
    r_outer = r_pipe_outer + ins_thickness
    r = (cylinder_film_resistance(h_inner, r_pipe_inner)
         + cylinder_resistance(r_pipe_inner, r_pipe_outer, k_pipe)
         + cylinder_resistance(r_pipe_outer, r_outer, k_ins)
         + cylinder_film_resistance(h_outer, r_outer))
    return dt / r


def critical_radius(k_ins, h_outer):
    """Critical insulation radius r_c = k/h below which insulation adds loss."""
    return k_ins / h_outer


if __name__ == "__main__":
    # Composite wall from the exercises: brick / insulation / gypsum.
    wall_layers = [
        (0.10, 0.7),    # brick
        (0.15, 0.04),   # insulation
        (0.015, 0.17),  # gypsum board
    ]
    u = composite_wall_u(wall_layers, h_inner=8.0, h_outer=25.0)
    print(f"composite wall U = {u:.3f} W/(m^2.K)")

    q, prof = composite_wall_profile(wall_layers, 8.0, 25.0, 22.0, -15.0)
    print(f"heat flux = {q:.1f} W/m^2")
    for label, t in prof:
        print(f"  {label:>18}: {t:6.1f} C")

    # Insulated steam pipe from the worked example, 50 mm insulation.
    qpm = insulated_pipe_loss(0.025, 0.030, 50.0, 0.04, 0.050,
                              h_inner=5000.0, h_outer=8.0, dt=130.0)
    print(f"pipe loss (50 mm insulation) = {qpm:.0f} W/m")
    print(f"critical radius = {critical_radius(0.04, 8.0) * 1000:.1f} mm")
