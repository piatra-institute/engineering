# Code assets — Volume II, Chapter 17 (Discrete mathematics)

Each script is self-contained and runnable with `uv run`:

```
uv run code/<script>.py
```

## Files

| File | Purpose | Used by |
|---|---|---|
| `dijkstra.py` | Binary-heap Dijkstra implementation; reproduces the trace of exercise 17.4. | Section 17.3, exercise 17.4, simulation exercise 1. |
| `kruskal.py` | Kruskal MST with union-by-rank and path compression; reproduces exercise 17.5. | Section 17.3, exercise 17.5, simulation exercise 2. |
| `erdos_renyi.py` | Erdos-Renyi $G(n, p)$ generator and giant-component sweep; reproduces the phase-transition simulation. | Section 17.2, simulation exercise 4. |
| `miller_rabin.py` | Deterministic-witness Miller-Rabin primality test in the working range; finds the first 100 primes above $10^{18}$. | Section 17.7, simulation exercise 5. |
| `sat_brute.py` | Brute-force SAT solver and random 3-CNF generator for the $2^{n}$ scaling benchmark. | Section 17.4, simulation exercise 3. |

## Conventions

- Pure-stdlib implementations; no third-party graph or solver
  libraries. The pedagogy is the algorithm, not the wrapping.
- Hash-randomised seeds fixed per script for reproducibility.
- Output is human-readable text on stdout, not files.
- Each script's `__main__` block reproduces the worked example
  from the chapter so the reader can spot-check before adapting
  the code to their own input.

## Provenance

Editor's reference implementations. The reader is encouraged to
re-implement from scratch before reading the code; the code's job
is to confirm the answer and to provide a working baseline against
which the reader's optimised version can be benchmarked.
