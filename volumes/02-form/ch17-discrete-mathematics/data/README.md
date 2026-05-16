# Data assets — Volume II, Chapter 17 (Discrete mathematics)

Each file is a small reference table. CSV format; first row is the header.

## Files

| File | Purpose | Source |
|---|---|---|
| `growth_classes.csv` | Tabulated values of $\log_{2} n$, $n$, $n \log_{2} n$, $n^{2}$, $n^{3}$, $2^{n}$, $n!$ at $n$ from 1 to 64. The reader uses this to sanity-check the asymptotic-hierarchy plot. | Editorial computation. |
| `feasibility_frontier.csv` | Per-growth-class largest $n$ feasible on a single-machine and a $10^{3}$-node cluster, given a one-year budget of $\approx 10^{18}$ and $\approx 10^{20}$ operations respectively (current as of 2026). | Editorial computation, section 17.8. |
| `worked_graph_edges.csv` | Edge list for the worked five-vertex graph of section 17.2 (also figure fig:vol02:ch17:worked-graph). | Editorial example. |
| `dijkstra_exercise.csv` | Directed weighted edge list for exercise 17.4 (Dijkstra trace), also figure fig:vol02:ch17:dijkstra-trace. | Editorial example. |

## Conventions

- Numeric values for `n_factorial` are written as integers up to
  $20! = 2.4 \times 10^{18}$; rows where the value overflows a
  signed 64-bit integer are marked `nan` to remind the reader
  that the value exists symbolically but is no longer a working
  count.
- `feasibility_frontier.csv` reports the year of the operations
  budget in the `note` column; the frontier shifts roughly two
  bits per decade and the reader should re-derive before quoting
  the numbers after 2030.

## Provenance

Editorial computation from the rules of section 17.8 and the
worked examples of sections 17.2 and 17.3. Verify against your
own arithmetic before quoting in a load-bearing context.
