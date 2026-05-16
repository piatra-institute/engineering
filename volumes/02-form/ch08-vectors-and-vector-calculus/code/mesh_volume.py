# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy>=1.26"]
# ///
"""Divergence-theorem volume of a closed triangulated surface.

Implements the per-triangle signed tetrahedron formula

    V = (1/6) sum_T  p1 . (p2 x p3)

where the sum runs over all oriented triangles T with vertices
(p1, p2, p3) in consistent outward-pointing order.

The script reads a Wavefront-style ``.obj`` mesh (vertices and triangle
faces only), computes the divergence-theorem volume, and reports the
result. A second routine computes the surface area as the sum of
triangle areas, for cross-checking against a separate measurement.

Reference: Zhang and Chen (2001), Efficient feature extraction for
2D/3D objects in mesh representation.

Usage:
    uv run mesh_volume.py ../data/unit_cube.obj
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np


def load_obj(path: Path) -> tuple[np.ndarray, np.ndarray]:
    """Parse vertex (``v``) and face (``f``) lines from a minimal ``.obj``.

    Returns ``(vertices, faces)`` where ``vertices`` has shape (n, 3)
    and ``faces`` has shape (m, 3) of 0-based vertex indices.
    """
    verts: list[tuple[float, float, float]] = []
    faces: list[tuple[int, int, int]] = []
    for raw in path.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if parts[0] == "v" and len(parts) >= 4:
            verts.append((float(parts[1]), float(parts[2]), float(parts[3])))
        elif parts[0] == "f" and len(parts) >= 4:
            # Drop texture/normal indices; convert to 0-based.
            idx = [int(tok.split("/")[0]) - 1 for tok in parts[1:4]]
            faces.append((idx[0], idx[1], idx[2]))
    return np.array(verts), np.array(faces, dtype=int)


def signed_volume(vertices: np.ndarray, faces: np.ndarray) -> float:
    """Divergence-theorem volume of a closed triangulated mesh.

    Sign is positive when face vertex order is counterclockwise as seen
    from outside the enclosed region. A negative result indicates a
    uniformly inverted orientation convention.
    """
    p1 = vertices[faces[:, 0]]
    p2 = vertices[faces[:, 1]]
    p3 = vertices[faces[:, 2]]
    triple = np.einsum("ij,ij->i", p1, np.cross(p2, p3))
    return float(triple.sum() / 6.0)


def surface_area(vertices: np.ndarray, faces: np.ndarray) -> float:
    """Sum of triangle areas; orientation-independent."""
    p1 = vertices[faces[:, 0]]
    p2 = vertices[faces[:, 1]]
    p3 = vertices[faces[:, 2]]
    cross = np.cross(p2 - p1, p3 - p1)
    return float(np.linalg.norm(cross, axis=1).sum() / 2.0)


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: mesh_volume.py <mesh.obj>", file=sys.stderr)
        return 2
    path = Path(argv[1])
    vertices, faces = load_obj(path)
    vol = signed_volume(vertices, faces)
    area = surface_area(vertices, faces)
    print(f"mesh:          {path.name}")
    print(f"vertices:      {len(vertices)}")
    print(f"triangles:     {len(faces)}")
    print(f"signed volume: {vol:.6f}")
    print(f"surface area:  {area:.6f}")
    if vol < 0:
        print(
            "warning: negative signed volume implies inverted orientation; "
            "reverse triangle vertex order.",
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
