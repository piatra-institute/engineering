# Volume X: Failure

**Working chapter count**: 16
**Working page total**: ~1,600
**Half-life of the contents**: durable. The mechanisms of failure age slowly; specific cases are fixed in time and need only date-tags.

## Scope

A real engineer is someone who knows how things die. The book makes failure a first-class subject of study: its mechanisms, its statistical structure, its organisational and political contexts, and its discipline of post-mortem. Settled questions 29-31 specify the book's reach: failure appears in every other book in microcosm, but here it is treated at full depth, with named accidents and their political contexts (Q30), and with software failure at the same depth as physical failure (Q31).

The book's working assumption is that the reader has already built things (Volumes III-IX). Now the reader learns how everything they could have built can break. The reader leaves with the discipline of post-mortem, the habit of asking "how does this fail" before asking "how does this work," and a working knowledge of the canonical industrial, infrastructural, medical, aerospace, and software accidents that shaped modern engineering practice.

## Arc within the book

Chapter 1 sets the discipline. Chapters 2-4 cover mechanical failure (fatigue, fracture, instability) at full depth. Chapters 5-7 cover software, concurrency, and cascading failure. Chapter 8 covers common-mode failure. Chapter 9 covers human factors. Chapter 10 covers organisational failure with the canonical cases. Chapter 11 covers regulatory and certification failure. Chapter 12 covers forensic engineering. Chapter 13 covers near-misses as the data engineering most undervalues. Chapter 14 covers maintenance failure as the slow accident. Chapter 15 covers ecological and planetary failure. Chapter 16 closes with the discipline of post-mortem.
## Chapters

- [Chapter 1: Failure as engineering subject](ch01-discipline-of-failure.md) (~80 pp)
- [Chapter 2: Fatigue, S-N curves, fracture mechanics](ch02-fatigue-fracture-mechanics.md) (~120 pp)
- [Chapter 3: Corrosion, wear, environmental degradation](ch03-corrosion-wear-degradation.md) (~100 pp)
- [Chapter 4: Instabilities, runaway, buckling, resonance](ch04-instabilities-runaway-buckling-resonance.md) (~100 pp)
- [Chapter 5: Software defects: types of bugs](ch05-software-defects.md) (~110 pp)
- [Chapter 6: Concurrency and distributed failure](ch06-concurrency-distributed-failure.md) (~110 pp)
- [Chapter 7: Cascading failure in networks](ch07-cascading-failure-in-networks.md) (~110 pp)
- [Chapter 8: Common-mode failure](ch08-common-mode-failure.md) (~100 pp)
- [Chapter 9: Human factors and operator error](ch09-human-factors-operator-error.md) (~100 pp)
- [Chapter 10: Organisational failure](ch10-organisational-failure.md) (~120 pp)
- [Chapter 11: Regulatory and certification failure](ch11-regulatory-and-certification-failure.md) (~110 pp)
- [Chapter 12: Forensic engineering and accident investigation](ch12-forensic-engineering.md) (~110 pp)
- [Chapter 13: Near-misses and weak signals](ch13-near-misses-and-weak-signals.md) (~80 pp)
- [Chapter 14: Maintenance failure: the slow accident](ch14-maintenance-failure.md) (~80 pp)
- [Chapter 15: Climate, ecological, planetary failure](ch15-climate-ecological-planetary-failure.md) (~100 pp)
- [Chapter 16: Post-mortem as practice](ch16-discipline-of-post-mortem.md) (~80 pp)

## Substantial book project

The reader investigates one engineering accident in primary-source depth. Reads the official investigation report. Reads two contemporaneous engineering papers. Reads one critical historical re-analysis. Produces a 30-50 page document containing: technical reconstruction, organisational analysis, regulatory analysis, lessons drawn at four scales (the part, the machine, the operator, the organisation), and a synthesis comparing the official narrative with the lessons that should have been learned.

## Bridges to adjacent books

- **In from Volumes III-VIII**: every chapter mirrors a construction chapter in those books.
- **Out to Volume XI**: design under risk presupposes the failure literacy this book provides.
- **Out to Volume XII**: planetary failure (15) is Volume XII's substrate.

## Source-text reading list

- Henry Petroski, *To Engineer Is Human*, *Design Paradigms*, *Success Through Failure*.
- Charles Perrow, *Normal Accidents*.
- Diane Vaughan, *The Challenger Launch Decision*.
- Sidney Dekker, *The Field Guide to Understanding Human Error*, *Drift into Failure*.
- Nancy Leveson, *Engineering a Safer World*, *Safeware*.
- John Downer, *Rational Accidents*.
- William Langewiesche, *Inside the Sky*, *American Ground*.
- NTSB, AAIB, BEA, NRC, NASA-Langley primary investigation reports (selected).
- Forensic-engineering primary literature (ASCE, IEEE).

## Open editorial questions

- Whether the canonical-cases distribution is right. Currently each chapter has its own marquee case studies; an alternative is a centralised case-studies appendix. Working assumption: distributed, on the principle that cases anchor mechanisms.
- Whether the climate/planetary chapter (15) belongs in Volume X or Volume XII. Currently in X, on the principle that planetary engineering failure is failure first; XII picks up the constructive side.
- Whether maintenance failure (14) duplicates IX.17. Currently 14 is the failure-mode view; IX.17 is the design-time view. Distinct.
