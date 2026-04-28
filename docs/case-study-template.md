# Engineering: case-study template

This template defines the standard form for every named accident, failure, and case study in the book. It exists because, without a template, named cases become narrative gravity wells that crowd out the technical mechanisms they were meant to illustrate.

The diagnostic flagged this risk in Volume X (`docs/diagnostic.md`, "Volume X: Failure"). The template applies wherever a named case appears: not just in Volume X, but in every chapter's failure section that names a real event.

## When to use the template

A case study is required whenever the chapter:

- Names a specific accident, incident, outage, recall, or failure event.
- Discusses an organisational, regulatory, or political failure with a public record.
- Cites a primary investigation report.

A case study is *not* required for:

- Generic failure mechanisms ("fatigue cracking propagates from a stress concentration") with no specific event.
- Hypothetical scenarios used as worked examples.
- Industry-pattern observations across many events ("pipeline incidents tend to involve...") that draw on multiple cases without singling out one.

## The seven-section template

Every case study, regardless of which chapter it lives in, has these seven sections in this order:

### 1. Identification

- Event name (the canonical name used in primary literature).
- Date and time, with timezone if relevant.
- Location.
- Operator / responsible organisation.
- Domain (aerospace, infrastructure, software, medical, energy, environmental, etc.).
- One-line summary of what happened.

### 2. Timeline

- Pre-event conditions (what the system was doing before).
- Initiating event.
- Sequence of failures, with timestamps.
- Detection and response.
- Outcome.

The timeline is sourced from the primary investigation report. If two primary reports disagree, both versions are recorded with sources.

### 3. Technical mechanism

- The physical, chemical, biological, software, or systems mechanism that caused the failure.
- The model that the engineers were operating under.
- The way that model was wrong or incomplete.
- The signals that, in retrospect, indicated the failure was approaching.

This section is cross-referenced to the chapter's main technical content. The mechanism in the case must connect to the mechanism the chapter is teaching. If it does not, the case is in the wrong chapter.

### 4. Organisational mechanism

- The decisions made by individuals and groups that allowed the technical failure to develop.
- Production pressures, schedule pressures, financial pressures.
- Safety culture: where it functioned, where it broke down.
- Knowledge that was present somewhere in the organisation but did not reach the decision point.
- Whistleblower dynamics if relevant.

Drawn from the primary investigation report and at least one secondary source (Vaughan, Dekker, Perrow, Leveson, or domain-specific equivalents).

### 5. Regulatory and political context

- The regulator and its decisions or non-decisions.
- The certification or oversight regime.
- Industry-state relationships.
- Political pressures on the regulator.
- Legal aftermath.

This section is sometimes brief (when the regulatory context is uncontroversial) and sometimes the largest section (Boeing 737 MAX, Volkswagen, Therac-25 aftermath).

### 6. Missed signals and counterfactuals

- Signals that were available but ignored, dismissed, or rationalised.
- Near-misses that preceded the event.
- Counterfactuals: what specific intervention, at what specific point, with what specific information, could have prevented the event.
- Why those interventions did not happen.

This section is the bridge to the chapter's argument. It is where the engineering lesson lives.

### 7. Sources

- Primary investigation report(s) with citation key (`acc:...`).
- Regulatory and legal documents (`law:...`).
- Secondary scholarly analyses (`text:...` or `paper:...`).
- Independent journalism or institutional histories where relevant.
- Datasets if quantitative claims appear (`data:...`).

A case study with fewer than two primary or near-primary sources is not yet ready for the book. It moves to the named-cases registry pending sourcing.

## Lessons by scale

After the seven sections, every case study closes with a "Lessons" block organised by scale:

- **The part.** What the smallest failed component teaches the reader about that material, mechanism, or unit.
- **The machine.** What the artifact teaches about the design, manufacture, or operation of that machine.
- **The operator.** What human factors, training, mental model, or interface lessons the case carries.
- **The organisation.** What management, communication, prioritisation, or culture lessons apply.
- **The regulator.** What oversight, certification, or institutional lessons apply.
- **The civilization.** Where Volume XII applies: the political-economy lesson, the maintenance-burden lesson, the risk-allocation lesson.

Not every scale gets a substantive lesson in every case. Sometimes the part-level lesson is empty (Aloha 243's organisational lessons dwarf its part-level lessons; Mars Climate Orbiter's part-level lesson is "the unit was wrong" and the organisation-level lesson is much larger). But the writer must explicitly say "no lesson at this scale" rather than silently skip.

## Length budget

A typical case-study block is 4-12 pages of prose:

- Identification: 0.5 pages.
- Timeline: 1-2 pages.
- Technical mechanism: 1-3 pages.
- Organisational mechanism: 1-2 pages.
- Regulatory context: 0.5-2 pages.
- Missed signals and counterfactuals: 1-2 pages.
- Sources: bibliography entries (no page weight in the chapter; accumulated in `references.bib`).
- Lessons by scale: 0.5-1 pages.

Cases that need more than 12 pages either have multiple distinct mechanisms (Boeing 737 MAX has the MCAS mechanism plus the certification mechanism plus the legal mechanism) and should be split into linked subsections, or are being given more weight than they merit and should be trimmed.

## What case studies do not do

A case study is not:

- A retelling of a familiar story for narrative effect.
- A morality tale.
- A blame assignment.
- An opportunity to relitigate the writer's existing opinion of the organisation.
- A vehicle for claims unsupported by the primary record.

A case study that does any of these is rewritten or cut.

## The named-cases registry

Cases that are reused across multiple chapters live in a registry under `docs/research/accidents/`. Each registry entry holds:

- The full seven-section case study at one canonical location.
- Cross-references to chapters that cite it.
- Bibliography entries.
- Fact-check status (verified, in-progress, contested).

Chapters that reference a registered case use the abbreviated form: a one-paragraph summary plus pointers to the registry entry and the chapter sections that develop the relevant mechanism. The full seven-section template appears once, in Volume X or in the registry, not redundantly.

The registry is not yet populated. Q56 in `open-questions.md` tracks its creation.

## Reviewer checklist for case studies

When a domain reviewer reads a chapter that contains a case study, the reviewer asks:

1. Is the technical mechanism described correctly per the primary report?
2. Are dates, places, and named actors accurate?
3. Is the organisational mechanism supported by the cited sources?
4. Is the regulatory context described correctly?
5. Is at least one counterfactual evidence-based, not invented?
6. Are all sources cited at the correct tier (primary for primary claims)?
7. Does the case connect to the chapter's main mechanism?

A case that fails any of these checks blocks the chapter's release.

## Forbidden cases

Cases where the available record is too thin for a seven-section treatment are not used in the book. Examples:

- Confidential or sealed accident reports without public summaries.
- Events where the operating organisation has actively suppressed the record and no independent reconstruction exists.
- Recent events whose investigation is incomplete (within 18 months of occurrence, typically).
- Events whose evidence base is dominated by speculation or social-media narrative.

The book waits. The discipline of the case study is also a discipline of patience.
