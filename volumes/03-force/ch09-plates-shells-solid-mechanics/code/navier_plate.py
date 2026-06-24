"""Navier double-sine series for a simply supported rectangular plate.

Computes the centre deflection of a simply supported rectangular plate of
size a x b under uniform pressure q0, by summing the Navier series

    w(x,y) = (16 q0 / (pi^6 D)) * sum_{m,n odd}
             sin(m pi x/a) sin(n pi y/b)
             / ( m n [ (m/a)^2 + (n/b)^2 ]^2 )

with D = E h^3 / (12 (1 - nu^2)). Run with: python navier_plate.py
"""

import math


def flexural_rigidity(E, h, nu):
    return E * h**3 / (12.0 * (1.0 - nu**2))


def navier_deflection(x, y, a, b, q0, D, n_terms=20):
    total = 0.0
    for m in range(1, 2 * n_terms, 2):       # odd m
        for n in range(1, 2 * n_terms, 2):   # odd n
            denom = m * n * ((m / a) ** 2 + (n / b) ** 2) ** 2
            total += (math.sin(m * math.pi * x / a)
                      * math.sin(n * math.pi * y / b) / denom)
    return 16.0 * q0 / (math.pi**6 * D) * total


if __name__ == "__main__":
    # Square steel plate, side 1 m, thickness 10 mm, 5 kPa (Exercise 1).
    E, nu, h = 200e9, 0.30, 10e-3
    a = b = 1.0
    q0 = 5.0e3
    D = flexural_rigidity(E, h, nu)
    w_center = navier_deflection(a / 2, b / 2, a, b, q0, D, n_terms=30)
    # one-term approximation
    w_one = navier_deflection(a / 2, b / 2, a, b, q0, D, n_terms=1)
    print(f"D = {D:.1f} N*m")
    print(f"centre deflection (30 terms) = {w_center*1e3:.4f} mm")
    print(f"centre deflection (1 term)   = {w_one*1e3:.4f} mm")
    print(f"closed-form coefficient w_max D /(q0 a^4) = "
          f"{w_center * D / (q0 * a**4):.5f}  (tabulated 0.00406)")
