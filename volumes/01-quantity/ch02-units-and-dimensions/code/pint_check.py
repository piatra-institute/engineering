"""
Runtime dimensional-consistency checking with Pint.

Demonstrates the pattern that the Vol I Ch 2 "Unit-error audit"
subsection recommends: attach a unit to every literal at the boundary
between code and physical reality, let the library raise a
DimensionalityError when an unsafe operation is attempted, and read
the result in the unit a downstream system expects.

The three worked cases reproduce the textbook examples:

  1. The Mars Climate Orbiter style failure: an impulse intended in
     newton-seconds and delivered in pound-force-seconds. Pint will
     convert the second silently because the dimensions match; the
     lesson is that dimensional consistency is necessary, not
     sufficient.
  2. The vincristine-overdose pattern: a dose intended in micrograms,
     prescribed as milligrams. Pint enforces the unit attachment;
     the comparison to a safe-dose-range limit catches the
     three-order-of-magnitude error.
  3. The Schiaparelli-style attitude case: a saturated rate sensor
     integrating to an attitude that flips the altimeter's sign.
     Pint does not catch the saturation itself; the sign check on
     the integrated altitude does.

Dependencies:
  pip install pint  (or `uv add pint`).

Usage:
  python pint_check.py
"""

from pint import UnitRegistry, DimensionalityError

ureg = UnitRegistry()
Q = ureg.Quantity


def case_one_impulse_unit_mismatch() -> None:
    """Newton-seconds vs pound-force-seconds, the MCO pattern."""
    delivered = Q(4.45, "lbf*s")
    intended_total = Q(100.0, "N*s")
    try:
        residual = intended_total - delivered
        print(f"residual impulse: {residual.to('N*s'):.3f}")
    except DimensionalityError as exc:
        print(f"DimensionalityError caught: {exc}")
    # Both are dimensionally [M][L][T]^{-1}; the subtraction runs.
    # Pint converts and the conversion factor of 4.45 is applied.
    # The lesson: catch this class of failure with a value-range
    # check, not the type system. See Mars Climate Orbiter (1999).
    converted = delivered.to("N*s")
    print(f"delivered = {delivered} = {converted:.3f} (factor 4.45)")


def case_two_vincristine_dose() -> None:
    """Microgram vs milligram for vincristine intrathecal limit."""
    safe_max_intrathecal = Q(0.0, "mg")  # vincristine: never IT
    prescribed = Q(2000.0, "ug")  # transcribed as 2 mg
    try:
        if prescribed.to("mg") > safe_max_intrathecal:
            print(
                f"REFUSE: prescribed {prescribed.to('mg')} "
                f"exceeds intrathecal limit {safe_max_intrathecal}"
            )
    except DimensionalityError as exc:
        print(f"DimensionalityError: {exc}")
    # Pint enforces dimensional consistency but cannot tell mg from
    # ug at the boundary if both arrive as numbers from a paper
    # form. Unit attachment must happen at the human-machine
    # interface, with a confirmation step, not silently downstream.


def case_three_attitude_altitude() -> None:
    """Saturated angular rate integrating to a negative altitude."""
    saturated_rate = Q(1.0, "rad/s")
    duration = Q(1.0, "s")
    integrated_angle = saturated_rate * duration
    print(f"integrated angle: {integrated_angle.to('rad'):.3f}")
    measured_altitude = Q(3.7, "km")
    spurious = -measured_altitude
    if spurious.magnitude < 0:
        print(
            f"REFUSE altitude {spurious}: negative; "
            f"reset to ground-truth radar reading"
        )


if __name__ == "__main__":
    print("--- Case 1: impulse units (MCO pattern) ---")
    case_one_impulse_unit_mismatch()
    print()
    print("--- Case 2: dose units (vincristine pattern) ---")
    case_two_vincristine_dose()
    print()
    print("--- Case 3: attitude/altitude (Schiaparelli pattern) ---")
    case_three_attitude_altitude()
