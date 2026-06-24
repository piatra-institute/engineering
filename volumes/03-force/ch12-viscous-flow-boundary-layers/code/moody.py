"""Friction factor for pipe flow: laminar formula plus the Colebrook=White
solve and its explicit Haaland approximation.

The Colebrook=White relation is implicit in f and is solved here by fixed-
point iteration on 1/sqrt(f). The Haaland form is explicit and accurate to
within a couple of percent across the engineering range, which is why it is
the workhorse for direct calculation.

Run:
    python moody.py
to reproduce the friction-factor table used in the chapter's Moody figure.
"""

from __future__ import annotations

import math


def f_laminar(Re: float) -> float:
    """Darcy friction factor in the laminar regime, exact under Hagen=
    Poiseuille assumptions. Valid for Re below about 2300."""
    return 64.0 / Re


def f_colebrook(Re: float, rel_rough: float, tol: float = 1e-10) -> float:
    """Darcy friction factor from the Colebrook=White relation, by fixed-
    point iteration. rel_rough is the relative roughness epsilon/D."""
    # Start from the Haaland estimate, then iterate the implicit relation.
    inv_sqrt_f = -1.8 * math.log10((rel_rough / 3.7) ** 1.11 + 6.9 / Re)
    for _ in range(100):
        f = 1.0 / inv_sqrt_f**2
        rhs = -2.0 * math.log10(rel_rough / 3.7 + 2.51 / (Re * math.sqrt(f)))
        if abs(rhs - inv_sqrt_f) < tol:
            inv_sqrt_f = rhs
            break
        inv_sqrt_f = rhs
    return 1.0 / inv_sqrt_f**2


def f_haaland(Re: float, rel_rough: float) -> float:
    """Explicit Haaland approximation to the Colebrook=White friction
    factor. The standard direct-calculation form."""
    inv_sqrt_f = -1.8 * math.log10((rel_rough / 3.7) ** 1.11 + 6.9 / Re)
    return 1.0 / inv_sqrt_f**2


def friction_factor(Re: float, rel_rough: float = 0.0) -> float:
    """Regime-aware friction factor: laminar below 2300, Colebrook above
    4000, linear blend across the transitional band."""
    if Re < 2300.0:
        return f_laminar(Re)
    if Re > 4000.0:
        return f_colebrook(Re, rel_rough)
    f_lam = f_laminar(2300.0)
    f_turb = f_colebrook(4000.0, rel_rough)
    w = (Re - 2300.0) / (4000.0 - 2300.0)
    return (1.0 - w) * f_lam + w * f_turb


if __name__ == "__main__":
    print(f"{'Re':>10} {'eps/D':>8} {'Colebrook':>12} {'Haaland':>10}")
    for Re in (4e3, 1e4, 3e4, 1e5, 3e5, 1e6, 1e7, 1e8):
        for er in (0.0, 1e-3, 1e-2):
            fc = f_colebrook(Re, er)
            fh = f_haaland(Re, er)
            print(f"{Re:10.0f} {er:8.4f} {fc:12.5f} {fh:10.5f}")
