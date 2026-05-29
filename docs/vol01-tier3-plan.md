# Vol I Tier 3 expansion plan

Date: 2026-05-29.
Status: Preparation. Awaiting authorisation to execute.
Companion to: `docs/pilot-density-vol01-ch01.md` (Tier 1 pilot, 2026-05-16).

## What this plan is for

Volume I currently sits at 360 pp against the ~720 pp dossier target — Tier 1+2 density, ~50% of nominal. This document specifies the Tier 3 expansion needed to close the remaining gap, chapter by chapter, with concrete additions named rather than left as categories. It is the canonical reference for the rollout; turn-by-turn execution should be driven from these per-chapter specs rather than re-derived.

The pilot (Ch 1 Tier 1, May 2026) and the Tier 1+2 rollout (Ch 2-9 across May 2026) demonstrated that the per-chapter additions can be staged, voice-rule compliant, and discipline-guard passing. Tier 3 is the same machinery at greater amplitude.

## Tier 3 definition

Tier 1 added: per-exercise solutions, registry-quality named-case mentions, 4-6 TikZ figures, co-located code/data, a second estimation block.

Tier 2 added: sub-subsection deepening, additional named cases at short-form-summary level, expanded project blocks, one full-page figure per chapter.

Tier 3 adds (this rollout):

1. **Long-form case studies (3-6 pp each).** Named accidents that currently carry 80-120 lines of Technical mechanism / Organisational context / Lesson move to 3-6 pp of narrative: decision points named, quantitative costs given, the chain of failures walked. The registry entry remains canonical, but the chapter narrates rather than summarises.

2. **Multi-page worked examples (3-4 pp each).** Currently most worked examples are 1-2 pp inline. Tier 3 builds full reference examples with setup, model, computation, sanity check, error analysis, and an explicit "how to check your own version" rubric. Two-to-three per chapter on average.

3. **Dossier-promised material brought to depth.** Five subsections (§4.7, §6.5, §6.6, §8.5, §8.7) exist in current chapters but at 30-50% of dossier page targets. Tier 3 brings them to target.

4. **Historical sketches (1-3 pp each).** Currently absent. Short narratives of how each measurement discipline came to be — SI 2019 redefinition, NIST origin, GUM evolution, atomic-clock arc, Kibble balance — placed where they ground the technical content.

5. **Full solutions on a curated subset of exercises.** Tier 1 added solution sketches (~5-15 lines each). Tier 3 promotes ~10 per chapter to full 0.5-1 pp solutions, especially derivations, simulations, and judgment exercises whose sketches leave the most work to the reader.

Out of Tier 3 scope: replacing TikZ figures with externally-designed diagrams; per-volume reviewer engagement on the new prose; Q57 target revision (the rollout's achieved density informs Q57; the decision itself comes after).

## Per-chapter specification

Each chapter section lists current state, the largest gaps named at section level, the specific Tier 3 additions to make, and an estimated page lift. Page targets reference the dossier at `docs/research/01-quantity/chNN-*.md`.

### Ch 1 — Why we measure

Current: 32 pp, target 60 pp, gap +28 pp. Existing assets: 6 figures, 6 code, 4 data.

Largest gaps:
- §1.4 "Measurement crises" (MCO, Gimli Glider, Ariane 5): three cases at ~80-120 lines each from Tier 1+2; dossier targets 12 pp for the section. Cases are catalogued but not narrated.
- §1.5 "The measurement habit": six-field schema (dated, instrument+calibration, operator, conditions, provenance, signature) named but no worked notebook entries.

Tier 3 additions:
- Three long-form case-study expansions, 4-5 pp each (~12 pp total): MCO with the trajectory-correction decision point and the institutional context for the unit mismatch; Gimli Glider with the fuel-unit cascade, the 767 EFIS quirk, and the crew's pilot-side recovery; Ariane 5 with the inertial-reference-system attitude-angle overflow and the inheritance from Ariane 4. Use the registry entries as source-of-truth.
- Five worked notebook entries, 1-2 pp each (~8 pp total): structural deflection logged across a week; chemical titration with reagent traceability; circuit-board temperature swept across operating conditions; mains-frequency drift over 24 h; mass loss in a long-running evaporation experiment. Each entry shows every schema field populated.
- Historical sketch (~3 pp): metric-system adoption 1799-2019, ending at the 2019 SI redefinition. Frame as "why the measurement habit needed standards to lean on."
- Two additional figures: a one-page traceability-pyramid poster (forward reference to Ch 3); a one-page failure tree for the Ariane case.
- Project block (~3 pp expansion): add explicit success rubric, common failure modes, example of a model submission.

Estimated lift: +28 pp. Existing prose: untouched. Additions land as new subsections within the existing section skeleton.

### Ch 2 — Units and dimensions

Current: 30 pp, target 70 pp, gap +40 pp. Existing assets: 4 figures, 5 code, 3 data.

Largest gaps:
- §2.4 "Dimensional analysis as debugging": dossier target 16 pp, current ~5 pp. The checking discipline is present; the worked-example bank is thin.
- §2.5 "Buckingham pi theorem": dossier target 15 pp, current ~3-4 pp. The procedure is stated; multi-step derivations and the connection to experimental scaling are missing.

Tier 3 additions:
- Three long Buckingham-pi worked examples, 3-4 pp each (~10 pp total): Nusselt-Rayleigh in free convection (with the Moody-diagram analogue for heat transfer); pump affinity laws (head, flow, power vs impeller speed and diameter); wind-tunnel model-to-prototype scaling for lift and drag, including the Reynolds-mismatch problem and what to do about it.
- Dimensionless-group intuition section (~4 pp): why Re, Fr, Ma, Sh matter; reading published correlations; the Moody diagram annotated, with a worked friction-factor extraction.
- Unit-error audit subsection (~3 pp): a small catalogue of spreadsheet-and-code failures (NASA MCO already in Ch 1, plus a pharma-dosing case and an aerospace-firmware case); strategies for dimensional self-checking in code (Pint, unitful, dimensional types in Haskell/Rust); how to make unit failures impossible-by-construction.
- Historical sketch (~3 pp): the long road from artefact units (the prototype metre, the IPK) to constant-defined units (2019 redefinition); why the kilogram redefinition mattered for working engineers.
- Project expansion (~2 pp): success rubric and a worked example of one of the five required dimensional derivations.

Estimated lift: +40 pp.

### Ch 3 — Calibration and traceability

Current: 34 pp, target 80 pp, gap +46 pp. Existing assets: 4 figures, 5 code, 3 data.

Largest gaps:
- §3.6 "Cross-domain examples": dossier target 14 pp across five domains (voltage, mass, length, frequency, temperature); each currently 2-3 pp. The chain from primary standard to working instrument is sketched but not walked.
- §3.5 "Drift, recalibration intervals, the cost of calibration": dossier target 14 pp; current ~5-6 pp. The drift mechanisms are named but the cost-tradeoff decision is not delivered.

Tier 3 additions:
- Five cross-domain deep dives, 3-4 pp each (~16 pp total replacing current ~10 pp):
  - Voltage: Josephson array → nanovolt comparators → handheld DMM. With the 2019 SI redefinition's effect on volt traceability.
  - Mass: Kibble balance (post-2019) → dead-weight tester → laboratory balance. The IPK-drift registry entry as the named case.
  - Length: stabilised laser interferometer → gauge blocks → micrometer. Thermal expansion as the silent error.
  - Frequency: cesium fountain → OCXO → mains-frequency monitor. Forward reference to Ch 6 GPS.
  - Temperature: ITS-90 fixed points → SPRT → industrial RTD. The platinum resistance scale.
- Calibration cost-benefit workflow (~5 pp): Type A vs Type B classification; risk-scoring matrix; recalibration interval calculation given drift rate and acceptable out-of-tolerance probability; total-cost-of-ownership table for in-house vs accredited-lab vs vendor-cal.
- A 4-5 pp worked example: a small QC lab designs its calibration schedule end-to-end. Buys this set of standards, recalibrates at this cadence, accepts this risk, ships at this confidence.
- Historical sketch (~2 pp): NIST and BIPM origin and the post-WWII metrology infrastructure that made global manufacturing possible.
- Named-case expansion (~3 pp): a calibration failure with named cost — a pharmaceutical scale that drifted out of tolerance and contaminated a batch, or the Hubble null-lens calibration failure as a forward-reference to Ch 7.
- Project expansion (~2 pp): the "trace one measurement back to a national standard" exercise gets a worked example for a household thermometer.

Estimated lift: +46 pp.

### Ch 4 — Error and uncertainty

Current: 34 pp, target 100 pp, gap +66 pp. **Largest single gap in the volume.** Existing assets: 4 figures, 6 code, 3 data.

Largest gaps:
- §4.3 "Propagation: linear and Monte Carlo": dossier target 18 pp; current ~8 pp. Linear rules are present; Monte Carlo is named but no full worked code walkthrough.
- §4.4 "Central limit theorem in practice": dossier target 10 pp; current ~3 pp. Conditions and t-distribution named; the "what sample size is enough" question not delivered.
- §4.5 "Significant figures": dossier target 10 pp; current ~3 pp. Rules stated; deep treatment of guard digits, error accumulation, reporting conventions absent.
- §4.6 "Confidence intervals as engineering tools": dossier target 15 pp; current ~5 pp. CI for a mean covered; connection to design margin, tolerance stack, product specs not made.
- §4.7 "The cost of a smaller error bar": dossier target 10 pp; current ~4 pp. Conceptual; the economic curve missing.

Tier 3 additions:
- Monte Carlo propagation expansion (~6 pp): conceptual motivation (when linearisation fails); full code walkthrough with multivariate input distribution, covariance, and output distribution analysis (the existing code/ assets are the base); two worked physical examples (mechanical tolerance stack on a three-part assembly; optical aberration budget).
- CLT-in-practice deepening (~5 pp): explicit demonstrations at n=3, 5, 10 showing t-correction; a case where CLT visibly fails (Cauchy, financial returns); bootstrap as the empirical alternative.
- Sig-figs expansion (~5 pp): guard-digit strategy in multi-step calculations; rounding accumulation across long pipelines; reporting conventions for lab vs customer vs publication; the spreadsheet case study (forward reference to Ch 8 replication).
- Confidence intervals in design (~7 pp): two-sample CI; prediction interval (where the next measurement falls); simultaneous CI for multiple comparisons; the connection to product specification, tolerance stacking, and design margin; a manufacturing case where a CI was misinterpreted as a spec.
- Cost-of-precision section expansion (~5 pp): labour, instrument upgrade, time-on-test trade-off curves; the diminishing-returns plot from real data; a calibration-service case (what does it cost to move from ±2% to ±0.5%?).
- Hubble case study expansion (~5 pp): the auxiliary-test override from the registry's narrative; the organisational context (schedule pressure, the reflective null corrector, the dropped axial-spacing check); the COSTAR retrofit cost.
- One additional 3-4 pp worked example: tolerance stack on a precision mechanical assembly with both linear-propagation and Monte Carlo answers, demonstrating where they agree and where they don't.

Estimated lift: +66 pp. This chapter is the highest priority because it is the volume's foundational uncertainty reference; under-densing it leaves the rest of the book without a load-bearing companion.

### Ch 5 — Sensors and instruments

Current: 46 pp, target 90 pp, gap +44 pp. Existing assets: 6 figures, 6 code, 4 data.

Largest gaps:
- §5.2 "Transducer principles": six domains catalogued at 2-3 pp each; dossier target is 20 pp total. Each domain needs deeper worked examples.
- §5.4 "Choosing the right sensor": procedure outlined; dossier target 12 pp; current ~4 pp. The decision tree and multiple full selections are missing.
- §5.5 "Common instruments": DMM substantively present; oscilloscope, micrometer, sensor arrays are minimal. Dossier target 20 pp; current ~6 pp.

Tier 3 additions:
- Four sensor-principle deep dives, 2-3 pp each (~10 pp added):
  - Thermal: RTD lead-resistance compensation, thermistor Steinhart-Hart curve, thermocouple cold-junction; what each fails at and why.
  - Mechanical: strain-gauge bridge (excitation, temperature compensation, four-arm), accelerometer (proof mass, damping, DC-response limitation), capacitive displacement sensor.
  - Optical: photodiode (shot noise, dark current), photomultiplier (gain vs bandwidth), CCD/CMOS pixel-level noise.
  - Magnetic: Hall effect, fluxgate magnetometer, search-coil for AC fields.
- Sensor-selection workflow expansion (~6 pp): decision checklist (range, resolution, speed, environment, cost, regulatory); three full worked selections (water temperature in a heating loop; vibration on a rotating shaft; visible-light intensity in a dim space).
- Common-instrument expansion (~14 pp):
  - Oscilloscope (~4 pp): time-base and bandwidth, vertical-resolution math, triggering modes, aliasing in DSO sampling.
  - Micrometer and gauge blocks (~3 pp): zero-setting, Abbe error, thermal effects on precision dimensional measurement.
  - Sensor arrays (~4 pp): thermistor chains, strain-gauge rosettes, image-sensor demosaicing, cross-talk in multi-channel acquisition.
  - Spectrum analyser (~3 pp): RBW, VBW, dynamic range, noise floor; reading a real spectrum analyser display.
- Historical sketch (~3 pp): the long arc from artisanal calibration to the modern datasheet (Weston, GE, Hewlett-Packard, Keysight); why datasheets read the way they do.
- Failure-section expansion (~3 pp): the "sensor lies in the same direction" mode developed with a quantified case (e.g., a fleet of identical pressure sensors all reading low due to the same firmware bias).

Estimated lift: +44 pp.

### Ch 6 — Time, frequency, signals

Current: 44 pp, target 80 pp, gap +36 pp. Existing assets: 6 figures, 7 code, 4 data.

Largest gaps:
- §6.4 "Sampling and aliasing": dossier target 16 pp; current ~5 pp. Nyquist stated; anti-alias filtering and practical failures missing.
- §6.5 "Time-frequency duality preview": 227 lines (~5 pp); dossier target 12 pp. Informal Fourier and spectrogram are sketched but not delivered.
- §6.6 "GPS as a measurement system": 227 lines (~5 pp); dossier target 12 pp. The satellite constellation and trilateration are present; relativistic corrections, multipath, and DGPS need depth.

Tier 3 additions:
- Practical aliasing expansion (~6 pp): why Nyquist is necessary but not sufficient; anti-alias filter design (order, rolloff, passband ripple); worked case for audio at 44.1 kHz; a data-logger case where aliased high-frequency noise corrupted a low-frequency measurement.
- Time-frequency duality deepening (~5 pp): decomposing periodic signals into frequency components informally (before II.12 PDEs and Fourier theory); spectrogram with a worked audio example; the time-frequency uncertainty principle (you can't have both); where this matters in practice (lock-in detection, FFT on an oscilloscope, vibration spectrograms).
- GPS deepening (~6 pp): full satellite-constellation geometry and the time-difference fix; relativistic corrections (special + general, the ~38 μs/day correction); multipath in urban canyons; differential GPS and the centimetre regime; the GPS-week-rollover case from the registry as the named failure mode.
- Time-precision historical sketch (~3 pp): from Huygens's pendulum to the cesium fountain to optical clocks and frequency combs; why time became the precision anchor.
- Failure-section expansion (~3 pp): Patriot/Dhahran narrative deepened with the cumulative-error mechanism, the patched-binary context, and the timing-software lifecycle.
- One additional 3-4 pp worked example: measuring mains frequency over 24 h, comparing to published grid data, computing Allan deviation, and interpreting the diurnal cycle.

Estimated lift: +36 pp.

### Ch 7 — Length, area, volume, mass

Current: 42 pp, target 70 pp, gap +28 pp. Existing assets: 6 figures, 5 code, 3 data.

Largest gaps:
- §7.2 "Area, volume, density": dossier target 10 pp; current ~4 pp. Three methods named; integration of 3D scan data and thermal corrections missing.
- §7.4 "Specialised quantities: viscosity, hardness, surface roughness": dossier target 15 pp; current ~5 pp. Three measurement paradigms each severely compressed.
- §7.6 "Failure section: Hubble mirror": named; dossier target 11 pp; current ~4 pp.

Tier 3 additions:
- Volume-measurement expansion (~3 pp): 3D-scan mesh integration walkthrough (cleaning, watertight check, numerical methods); thermal-expansion correction; a case where water-displacement failed (porous clay).
- Viscosity deep dive (~3-4 pp): rotational vs capillary viscometers; shear-thinning fluids and power-law models; Arrhenius temperature dependence; measuring at process conditions vs lab conditions.
- Hardness deep dive (~3-4 pp): Rockwell, Vickers, Brinell indentation mechanics; why scale conversions are empirical not theoretical; depth-of-hardness case studies (surface hardening, carburising); the meaning of "62 HRC" on a knife datasheet.
- Surface-roughness deep dive (~3 pp): stylus-profilometer operation, lateral resolution, vertical noise; Ra vs Rq vs Rz; optical alternatives (interferometric, confocal); a finish-tolerance failure case.
- Hubble case-study expansion (~5 pp): null-lens test setup, the inserted lens-spacer error, why the cross-check on the auxiliary test was overridden, the on-orbit symptom diagnosis, the COSTAR retrofit cost, the post-flight process changes. Use the registry entry as source.
- Historical sketch (~2 pp): the metre's three definitions (1799 artefact, 1960 krypton, 1983 speed-of-light); the kilogram's 2019 redefinition.

Estimated lift: +28 pp.

### Ch 8 — Statistics for engineers

Current: 44 pp, target 90 pp, gap +46 pp. Existing assets: 6 figures, 6 code, 3 data.

Largest gaps:
- §8.3 "Hypothesis testing": dossier target 15 pp; current ~5 pp. Null/alternative defined; engineering decision context missing.
- §8.5 "Bayesian intuition": 168 lines (~4 pp); dossier target 12 pp. Concept named; prior+likelihood→posterior not delivered.
- §8.6 "Sample size and power": dossier target 10 pp; current ~3 pp. Power named; computation and the type-II-error cost not delivered.
- §8.7 "P-hacking and forking paths": dossier target 10 pp; current ~3 pp. Title present; the multiple-comparisons problem not developed.

Tier 3 additions:
- Hypothesis-testing workflow (~6 pp): reject/don't-reject language; p-value interpretation; three worked engineering decisions (does this batch meet spec? did the design change help? does the sensor calibrate the same at two temperatures?); when to use one-sided vs two-sided; the engineering preference for confidence intervals over p-values.
- Power analysis (~5 pp): why type-II error is costly; power curves; sample-size calculators (parametric and nonparametric); a design case where someone tested too few samples and missed a real effect.
- CI and prediction-interval expansion (~3 pp): CI for a difference (two-sample, paired, unpaired); prediction interval intuition; Bonferroni for simultaneous CIs; the manufacturing case where a CI was misinterpreted as a spec.
- Bayesian deepening (~5 pp): prior+likelihood→posterior in concrete engineering terms (you suspect a component is defective; you test it pass-fail; what's the probability it actually works?); beta-binomial as the working conjugate prior; when to use Bayesian methods (limited data, strong prior, sequential testing).
- P-hacking and replication (~5 pp): multiple-comparisons problem; correction methods (Bonferroni, FDR); pre-registration; the file-drawer effect; one real engineering replication failure (a sensor-calibration claim that didn't hold up across independent labs).
- Historical sketch (~2 pp): from Fisher to Neyman-Pearson to the ASA's 2016 statement on p-values; why the replication crisis pushed engineering toward stricter pre-registration.
- Project expansion (~2 pp): the 30-trial experiment gets a worked example showing what a model report looks like (problem, design, data, analysis, conclusion).

Estimated lift: +46 pp.

### Ch 9 — Discipline of estimation

Current: 54 pp, target 80 pp, gap +26 pp. **Smallest gap.** Existing assets: 6 figures, 5 code, 4 data.

Largest gaps:
- §9.3-9.5 (estimation before calculation, sanity-checking, deep uncertainty): combined ~5 pp; dossier target 30 pp combined. Compressed.
- §9.7 "Failure section: O-ring": ~2 pp; dossier target 10 pp.
- The 50-problem project: needs a deep population of problems across domains (currently fewer than 50 worked).

Tier 3 additions:
- "Estimation as a design habit" expansion (~5 pp): when to estimate (early design, before calculation, before experiment); how to use the estimate (sanity check, risk flag, stopping rule); a long case study where a Fermi estimate caught a $1M+ design error before fabrication.
- Deep-uncertainty section expansion (~4 pp): estimating when mechanisms are unknown (compound effects, black-swan risk); scenario analysis (best / likely / worst); probabilistic risk assessment intuition; a case where a tail-risk estimate mattered (extreme weather design load, supply-chain failure).
- O-ring failure expansion (~5 pp): the pre-launch decision reasoning (qualitative "should be OK" vs quantitative erosion-rate estimates); what a 1985-era quantitative failure-rate estimate would have shown; the post-disaster shift to evidence-based engineering. Use the Challenger registry entry.
- 50-problem bank completion (~5 pp): ensure full coverage across domains (biology, materials, geoscience, energy, information, finance) with realistic engineering contexts. Each problem with a Fermi-style decomposition and a check against ground truth where lookable.
- Historical sketch (~2 pp): Fermi's piano-tuner question to Mahajan's modern estimation pedagogy; why orders-of-magnitude reasoning became part of the engineering canon.
- Closing reflection expansion (~2 pp): estimation as a moral discipline (Q43 half-life); the working engineer's obligation to estimate before computing.

Estimated lift: +26 pp.

## Pre-flight cleanups

These should land before or during the rollout, so the expansion doesn't bake in regressions:

1. **Bibliography gaps in Vol VI Ch 8 and Ch 9.** 32 missing keys currently render as `[?]`. Not Vol I, but they break the build's clean state and obscure regressions introduced by Tier 3. Add stub entries (~30 min) before the Tier 3 rollout starts.
2. **Baseline status refresh.** `docs/status.md` Vol I span ("pp 1-328") and `CLAUDE.md` page counts ("3289 pages") are stale; current rebuild puts Vol I at 360 pp and the PDF at 3411 pp. Refresh before Tier 3 so per-turn deltas measure from a true baseline.
3. **Makefile / latexmkrc robustness.** The build sometimes leaves artifacts in the half-built state we hit before this turn (missing `.bbl`, populated `.bcf`). A small `.latexmkrc` change (`$force_mode = 1`) or a `-f` flag in the Makefile's latexmk invocation would prevent the next stale-PDF surprise mid-rollout.
4. **Vol I-only scratch validation.** Before the first Tier 3 chapter lands, run a small scratch expansion on a single section of Ch 4 (the highest-gap chapter) to validate the Tier 3 spec produces voice-compliant prose without surprise breakages. Equivalent of the May-16 pilot but at one tier higher.

## Execution options

| Option | Pace | Per-turn output | Best for |
|---|---|---|---|
| **A. Sequential single-chapter** | 1 chapter per turn, main thread | +28 to +66 pp per turn | Quality-first; default per `feedback_drafting_pace`. |
| **B. Parallel worktree fleet** | 5+4 batches across 2 turns | All 9 chapters in 2-3 turns | Throughput-first; matches the Vol I Tier 1+2 pattern. Needs explicit go-ahead. |
| **C. Hybrid, gap-weighted** | Main thread leads Ch 4; worktree agents close the rest in waves | Ch 4 in turn 1; remaining 8 in turn 2-3 | Best lift-per-turn ratio. |
| **D. Priority subset** | Ch 4, 3, 8 only (the +158 pp of biggest gaps) | 3 turns sequential or 1 turn parallel | If full Tier 3 is over-budget. Closes the worst gaps without committing to the full target. |

## Verification

Per-chapter (each Tier 3 expansion):
- `make check` — structural invariants.
- `make audit-docs` — stale-reference scan.
- `make accidents` — registry/citation consistency for any newly cited or newly expanded named case.
- `make exercise-counts` — `chapmeta` Exercise target line vs prose.
- Voice-rule scan of new prose: em-dashes (none), AI-tic vocabulary (per `docs/voice.md` ban-list), self-announcing topic sentences, negate-first-then-pivot, currency `\$` escape.
- Typo scan: `\end{exercise>` and analogous angle-bracket-instead-of-closing-brace errors.
- `make distclean && make` produces a clean PDF and the new chapter page span is recorded.

Per-volume (after Tier 3 completes on all 9 chapters):
- All four discipline guards PASS on the merged tree.
- New PDF page count and per-chapter span recorded.
- `docs/status.md` Vol I row updated: Vol I at Tier 3 density, pp 1-N where N is the new total.
- `CLAUDE.md` status footer updated.
- `docs/research/accidents/README.md` updated if Tier 3 introduced new registry entries.
- A closing entry in this document recording achieved density and the data point for Q57's eventual settlement.

## Estimated total lift

| Chapter | Current | Target | Tier 3 add | After Tier 3 |
|---|---:|---:|---:|---:|
| Ch 1 | 32 | 60 | +28 | 60 |
| Ch 2 | 30 | 70 | +40 | 70 |
| Ch 3 | 34 | 80 | +46 | 80 |
| Ch 4 | 34 | 100 | +66 | 100 |
| Ch 5 | 46 | 90 | +44 | 90 |
| Ch 6 | 44 | 80 | +36 | 80 |
| Ch 7 | 42 | 70 | +28 | 70 |
| Ch 8 | 44 | 90 | +46 | 90 |
| Ch 9 | 54 | 80 | +26 | 80 |
| **Vol I total** | **360** | **720** | **+360** | **720** |

If achieved, Vol I lands at 100% of dossier target. The PDF moves from ~3411 pp to ~3771 pp project-wide (Vol I shift only). This becomes the per-volume density model for the eventual Q57 settlement decision and the eventual Vol II-XII Tier 3 rollouts.
