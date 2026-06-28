"""Step-index optical-fibre numerical aperture and acceptance geometry.

Computes the numerical aperture from the core and cladding indices, the
critical angle for total internal reflection at the core-cladding boundary,
and the acceptance half-angle in air at the input face. Reproduces the
telecom-fibre numbers used in the optical-fibre section.
"""

from __future__ import annotations

import math


def numerical_aperture(n_core: float, n_clad: float) -> float:
    """NA = sqrt(n_core^2 - n_clad^2)."""
    return math.sqrt(n_core ** 2 - n_clad ** 2)


def critical_angle(n_core: float, n_clad: float) -> float:
    """Critical angle (rad) inside the core for TIR at the boundary."""
    return math.asin(n_clad / n_core)


def acceptance_angle(n_core: float, n_clad: float, n_outside: float = 1.0) -> float:
    """Acceptance half-angle (rad) in the launch medium (air by default)."""
    return math.asin(numerical_aperture(n_core, n_clad) / n_outside)


if __name__ == "__main__":
    nc, ncl = 1.4500, 1.4467
    na = numerical_aperture(nc, ncl)
    print(f"NA = {na:.4f}")
    print(f"critical angle = {math.degrees(critical_angle(nc, ncl)):.3f} deg")
    print(f"acceptance half-angle = {math.degrees(acceptance_angle(nc, ncl)):.3f} deg")
