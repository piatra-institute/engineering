# Volume I: Quantity

**Working chapter count**: 9
**Working page total**: ~720
**Half-life of the contents**: foundational. Almost nothing in this book ages.

## Scope

The book teaches the reader to convert reality into numbers, and to know what those numbers mean. It is the smallest of the twelve volumes because its content is foundational rather than encyclopedic. The reader leaves with the habits of measurement: estimation before calculation, dimensional analysis as a debugging tool, error as a first-class quantity carried alongside every result, calibration as the discipline by which a measurement gets its meaning, and statistical literacy sufficient to know when a result is real.

The reader does not leave able to design a measurement instrument. That is Volume VIII territory. The reader leaves able to use one, distrust one, and recognise when a colleague's number was produced without the discipline this book demands.

## Arc within the book

Chapter 1 establishes that engineering and measurement are the same discipline at different scales. Chapter 2 introduces units and dimensions as the syntax. Chapter 3 introduces calibration as the semantics. Chapter 4 introduces error as the unavoidable companion of every reported number. Chapters 5-7 give the reader concrete instruments and the physical quantities they touch. Chapter 8 introduces the statistics every working engineer needs. Chapter 9 closes the book by turning estimation into a discipline the reader practices for the rest of the work, having earned the right to estimate by understanding what is being estimated.
## Chapters

- [Chapter 1: Why we measure](ch01-why-we-measure.md) (~60 pp)
- [Chapter 2: Units and dimensions](ch02-units-and-dimensions.md) (~70 pp)
- [Chapter 3: Calibration and traceability](ch03-calibration-and-traceability.md) (~80 pp)
- [Chapter 4: Error and uncertainty](ch04-error-and-uncertainty.md) (~100 pp)
- [Chapter 5: Sensors and instruments](ch05-sensors-and-instruments.md) (~90 pp)
- [Chapter 6: Time, frequency, and signals](ch06-time-frequency-signals.md) (~80 pp)
- [Chapter 7: Length, area, volume, mass](ch07-length-area-volume-mass.md) (~70 pp)
- [Chapter 8: Statistics for engineers](ch08-statistics-for-engineers.md) (~90 pp)
- [Chapter 9: The discipline of estimation](ch09-discipline-of-estimation.md) (~80 pp)

## Substantial book project

The reader builds a personal measurement notebook over the course of the book. By Chapter 9 the notebook contains: at least one calibration of a household instrument; at least one error-bounded measurement of a non-trivial quantity; at least three orders-of-magnitude estimates compared to ground truth; one fully-documented experiment with at least 30 trials and proper statistical analysis. The notebook is graded against a public rubric.

## Bridges to adjacent books

- **Out to Volume II**: every quantity introduced here lives inside the mathematical structures Volume II will formalise. The transition is from "we have numbers" to "we have functions of numbers."
- **Out to all subsequent volumes**: every chapter of every volume invokes the estimation environment introduced in I.9 and the error-propagation discipline introduced in I.4.
- **Forward references**: the failure mode of "the sensor lies in the same direction" (I.5.6) reappears as a structural problem in Volume X chapter 9 (Human factors and operator error).

## Source-text reading list

- BIPM, *The International System of Units (SI Brochure)*, current edition.
- John R. Taylor, *An Introduction to Error Analysis*.
- Charles Perrow, *Normal Accidents* (selected chapters).
- Henry Petroski, *To Engineer Is Human* (selected chapters).
- David MacKay, *Sustainable Energy: Without the Hot Air* (for estimation discipline).
- Sanjoy Mahajan, *The Art of Insight in Science and Engineering*.
- ISO/IEC Guide 98-3, *Guide to the Expression of Uncertainty in Measurement*.
- The NIST Engineering Statistics Handbook (online).

## Open editorial questions for this book

- Whether Bayesian reasoning gets one section here (8.5) or its own chapter. Currently one section. Revisit if the section consistently runs over 12 pp.
- Whether the Buckingham pi theorem (2.5) should be deferred to Volume II as a topic in dimensional analysis-as-mathematics. Currently here. Working assumption: it is more useful in I.2 as a debugging tool than in II as a theorem.
- Whether Chapter 6 should split into a clock chapter and a signal-sampling chapter. Currently combined. Working assumption: combined, with the heavier signal-processing material deferred to Volume IV (waves) and Volume VII (signal processing).
