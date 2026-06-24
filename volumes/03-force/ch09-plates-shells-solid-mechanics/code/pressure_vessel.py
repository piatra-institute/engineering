"""Membrane stresses and wall-thickness sizing for thin pressure vessels.

Implements the thin-wall membrane formulas:
    sphere:    sigma = p R / (2 h)
    cylinder:  hoop  = p R / h,   axial = p R / (2 h)
and inverts them to size a wall thickness for a given allowable stress and
safety factor. Run with: python pressure_vessel.py
"""


def sphere_stress(p, R, h):
    return p * R / (2.0 * h)


def cylinder_stress(p, R, h):
    hoop = p * R / h
    axial = p * R / (2.0 * h)
    return hoop, axial


def size_cylinder_wall(p, R, sigma_allow, safety):
    """Wall thickness so that hoop stress = sigma_allow / safety."""
    return p * R * safety / sigma_allow


def size_sphere_wall(p, R, sigma_allow, safety):
    return p * R * safety / (2.0 * sigma_allow)


if __name__ == "__main__":
    p = 4.0e6            # 4 MPa internal pressure
    R = 0.40             # inner radius 0.4 m
    sigma_Y = 250e6      # yield 250 MPa
    safety = 3.0

    t_cyl = size_cylinder_wall(p, R, sigma_Y, safety)
    t_sph = size_sphere_wall(p, R, sigma_Y, safety)
    print(f"cylinder wall (hoop, SF=3): {t_cyl*1e3:.2f} mm")
    print(f"sphere/cap wall (SF=3):     {t_sph*1e3:.2f} mm")
    print(f"ratio cyl/sphere = {t_cyl/t_sph:.2f}  (expect 2.0)")

    hoop, axial = cylinder_stress(p, R, t_cyl)
    print(f"check: hoop={hoop/1e6:.1f} MPa, axial={axial/1e6:.1f} MPa, "
          f"ratio={hoop/axial:.2f}")
