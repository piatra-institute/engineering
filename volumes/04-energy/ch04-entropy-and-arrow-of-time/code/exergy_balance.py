"""Component exergy-destruction accounting for a steady-flow process.

Each component destroys exergy at the rate T0 * S_gen_dot, where S_gen_dot is
its entropy-generation rate and T0 is the dead-state (ambient) temperature.
Given the component entropy-generation rates and the inlet fuel exergy, the
function returns the exergy destroyed in each component, the surviving stream,
and the second-law efficiency. Produces the percentages in the chapter's
Grassmann diagram.

Powers in watts, temperatures in kelvin, entropy rates in W/K.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Component:
    name: str
    s_gen: float  # entropy generation rate, W/K


def exergy_report(fuel_exergy: float, t0: float, components: list[Component],
                  useful_work: float) -> None:
    """Print a component-by-component exergy balance and the second-law efficiency."""
    print(f"fuel exergy in      {fuel_exergy / 1e6:8.3f} MW   (100.0 %)")
    total_destroyed = 0.0
    for c in components:
        destroyed = t0 * c.s_gen
        total_destroyed += destroyed
        print(f"  destroyed: {c.name:12s} {destroyed / 1e6:8.3f} MW   "
              f"({100 * destroyed / fuel_exergy:5.1f} %)")
    print(f"useful work out     {useful_work / 1e6:8.3f} MW   "
          f"({100 * useful_work / fuel_exergy:5.1f} %)")
    eta_II = useful_work / fuel_exergy
    print(f"second-law efficiency  {100 * eta_II:5.1f} %")
    accounted = (useful_work + total_destroyed) / fuel_exergy
    print(f"balance closure        {100 * accounted:5.1f} % "
          f"(remainder leaves as rejected-stream exergy)")


def main() -> None:
    t0 = 298.15
    fuel = 100.0e6  # 100 MW of fuel exergy
    components = [
        Component("boiler", s_gen=fuel * 0.45 / t0),
        Component("turbine", s_gen=fuel * 0.05 / t0),
        Component("condenser", s_gen=fuel * 0.10 / t0),
    ]
    # 45 + 5 + 10 destroyed = 60 %; 40 % leaves as useful work; balance closes.
    exergy_report(fuel, t0, components, useful_work=fuel * 0.40)


if __name__ == "__main__":
    main()
