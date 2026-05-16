# Code assets, Volume II, Chapter 16 (Numerical methods)

Each script is self-contained and runnable with `uv run`:

```
uv run code/<script>.py
```

All scripts use only the Python standard library plus NumPy and SciPy
where noted; no platform-specific dependencies.

## Files

| File | Purpose | Used by |
|---|---|---|
| `floating_point_demo.py` | Print binary64 unit round-off, machine epsilon, the binary expansion of $0.1$, and the absolute representation error of $0.1$. | Section 16.1 estimation, Calculation exercises 1 and 2. |
| `catastrophic_cancellation.py` | Compare naive vs Taylor-stable evaluation of $\sin(x) - x + x^{3}/6$ across $x = 10^{0}$ through $10^{-12}$. | Section 16.2 second estimation, Estimation exercise 14, Figure \ref{fig:vol02:ch16:catastrophic-cancellation}. |
| `kahan_summation.py` | Compare naive sequential summation and Kahan compensated summation for a vector of $10^{6}$ alternating-sign numbers. | Section 16.1 estimation. |
| `newton_safeguarded.py` | Safeguarded root-finder combining Newton's method with bisection fall-back; demonstrates the safeguard catching a Newton divergence from a poor initial guess. | Section 16.3, Design exercise 3 (safeguarded root-finder). |
| `convergence_orders.py` | Compute the iteration-error trace for bisection, secant, and Newton on $\cos x - x = 0$; verify the three convergence rates from the slopes on a log scale. | Section 16.3, Simulation exercise 1, Figure \ref{fig:vol02:ch16:convergence-orders}. |
| `hilbert_solve.py` | Solve a Hilbert-matrix linear system at orders $n = 5, 8, 10, 12, 14$ by LU partial pivoting and by truncated SVD; report the relative error against the known solution $\vect{x} = (1, 1, \ldots, 1)^{\transpose}$. | Section 16.4, Simulation exercise 3. |
| `patriot_drift.py` | Reconstruct the Patriot Dhahran timing-drift model: cumulative timing error vs operating hours, predicted-position error at Scud-class velocity. | Section 16.8.1, Figure \ref{fig:vol02:ch16:patriot-drift}, Failure-analysis exercise 1. |
| `stiffness_demo.py` | Integrate the stiff problem $\dot y_1 = -1000 (y_1 - \cos t)$, $\dot y_2 = -y_2 + y_1$ with explicit RK4 (largest stable step) and with BDF; report wall-clock time and step count. | Section 16.6, Simulation exercise 4. |

## Conventions

- Random seeds pinned to `42` where any random number is drawn.
- Output is human-readable text on stdout; the patriot-drift script
  optionally writes `../data/patriot-drift.csv`.
- Each script ends with a brief stdout summary that an editor can
  copy into a chapter or notebook.

## Provenance

Editor's reference implementations. The Patriot drift reconstruction
is from the GAO report \cite{acc:gao-patriot-1992}; the catastrophic-
cancellation example follows \cite[\S 1.14]{text:higham-numerical}; the
Hilbert-matrix example follows the canonical treatment in
\cite[ch.~12]{text:trefethen-bau1997}.
