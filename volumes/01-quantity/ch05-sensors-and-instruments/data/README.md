# Data assets - Volume I, Chapter 5 (Sensors and instruments)

## Files

| File | Source | Used by |
|---|---|---|
| `thermistor_calibration_example.csv` | Editor's worked-example calibration table for a 10 kOhm NTC thermistor in the chapter project's voltage divider; six bath points, illustrative only. | Project (calibration step); Simulation exercise 3. |
| `sensor_uncertainty_budget.csv` | Editor's worked-example uncertainty budget for the calibrated thermistor measurement; expanded uncertainty U(k=2) = 0.156 C; illustrative. | Project (uncertainty-budget step); Design exercise on clinical thermometer. |
| `sensor_principles.csv` | Editor's compact catalogue of representative sensors across the six families with measurand, working range, typical accuracy, and readout; values are working numbers a reader could verify in any modern sensor handbook. | Sections 5.2 and 5.4; selection exercises. |

## Provenance

Reference data only; not measurement results. The reader's own
measurements should replace these values when working the
exercises and project. For the catalogue file, manufacturer
datasheets and Fraden's handbook are the authoritative sources.

## Conventions

- All temperatures in Celsius unless stated.
- All resistances in ohms; voltages in volts; uncertainties as one
  standard uncertainty (k = 1) unless the column name says otherwise.
- Comma-separated; UTF-8; first row is the header.
