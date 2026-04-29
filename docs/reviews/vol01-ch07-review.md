# Vol 01 Ch 07 Review

**Resolved: 2026-04-29.** All G1-G35 fixes and voice items B1-B14 applied to `volumes/01-quantity/ch07-length-area-volume-mass/chapter.tex`. Two new bibliography entries added: `std:iso-1-2022` (standard reference temperature for dimensional specifications, cited at G9) and `std:iso-21920-2-2021` (current surface-roughness terms standard, cited at G22, replacing the prior ISO 4287 reference). Technical defects corrected: scaling-archetype decade count (sixteen to seventeen), transistor-channel example replaced with "features in advanced integrated circuits, at a few nanometres," "fountain clock interferometer" replaced with "laser interferometer tied to an optical frequency standard," equal-arm versus force-restoration balance distinction restored, "gigatonne (a fully laden bulk carrier)" corrected to ship-scale weighbridges at $10^{8}$ to $10^{9} \,\si{\kilogram}$, air-buoyancy "loses weight by the mass of the displaced air" corrected to "loses apparent weight by the weight of the air it displaces," Hubble figure error stated as $0.4$-wave rms wavefront error at $632.8 \,\si{\nano\meter}$ alongside the local short form. Project hazard wording tightened (object selection, water away from electrical devices). Contact-based dimensional reconstruction promoted to mastery option using stacked-slice volume rather than divergence-theorem mesh. Body-surface-area and road-freight estimation exercises rewritten to bring sources into the solution notes. New simulation exercise (Monte Carlo on the triaxial ellipsoid) replaces the unsourced roughness exercise; total exercise count remains 28. Build verified: `make distclean && make strict` produces a 693-page `main.pdf`; `make check`, `make audit-docs`, `make accidents`, and `make exercise-counts` all PASS. The transient first-pass undefined-reference warning Codex saw for `tab:vol01-ch06-clock-families` resolves on the second latexmk pass (the label is present at `volumes/01-quantity/ch06-time-frequency-signals/chapter.tex:332`).

Build-facing note: Chapter 7 has no chapter-local unresolved citation or cross-reference in the checks we ran. `make strict` still reports one existing undefined reference outside this chapter, `tab:vol01-ch06-clock-families` in Volume I Chapter 6. The editor should fix that build warning separately before treating the full book build as clean.

Scope checked: `docs/editorial-decisions.md`, `docs/voice.md`, `docs/citation-policy.md`, `docs/reviewer-guide.md`, `docs/case-study-template.md`, `docs/research/landscape.md`, `docs/research/01-quantity/ch07-length-area-volume-mass.md`, `volumes/01-quantity/_volume.tex`, `volumes/01-quantity/ch07-length-area-volume-mass/chapter.tex`, and the cited BibLaTeX entries `std:bipm-si2019`, `std:jcgm-vim`, `text:ashby2017`, `text:taylor1997`, and `acc:nasa-hubble-optical-systems-1990`. We also checked external primary or institutional sources: [NASA NTRS, Hubble Space Telescope Optical Systems Failure Report](https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/19910003124.pdf), [BIPM SI Brochure](https://www.bipm.org/en/publications/si-brochure), [BIPM practical realizations](https://www.bipm.org/en/publications/mises-en-pratique/), [JCGM VIM](https://www.bipm.org/documents/20126/2071204/JCGM_200_2012.pdf/f0e1ad45-d337-bbeb-53a6-15fe649d0ff1), [ISO 1:2022](https://www.iso.org/standard/80702.html), and [ISO 21920-2:2021](https://www.iso.org/standard/72226.html).

## A. Verdicts

Technical: blocked. The chapter contains two embarrassing technical defects: the impossible "gigatonne" bulk-carrier claim, and an overbroad balance and scale treatment that blurs equal-arm mass comparison, force-restoration balances, and force scales. The chapter also has too many uncited instrument-performance figures for a metrology chapter.

Pedagogical: approved-with-corrections. The main habit, independent measurement with uncertainty, is sound and the project matches the dossier, but the contact-mesh option is too hard for the household track, the exercise set has no simulation item despite Q16, and several exercises require outside references without giving the reader a path.

Voice: approved-with-corrections. The chapter is mostly in the book's working register and has no em dash violations, but it leans on self-announcing topic sentences, a few inflated absolutes, and several meta tails that `docs/voice.md` explicitly tells us to cut.

## B. Voice Review

The chapter is cleaner than many drafts. It avoids the banned AI-tic vocabulary, it does not use rhetorical questions, and it does not overuse the guide's paragraph-opener warning. The voice problems are local and fixable. We list them in order.

1. `volumes/01-quantity/ch07-length-area-volume-mass/chapter.tex:20-27`

Offending sentence: "We walk the four quantities, name their working instruments, fold in viscosity, hardness, and surface roughness as extended cases, and close on the fact that disagreement among independent methods is the only honest detector of a wrong ruler."

Rule violated: `docs/voice.md`, "Not pedagogical in the bad sense" and "Self-announcing topic sentences." The sentence tells the reader the chapter's route rather than making the claim.

Rewrite: "Length, area, volume, and mass become engineering quantities only when their instruments, uncertainty budgets, and independent checks travel with them."

2. `chapter.tex:31-37`

Offending sentence: "Length is the quantity engineering measures most often and at the widest dynamic range."

Rule violated: `docs/voice.md`, "Not hyped" and "Numbers carry their year." The sentence makes an absolute claim without support.

Rewrite: "Length is one of the quantities engineering measures most often, and its practical range is unusually wide."

3. `chapter.tex:40-46`

Offending sentence: "The geometric quantities span more decades than any other base quantity in everyday engineering."

Rule violated: `docs/voice.md`, "No invented scenes or figures" and "Not hyped." The "more decades than any other" claim is unsupported and likely impossible to defend across fields.

Rewrite: "Geometric quantities span enough decades that the reader needs an internal ruler, from atomic spacing to continental distance."

4. `chapter.tex:51-54`

Offending sentence: "The reader meets seven length instruments in routine engineering practice."

Rule violated: `docs/voice.md`, "Self-announcing topic sentences." This is a course-map sentence.

Rewrite: "Seven instruments cover much of routine length work."

5. `chapter.tex:245-251`

Offending sentence: "A density measurement is no more precise than the less precise of its two inputs, in relative terms."

Rule violated: `docs/voice.md`, "Formally precise." The prose oversimplifies the quadrature result. If the two relative uncertainties are equal, the result is larger than either by a factor of square root two.

Rewrite: "The larger relative uncertainty usually dominates the density uncertainty; when the two inputs are comparable, both must be carried in quadrature."

6. `chapter.tex:279-287`

Offending sentence: "A direct measurement of the same plate using a kitchen scale and water displacement, performed by the reader before this paragraph was written, gave $830 \,\si{\gram}$ and $370 \,\si{\milli\liter}$ displacement, density $2240 \,\si{\kilogram\per\meter\cubed}$."

Rule violated: `docs/voice.md`, "No invented scenes or figures." The source is opaque and the phrase "before this paragraph was written" reads like authorial performance rather than a reproducible measurement record.

Rewrite: "As a worked comparison, take a measured plate with $m = 830 \,\si{\gram}$ and displaced volume $V = 370 \,\si{\milli\liter}$; its density is $2240 \,\si{\kilogram\per\meter\cubed}$."

7. `chapter.tex:290-306`

Offending sentence: "Surface area matters in heat transfer (convective and radiative), in chemical reactions (catalyst loading, corrosion, drug dissolution), in coating cost estimation, and in biological transport."

Rule violated: `docs/voice.md`, "No invented scenes or figures." The examples are good, but they are load-bearing domain claims with no citation or later worked use.

Rewrite: "Surface area enters heat-transfer, reaction-rate, coating, and biological-transport calculations; Volume IV and Volume V return to those uses with the governing models."

8. `chapter.tex:390-398`

Offending sentence: "Mass spectrometry is not a household instrument."

Rule violated: `docs/voice.md`, "Negate-first-then-pivot construction." The next sentence pivots into where the reader meets it.

Rewrite: "Mass spectrometry belongs to chemistry, biochemistry, materials analysis, and nuclear science rather than household measurement."

9. `chapter.tex:393-398`

Offending sentence: "We name it here so that the reader knows the instrument exists and what its working principle is, and so that the catalogue of mass instruments spans the dynamic range from the gigatonne (a fully laden bulk carrier) to the dalton (a single proton)."

Rule violated: `docs/voice.md`, "Not pedagogical in the bad sense" and "No invented scenes or figures." "We name it here so that" is a self-justifying tail, and the bulk-carrier figure is technically wrong.

Rewrite: "It belongs in the catalogue because mass work ranges from ship-scale weighbridges to atomic-scale mass-to-charge measurements."

10. `chapter.tex:433-438`

Offending sentence: "Three quantities appear often enough in working engineering that a chapter on length, area, volume, and mass cannot pass them in silence."

Rule violated: `docs/voice.md`, "Not breathless." "Cannot pass them in silence" is a stage phrase.

Rewrite: "Three related quantities recur often enough to name here before Volume V treats them in detail."

11. `chapter.tex:528-535`

Offending sentence: "The chapter's central pedagogical move is here."

Rule violated: `docs/voice.md`, "Not pedagogical in the bad sense." The sentence announces pedagogy to the reader.

Rewrite: "The practical test is independent measurement of the same quantity."

12. `chapter.tex:537-541`

Offending sentence: "Cross-checking is the only honest detector of a wrong ruler."

Rule violated: `docs/voice.md`, "Not hyped." The sentence is memorable, but "only honest" overstates. Calibration audits, interlaboratory comparisons, and traceability reviews can also detect wrong references.

Rewrite: "Cross-checking is the most direct detector of a wrong ruler available inside a local measurement task."

13. `chapter.tex:748-750`

Offending sentence: "A reader who treats a precise instrument as authoritative without independent verification is reading from Hubble's playbook."

Rule violated: `docs/voice.md`, "The flat declarative." The idiom is cute where the failure section needs plain force.

Rewrite: "A reader who treats a precise instrument as authoritative without independent verification repeats the Hubble failure mode."

14. `chapter.tex:917-923`

Offending sentence: "The exercises move from numerical calculation through derivation, estimation, design, diagnosis, failure analysis, and judgment. Closed problems have full solutions; open-ended problems have rubrics or reference write-ups. Exercises are tagged with their reader-path tier."

Rule violated: `docs/voice.md`, "Self-announcing topic sentences" and "No invented scenes or figures." The chapter file does not contain those solutions or rubrics, and no companion file exists for this chapter.

Rewrite: "The exercises test calculation, derivation, estimation, design, diagnosis, failure analysis, and judgment. The editor should attach solutions and rubrics before release."

## C. Technical Review

The chapter's main equations are dimensionally sound. The area propagation formula, density propagation formula, compatibility-ratio calculation, ellipsoid volume calculation, and difference uncertainty calculation all cancel correctly. The worked stone example gives $39.2 \,\si{\milli\liter}$ for the ellipsoid, $u_B \approx 3.3 \,\si{\milli\liter}$, and $r \approx 2.4$; those numbers check.

The named accident is also basically correct. The NASA Optical Systems Failure Report, NASA TM-103443, supports the RNC lens spacing error of about $1.3 \,\si{\milli\meter}$, the auxiliary-test warnings, the reliance on the reflective null corrector, and the cost and schedule pressure. The chapter's citation to `acc:nasa-hubble-optical-systems-1990` is the right tier. We would still sharpen line 696: the NASA NTRS abstract states a 0.4-wave rms wavefront error at 632.8 nm. The local accident registry uses the "about $2 \,\si{\micro\meter}$ too flat at the outer edge" short form. That is acceptable if the chapter keeps the primary report citation, but it should avoid making the edge error sound like the only specification of the optical fault.

The defects are elsewhere.

First, the scaling archetype has a numerical error. From $10^{-10} \,\si{\meter}$ to $10^{7} \,\si{\meter}$ is a factor of $10^{17}$, or seventeen decades, not sixteen. If the chapter wants sixteen decades, the upper endpoint should be $10^{6} \,\si{\meter}$ or the lower endpoint should be $10^{-9} \,\si{\meter}$.

Second, the opening length example uses "the diameter of a transistor channel, near $10^{-9} \,\si{\meter}$." A transistor channel is usually described by gate length, channel length, fin width, or feature pitch, and modern technology-node labels are not literal dimensions. The sentence should use "features in advanced integrated circuits, at a few nanometres" or use atomic spacing for the lower end.

Third, "fountain clock interferometer" is an awkward and likely wrong instrument phrase. Atomic fountain clocks realize time and frequency; length interferometry is tied to optical frequency and the speed of light. If the sentence wants a dramatic range, say "a steel rule to a laser interferometer tied to an optical frequency standard."

Fourth, the ruler and tape item says calibration against "a gauge block or an SI metre bar." Gauge blocks are not the standard way to calibrate tape measures across metres, and an "SI metre bar" is historical language after the modern definition of the metre. The chapter needs a current dimensional metrology source, or it should phrase the point more generally as calibration against a traceable length standard at a stated temperature.

Fifth, the caliper resolutions are too rough. A "Vernier caliper" commonly resolves $0.02 \,\si{\milli\meter}$ or $0.05 \,\si{\milli\meter}$; $0.1 \,\si{\milli\meter}$ describes a simple sliding scale. Digital calipers often display $0.01 \,\si{\milli\meter}$, but display resolution is not accuracy. The chapter should separate display resolution, repeatability, and accuracy.

Sixth, the CMM, total-station, and interferometer performance numbers are presented without standards or manufacturer classes. "Kilometres at millimetre resolution" for a total station should be "millimetre plus ppm accuracy under specified conditions." "Fractional length uncertainties near $10^{-7}$ to $10^{-8}$ are routine" for a calibrated bench interferometer is plausible for some setups and weak for others. A metrology chapter cannot leave these as free-floating figures.

Seventh, the density section gives material densities correctly for common materials, but it makes a false practical comparison. A kitchen scale with $1 \,\si{\gram}$ resolution on a $100 \,\si{\gram}$ sample is a $10^{-2}$ relative display step, not $10^{-3}$. If the chapter wants $10^{-3}$, it needs a $0.1 \,\si{\gram}$ scale or a kilogram-scale sample.

Eighth, the estimation block uses uncited ceramic densities and an opaque "performed by the reader" measurement. The calculation itself is fine: $830/370 = 2.24 \,\si{\gram\per\centi\meter\cubed}$. The problem is provenance and repeatability.

Ninth, the mass section needs conceptual repair. Equal-arm balances compare mass and are nearly independent of local $g$ for the same site and air conditions. Force-restoration electronic balances measure force and report mass after calibration. Load-cell scales measure force and report mass units by convention. The chapter currently states "A balance reports mass, not weight" and then immediately says a balance moved in latitude reads differently unless recalibrated. That is true for many electronic balances, not for the classical two-pan balance described a few paragraphs earlier.

Tenth, the Quito example is plausible in order of magnitude, but it needs a source or a local-gravity calculation. A claim about local $g$ in a named city is a dated geophysical figure. It also depends on the calibration point chosen for "northern Europe."

Eleventh, the mass spectrometer paragraph says the mass-instrument catalogue spans "from the gigatonne (a fully laden bulk carrier) to the dalton." A fully laden bulk carrier is not a gigatonne. The largest ships are on the order of $10^8$ to $10^9 \,\si{\kilogram}$, hundreds of thousands of tonnes, while a gigatonne is $10^{12} \,\si{\kilogram}$. This is the most embarrassing numerical error in the chapter.

Twelfth, the air-buoyancy section says a sample "loses weight by the mass of the displaced air." It loses apparent weight by the weight of displaced air. The apparent mass correction also depends on the density of the reference weights. The example's order of magnitude is acceptable, but the wording should be corrected.

Thirteenth, the viscosity, hardness, and roughness subsections need standards. Water at $20 \,\si{\degreeCelsius}$ near $1 \,\si{\milli\pascal\second}$ is correct. The engine-oil and honey ranges are broad and temperature-dependent. The "factor of two for every $20 \,\si{\degreeCelsius}$ for many liquids" sentence is too loose. Hardness scales need ASTM or ISO references. Surface roughness should refer to the current ISO 21920 profile standard rather than "ISO 4287 conventions," which ISO now lists as withdrawn and replaced by ISO 21920-2:2021 for terms and parameters.

Cross-references are clean in this chapter. The file defines `\label{vol01:ch07}` and does not use `\cref`, `\autoref`, or `\ref`. The plain prose references to sections and previous chapters are human-readable, but "section 7.5" in lines 777 and 879 will become fragile if sections are rearranged. Use a label when the section exists.

## D. Pedagogical Review

The chapter does build the promised habit. The central habit is not "learn four quantities." It is "measure the same quantity several independent ways and force the disagreement to teach you." That habit appears in the cross-checking section, the stone example, the Hubble failure section, the project, and several exercises. The failure section closes the chapter's mechanism well: Hubble's RNC was a wrong ruler, and auxiliary tests were the missing independent measurement.

The archetypes are handled cleanly in concept. Scaling appears in the length section and balance appears in the mass section. The balance archetype recurs from earlier dimensional balance work rather than arriving as a new unexplained idea. The only archetype defect is the decade-count error in the scaling box.

The estimation block works in shape: estimate first, calculate from a crude geometric model, compare to a measurement. It needs source cleanup, but as a teaching move it is on target. The model is simple enough for an adult reader and tied to density as material discriminator.

The exercises hit most Q16 categories. We counted 28 exercises, matching the chapmeta target: five calculation, four derivation, five estimation, four design, four diagnosis and reverse engineering, three failure analysis, and three judgment. There is no simulation exercise. For this chapter, a light simulation exercise would fit naturally: Monte Carlo propagation for the ellipsoid, compatibility-ratio sensitivity, or random grid-cell area counting. The absence is not fatal, but Q16 names simulation explicitly.

Several exercises need calibration. The body-surface-area exercise asks the reader to compare to the Du Bois formula, but the chapter gives no citation or form of the formula. The semi-trailer exercise asks for EU regulation and year, which turns an estimation exercise into a legal lookup unless a source is supplied. The roughness exercise asks the reader to cite milling and polishing $R_a$ values, but the chapter has not provided a source. Those can stay if the exercise heading declares "research allowed" and the solutions file supplies acceptable references.

The project matches Q55 in intent: three independent volume measurements, uncertainty bars, pairwise compatibility, and a 1500-word reflection. The water-displacement and geometric methods are tractable. The image-based method is plausible if the reader has access to a scanning app, though the uncertainty procedure needs more concrete guidance. The contact-based dimensional reconstruction option is too ambitious for the household track. Twenty surface points plus a closed polyhedral mesh and divergence-theorem volume is beyond the chapter's mathematical prerequisites, especially before Volume II. It should be mastery or removed from the required menu.

The project also needs a safety correction. It labels hazard class "none," but immersion of jewellery, tools, and pottery can damage objects, and glassware plus water on a workbench can still create minor household risks. The hazard class can remain none only if the object-selection text tells the reader to use an expendable object and avoid sharp, electrical, valuable, or water-damaged items.

The chapter respects engineering depth most of the time. It does not drift into science-undergraduate derivations. The risk is the opposite: specialized quantities are introduced at recognition level with too little citation discipline. That is acceptable as a bridge to Volume V only after the standards and data sources are named.

## E. Citation Discipline

The chapter cites five entries. The Hubble accident citation is the right tier. The SI and VIM entries are appropriate for the epigraph's vocabulary, but the epigraph should not imply that the quoted sentence is a phrase from either source. Mark it as the book's formulation or remove the source line.

The following load-bearing claims need citations or weaker wording:

1. Instrument ranges and resolutions for rulers, tapes, calipers, micrometers, dial gauges, CMMs, laser distance meters, total stations, and interferometers at lines 57-106.
2. The standard reference temperature of $20 \,\si{\degreeCelsius}$ at line 131. Cite ISO 1:2022 or an equivalent dimensional-metrology source.
3. The stoneware and porcelain density values at lines 263-266.
4. The kitchen-scale and graduated-cylinder relative uncertainty comparison at lines 247-250.
5. The 2019 mass-realization claim at lines 310-314. Cite BIPM locally.
6. Analytical-balance and microbalance resolutions at lines 344-347.
7. The Quito local-gravity example at lines 367-370.
8. Dynamic-viscosity values for water, engine oil, and honey at lines 444-448.
9. The viscosity temperature sensitivity claim at lines 465-467.
10. Hardness scale descriptions and conversion limits at lines 477-494. Ashby is a reasonable materials text, but standards would be better for scale definitions.
11. Surface roughness values and the sampling-length/cutoff standard at lines 503-523. Replace ISO 4287 with current ISO 21920 references unless the book deliberately teaches the older standard for historical reasons.
12. COSTAR servicing details at lines 752-760. This can cite NASA mission records or stay under the Hubble report if the report covers the correction.

The citation-policy tier issue is clear: standards claims should use `std:` entries rather than textbooks alone. Accident claims do use the primary investigation report. Materials-property claims can use Ashby, but ceramic-density and viscosity-property claims need a handbook or standards source.

## F. Reader-Path Tagging

The main path tags are defensible. Length, area-volume-density, mass, cross-checking, failure, and project should be core for Volume I. Specialized quantities as standard is correct because the chapter only asks recognition, not mastery.

Two local changes would improve the path discipline. The mass spectrometer subsection should stay standard inside the mass section or be marked as a short standard aside; it is not core household measurement. The contact-based dimensional reconstruction method in the project should be marked mastery or explicitly optional enrichment. A reader on the core path should not need a closed-mesh divergence-theorem computation before Volume II.

No mastery boxes are present. That is acceptable. The chapter does not need a mastery box around Hubble or the compatibility ratio. If a mastery box is added, the right target is the polyhedral-mesh volume formula or a Monte Carlo compatibility simulation.

## G. Specific Concrete Fixes

1. `volumes/01-quantity/ch07-length-area-volume-mass/chapter.tex:20-27`

Current text: "Length, area, volume, and mass are the four quantities an engineer cannot leave unmeasured. The instruments that read them range from a thumb on a workbench to a fountain clock interferometer, and the arithmetic that ties them together follows the algebraic uncertainty rules of chapter 4. We walk the four quantities, name their working instruments, fold in viscosity, hardness, and surface roughness as extended cases, and close on the fact that disagreement among independent methods is the only honest detector of a wrong ruler."

Proposed replacement: "Length, area, volume, and mass are the first quantities an engineer writes down about a physical object. The instruments that read them range from a steel rule on a bench to a laser interferometer tied to an optical frequency standard. Their arithmetic follows the uncertainty rules of chapter 4, and their discipline is independent checking: when two methods disagree outside their combined uncertainty, the measurement process has found a wrong ruler."

2. `chapter.tex:31-35`

Current text: "Length is the quantity engineering measures most often and at the widest dynamic range. A working engineer reads length over a span from the diameter of a transistor channel, near $10^{-9} \,\si{\meter}$, to the orbital radius of a geostationary satellite, near $4 \times 10^{7} \,\si{\meter}$."

Proposed replacement: "Length is one of engineering's most common measurements, and its practical range is unusually wide. A working engineer may meet lengths from features in advanced integrated circuits, at a few nanometres, to the orbital radius of a geostationary satellite, about $4.2 \times 10^{7} \,\si{\meter}$ from Earth's centre."

3. `chapter.tex:39-47`

Current text: "The geometric quantities span more decades than any other base quantity in everyday engineering. A reader who carries an internal ruler from $10^{-10} \,\si{\meter}$ (atomic spacing) to $10^{7} \,\si{\meter}$ (continental distance) has built sixteen decades of internal calibration."

Proposed replacement: "Geometric quantities span enough decades that the reader needs an internal ruler. A reader who carries a scale from $10^{-10} \,\si{\meter}$ (atomic spacing) to $10^{7} \,\si{\meter}$ (continental distance) has built seventeen decades of internal calibration."

4. `chapter.tex:57-63`

Current text: "Resolution at the millimetre, working range from a few centimetres to several metres. Calibration against a gauge block or an SI metre bar is the standard quality-control step."

Proposed replacement: "Resolution at the millimetre, working range from a few centimetres to several metres. Verification against a traceable length standard at a stated reference temperature is the standard quality-control step; tape measures also need controlled tension and support."

5. `chapter.tex:64-69`

Current text: "Resolution at $0.1 \,\si{\milli\meter}$ on a low-cost analog instrument and $0.01 \,\si{\milli\meter}$ on a digital one, working range to $200 \,\si{\milli\meter}$ on a benchtop unit."

Proposed replacement: "Display resolution commonly ranges from $0.02$ to $0.05 \,\si{\milli\meter}$ on a Vernier instrument and $0.01 \,\si{\milli\meter}$ on a digital one, with working range often $150$ to $200 \,\si{\milli\meter}$ on a bench unit. Accuracy is worse than display resolution and must be taken from the instrument specification."

6. `chapter.tex:82-90`

Current text: "Working range up to a metre on a benchtop CMM and several metres on a large industrial unit; uncertainty depending on the machine class, often quoted as a length-dependent budget of the form $A + B L$ with $L$ the measured length."

Proposed replacement: "Working range runs from benchtop machines below a metre to large industrial machines of several metres. The uncertainty is machine-class and environment dependent, commonly specified as a length-dependent maximum permissible error such as $A + B L$, with the units of $A$, $B$, and $L$ stated by the relevant CMM specification."

7. `chapter.tex:91-96`

Current text: "Hand-held units cover a few decimetres to a hundred metres at centimetre resolution; surveying total stations cover kilometres at millimetre resolution under good conditions."

Proposed replacement: "Hand-held units cover a few decimetres to roughly a hundred metres, with accuracy set by the instrument class and target. Surveying total stations can work over kilometre distances, but their specifications are usually given as millimetres plus parts per million under stated atmospheric and target conditions."

8. `chapter.tex:97-106`

Current text: "Frequency-stabilised laser interferometry is the working primary metre realisation for a national metrology institute. Sub-micrometre accuracy at the working laboratory scale is achievable; fractional length uncertainties at the laboratory bench level near $10^{-7}$ to $10^{-8}$ are routine for a calibrated instrument."

Proposed replacement: "Frequency-stabilised laser interferometry is one route by which national metrology institutes realise length from the SI definition of the metre \cite{std:bipm-si2019}. In ordinary laboratory use, the uncertainty is usually dominated by alignment, air refractive index, temperature, and the mechanical setup, rather than by the optical frequency itself."

9. `chapter.tex:122-132`

Current text: "The discipline is to record the workpiece temperature, the instrument temperature, the calibration reference temperature, and either correct to a standard reference temperature (commonly $20 \,\si{\degreeCelsius}$) or report the measurement at its actual temperature with the correction stated."

Proposed replacement: "The discipline is to record the workpiece temperature, the instrument temperature, and the calibration reference temperature. For dimensional specifications, correct to the standard reference temperature of $20 \,\si{\degreeCelsius}$ where the specification requires it, or report the measurement at its actual temperature with the correction stated \cite{std:iso-1-2022}."

10. `chapter.tex:245-251`

Current text: "A density measurement is no more precise than the less precise of its two inputs, in relative terms. The mass measurement is usually the cheaper input to refine: a kitchen scale can give a relative uncertainty near $10^{-3}$ on a hundred-gram sample, while a graduated cylinder on a household object often gives $10^{-2}$ relative volume uncertainty."

Proposed replacement: "The larger relative uncertainty usually dominates the density uncertainty; when the two inputs are comparable, both contributions must be carried in quadrature. The mass measurement is often the cheaper input to refine: a $0.1 \,\si{\gram}$ scale gives a relative display step near $10^{-3}$ on a hundred-gram sample, while a $1 \,\si{\gram}$ kitchen scale is nearer $10^{-2}$."

11. `chapter.tex:261-266`

Current text: "A reader looks around and chooses a household object with a known material. We pick a thick ceramic dinner plate. The material is glazed stoneware, with published density typically near $2300 \,\si{\kilogram\per\meter\cubed}$ for stoneware and somewhat higher for porcelain, $2500$ to $2600 \,\si{\kilogram\per\meter\cubed}$."

Proposed replacement: "A reader looks around and chooses a household object with a known material. We pick a thick ceramic dinner plate. Published engineering data put many dense ceramic bodies in the range of roughly $2200$ to $2600 \,\si{\kilogram\per\meter\cubed}$, with the exact value depending on clay body, porosity, and firing process \cite{text:ashby2017}."

12. `chapter.tex:279-287`

Current text: "A direct measurement of the same plate using a kitchen scale and water displacement, performed by the reader before this paragraph was written, gave $830 \,\si{\gram}$ and $370 \,\si{\milli\liter}$ displacement, density $2240 \,\si{\kilogram\per\meter\cubed}$. The estimate landed within $5\,\%$ of the measurement, which is closer than the factor-of-three target the estimation discipline asks for."

Proposed replacement: "As a worked comparison, take a measured plate with mass $830 \,\si{\gram}$ and displaced volume $370 \,\si{\milli\liter}$. The resulting density is $2240 \,\si{\kilogram\per\meter\cubed}$. The estimate, $2200 \,\si{\kilogram\per\meter\cubed}$, is within about $2\,\%$ of that measurement, much closer than the factor-of-three target the estimation discipline asks for."

13. `chapter.tex:310-314`

Current text: "Mass is the second quantity in the SI base set whose realisation changed in the 2019 redefinition. Chapter 3 of this volume covered the realisation chain; this section covers the working instruments the reader meets between the kilogram's primary realisation and the kitchen."

Proposed replacement: "The kilogram's definition changed in the 2019 SI redefinition, when the Planck constant was assigned an exact numerical value \cite{std:bipm-si2019}. Chapter 3 covered the realisation chain; this section covers the working instruments the reader meets between primary mass realisation and the kitchen."

14. `chapter.tex:351-359`

Current text: "A balance reports mass, not weight. Weight is the gravitational force on the mass at the local gravitational acceleration $g$. The distinction matters: a balance calibrated at one latitude with a local $g$ value reads correctly at the same site only as long as $g$ has not changed. A balance moved to a different latitude or altitude shows a different indication for the same mass unless it is recalibrated."

Proposed replacement: "A classical equal-arm balance compares mass against mass. Local gravitational acceleration cancels to first order because both pans sit in the same gravitational field. A force-restoration electronic balance instead measures the force needed to restore equilibrium and reports mass after calibration. That instrument must be calibrated for its site, because a move to a different latitude or altitude changes the relation between mass and weight."

15. `chapter.tex:363-370`

Current text: "A bathroom scale, a postal scale, a kitchen scale, and a truck scale all read the gravitational force on the load and report a value calibrated to mass. The reading is correct only at the gravitational acceleration the scale was calibrated for. A bathroom scale manufactured for the European market and shipped to a customer in Quito, where local $g$ is about $0.5\,\%$ smaller than the design value, reads about $0.5\,\%$ low."

Proposed replacement: "A bathroom scale, a postal scale, a kitchen scale, and a truck scale usually read the gravitational force on the load and report a mass-equivalent value. The reading is tied to the gravitational acceleration assumed during calibration. If a force scale calibrated in northern Europe is used near the equator at high altitude, the local value of $g$ can differ by several tenths of a percent; without recalibration, the indicated mass shifts by the same fraction."

16. `chapter.tex:390-398`

Current text: "Mass spectrometry is not a household instrument. A reader meets it in chemistry, biochemistry, materials analysis, and nuclear science; the masses it reports are atomic or molecular and the instrument calibration is itself a research-grade procedure. We name it here so that the reader knows the instrument exists and what its working principle is, and so that the catalogue of mass instruments spans the dynamic range from the gigatonne (a fully laden bulk carrier) to the dalton (a single proton)."

Proposed replacement: "Mass spectrometry belongs to chemistry, biochemistry, materials analysis, and nuclear science. It reports mass-to-charge ratio for atomic and molecular ions, and its calibration is a specialist procedure. It belongs in the catalogue because mass work ranges from ship-scale weighbridges, on the order of $10^{8}$ to $10^{9} \,\si{\kilogram}$ for the largest loaded vessels, to atomic-scale measurements in daltons."

17. `chapter.tex:404-413`

Current text: "Air is not weightless. A sample in air loses weight by the mass of the displaced air, which is non-negligible for samples of low density."

Proposed replacement: "Air has density. A sample in air loses apparent weight by the weight of the air it displaces, and the apparent mass correction becomes significant for low-density samples or high-precision weighing."

18. `chapter.tex:444-448`

Current text: "Water at $20 \,\si{\degreeCelsius}$ has dynamic viscosity near $1 \,\si{\milli\pascal\second}$; engine oil ranges from $50$ to $500 \,\si{\milli\pascal\second}$ depending on temperature and grade; honey near $5000 \,\si{\milli\pascal\second}$."

Proposed replacement: "Water at $20 \,\si{\degreeCelsius}$ has dynamic viscosity near $1 \,\si{\milli\pascal\second}$. Lubricating oils and honey occupy much higher, strongly temperature-dependent ranges, so any quoted value must carry temperature, grade, and source."

19. `chapter.tex:465-469`

Current text: "Viscosity changes by a factor of two for every $20 \,\si{\degreeCelsius}$ for many liquids; a measurement at an unrecorded temperature is uncalibrated."

Proposed replacement: "Viscosity is strongly temperature-dependent; for many liquids, a modest temperature change moves the reading by engineering-significant amounts. A viscosity measurement at an unrecorded temperature is incomplete."

20. `chapter.tex:488-494`

Current text: "The recurring failure mode is the conversion. A reader who reads a \"hardness of 50\" without the scale qualifier (HRC, HV, HB) cannot interpret the number. The scale's conversion to other scales is material-dependent and approximate; a published correlation table exists for steels but is not universal."

Proposed replacement: "The recurring failure mode is conversion. A reader who reads a \"hardness of 50\" without the scale qualifier, such as HRC, HV, or HB, cannot interpret the number. Converting among hardness scales is material-dependent and approximate; use a standard or a material-specific correlation table, and report the source with the converted value."

21. `chapter.tex:503-505`

Current text: "Machined steel surfaces typically reach $R_{a}$ between $0.1$ and $10 \,\si{\micro\meter}$; polished optical surfaces reach $R_{a}$ near $1 \,\si{\nano\meter}$."

Proposed replacement: "Machined and polished surfaces span orders of magnitude in $R_{a}$, from micrometre-scale roughness for many machined finishes to nanometre-scale roughness for high-quality optical polishing. Quote a process-specific value only with the measurement method and source."

22. `chapter.tex:515-523`

Current text: "The recurring failure mode is sampling length and cutoff filter. A profilometer reading is sensitive to the length over which the profile is sampled and to the spatial-frequency cutoff applied to separate roughness from waviness and form. Two laboratories measuring \"the same surface\" can report different $R_{a}$ values if their sampling lengths and cutoff filters differ. The discipline is to specify the sampling length, the cutoff, and the filter type alongside the roughness value, in accordance with the relevant ISO 4287 conventions."

Proposed replacement: "The recurring failure mode is sampling length and filtering. A profilometer reading is sensitive to the length over which the profile is sampled and to the spatial-frequency filter used to separate roughness from waviness and form. Two laboratories measuring \"the same surface\" can report different $R_{a}$ values if their evaluation lengths and filters differ. The discipline is to specify the evaluation length, cutoff or nesting index, filter type, and governing standard alongside the roughness value \cite{std:iso-21920-2-2021}."

23. `chapter.tex:528-541`

Current text: "The chapter's central pedagogical move is here. A single measurement reports a value with an uncertainty derived from chapter 4's algebraic rules. A second, independent measurement of the same quantity reports another value with another uncertainty. If the two agree within their combined uncertainty, the engineer's confidence in the quantity grows. If they disagree by more than the combined uncertainty, a previously uncharacterised error source is present in at least one of the methods. Cross-checking is the only honest detector of a wrong ruler."

Proposed replacement: "The practical test is independent measurement of the same quantity. A single measurement reports a value with an uncertainty derived from chapter 4's algebraic rules. A second, independent measurement reports another value with another uncertainty. If the two agree within their combined uncertainty, confidence in the quantity grows. If they disagree by more than the combined uncertainty, at least one method has an uncharacterised error source. Cross-checking is the most direct wrong-ruler detector available inside a local measurement task."

24. `chapter.tex:571-574`

Current text: "A value of $r$ near $1$ or below means the two measurements agree within their combined standard uncertainty. A value of $r$ near $2$ or higher means the two methods disagree at the level of confidence their reported uncertainties would justify."

Proposed replacement: "A value of $r$ near $1$ or below means the two measurements agree within their combined standard uncertainty. A value near $2$ is a warning threshold: the methods disagree by about twice their combined standard uncertainty, so the application must decide whether to investigate, widen the uncertainty budget, or repeat the measurement."

25. `chapter.tex:629-636`

Current text: "Two candidates: the geometric model is too smooth (the stone has ridges and concavities the ellipsoid does not capture), or the displacement reading included air bubbles trapped on the stone's surface."

Proposed replacement: "Two candidates are immediate. The geometric model may be too smooth, because the stone has ridges and concavities the ellipsoid does not capture. The displacement reading may also be biased high if air bubbles clung to the stone's surface."

26. `chapter.tex:696-698`

Current text: "the mirror's outer edge was about $2 \,\si{\micro\meter}$ too flat, an error large enough to ruin diffraction-limited imaging across the optical bandpass \cite{acc:nasa-hubble-optical-systems-1990}."

Proposed replacement: "the mirror's figure error corresponded to severe spherical aberration, described by the investigation report as a $0.4$-wave rms wavefront error at $632.8 \,\si{\nano\meter}$; in the local short form, the outer edge was about $2 \,\si{\micro\meter}$ too flat \cite{acc:nasa-hubble-optical-systems-1990}."

27. `chapter.tex:748-750`

Current text: "A reader who treats a precise instrument as authoritative without independent verification is reading from Hubble's playbook."

Proposed replacement: "A reader who treats a precise instrument as authoritative without independent verification repeats the Hubble failure mode."

28. `chapter.tex:795-803`

Current text: "Hazard class: none. Tools. A kitchen scale or postal scale, resolution $\sim 1 \,\si{\gram}$. A ruler or tape measure, resolution $\sim 1 \,\si{\milli\meter}$. A beaker, measuring cup, or graduated cylinder for water displacement. Tap water. A smartphone camera (optional, for image-based reconstruction). Paper and pencil for the geometric approximation."

Proposed replacement: "Hazard class: none, provided the reader chooses an expendable object, uses stable glassware or plasticware, and keeps water away from electrical devices. Tools. A kitchen scale or postal scale, resolution about $1 \,\si{\gram}$. A ruler or tape measure, resolution about $1 \,\si{\milli\meter}$. A beaker, measuring cup, or graduated cylinder for water displacement. Tap water. A smartphone camera, optional for image-based reconstruction. Paper and pencil for the geometric approximation."

29. `chapter.tex:846-856`

Current text: "Compute the standard uncertainty by repeating the reconstruction with a small perturbation to the scale reference and to the mesh resolution setting; the spread in the resulting volumes is the finite-difference standard uncertainty for the method."

Proposed replacement: "Estimate the method uncertainty by repeating the reconstruction at least three times: once with the nominal scale reference, once with the scale reference shifted by its estimated uncertainty, and once with a different mesh-resolution setting. Report the spread as a sensitivity check, and state plainly that this is a method repeatability estimate rather than a traceable photogrammetry uncertainty."

30. `chapter.tex:857-864`

Current text: "Contact-based dimensional reconstruction. Sample the object's surface at a regular grid of points using a calliper or ruler. For at least twenty surface points, record each point's coordinates relative to a chosen reference frame on the object. Construct a polyhedral mesh from the points and compute its volume by the divergence-theorem formula for a closed mesh. Repeat the sampling and reconstruction; the spread is the standard uncertainty."

Proposed replacement: "Contact-based dimensional reconstruction. Mastery option. Sample the object's surface at a regular grid of points using a calliper or ruler. Record enough cross-sections to approximate the object as stacked slices, compute the area of each slice, and estimate volume by summing slice area times slice spacing. Repeat the sampling; the spread is a repeatability estimate. A closed-mesh divergence-theorem calculation belongs in Volume II or in a mastery note."

31. `chapter.tex:917-923`

Current text: "The exercises move from numerical calculation through derivation, estimation, design, diagnosis, failure analysis, and judgment. Closed problems have full solutions; open-ended problems have rubrics or reference write-ups. Exercises are tagged with their reader-path tier."

Proposed replacement: "The exercises test numerical calculation, derivation, estimation, design, diagnosis, failure analysis, and judgment. Closed problems need full solutions before release; open-ended problems need rubrics or reference write-ups. Exercises are tagged with their reader-path tier."

32. `chapter.tex:1016-1056`

Current text: the estimation subsection has five exercises and no simulation exercise in the whole exercise set.

Proposed replacement: Add the following exercise after line 1048 and keep the total target at 28 by merging or removing the roughness citation exercise:
"A triaxial ellipsoid has semi-axes $a = 2.6 \,\si{\centi\meter}$, $b = 2.0 \,\si{\centi\meter}$, and $c = 1.8 \,\si{\centi\meter}$, each with standard uncertainty $0.1 \,\si{\centi\meter}$. Run or outline a Monte Carlo simulation with at least $10\,000$ draws to estimate the distribution of $V = \tfrac{4}{3}\pi abc$. Compare the simulated standard deviation with the product-of-powers result."

33. `chapter.tex:1026-1030`

Current text: "Estimate the surface area of an adult human body, in square metres. State your method and the factor-of-three confidence range. Compare your estimate to the published Du Bois formula or another cited clinical estimate of body-surface area."

Proposed replacement: "Estimate the surface area of an adult human body, in square metres, using a body-as-cylinders or body-as-boxes model. State your method and factor-of-three confidence range. Then compare your estimate to a cited clinical body-surface-area formula supplied in the solution notes."

34. `chapter.tex:1033-1039`

Current text: "Estimate the mass of a fully laden semi-trailer truck on a European motorway, given that EU regulations limit the gross combination weight to specified maximum values. State the regulatory limit you assume and the year of the regulation; estimate the typical loaded fraction; report the result with a factor-of-three confidence range."

Proposed replacement: "Estimate the mass of a fully laden road freight vehicle. Use a stated legal gross combination mass supplied in the problem or solution notes, then estimate the typical loaded fraction and report the result with a factor-of-three confidence range."

35. `bibliography/references.bib:113-119`

Current text: the standards block contains `std:jcgm-vim` but no ISO 1 or ISO 21920 entry.

Proposed replacement: Add standards entries for `std:iso-1-2022` and `std:iso-21920-2-2021`, using ISO as the organization, titles matching the ISO pages, and years 2022 and 2021 respectively. The chapter should cite those entries at the temperature-reference and roughness-standard claims.

## H. Structural Risks For The Larger Project

1. The dossier schema does not force a source plan for standards-heavy chapters. Chapter 7 is a metrology chapter, yet most instrument specifications and standards references are absent from the dossier and prose. Add a dossier field for "standards required" and require each instrument class to name either a standard, a calibration guide, or a representative specification source before drafting.

2. The exercise architecture promises solutions and rubrics without a companion artifact. The prose states that closed problems have full solutions, but no solution file exists for this chapter. Before another chapter is reviewed, decide whether solutions live beside each chapter, in a separate instructor volume, or in an online repository, then make the release checklist fail when the promised artifact is missing.

3. The project protocol needs a prerequisite and path check. Q55 correctly assigns the Chapter 7 project as household plus analysis, but the chapter adds a divergence-theorem mesh method that exceeds the declared prerequisites. Add a project-review gate that checks tools, mathematical prerequisites, hazard class, expected time, and reader-path tier against the volume opener before the chapter reaches review.
