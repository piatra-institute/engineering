"""Numerical solution of the Blasius flat-plate boundary-layer equation.

The similarity transformation reduces the laminar zero-pressure-gradient
boundary layer to the third-order ordinary differential equation

    2 f''' + f f'' = 0,     f(0) = 0, f'(0) = 0, f'(inf) = 1.

This is a boundary-value problem; the standard route is a shooting method
that guesses f''(0) and integrates until f'(eta) approaches 1. The known
answer is f''(0) approx 0.33206, which fixes the wall shear and hence the
skin-friction coefficient C_f = 0.664 / sqrt(Re_x).

Run:
    python blasius.py
to print f''(0), the 99-percent thickness, and the tabulated profile used
in the chapter's Blasius figure.
"""

from __future__ import annotations


def rhs(state):
    """State = (f, f', f''). Returns (f', f'', f''') from 2 f''' = -f f''."""
    f, fp, fpp = state
    return (fp, fpp, -0.5 * f * fpp)


def integrate(fpp0, eta_max=10.0, h=1e-3):
    """Integrate the Blasius system with RK4 from eta=0 given f''(0)=fpp0.
    Returns the eta grid and the state history."""
    state = (0.0, 0.0, fpp0)
    etas = [0.0]
    hist = [state]
    n = int(eta_max / h)
    for i in range(n):
        s = state
        k1 = rhs(s)
        k2 = rhs(tuple(s[j] + 0.5 * h * k1[j] for j in range(3)))
        k3 = rhs(tuple(s[j] + 0.5 * h * k2[j] for j in range(3)))
        k4 = rhs(tuple(s[j] + h * k3[j] for j in range(3)))
        state = tuple(
            s[j] + (h / 6.0) * (k1[j] + 2 * k2[j] + 2 * k3[j] + k4[j])
            for j in range(3)
        )
        etas.append((i + 1) * h)
        hist.append(state)
    return etas, hist


def shoot(tol=1e-8):
    """Bisection on f''(0) so that f'(eta_max) = 1."""
    lo, hi = 0.1, 0.6
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        _, hist = integrate(mid)
        fp_inf = hist[-1][1]
        if fp_inf > 1.0:
            hi = mid
        else:
            lo = mid
        if hi - lo < tol:
            break
    return 0.5 * (lo + hi)


if __name__ == "__main__":
    fpp0 = shoot()
    etas, hist = integrate(fpp0, h=1e-3)
    print(f"f''(0) = {fpp0:.5f}  (reference 0.33206)")
    # 99-percent thickness: first eta where f' >= 0.99.
    for eta, s in zip(etas, hist):
        if s[1] >= 0.99:
            print(f"eta_99 = {eta:.3f}  (reference 5.0)")
            break
    print(f"{'eta':>6} {'f_prime':>10}")
    for eta, s in zip(etas, hist):
        if abs(eta - round(eta * 2.5) / 2.5) < 5e-4:
            print(f"{eta:6.2f} {s[1]:10.4f}")
