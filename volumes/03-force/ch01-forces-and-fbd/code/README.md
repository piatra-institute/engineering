# Code for Volume III, Chapter 1 (Forces and free-body diagrams)

Small, dependency-light scripts that back the worked examples, figures,
and simulation exercises. All are runnable with `python <file>`; the
only hard dependency is `numpy` (a couple of optional plots use
`matplotlib`).

| File | What it does | Used by |
|------|--------------|---------|
| `resolve_forces.py` | Resolve planar forces into components, sum them, and check rigid-body equilibrium (net force and net moment). Includes a ladder demo. | "Force as a vector"; ladder worked example |
| `truss_solver.py` | Solve a planar pin-jointed truss by the method of joints, assembled as one linear system. Includes a triangle-truss demo. | Simulation exercise (truss FBD solver); method-of-joints example |
| `block_on_incline.py` | Sweep the inclination angle of a rough plane and report the friction force, the static plateau, and the slip threshold `atan(mu_s)`. | Simulation exercise (block on incline); Coulomb-friction figure |

The reference outputs these scripts produce are tabulated in the
`data/` folder alongside this chapter.
