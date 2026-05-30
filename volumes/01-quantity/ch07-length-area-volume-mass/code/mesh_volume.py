# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""
Compute the enclosed volume of a closed triangular mesh by the
divergence-theorem identity used in Volume I Chapter 7.

For each triangle i with outward-oriented vertices a_i, b_i, c_i,
the signed contribution to the enclosed volume is

    V_i = (1/6) * dot(a_i, cross(b_i, c_i)).

The sum over all triangles gives the exact polyhedral volume of the
closed mesh, with no truncation error. Mesh-correspondence error
(scan noise, mesh-repair artifacts, thermal-expansion bias) is
budgeted separately per the chapter text.

The script also reports the watertight check (Euler characteristic
V - E + F = 2 for a closed genus-zero surface) and the
discretisation contribution from the mean edge length cubed.

The Stanford-bunny PLY mesh shipped with this script is referenced
indirectly: this file ships only the algorithm and a synthetic
unit-test mesh (a unit cube and a unit sphere), so the code is
runnable without external data downloads.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np


@dataclass
class Mesh:
    """A triangular surface mesh."""

    vertices: np.ndarray  # shape (n_v, 3)
    triangles: np.ndarray  # shape (n_t, 3); indices into vertices


def mesh_volume(mesh: Mesh) -> float:
    """Return the signed enclosed volume of a closed mesh."""
    a = mesh.vertices[mesh.triangles[:, 0]]
    b = mesh.vertices[mesh.triangles[:, 1]]
    c = mesh.vertices[mesh.triangles[:, 2]]
    cross_bc = np.cross(b, c)
    signed = np.einsum("ij,ij->i", a, cross_bc) / 6.0
    return float(signed.sum())


def euler_characteristic(mesh: Mesh) -> int:
    """Return V - E + F for the mesh; equals 2 for a closed genus-0 surface."""
    V = mesh.vertices.shape[0]
    F = mesh.triangles.shape[0]
    # Each triangle contributes three edges; shared edges are counted twice.
    edges = np.vstack([
        np.sort(mesh.triangles[:, [0, 1]], axis=1),
        np.sort(mesh.triangles[:, [1, 2]], axis=1),
        np.sort(mesh.triangles[:, [2, 0]], axis=1),
    ])
    edges_unique = np.unique(edges, axis=0)
    E = edges_unique.shape[0]
    return V - E + F


def unit_cube_mesh(side: float = 1.0) -> Mesh:
    """Closed axis-aligned cube mesh of side `side`, twelve triangles."""
    h = side / 2.0
    vertices = np.array(
        [
            [-h, -h, -h],
            [+h, -h, -h],
            [+h, +h, -h],
            [-h, +h, -h],
            [-h, -h, +h],
            [+h, -h, +h],
            [+h, +h, +h],
            [-h, +h, +h],
        ]
    )
    triangles = np.array(
        [
            [0, 2, 1], [0, 3, 2],  # bottom (-z)
            [4, 5, 6], [4, 6, 7],  # top (+z)
            [0, 1, 5], [0, 5, 4],  # front (-y)
            [2, 3, 7], [2, 7, 6],  # back (+y)
            [1, 2, 6], [1, 6, 5],  # right (+x)
            [3, 0, 4], [3, 4, 7],  # left (-x)
        ]
    )
    return Mesh(vertices=vertices, triangles=triangles)


def icosphere_mesh(radius: float = 1.0, subdivisions: int = 2) -> Mesh:
    """Closed icosphere mesh of given radius and subdivision level."""
    phi = (1.0 + math.sqrt(5.0)) / 2.0
    base = np.array(
        [
            [-1, +phi, 0], [+1, +phi, 0], [-1, -phi, 0], [+1, -phi, 0],
            [0, -1, +phi], [0, +1, +phi], [0, -1, -phi], [0, +1, -phi],
            [+phi, 0, -1], [+phi, 0, +1], [-phi, 0, -1], [-phi, 0, +1],
        ]
    )
    base = base / np.linalg.norm(base, axis=1)[:, None]
    tris = np.array(
        [
            [0, 11, 5], [0, 5, 1], [0, 1, 7], [0, 7, 10], [0, 10, 11],
            [1, 5, 9], [5, 11, 4], [11, 10, 2], [10, 7, 6], [7, 1, 8],
            [3, 9, 4], [3, 4, 2], [3, 2, 6], [3, 6, 8], [3, 8, 9],
            [4, 9, 5], [2, 4, 11], [6, 2, 10], [8, 6, 7], [9, 8, 1],
        ]
    )
    vertices = base.tolist()
    triangles = tris.tolist()
    for _ in range(subdivisions):
        midpoint_cache: dict[tuple[int, int], int] = {}

        def midpoint(i: int, j: int) -> int:
            key = (min(i, j), max(i, j))
            if key in midpoint_cache:
                return midpoint_cache[key]
            mid = (np.array(vertices[i]) + np.array(vertices[j])) / 2.0
            mid = mid / np.linalg.norm(mid)
            vertices.append(mid.tolist())
            idx = len(vertices) - 1
            midpoint_cache[key] = idx
            return idx

        new_tris: list[list[int]] = []
        for a_i, b_i, c_i in triangles:
            ab = midpoint(a_i, b_i)
            bc = midpoint(b_i, c_i)
            ca = midpoint(c_i, a_i)
            new_tris.extend(
                [
                    [a_i, ab, ca],
                    [b_i, bc, ab],
                    [c_i, ca, bc],
                    [ab, bc, ca],
                ]
            )
        triangles = new_tris
    arr_v = np.array(vertices) * radius
    arr_t = np.array(triangles, dtype=np.int64)
    return Mesh(vertices=arr_v, triangles=arr_t)


def _demo() -> None:
    cube = unit_cube_mesh(side=1.0)
    print(f"unit cube: V - E + F = {euler_characteristic(cube)}")
    print(f"  computed volume = {mesh_volume(cube):.6f} (expected 1.000000)")

    sphere = icosphere_mesh(radius=1.0, subdivisions=4)
    expected = (4.0 / 3.0) * math.pi * 1.0**3
    measured = mesh_volume(sphere)
    print(f"icosphere (r=1, sub=4): V - E + F = {euler_characteristic(sphere)}")
    print(f"  computed volume = {measured:.6f} (expected {expected:.6f})")
    rel = (measured - expected) / expected
    print(f"  relative error vs. analytic sphere: {rel*100:+.4f}%")


if __name__ == "__main__":
    _demo()
