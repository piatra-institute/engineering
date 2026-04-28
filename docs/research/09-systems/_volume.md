# Volume IX: Systems

**Working chapter count**: 19
**Working page total**: ~1,980
**Half-life of the contents**: durable for control theory and systems theory; medium-life for cyber-physical and infrastructure-as-system specifics.

## Scope

Volume IX is where the reader stops thinking about one machine and starts thinking about many machines, control loops, queues, networks, infrastructures, and the human institutions wrapped around them. Feedback, control, signals, reliability, queueing, optimisation under uncertainty, multi-agent systems, infrastructure, cyber-physical systems, resilience, maintenance: the discipline of making many things work together without lying to themselves.

The book is dense (Q11) because systems thinking has accumulated many sub-disciplines (control theory, reliability engineering, operations research, network science, decision theory) that share the same fundamental question and treat it with different mathematical tools. The book aligns them.

The depth standard is engineering depth: the reader can analyse, design, and verify systems at the level a working systems engineer applies. The reader does not leave able to derive optimal-control theory in measure-theoretic generality; that remains a graduate-mathematics specialisation.

## Arc within the book

Chapter 1 sets the modelling baseline. Chapters 2-5 cover the control core: linear, state-space, nonlinear, adaptive. Chapter 6 covers stochastic systems and Kalman filtering. Chapters 7-8 cover reliability and queueing. Chapter 9 covers optimisation in operation. Chapter 10 covers engineering project management, placed here because real engineering is delivered through projects and many failures are project failures before they are technical failures. Chapter 11 covers decision under uncertainty. Chapters 12-14 scale up: multi-agent and game-theoretic systems (with stigmergy and indirect coordination as a load-bearing sub-section), network systems, cyber-physical. Chapters 15-16 cover infrastructure as system, and coupled human-technical systems. Chapters 17-18 cover resilience and the practical disciplines of maintenance and observability. Chapter 19 closes with the harder skill: seeing systems whole.
## Chapters

- [Chapter 1: Modelling dynamic systems](ch01-modelling-dynamic-systems.md) (~100 pp)
- [Chapter 2: Linear control: transfer functions, Bode, Nyquist](ch02-linear-control.md) (~120 pp)
- [Chapter 3: State-space and modern control](ch03-state-space-modern-control.md) (~120 pp)
- [Chapter 4: Nonlinear and robust control](ch04-nonlinear-and-robust-control.md) (~110 pp)
- [Chapter 5: Adaptive and learning control](ch05-adaptive-and-learning-control.md) (~100 pp)
- [Chapter 6: Stochastic systems and Kalman filtering](ch06-stochastic-systems-kalman.md) (~120 pp)
- [Chapter 7: Reliability theory](ch07-reliability-theory.md) (~110 pp)
- [Chapter 8: Queueing theory and capacity planning](ch08-queueing-and-capacity.md) (~100 pp)
- [Chapter 9: Optimisation in operation](ch09-optimisation-in-operation.md) (~100 pp)
- [Chapter 10: Engineering project management](ch10-project-management.md) (~100 pp)
- [Chapter 11: Decision-making under uncertainty](ch11-decision-under-uncertainty.md) (~110 pp)
- [Chapter 12: Multi-agent and game-theoretic systems](ch12-multi-agent-and-game-theoretic.md) (~110 pp)
- [Chapter 13: Network systems](ch13-network-systems.md) (~120 pp)
- [Chapter 14: Cyber-physical systems](ch14-cyber-physical-systems.md) (~120 pp)
- [Chapter 15: Infrastructure as system](ch15-infrastructure-as-system.md) (~110 pp)
- [Chapter 16: Coupled human-technical systems](ch16-coupled-human-technical-systems.md) (~110 pp)
- [Chapter 17: Resilience and antifragility](ch17-resilience-and-antifragility.md) (~110 pp)
- [Chapter 18: Maintenance, observability, life-cycle](ch18-maintenance-observability-life-cycle.md) (~120 pp)
- [Chapter 19: Seeing systems whole](ch19-seeing-systems-whole.md) (~120 pp)

## Substantial book project

The reader takes a real, observable system in their environment (a small office, a household, a personal-server stack, a supply chain they participate in, a sports team's training schedule) and produces a systems analysis: model, control loops identified, failure modes mapped, reliability estimated, observability strategy, recommended improvements. Reviewed against the same rubric a consulting systems engineer would face.

## Bridges to adjacent books

- **In from Volumes II, III, IV, VII, VIII**: every prior book contributes mathematics, machinery, or computing.
- **Out to Volume X**: failure of systems is the dual of construction of systems; X is the dark mirror of IX.
- **Out to Volume XI**: design under risk is design with full systems awareness.
- **Out to Volume XII**: civilization is many systems coupled; XII applies IX at planetary scale.

## Source-text reading list

- Karl Åström and Richard Murray, *Feedback Systems*.
- Joao Hespanha, *Linear Systems Theory*.
- Donella Meadows, *Thinking in Systems*.
- Charles Perrow, *Normal Accidents*.
- Sidney Dekker, *The Field Guide to Understanding Human Error*.
- Erik Hollnagel, *Safety-I and Safety-II*.
- Nancy Leveson, *Engineering a Safer World* (STAMP).
- Ronald Howard, *Decision Analysis*.
- Hossein Pishro-Nik, *Introduction to Probability, Statistics, and Random Processes* (selected systems-context).

## Open editorial questions

- Whether reliability (7) and FMEA belong here or in Volume X. Currently here as a design-time discipline; X handles failure post-hoc.
- Whether project management (10) belongs in Systems or in Design. Currently here, on the principle that projects are systems with a delivery deadline.
- Whether maintenance (18) deserves to be its own short book at scale. Currently a chapter.
- Whether the closing chapter (19) is too philosophical. Working assumption: kept, because the synthesis matters at the end of the densest book.
