"""
A small planar truss solver by the method of joints, assembled as a
single linear system A x = b and solved at once.

Supports:
  - Volume III, Chapter 1, simulation exercise "numerical FBD solver for
    a planar truss with up to ten joints"
  - The method-of-joints worked example and exercise 1.7.

Model:
  - Joints are points with (x, y) coordinates.
  - Members are two-force members connecting two joints; the unknown is
    the axial force, tension positive.
  - Supports: 'pin' fixes both x and y (two reactions); 'roller_x' fixes
    y only (vertical reaction); 'free' fixes nothing.
  - Loads are (Fx, Fy) applied at joints.

The unknowns are the member forces followed by the support reactions.
Each joint contributes two equilibrium equations (sum Fx, sum Fy). A
statically determinate truss has 2 * n_joints == n_members + n_reactions.

Dependencies:
  numpy

Usage:
  python truss_solver.py        # runs the three-member demo
"""

import numpy as np


def solve_truss(joints, members, supports, loads):
    """Return (member_forces, reactions) for a determinate planar truss.

    joints:   dict name -> (x, y)
    members:  list of (joint_a, joint_b) tuples
    supports: dict name -> 'pin' | 'roller_x' | 'free'
    loads:    dict name -> (Fx, Fy)
    """
    jnames = list(joints)
    jidx = {n: i for i, n in enumerate(jnames)}
    n_eq = 2 * len(jnames)

    # Build the reaction unknown list.
    reactions = []
    for n in jnames:
        s = supports.get(n, "free")
        if s == "pin":
            reactions += [(n, "x"), (n, "y")]
        elif s == "roller_x":
            reactions += [(n, "y")]

    n_unk = len(members) + len(reactions)
    if n_unk != n_eq:
        raise ValueError(
            f"truss not determinate: {n_eq} equations, {n_unk} unknowns")

    A = np.zeros((n_eq, n_unk))
    b = np.zeros(n_eq)

    # Member columns: a tension force on joint J points from J toward the
    # other joint (unit vector along the member).
    for k, (a, c) in enumerate(members):
        pa, pc = np.array(joints[a]), np.array(joints[c])
        u = (pc - pa) / np.linalg.norm(pc - pa)
        A[2 * jidx[a], k] += u[0]
        A[2 * jidx[a] + 1, k] += u[1]
        A[2 * jidx[c], k] += -u[0]
        A[2 * jidx[c] + 1, k] += -u[1]

    # Reaction columns.
    for r, (n, comp) in enumerate(reactions):
        col = len(members) + r
        if comp == "x":
            A[2 * jidx[n], col] = 1.0
        else:
            A[2 * jidx[n] + 1, col] = 1.0

    # Load vector goes to the right-hand side (equilibrium: internal +
    # reaction + applied = 0, so move applied to b with a sign flip).
    for n, (fx, fy) in loads.items():
        b[2 * jidx[n]] -= fx
        b[2 * jidx[n] + 1] -= fy

    x = np.linalg.solve(A, b)
    member_forces = {f"{a}{c}": x[k] for k, (a, c) in enumerate(members)}
    reaction_vals = {f"{n}_{comp}": x[len(members) + r]
                     for r, (n, comp) in enumerate(reactions)}
    return member_forces, reaction_vals


def demo():
    # Simple determinate triangle truss:
    #   A (pin) at origin, B (roller) at (4,0), C at (2,2).
    # A downward load of 10 kN at C.
    joints = {"A": (0.0, 0.0), "B": (4.0, 0.0), "C": (2.0, 2.0)}
    members = [("A", "B"), ("A", "C"), ("B", "C")]
    supports = {"A": "pin", "B": "roller_x"}
    loads = {"C": (0.0, -10.0)}   # kN
    mf, rx = solve_truss(joints, members, supports, loads)
    print("member forces (kN, +tension):")
    for k, v in mf.items():
        print(f"  {k}: {v:+7.3f}")
    print("reactions (kN):")
    for k, v in rx.items():
        print(f"  {k}: {v:+7.3f}")


if __name__ == "__main__":
    demo()
