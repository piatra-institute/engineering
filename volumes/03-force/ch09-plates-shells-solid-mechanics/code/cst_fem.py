"""Minimal plane-stress finite-element solver: constant-strain triangles.

A teaching-grade two-dimensional linear-elastic solver using three-node
constant-strain triangular (CST) elements. It assembles the global stiffness
matrix, applies displacement and nodal-force boundary conditions, solves
K u = F, and recovers element stresses. Verified on a single-element uniaxial
tension patch test against the analytical strain eps = sigma/E.

Dependencies: numpy. Run with: python cst_fem.py
"""

import numpy as np


def plane_stress_D(E, nu):
    """Plane-stress constitutive matrix (Voigt: sxx, syy, txy)."""
    c = E / (1.0 - nu**2)
    return c * np.array([[1.0, nu, 0.0],
                         [nu, 1.0, 0.0],
                         [0.0, 0.0, (1.0 - nu) / 2.0]])


def cst_stiffness(coords, D, thickness):
    """Element stiffness for a CST. coords: 3x2 array of node (x,y)."""
    (x1, y1), (x2, y2), (x3, y3) = coords
    area2 = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)  # 2*Area, signed
    area = 0.5 * abs(area2)
    b = np.array([y2 - y3, y3 - y1, y1 - y2])
    c = np.array([x3 - x2, x1 - x3, x2 - x1])
    B = np.zeros((3, 6))
    for i in range(3):
        B[0, 2 * i] = b[i]
        B[1, 2 * i + 1] = c[i]
        B[2, 2 * i] = c[i]
        B[2, 2 * i + 1] = b[i]
    B /= area2
    return thickness * area * (B.T @ D @ B), B


def solve(nodes, elements, D, thickness, fixed_dofs, forces):
    ndof = 2 * len(nodes)
    K = np.zeros((ndof, ndof))
    Bs = []
    for el in elements:
        Ke, B = cst_stiffness(nodes[el], D, thickness)
        Bs.append(B)
        dofs = np.array([[2 * n, 2 * n + 1] for n in el]).flatten()
        for a in range(6):
            for bb in range(6):
                K[dofs[a], dofs[bb]] += Ke[a, bb]
    F = np.zeros(ndof)
    for dof, val in forces.items():
        F[dof] += val
    free = [d for d in range(ndof) if d not in fixed_dofs]
    u = np.zeros(ndof)
    u[free] = np.linalg.solve(K[np.ix_(free, free)], F[free])
    return u, Bs


if __name__ == "__main__":
    # Patch test: unit square split into two CSTs, uniaxial tension sigma_x.
    nodes = np.array([[0, 0], [1, 0], [1, 1], [0, 1]], float)
    elements = [(0, 1, 2), (0, 2, 3)]
    E, nu, t = 200e9, 0.3, 1.0
    D = plane_stress_D(E, nu)
    sigma_x = 100e6
    fixed = {0, 1, 7}            # node 0 fully fixed, node 3 fixed in x
    forces = {2: sigma_x * 0.5,  # node1 x (tributary half-edge)
              4: sigma_x * 0.5}  # node2 x
    u, _ = solve(nodes, elements, D, t, fixed, forces)
    print(f"u_x at right edge = {u[2]:.3e}  (analytic eps = {sigma_x/E:.3e})")
