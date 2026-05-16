# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy>=1.26"]
# ///
"""Sanity sweep for the divergence-theorem volume formula.

Generates three reference meshes (a unit cube, a regular tetrahedron, a
geodesic sphere of varying refinement), computes their signed
divergence-theorem volume, and reports the relative error against the
analytical volume. The sphere case exhibits the expected second-order
convergence of the piecewise-flat approximation.

Usage:
    uv run triple_product_sweep.py
"""

from __future__ import annotations

import numpy as np

from mesh_volume import signed_volume


def unit_cube() -> tuple[np.ndarray, np.ndarray]:
    """Unit cube with 8 vertices and 12 outward-oriented triangles."""
    v = np.array(
        [
            [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
            [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1],
        ],
        dtype=float,
    )
    f = np.array(
        [
            [0, 3, 2], [0, 2, 1],  # bottom (z=0), outward = -z
            [4, 5, 6], [4, 6, 7],  # top (z=1), outward = +z
            [0, 1, 5], [0, 5, 4],  # front (y=0), outward = -y
            [2, 3, 7], [2, 7, 6],  # back (y=1), outward = +y
            [1, 2, 6], [1, 6, 5],  # right (x=1), outward = +x
            [0, 4, 7], [0, 7, 3],  # left (x=0), outward = -x
        ],
        dtype=int,
    )
    return v, f


def tetrahedron() -> tuple[np.ndarray, np.ndarray]:
    """Regular tetrahedron inscribed in the unit cube; volume 1/3."""
    v = np.array(
        [[0, 0, 0], [1, 1, 0], [1, 0, 1], [0, 1, 1]],
        dtype=float,
    )
    # Outward-oriented winding (CCW from outside) verified by signed-volume sign.
    f = np.array(
        [[0, 1, 2], [0, 3, 1], [0, 2, 3], [1, 3, 2]],
        dtype=int,
    )
    return v, f


def icosphere(refine: int = 2) -> tuple[np.ndarray, np.ndarray]:
    """Geodesic unit sphere via icosahedron subdivision; volume 4 pi / 3."""
    phi = (1.0 + np.sqrt(5.0)) / 2.0
    verts = np.array(
        [
            [-1, phi, 0], [1, phi, 0], [-1, -phi, 0], [1, -phi, 0],
            [0, -1, phi], [0, 1, phi], [0, -1, -phi], [0, 1, -phi],
            [phi, 0, -1], [phi, 0, 1], [-phi, 0, -1], [-phi, 0, 1],
        ],
        dtype=float,
    )
    verts /= np.linalg.norm(verts, axis=1, keepdims=True)
    faces = np.array(
        [
            [0, 11, 5], [0, 5, 1], [0, 1, 7], [0, 7, 10], [0, 10, 11],
            [1, 5, 9], [5, 11, 4], [11, 10, 2], [10, 7, 6], [7, 1, 8],
            [3, 9, 4], [3, 4, 2], [3, 2, 6], [3, 6, 8], [3, 8, 9],
            [4, 9, 5], [2, 4, 11], [6, 2, 10], [8, 6, 7], [9, 8, 1],
        ],
        dtype=int,
    )
    for _ in range(refine):
        verts_list = verts.tolist()
        cache: dict[tuple[int, int], int] = {}

        def midpoint(a: int, b: int) -> int:
            key = (min(a, b), max(a, b))
            if key in cache:
                return cache[key]
            m = (np.array(verts_list[a]) + np.array(verts_list[b])) / 2.0
            m /= np.linalg.norm(m)
            verts_list.append(m.tolist())
            idx = len(verts_list) - 1
            cache[key] = idx
            return idx

        new_faces: list[list[int]] = []
        for a, b, c in faces:
            ab = midpoint(a, b)
            bc = midpoint(b, c)
            ca = midpoint(c, a)
            new_faces.extend(
                [[a, ab, ca], [b, bc, ab], [c, ca, bc], [ab, bc, ca]]
            )
        verts = np.array(verts_list)
        faces = np.array(new_faces, dtype=int)
    return verts, faces


def main() -> int:
    cases = [
        ("unit cube", *unit_cube(), 1.0),
        ("regular tetrahedron", *tetrahedron(), 1.0 / 3.0),
        ("icosphere (refine=0)", *icosphere(0), 4.0 * np.pi / 3.0),
        ("icosphere (refine=2)", *icosphere(2), 4.0 * np.pi / 3.0),
        ("icosphere (refine=4)", *icosphere(4), 4.0 * np.pi / 3.0),
    ]
    print(f"{'case':<24} {'tris':>6} {'V_DT':>12} {'V_true':>12} {'rel.err':>10}")
    for name, verts, faces, v_true in cases:
        v_dt = signed_volume(verts, faces)
        rel = abs(v_dt - v_true) / v_true
        print(f"{name:<24} {len(faces):>6} {v_dt:>12.6f} {v_true:>12.6f} {rel:>10.2e}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
