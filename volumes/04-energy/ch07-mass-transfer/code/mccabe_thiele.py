"""Binary McCabe-Thiele stage counter for constant relative volatility.

Steps a staircase between the equilibrium curve y = a x / (1 + (a-1) x)
and the rectifying / stripping operating lines to count equilibrium
stages between the bottoms and distillate specifications. The model
assumes constant molal overflow and a constant relative volatility a.

Usage:
    python mccabe_thiele.py
"""

from __future__ import annotations


def y_eq(x: float, alpha: float) -> float:
    """Vapour mole fraction in equilibrium with liquid x."""
    return alpha * x / (1.0 + (alpha - 1.0) * x)


def x_eq(y: float, alpha: float) -> float:
    """Liquid mole fraction in equilibrium with vapour y (inverse)."""
    return y / (alpha - (alpha - 1.0) * y)


def stages(xD: float, xW: float, zF: float, alpha: float, R: float,
           q: float = 1.0) -> dict:
    """Count equilibrium stages by stepping down from xD to xW.

    xD, xW : distillate and bottoms light-key mole fractions
    zF     : feed composition
    alpha  : relative volatility (light to heavy)
    R      : reflux ratio
    q      : feed thermal quality (1.0 = saturated liquid)
    """
    # rectifying operating line: y = R/(R+1) x + xD/(R+1)
    m_rect = R / (R + 1.0)
    b_rect = xD / (R + 1.0)

    # q-line: y = q/(q-1) x - zF/(q-1); for q = 1 it is vertical at x = zF.
    if abs(q - 1.0) < 1e-9:
        x_pinch = zF
        y_pinch = m_rect * x_pinch + b_rect
    else:
        m_q = q / (q - 1.0)
        b_q = -zF / (q - 1.0)
        x_pinch = (b_q - b_rect) / (m_rect - m_q)
        y_pinch = m_rect * x_pinch + b_rect

    # stripping operating line passes through (xW, xW) and the q-line pinch
    m_strip = (y_pinch - xW) / (x_pinch - xW)
    b_strip = xW - m_strip * xW

    def op_line(x: float) -> float:
        if x >= x_pinch:
            return m_rect * x + b_rect
        return m_strip * x + b_strip

    n = 0
    x = xD
    y = xD            # start on the diagonal at the distillate
    feed_stage = None
    while x > xW and n < 200:
        x = x_eq(y, alpha)        # horizontal step to equilibrium curve
        n += 1
        if feed_stage is None and x <= x_pinch:
            feed_stage = n
        if x <= xW:
            break
        y = op_line(x)            # vertical step to the operating line
    return {"stages": n, "feed_stage": feed_stage,
            "x_pinch": x_pinch, "R_min_slope": m_rect}


if __name__ == "__main__":
    out = stages(xD=0.95, xW=0.05, zF=0.45, alpha=2.4, R=1.8)
    print(f"equilibrium stages : {out['stages']}")
    print(f"feed stage         : {out['feed_stage']}")
