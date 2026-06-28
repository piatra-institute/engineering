"""Modified nodal analysis (MNA) for resistive DC circuits.

Build the conductance matrix from a netlist of resistors, independent
current sources, and independent voltage sources, then solve for the node
voltages. The procedure is the linear-algebra core of every SPICE-style
simulator: stamp each element into a system matrix, then invert.

Netlist convention: nodes are integers, node 0 is ground (reference).
Each element is a tuple (kind, n_plus, n_minus, value):
  ('R', a, b, ohms)    resistor between nodes a and b
  ('I', a, b, amps)    current source forcing current from a to b
  ('V', a, b, volts)   voltage source fixing v(a) - v(b)

Units: ohms, amperes, volts. No dependent sources in this minimal version.
"""

from __future__ import annotations

import numpy as np


def solve_dc(netlist, n_nodes):
    """Return node voltages (node 0 = ground) for a resistive DC circuit.

    Uses modified nodal analysis so that ideal voltage sources are handled
    by adding one extra unknown (the source current) per source.
    """
    v_sources = [e for e in netlist if e[0] == "V"]
    n_unknowns = (n_nodes - 1) + len(v_sources)
    A = np.zeros((n_unknowns, n_unknowns))
    z = np.zeros(n_unknowns)

    def idx(node):
        # node 0 is ground and has no row/column
        return node - 1

    for kind, a, b, val in netlist:
        if kind == "R":
            g = 1.0 / val
            for n in (a, b):
                if n != 0:
                    A[idx(n), idx(n)] += g
            if a != 0 and b != 0:
                A[idx(a), idx(b)] -= g
                A[idx(b), idx(a)] -= g
        elif kind == "I":
            if a != 0:
                z[idx(a)] -= val
            if b != 0:
                z[idx(b)] += val

    # stamp voltage sources into the bordered block
    row = n_nodes - 1
    for k, (kind, a, b, val) in enumerate(v_sources):
        r = row + k
        if a != 0:
            A[r, idx(a)] += 1.0
            A[idx(a), r] += 1.0
        if b != 0:
            A[r, idx(b)] -= 1.0
            A[idx(b), r] -= 1.0
        z[r] = val

    x = np.linalg.solve(A, z)
    voltages = np.concatenate(([0.0], x[: n_nodes - 1]))
    return voltages


if __name__ == "__main__":
    # A 12 V source through 100 ohm into a node, then 50 ohm to ground.
    # Expect v(1) = 12 * 50/150 = 4.0 V.
    net = [
        ("V", 2, 0, 12.0),
        ("R", 2, 1, 100.0),
        ("R", 1, 0, 50.0),
    ]
    v = solve_dc(net, n_nodes=3)
    print("node voltages (V):", np.round(v, 4))
    print("expected v(1) = 4.0 V")
