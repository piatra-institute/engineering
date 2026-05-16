"""
Uncertainty propagation per ISO/IEC GUM: Type A and Type B evaluation,
linear and product propagation rules in the small-error limit.

Supports the chapter's discussion of GUM uncertainty evaluation and
the derivation exercises on uncertainty propagation.

Dependencies:
  numpy (only for the Type A demonstration; the propagation rules are
  pure-Python).

Usage:
  python uncertainty_propagation.py
"""

from dataclasses import dataclass
from math import sqrt


@dataclass(frozen=True)
class Measurement:
    """A measured quantity with its standard uncertainty.

    The unit is carried explicitly to enforce the chapter's discipline
    that every quantity at every step carries its unit.
    """
    value: float
    standard_uncertainty: float
    unit: str

    def __post_init__(self) -> None:
        if self.standard_uncertainty < 0:
            raise ValueError("standard uncertainty cannot be negative")

    def expand(self, k: float = 2.0) -> tuple[float, float, str]:
        """Return (value, expanded_uncertainty, unit) at coverage k."""
        return self.value, k * self.standard_uncertainty, self.unit


def type_a_evaluation(readings: list[float], unit: str) -> Measurement:
    """Type A: standard uncertainty from the standard deviation of the
    sample mean of n readings."""
    n = len(readings)
    if n < 2:
        raise ValueError("Type A evaluation requires at least 2 readings")
    mean = sum(readings) / n
    s2 = sum((r - mean) ** 2 for r in readings) / (n - 1)
    u = sqrt(s2 / n)
    return Measurement(value=mean, standard_uncertainty=u, unit=unit)


def type_b_uniform(half_width: float, value: float,
                   unit: str) -> Measurement:
    """Type B: standard uncertainty from a uniform distribution of given
    half-width (e.g., from an instrument's stated resolution)."""
    u = half_width / sqrt(3.0)
    return Measurement(value=value, standard_uncertainty=u, unit=unit)


def combine_quadrature(*components: Measurement) -> float:
    """Combined standard uncertainty for uncorrelated components.

    Returns the combined standard uncertainty only; the caller is
    responsible for combining with a value and unit.
    """
    return sqrt(sum(c.standard_uncertainty ** 2 for c in components))


def propagate_product(x: Measurement, y: Measurement, unit_z: str) -> Measurement:
    """Propagation rule for z = x * y in the small-error limit, x, y
    uncorrelated. Returns the product value with its standard uncertainty."""
    value = x.value * y.value
    rel_u_x = x.standard_uncertainty / abs(x.value) if x.value else 0.0
    rel_u_y = y.standard_uncertainty / abs(y.value) if y.value else 0.0
    rel_u_z = sqrt(rel_u_x ** 2 + rel_u_y ** 2)
    return Measurement(value=value, standard_uncertainty=abs(value) * rel_u_z,
                       unit=unit_z)


def propagate_sum(x: Measurement, y: Measurement, unit_z: str,
                  rho: float = 0.0) -> Measurement:
    """Propagation rule for z = x + y in the small-error limit,
    correlation rho. Returns z's value and standard uncertainty."""
    if x.unit != y.unit:
        raise ValueError(f"unit mismatch: {x.unit} vs {y.unit}")
    value = x.value + y.value
    u_z = sqrt(x.standard_uncertainty ** 2 + y.standard_uncertainty ** 2
               + 2 * rho * x.standard_uncertainty * y.standard_uncertainty)
    return Measurement(value=value, standard_uncertainty=u_z, unit=unit_z)


def main() -> None:
    # Example 1: Type A from a series of readings of the same voltage.
    voltage_readings = [5.012, 5.008, 5.015, 5.011, 5.009, 5.014, 5.010]
    v = type_a_evaluation(voltage_readings, unit="V")
    print(f"Type A: V = {v.value:.4f} ± {v.standard_uncertainty:.4f} V "
          f"(from {len(voltage_readings)} readings)")

    # Example 2: Type B from instrument resolution.
    res = type_b_uniform(half_width=0.005, value=5.00, unit="V")
    print(f"Type B: V = {res.value:.4f} ± {res.standard_uncertainty:.4f} V "
          f"(from ±0.005 V resolution)")

    # Combined uncertainty (Type A and Type B for the same measurand).
    combined_u = combine_quadrature(v, res)
    print(f"Combined u_c = {combined_u:.4f} V")
    print(f"Expanded U (k=2) = {2 * combined_u:.4f} V")

    # Example 3: propagation through a product (P = V * I).
    current = Measurement(value=0.100, standard_uncertainty=0.001, unit="A")
    power = propagate_product(v, current, unit_z="W")
    print(f"P = V * I = {power.value:.4f} ± {power.standard_uncertainty:.5f} W")

    # Example 4: propagation through a sum (m_total = m_1 + m_2),
    # correlated and uncorrelated.
    m1 = Measurement(value=2.500, standard_uncertainty=0.010, unit="kg")
    m2 = Measurement(value=1.250, standard_uncertainty=0.008, unit="kg")
    m_uncorr = propagate_sum(m1, m2, unit_z="kg", rho=0.0)
    m_corr = propagate_sum(m1, m2, unit_z="kg", rho=0.9)
    print(f"m_total (rho=0)   = {m_uncorr.value:.4f} ± "
          f"{m_uncorr.standard_uncertainty:.4f} kg")
    print(f"m_total (rho=0.9) = {m_corr.value:.4f} ± "
          f"{m_corr.standard_uncertainty:.4f} kg")


if __name__ == "__main__":
    main()
