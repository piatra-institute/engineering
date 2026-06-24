"""Mechanical generation of Euler-Lagrange equations with SymPy.

Demonstrates the bookkeeping economy the chapter claims: write the
Lagrangian once, and the equations of motion fall out of a standard
differentiation pattern with no free-body diagram and no constraint
force. Worked here for the simple pendulum and the bead on a rotating
hoop; the same pattern handles the double pendulum unchanged.

Run:
    python lagrangian_symbolic.py
prints the symbolic equations of motion to stdout. Requires sympy.
"""

from __future__ import annotations
import sympy as sp


def euler_lagrange(L, q, t):
    """Return d/dt(dL/dqdot) - dL/dq for a single coordinate q(t)."""
    qdot = sp.diff(q, t)
    dL_dqdot = sp.diff(L, qdot)
    dL_dq = sp.diff(L, q)
    return sp.simplify(sp.diff(dL_dqdot, t) - dL_dq)


def simple_pendulum():
    t, m, g, ell = sp.symbols("t m g L", positive=True)
    th = sp.Function("theta")(t)
    thd = sp.diff(th, t)
    T = sp.Rational(1, 2) * m * ell**2 * thd**2
    U = m * g * ell * (1 - sp.cos(th))
    eom = euler_lagrange(T - U, th, t)
    return sp.Eq(eom, 0)


def bead_on_hoop():
    t, m, g, R, Om = sp.symbols("t m g R Omega", positive=True)
    th = sp.Function("theta")(t)
    thd = sp.diff(th, t)
    T = sp.Rational(1, 2) * m * R**2 * (thd**2 + Om**2 * sp.sin(th)**2)
    U = m * g * R * (1 - sp.cos(th))
    eom = euler_lagrange(T - U, th, t)
    return sp.Eq(sp.simplify(eom), 0)


def main():
    print("Simple pendulum equation of motion:")
    sp.pprint(simple_pendulum())
    print()
    print("Bead on rotating hoop equation of motion:")
    sp.pprint(bead_on_hoop())


if __name__ == "__main__":
    main()
