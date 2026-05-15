# Engineering: project diagnostic

Date: 2026-04-28

> **Note (2026-04-29).** This diagnostic captures the repository state at the
> end of Phase 0.6. Phase 0.7 has since landed: Volume I now carries first-draft
> prose for all nine chapters, each reviewed and resolved (`docs/reviews/`),
> with a `~696`-page PDF instead of the `491`-page structural state described
> below. The diagnostic's three top risks (source-of-truth drift, scale honesty,
> verification discipline) are now partially mitigated; see `docs/status.md`
> for the current treatment. The diagnostic is preserved as a snapshot.
>
> **Note (2026-05-15).** Phase 1 has advanced through Volumes II-V drafted in
> full and Volume VI partially drafted (Ch 1-10 of 13). The PDF now runs 1972
> pages; 76 chapters carry first-draft prose; 210 bibliography entries; 20
> named-case registry entries. Vol I remains at Stage 5; Vols II-VI sit at
> Stage 4 awaiting Codex review. The diagnostic's content recommendations
> (curriculum coverage, source discipline, named-case treatment) have largely
> been honoured during drafting; gaps now sit at the page-density question
> (Q57) and the companion-note architecture question (Q54). The diagnostic
> remains preserved as a snapshot of Phase 0.6.

This diagnostic is a second pass over the current repository after the
Phase 0.6 expansion. It supersedes the earlier diagnostic that described the
retired `books/` layout and the 163-chapter state. The current project lives
under `volumes/`, has 174 chapter shells, and has matching per-chapter dossiers
under `docs/research/`.

This pass reads the repository as four things at once:

- A book architecture.
- A set of chapter and volume outlines.
- A production system for a very large technical text.
- A content map that should reveal missing engineering domains before prose
  begins.

## Executive judgement

The project is materially stronger than it was at the earlier Phase 0 state.
The obvious structural weakness, source-of-truth drift between generated TeX
and the research dossiers, has been partly fixed. The chapter shells now carry
dossier-derived `\chapmeta` blocks with half-life, archetype, exercise target,
and project-track placeholder. The layout now mirrors the real unit of work:
one folder per chapter, with room for figures, code, data, solutions, and review
logs.

The Phase 0.6 expansion also closed several real curriculum gaps. Acoustics,
mass transfer and separation processes, plasma physics, bioinformatics, quantum
computing, power electronics, MEMS, project management, user research, defence
systems, and space infrastructure are now present as chapters. That was not
cosmetic. Those topics changed the shape of Volumes III, IV, VI, VII, VIII, IX,
XI, and XII.

The project is still not a book draft. The 174 `chapter.tex` files are
structural shells: title, label, empty epigraph, metadata, section headings, and
TODO blocks. The usable intellectual content lives in the dossiers, not in the
chapter prose. That is acceptable for Stage 1, but it should stay visible in the
status language. A 491-page PDF exists, but it is a navigable outline, not 491
pages of book.

The highest current risk is no longer basic source-of-truth drift. The highest
risk is outline drift after expansion. Several volume dossiers and operational
documents still describe the old chapter numbering and old page counts. The
new chapters are present, but the surrounding narrative has not fully absorbed
them. If prose starts before that is repaired, writers will draft against stale
arcs.

The second current risk is content omission by implication. The 174 chapters
cover an enormous amount, but the outline still underrepresents some domains
that working engineers meet constantly: geotechnical and construction practice,
process engineering and process safety, electrical power-system protection,
engineering economics, manufacturing quality, standards and code literacy,
formal software assurance, environmental waste and pollution control, and the
practical safety discipline required for reader projects.

The third current risk is production readiness. Every chapter still has
`Project track: TBD`; every chapter has an empty epigraph; the TeX source has no
`estimation` environments and no in-text citations; the named-cases registry is
not created; solutions and rubrics are not designed. These are not defects in a
Phase 0 outline, but they are blockers for credible Phase 1 prose.

## Current inventory

Measured with the current tree and `make stats`:

| Item | Current state |
| --- | --- |
| Volumes | 12 |
| Chapter shells | 174 |
| Per-volume dossiers | 12 |
| Per-chapter dossiers | 174 |
| `\chapmeta` blocks | 174 |
| `Half-life: TBD` in chapter shells | 0 |
| `Project track: TBD` in chapter shells | 174 |
| TeX TODO markers | 1853 |
| Empty chapter epigraphs | 174 |
| Section headings | 1640 |
| Bibliography entries | 34 |
| `\begin{estimation}` in chapter shells | 0 |
| `\cite{...}` in chapter/body source | 0 |
| Structural PDF | 491 pages |

Chapter counts by volume:

| Volume | Count | Phase 0.6 additions of note |
| --- | ---: | --- |
| I Quantity | 9 | none |
| II Form | 18 | none |
| III Force | 13 | acoustics |
| IV Energy | 14 | mass transfer, plasma physics |
| V Matter | 12 | none |
| VI Life | 13 | bioinformatics |
| VII Information | 19 | quantum computing |
| VIII Machines | 14 | power electronics, MEMS |
| IX Systems | 19 | project management |
| X Failure | 16 | none |
| XI Design | 13 | user research |
| XII Civilization | 14 | defence systems, space infrastructure |

Verification run during this pass:

- `make stats` reports the counts above.
- `make check` passes: 174 chapter files have chapter, label, and chapmeta.
- `make strict` completes and writes a 491-page `main.pdf`.

The strict build still reports warning classes that should become release
checks later: duplicate page identifiers in frontmatter, header-height warnings,
overfull boxes from long headings, hyperref warnings from math in PDF strings,
and an empty bibliography in the current structural PDF.

## What improved since the earlier diagnostic

### 1. The repository layout now matches the unit of work

The previous `books/` layout has been replaced by:

- `volumes/<NN>-<slug>/_volume.tex`
- `volumes/<NN>-<slug>/ch<MM>-<slug>/chapter.tex`
- `docs/research/<NN>-<slug>/_volume.md`
- `docs/research/<NN>-<slug>/ch<MM>-<slug>.md`

This is the right long-term shape. Chapters will need local figures, local
datasets, local code, local solutions, local review logs, and sometimes local
companion notes. A one-folder-per-chapter structure prevents the main source
tree from becoming unmanageable.

### 2. Chapter metadata is now present in the shells

Every chapter shell has a `\chapmeta{...}` block. The half-life TODO problem is
gone at chapter level. The shell now reminds the writer of:

- Half-life category.
- Archetypes invoked.
- Exercise target.
- Project-track placeholder.

This fixes a large part of the earlier source-of-truth problem. It does not
finish it, because the shell still lacks project track, prerequisites, source
targets, named cases, exercise taxonomy, and safety notes.

### 3. The operational policy layer is much stronger

The repository now has concrete policy documents for:

- Voice and house style.
- Citation tiers and citation-key categories.
- Case-study structure.
- Reviewer roles and checklist.
- Release checks.
- Research pipeline.
- Open questions.
- Interlude management.

This is the right move. A 174-chapter technical project cannot be governed by
memory. The policy layer makes quality review possible.

### 4. Phase 0.6 closed real content holes

The new chapters are mostly well chosen. In particular:

- Acoustics belongs in Force, not as a footnote to waves.
- Mass transfer and separation processes closes a major chemical/process gap.
- Plasma physics gives Energy a route to fusion, electric propulsion, arcs, and
  ionized media.
- Bioinformatics prevents Life from treating biological information as only a
  wet-lab topic.
- Quantum computing prevents Information from being dated before prose begins.
- Power electronics is essential for modern machines, drives, grids, EVs, and
  renewable systems.
- MEMS gives sensors and microsystems a proper engineering home.
- Project management is necessary because many engineering failures are project
  failures before they are technical failures.
- User research improves Design by adding the front end of requirements.
- Defence and space infrastructure belong in Civilization because they are
  civilization-scale engineering domains, not just technologies.

## Structural and document drift

### 1. Several volume arcs still describe the old chapter order

The new chapters are present in the chapter lists, but several `_volume.md`
arc paragraphs still narrate the old numbering.

Examples:

- Volume III says Chapters 7-8 are structural mechanics and Chapters 9-12 are
  fluids. Chapter 7 is now Acoustics, Chapters 8-9 are structural mechanics,
  and Chapters 10-13 are fluids.
- Volume IV says Chapters 7-9 are electromagnetism, Chapter 10 is optics,
  Chapter 11 is quantum effects, and Chapter 12 closes with energy systems.
  The current chapter list has mass transfer at 7, electromagnetism at 8,
  circuits at 9, EM waves at 10, optics at 11, quantum at 12, plasma at 13, and
  energy systems at 14.
- Volume VI's arc still treats Chapter 11 as biocompatibility and Chapter 12 as
  the closing regenerative-medicine chapter. Bioinformatics is now Chapter 11,
  biocompatibility is Chapter 12, and regenerative medicine is Chapter 13.
- Volume VII's arc and bridges still describe the pre-quantum numbering:
  signal processing, digital control, ML, AI, and software engineering are now
  Chapters 15-19, not 14-18.
- Volume VIII's arc still says analog and digital electronics are Chapters 8-9,
  sensors are 10, robotics is 11, and hydraulics/mechatronics is 12. Power
  electronics and MEMS shifted the end of the volume.
- Volume IX's arc still says Chapters 9-10 are operations optimisation and
  decision under uncertainty, but project management is now Chapter 10 and
  decision under uncertainty is Chapter 11.
- Volume XI's arc still describes the pre-user-research order and treats the
  capstone as Chapter 12. It is now Chapter 13.
- Volume XII's arc still says Chapters 9-10 are climate engineering and
  planetary boundaries. Defence and space now occupy Chapters 9-10; climate and
  planetary boundaries are Chapters 11-12.

Fix: run a volume-dossier refresh pass before drafting. This should not be a
mere renumbering pass. Each volume arc should explain why the inserted chapters
belong where they now sit.

### 2. Operational docs contain stale counts

The following stale references remain:

- `docs/status.md` says "163 chapter shells" under "What is complete" and says
  the PDF is around 465 pages, while the live state is 174 chapters and around
  491 pages.
- `docs/research-pipeline.md` says all 163 chapters are at Stage 1 and uses
  163 chapters in capacity planning.
- `docs/research/landscape.md` has an updated page-budget table, but the
  problem/project budget still says 163 chapters, about 4900 exercises, and a
  final capstone in Volume XI Chapter 12. The capstone is now Chapter 13.
- `scripts/generate_scaffolding.py` still opens with comments saying it
  generates 163 chapter shells from `docs/research/book-XX-*.md`, even though
  later code and the current output are 174 and use the split dossier layout.
- `Makefile` target `outline` still loops over `docs/research/book-*.md`, a
  path pattern that no longer matches the current dossier structure.
- `appendices/appD-reading-list.tex` references
  `docs/research/book-NN-slug.md`, which is obsolete and creates an overfull
  box in the strict build.
- `README.md` has a duplicated "5." in the anchor-doc list.

Fix: add a stale-count check to `make check`, or create `make audit-docs`, that
flags `163`, `465`, `book-*.md`, `book-NN`, and old capstone references outside
historical phase notes.

### 3. The generator still owns chapter structure

The README says the generator is the source of truth for slugs, titles, and
section structure, and the dossiers are the source of truth for metadata. That
split is workable, but it has a cost: the chapter outline lives in Python data,
while editorial discussion lives in Markdown dossiers.

This is acceptable for scaffolding. It becomes awkward in prose. Writers will
edit dossiers, not Python. If section lists change during writing, they should
not require hand-editing a 2000-line Python file unless that file remains the
intentional canonical outline.

Fix options:

- Keep the current model, but say explicitly that section structure is edited
  in the generator until prose starts.
- Move chapter section structure into the Markdown dossiers and let the
  generator parse it.
- Freeze scaffolding after Phase 0.6 and stop regenerating chapter files except
  through explicit migrations.

The second option is best long term. The first is acceptable for the pilot. The
third is safest once prose begins.

## Chapter and content gap audit

The current outline is broad and serious. It covers measurement, engineering
math, mechanics, thermodynamics, heat transfer, mass transfer, electromagnetism,
optics, quantum effects, plasma, materials, biology, information systems,
software, machines, control, reliability, failure, design, and civilization
scale infrastructure.

The remaining gaps are not random missing topics. They cluster around the
messy parts of engineering practice: ground, site, plant, power, safety,
standards, economics, quality, environment, and assurance.

### Gap 1: Civil, geotechnical, and construction engineering

The outline has structural mechanics in Volume III, concrete as a material in
Volume V, and buildings/cities in Volume XII. It does not yet have a clear home
for the ground and the construction process.

Missing or thin topics:

- Soil mechanics.
- Foundations.
- Retaining walls and earth pressure.
- Slope stability.
- Site investigation and uncertainty in ground models.
- Surveying and geospatial control.
- Drainage as a structural and site constraint.
- Seismic, wind, fire, and code load cases.
- Construction sequencing.
- Temporary works.
- Inspection, commissioning, and field tolerances.

Why this matters: a large fraction of engineering becomes physical through
sites, foundations, construction tolerances, and code-governed inspection. A
book with beams, plates, materials, and cities but no ground risks sounding like
it was written from a clean desk instead of from engineering practice.

Fix:

- Minimum: add explicit geotechnical and construction sections to Volume III
  Chapters 8-9 and Volume XII Chapter 7.
- Better: add a new chapter, likely in Volume III after plates/shells or in
  Volume XII before buildings/cities, titled something like "Ground,
  foundations, and construction." If the project wants one canonical civil
  chapter, this is the most defensible new chapter.
- Also add named failures: Aberfan, Vajont, Banqiao, St. Francis Dam, Hyatt
  Regency, Citicorp, Surfside, Morandi, and one tailings-dam failure, each only
  where primary sources support them.

### Gap 2: Process engineering and process safety

The new mass-transfer chapter is a major improvement. It covers diffusion,
convective mass transfer, distillation, absorption, extraction, adsorption,
membranes, drying, crystallisation, leaching, fouling, and separation failures.

What remains missing is the plant-level process-engineering discipline.

Missing or thin topics:

- Process flow diagrams and P&IDs.
- Reactor design beyond basic reactions and equilibria.
- Unit operations as an integrated process.
- Process control in plants.
- Relief systems and overpressure protection.
- Hazard and operability analysis.
- Layers of protection analysis.
- Safety instrumented systems.
- Process safety management.
- Commissioning, startup, shutdown, and abnormal operations.

Why this matters: chemical, energy, pharmaceutical, food, water, and
biomanufacturing systems all depend on process engineering. Without it, mass
transfer becomes a chapter of transport phenomena rather than a route to plant
design.

Fix:

- Minimum: extend Volume IV Chapter 7 with a "process integration" section and
  add process-control/safety subsections in Volume IX and Volume X.
- Better: add a new Volume IV or Volume IX chapter called "Process engineering
  and process safety." It would connect thermodynamics, heat transfer, mass
  transfer, reactions, control, reliability, and failure.
- Add Bhopal, Texas City 2005, Flixborough, Buncefield, Deepwater Horizon, and
  one pharmaceutical or food-process contamination case to the named-cases
  registry.

### Gap 3: Electrical power systems beyond conversion electronics

Power electronics is now present and strong. Energy systems integration and
planet-scale energy are present. What is thin is the practical grid and
installation discipline between them.

Missing or thin topics:

- Transformers and switchgear.
- Three-phase power at system depth.
- Short-circuit analysis.
- Protection coordination.
- Protective relays.
- Grounding and bonding.
- Arc flash.
- Power quality and harmonics.
- Substations.
- Grid codes and interconnection requirements.

Why this matters: power electronics without protection and grounding is an
incomplete picture of real electrical engineering. Grid-tied systems fail at
interfaces, protection settings, installation practice, and regulatory
interconnection as often as at converter topology.

Fix:

- Add a power-systems protection section to Volume IV Chapter 14.
- Add grid-code and interconnection material to Volume VIII Chapter 9.
- Add arc-flash, grounding, and safe electrical work to the project safety
  policy before any reader build project uses mains voltage.

### Gap 4: Proactive safety engineering and assurance cases

Failure is treated seriously. Reliability theory, FMEA, fault trees, common-mode
failure, human factors, regulation, forensic engineering, and post-mortems are
all present. The missing piece is safety as a design-time assurance discipline.

Missing or thin topics:

- Hazard analysis beyond FMEA and fault trees.
- HAZOP.
- STPA and system-theoretic safety.
- Safety cases and assurance cases.
- ALARP and risk acceptability.
- SIL and safety instrumented functions.
- Safety-critical software standards.
- Medical, automotive, aerospace, rail, and nuclear assurance regimes.
- Traceability from hazard to requirement to test evidence.

Why this matters: the book teaches how things fail and how to design under risk,
but a working engineer also needs to know how an organization argues, with
evidence, that a system is acceptably safe before deployment.

Fix:

- Add "safety assurance" as a named thread across Volume IX Chapter 7, Volume IX
  Chapter 14, Volume X Chapter 11, and Volume XI Chapter 9.
- Consider one integrated chapter in Volume XI: "Safety cases, standards, and
  sign-off." If no new chapter is added, expand the certification chapter
  substantially.

### Gap 5: Engineering economics, procurement, and cost

Project management now exists. Maintenance includes life-cycle costing. Design
and civilization discuss political economy. Still, the core engineering
economics toolkit is not explicit.

Missing or thin topics:

- NPV and discounting.
- Cost of capital.
- CAPEX, OPEX, and total cost of ownership.
- Cost-estimate classes and uncertainty.
- Learning curves.
- Sensitivity analysis for cost.
- Procurement and contracting models.
- Make/buy decisions.
- Cost-risk tradeoffs.
- Real options under uncertainty.

Why this matters: engineering decisions are constrained by money as surely as
by stress, heat, entropy, and information. A reader who can size a beam but
cannot compare life-cycle costs is not yet ready for real design tradeoffs.

Fix:

- Add engineering economics to Volume IX Chapter 10 and Volume XI Chapter 2.
- Add a recurring "cost model" box type or subsection for major design
  chapters.
- Require every substantial volume project to include cost estimate, uncertainty
  range, and life-cycle cost.

### Gap 6: Manufacturing quality and industrial quality systems

Manufacturing, CAD, tolerancing, materials properties, and testing are present.
Quality as a production discipline is still thin.

Missing or thin topics:

- Statistical process control.
- Process capability indices.
- Gauge R&R.
- Acceptance sampling.
- Control plans.
- First article inspection.
- Nonconformance and corrective action.
- ISO 9001 as a quality-system example.
- Six Sigma as a toolset, without hype.
- Tolerance stack-up as a manufacturing-quality system, not only a drawing
  topic.

Why this matters: repeatability is the difference between a prototype and a
product. The project currently teaches how to make and test, but not yet enough
about how a production system knows it is still making the same thing.

Fix:

- Add a manufacturing-quality section to Volume VIII Chapter 6.
- Add SPC and process capability to Volume I or II statistics examples, then
  reuse them in Volume VIII.
- Add quality-system failure cases to Volume X and review/checklist material to
  Volume XI.

### Gap 7: Environmental engineering, waste, and pollution control

Water, sanitation, climate, planetary boundaries, materials degradation, and
food systems are present. The remaining weakness is waste and pollution control
as engineered systems rather than only planetary outcomes.

Missing or thin topics:

- Air pollution control.
- Solid waste systems.
- Hazardous waste treatment.
- Wastewater-treatment process detail beyond one section.
- Landfills, leachate, and liners.
- PFAS and persistent contaminants as engineering problems.
- Life-cycle assessment methods.
- Environmental monitoring and permitting.

Why this matters: engineers do not only produce artifacts. They produce waste
streams, emissions, residues, and long-tail maintenance burdens. These deserve
mechanistic treatment before the political-economy discussion.

Fix:

- Expand Volume XII Chapter 3 beyond supply/sanitation into treatment-process
  detail.
- Add waste and pollution subsections to Volume XII Chapter 12.
- Add life-cycle assessment method material to Volume XI Chapter 10.
- Add environmental source categories to the citation policy and named-cases
  registry.

### Gap 8: Standards, codes, legal liability, and professional practice

Certification, regulation, and engineering ethics are present. What is thin is
standards literacy: how a working engineer reads, applies, cites, and deviates
from codes and standards.

Missing or thin topics:

- How standards are written and revised.
- Normative versus informative clauses.
- Code-based design.
- Authority having jurisdiction.
- Design records and drawing sign-off.
- Professional licensure where relevant.
- Liability, negligence, duty of care, and standard of care.
- Deviation control and waiver processes.

Why this matters: standards are not decorative citations. They are part of the
operating system of engineering practice.

Fix:

- Add a "standards literacy" appendix or a Volume XI section.
- Require every standards-driven chapter to name the standards family it uses.
- Seed the bibliography with real `std:` entries before writing standards-heavy
  chapters.

### Gap 9: Software assurance, formal methods, privacy, and data governance

Volume VII is broad and good. It covers algorithms, data structures, systems,
security, distributed systems, ML, AI, and software engineering. The risk is
that production software assurance gets compressed into testing and CI/CD.

Missing or thin topics:

- Requirements traceability for software.
- Formal verification and model checking.
- Static analysis beyond compiler checks.
- Property-based testing at depth.
- Secure software supply chain as an engineering system.
- Privacy engineering.
- Data governance.
- Dataset documentation, lineage, and deletion.
- Safety-critical software standards and evidence packages.

Why this matters: the book gives software equal dignity with physical
engineering. That requires software assurance to be treated as a real discipline,
not just as better testing habits.

Fix:

- Expand Volume VII Chapter 19 with formal assurance, requirements traceability,
  and evidence packages.
- Add privacy and data governance to databases, security, ML, and modern AI.
- Tie safety-critical software into Volume X and Volume XI, not only Volume VII.

### Gap 10: Geospatial engineering, GIS, and remote sensing

Surveying appears implicitly in measurement and infrastructure, but GIS,
mapping, remote sensing, and geospatial data are not explicit.

Missing or thin topics:

- Surveying and coordinate reference systems.
- GPS/GNSS beyond time measurement.
- GIS layers and spatial joins.
- Remote sensing.
- Earth observation data.
- Terrain models.
- Map projection errors.
- Geospatial uncertainty.

Why this matters: infrastructure, climate, transport, water, agriculture,
defence, and space all rely on geospatial data. Treating geospatial work as
background misses a recurring engineering interface.

Fix:

- Add geospatial sections to Volume I, Volume XII Chapter 4, Volume XII Chapter
  5, and Volume XII Chapter 10.
- Add one worked cross-volume case: flood-risk mapping or transport-network
  accessibility using real geospatial data.

### Gap 11: Resource extraction, mining, petroleum, and tailings

The project covers materials and energy use, but extraction is mostly implicit.
That may be a deliberate omission, but it should be deliberate.

Missing or thin topics:

- Mining systems.
- Ore grades and resource estimation.
- Petroleum drilling and reservoir engineering.
- Tailings dams.
- Resource depletion and EROI.
- Environmental and labor risk in extraction.

Why this matters: materials and energy do not enter civilization at the factory
gate. Extraction is where many technical, environmental, and political risks
begin.

Fix:

- Decide explicitly whether extraction is in scope.
- If in scope, add subsections to Volume V, Volume XII Chapter 2, and Volume XII
  Chapter 12, plus tailings-dam cases in Volume X.
- If out of scope, state the omission in the landscape or Volume XII scope.

### Gap 12: Human factors, ergonomics, and accessibility as engineering

User research and operator error are present. Accessibility appears in Design.
The remaining issue is human factors as quantitative engineering practice.

Missing or thin topics:

- Anthropometry.
- Ergonomics.
- Cognitive workload.
- Task analysis.
- Alarm design.
- Control-room design.
- Human reliability analysis.
- Accessibility standards and assistive-technology engineering.

Why this matters: the interface archetype is one of the book's central devices.
The human body and human attention are part of that interface.

Fix:

- Strengthen Volume X Chapter 9 with quantitative human factors.
- Extend Volume XI Chapter 3 and Chapter 10 with accessibility standards and
  measurable usability/accessibility evidence.
- Use one medical-device or industrial-control-room case as a full case study.

### Gap 13: Reader project safety

The dossier projects are ambitious, which is good. Some are also risky if
written without guardrails: distillation, power converters, batteries, robotics,
high voltage, biological work, defence-adjacent projects, and physical machines.

Missing or thin topics:

- General lab, shop, electrical, chemical, and biological safety policy.
- Hazard class per project.
- Tools required.
- Minimum supervision level.
- Safe alternative tracks.
- Prohibited builds.
- Disposal and environmental safety.

Why this matters: a serious adult learner can be trusted with hard work, but
the book should not quietly push readers into unsafe builds.

Fix:

- Add a project-safety appendix before prose starts.
- Add project track and hazard class to `\chapmeta` or the chapter dossier.
- Require every chapter project to offer at least one safe simulation or
  analysis track when the physical track carries non-trivial hazard.
- Treat defence-adjacent projects as analysis, detection, provenance,
  resilience, or simulation tasks unless explicitly reviewed for safety and
  dual-use risk.

### Gap 14: Technical communication and data visualization

The project has CAD/drawing, reports in projects, statistics, and Tufte in the
cross-volume reading list. It does not yet teach engineering communication as a
discipline.

Missing or thin topics:

- Plot design and graphical honesty.
- Tables with provenance.
- Technical memos.
- Design-review packets.
- Incident reports.
- Dashboards and observability displays.
- Decision records.
- Explaining uncertainty to non-specialists.

Why this matters: engineering fails when the result is technically correct but
communicated in a form that decision-makers misread.

Fix:

- Add graph and table discipline to Volume I and Volume II.
- Add report and decision-record standards to Volume XI.
- Add dashboards to Volume IX observability and Volume VII data systems.

### Gap 15: Solutions, rubrics, and assessment architecture

The outline targets thousands of exercises, 174 chapter projects, 12 substantial
volume projects, studios, and a capstone. The repository does not yet define how
solutions and rubrics live.

Missing:

- Exercise taxonomy.
- Difficulty levels.
- Answer format.
- Full solutions versus hints.
- Auto-checkable exercises.
- Project rubrics.
- Reviewer rubric for capstone.
- Companion repository layout for code/data exercises.

Why this matters: the exercises are a core part of the formation promise. If
they are not architected early, they will become inconsistent across volumes.

Fix:

- Add `docs/exercise-system.md`.
- Add `solutions/` or per-chapter `solutions/` policy before writing many
  exercises.
- Define exercise types: calculation, derivation, estimation, simulation,
  design, critique, case reconstruction, and project.
- Require the pilot chapter to include production-grade exercises and at least
  one worked solution.

## Per-volume critique

### Volume I: Quantity

Strong foundation. Measurement, units, calibration, error, sensors, statistics,
and estimation are the right opening. The project should add more explicit
graph/table/data-visualization discipline here because every later empirical
claim depends on it. This is also the natural place to introduce provenance for
measurements and datasets.

### Volume II: Form

Broad and defensible. The engineering-math scope is coherent and avoids
graduate-math sprawl. The main risk is overload. The reader-path model from Q51
is especially important here because Volume II can become a gate that blocks
otherwise capable readers. Probability, inference, optimisation, and numerical
methods are strong choices to keep inside the main math volume.

### Volume III: Force

The addition of acoustics is correct. The mechanics and fluids spine is strong.
The remaining weakness is civil/geotechnical reality: ground, foundations,
seismic/wind/fire load cases, construction sequencing, and inspection. The
volume currently teaches clean mechanics better than messy site mechanics.

### Volume IV: Energy

The mass-transfer chapter fixes a major omission. Plasma physics is useful and
well placed. The volume now needs its arc rewritten because the old
thermo-to-EM narrative no longer describes the contents. The main content gap is
process engineering and power-system protection: plant-level integration,
process safety, substations, grid protection, and safe electrical practice.

### Volume V: Matter

Solid and coherent. Materials classes, degradation, selection, processing, and
energetic materials belong. The main gaps are environmental material flows,
resource extraction, waste streams, toxicity, and lifecycle assessment. Concrete
is present under ceramics, which is good, but the civil consequences of concrete
need bridges to Volume III and XII.

### Volume VI: Life

Bioinformatics was a necessary addition. The volume now has a good route from
cells to tissue, biomechanics, control systems, populations, synthetic biology,
biomanufacturing, bioinformatics, devices, and regenerative medicine. The
volume dossier needs renumbering. Content risks: biosafety, clinical/regulatory
practice, and bio-data governance need explicit handling.

### Volume VII: Information

Very strong. It gives software and computation the dignity of engineering
instead of treating them as a tool appendix. Quantum computing was a good
addition. The main gaps are formal assurance, privacy engineering, data
governance, and safety-critical software standards. These should be added
without turning the volume into a computer-science degree.

### Volume VIII: Machines

The addition of power electronics and MEMS makes the volume much more modern.
The mechanical, manufacturing, electronics, sensors, robotics, and mechatronics
arc is sound. The weaknesses are manufacturing quality systems, electrical
safety/protection, and production operations. The volume should teach the
difference between a working prototype and a qualified product.

### Volume IX: Systems

One of the strongest volumes. Control, stochastic systems, reliability,
queueing, optimisation, project management, decision under uncertainty,
multi-agent systems, networks, cyber-physical systems, infrastructure, coupled
human-technical systems, resilience, maintenance, and systems synthesis form a
real systems curriculum. The missing pieces are engineering economics,
procurement, safety assurance, and standards at system level.

### Volume X: Failure

The concept is excellent. Failure as its own full volume is one of the project's
best choices. The risk is case-study quality. Without a named-cases registry,
the same accidents will be retold inconsistently or shallowly. The volume also
needs process-safety, civil/geotechnical, power-system, software-assurance, and
environmental-waste cases to match the gap list above.

### Volume XI: Design

User research was the right addition. The design sequence now begins closer to
the real front end of engineering work. The volume should now absorb standards,
safety cases, engineering economics, accessibility evidence, design records,
and sign-off practice. The capstone is Chapter 13; all documents saying Chapter
12 need updating.

### Volume XII: Civilization

Defence and space infrastructure make the volume more honest about what
civilization-scale engineering includes. The volume is ambitious and largely
coherent. The remaining gaps are waste, extraction, geospatial infrastructure,
disaster management, environmental permitting, and the mundane maintenance
institutions that keep civilization-scale systems alive.

## Dossier schema critique

The per-chapter dossiers are useful, but too thin for Stage 2. A typical
chapter dossier currently contains:

- Chapter title and page target.
- Section list with page budgets.
- Archetype.
- Project brief.
- Exercise count.
- Link back to the volume dossier and chapter shell.

That is enough for scaffolding. It is not enough for source acquisition or
production prose.

Recommended additions to the per-chapter dossier schema:

- Scope: what the chapter must teach.
- Non-goals: what the chapter refuses to teach.
- Prerequisites: prior chapters required.
- Forward dependencies: later chapters that rely on it.
- Core derivations or models.
- Required worked examples.
- Required estimation blocks.
- Named cases and accident-registry links.
- Source-acquisition checklist.
- Standards and primary-source targets.
- Project track, hazard class, tools, and safe alternatives.
- Exercise taxonomy and difficulty distribution.
- Companion-note needs for fast-aging material.
- Open editorial questions specific to the chapter.

Without this schema, Stage 2 source acquisition will be inconsistent across
writers.

## Recommended fixes before Phase 1 prose

### Priority 1: Clean all post-expansion drift

Do this before drafting the pilot:

- Refresh every `_volume.md` arc paragraph and bridge note affected by new
  chapters.
- Update `docs/status.md`, `docs/research-pipeline.md`,
  `docs/research/landscape.md`, generator comments, README numbering, Makefile
  `outline`, and appendix path references.
- Add a stale-reference check for `163`, `465`, old capstone references, and
  obsolete `book-*.md` paths.

### Priority 2: Create a content gap register

Add `docs/content-gap-register.md` or use `docs/open-questions.md` to track the
gap decisions explicitly. For each gap, record:

- Decision: add chapter, add sections, companion note, or deliberate omission.
- Owner volume.
- Affected chapters.
- Source requirements.
- Whether it blocks pilot prose.

The important point is not to add every possible topic. The important point is
to make omission deliberate.

### Priority 3: Decide whether to add chapters

The minimum no-new-chapter path is possible, but only if sections are added
carefully. The better path is to consider two to five new chapters.

Most defensible new chapters:

1. `Ground, foundations, and construction`.
2. `Process engineering and process safety`.
3. `Power systems: protection, grounding, and grid practice`.
4. `Safety assurance, standards, and sign-off`.
5. `Engineering economics and quality`.

The first two are the strongest candidates for actual new chapters. The others
could be handled as major sections if the project wants to hold the chapter
count near 174.

### Priority 4: Resolve Q55 project tracks and add project safety

Every chapter currently has `Project track: TBD`. This is the most visible
unfinished metadata field. Resolve it by volume, not ad hoc.

Recommended track fields:

- Primary track: physical, simulation, household, software, analysis, field, or
  hybrid.
- Hazard class: none, low, moderate, high, prohibited without supervision.
- Tools required.
- Safe alternative.
- Expected artifact.

### Priority 5: Start the named-cases registry

Create `docs/research/accidents/` before any failure prose starts. Seed it with
at least 30 entries across domains:

- Measurement and unit failures.
- Aerospace.
- Civil and structural.
- Process safety.
- Medical devices.
- Software and security.
- Power and grid.
- Environmental and ecological.
- Organizational and regulatory failures.

Each entry should carry primary source status, not just a popular name.

### Priority 6: Build the exercise and solution architecture

Before writing many exercises, decide:

- Where solutions live.
- Which exercises receive full solutions.
- Which are auto-checkable.
- How projects are graded.
- How exercises are tagged by type and difficulty.
- Whether code/data exercises live beside chapters or in a companion repo.

The pilot chapter should prove this architecture, not merely produce prose.

### Priority 7: Strengthen `make check`

Current `make check` is useful but too shallow. Add checks gradually:

- Every chapter has Project and Exercises sections.
- Every volume dossier chapter count matches actual chapter files.
- No `Project track: TBD` after the project-track pass.
- No empty epigraphs after prose status.
- No `\TODO` in release targets.
- No stale counts or obsolete paths in docs.
- No math tokens in PDF strings for section titles.
- No missing bibliography entries once citations begin.
- No named accident without registry entry or primary-source status.

## Suggested next work order

1. Run a one-day drift cleanup across docs and generator comments.
2. Create a gap register and decide which gaps become chapters versus sections.
3. Refresh affected volume arcs.
4. Resolve project tracks for Volume I only.
5. Write the pilot chapter, Volume I Chapter 1, with full citations, estimation
   blocks, exercises, project rubric, and review checklist.
6. Use the pilot to revise the dossier schema and release checklist.
7. Only then scale to other chapters.

## Bottom line

The project is viable as an architecture. It has a real thesis, a defensible
sequence, a strong failure discipline, and a serious operational policy layer.
Phase 0.6 moved it from a good skeleton to a much better curriculum map.

The content gaps are concentrated and fixable. The biggest missing domains are
not exotic edge cases. They are the practical disciplines that turn models into
working infrastructure: ground, construction, process plants, power protection,
safety assurance, economics, quality, standards, waste, and project safety.

The next pass should not start by writing 174 chapters. It should stabilize the
post-expansion outline, make the remaining omissions explicit, and then carry
one pilot chapter to production standard. That pilot will reveal the real cost
of the whole project.
