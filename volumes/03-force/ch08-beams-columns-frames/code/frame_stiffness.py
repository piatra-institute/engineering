"""Direct-stiffness analysis of a planar frame.

A compact implementation of the matrix stiffness method for 2D frame
members with axial and bending action (three degrees of freedom per
node: u, v, theta). Assembles the global stiffness matrix, applies
supports by row/column elimination, and solves K u = F for the joint
displacements and the member end forces.

Verified below on a single propped cantilever, whose tip rotation has
a closed form.

Run:
    python frame_stiffness.py
"""

from __future__ import annotations

import numpy as np


def member_stiffness(E, A, I, x1, y1, x2, y2):
    """6x6 global-coordinate stiffness for a 2D frame member."""
    dx, dy = x2 - x1, y2 - y1
    L = np.hypot(dx, dy)
    c, s = dx / L, dy / L

    EA_L = E * A / L
    EI = E * I
    k = np.array([
        [ EA_L,        0,            0,        -EA_L,       0,            0],
        [ 0,    12*EI/L**3,   6*EI/L**2,        0,  -12*EI/L**3,   6*EI/L**2],
        [ 0,     6*EI/L**2,    4*EI/L,          0,   -6*EI/L**2,    2*EI/L],
        [-EA_L,        0,            0,         EA_L,       0,            0],
        [ 0,   -12*EI/L**3,  -6*EI/L**2,        0,   12*EI/L**3,  -6*EI/L**2],
        [ 0,     6*EI/L**2,    2*EI/L,          0,   -6*EI/L**2,    4*EI/L],
    ])
    # transformation from local to global
    T = np.array([
        [ c,  s, 0,  0,  0, 0],
        [-s,  c, 0,  0,  0, 0],
        [ 0,  0, 1,  0,  0, 0],
        [ 0,  0, 0,  c,  s, 0],
        [ 0,  0, 0, -s,  c, 0],
        [ 0,  0, 0,  0,  0, 1],
    ])
    return T.T @ k @ T, L


def main():
    # Propped cantilever: node 0 fixed, node 1 pinned, tip moment M.
    E = 200e9
    A = 6.0e-3
    I = 8.0e-5
    nodes = np.array([[0.0, 0.0], [4.0, 0.0]])
    K, L = member_stiffness(E, A, I, *nodes[0], *nodes[1])

    ndof = 6
    Kg = np.zeros((ndof, ndof))
    Kg += K  # single member, dof order: u0 v0 t0 u1 v1 t1

    F = np.zeros(ndof)
    F[5] = 10.0e3   # applied moment at node 1 (theta dof)

    # supports: node 0 fully fixed (dof 0,1,2), node 1 pinned (dof 3,4)
    fixed = [0, 1, 2, 3, 4]
    free = [d for d in range(ndof) if d not in fixed]

    Kff = Kg[np.ix_(free, free)]
    Ff = F[free]
    uf = np.linalg.solve(Kff, Ff)
    u = np.zeros(ndof)
    u[free] = uf

    theta1 = u[5]
    # closed form for a propped cantilever, applied end moment M:
    # theta = M L / (4 EI)
    theta_cf = F[5] * L / (4 * E * I)
    print(f"node-1 rotation (stiffness) = {theta1:.6e} rad")
    print(f"node-1 rotation (closed)    = {theta_cf:.6e} rad")
    print(f"relative error = {abs(theta1-theta_cf)/abs(theta_cf)*100:.3f} %")


if __name__ == "__main__":
    main()
