"""Centroid and second moment of area of a composite planar section
built from axis-aligned rectangles, with the parallel-axis theorem
applied automatically.

A section is given as a list of rectangles, each (width b, height h,
x-centre, y-centre). Negative-area rectangles model holes. The routine
returns the area-weighted centroid and the second moment of area about
the horizontal and vertical centroidal axes.

Verified in the chapter against I = b h^3 / 12 for a single rectangle
and against the rolled-I-section exercise.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Rect:
    b: float   # width  (x-extent)
    h: float   # height (y-extent)
    xc: float  # centroid x
    yc: float  # centroid y
    hole: bool = False

    @property
    def area(self) -> float:
        a = self.b * self.h
        return -a if self.hole else a

    @property
    def Ix_self(self) -> float:
        # about own horizontal centroidal axis
        return self.b * self.h ** 3 / 12.0

    @property
    def Iy_self(self) -> float:
        return self.h * self.b ** 3 / 12.0


def section_properties(rects):
    """Return (A, xbar, ybar, Ix, Iy) for the composite section.

    Ix, Iy are second moments about the composite centroidal axes.
    """
    A = sum(r.area for r in rects)
    if A == 0:
        raise ValueError("section has zero net area")
    xbar = sum(r.area * r.xc for r in rects) / A
    ybar = sum(r.area * r.yc for r in rects) / A

    Ix = 0.0
    Iy = 0.0
    for r in rects:
        sign = -1.0 if r.hole else 1.0
        dy = r.yc - ybar
        dx = r.xc - xbar
        Ix += sign * (r.Ix_self + r.b * r.h * dy ** 2)
        Iy += sign * (r.Iy_self + r.b * r.h * dx ** 2)
    return A, xbar, ybar, Ix, Iy


if __name__ == "__main__":
    # single rectangle 50 mm x 300 mm: I = b h^3/12
    one = [Rect(b=0.05, h=0.30, xc=0.0, yc=0.0)]
    A, xb, yb, Ix, Iy = section_properties(one)
    print(f"rectangle: Ix = {Ix:.4e} m^4  (b h^3/12 = {0.05*0.30**3/12:.4e})")

    # rolled I-section: flanges 200x20, web 200x10, total depth 240 (mm)
    mm = 1e-3
    flange_b, flange_t = 200 * mm, 20 * mm
    web_h, web_t = 200 * mm, 10 * mm
    total = 2 * flange_t + web_h
    rects = [
        Rect(flange_b, flange_t, 0.0, total / 2 - flange_t / 2),         # top
        Rect(web_t, web_h, 0.0, 0.0),                                    # web (centred)
        Rect(flange_b, flange_t, 0.0, -(total / 2 - flange_t / 2)),      # bottom
    ]
    A, xb, yb, Ix, Iy = section_properties(rects)
    print(f"I-section: A = {A*1e6:.1f} mm^2, Ix = {Ix:.4e} m^4")
