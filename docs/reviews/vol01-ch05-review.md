# Volume 1 Chapter 5 review: Sensors and instruments

Resolved: 2026-04-29.

The 38 fixes in section G have been applied. The two release-blocking
errors are closed.

The voltage-divider orientation contradiction (G17, G28, G32) is
fixed. The chapter now consistently states the configuration as: the
fixed reference resistor is the upper leg (from $V_{\text{cc}}$ to
the ADC node) and the thermistor is the lower leg (from the ADC node
to ground), giving $V_{\text{out}} = V_{\text{cc}} R_{\text{th}} /
(R_{\text{ref}} + R_{\text{th}})$. The estimation block, the project
procedure, and the calculation exercise (formerly G32) all reflect
this same orientation. The chapter no longer asks the reader to wire
the circuit one way and compute it another.

The reader-path tagging on the estimation block is fixed. §5.4
"Choosing the right sensor" is now `\pathtag{core}` rather than
`\pathtag{standard}`, so the chapter's only formal `\begin
{estimation}` block sits on the core path. A core reader can no
longer skip the estimation block by following only `\pathtag{core}`
sections.

Technical corrections: the strain-gauge framing now correctly says
the immediate measured quantity is strain (not stress); LVDTs moved
from under the capacitance bullet to the mechanical/inductive
section per the suggestion in G7; PMT comparison rewritten without
the "slower than solid-state" overstatement; SQUIDs no longer claimed
as "the highest-sensitivity" without naming the cryogenic and
shielding burden; the manufacturer accuracy specification paragraph
no longer asserts a coverage interval as the default reading;
recalibration interval claim no longer derives a specific calendar
interval from the drift specification alone; Steinhart-Hart equation
now uses $\ln(R/R_{\ast})$ with a reference resistance, with an
explanatory paragraph on the dimensional convention; project hazard
statement extended with explicit waterproof-probe / dry-electronics /
no-near-boiling-water language; project temperature range narrowed
from $0$--$100$ to $0$--$80 \,\si{\degreeCelsius}$ to match the
settled low-hazard brief and the new water-temperature limit.

Citations: the paragraph on common-mode failure now cites
`gen:perrow1984` (Normal Accidents) for the chronic-class claim and
`text:leveson2011` for the redundancy-needs-analysis claim; the
Steinhart-Hart paragraph cites `text:fraden2016`; ITS-90 references
cite `web:bipm-cct-its90`; the calibration-function paragraph cites
`std:jcgm-vim`; the sensor families intro cites `text:fraden2016`.
The Air France 447 paragraph (G25) is rewritten to follow the
registry short-form more tightly, removing the absolute "all three
simultaneously" claim and replacing it with the BEA's "temporary
inconsistency between measured airspeeds, likely following
obstruction of the pitot probes by ice crystals at high altitude"
language. The Ariane 5 Flight 501 reference (G26) now cites
`acc:ariane501-ifr`.

Voice rewrites (B1--B13): self-announcing topic sentences in the
opening, the §5.2 introduction, the §5.4 introduction, the §5.5
introduction, and the failure section's opening have been rewritten;
banned filler ("Robust") removed from thermocouple and LVDT
descriptions; banned negate-first-then-pivot construction removed
from piezoelectric, range-vs-burst-pressure, sensor-failure, and
common-mode-failure paragraphs; meta-explanation tails about
chapter structure and future-volume references rewritten; the
exercise preface no longer leaks "internal architecture."

Chapmeta named-cases list updated (G38): Hubble removed (it was
listed but not discussed in prose); Ariane 5 Flight 501 added (it
is now cited in the chronic-class list with `\cite{acc:ariane501-ifr}`).

Project procedure updates (G29, G30, G31): water-bath instructions
include the waterproof probe, settling time, and a temperature limit
of $60 \,\si{\degreeCelsius}$ rather than "near boiling"; uncertainty
budget rewritten to remove the post-calibration thermistor-tolerance
double-count; verification step asks for the difference's
uncertainty (including the reference thermometer) and a stated
coverage factor.

Exercise corrections: voltage-divider exercise (G32) reflects the
corrected orientation and asks for fractional sensitivity; the
derivation exercise (G33) is reframed as a small-signal expansion
around the symmetric operating point, derived algebraically rather
than via partial derivatives, with an explicit forward reference to
Volume II for the general case (this preserves Q2 alignment); the
smartphone gyroscope estimation (G34) now asks for accumulated
orientation uncertainty over a $60 \,\si{\second}$ measurement
rather than an unspecified angular resolution; the Steinhart-Hart
fitting exercise (G35) supplies the part number and synthetic data
explicitly; the clinical-thermometer design exercise (G36) uses
expanded-uncertainty language consistent with the GUM. The total
remains $30$ exercises, matching the chapmeta target and verified
mechanically by `make exercise-counts`.

Volume I opener (G37) is updated to reconcile the archetype
inventory with what Vol I actually introduces. The opener now lists
six archetypes (scaling, balance, failure, uncertainty, interface,
transport) as Vol I's first formal introductions, and the four
remaining (stability, optimisation, control, ethics) as
later-volume material. This closes the architecture drift Codex
flagged in section H risk 1.

The build is clean: `make strict` produces a 594-page `main.pdf`;
`make check`, `make audit-docs`, `make accidents`, and `make
exercise-counts` all PASS; `grep` finds no em-dashes in the chapter
source.

The structural risks named in section H are partly closed: H1
(archetype ledger drift) is closed at the Volume I opener level; H2
(named-case tooling fuzzy matching for prose variants and
chapmeta-named cases) remains open as a Phase 0.7 task; H3
(citation-policy lane for datasheet and commercial-specification
references) remains open as a Phase 0.7 task and is partly mitigated
by the chapter now refusing to pin specific DMM and oscilloscope
performance numbers in the permanent text.

Draft review returned 2026-04-29.

Build-facing note: no obvious chapter-specific build breaker was found. `make check` passes across 174 chapter shells, `make accidents` passes, `make exercise-counts` passes for the five prose chapters, and `make strict` reports `main.pdf` up to date. This was not a forced clean rebuild. The chapter has no `\cref`, `\autoref`, or `\ref` commands beyond its own `\label{vol01:ch05}`.

Sources checked for this review include the local dossier, the Volume I dossier, the Volume I opener, the cited BibLaTeX entries `std:jcgm-vim`, `text:fraden2016`, and `acc:bea-af447`, the Air France 447 registry entry, the Hubble primary mirror registry entry, the Ariane 5 Flight 501 registry entry, and the BEA Air France 447 investigation page and final report. External source links checked: `https://bea.aero/en/investigation-reports/notified-events/detail/accident-to-the-airbus-a330-203-registered-f-gzcp-and-operated-by-air-france-occured-on-06-01-2009-in-the-atlantic-ocean/` and `https://bea.aero/fileadmin/documents/docspa/2009/f-cp090601.en/pdf/f-cp090601.en.pdf`.

## A. Verdicts

Technical: blocked. Blockers: the thermistor voltage-divider text contradicts itself about which element is upper versus lower, so the equation, project, and exercises cannot all be correct; the chapter also makes many instrument-performance claims without source-tier support.

Pedagogical: blocked. Blockers: the required project inherits the voltage-divider contradiction and adds unsafe or underspecified water-immersion instructions; the required estimation block sits inside a `standard` path section, so a `core` reader can miss it.

Voice: approved-with-corrections. The chapter is mostly usable, but several sentences are self-announcing, use banned filler such as "Robust," or use the negate-first-then-pivot construction.

## B. Voice review

We walk the chapter in order. The voice problem is not density. It is placement: the weak sentences appear in the opening, in catalogue entries, and in the failure section where the prose should sound most like worked judgment.

1. Lines 23-33: "This chapter takes up the sensor as an engineering object. We catalogue the physical principles by which sensors translate the world, name the specifications by which they are compared, describe the procedure by which the right sensor is chosen, survey the working instruments that wrap sensors into usable form, and close with the recurring failure mode in which multiple nominally independent sensors fail together because they share a single environmental cause."

Rule: `docs/voice.md`, self-announcing topic sentences. This is a table of contents written as prose.

Rewrite: "A sensor is an engineering object: a physical interface, a calibration function, a transport chain, and a failure source. We judge it by the physical principle that produces the signal, the specifications that bound the signal, the instrument that carries it, and the shared causes that can make redundant sensors fail together."

2. Lines 95-99: "The physical principles by which sensors translate quantities into signals fall into a small number of families. We sketch six. A modern sensor handbook \cite{text:fraden2016} gives a more exhaustive catalogue; the families below cover the bulk of the sensors a working engineer in any domain encounters."

Rule: `docs/voice.md`, self-announcing topic sentence. "We sketch six" announces the classroom move instead of making it.

Rewrite: "Most working sensors translate quantities through six physical families: thermal, electrical, optical, mechanical, chemical, and magnetic. Fraden's handbook \cite{text:fraden2016} gives the longer catalogue; this chapter keeps the families a working engineer must recognise before reading a datasheet."

3. Lines 107-114: "Working range from cryogenic to about $1700 \,\si{\degreeCelsius}$ depending on type (J, K, T, R, S, B); voltages in the millivolt range; characteristic sensitivity around $40 \,\si{\micro\volt \per\kelvin}$ for type K. Robust, wide-range, but need a reference junction and amplification."

Rule: `docs/voice.md`, AI-tic vocabulary and engineering-flavoured filler. "Robust" is banned when it stands in for a specific property.

Rewrite: "Common thermocouple types cover cryogenic service through high-temperature furnace service, with the upper range near $1700 \,\si{\degreeCelsius}$ for noble-metal types. Type K sensitivity near room temperature is about $40 \,\si{\micro\volt\per\kelvin}$. Thermocouples tolerate heat and mechanical abuse better than most contact temperature sensors, but they require reference-junction compensation and low-noise amplification."

4. Lines 134-136: "The reader's project in this chapter uses an NTC thermistor; we will return to the Steinhart-Hart relationship in section 5.4 and again in the project description."

Rule: `docs/voice.md`, meta-explanation tail. The sentence tells us where the syllabus goes.

Rewrite: "The chapter project uses an NTC thermistor, so the Steinhart-Hart and beta-parameter models will carry the calibration work."

5. Lines 210-211: "Cannot measure static loads (the charge leaks away), but excellent for dynamic measurements."

Rule: `docs/voice.md`, negate-first-then-pivot construction. It also uses "excellent" as praise where a mechanism would be stronger.

Rewrite: "Piezoelectric readouts have a finite leakage time constant, so they measure dynamic force, pressure, acceleration, and ultrasound most cleanly."

6. Lines 212-215: "LVDTs (linear variable differential transformers) produce an AC voltage proportional to the displacement of a ferromagnetic core within a coil assembly. Robust, contactless, linear over their working range."

Rule: `docs/voice.md`, AI-tic vocabulary. "Robust" is doing no engineering work.

Rewrite: "LVDTs (linear variable differential transformers) produce an AC voltage proportional to the displacement of a ferromagnetic core within a coil assembly. With no sliding electrical contact at the moving core, they tolerate dirty industrial displacement measurements and stay linear over their specified range."

7. Lines 326-331: "A pressure transducer rated for $0$ to $10 \,\si{\bar}$ may be safe to operate to $20 \,\si{\bar}$ ("burst pressure"), but the readings between $10$ and $20 \,\si{\bar}$ are outside specification. A transducer exposed to inputs above the range (and below the burst pressure) may not be damaged but is not making a calibrated measurement."

Rule: `docs/voice.md`, negate-first-then-pivot construction. The second sentence also repeats the first.

Rewrite: "A pressure transducer rated for $0$ to $10 \,\si{\bar}$ may survive a higher proof or burst pressure, but readings above $10 \,\si{\bar}$ are outside the calibrated range. Survival is a mechanical claim; calibration is a measurement claim."

8. Lines 400-402: "The procedure for choosing a sensor for an engineering application is a standard sequence. We name the steps; the underlying judgment is what experience develops."

Rule: `docs/voice.md`, self-announcing topic sentence. "We name the steps" is process narration.

Rewrite: "Sensor selection starts as a checklist and becomes judgment with use. The checklist matters because it forces the measurand, environment, interface, cost, and calibration record into the same decision."

9. Lines 522-527: "A sensor produces a signal; an instrument turns the signal into a useful indication. We sketch six instruments the reader will meet constantly. A reader without specific exposure should treat this section as a working vocabulary; depth in any given instrument is in Volume VIII chapter 11 (Sensors and actuators) and in the domain-specific volumes."

Rule: `docs/voice.md`, self-announcing topic sentence and bad pedagogical signposting.

Rewrite: "A sensor produces a signal; an instrument turns the signal into an indication a working engineer can read, record, calibrate, and challenge. Six instruments form the minimum vocabulary here: the digital multimeter, oscilloscope, micrometer, scale, microscope, and sensor array."

10. Lines 632-633: "Sensor arrays will recur in Volume VII (information) and Volume IX (systems); for now, the reader should know that the section's single-sensor framing generalises."

Rule: `docs/voice.md`, meta-explanation tail. The sentence announces future recurrence instead of stating the generalisation.

Rewrite: "The single-sensor model generalises to arrays by adding geometry, timing, correlation, and fusion."

11. Lines 647-651: "A sensor's failure mode is what the engineer should worry about. The recurring pattern is that nominally independent sensors distributed across a system often fail not independently but together, because they share a single environmental cause, a single calibration history, or a single manufacturing batch."

Rule: `docs/voice.md`, negate-first-then-pivot construction. The first sentence also overstates, since the engineer worries about performance, integration, calibration, and failure.

Rewrite: "A sensor's failure mode belongs in the design record. Nominally independent sensors often share one environmental cause, calibration history, firmware version, or manufacturing batch; that shared cause can make the readings fail together."

12. Lines 665-671: "Common-mode failure is not a marginal effect. It is the dominant failure mode in many high-reliability systems precisely because those systems have already eliminated the obvious single-point failures. Independence in design does not guarantee independence in failure; the engineer who relies on redundancy without analysing the common-mode failure modes is relying on a redundancy that does not deliver what it claims."

Rule: `docs/voice.md`, negate-first-then-pivot construction and overstatement. The technical claim also needs a stronger source.

Rewrite: "Common-mode failure can dominate after obvious single-point failures have been removed. Redundancy only buys independence after the shared physical, software, calibration, and environmental causes have been analysed."

13. Lines 848-852: "The exercises train calculation, derivation, estimation, simulation, design, diagnosis, failure analysis, and judgment. Calculation and derivation problems have full solutions; open-ended problems have rubrics or reference write-ups. Exercises are tagged with their reader-path tier."

Rule: `docs/voice.md`, bad pedagogical signposting. This is internal architecture leaking into chapter prose.

Rewrite: "The exercises move from numerical sensor calculations to selection, diagnosis, and failure analysis. Closed problems should have full solutions; design and judgment problems should have rubrics or reference write-ups in the solutions volume."

## C. Technical review

The chapter covers the right territory, but it is not technically releasable. The main failure is not one isolated wrong number. It is that catalogue prose, project prose, and exercises make instrument-performance claims without enough source discipline, then the project depends on a voltage-divider definition that contradicts itself.

The thermistor divider is the largest hard error. Lines 496-498 state

`V_{\text{out}} = V_{\text{in}} R_{\text{th}} / (R_{\text{th}} + R_{\text{ref}})`.

That equation is correct when the output is taken across the thermistor as the lower leg of the divider, or when the thermistor is otherwise the element tied to the reference node. The project procedure at lines 780-784 says the thermistor is the upper element. With the thermistor as the upper element and the reference resistor as the lower element, the output at the midpoint is

`V_{\text{out}} = V_{\text{cc}} R_{\text{ref}}/(R_{\text{th}} + R_{\text{ref}})`.

The same contradiction recurs in the calculation exercise at lines 882-890. A reader who wires the project as written and computes it as written will invert the transfer curve. This blocks both technical and pedagogical approval.

The thermistor numerical estimates are broadly plausible after the divider orientation is fixed. For a $10 \,\si{\kilo\ohm}$ NTC thermistor with $\beta = 3950 \,\si{\kelvin}$ and $R_{0}=10 \,\si{\kilo\ohm}$ at $25 \,\si{\degreeCelsius}$, the beta model gives about $33.6 \,\si{\kilo\ohm}$ at $0 \,\si{\degreeCelsius}$, $3.59 \,\si{\kilo\ohm}$ at $50 \,\si{\degreeCelsius}$, and $0.70 \,\si{\kilo\ohm}$ at $100 \,\si{\degreeCelsius}$. The resistance ratio from $0$ to $100 \,\si{\degreeCelsius}$ is about 48, so the line 463 phrase "about $40$" is acceptable as an order-of-magnitude statement. The ADC estimate is directionally right for a one-degree project, but the line 501 target of $0.1 \,\si{\degreeCelsius}$ is too fine for the casual "10-bit is roughly enough" conclusion across the whole range. With a 3.3 V, 10-bit ADC and the formula as written, one LSB maps to about $0.09 \,\si{\degreeCelsius}$ near $25 \,\si{\degreeCelsius}$, about $0.13 \,\si{\degreeCelsius}$ near $50 \,\si{\degreeCelsius}$, and about $0.56 \,\si{\degreeCelsius}$ near $100 \,\si{\degreeCelsius}$. The text should say 10-bit is adequate for a $1 \,\si{\degreeCelsius}$ project and 12-bit is preferable for sub-degree work.

The Steinhart-Hart equation at lines 467-469 uses `\ln R`. As written, that is the logarithm of a dimensional quantity. Sensor handbooks often use the numerical resistance in ohms by convention, but the chapter has just spent four chapters teaching dimensions-first discipline. This equation should either use `\ln(R/R_{\ast})` with a reference resistance or state that `R` denotes the numerical value of the resistance in ohms and that the fitted coefficients carry the corresponding convention. The beta equation at lines 476-478 is dimensionally sound: $\beta$ has units of kelvin, and $\beta(1/T-1/T_{0})$ is dimensionless.

Several catalogue claims are technically imprecise. Lines 56-60 say a strain gauge output is resistance and the engineer wants stress. The immediate measured mechanical quantity is strain. Stress follows only after a constitutive model, geometry, load path, and temperature compensation. Lines 151-155 place LVDTs in a capacitance-sensor bullet. An LVDT is inductive, not capacitive. Lines 175-178 say photomultiplier tubes are "slower than solid-state." That is wrong as a general claim. PMTs are often used for fast, low-light timing; the comparison depends on detector area, readout, gain, and bandwidth. Lines 274-277 call SQUIDs the highest-sensitivity magnetic sensors but do not state the cryogenic and shielding burden, which is part of the engineering judgment.

The specifications section has a standards issue. Lines 296-303 say a plus-minus accuracy specification "typically means a coverage interval (an expanded uncertainty) under stated conditions." That is not safe. Many datasheets use plus-minus accuracy as a maximum permissible error, limit of error, or manufacturer guarantee under stated conditions, not a metrological coverage interval with a disclosed probability model. The chapter should teach the reader to refuse coverage-factor inference unless the datasheet states the convention. Lines 343-349 also over-compute the recalibration interval from drift. A $0.1\,\%$ per year drift and $1\,\%$ application requirement do not by themselves imply a ten-year interval. Initial calibration uncertainty, drift distribution, guard band, environmental exposure, confidence level, and consequence of error all enter.

The instrument survey contains many numerical figures that are plausible but uncited: thermocouple ranges and sensitivity, RTD range, thermistor range, gauge factors, DMM accuracy, oscilloscope sample rates, micrometer ranges and resolution, balance resolution, microscope resolution, SEM/TEM/AFM resolution, and smartphone sensor lists. Under `docs/citation-policy.md`, empirical performance claims need primary sources or at least appropriate handbook support. `text:fraden2016` can support a general sensor taxonomy, but it is too broad to carry current oscilloscope ranges, DMM performance, smartphone sensor inventory, and commercial lead-time claims. The oscilloscope and smartphone claims are also medium-life or fast-aging and need "current as of YYYY" language if retained.

The Air France 447 paragraph aligns broadly with the BEA final report. The BEA page and final report support the core chain: temporary inconsistency between measured airspeeds likely following pitot obstruction by ice crystals, autopilot disconnection, reconfiguration to alternate law, inappropriate control inputs, failure to diagnose stall, and loss of all 228 people aboard. The paragraph should be less absolute about "all three" pitot probes being obstructed simultaneously unless it quotes the registry language or pins the report section. The BEA result is framed in terms of temporary inconsistency between measured airspeeds likely following obstruction of the pitot probes by ice crystals. The chapter's wording is acceptable for a short-form case if it stays close to the registry and primary report.

The chapter's named-case discipline is incomplete. Hubble is listed in `\chapmeta` as a named case, but the chapter never discusses or cites it. Ariane 5 Flight 501 is named at lines 716-719 without citing `acc:ariane501-ifr`. Air France 447 is cited to the primary BEA report, which is good, but the policy also asks for at least one independent secondary analysis for named accidents. If this chapter uses only the abbreviated registry form, we can tolerate a short case, but the sentence calling AF447 "canonical" needs secondary support or should be cut.

There are no cross-reference failures because the chapter does not use `\cref`, `\autoref`, or `\ref`. Its own label exists. The structural checks pass, but the accident tooling missed a prose mention of Ariane 5 Flight 501 in this chapter, which should be treated as a tooling defect rather than a chapter pass.

## D. Pedagogical review

The chapter promises the habit of treating sensors as interfaces between physical reality and data. That habit is right for Volume I. The best parts are the interface and transport archetype blocks, the sensor selection checklist, the thermistor project, and the common-mode failure section. Those pieces teach the reader to ask where the number came from before trusting it.

The current draft undercuts that habit in three ways.

First, the project is not yet buildable as written. The thermistor-divider orientation error means the physical circuit, formula, simulation, exercise, and fitted curve can disagree. A solitary reader would not know whether the algebra is wrong or the wiring description is wrong. That is exactly the kind of measurement-chain confusion the chapter is supposed to prevent.

Second, the project safety and measurement instructions are too casual. Q55-ch05 settled the hazard class as low, with battery-voltage circuits, no mains-voltage work, warm or cool water, and no soldering required. The chapter adds "optionally near boiling" and tells the reader to immerse the thermistor and reference thermometer in water. It does not say to use a waterproof thermistor probe, to keep the breadboard and microcontroller dry, to avoid bare leads in water, or to keep hot water below scalding temperature. This is not a high-hazard project, but the written procedure should model the same discipline it asks from the reader.

Third, the reader-path tags make the core path leaky. The only formal `\begin{estimation}` block sits inside `\section{Choosing the right sensor}\pathtag{standard}`. Q20 and the reviewer guide require a formal estimation environment in every chapter, and Q51 says core contains the spine. A core-path reader should not be able to skip the only estimation block. Either the section should be promoted to core, or the thermistor case and estimation block should be split into a new core section.

The exercise set has the right count and the right surface spread: 30 exercises, with calculation, derivation, estimation, simulation, design, diagnosis, failure analysis, and judgment. It does less well at making those types distinct. The "Diagnosis and reverse engineering" group is diagnosis only; it gives the plausible mechanisms in parentheses, which removes much of the diagnostic work. The simulation exercise that asks the reader to compare a synthetic beta-model data set to the exact Steinhart-Hart form for a published thermistor part is under-specified unless the chapter names the part and gives a data source. The smartphone gyroscope estimation exercise asks for angular resolution from bias instability and angular random walk without an observation time or filtering rule, so it is not answerable as written.

Difficulty calibration is uneven. The first five calculation exercises are appropriate. The voltage-divider uncertainty derivation is too hard if it really requires correlated partial derivatives through $R_{\text{th}}/(R_{\text{th}}+R_{\text{ref}})$, but the prompt frames it as a simple product-and-ratio rule. That will teach the wrong method unless revised. The project is a good Volume I first hardware task once the wiring, immersion, and uncertainty model are tightened. The reflection questions are strong, especially the comparison between one-degree and tenth-degree temperature measurement.

The estimation block works as a model in sequence but not in placement. It estimates before calculating and points the reader toward precision budget. It needs a corrected ADC-resolution conclusion and a corrected resistor-tolerance sentence. As written, it says "typically $\pm 1\,\%$ for $5\,\%$-tolerance through-hole resistors," which is internally contradictory.

The failure section closes the chapter's main mechanism well. Common-mode sensor failure is exactly the failure mode this chapter should teach. It would be stronger if the AF447 paragraph followed the registry short form more tightly, cited the BEA report for the mechanism, and reserved organisational claims for Volume X unless it adds the secondary source required by policy.

The archetype invocation is useful but architecturally inconsistent. Chapter 3 does introduce interface, and this chapter reasonably develops it. The Volume I opener, however, says interface and transport appear from Volume II onward. The chapter is not the only problem; the volume architecture has drifted. The editor should reconcile the opener, landscape, and dossiers before more Volume I chapters are reviewed.

## E. Citation discipline

The chapter has only three explicit citation keys: `std:jcgm-vim`, `text:fraden2016`, and `acc:bea-af447`. All three exist in `bibliography/references.bib`. That is not enough for the claims the chapter makes.

The epigraph cites VIM and Fraden for a sentence that is not a quotation and reads like an invented working rule. That can stand if treated as a paraphrase, but it should not imply VIM contains that sentence. Better: cite VIM for the definitions of sensor, transducer, indication, and measurand in the first definitional paragraph, not in the epigraph.

The chapter should cite VIM or JCGM terms at the definitions of sensor, transducer, accuracy, precision, resolution, measurand, calibration function, and indication. It currently cites VIM only in the epigraph. That leaves the definitional work unsupported.

The catalogue of sensor types can use `text:fraden2016`, but specific numerical ranges should either cite handbook sections or be softened. The following claims need citations if retained: thermocouple upper range and type K sensitivity; RTD upper range and ITS-90 traceability; thermistor range and beta-parameter values; strain-gauge gauge factors; DMM accuracy ranges; oscilloscope sample-rate and bit-depth ranges; micrometer resolution; analytical-balance and kitchen-scale resolution; microscope, SEM, TEM, and AFM resolution; smartphone sensor inventory. Several of these are empirical performance claims and need primary manufacturer datasheets or standards if the figure is load-bearing.

The AF447 case cites the BEA final report, which is the correct primary source tier. The follow-on claim about "subsequent regulatory action, including pitot replacement and revised unreliable-airspeed training" also needs a citation, either to BEA recommendations and EASA action or to a secondary source if the chapter describes the post-report safety response. The sentence calling AF447 "canonical" needs secondary support or deletion.

The Ariane 5 Flight 501 sentence at lines 716-719 is a named accident claim with no citation. It should cite `acc:ariane501-ifr` or be removed. The Hubble named case in `\chapmeta` should either appear in the prose with `acc:nasa-hubble-optical-systems-1990` or be removed from the named-cases list.

The project uses published Steinhart-Hart coefficients for a chosen part but names no part and gives no example source. Either the project should specify one representative thermistor datasheet for the reference solution, or the simulation track should use a fully supplied synthetic coefficient set and avoid pretending it is a published part.

## F. Reader-path tagging

The top-level section tags are close, but one placement is not defensible.

`What a sensor is` as `core` is correct. The reader needs the interface and transport framing.

`Transducer principles` as `core` is defensible only if the chapter keeps it as a compact recognition catalogue. At its current length, it reads like standard working vocabulary rather than core spine. We would either keep a short core classification and move detailed bullets to standard, or keep the current tag and accept that Volume I core is not minimal.

`Sensor specifications` as `core` is correct. Accuracy, precision, resolution, range, drift, hysteresis, and cross-sensitivity are central to reading a sensor datasheet.

`Choosing the right sensor` as `standard` is the problem. It contains the thermistor case, the only formal estimation block, and the bridge into the project. Promote it to `core` or split the thermistor case into a new core section.

`Common instruments` as `standard` is correct. It is useful vocabulary, not the chapter spine.

`Failure` as `core` is correct. The common-mode failure mechanism closes the chapter's main argument.

`Project` as `core` is correct. The project is the reader's first hardware measurement chain in the volume.

The exercise subsection tags are mostly defensible: calculation, estimation, diagnosis, and failure analysis as core; derivation and design as standard; simulation as mastery. The derivation subsection may contain one exercise that belongs to mastery if the voltage-divider uncertainty prompt is corrected to use partial derivatives and covariance.

## G. Specific concrete fixes

1. File: `volumes/01-quantity/ch05-sensors-and-instruments/chapter.tex`, lines 23-33.

Current text: "This chapter takes up the sensor as an engineering object. We catalogue the physical principles by which sensors translate the world, name the specifications by which they are compared, describe the procedure by which the right sensor is chosen, survey the working instruments that wrap sensors into usable form, and close with the recurring failure mode in which multiple nominally independent sensors fail together because they share a single environmental cause."

Proposed replacement: "A sensor is an engineering object: a physical interface, a calibration function, a transport chain, and a failure source. We judge it by the physical principle that produces the signal, the specifications that bound the signal, the instrument that carries it, and the shared causes that can make redundant sensors fail together."

2. File: `volumes/01-quantity/ch05-sensors-and-instruments/chapter.tex`, lines 56-60.

Current text: "A strain gauge's output is a resistance; the engineer wants a stress."

Proposed replacement: "A strain gauge's output is a resistance change; the engineer first obtains strain, then obtains stress only after applying a material model, geometry, and temperature compensation."

3. File: `volumes/01-quantity/ch05-sensors-and-instruments/chapter.tex`, lines 77-89.

Current text: "The transport archetype recurs throughout the work: it appears in heat and mass transfer (Volume IV), in network packet routing (Volume VII), in supply chains and infrastructure flows (Volume IX, Volume XII)."

Proposed replacement: "The transport archetype recurs throughout the work: it appears in heat and mass transfer (Volume IV and Volume V), in network packet routing (Volume VII), in system flows (Volume IX), and in supply chains and infrastructure flows (Volume XII)."

4. File: `volumes/01-quantity/ch05-sensors-and-instruments/chapter.tex`, lines 95-99.

Current text: "The physical principles by which sensors translate quantities into signals fall into a small number of families. We sketch six. A modern sensor handbook \cite{text:fraden2016} gives a more exhaustive catalogue; the families below cover the bulk of the sensors a working engineer in any domain encounters."

Proposed replacement: "Most working sensors translate quantities through six physical families: thermal, electrical, optical, mechanical, chemical, and magnetic. Fraden's handbook \cite{text:fraden2016} gives the longer catalogue; this chapter keeps the families a working engineer must recognise before reading a datasheet."

5. File: `volumes/01-quantity/ch05-sensors-and-instruments/chapter.tex`, lines 107-114.

Current text: "Working range from cryogenic to about $1700 \,\si{\degreeCelsius}$ depending on type (J, K, T, R, S, B); voltages in the millivolt range; characteristic sensitivity around $40 \,\si{\micro\volt \per\kelvin}$ for type K. Robust, wide-range, but need a reference junction and amplification."

Proposed replacement: "Common thermocouple types cover cryogenic service through high-temperature furnace service, with the upper range near $1700 \,\si{\degreeCelsius}$ for noble-metal types. Type K sensitivity near room temperature is about $40 \,\si{\micro\volt\per\kelvin}$. Thermocouples tolerate heat and mechanical abuse better than most contact temperature sensors, but they require reference-junction compensation and low-noise amplification. Add a handbook or standards citation for the range and sensitivity figures."

6. File: `volumes/01-quantity/ch05-sensors-and-instruments/chapter.tex`, lines 115-119.

Current text: "Highly linear, accurate, traceable to ITS-90 fixed points, but slower than thermocouples and more expensive."

Proposed replacement: "Industrial platinum RTDs are more linear than thermistors over moderate ranges and can be calibrated through procedures tied to ITS-90 realisations; they are usually slower and more expensive than thermocouples in rugged high-temperature service."

7. File: `volumes/01-quantity/ch05-sensors-and-instruments/chapter.tex`, lines 151-155.

Current text: "Capacitance sensors: detect changes in capacitance from displacement, dielectric constant change, proximity, or fluid level. Used in displacement transducers (LVDTs and capacitive variants), capacitive touch sensors, and industrial level gauges."

Proposed replacement: "Capacitance sensors: detect changes in capacitance from displacement, dielectric constant change, proximity, or fluid level. Used in capacitive displacement probes, capacitive touch sensors, and industrial level gauges. LVDTs belong under mechanical or inductive displacement sensing, not under capacitance."

8. File: `volumes/01-quantity/ch05-sensors-and-instruments/chapter.tex`, lines 175-178.

Current text: "Photomultiplier tubes amplify weak optical signals through cascaded electron multiplication. Very high sensitivity, slower than solid-state, used in low-light and spectroscopy applications."

Proposed replacement: "Photomultiplier tubes amplify weak optical signals through cascaded electron multiplication. They provide high gain and fast low-light detection, with size, high-voltage supply, magnetic-field sensitivity, and fragility as the usual trade-offs against solid-state photodetectors."

9. File: `volumes/01-quantity/ch05-sensors-and-instruments/chapter.tex`, lines 206-211.

Current text: "Piezoelectric sensors produce a charge under applied stress. Quartz, lead-zirconate-titanate (PZT), and polyvinylidene fluoride (PVDF) are common materials. Used in accelerometers, force transducers, ultrasound transducers. Cannot measure static loads (the charge leaks away), but excellent for dynamic measurements."

Proposed replacement: "Piezoelectric sensors produce charge under applied stress. Quartz, lead-zirconate-titanate (PZT), and polyvinylidene fluoride (PVDF) are common materials. They are used in accelerometers, dynamic force transducers, pressure transducers, and ultrasound transducers. With ordinary charge readout, leakage gives the measurement a finite low-frequency cutoff, so piezoelectric sensors are best treated as dynamic sensors unless the instrument is designed for quasi-static use."

10. File: `volumes/01-quantity/ch05-sensors-and-instruments/chapter.tex`, lines 212-215.

Current text: "Robust, contactless, linear over their working range."

Proposed replacement: "With no sliding electrical contact at the moving core, LVDTs tolerate dirty industrial displacement measurements and stay linear over their specified range."

11. File: `volumes/01-quantity/ch05-sensors-and-instruments/chapter.tex`, lines 274-277.

Current text: "Superconducting quantum interference devices (SQUIDs): the highest-sensitivity magnetic sensors, used in biomagnetic measurements (magnetoencephalography), low-field NMR, and precision metrology."

Proposed replacement: "Superconducting quantum interference devices (SQUIDs): among the most sensitive magnetic sensors available, used in biomagnetic measurements (magnetoencephalography), low-field NMR, and precision metrology. Their engineering cost is the cryogenic, shielding, and noise-control system around the sensor."

12. File: `volumes/01-quantity/ch05-sensors-and-instruments/chapter.tex`, lines 296-303.

Current text: "A sensor specification of "$\pm 0.5\,\%$ of reading" without further qualification typically means a coverage interval (an expanded uncertainty) under stated conditions. Whether the coverage factor is $k = 1$, $k = 2$, or a maximum-permissible-error rectangular distribution depends on the manufacturer's convention."

Proposed replacement: "A sensor specification of "$\pm 0.5\,\%$ of reading" without further qualification is a manufacturer's error limit under stated conditions, not automatically a coverage interval. The datasheet may define it as maximum permissible error, expanded uncertainty, typical error, or a test limit. The reader should not infer $k = 1$, $k = 2$, or a rectangular distribution from the plus-minus sign alone."

13. File: `volumes/01-quantity/ch05-sensors-and-instruments/chapter.tex`, lines 343-349.

Current text: "A drift specification of $0.1\,\%$ per year on a sensor operating in an application that requires $1\,\%$ accuracy implies a recalibration interval not exceeding ten years, adjusted downward for confidence."

Proposed replacement: "A drift specification of $0.1\,\%$ per year on a sensor operating in an application that requires $1\,\%$ accuracy gives only a first bound on recalibration interval. The working interval also depends on initial calibration uncertainty, drift distribution, guard band, environmental exposure, and consequence of error."

14. File: `volumes/01-quantity/ch05-sensors-and-instruments/chapter.tex`, lines 398-402.

Current text: "\section{Choosing the right sensor}\pathtag{standard}"

Proposed replacement: "\section{Choosing the right sensor}\pathtag{core}"

15. File: `volumes/01-quantity/ch05-sensors-and-instruments/chapter.tex`, lines 450-457.

Current text: "we want to measure water and air temperatures in a kitchen environment over the range $0$ to $100 \,\si{\degreeCelsius}$ with combined standard uncertainty better than $\pm 1 \,\si{\degreeCelsius}$."

Proposed replacement: "we want to measure water and air temperatures in a kitchen environment over the range $0$ to $80 \,\si{\degreeCelsius}$ with expanded uncertainty no larger than $\pm 1 \,\si{\degreeCelsius}$ at a stated coverage factor. The lower range keeps the project inside the settled low-hazard brief."

16. File: `volumes/01-quantity/ch05-sensors-and-instruments/chapter.tex`, lines 467-469.

Current text: "\frac{1}{T} = A + B \ln R + C (\ln R)^{3},"

Proposed replacement: "\frac{1}{T} = A + B \ln\!\left(\frac{R}{R_{\ast}}\right) + C \left[\ln\!\left(\frac{R}{R_{\ast}}\right)\right]^{3},"

Add after the equation: "Here $R_{\ast}$ is a reference resistance, commonly $1 \,\si{\ohm}$ when handbook coefficients are reported for the numerical value of $R$ in ohms. The logarithm must act on a dimensionless ratio or on a stated numerical convention."

17. File: `volumes/01-quantity/ch05-sensors-and-instruments/chapter.tex`, lines 496-505.

Current text: "The thermistor is read through a voltage divider with $V_{\text{out}} = V_{\text{in}} R_{\text{th}} / (R_{\text{th}} + R_{\text{ref}})$."

Proposed replacement: "Define the divider before estimating it. In this chapter the fixed reference resistor is the upper leg and the thermistor is the lower leg, so the midpoint voltage is $V_{\text{out}} = V_{\text{in}} R_{\text{th}}/(R_{\text{ref}} + R_{\text{th}})$. With a $10 \,\si{\kilo\ohm}$ reference resistor and a $10 \,\si{\kilo\ohm}$ thermistor at room temperature, the midpoint sits near half the supply."

18. File: `volumes/01-quantity/ch05-sensors-and-instruments/chapter.tex`, lines 507-516.

Current text: "The dominant uncertainty source is therefore not the ADC quantisation; it is the thermistor's own tolerance (typically $\pm 1\,\%$ on resistance at $25 \,\si{\degreeCelsius}$, with the temperature error depending on slope), the reference resistor's tolerance (typically $\pm 1\,\%$ for $5\,\%$-tolerance through-hole resistors, $\pm 0.1\,\%$ for precision parts), and the calibration of the working temperature reference."

Proposed replacement: "For a one-degree project, ADC quantisation is usually smaller than the reference thermometer, resistor tolerance, self-heating, and fit residuals. For a tenth-degree project, a 10-bit ADC becomes marginal near the ends of the range and a 12-bit ADC is the safer choice. A common through-hole resistor may be $\pm 5\,\%$; ordinary metal-film parts are often $\pm 1\,\%$; precision reference resistors may be $\pm 0.1\,\%$ or better."

19. File: `volumes/01-quantity/ch05-sensors-and-instruments/chapter.tex`, lines 531-536.

Current text: "A four-and-a-half-digit handheld DMM has a working accuracy of about $\pm 0.05$ to $\pm 0.5\,\%$ of reading depending on function and range; a six-and-a-half-digit benchtop DMM reaches $\pm 0.001\,\%$ or better for DC voltage with appropriate calibration."

Proposed replacement: "A four-and-a-half-digit handheld DMM and a six-and-a-half-digit benchtop DMM can differ by orders of magnitude in DC-voltage accuracy, input burden, stability, and calibration interval. Replace this sentence with two cited datasheet examples, current as of the year of the cited datasheets, or move the numerical comparison to a companion note."

20. File: `volumes/01-quantity/ch05-sensors-and-instruments/chapter.tex`, lines 549-556.

Current text: "Modern digital storage oscilloscopes (DSOs) sample the input at rates from $\sim 100\,\text{MS}/\text{s}$ to $\sim 100\,\text{GS}/\text{s}$ (megasamples to gigasamples per second), with vertical resolution typically $8$ to $12$ bits."

Proposed replacement: "Digital storage oscilloscopes (DSOs) specify sample rate, analog bandwidth, memory depth, trigger performance, vertical resolution, and probe loading as a measurement system. If numerical ranges are retained here, cite representative manufacturer datasheets and state the year, because oscilloscope performance is a medium-life commercial claim."

21. File: `volumes/01-quantity/ch05-sensors-and-instruments/chapter.tex`, lines 611-617.

Current text: "Beyond optical resolution, the \engterm{scanning electron microscope (SEM)} reaches a few nanometres by focusing an electron beam onto the specimen and detecting backscattered or secondary electrons; the \engterm{transmission electron microscope (TEM)} reaches sub-nanometre by transmitting electrons through a thin specimen; \engterm{atomic force microscopy (AFM)} reaches sub-nanometre by scanning a sharp tip across the specimen surface."

Proposed replacement: "Beyond optical resolution, SEM, TEM, and AFM trade sample preparation, vacuum or surface requirements, calibration, and artefacts for much smaller length scales. Keep the numerical resolution claims only with citations to a microscopy handbook or representative instrument specifications; otherwise state the ordering qualitatively here and leave the quantitative treatment to Volume V."

22. File: `volumes/01-quantity/ch05-sensors-and-instruments/chapter.tex`, lines 635-642.

Current text: "The smartphone is itself a sensor array. A typical smartphone contains an accelerometer, a gyroscope, a magnetometer, a barometer, a proximity sensor, an ambient-light sensor, multiple microphones, multiple cameras (each with its own image sensor), GPS and other satellite receivers, cellular and Wi-Fi radio receivers, and an array of capacitive touch sensors on the screen. The reader's smartphone is, by raw sensor count, one of the most densely instrumented objects in their daily environment."

Proposed replacement: "A smartphone is a consumer sensor array. A model current as of 2026 may contain an accelerometer, gyroscope, magnetometer, barometer, proximity sensor, ambient-light sensor, microphones, cameras, GNSS receiver, cellular and Wi-Fi radios, and capacitive touch sensors. The exact inventory is model-specific, so any engineering use begins by reading the device specification and verifying the sensor output against a known reference."

23. File: `volumes/01-quantity/ch05-sensors-and-instruments/chapter.tex`, lines 647-651.

Current text: "A sensor's failure mode is what the engineer should worry about. The recurring pattern is that nominally independent sensors distributed across a system often fail not independently but together, because they share a single environmental cause, a single calibration history, or a single manufacturing batch."

Proposed replacement: "A sensor's failure mode belongs in the design record. Nominally independent sensors often share one environmental cause, calibration history, firmware version, or manufacturing batch; that shared cause can make the readings fail together."

24. File: `volumes/01-quantity/ch05-sensors-and-instruments/chapter.tex`, lines 665-671.

Current text: "Common-mode failure is not a marginal effect. It is the dominant failure mode in many high-reliability systems precisely because those systems have already eliminated the obvious single-point failures."

Proposed replacement: "Common-mode failure can dominate after obvious single-point failures have been removed. Redundancy only buys independence after the shared physical, software, calibration, and environmental causes have been analysed. Add a citation to a reliability or safety-engineering source if the stronger claim is retained."

25. File: `volumes/01-quantity/ch05-sensors-and-instruments/chapter.tex`, lines 673-703.

Current text: the Air France 447 subsection.

Proposed replacement: keep the subsection, but replace the event paragraph with the registry short form and cite the BEA report at the end: "On 1 June 2009 Air France Flight 447, an Airbus A330-203 from Rio de Janeiro to Paris, crashed into the Atlantic with the loss of all 228 people aboard. The BEA final report identified the precipitating event as temporary inconsistency between measured airspeeds, likely following obstruction of the pitot probes by ice crystals at high altitude. The autopilot disconnected, the flight-control system reconfigured to alternate law, and the crew assumed manual control with conflicting cockpit information. Sustained nose-up inputs led the aircraft into a stall that the crew did not diagnose or recover before impact \cite{acc:bea-af447}." Then add a secondary citation or remove "canonical."

26. File: `volumes/01-quantity/ch05-sensors-and-instruments/chapter.tex`, lines 716-719.

Current text: "A subtle bug in a sensor's embedded firmware affects every unit running that firmware version. The Ariane 5 Flight 501 case, treated in chapters 1 and 2, illustrates the same pattern in flight-control software."

Proposed replacement: "A subtle bug in a sensor's embedded firmware affects every unit running that firmware version. Ariane 5 Flight 501 illustrates the same common-mode software pattern in an inertial reference system: the primary and backup SRI ran the same software and failed from the same unhandled conversion overflow \cite{acc:ariane501-ifr}."

27. File: `volumes/01-quantity/ch05-sensors-and-instruments/chapter.tex`, lines 742-759.

Current text: project opening and hazard statement.

Proposed replacement: add after the hazard statement: "For the physical track, use a waterproof thermistor probe or keep the thermistor bead and leads electrically isolated from the water. Keep the breadboard, microcontroller, and power source dry and away from the container. Use cool, room-temperature, and warm water only; do not use boiling or near-boiling water for this project."

28. File: `volumes/01-quantity/ch05-sensors-and-instruments/chapter.tex`, lines 780-784.

Current text: "Wire (or simulate) the thermistor as the upper element of a voltage divider with the reference resistor, supplied by the microcontroller's $V_{\text{cc}}$ (typically $3.3 \,\si{\volt}$ or $5.0 \,\si{\volt}$). Read the divider output through the microcontroller's ADC."

Proposed replacement: "Wire (or simulate) the fixed reference resistor as the upper element from $V_{\text{cc}}$ to the ADC node and the thermistor as the lower element from the ADC node to ground. Then $V_{\text{out}} = V_{\text{cc}} R_{\text{th}}/(R_{\text{ref}}+R_{\text{th}})$. Read the midpoint voltage through the microcontroller's ADC."

29. File: `volumes/01-quantity/ch05-sensors-and-instruments/chapter.tex`, lines 785-791.

Current text: "immerse the thermistor and the reference thermometer in water at three or more known temperatures (e.g., ice water, room-temperature water, hot water cooled gradually, optionally near boiling)."

Proposed replacement: "place the waterproof thermistor probe and the reference thermometer in a stirred water bath at three or more reference temperatures (for example ice water, room-temperature water, and warm water below $60 \,\si{\degreeCelsius}$). Wait for both readings to settle. At each calibration point, record the divider output and reference temperature. Take at least ten samples per point and record their mean and standard deviation."

30. File: `volumes/01-quantity/ch05-sensors-and-instruments/chapter.tex`, lines 799-805.

Current text: "List each input source (thermistor tolerance, reference-resistor tolerance, ADC quantisation, ADC noise, calibration reference uncertainty, fit residuals) with an estimated standard uncertainty contribution."

Proposed replacement: "List each uncertainty source after calibration: reference thermometer uncertainty, reference-resistor tolerance, ADC reference-voltage uncertainty, ADC quantisation, electrical noise, self-heating, thermal contact, bath non-uniformity, and fit residuals. Do not count the thermistor's nominal resistance tolerance as a separate post-calibration uncertainty unless the model extrapolates outside the calibrated range."

31. File: `volumes/01-quantity/ch05-sensors-and-instruments/chapter.tex`, lines 806-809.

Current text: "Check that the difference is within the combined expanded uncertainty."

Proposed replacement: "Compute the uncertainty of the difference between the calibrated thermistor reading and the reference thermometer reading, including the reference thermometer's uncertainty. Check whether the observed difference is within the chosen expanded uncertainty and state the coverage factor."

32. File: `volumes/01-quantity/ch05-sensors-and-instruments/chapter.tex`, lines 882-890.

Current text: "thermistor $R_{\text{th}}$ as the upper element. Compute the output voltage $V_{\text{out}} = V_{\text{in}} R_{\text{th}} / (R_{\text{th}} + R_{\text{ref}})$"

Proposed replacement: "fixed resistor $R_{\text{ref}}$ as the upper element and thermistor $R_{\text{th}}$ as the lower element. Compute the output voltage $V_{\text{out}} = V_{\text{in}} R_{\text{th}}/(R_{\text{ref}}+R_{\text{th}})$"

Also replace "small changes in $R_{\text{th}}$" with "small fractional changes in $R_{\text{th}}$" if the intended answer is maximum sensitivity near $R_{\text{th}}=R_{\text{ref}}$.

33. File: `volumes/01-quantity/ch05-sensors-and-instruments/chapter.tex`, lines 903-910.

Current text: "Starting from the algebraic product-and-ratio rule, derive the relative uncertainty in a voltage divider output..."

Proposed replacement: "Starting from partial derivatives, derive the standard uncertainty in a voltage-divider output $V_{\text{out}} = V_{\text{in}} R_{\text{th}}/(R_{\text{ref}}+R_{\text{th}})$ for uncorrelated $V_{\text{in}}$, $R_{\text{th}}$, and $R_{\text{ref}}$. Then state the approximation that results when the resistance uncertainties are small and $R_{\text{th}} \approx R_{\text{ref}}$."

34. File: `volumes/01-quantity/ch05-sensors-and-instruments/chapter.tex`, lines 973-979.

Current text: smartphone gyroscope estimation exercise.

Proposed replacement: "Estimate the accumulated orientation uncertainty of a smartphone gyroscope over a $60 \,\si{\second}$ measurement, assuming a constant bias uncertainty of $10 \,\si{\degree\per\hour}$ and angular random walk of $0.1 \,\si{\degree\per\sqrt{\hour}}$. Compare the result with a tilt measurement that needs $0.5 \,\si{\degree}$ angular uncertainty for the building-height project of chapter 4."

35. File: `volumes/01-quantity/ch05-sensors-and-instruments/chapter.tex`, lines 1006-1012.

Current text: "Fit the Steinhart-Hart equation ... compare to the exact Steinhart-Hart form for a published thermistor part."

Proposed replacement: "Fit the Steinhart-Hart equation to a supplied synthetic calibration table for one named thermistor part. The problem statement must give the part number, the source of the nominal coefficients, and the generated noisy data. Compare the fitted curve with the beta-parameter approximation over $0$ to $80 \,\si{\degreeCelsius}$ and report the maximum temperature difference."

36. File: `volumes/01-quantity/ch05-sensors-and-instruments/chapter.tex`, lines 1027-1031.

Current text: "with required combined standard uncertainty $0.1 \,\si{\degreeCelsius}$ at $k = 2$."

Proposed replacement: "with required expanded uncertainty $\pm 0.1 \,\si{\degreeCelsius}$ at $k = 2$."

37. File: `volumes/01-quantity/_volume.tex`, lines 176-177.

Current text: "The remaining six archetypes (transport, stability, optimisation, control, interface, ethics) appear from Volume II onwards."

Proposed replacement: "The remaining archetypes arrive as needed. Interface appears first in Chapter 3 as the calibration handoff and recurs in Chapter 5 as the sensor-to-system handoff. Transport appears first in Chapter 5 as signal transport through the measurement chain. Stability, optimisation, control, and ethics arrive in later volumes."

38. File: `volumes/01-quantity/ch05-sensors-and-instruments/chapter.tex`, lines 17-20.

Current text: "Named cases: Air France Flight 447 (2009), as a common-mode sensor-failure case in the failure section; Hubble Space Telescope primary mirror (1990), revisited briefly from chapters 2--4 as a reference-instrument case."

Proposed replacement: "Named cases: Air France Flight 447 (2009), as a common-mode sensor-failure case in the failure section; Ariane 5 Flight 501 (1996), as a common-mode software case in the chronic-class list."

If Hubble remains in `\chapmeta`, add a short cited Hubble paragraph in the failure section. Otherwise remove it from the named-case list.

## H. Structural risks for the larger project

1. Archetype ownership is drifting across the dossier, opener, and chapter prose. Chapter 3 and Chapter 5 use interface; Chapter 5 introduces transport; the Volume I opener says both wait until Volume II. This is not a chapter-only problem. The project needs one archetype ledger with first appearance, later recurrence, and allowed wording. Without that ledger, each chapter will silently reassign the conceptual map.

2. Named-case tooling is too narrow. `make accidents` passed, but this chapter names Ariane 5 Flight 501 in prose without the registry citation and lists Hubble in `\chapmeta` without using it in prose. The check should scan `\chapmeta` named-case fields and fuzzy variants in prose, then require the registry key in the same chapter. The current pass result can give a false sense of safety.

3. The citation policy needs a datasheet and commercial-specification lane. Chapters like this one need to cite representative manufacturer datasheets without making the permanent text age around specific products. The current policy distinguishes primary, handbook, and tertiary sources, but it does not tell the writer how to support typical DMM, oscilloscope, thermistor, smartphone, and microscope performance figures. The release checklist should require either dated representative datasheets or a move to companion notes for fast-aging commercial ranges.

