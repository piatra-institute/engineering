# Volume III: Force

**Working chapter count**: 13
**Working page total**: ~1,300
**Half-life of the contents**: durable. Newton's laws, stress, strain, fluid dynamics fundamentals do not age.

## Scope

Force is the first physical book. The reader takes the mathematics of Volume II and points it at the mechanical world: at why things stand, why they move, and why they break. The book covers statics, dynamics, mechanics of deformable solids, and fluid mechanics through compressible flow. Materials enter as constants (stiffness, density, viscosity) here; their internal structure is Volume V.

The reader leaves able to draw a free-body diagram for any mechanical situation, derive the equations of motion, identify the dominant failure mode, and choose a model whose simplifications are honest about what is being thrown away.

## Arc within the book

Chapter 1 is the orientation: forces are vectors, free-body diagrams are the engineer's first habit, and constraints determine everything. Chapters 2-3 do statics and the mechanics of stress and strain. Chapters 4-6 do dynamics: kinematics, energy methods, vibrations. Chapter 7 generalises vibration into acoustics: wave engineering in solids and fluids, placed here because it belongs to mechanics, not to a footnote in fluids. Chapters 8-9 are structural mechanics: beams, columns, frames, plates, shells. Chapters 10-13 are fluid mechanics, ascending from statics through Bernoulli to viscous flow and finally compressible flow.
## Chapters

- [Chapter 1: Forces and free-body diagrams](ch01-forces-and-fbd.md) (~90 pp)
- [Chapter 2: Statics of rigid bodies](ch02-statics-of-rigid-bodies.md) (~100 pp)
- [Chapter 3: Stress and strain](ch03-stress-and-strain.md) (~120 pp)
- [Chapter 4: Dynamics: kinematics and Newton's laws](ch04-dynamics-and-newtons-laws.md) (~100 pp)
- [Chapter 5: Energy methods](ch05-energy-methods.md) (~90 pp)
- [Chapter 6: Vibrations](ch06-vibrations.md) (~110 pp)
- [Chapter 7: Acoustics: waves in solids and fluids](ch07-acoustics.md) (~100 pp)
- [Chapter 8: Beams, columns, frames](ch08-beams-columns-frames.md) (~120 pp)
- [Chapter 9: Plates, shells, solid mechanics](ch09-plates-shells-solid-mechanics.md) (~120 pp)
- [Chapter 10: Fluid statics](ch10-fluid-statics.md) (~80 pp)
- [Chapter 11: Fluid dynamics: inviscid](ch11-fluid-dynamics-inviscid.md) (~110 pp)
- [Chapter 12: Viscous flow, boundary layers](ch12-viscous-flow-boundary-layers.md) (~110 pp)
- [Chapter 13: Compressible flow, aerodynamics](ch13-compressible-flow-aerodynamics.md) (~110 pp)

## Substantial book project

The reader designs, analyses, builds, and tests a small mechanical artifact under load: a cantilever crane, a small bridge, a wind tunnel, or equivalent. The deliverable is a 30-50 page engineering report including FBDs, stress analysis, FEM verification, vibration check, and as-built test data, with explicit error bars throughout.

## Bridges to adjacent books

- **In from Volumes I-II**: vector calculus, ODEs, and linear algebra are used from page one.
- **Out to Volume IV**: thermodynamics begins where mechanics' "energy" leaves off; momentum balance becomes heat balance.
- **Out to Volume V**: stress, strain, and material properties feed directly into materials selection and microstructural reasoning.
- **Out to Volume VIII**: the entire book is the design basis for machines.
- **Out to Volume IX**: vibrations and modal analysis are the entry point to dynamic-systems control.
- **Out to Volume X**: every failure section here pairs with a deeper analysis in Volume X (e.g., Tacoma Narrows in 13.8 → full case study in X.4).

## Source-text reading list

- J. L. Meriam and L. G. Kraige, *Engineering Mechanics: Statics and Dynamics*.
- Stephen Crandall et al., *An Introduction to the Mechanics of Solids*.
- Frank White, *Fluid Mechanics*.
- Hibbeler, *Mechanics of Materials*.
- L. D. Landau and E. M. Lifshitz, *Mechanics* and *Fluid Mechanics* (selected sections).
- Henry Petroski, *Design Paradigms* (for the failure framing).

## Open editorial questions

- Whether plate/shell theory (8) deserves its own chapter or merges with stress/strain (3). Currently separate.
- Whether vibrations (6) belongs here or in Volume IX (Systems). Currently here, on the principle that mechanical vibration is mechanics first and control second.
- Whether compressible flow (12) is too aerospace-flavoured for a general engineering book. Working assumption: included, because energy and propulsion in Volume IV depend on it.
