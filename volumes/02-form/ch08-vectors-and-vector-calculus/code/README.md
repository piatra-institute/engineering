# Code for Vol II Ch 8 (Vectors and vector calculus)

Two `uv`-runnable scripts implement the chapter's working tools.

## Files

| Script | Purpose |
|---|---|
| `mesh_volume.py` | Reads a minimal Wavefront `.obj` mesh and prints the divergence-theorem signed volume and the surface area. |
| `triple_product_sweep.py` | Builds three reference meshes (unit cube, regular tetrahedron, geodesic icosphere at three refinements) and reports the relative error of the divergence-theorem volume against the analytical value. |

## Usage

```
uv run mesh_volume.py ../data/unit_cube.obj
uv run triple_product_sweep.py
```

Both scripts carry PEP 723 inline metadata; `uv` resolves `numpy` automatically.

## What the sweep shows

On a clean run the cube and tetrahedron reproduce the analytical volume to floating-point precision. The icosphere converges at second order in the mesh edge length: refining the mesh from 320 to 5120 triangles reduces the relative error from about $3 \times 10^{-2}$ to $2 \times 10^{-3}$, the expected fifteenfold gain. The reader who finds a sign-reversed result on either reference shape has produced a uniformly inverted orientation convention; the chapter's failure section is the remedy.

## Data

The companion `../data/` directory carries the three reference `.obj` meshes the `mesh_volume.py` script can read, plus a CSV of the sweep output for cross-reference.
