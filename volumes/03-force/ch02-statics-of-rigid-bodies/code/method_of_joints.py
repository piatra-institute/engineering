"""Planar pin-jointed truss solver by the global stiffness-free
equilibrium method (one linear system over all member forces and
reactions).

The solver assembles the 2*j joint-equilibrium equations and solves
for the m member forces and r reaction components in one linear solve,
which is the matrix form of the method of joints. It checks statical
determinacy (m + r == 2*j) before solving.

Sign convention: positive member force is tension (member pulls its
end joints toward each other -> the force on a joint points away from
the joint, along the member, into the member).

Verified in the chapter against the six-bay Pratt truss worked
example (max chord force 90 kN; third-bay diagonal 10*sqrt(2) kN).
"""

from __future__ import annotations

import numpy as np


def solve_truss(joints, members, loads, supports):
    """Solve a planar truss.

    Parameters
    ----------
    joints : dict[str, tuple[float, float]]
        Joint name -> (x, y) coordinates.
    members : list[tuple[str, str]]
        Each member as a pair of joint names.
    loads : dict[str, tuple[float, float]]
        Joint name -> applied (Fx, Fy) external load.
    supports : dict[str, str]
        Joint name -> 'pin' (reacts x and y) or 'roller_y' (reacts y
        only) or 'roller_x' (reacts x only).

    Returns
    -------
    member_forces : dict[tuple[str, str], float]
        Axial force per member; positive is tension.
    reactions : dict[str, tuple[float, float]]
        Reaction (Rx, Ry) per support joint.
    """
    jnames = list(joints)
    jindex = {name: i for i, name in enumerate(jnames)}
    n_eq = 2 * len(jnames)

    # Build the list of reaction unknowns.
    reaction_cols = []  # (joint, component) where component in {'x','y'}
    for jn, kind in supports.items():
        if kind == "pin":
            reaction_cols.append((jn, "x"))
            reaction_cols.append((jn, "y"))
        elif kind == "roller_y":
            reaction_cols.append((jn, "y"))
        elif kind == "roller_x":
            reaction_cols.append((jn, "x"))
        else:
            raise ValueError(f"unknown support kind: {kind!r}")

    n_unknowns = len(members) + len(reaction_cols)
    if n_unknowns != n_eq:
        raise ValueError(
            f"not statically determinate: {len(members)} members + "
            f"{len(reaction_cols)} reactions != {n_eq} equations"
        )

    A = np.zeros((n_eq, n_unknowns))
    b = np.zeros(n_eq)

    # Member-force columns. A tension force in member (p, q) pulls joint p
    # toward q: unit vector from p to q.
    for col, (p, q) in enumerate(members):
        xp, yp = joints[p]
        xq, yq = joints[q]
        dx, dy = xq - xp, yq - yp
        length = np.hypot(dx, dy)
        ux, uy = dx / length, dy / length
        ip, iq = jindex[p], jindex[q]
        # force on joint p from a tension member points p -> q
        A[2 * ip, col] += ux
        A[2 * ip + 1, col] += uy
        # equal and opposite on joint q
        A[2 * iq, col] += -ux
        A[2 * iq + 1, col] += -uy

    # Reaction columns.
    for k, (jn, comp) in enumerate(reaction_cols):
        col = len(members) + k
        i = jindex[jn]
        if comp == "x":
            A[2 * i, col] = 1.0
        else:
            A[2 * i + 1, col] = 1.0

    # Right-hand side: equilibrium is (member + reaction) + applied = 0,
    # so move applied loads to the RHS with a sign flip.
    for jn, (fx, fy) in loads.items():
        i = jindex[jn]
        b[2 * i] -= fx
        b[2 * i + 1] -= fy

    x = np.linalg.solve(A, b)

    member_forces = {m: float(x[i]) for i, m in enumerate(members)}
    reactions: dict[str, list[float]] = {jn: [0.0, 0.0] for jn in supports}
    for k, (jn, comp) in enumerate(reaction_cols):
        val = float(x[len(members) + k])
        reactions[jn][0 if comp == "x" else 1] = val
    reactions = {jn: tuple(v) for jn, v in reactions.items()}
    return member_forces, reactions


def _pratt_example():
    """The six-bay Pratt truss of the chapter worked example."""
    joints = {}
    for i in range(7):
        joints[f"L{i}"] = (2.0 * i, 0.0)
    for i in range(1, 6):
        joints[f"U{i}"] = (2.0 * i, 2.0)

    members = [
        ("L0", "L1"), ("L1", "L2"), ("L2", "L3"), ("L3", "L4"),
        ("L4", "L5"), ("L5", "L6"),
        ("U1", "U2"), ("U2", "U3"), ("U3", "U4"), ("U4", "U5"),
        ("L0", "U1"), ("L6", "U5"),
        ("U1", "L1"), ("U2", "L2"), ("U3", "L3"), ("U4", "L4"), ("U5", "L5"),
        ("U1", "L2"), ("U2", "L3"), ("L3", "U4"), ("L4", "U5"),
    ]
    loads = {f"L{i}": (0.0, -20.0) for i in range(1, 6)}  # kN, downward
    supports = {"L0": "pin", "L6": "roller_y"}
    return joints, members, loads, supports


if __name__ == "__main__":
    joints, members, loads, supports = _pratt_example()
    forces, reactions = solve_truss(joints, members, loads, supports)
    print("reactions (kN):")
    for jn, (rx, ry) in reactions.items():
        print(f"  {jn}: Rx={rx:8.3f}  Ry={ry:8.3f}")
    print("member forces (kN, + tension):")
    for m, f in forces.items():
        print(f"  {m[0]:>3}-{m[1]:<3}: {f:8.3f}")
    chord = max(abs(f) for m, f in forces.items()
                if m[0].startswith(("U", "L")))
    print(f"\nmax |chord force| approx {chord:.3f} kN")
