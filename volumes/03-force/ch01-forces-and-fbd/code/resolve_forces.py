"""
Resolve a list of planar forces into Cartesian components, sum them, and
report the resultant force and the net moment about a chosen point.

Supports:
  - Volume III, Chapter 1, "Force as a vector" and "Free-body diagrams"
  - The concurrent-force and rigid-body equilibrium checks in the worked
    examples and exercises.

A force is given by its magnitude, its line-of-action angle measured
counterclockwise from the +x axis (degrees), and the (x, y) point at
which it is applied. The net moment uses the 2D cross product
M = r_x * F_y - r_y * F_x, counterclockwise positive.

Dependencies:
  numpy

Usage:
  python resolve_forces.py            # runs the ladder demo
"""

import math
from dataclasses import dataclass

import numpy as np


@dataclass
class Force:
    magnitude: float          # newtons
    angle_deg: float          # CCW from +x
    point: tuple              # (x, y) point of application, metres
    name: str = ""

    def components(self) -> np.ndarray:
        a = math.radians(self.angle_deg)
        return self.magnitude * np.array([math.cos(a), math.sin(a)])


def resultant(forces) -> np.ndarray:
    """Vector sum of the force components."""
    return sum((f.components() for f in forces), np.zeros(2))


def net_moment(forces, about=(0.0, 0.0)) -> float:
    """Net moment about `about`, CCW positive (2D scalar cross product)."""
    o = np.asarray(about, dtype=float)
    m = 0.0
    for f in forces:
        r = np.asarray(f.point, dtype=float) - o
        fx, fy = f.components()
        m += r[0] * fy - r[1] * fx
    return m


def is_equilibrium(forces, about=(0.0, 0.0), tol=1e-6) -> bool:
    """True if sum F and net moment both vanish to tolerance."""
    R = resultant(forces)
    M = net_moment(forces, about)
    return bool(np.linalg.norm(R) < tol and abs(M) < tol)


def demo_ladder():
    """Uniform ladder, L = 4 m, m = 12 kg, theta = 60 deg.

    Solve N_W, N_F, F_f from the closed-form result and confirm the
    force list is in equilibrium.
    """
    g, m, L, theta = 9.81, 12.0, 4.0, math.radians(60.0)
    N_F = m * g
    N_W = m * g / (2.0 * math.tan(theta))
    F_f = N_W
    foot = (L * math.cos(theta), 0.0)   # foot on the floor
    top = (0.0, L * math.sin(theta))    # against the wall
    mid = (foot[0] / 2.0, top[1] / 2.0)

    forces = [
        Force(m * g, -90.0, mid, "weight"),
        Force(N_W, 0.0, top, "wall normal"),     # horizontal, away from wall
        Force(N_F, 90.0, foot, "floor normal"),  # straight up
        Force(F_f, 180.0, foot, "floor friction"),  # toward the wall
    ]
    print(f"N_W = {N_W:7.2f} N   N_F = {N_F:7.2f} N   F_f = {F_f:7.2f} N")
    print(f"min mu_s = {F_f / N_F:.3f}  (closed form 1/(2 tan th) = "
          f"{1/(2*math.tan(theta)):.3f})")
    print(f"resultant = {resultant(forces)}  net moment(foot) = "
          f"{net_moment(forces, foot):.3e}")
    print(f"equilibrium: {is_equilibrium(forces, about=foot)}")


if __name__ == "__main__":
    demo_ladder()
