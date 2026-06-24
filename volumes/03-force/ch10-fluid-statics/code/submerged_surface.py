"""Resultant force and centre of pressure on a flat submerged rectangle.

Implements the two working results of Section 10.4:

    F   = rho g h_C A          (resultant, equals pressure at centroid times area)
    h_P = h_C + I_xx / (h_C A) (centre of pressure, below the centroid)

with h measured vertically below the free surface. For a plate inclined
at angle theta to the horizontal, the offset along the plate is
I_xx * sin(theta) / (h_C A). Run with:

    uv run volumes/03-force/ch10-fluid-statics/code/submerged_surface.py
"""

import math

RHO = 1000.0   # kg/m^3, fresh water
G = 9.81       # m/s^2


def rectangle_force(width, height, top_depth, theta_deg=90.0, rho=RHO):
    """Force (N) and centre-of-pressure depth (m) on a vertical or inclined
    rectangle. top_depth is the vertical depth of the top edge; theta is the
    plate angle to horizontal (90 = vertical)."""
    theta = math.radians(theta_deg)
    area = width * height
    # centroid depth (vertical) = top_depth + (height/2) * sin(theta)
    h_c = top_depth + 0.5 * height * math.sin(theta)
    p_c = rho * G * h_c
    force = p_c * area
    # second moment about centroidal horizontal axis for a rectangle of
    # along-plate span 'height': I = width * height^3 / 12
    i_xx = width * height ** 3 / 12.0
    # vertical depth of centre of pressure
    h_p = h_c + i_xx * math.sin(theta) ** 2 / (h_c * area)
    return force, h_c, h_p


if __name__ == "__main__":
    # Worked example: tilted gate, w=2, b=3, h_T=1, theta=60 deg
    F, hc, hp = rectangle_force(2.0, 3.0, 1.0, theta_deg=60.0)
    print("Tilted gate (w=2 m, b=3 m, h_T=1 m, theta=60 deg):")
    print(f"  centroid depth h_C = {hc:.3f} m")
    print(f"  resultant force F  = {F/1e3:.1f} kN")
    print(f"  centre-of-pressure depth h_P = {hp:.3f} m")

    # Vertical dam, H=30 m, length 200 m
    F, hc, hp = rectangle_force(200.0, 30.0, 0.0, theta_deg=90.0)
    print("\nVertical dam (H=30 m, L=200 m, surface at crest):")
    print(f"  resultant force F  = {F/1e6:.1f} MN")
    print(f"  line of action at depth {hp:.2f} m  (=> {30-hp:.2f} m above base)")
