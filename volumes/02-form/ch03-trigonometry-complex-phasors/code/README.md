# Code assets - Volume II, Chapter 3 (Trigonometry, complex numbers, phasors)

Executable supporting code for the chapter's worked examples and
exercises.

## Files

| File | Purpose | Used by |
|---|---|---|
| `phasor_add.py` | Phasor adder; adds two sinusoids at the same frequency by converting to phasors and reports the resulting amplitude and phase. | Calculation exercise (phasor sum); section 3.4. |
| `rlc_response.py` | Series RLC steady-state response: computes $Z(\omega)$, $\tilde I$, and each element voltage by phasor algebra for a swept frequency range; also integrates the underlying ODE and compares to the phasor result. | Project; simulation exercise (RLC ODE); figure `fig-phasor-rlc`. |
| `phase_unwrap.py` | Generates a wrapped phase signal and runs a simple first-order unwrap algorithm; demonstrates the silent failure when the sample spacing is too coarse. | Simulation exercise (wrap and unwrap); failure-analysis exercise (laser interferometer). |
| `beat_demo.py` | Synthesises two sinusoids of nearby frequencies and plots their sum to display the beat envelope. | Section 3.1 (sum-to-product identity); figure `fig-beating`. |

## Running

Each file's docstring lists dependencies and the command to run.
`phasor_add.py` and `phase_unwrap.py` require `numpy` and
`matplotlib`. `rlc_response.py` additionally requires
`scipy.integrate` for the ODE comparison. `beat_demo.py` requires
`numpy` and `matplotlib`.

A representative invocation:

```
uv run --with numpy --with matplotlib --with scipy \
  volumes/02-form/ch03-trigonometry-complex-phasors/code/rlc_response.py
```
