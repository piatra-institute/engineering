"""Richardson extrapolation for a mesh-convergence study.

Given a quantity of interest computed on three meshes with a constant
refinement ratio r (element-size ratio), estimate the observed order of
convergence p and the mesh-independent (extrapolated) value:

    p = ln( (f1 - f2) / (f2 - f3) ) / ln(r)
    f_exact ~= f3 + (f3 - f2) / (r^p - 1)

where f1, f2, f3 are coarse-to-fine results. Run with:
python richardson_convergence.py
"""

import math


def richardson(f1, f2, f3, r):
    p = math.log((f1 - f2) / (f2 - f3)) / math.log(r)
    f_exact = f3 + (f3 - f2) / (r**p - 1.0)
    gci = abs((f3 - f2) / f3) / (r**p - 1.0)   # grid-convergence index (rel.)
    return p, f_exact, gci


if __name__ == "__main__":
    # Peak stress at a hole on three meshes, refinement ratio 2 (MPa).
    f1, f2, f3 = 128.0, 139.0, 146.0
    p, f_exact, gci = richardson(f1, f2, f3, r=2.0)
    print(f"observed order p   = {p:.2f}")
    print(f"extrapolated value = {f_exact:.1f} MPa  (analytic 150)")
    print(f"grid-convergence index on finest mesh = {gci*100:.1f} %")
