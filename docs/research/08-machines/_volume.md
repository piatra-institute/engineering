# Volume VIII: Machines

**Working chapter count**: 14
**Working page total**: ~1,560
**Half-life of the contents**: durable for the mechanical-design and manufacturing core; medium-life for additive manufacturing, modern electronics, and robotics specifics.

## Scope

The book is where mathematics, physics, materials, and computing become artifact. Mechanism design, structures, manufacturing, electronics, sensors, actuators, robotics, and the integration of mechanical, electrical, and digital subsystems. The reader leaves able to design a machine end-to-end at an honest first-pass level: kinematic synthesis, stress and fatigue analysis, manufacturing-route selection, electronic interfacing, sensor integration, and control architecture.

The chapters are slightly longer than the book average (130 pp default) because each chapter integrates content from multiple earlier books. Page budget is tighter than scope, on purpose: the book is the synthesis point of Volumes I-VII.

## Arc within the book

Chapters 1-3 cover the mechanical core: mechanisms, bearings, machine elements. Chapter 4 covers fatigue and wear-driven design. Chapter 5 covers CAD and engineering drawing. Chapters 6-7 cover manufacturing: traditional and additive. Chapter 8 covers analog electronics. Chapter 9 covers power electronics: drives, inverters, and grid-tie, placed here because EV powertrains, motor drives, and renewable inverters are central modern engineering and a book that stops at op-amps misses where machines now spend their power budget. Chapter 10 covers digital electronics and embedded systems. Chapter 11 covers sensors and actuators at macro scale. Chapter 12 covers MEMS and microsystems: the same sensors, miniaturised, where stiction and packaging stress replace bearings and bolts as failure modes. Chapter 13 covers robotics. Chapter 14 closes with hydraulics, pneumatics, and the mechatronic integration that makes the whole machine work.
## Chapters

- [Chapter 1: Mechanisms: linkages, cams, gears](ch01-mechanisms-linkages-cams-gears.md) (~120 pp)
- [Chapter 2: Bearings, lubrication, tribology](ch02-bearings-lubrication-tribology.md) (~100 pp)
- [Chapter 3: Machine elements: fasteners, springs, joints](ch03-machine-elements-fasteners-springs-joints.md) (~120 pp)
- [Chapter 4: Machine design under fatigue and wear](ch04-fatigue-and-wear-design.md) (~140 pp)
- [Chapter 5: CAD and engineering drawing](ch05-cad-and-engineering-drawing.md) (~110 pp)
- [Chapter 6: Manufacturing: machining, casting, forming](ch06-manufacturing-machining-casting-forming.md) (~140 pp)
- [Chapter 7: Additive manufacturing](ch07-additive-manufacturing.md) (~110 pp)
- [Chapter 8: Analog electronics](ch08-analog-electronics.md) (~140 pp)
- [Chapter 9: Power electronics: drives, inverters, grid-tie](ch09-power-electronics.md) (~120 pp)
- [Chapter 10: Digital electronics, embedded systems](ch10-digital-electronics-embedded.md) (~140 pp)
- [Chapter 11: Sensors and actuators](ch11-sensors-and-actuators.md) (~130 pp)
- [Chapter 12: MEMS and microsystems](ch12-mems-microsystems.md) (~100 pp)
- [Chapter 13: Robotics](ch13-robotics.md) (~140 pp)
- [Chapter 14: Hydraulics, pneumatics, mechatronic integration](ch14-hydraulics-pneumatics-mechatronic-integration.md) (~130 pp)

## Substantial book project

The reader designs, builds, and characterises a complete machine at small scale. Examples: a 3-axis CNC, a small robotic arm, a precision linear stage, a bench-top centrifuge, a CV-based sorter, a small autonomous vehicle. The deliverable is a full engineering pack: requirements, drawings, BOM, FMEA, controller design, software, test data, error budget, manual.

## Bridges to adjacent books

- **In from Volumes III, IV, V**: every chapter depends on mechanics, energy, and materials.
- **In from Volume VII**: digital electronics (10), robotics (13), and mechatronics (14) depend on Volume VII chapters 6, 7, 15, 16.
- **Out to Volume IX**: every machine is a control problem; this book is the substrate for Volume IX.
- **Out to Volume X**: every failure section here pairs with a Volume X case study, and the fatigue/fracture material in 4 is the ground truth Volume X chapter 2 starts from.
- **Out to Volume XI**: design as discipline (Volume XI) builds on the practical design done here.

## Source-text reading list

- Joseph Shigley and Charles Mischke, *Mechanical Engineering Design*.
- Robert Norton, *Design of Machinery*.
- Serope Kalpakjian and Steven Schmid, *Manufacturing Engineering and Technology*.
- Paul Horowitz and Winfield Hill, *The Art of Electronics*.
- Henrik Christensen, *Springer Handbook of Robotics* (selected chapters).
- Gabriel Kron and others, *Tensor Analysis of Networks* (cross-domain).
- Jay Lee on industrial mechatronics.

## Open editorial questions

- Whether robotics (13) deserves a sub-book at scale. Currently one chapter.
- Whether hydraulics/pneumatics (14) should be earlier (alongside fluid mechanics in Volume III). Currently here, on the principle that they are machine elements first.
- Whether sensors and actuators (11) should be one chapter or two. Currently combined.
- Whether MEMS (12) belongs in Machines or in Volume V (Matter). Currently here, on the principle that microsystems are first machines and only secondarily a materials topic.
- Whether power electronics (9) should sit beside circuits in Volume IV instead. Currently here, on the principle that the chapter is design-of-converters as machines, not theory of voltage and current.
