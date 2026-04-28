# Chapter 1 pilot review: "Why we measure"

Resolved: 2026-04-28.

The 40 fixes in section G have been applied. The bibliography has the
Kelvin entry (`hist:kelvin1891`), the Boeing reference
(`web:boeing-commercial-reference`), and the Lockwood Board of Inquiry
report (`acc:lockwood-gimli1985`, replacing the unverifiable
`acc:casb-gimli`). The chapter prose has the technical corrections to
the Mars Climate Orbiter, Air Canada 143, and Ariane 5 Flight 501
sections; the Type A / Type B clarification; the corrected estimation
block with a postmortem; the project's revised time budget; the
exercise reader-path tags; the deferred-to-chapter-4 markers on the
covariance derivations; the standards/customary-units rephrasing of
the failure section; the chapter cross-reference fix
("next chapter" -> "Chapter 3"); and the voice rewrites flagged in
section B that overlap with the G fixes. The build is clean: `make
strict` produces a 512-page `main.pdf`; `make check` and `make
audit-docs` PASS; `grep` finds no em-dashes in the chapter source.

The structural risks named in section H (named-cases registry, source
ledger with page pins, exercise architecture with prerequisites) are
recorded as Phase 0.7 work and tracked separately. They block scaling
to chapter 2 only after the second chapter's draft starts; the editor's
position is to write chapter 2 next, then triage section H based on
what the second chapter actually demands.

## A. Verdict per role

Technical reviewer: blocked.

Pedagogical reviewer: approved-with-corrections.

Voice reviewer: approved-with-corrections.

The chapter has a real spine: measurement as public, dated, unit-bearing knowledge. The project is pointed in the right direction. The exercise mix is close to the Q16 target. But the pilot cannot set the template yet. The technical block is not one grand error; it is a pattern of compressed claims, missing source apparatus, and several sentences that turn verification failures into measurement failures by rhetorical pressure. For a first chapter, that is exactly where an external reader will press.

Sources checked for this review include the NASA Mars Climate Orbiter Mishap Investigation Board Phase I Report at `https://llis.nasa.gov/llis_lib/pdf/1009464main1_0641-mr.pdf`, the ESA Ariane 501 Inquiry Board report at `https://esamultimedia.esa.int/docs/esa-x-1819eng.pdf`, ESA press release PR 33-1996 at `https://www.esa.int/Newsroom/Press_Releases/Ariane_501_-_Presentation_of_Inquiry_Board_report`, ISO/IEC Guide 98-3:2008 at `https://www.iso.org/standard/50461.html`, JCGM/VIM definitions at `https://www.iso.org/sites/JCGM/VIM/JCGM_200e_FILES/MAIN_JCGM_200e/02_e.html`, BIPM SI brochure material at `https://www.bipm.org/en/publications/si-brochure`, Boeing's Commercial Airplanes Reference Guide at `https://www.boeing.com/productstory/Commercial_Airplanes_Reference_Guide.pdf`, and Kelvin's Popular Lectures and Addresses record at Google Books, `https://books.google.com/books/about/Popular_Lectures_and_Addresses_Constitut.html?id=JcMKAAAAIAAJ`. For Air Canada 143, the repository citation is not presently verifiable from the bibliography. Public copies of the 1985 Lockwood Board of Inquiry report support the conversion narrative, but the release citation needs an archived official or library scan, with page numbers.

## B. Voice review

The chapter is mostly in the house register, but it still has sentences that sound like a generated explainer, a maxim, or a slogan. The following are sentence-level voice findings, walking in chapter order.

1. Line 18: "We open the work with the act that opens engineering itself: putting a number on the world."

Problem: portentous opener. "Putting a number on the world" is memorable but too slogan-shaped for the first sentence of a 12-volume formation text.

Rewrite: "We begin with measurement because every later engineering act depends on a number that can be checked."

2. Lines 25-28: "Measurement is the act by which the world becomes accountable to engineering."

Problem: abstract flourish. The following sentence already does the work.

Rewrite: "Measurement turns a private observation into a claim another engineer can test."

3. Lines 30-38: "Pre-measurement crafts were not crafts without quantities."

Problem: negate-first construction and overbroad historical frame.

Rewrite: "Older crafts carried quantities in trained bodies, tools, proportions, marks, sounds, and repeated practice."

4. Lines 49-49: "The number is the price of admission to the engineering world."

Problem: aphorism. It lands, but it is too polished and too absolute.

Rewrite: "A recorded number is what lets the work leave the hands of its first maker."

5. Lines 76-77: "Each of those is a reason measurement exists in engineering. None is satisfied by intuition."

Problem: thesis restatement with a false absolute. Intuition can partly satisfy diagnosis and comparison, but not public accountability.

Rewrite: "Intuition can start each task; measurement is what lets another engineer audit it."

6. Lines 79-84: "This chapter introduces measurement as a discipline."

Problem: self-announcing topic sentence. The section list that follows is syllabus prose.

Rewrite: "The rest of Volume I turns that discipline into working habits: units, calibration, traceability, error propagation, instruments, statistics, and estimation."

7. Lines 91-95: "A working engineer carries an internal ruler that maps any quantity in their domain to its order of magnitude without conscious calculation."

Problem: "without conscious calculation" overstates expert intuition and makes the habit sound mystical.

Rewrite: "A working engineer builds an internal ruler for orders of magnitude in their domain."

8. Lines 109-110: "Strip the numbers from that slip and ask what the engineer is signing for. Wet stone."

Problem: rhetorical fragment. Strong, but too theatrical for an example that should be source-clean.

Rewrite: "Without the numbers, the delivery slip no longer identifies an engineering material."

9. Lines 118-120: "A pharmacist preparing a sterile dose without weighing the active ingredient is dispensing hope."

Problem: high-flourish metaphor. It risks sounding glib in a medication example.

Rewrite: "A pharmacist preparing a sterile dose without weighing the active ingredient cannot defend the dose."

10. Lines 127-128: "Engineering history is, in part, a graveyard of unmeasured judgments."

Problem: melodramatic and uncited. The following named cases carry enough weight if sourced.

Rewrite: "Many engineering failures include a missing, ignored, or misread measurement."

11. Lines 136-138: "The lesson here is the prior one: an engineer without measurement has no record, and an engineer with no record has no defence against a hostile review by reality."

Problem: "hostile review by reality" is a clever phrase where a technical claim belongs.

Rewrite: "The prior lesson is simpler: an engineer without a measurement record cannot reconstruct the decision."

12. Line 149: "We will, throughout this work, treat the second kind as the discipline."

Problem: throat-clearing manifesto.

Rewrite: "Throughout this work, engineering knowledge means the second kind."

13. Lines 197-198: "The point of the exercise is not the answer. It is the habit."

Problem: banned negate-first-then-pivot pattern.

Rewrite: "The exercise trains the habit more than the answer."

14. Lines 239-239: "Neither: a free-running interpolation of the engineer's mood."

Problem: cute insult. It will date badly and weakens a basic distinction.

Rewrite: "Neither: a display that drifts unpredictably and has not been calibrated."

15. Lines 266-267: "Significant figures are a coarse, finger-counting proxy for uncertainty."

Problem: "finger-counting" is dismissive and informal.

Rewrite: "Significant figures are a coarse proxy for uncertainty."

16. Lines 272-273: "A report with neither is a report that does not know what it knows."

Problem: aphoristic tail.

Rewrite: "A report with neither has not stated how much confidence its number deserves."

17. Lines 298-299: "Three engineering accidents make the discipline of measurement vivid."

Problem: self-announcing and generic.

Rewrite: "Three accidents show what happens when a number crosses an interface without the protection it needs."

18. Lines 319-321: "The number that mattered was not derived incorrectly. The number that mattered was communicated between two systems with different unit conventions, neither of which forced the conversion to occur."

Problem: banned negative pivot and an inaccurate technical subject.

Rewrite: "The failure sat in the interface between contractor data and the navigation model: one side delivered impulse in English units, while the documented interface required newton seconds."

19. Lines 349-351: "The Gimli Glider made its landing because its flight crew were exceptional pilots, not because the system worked."

Problem: strong, but it drifts toward hero/blame narration. The case-study template asks for mechanisms.

Rewrite: "The safe landing does not vindicate the fuelling system; it shows that crew skill recovered after the measurement system had already failed."

20. Lines 391-396: "The lesson here is in the basement of the discipline..."

Problem: "basement of the discipline" is metaphor for emphasis. "rumour" is a slogan.

Rewrite: "The lesson is basic: every number that crosses an interface must carry its unit, range, and provenance. Without those, the receiving system cannot know what quantity it has received."

21. Lines 497-499: "We do not begin with a calamity; we begin with a chronic, low-grade failure that has cost engineering more than most named accidents."

Problem: banned negative pivot and unsupported scale claim.

Rewrite: "We begin with a chronic failure mode: unit systems meet at interfaces, and the conversion is treated as memory work."

22. Lines 512-513: "The persistence is not irrational."

Problem: negate-first compression.

Rewrite: "Imperial persistence has engineering causes."

23. Lines 537-539: "Each of these is mundane. Each has, on documented occasions, killed people. The discipline that prevents them is not heroic; it is clerical."

Problem: triple declarative plus negative pivot. Also uncited.

Rewrite: "These errors look clerical until they reach a patient, aircraft, plant, or bridge. Preventing them requires written units, checked conversions, and audited interfaces."

24. Lines 556-559: "We close the chapter on this rule because it is the smallest, hardest, and most consequential measurement habit the volume introduces."

Problem: inflated ranking. It does not need superlatives.

Rewrite: "We close on this rule because it is the measurement habit the reader will use in every later chapter."

25. Lines 490-493: "These four practices are too small for a chapter. They are too large for a footnote."

Problem: balanced aphorism. It is pleasant, but generic.

Rewrite: "These practices are small enough to skip and important enough to record here."

## C. Technical review

The chapter blocks technically until the following issues are corrected.

Kelvin epigraph. The wording is not source-faithful as a direct quotation. The common text begins with "I often say that..." and the second half includes "but when you cannot measure it, when you cannot express it in numbers..." The chapter omits the second "measure it" clause without ellipsis and cites no bibliographic entry or page. Add a `hist:` entry for Kelvin, Popular Lectures and Addresses, volume 1, "Electrical Units of Measurement", lecture delivered 3 May 1883, with page pin. If the shortened wording is kept, mark the omissions.

Mars Climate Orbiter. The main error is line 312: "spacecraft software expected newton seconds." The NASA report describes a ground software and operations-navigation interface. SM_FORCES output in the AMD file was required to be in metric units, and trajectory modelers assumed that it was. The report states that after-the-fact analysis found the small-forces delta-v reports were low by a factor of 4.45 because impulse bit data was delivered in lb-sec instead of N-sec. The chapter should not put the expectation in spacecraft software. The counterfactual at lines 322-323, "would have caught it on the first ground test," is uncited and too certain. NASA's recommendations support unit verification and software audits, not that a particular first test would have caught it.

Air Canada Flight 143. The conversion arithmetic is broadly right: 1.77 lb/L divided by 2.2 gives about 0.80 kg/L, so using 1.77 as kg/L overstates fuel mass by about 2.2. The chapter is too narrow when it says "the crew used" the wrong density. The available inquiry material describes a shared failure among flight crew, maintenance, fuelling, manuals, and assignment of responsibility. "Canada's first metric-instrumented aircraft" is also too broad. The report says the 767's fuel gauges and load calculations were in kilograms and its drip sticks in centimetres; other aircraft systems still used non-metric aviation units. The bibliography entry `acc:casb-gimli` is not release-ready: the title and institution need confirmation, URL or archive location, and page pins. I found a public copy of the 1985 Lockwood Board of Inquiry report, but not a stable official CASB-hosted copy from the bibliography alone.

Ariane 5 Flight 501. The chapter's core mechanism is mostly right but has two important imprecisions. First, line 356 says "39 seconds after lift-off." The Inquiry Board timeline is relative to `H_0`, the start of main engine ignition. Lift-off was about `H_0 + 7.5 s`; the vehicle began to disintegrate about `H_0 + 39 s`, and ESA's public summary describes loss of guidance at 37 seconds after main engine ignition, about 30 seconds after lift-off. Second, the chapter frames the missing check as "measurement" of maximum horizontal velocity. The report frames it as inadequate analysis and testing of the inertial reference system and complete flight control system, plus reuse of Ariane 4 SRI software. The overflowing value was the internal alignment variable BH, Horizontal Bias, related to horizontal velocity, in a function that served no purpose after lift-off for Ariane 5. That is a verification-domain failure with a measurement theme, not a measurement failure in the ordinary sense.

Boeing 747 estimation block. The published MTOW figure is close: Boeing lists 396,890 kg, 875,000 lb, for the maximum 747-400. But the estimation is internally poor. It assigns empty mass as about 400 t, then adds fuel and passengers to reach 600 t. Empty mass cannot exceed the 396.89 t MTOW. Boeing's reference guide and common airport-planning data put operating empty weight closer to 179 t for a passenger 747-400, with fuel capacity roughly 216,800 L, or about 170 t at jet-fuel density. A better estimate is 40 t passengers and bags, 180 t empty aircraft, 150 to 170 t fuel, and some cargo/reserve margin, giving about 370 to 430 t. The current block trains the right order-of-magnitude habit but also normalizes an impossible subtotal.

Type A / Type B uncertainty. The chapter correctly states that Type A evaluation uses statistical analysis and Type B uses other information. The heading "Random and systematic uncertainty" is the problem. GUM and VIM distinguish method of evaluation from random/systematic behavior. A Type B component can describe a systematic effect after correction; a Type A analysis can estimate repeatability under defined conditions. The sentence "random error can be reduced by averaging, systematic error cannot" is useful as an introduction, but it must not be made equivalent to Type A and Type B. The claim that combined uncertainty cannot be smaller than either component needs the uncorrelated, positive-variance case stated; the exercise on correlated sums later asks for a case where uncertainty becomes smaller through negative covariance.

Unit arithmetic. The prose conversion factor for MCO should be 1 lbf = 4.4482216152605 N, so "approximately 4.45" is acceptable. The Air Canada 1.77 lb/L versus about 0.80 kg/L conversion is acceptable, but the chapter should show the division by 2.2 at least once. Exercise 2 gives 396 t as a round MTOW; the conversions are approximately 396,000 kg, 873,031 lb, and 27,135 slugs. If the exercise wants Boeing's exact MTOW, use 396,890 kg, 875,000 lb, and about 27,196 slugs. The torque exercise should expect 40 N m = 29.50 ft lbf and 40 ft lbf = 54.23 N m. The medical syringe exercise gives 0.008 mL, or 8 microlitres; as written it is not answerable without a required tolerance or a syringe resolution.

Other technical imprecisions. Line 423 says calibration is "the subject of the next chapter," but Chapter 2 is Units and dimensions; calibration is Chapter 3. Lines 206-210 describe estimating error from dispersion, resolution, certificates, and propagation rules. That estimates uncertainty, not error. Lines 242-246 say accuracy is improved by calibration; calibration establishes a relation to a reference, while adjustment or correction improves trueness in use. The statement can be repaired, but left as is it will irritate a metrologist.

## D. Pedagogical review

The chapter does build a measurement habit. Its strongest teaching sequence is "measurement as shareable record" to "estimation before calculation" to "seven-component measurement entry" to "one-week household logbook." That is the right first-chapter move. The chapter also does the important thing early: it asks the reader to record estimates before measuring, which attacks hindsight correction and confirmation bias.

The pedagogical problem is difficulty drift. The prose says the reader does not need the formal uncertainty machinery yet, then the exercises ask for standard deviation of the mean, propagation of product uncertainty, correlated uncertainty of sums, normal simulations, bivariate normal sampling, and sample-standard-deviation plots. Those are legitimate exercises for Volume I, but not for this chapter unless the exercise set is explicitly path-tagged and scaffolded. A core reader in Chapter 1 can do unit conversions, record measurements, estimate orders of magnitude, and diagnose unit-interface failures. They cannot be expected to derive covariance propagation before the book has taught variance.

The 28 exercises are numerically balanced across Q16 types:

- Calculation: 4.
- Derivation: 3.
- Estimation: 5.
- Simulation: 3.
- Design: 3.
- Diagnosis and reverse engineering: 3.
- Failure analysis: 3.
- Judgment: 4.

That distribution is good for a pilot template, but several individual problems need sharper constraints. Exercise 715, smartphone measurements per second, is too vague to be gradeable. Exercise 763, kitchen scale calibration to 2 percent, depends on the legal tolerances and local packaging of the chosen references; it needs allowed reference classes. Exercise 659, syringe volume, needs a tolerance and must say whether an ordinary syringe is permitted. Exercises 668-691 and 730-752 should become standard/mastery, not core. Exercise 721 requires the reader to look up global cement production; it is a good dated-statistics exercise, but the problem should require a source and year, and the solution should cite a specific dataset.

The project matches Q55-pilot in kind: household plus analysis, no serious hazard, logbook plus reflection. The time budget does not match the adult-life assumption. Two to four hours per day for seven days, plus analysis and writing, is 16 to 31 hours for the first chapter. The project can be serious without demanding that much daily attention. A better version asks for 20 to 30 minutes of measurement per day, one longer repeat-measurement session, and a two to three hour analysis block at the end.

The estimation block can become the recurring template, but the 747 example needs repair before it becomes canonical. A first template should not include an impossible component estimate. The template should show: rough decomposition, sanity check against a known bound, result, comparison to source, and postmortem on the error. That last step is missing. It says the factor-of-three check "almost passed"; it did pass if the estimate is high by 1.5. The phrase should be "passed."

## E. Citation discipline

The chapter fails citation discipline as a pilot.

Missing load-bearing citations:

- Lines 4-8, Kelvin epigraph: direct historical quotation with no bibliography entry and no page pin.
- Lines 30-38, claims about smiths, masons, millwrights, craft knowledge, and transmission through apprenticeship.
- Lines 100-107, construction delivery-slip details, slump, chloride content, and 7/28-day cylinder verification.
- Lines 118-124, pharmacy sterile dose, welding procedure variables, and router reconfiguration as cross-domain examples.
- Lines 127-138, Tay Bridge, Tacoma Narrows, Bhopal, Chernobyl, Deepwater Horizon.
- Lines 172-194 and 644-650, Boeing 747-400 MTOW and conversions.
- Lines 242-246, precision/accuracy correction routes, if left as a metrology claim rather than a local teaching simplification.
- Lines 501-520, 2026 two-system unit-system claim, US/UK/customary persistence, and industry examples.
- Lines 537-538, "Each has, on documented occasions, killed people."
- Lines 549-553, specific examples of artifacts using imperial values, if kept as factual examples rather than house-style statements.

Citation-tier mismatches:

- Named accidents cite `acc:` entries, but the three short case treatments do not meet the named-accident rule in `docs/citation-policy.md`: official primary report, regulatory/legal context where relevant, independent secondary analysis, technical mechanism, organisational mechanism, and lessons by scale. If Chapter 1 uses abbreviated cases, the registry must exist and carry the full apparatus.
- `acc:casb-gimli` is not adequately verifiable from the bibliography. The source may exist, but the current entry gives no report number, URL, archive, or page data. The available public report I could verify is the 1985 Lockwood Board of Inquiry final report, not the exact title in the bib entry.
- `std:bipm-si2019` supports what SI is, but not the whole claim about customary/imperial use in US construction, UK plumbing, aviation operations, and legacy datasheets.
- `text:mahajan2014` is acceptable for estimation pedagogy, but not for Boeing aircraft data.

Bibliography apparatus problem:

For a pilot chapter, `references.bib` needs URLs, report numbers, and access or archive notes for public primary reports. The chapter also needs page or section pins for direct quotations, accident mechanisms, and standards definitions. Without those pins, the reviewer cannot distinguish a verified source from a remembered story.

## F. Reader-path tagging

The current tags are not yet defensible as the pilot convention.

The case-study section is tagged `standard`, but it carries the chapter's public proof that measurement failures matter. For a first-pass reader, at least the three-case pattern and one fully worked case must be `core`. A workable split is: case summaries `standard`, "The pattern" `core`, and a compact Mars Climate Orbiter interface diagram `core`.

The `mastery` box on significant figures is mis-tagged. Significant figures are not mastery material in a measurement volume. Either move it to Chapter 2 or 4, or make it `standard`.

The project section is untagged, so it defaults to `standard`. Q51 says projects are part of the core path. Add `\pathtag{core}` to `\section{Project}` or make the project environment itself carry core status.

The exercise section is untagged and defaults to standard. That is acceptable only if each exercise group carries path labels. Calculation, basic estimation, measurement logbook diagnosis, and the first failure-analysis problem can be core. Derivations with covariance and the simulation block should be standard/mastery until the needed statistics and programming have been taught.

## G. Specific concrete fixes

1. File: `volumes/01-quantity/ch01-why-we-measure/chapter.tex`, lines 4-8.

Current text: `When you can measure what you are speaking about...`

Proposed replacement: Use the full Kelvin quotation with ellipses for any omission, and add a citation in the epigraph source: `William Thomson, Lord Kelvin, "Electrical Units of Measurement," lecture delivered at the Institution of Civil Engineers, 3 May 1883, in \emph{Popular Lectures and Addresses}, vol. 1, pp. 80-81 \cite[p.~80]{hist:kelvin1891}.`

2. File: `bibliography/references.bib`, after line 202.

Current text: no Kelvin entry.

Proposed replacement: Add `@book{hist:kelvin1891, author = {Thomson, William}, title = {Popular Lectures and Addresses, Volume I: Constitution of Matter}, publisher = {Macmillan and Co.}, year = {1891}, address = {London}, note = {Includes "Electrical Units of Measurement," lecture delivered 3 May 1883}}`.

3. File: `volumes/01-quantity/ch01-why-we-measure/chapter.tex`, lines 18-21.

Current text: `We open the work with the act that opens engineering itself: putting a number on the world.`

Proposed replacement: `We begin with measurement because every later engineering act depends on a number that can be checked, repeated, and communicated. Before we model, design, build, or repair, we measure.`

4. File: `volumes/01-quantity/ch01-why-we-measure/chapter.tex`, lines 25-28.

Current text: `Measurement is the act by which the world becomes accountable to engineering.`

Proposed replacement: `Measurement turns a private observation into a public engineering claim. Once a quantity has been measured, it can be compared, reproduced, communicated, archived, contracted, diagnosed, and calibrated.`

5. File: `volumes/01-quantity/ch01-why-we-measure/chapter.tex`, lines 30-38.

Current text: `Pre-measurement crafts were not crafts without quantities...`

Proposed replacement: `Older crafts carried quantities in trained bodies, tools, proportions, marks, sounds, and repeated practice. The smith's judgement of iron, the mason's judgement of stone, and the millwright's judgement of timber could be precise in practice. What they could not always do was travel cleanly through a drawing, contract, calibration certificate, or failure investigation.`

6. File: `volumes/01-quantity/ch01-why-we-measure/chapter.tex`, lines 79-84.

Current text: `This chapter introduces measurement as a discipline...`

Proposed replacement: `The rest of Volume I turns this discipline into working habits: units, calibration, traceability, error propagation, sensors, instruments, statistics, and estimation. Volume II then gives those quantities mathematical form.`

7. File: `volumes/01-quantity/ch01-why-we-measure/chapter.tex`, lines 100-107.

Current text: foundation-pour delivery slip paragraph with slump, chloride content, and 7/28-day cylinders.

Proposed replacement: Keep the paragraph but add standards citations, or generalise it: `A delivery slip names the mix design, the specified strength, the time of mixing, and the truck identification. Site tests and later strength tests turn that delivery into a record rather than a promise.`

8. File: `volumes/01-quantity/ch01-why-we-measure/chapter.tex`, lines 127-138.

Current text: `Engineering history is, in part, a graveyard of unmeasured judgments...`

Proposed replacement: `Many engineering failures include a missing, ignored, or misread measurement. We will study Tay Bridge, Tacoma Narrows, Bhopal, Chernobyl, and Deepwater Horizon in Volume X only where the primary record supports the mechanism. The lesson here is narrower: a decision without a measurement record cannot be reconstructed after failure.`

9. File: `volumes/01-quantity/ch01-why-we-measure/chapter.tex`, lines 180-194.

Current text: 747 estimate with `empty mass \sim 10 \times payload, so \sim 400 t` and `Sum: roughly \sim 600 t`.

Proposed replacement: `A 747-400 carries roughly 400 passengers; with crew and baggage, call that 40 t. A wide-body airframe is several times heavier than its passenger load; call the operating empty mass about 200 t. Long-haul fuel is comparable to the empty-mass scale; call it 150 to 170 t. Add a small cargo and reserve margin. Estimate: 390 to 430 t. Boeing lists the maximum 747-400 take-off weight as 396,890 kg, or about 397 t \cite{web:boeing-commercial-reference}.`

10. File: `bibliography/references.bib`, web section.

Current text: no Boeing source.

Proposed replacement: Add `@misc{web:boeing-commercial-reference, author = {{Boeing Commercial Airplanes}}, title = {Commercial Airplanes Reference Guide}, howpublished = {\url{https://www.boeing.com/productstory/Commercial_Airplanes_Reference_Guide.pdf}}, year = {2026}, note = {747-400 principal characteristics}}`.

11. File: `volumes/01-quantity/ch01-why-we-measure/chapter.tex`, lines 206-210.

Current text: `we estimate the error from the dispersion...`

Proposed replacement: `In most engineering settings the error is not known. We estimate uncertainty from repeated measurements, instrument resolution, calibration records, and propagation from input quantities.`

12. File: `volumes/01-quantity/ch01-why-we-measure/chapter.tex`, lines 212-218.

Current text: VIM error/uncertainty sentence.

Proposed replacement: Keep the VIM distinction but make it exact: `The international vocabulary of metrology defines measurement error as a measured quantity value minus a reference quantity value, and measurement uncertainty as a non-negative parameter characterising the dispersion of quantity values attributed to the measurand \cite{std:jcgm-vim}.`

13. File: `volumes/01-quantity/ch01-why-we-measure/chapter.tex`, lines 242-246.

Current text: `precision is improved by the instrument and the procedure, accuracy by calibration against a reference.`

Proposed replacement: `Precision is usually improved by the instrument, environment, and procedure. Calibration estimates the relation between indication and reference; adjustment or correction is what improves the reported value.`

14. File: `volumes/01-quantity/ch01-why-we-measure/chapter.tex`, lines 248-257.

Current text: subsection title `Random and systematic uncertainty` followed by Type A/B.

Proposed replacement: Change title to `\subsection{Type A and Type B evaluation}` and add: `Type A and Type B name how an uncertainty component is evaluated. They do not mean random and systematic. Random and systematic describe how errors behave in repeated measurements.`

15. File: `volumes/01-quantity/ch01-why-we-measure/chapter.tex`, lines 259-263.

Current text: `random error can be reduced by averaging, systematic error cannot, and the combined uncertainty cannot be smaller than either component.`

Proposed replacement: `Averaging can reduce the standard uncertainty associated with independent random variation. It does not remove a shared bias. For uncorrelated components combined in quadrature, the combined standard uncertainty is at least as large as the largest component; correlated components require the covariance term introduced in Chapter 4.`

16. File: `volumes/01-quantity/ch01-why-we-measure/chapter.tex`, lines 265-274.

Current text: significant figures in a `mastery` box.

Proposed replacement: Make it a standard paragraph or move it to Chapter 2. If it stays here, remove `\begin{mastery}` and soften `finger-counting`.

17. File: `volumes/01-quantity/ch01-why-we-measure/chapter.tex`, lines 285-286.

Current text: `with the confidence stated when it differs from 1 \sigma`.

Proposed replacement: `with the coverage probability or rule for the range stated.`

18. File: `volumes/01-quantity/ch01-why-we-measure/chapter.tex`, lines 298-301.

Current text: `We treat each briefly here as a measurement story...`

Proposed replacement: `We use abbreviated case summaries here and keep the full seven-part case records in the named-cases registry. Until that registry exists, these summaries are draft notes, not release-ready case studies.`

19. File: `volumes/01-quantity/ch01-why-we-measure/chapter.tex`, lines 310-324.

Current text: `ground software supplied trajectory correction data... spacecraft software expected newton seconds...`

Proposed replacement: `The mishap investigation found that the SM_FORCES ground software used thruster performance data in English units. Its AMD output file was required, by interface documentation, to contain impulse data in newton seconds, but the data were delivered in pound-force seconds. The trajectory modelers therefore used values low by about 4.45 in the orbit-determination model \cite{acc:nasa-mco-mib}.`

20. File: `volumes/01-quantity/ch01-why-we-measure/chapter.tex`, lines 319-324.

Current text: `A single, mandatory units-on-the-wire policy at the interface would have caught it on the first ground test.`

Proposed replacement: `The report's recommendations point to the missing barrier: verify consistent units across design and operations, audit data transferred between JPL and Lockheed Martin, and verify the small-forces models.`

21. File: `volumes/01-quantity/ch01-why-we-measure/chapter.tex`, lines 333-341.

Current text: `The 767 was Canada's first metric-instrumented aircraft... The crew used...`

Proposed replacement: `The 767 introduced kilograms into Air Canada's fuel quantity and load-calculation workflow while fuel volume was still handled in litres. In the abnormal drip-stick procedure, the people calculating the load used a factor near 1.77 lb/L where the calculation required about 0.80 kg/L. The result overstated fuel mass by about 2.2.`

22. File: `bibliography/references.bib`, lines 169-176.

Current text: `@techreport{acc:casb-gimli...}`

Proposed replacement: Verify the exact primary source. If using the Lockwood report, replace with `@techreport{acc:lockwood-gimli1985, author = {{Board of Inquiry} and Lockwood, George H.}, title = {Final Report of the Board of Inquiry Investigating the Circumstances of an Accident Involving the Air Canada Boeing 767 Aircraft C-GAUN at Gimli, Manitoba, 23 July 1983}, institution = {Minister of Supply and Services Canada}, year = {1985}, number = {Catalogue No. T22-64/1985E}}`, plus archive URL or library record.

23. File: `volumes/01-quantity/ch01-why-we-measure/chapter.tex`, lines 355-358.

Current text: `broke up 39 seconds after lift-off.`

Proposed replacement: `began to disintegrate about 39 seconds after main engine ignition, about 31 seconds after lift-off.`

24. File: `volumes/01-quantity/ch01-why-we-measure/chapter.tex`, lines 360-367.

Current text: Ariane conversion paragraph.

Proposed replacement: Add the alignment-function context: `The exception occurred inside the SRI alignment function, which was still running after lift-off because of an Ariane 4 requirement and was not needed for Ariane 5 after lift-off.`

25. File: `volumes/01-quantity/ch01-why-we-measure/chapter.tex`, lines 369-375.

Current text: `The validation envelope had not been measured against the new vehicle...`

Proposed replacement: `The Ariane 5 qualification work had not adequately analysed or tested that SRI software against the Ariane 5 flight domain. The missing check was not a sensor reading in flight; it was a verification test of the reused software against the new trajectory.`

26. File: `volumes/01-quantity/ch01-why-we-measure/chapter.tex`, lines 379-396.

Current text: pattern list says all three cases involved two systems with different number conventions.

Proposed replacement: Split the pattern: `Mars and Gimli are unit-interface failures. Ariane 501 is a range and reuse-envelope failure. The shared discipline is interface measurement: units, ranges, data types, provenance, and validation envelope must be explicit before integration.`

27. File: `volumes/01-quantity/ch01-why-we-measure/chapter.tex`, lines 423-425.

Current text: `Calibration is the subject of the next chapter.`

Proposed replacement: `Calibration is the subject of Chapter 3.`

28. File: `volumes/01-quantity/ch01-why-we-measure/chapter.tex`, lines 483-484.

Current text: `Note the zero offset before each reading session, and apply or correct.`

Proposed replacement: `Note the zero offset before each reading session, then correct the reading or record that no correction was applied.`

29. File: `volumes/01-quantity/ch01-why-we-measure/chapter.tex`, lines 501-520.

Current text: unit-system persistence paragraph.

Proposed replacement: Add sources beyond BIPM, and separate SI authority from customary use: `SI is the international system maintained through the BIPM and CGPM \cite{std:bipm-si2019}. US customary and imperial units persist in specific jurisdictions, codes, installed instruments, and legacy designs; cite NIST, relevant national law, and industry standards before naming sectors.`

30. File: `volumes/01-quantity/ch01-why-we-measure/chapter.tex`, lines 537-539.

Current text: `Each has, on documented occasions, killed people.`

Proposed replacement: `Some have killed people, and all have produced expensive failures. The text should cite one documented case per category or cut the sentence.`

31. File: `volumes/01-quantity/ch01-why-we-measure/chapter.tex`, lines 561-563.

Current text: `\section{Project}` with no path tag.

Proposed replacement: `\section{Project}\pathtag{core}`.

32. File: `volumes/01-quantity/ch01-why-we-measure/chapter.tex`, lines 622-623.

Current text: `Two to four hours per day for seven days, plus two to three hours...`

Proposed replacement: `Twenty to thirty minutes per day for seven days, one repeat-measurement session of one to two hours, plus two to three hours of analysis and writing.`

33. File: `volumes/01-quantity/ch01-why-we-measure/chapter.tex`, lines 628-633.

Current text: exercise intro omits simulation, diagnosis, reverse engineering, and failure analysis.

Proposed replacement: `The exercises mix calculation, derivation, estimation, simulation, design, diagnosis, reverse engineering, failure analysis, and judgment per Q16.`

34. File: `volumes/01-quantity/ch01-why-we-measure/chapter.tex`, lines 668-691.

Current text: derivation exercises on standard deviation of mean, product propagation, and correlated sums.

Proposed replacement: Add path tags or defer: mark Exercise 668 as `standard`, move 675 and 687 to Chapter 4, or precede them with a short derivation scaffold defining variance, covariance, independence, and linearisation.

35. File: `volumes/01-quantity/ch01-why-we-measure/chapter.tex`, lines 715-719.

Current text: smartphone measurements per second.

Proposed replacement: `Estimate how many sensor readings your phone records during one minute while sitting still with the screen on. Count only sensors you can name from settings, documentation, or an installed sensor logger. State what you excluded.`

36. File: `volumes/01-quantity/ch01-why-we-measure/chapter.tex`, lines 721-725.

Current text: global cement mass-flow exercise.

Proposed replacement: Require citation: `Use a cited production figure from USGS, Global Cement and Concrete Association, or another named dataset, state the year, and compute tonnes per second.`

37. File: `volumes/01-quantity/ch01-why-we-measure/chapter.tex`, lines 730-752.

Current text: three simulation exercises with no path tags.

Proposed replacement: Mark the simulation subsection `\pathtag{mastery}` or make the first simulation standard and the bivariate-normal exercise mastery. Add a no-code spreadsheet option for the first simulation if Chapter 1 must remain self-contained.

38. File: `volumes/01-quantity/ch01-why-we-measure/chapter.tex`, lines 763-768.

Current text: kitchen scale calibration with "items the reader can be sure about."

Proposed replacement: `Use one of three reference classes: a calibration mass, coins whose official mass is published for the reader's country, or a sealed package with labelled net mass and stated packaging tolerance. State why the reference is only a check, not a traceable calibration.`

39. File: `volumes/01-quantity/ch01-why-we-measure/chapter.tex`, lines 789-794.

Current text: car fuel-economy discrepancy asks for "most plausible primary suspect."

Proposed replacement: `State at least three sources of discrepancy, then name the first measurement you would repeat before blaming the dashboard algorithm.`

40. File: `volumes/01-quantity/ch01-why-we-measure/chapter.tex`, lines 836-840.

Current text: supplier catalogue is in `pound mass and inches`.

Proposed replacement: `the supplier's catalogue gives dimensions in inches and allowable loads in lbf.`

## H. Top three structural risks

1. The named-case policy and the chapter-length instinct are in conflict. The pilot wants quick examples; the case-study template requires a seven-part record for every named accident. Before Chapter 2, create the named-cases registry and define a legal abbreviated form: one paragraph in the chapter, full apparatus in the registry, mandatory source pins, and lessons by scale. Without that, every chapter will either bloat or violate the policy.

2. The citation system is not yet strong enough for a 20,000-page technical work. Prefixes exist, but entries lack URLs, report numbers, archive locations, page pins, and claim maps. Before Chapter 2, add a per-chapter source ledger with columns for claim, line range, source key, page or section, tier, and verification status. The release checklist should fail a chapter on missing pins for quotations, standards definitions, accident mechanisms, and empirical numbers.

3. The exercise architecture needs path-aware difficulty gates. Q16 gives a healthy exercise taxonomy, but Chapter 1 already pulls in statistics, covariance, programming, and web data lookup before those tools are taught. Before Chapter 2, require each exercise to carry type, path, prerequisites, expected time, solution form, and source needs. That one schema will prevent future chapters from looking balanced by type while being miscalibrated by prerequisite.

