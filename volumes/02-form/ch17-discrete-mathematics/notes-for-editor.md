# Notes for editor: Vol II Ch 17 (Discrete mathematics, graphs, combinatorics)

Drafted 2026-04-29.

## Shared-file changes

### `bibliography/references.bib`

Added one new BibLaTeX entry to support the chapter epigraph:

- `gen:dijkstra1972` — Dijkstra, "Notes on Structured Programming," in
  Dahl, Dijkstra, Hoare (eds.), *Structured Programming*, Academic
  Press, 1972, pp. 1-82. Used as the chapter epigraph (page 6 of the
  Dijkstra essay). The entry uses the `gen:` prefix because the
  Dijkstra essay is a cross-book influence in the same sense as
  Polya's *How to Solve It* and Vincenti's *What Engineers Know*: it
  shapes the project's overall stance on complexity and discipline,
  not just one chapter.

No other shared-file changes.

## Within-chapter notes

- Chapter mass: roughly 25-30 pages of first-draft prose against a
  100-page production target. The dossier's per-section page targets
  (10/15/18/12/10/10/12/13) are deliberately under-served at
  first-draft density; the chapter is paced for the working chapter
  shape (8 sections, an estimation block, an archetype box, a mastery
  box, a project, 40 exercises) rather than for the long-form target.
  Production-density expansion will deepen the algorithmic-graph
  section (more worked examples on Dijkstra, Bellman-Ford, MST), the
  recurrences and generating functions section (more master-theorem
  worked cases, a worked generating-function derivation beyond
  Fibonacci), and the failure section (a named software-test case
  from a public industrial dataset).
- Archetype: scaling and optimisation, both as named in the dossier.
  Scaling appears in the counting hierarchy of section 17.1 and in
  the asymptotic hierarchy of section 17.5; optimisation appears as
  the boxed archetype in section 17.3.
- Big-$O$, $\Omega$, $\Theta$ are introduced here as required by the
  brief. Section 17.5 gives the formal definitions and the working
  hierarchy.
- Master theorem and generating functions are presented at the
  recognition level required by the brief. The closed-form Fibonacci
  derivation by partial fractions is stated; the general theory is
  not.
- Cryptographic primitives (RSA, Diffie-Hellman, hash functions) are
  presented at the recognition level required by the brief, with a
  forward reference to Volume VII for depth.
- Project track aligned with Q55-vol02-ch17 settlement of 2026-04-29.
- 40 exercises: 8 calculation, 8 derivation, 5 estimation, 5
  simulation, 3 design, 4 diagnosis, 3 failure analysis, 4 judgement.
- No named accidents requiring a registry entry. The DES discussion
  in failure-analysis is a class observation, not a single named
  event.
