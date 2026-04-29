# Engineering: editorial decisions log

The fifty editorial questions whose answers commit the book to specific design choices. All fifty were settled on 2026-04-26 in a single negotiating session, after which this file became the project's decisions log rather than its open-questions list. The five questions originally flagged **(load-bearing)** were settled first; the remaining forty-five were settled in the same pass, anchored by the load-bearing five.

When a settled answer needs revision, do not delete the previous Settled block. Add a new Settled block beneath it, dated, with the new wording and a brief note on why the change was needed. The history is part of the document.

# Project definition

The compact project definition that follows from the fifty settlements:

> *Engineering* is a digital-first, multi-volume, 20,000-page formation text for serious adult learners. It teaches the wide discipline of reliable intervention under constraint, using engineering-depth science, recurring problem archetypes, estimation, design, simulation, physical projects, failure analysis, ethics, and civilization-scale synthesis.

The core constraint:

> It must read like one guided ascent, while being technically strong enough that domain experts do not flinch.

The book's thesis, as settled in question 35:

> Engineering is the discipline by which measured reality becomes reliable intervention under constraint, failure, scale, and responsibility.
>
> Engineering is not applied science.
> Engineering is disciplined intervention.

# Audience and the reader's life

## 1. Audience  (load-bearing)

Is the audience really 25-year-olds, or any serious adult learner? Does the book address itself to one and treat the other as overhearing?

### Settled 2026-04-26

The primary reader is **any serious adult learner**, with the imagined reader being a capable 25-year-old who wants to become an engineer in mind and practice. The book addresses that reader directly, while allowing older professionals, self-taught builders, and students to overhear without feeling excluded.

Implication: do not write it as a youth textbook, university textbook, or credential manual. Write it as a formation text for a serious adult.

## 2. Mathematical preparation

Is the reader assumed to be mathematically prepared (calc, linear algebra), or is Volume II the first place they meet derivatives?

### Settled 2026-04-26

The reader is assumed to have solid secondary-school algebra, geometry, trigonometry, and basic scientific notation, but **not** calculus or linear algebra. Volume II introduces derivatives, integrals, vectors, matrices, probability, and differential equations from first principles, but at adult speed.

## 3. Reader's life situation

Is the reader already in a job, a degree programme, neither? Does the book assume employment, parallel study, or a clean slate?

### Settled 2026-04-26

The reader is assumed to have an adult life, not a protected student existence. The book is designed for self-study alongside work or parallel study, with suggested "slow," "standard," and "intensive" paths.

## 4. Language

Romanian-first or English-first? If both, which one is the source-of-truth and which is the translation?

### Settled 2026-04-26

English is the source-of-truth language. Romanian may exist as a translation or companion edition, but terminology, notation, citations, and errata are governed by the English edition.

## 5. Self-taught or paired with teacher

Self-taught or paired with a teacher? The book changes if the reader has nobody to ask vs. a weekly office hour.

### Settled 2026-04-26

The book is designed to be self-taught, with optional use by teachers, mentors, reading groups, or institutions. No chapter may require a lecturer to make it intelligible; the text itself must carry the explanation.

# Scope: what counts as "engineering"

## 6. Sense of "engineering"  (load-bearing)

The wide German sense (Ingenieurwissenschaft, all applied science) or the narrower licensed-PE sense?

### Settled 2026-04-26

The book uses the **wide sense of engineering**: the disciplined transformation of scientific, mathematical, computational, biological, material, and organisational knowledge into reliable interventions in the world. Licensed professional engineering is treated as one historically important institutional form, not the boundary of the subject.

Implication: software, biology, infrastructure, systems, energy, computation, manufacturing, and organisation all belong. The book is not "civil/mechanical/electrical plus extras." It is applied world-making under constraint.

## 7. Software engineering

Is software engineering the same kind of engineering as civil engineering in this book, or parallel? They have different epistemologies.

### Settled 2026-04-26

Software engineering is treated as genuine engineering, but with a distinct epistemology: formal systems, cheap replication, adversarial complexity, invisible failure modes, and extreme scale. It belongs inside the main structure, while also receiving dedicated treatment in the information and systems volumes.

## 8. Mathematics in Volume II

Volume II is mathematics. Is it engineering-mathematics (taught for use) or mathematics-for-engineers (taught for understanding)? They produce different volumes.

### Settled 2026-04-26

Volume II teaches **engineering mathematics**: mathematics as a language of models, constraints, change, uncertainty, and computation. Understanding is required, but the standard is usable power rather than disciplinary mathematical completeness.

## 9. Depth of physics, chemistry, biology  (load-bearing)

Volumes III-VI are physics, chemistry, biology. Are these taught at a working-engineer's depth, or to the depth of a science undergraduate? The page budget cannot do both.

### Settled 2026-04-26

Volumes III-VI are taught at **working-engineer depth**, not science-undergraduate depth. They go deep where engineering judgment requires depth, but they do not try to reproduce a full physics, chemistry, biology, or computer science degree inside the book.

Implication: the standard is not "could pass every undergraduate science exam." The standard is "can model, design, diagnose, and responsibly intervene in systems that depend on these sciences."

The sciences are taught as:

| Domain | Depth standard |
| --- | --- |
| Physics | enough to model forces, fields, energy, fluids, heat, waves, materials, signals, and machines |
| Chemistry | enough to reason about reactions, materials, corrosion, combustion, batteries, polymers, process systems |
| Biology | enough to understand living systems as self-maintaining, adaptive, evolved, failure-prone systems |
| Computer science | enough to build and reason about algorithms, software systems, hardware, networks, simulation, AI, and information flow |

So: **engineering depth, not disciplinary completeness**.

## 10. Social science

Where does the social science live? Risk perception, organisations, regulation, behavioural economics. They are real engineering inputs but they are not in the twelve volumes.

### Settled 2026-04-26

Social science lives primarily in Volumes IX-XII: systems, failure, design, and civilization. Risk perception, organisations, regulation, economics, institutions, procurement, incentives, and public trust are treated as engineering inputs, not decorative context.

# Structure of the twelve volumes

## 11. Number of chapters per volume

Is "12 chapters per volume" the right floor, or do II Form and VII Information deserve 18-20 while I Quantity deserves 8?

### Settled 2026-04-26

Twelve chapters per volume is a useful default, not a rule. Shorter foundational volumes may have 8-10 chapters; dense volumes such as Form, Information, Systems, and Failure may require 16-20.

## 12. Chapter length

Fixed chapter length, or variable? A 250-page chapter is not a chapter; a 30-page chapter is not full-weight. What is the band?

### Settled 2026-04-26

A normal chapter should fall between **60 and 140 pages**, with around **90 pages** as the default. Anything much longer should be split; anything much shorter should be treated as an interlude, appendix, or section.

## 13. Appendices

Per-volume appendices, or one master appendix? Doxonomics has one master.

### Settled 2026-04-26

Each volume gets its own technical appendices, while the full project also has a master appendix for notation, units, constants, standards literacy, glossary, and cross-domain reference tables. Local appendices serve the chapter; the master appendix serves the whole work.

## 14. Interludes

Interludes between volumes, like the part-interludes in Doxonomics? They are short, they bridge the arc, they may be the only place lyric prose belongs.

### Settled 2026-04-26

There should be short interludes between volumes. They bridge the intellectual arc, summarize what has changed in the reader's model of the world, and prepare the next domain without carrying heavy technical content.

## 15. Single-pass or return text

Is the book read once, or designed for return visits? A single-pass reference and a return-to-it text are structurally different.

### Settled 2026-04-26

The book is designed for a sequential first reading and later return visits. Its first duty is formation; its second duty is reference.

# Pedagogy

## 16. Exercise type

What does a typical exercise look like? Numerical answer, multi-page derivation, open-ended design, all of the above?

### Settled 2026-04-26

Exercises include numerical calculation, derivation, estimation, simulation, design, diagnosis, reverse engineering, failure analysis, and open-ended judgment. The exercise system should teach both correctness and engineering taste.

## 17. Solutions

Are solutions provided? Full, hints-only, half, none? Each choice tells the reader what kind of book this is.

### Settled 2026-04-26

Full solutions are provided for core problems; hints are provided for larger design problems; open-ended projects receive rubrics rather than single answers. The book should help the solitary reader recover from mistakes without making the problems toothless.

## 18. Number of problems

The chat suggests ~5,000 archetypal problems. Is that the target? It implies ~35 per chapter. Confirm or revise.

### Settled 2026-04-26

The target is approximately **5,000 problems**, with a working range of **4,800-5,500**. Most chapters should contain 25-40 problems, adjusted by difficulty and project density.

## 19. Project density

Project density: are there projects per chapter, per volume, or one per volume plus one final capstone?

### Settled 2026-04-26

Each chapter should have at least one small applied task, each volume should have one substantial project, and the full sequence should contain several cumulative design studios plus a final capstone. Projects are not ornamental; they are where the reader becomes answerable to reality.

## 20. Estimation exercises

Estimation as a recurring exercise type. The chat lists "estimate before calculating" as the first hidden-curriculum instinct. Is there a dedicated estimation environment that recurs across volumes?

### Settled 2026-04-26

Estimation is a recurring formal environment in every chapter. The reader should repeatedly estimate before calculating, then compare estimate, model, simulation, and measured result.

# Voice and register

## 21. Voice  (load-bearing)

Authorial "we", implied single author, invisible narrator, or first-person "I"? The book's identity sits here.

### Settled 2026-04-26

The voice is **authorial "we"**, with an implied single guiding intelligence rather than a faceless committee or first-person memoirist. The register is **formal-narrative**: rigorous, sequential, technically serious, but allowed to think aloud, bridge domains, and occasionally become memorable.

Implication: not MIT-problem-set dryness, not pop-science chat, not manifesto. More like a disciplined guide walking the reader through reality's operating manual.

Use:

> "We begin with measurement."

Not:

> "I will show you..."

And not:

> "The student should observe..."

This matters because the book is too large to survive without companionship. The reader needs a narrator, not just a syllabus.

## 22. Register

Formal-academic (MIT textbook register) or formal-narrative (Feynman, Wheeler, Polya register)? The chat's prose is closer to the latter; the Doxonomics archetype is closer to the former.

### Settled 2026-04-26

The register is **formal-narrative**: rigorous enough for technical seriousness, readable enough for sequential adult study. The model is closer to Feynman, Polya, Wheeler, and a good engineering mentor than to a dry course packet.

## 23. Historical personalities

Are historical engineering personalities named (Archimedes, Maxwell, Shannon, Brunel, Levin), or kept impersonal?

### Settled 2026-04-26

Historical figures are named when they clarify a mechanism, invention, controversy, failure, or conceptual turn. The book avoids hero worship; people appear as part of the development of tools, institutions, models, and mistakes.

## 24. Lyric prose

How much rhetorical lyric is permitted inside the chapters, vs. confined to frontmatter and book-openings? The cover's "lifting, joining, heating, flowing..." is lyric. Is that allowed in-chapter or only in the bridges?

### Settled 2026-04-26

Lyric prose is permitted in openings, interludes, transitions, and closing passages, but it must not replace proof, derivation, measurement, or design reasoning. Inside technical chapters, lyric language should sharpen memory, not decorate weakness.

# Correctness and verifiability

## 25. Technical correctness

How does the book guarantee technical correctness across 20K pages? Per-volume external review, per-chapter, per-claim?

### Settled 2026-04-26

The project requires domain reviewers for each volume, technical reviewers for chapters, computational verification for numerical examples, and a public errata process. Every worked example should be reproducible, and every table should have provenance.

## 26. Citation discipline

Citation discipline: when is a primary source required, when is a classical handbook adequate, when is a working benchmark or tertiary explainer permitted?

### Settled 2026-04-26

Primary sources are required for standards, laws, regulations, accidents, historical claims, and empirical performance claims. Classical handbooks and established textbooks are acceptable for settled technical material; tertiary explainers may guide pedagogy but may not support load-bearing claims.

## 27. Hedging

When does the book hedge? "Engineering consensus is X" vs. "X is the case" vs. "the textbook simplification is X but practitioners know Y." What is the default?

### Settled 2026-04-26

The book distinguishes physical law, model assumption, engineering convention, empirical regularity, professional consensus, and field practice. The default wording should make assumptions explicit without drowning the reader in caveats.

## 28. Aging empirical claims

The book makes empirical claims (cost, scale, performance, failure rates) that age. Is there an explicit "values current as of YYYY" convention?

### Settled 2026-04-26

All empirical, commercial, regulatory, cost, performance, and software-specific claims receive an explicit "current as of YYYY" convention. Fast-aging material is tagged and preferentially moved to companion notes when possible.

# Failure as first-class

## 29. Failure throughout the book

Volume X is on Failure. Does failure also appear, in microcosm, in every other volume? (e.g., a failure section per chapter)

### Settled 2026-04-26

Failure appears in every volume and every major chapter, not only in Volume X. Each chapter should ask: how does this model fail, how does this material fail, how does this system fail, and how does the engineer notice in time?

## 30. Named accidents

Are real industrial accidents named (Bhopal, Chernobyl, Boeing 737 MAX, Therac-25, Tacoma Narrows, Genoa Morandi Bridge), with their political contexts, or anonymised?

### Settled 2026-04-26

Real industrial, infrastructural, medical, aerospace, software, and environmental accidents are named and studied with their technical, organisational, regulatory, and political contexts. Public failures should not be anonymised when the record is available and sourceable.

## 31. Software failure

Is software failure treated at the same depth as physical failure? The Mars Climate Orbiter, Patriot timing bug, Knight Capital, Boeing MCAS are software-engineering case studies. Are they Volume X, Volume VII, or both?

### Settled 2026-04-26

Software failure is treated at the same seriousness as physical failure. Technical mechanisms belong in the information/software volume; system-level, organisational, safety, and governance lessons recur in the failure and civilization volumes.

# Originality vs synthesis

## 32. Original argumentation

The book is largely synthesis from existing canon. How much original argumentation is permitted? Is there a Piatra-Institute thesis ("engineering as the disciplined continuation of primitive acts" is one), and how load-bearing is it?

### Settled 2026-04-26

Original argumentation is permitted at the level of synthesis, framing, sequence, and cross-domain interpretation. Technical claims must remain grounded in established science, engineering practice, standards, and reproducible reasoning.

## 33. Contrarian positions

Are there places where the book takes a contrarian position? (e.g., that modern engineering pedagogy over-emphasises optimisation and under-emphasises maintenance, or that systems thinking has been hollowed out into platitude.)

### Settled 2026-04-26

Contrarian positions are allowed when they are explicitly argued and evidenced. Likely recurring arguments include: maintenance is under-taught, optimisation is over-glorified, systems thinking is often diluted into slogans, and engineering education hides too much institutional reality.

## 34. Volume XII: Civilization

Is "civilization" Volume XII a synthesis of the previous eleven, or a substantively new domain (urban planning, climate engineering, planetary systems)? Either is defensible; they produce very different books.

### Settled 2026-04-26

Volume XII is both synthesis and a substantive domain. It covers infrastructure, cities, climate systems, public works, logistics, regulation, procurement, standards, institutional capacity, maintenance, and the political economy of engineered life.

## 35. Thesis  (load-bearing)

Beyond "here is engineering," does the book have a thesis the way Doxonomics has one? If yes, what is it, in one sentence?

### Settled 2026-04-26

> Engineering is the discipline by which measured reality becomes reliable intervention under constraint, failure, scale, and responsibility.

Expanded version:

> Engineering begins when humans measure the world, continues when they model its constraints, becomes serious when they build systems that must survive contact with reality, and becomes civilization-scale when those systems reshape the conditions under which other people live.

Implication: this book is not merely "all engineering knowledge." It has an argument:

> Engineering is not applied science.
> Engineering is disciplined intervention.

Science asks: **what is true?**
Engineering asks: **what can be made to work, for whom, under what constraints, for how long, and at what cost if it fails?**

That distinction quietly governs all twelve volumes.

# Cross-domain bridges

## 36. Repeated derivations

Should the book repeat parallel derivations across domains (the same conservation argument applied to mass, charge, momentum, information, in adjacent chapters), or teach the abstraction once and trust the reader?

### Settled 2026-04-26

Parallel derivations should be repeated early across domains until the abstraction becomes natural. Later chapters may refer back to the shared structure, but the reader must first feel the analogy in mass, charge, momentum, heat, information, and population.

## 37. Problem archetypes

Are problem archetypes (balance, transport, stability, optimisation, scaling, failure, control, interface, uncertainty, ethics) a theorem-style environment that recurs across volumes, or just a one-time chapter heading?

### Settled 2026-04-26

Problem archetypes are a recurring formal environment, not a one-time chapter. Balance, transport, stability, optimisation, scaling, failure, control, interface, uncertainty, and ethics should reappear across the entire work as named patterns.

## 38. Biology and information

Does the book treat biology and information as different from physics-and-chemistry, or as more of the same? The chat suggests "engineering's encounter with self-organising matter" for Life: that frame is unusual and load-bearing.

### Settled 2026-04-26

Biology and information are treated as genuinely distinctive domains, while still connected to physics, chemistry, and mathematics. Life is framed as self-maintaining, evolved, adaptive matter; information is framed as structure, representation, control, and constraint.

# Materials and execution practicalities

## 39. Workshop access

The reader needs a workshop, a soldering iron, a 3D printer. What about a reader who can't access those? Is there a virtual or simulation-only track?

### Settled 2026-04-26

The book has two practical tracks: a physical track and a simulation/household track. A reader with no workshop should still be able to progress through measurement, modelling, coding, simulation, reverse engineering, and low-cost experiments.

## 40. Paper or digital

Is this paper-publishable? At 20K pages, the physical artifact is twelve volumes. Is that intended, or is this primarily a digital object that occasionally prints?

### Settled 2026-04-26

The project is digital-first and paper-compatible. The canonical form is modular PDF/HTML, while the print form is a multi-volume edition rather than a single physical object.

## 41. Companion website

Does the project need a companion website, errata system, online community? Or is it a sealed text?

### Settled 2026-04-26

A companion website is necessary. It should host errata, datasets, code, simulations, problem files, project templates, updates, reviewer notes, and possibly reading-group infrastructure.

## 42. Licensing

What is the licensing position: all rights reserved, Creative Commons, copyleft? The choice shapes who reads it and how.

### Settled 2026-04-26

The main text should use a Creative Commons license, preferably **CC BY-NC-SA** for the first edition unless a stronger open-access strategy is chosen later. Code should use a permissive software license such as MIT or Apache 2.0; datasets should be as open as legally possible.

### Settled 2026-04-28 (confirms Q53)

Confirmed: prose under **CC BY-NC-SA 4.0**; code under **MIT** (with Apache 2.0 acceptable for repositories where Apache's patent grant is desirable); datasets under **CC0** by default and **CC BY 4.0** when attribution is required by the upstream source. License files live at the project root and at each companion repository's root. The book's preface and the companion website both state the license posture in the reader-facing language.

# Aging and shelf life

## 43. Half-life tagging

The chat names a 30-year horizon. Some material ages in months (specific software stacks, current AI), some in decades (Maxwell's equations). Is there explicit half-life tagging per chapter?

### Settled 2026-04-26

Chapters and sections should carry implicit or explicit half-life categories: foundational, durable, medium-life, and fast-aging. Maxwell's equations and conservation laws age differently from AI tooling, chip availability, regulations, or commercial software.

## 44. Fast-aging omissions

Are there content categories deliberately omitted because they age too fast (specific microcontroller pinouts, current commercial CAD packages, the latest LLM)? Where is the line?

### Settled 2026-04-26

Fast-aging specifics should usually be excluded from the main narrative unless they are historically or conceptually important. Current tools, software versions, product names, microcontroller pinouts, and frontier AI details belong in companion notes rather than the permanent spine.

## 45. Second edition

Is there a planned second-edition mechanism, or is the first edition meant to be the last?

### Settled 2026-04-26

The project should have a planned update mechanism from the beginning. Minor corrections and companion updates happen continuously; major editions should be issued on a five-year cycle.

# Ethics and responsibility

## 46. What engineering is for

The book ends with "discipline becomes civilization," an ethical claim. How explicit is the book about what engineering is for and what it should not be for?

### Settled 2026-04-26

The book is explicit that engineering is for reliable, responsible intervention in the world. It does not pretend that building is morally neutral; engineered systems allocate risk, power, convenience, cost, and harm.

## 47. Dual-use and harmful work

What is the position on dual-use, military, surveillance, and environmental-harm work? Mentioned as case study, taught as professional dilemma, or treated as outside scope?

### Settled 2026-04-26

Military, surveillance, dual-use, environmental-harm, and coercive technologies are treated as professional and civilizational dilemmas. The book may analyze them as case studies, but it does not become an operational manual for harm.

## 48. Professional ethics

Is there an explicit professional-ethics chapter or book section? Codes, whistleblowing, the duty to report?

### Settled 2026-04-26

There should be explicit professional ethics coverage: codes, duty of care, public safety, whistleblowing, conflicts of interest, certification, maintenance obligations, and the duty to report known danger. Ethics also recurs throughout technical chapters where design choices create risk.

## 49. Engineering as political

Does the book address engineering-as-political (who chooses which infrastructure gets built, who pays, who is displaced)? Volumes IX, X, XI, XII all touch this; one of them needs to own it.

### Settled 2026-04-26

Volume XII owns engineering-as-political, with support from Volumes IX-XI. It covers who chooses infrastructure, who pays, who benefits, who is displaced, who maintains it, who is blamed when it fails, and who gets to call the result progress.

# Authorship and sustainability

## 50. Authorship

Who is the author? A single named person, a Piatra-Institute project, a coalition with named domain-leads? At 20K pages this is decades of work; the team model determines everything else.

### Settled 2026-04-26

The project is a **Piatra Institute work with a single general editor and named domain leads**. The general editor preserves sequence, thesis, voice, and architecture; domain leads and reviewers preserve correctness.

# Phase 0.6 / Phase 1 settlements

## 51. Reader-path model

The book is roughly 18,400 pages. A first-pass reader cannot traverse it linearly without a structural device that says which sections are required, which are working-engineer default, and which are optional. We need three paths and a tagging convention.

### Settled 2026-04-28

Three reader paths, tagged at section level (not paragraph level):

- **core**: the spine. The minimum a reader must touch to call the book read. Worked examples, central derivations, project, failure section, and the chapter's structural argument.
- **standard**: working-engineer depth. The chapter's actual argument and apparatus. Default register; what the chapter is really about.
- **mastery**: optional advanced material. Inline boxes, deeper derivations, edge cases, research-adjacent topics. A reader may skip every mastery box without losing the thread.

Tagging is applied via `\pathtag{core|standard|mastery}` immediately after a section heading. Inline mastery boxes use `\begin{mastery} ... \end{mastery}`. The default for an unmarked section is `standard`. The reader-path declaration appears in `frontmatter/how-to-use.tex`; per-volume openers may restate the path-budget.

## 52. Pilot chapter

The diagnostic recommends Volume I Chapter 1 ("Why we measure") as the production-standard pilot.

### Settled 2026-04-28

The pilot is **Volume I Chapter 1, "Why we measure."** The general editor writes the first draft; one technical reviewer (measurement and metrology) and one pedagogical reviewer pass it through `reviewer-guide.md` before any second chapter is started. The pilot sets the standard for voice, citation discipline, estimation environments, archetype invocations, exercise design, project rubric, and reader-path tagging.

## 55. Per-chapter project track

Every chapter has `Project track: TBD` in its `\chapmeta`. Resolving Q55 across all 174 chapters is a Phase 0.7 editorial pass. Q55-pilot resolves it for the pilot chapter only.

### Settled 2026-04-28 (Q55-pilot)

Vol I Ch 1 project track: **household + analysis (hybrid)**. Hazard class: **none**. Tools: scale, thermometer, stopwatch, ruler, smartphone (sensors and stopwatch app). Artifact: a one-week measurement logbook with explicit error bars on every quantity, plus a 1500-word reflection on which quantities were stable, which drifted, and which the reader could not measure with the tools available. Solutions take the form of a published reference logbook from the general editor, not a single answer key.

### Settled 2026-04-28 (Q55-ch02)

Vol I Ch 2 project track: **analysis** (paper/pencil only, no instruments). Hazard class: **none**. Tools: paper, pencil, calculator, and an optional plotting environment for the Buckingham pi exercises that benefit from a graph. Artifact: five physical relationships derived using only dimensional analysis (e.g., pendulum period, drag on a sphere, heat-conduction time scale, free-fall time, capillary rise), each presented with explicit dimensional balance, the dimensionless groups identified, and a check against the published functional form. Solutions take the form of a published reference set of derivations from the general editor.

### Settled 2026-04-28 (Q55-ch03)

Vol I Ch 3 project track: **analysis** with an optional household component. Hazard class: **none**. Tools: paper, pencil, internet research access for standards documents and manufacturer calibration certificates, and one household measuring instrument of the reader's choice. Artifact: a traceability-chain document for one measurement in the reader's life (a bathroom scale, a kitchen thermometer, a smartphone clock, a GPS coordinate, a workplace instrument, or equivalent), tracing the chain from the reader's instrument through working standard, secondary standard, primary standard, to the SI defining constant. Each link in the chain is documented with sources (calibration certificate where available; standards-body publications; manufacturer documentation). The deliverable is a 1500-word document with the chain explicit, gaps in the chain named, and a reflection on what would change in the reader's confidence in the measurement if any link failed.

The remaining 171 chapters' project-track resolution is deferred to Phase 0.7.

# How to use this file

When a settled answer needs to be revised, do not delete the previous Settled block. Add a new Settled block beneath it, dated, with the new wording and a brief note on why the change was needed. The history is part of the document.

A new question that arises during writing is appended to the end of its appropriate section, numbered 51 onward, with the same Settled-block convention. The convention does not lock the document at fifty.

The five questions originally flagged **(load-bearing)** were the ones whose answers constrain everything else. Their flags are preserved as a historical signal: when a new question's answer would conflict with question 1, 6, 9, 21, or 35, the new question is the one that gives way unless the load-bearing answer is itself revised.
