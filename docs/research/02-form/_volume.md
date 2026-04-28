# Volume II: Form

**Working chapter count**: 18
**Working page total**: ~1,800
**Half-life of the contents**: foundational throughout, except Chapter 16 (Numerical methods) which is medium-life.

## Scope

The book teaches mathematics as the language of engineering: not for its own beauty, not as a compressed pure-mathematics degree, but as the toolset used in every subsequent book. From settled question 8, the standard is **engineering mathematics**: usable power. The reader leaves able to differentiate, integrate, solve linear systems, set up and solve ODEs and the simpler PDEs, reason probabilistically, optimise under constraint, and translate a real problem into a model that can be solved.

The reader does not leave able to prove the spectral theorem, derive measure theory from first principles, or audit a graduate analysis course. Those are different objects. The book is honest about what is offered and what is not.

## Arc within the book

Chapters 1-4 set the algebraic and analytic ground. Chapters 5-7 are the calculus core: derivatives, integrals, ODEs. Chapters 8-11 are the linear-algebra-and-multivariable core: vectors, matrices, eigenvalues, gradients. Chapter 12 introduces PDEs as the language of distributed phenomena. Chapters 13-14 cover probability and inference. Chapters 15-16 cover optimisation and numerical methods, which are where engineering mathematics earns its salary. Chapter 17 gives the discrete-mathematics literacy modern engineering requires. Chapter 18 is the closing chapter that asks the reader to take a real problem and turn it into mathematics, integrating everything in the book.
## Chapters

- [Chapter 1: Algebra and proof discipline](ch01-algebra-and-proof.md) (~80 pp)
- [Chapter 2: Functions and graphs](ch02-functions-and-graphs.md) (~80 pp)
- [Chapter 3: Trigonometry, complex numbers, phasors](ch03-trigonometry-complex-phasors.md) (~90 pp)
- [Chapter 4: Sequences, series, limits](ch04-sequences-series-limits.md) (~80 pp)
- [Chapter 5: Differentiation](ch05-differentiation.md) (~110 pp)
- [Chapter 6: Integration](ch06-integration.md) (~110 pp)
- [Chapter 7: Differential equations: ODEs](ch07-odes.md) (~120 pp)
- [Chapter 8: Vectors and vector calculus](ch08-vectors-and-vector-calculus.md) (~100 pp)
- [Chapter 9: Linear algebra](ch09-linear-algebra.md) (~110 pp)
- [Chapter 10: Eigenvalues and decompositions](ch10-eigenvalues-and-decompositions.md) (~110 pp)
- [Chapter 11: Multivariable calculus](ch11-multivariable-calculus.md) (~100 pp)
- [Chapter 12: PDEs: heat, wave, Laplace](ch12-pdes.md) (~120 pp)
- [Chapter 13: Probability theory](ch13-probability.md) (~100 pp)
- [Chapter 14: Statistical inference](ch14-statistical-inference.md) (~100 pp)
- [Chapter 15: Optimisation](ch15-optimisation.md) (~110 pp)
- [Chapter 16: Numerical methods](ch16-numerical-methods.md) (~110 pp)
- [Chapter 17: Discrete mathematics, graphs, combinatorics](ch17-discrete-mathematics.md) (~100 pp)
- [Chapter 18: Mathematical modelling: real problem to math](ch18-mathematical-modelling.md) (~100 pp)

## Substantial book project

The reader takes a real-world phenomenon of their choice (a heating system, a queue at a coffee shop, a small electrical circuit, a population of bacteria, anything they can measure), instruments it (Volume I skills), models it (Volume II skills), and produces a 20-30 page document containing: data, model derivation, model fit, error analysis, predictions, validation. The document is judged against the same rubric a mid-career engineer would face: would the model survive a hostile review?

## Bridges to adjacent books

- **In from Volume I**: every quantity has its language now.
- **Out to Volume III**: vectors, derivatives, ODEs are the language Volume III uses on the first page. The transition is seamless because the reader has been using physical examples throughout Volume II.
- **Out to Volume IV**: PDEs (heat, wave) are the prerequisites for Volume IV's heat-transfer and electromagnetism chapters.
- **Out to Volume VII**: discrete math (17), probability (13-14), optimisation (15), numerical methods (16) are direct prerequisites for nearly every chapter of Volume VII.
- **Out to Volume IX**: linear algebra (9-10), ODEs (7), and optimisation (15) are the formal core of Volume IX's control and systems chapters.

## Source-text reading list

- Gilbert Strang, *Linear Algebra and Its Applications* and *Calculus*.
- George Polya, *How to Solve It* and *Mathematics and Plausible Reasoning*.
- William Boyce and Richard DiPrima, *Elementary Differential Equations*.
- Lloyd Trefethen and David Bau, *Numerical Linear Algebra*.
- Sheldon Ross, *A First Course in Probability*.
- Stephen Boyd and Lieven Vandenberghe, *Convex Optimization*.
- Cleve Moler, *Numerical Computing with MATLAB* (for floating-point discipline).

## Open editorial questions

- Whether probability and statistical inference (13-14) should split into a separate sub-book at some scale. Currently combined.
- Whether numerical methods (16) belongs here or distributed across chapters. Currently centralised in 16.
- Whether Chapter 18 (modelling) should be the opening chapter of Volume III instead. Currently the closing chapter of Volume II. Working assumption: closing II is correct because the reader needs the full toolkit before being asked to model.
