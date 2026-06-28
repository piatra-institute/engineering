"""Thin-lens and lens-maker arithmetic.

Solves the thin-lens imaging equation and the lens-maker's equation under the
sign conventions of Chapter 11: object distance s_o positive for a real
object on the incoming side, image distance s_i positive for a real image on
the outgoing side, focal length f positive for a converging lens. Surface
radius R is positive when the centre of curvature lies on the outgoing side.

Run as a script to reproduce the worked numbers used in the chapter.
"""

from __future__ import annotations


def focal_length(n: float, r1: float, r2: float) -> float:
    """Lens-maker's equation: 1/f = (n - 1)(1/R1 - 1/R2). Radii in metres."""
    return 1.0 / ((n - 1.0) * (1.0 / r1 - 1.0 / r2))


def image_distance(s_o: float, f: float) -> float:
    """Thin-lens equation solved for the image distance s_i."""
    return 1.0 / (1.0 / f - 1.0 / s_o)


def magnification(s_o: float, s_i: float) -> float:
    """Lateral magnification M = -s_i / s_o."""
    return -s_i / s_o


def describe(s_o: float, f: float) -> str:
    s_i = image_distance(s_o, f)
    m = magnification(s_o, s_i)
    real = "real" if s_i > 0 else "virtual"
    orient = "inverted" if m < 0 else "erect"
    return (f"s_i = {s_i*100:.2f} cm, M = {m:.3f} "
            f"({real}, {orient}, |M| = {abs(m):.3f})")


if __name__ == "__main__":
    # Worked example: biconvex BK7 lens, R1 = +75 mm, R2 = -50 mm.
    f = focal_length(n=1.517, r1=+0.075, r2=-0.050)
    print(f"lens-maker focal length: {f*1000:.1f} mm")
    # Object 30 cm in front of a 20 cm converging lens.
    print("object at 30 cm, f = 20 cm:", describe(s_o=0.30, f=0.20))
