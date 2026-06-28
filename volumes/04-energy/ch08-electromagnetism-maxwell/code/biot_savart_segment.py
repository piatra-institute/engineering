"""Numerical Biot-Savart integral for a finite straight wire segment.

Compares the discretised line integral against the closed form
    B = (mu0 I / 4 pi r) (sin theta_2 - sin theta_1),
where theta_1, theta_2 are measured from the foot of the perpendicular
from the field point to the wire. Used in Section 8.8 and the simulation
exercise. Also maps the field of a square current loop by summing four
segments and reports the centre value against mu0 I sqrt(2)/(pi a).
"""

import numpy as np

MU0 = 4.0e-7 * np.pi  # H/m


def biot_savart_segment(p_start, p_end, current, field_point, n=2000):
    """Field at field_point from a straight segment carrying `current`.

    p_start, p_end, field_point are length-3 arrays in metres. Returns the
    B vector in tesla via midpoint quadrature of dl x r_hat / r^2.
    """
    p_start = np.asarray(p_start, float)
    p_end = np.asarray(p_end, float)
    field_point = np.asarray(field_point, float)
    ts = (np.arange(n) + 0.5) / n
    seg = p_end - p_start
    points = p_start + np.outer(ts, seg)        # midpoints along the wire
    dl = seg / n                                # constant vector element
    r = field_point - points                    # source-to-field vectors
    r_mag = np.linalg.norm(r, axis=1)
    integrand = np.cross(np.tile(dl, (n, 1)), r) / r_mag[:, None] ** 3
    return MU0 * current / (4.0 * np.pi) * integrand.sum(axis=0)


def straight_wire_closed_form(current, r, theta1_deg, theta2_deg):
    """Closed-form magnitude for a finite straight segment."""
    t1 = np.radians(theta1_deg)
    t2 = np.radians(theta2_deg)
    return MU0 * current / (4.0 * np.pi * r) * (np.sin(t2) - np.sin(t1))


def square_loop_centre(side, current):
    """B at the centre of a square loop of given side, by four segments."""
    a = side
    half = a / 2.0
    corners = [
        np.array([-half, -half, 0.0]),
        np.array([half, -half, 0.0]),
        np.array([half, half, 0.0]),
        np.array([-half, half, 0.0]),
    ]
    centre = np.array([0.0, 0.0, 0.0])
    total = np.zeros(3)
    for i in range(4):
        total += biot_savart_segment(corners[i], corners[(i + 1) % 4], current, centre)
    return total


if __name__ == "__main__":
    # Infinite-wire check: a long segment seen perpendicular at r should
    # approach mu0 I / (2 pi r) as the segment length grows.
    I, r = 1.0, 0.01
    fp = np.array([r, 0.0, 0.0])
    for half_len in (0.1, 1.0, 10.0):
        B = biot_savart_segment([0, 0, -half_len], [0, 0, half_len], I, fp,
                                n=20000)
        print(f"half-length {half_len:6.1f} m: |B| = {np.linalg.norm(B)*1e6:7.3f} uT")
    print(f"infinite-wire prediction: {MU0*I/(2*np.pi*r)*1e6:7.3f} uT")

    # Square loop centre vs analytic 2*sqrt(2)*mu0 I / (pi a)
    a = 0.1
    Bc = square_loop_centre(a, I)
    analytic = 2.0 * np.sqrt(2.0) * MU0 * I / (np.pi * a)
    print(f"square-loop centre: numeric {np.linalg.norm(Bc)*1e6:.3f} uT, "
          f"analytic {analytic*1e6:.3f} uT")
