# Named-cases registry: schema

This file defines the format every entry under `docs/research/accidents/` must take. The schema is intentionally rigid. The discipline of the registry, and its usefulness to the chapter writers and reviewers who depend on it, rests on the rigidity.

A registry entry is the single canonical record of a named accident in this project. Chapters that mention the accident quote one of its short-form summaries verbatim, or paraphrase the technical mechanism here, and cite the registry's primary or closest-equivalent source. Chapters do not re-narrate the accident from memory or from textbook explanations. The registry is the source of truth.

## Filename convention

Entries live at `docs/research/accidents/<slug>-<year>.md`, where:

- `<slug>` is the canonical short name in kebab-case: `mars-climate-orbiter`, `tacoma-narrows`, `air-canada-143`, `therac-25`.
- `<year>` is `YYYY` for a single-year event or `YYYY-YYYY` for an event spanning multiple years.

Examples: `mars-climate-orbiter-1999.md`, `air-canada-143-1983.md`, `therac-25-1985-1987.md`.

## Required structure

Every entry has YAML frontmatter followed by six required sections, in this order. The sections are not optional; an entry that omits one is at status `placeholder`, not `verified`.

### Frontmatter

```
---
name: <Canonical name as readers know it>
year: <YYYY or YYYY-YYYY>
domain: <aerospace | civil | process | power | software | medical | environmental | other>
primary_source: <bibliography key, or "no single primary report; closest-equivalent: <key>">
secondary_sources: [<bibliography key>, <bibliography key>, ...]
short_form: <one-sentence canonical summary, used as drop-in across chapters>
status: <verified | provisional | placeholder>
---
```

Field notes:

- `name`: the form a chapter writer would use in prose. "Air Canada Flight 143" not "Gimli Glider"; "Therac-25" not "the Therac accidents." If the popular name differs from the canonical name, mention the popular name in the body, not the frontmatter.
- `year`: the year of the technical event, not the year of the report. Multi-year events use a range (Therac-25 is `1985-1987`).
- `domain`: one of the eight tags above. Tags map to volumes: aerospace primarily Vol IX-X, civil primarily Vol III-X-XII, process primarily Vol IV-V-X, power primarily Vol IV-IX-XII, software primarily Vol VII-X, medical primarily Vol VI-X, environmental primarily Vol V-XII, other for cases that do not fit (rare).
- `primary_source`: a single BibLaTeX key from `bibliography/references.bib`. If no single official investigation report exists, the value is `no single primary report; closest-equivalent: <key>` and the body must justify why no primary exists.
- `secondary_sources`: a YAML list of additional bibliography keys for independent analyses, peer-reviewed reconstructions, regulatory follow-up reports, scholarly histories. Empty list `[]` is allowed but unusual for a verified entry.
- `short_form`: one sentence, ~25-40 words. This is what chapters quote when they need a one-line summary. Engineering, not literary.
- `status`: `verified` (primary or closest-equivalent source confirmed, mechanism aligned with source, all required sections present), `provisional` (primary source identified but not fully read; gaps in mechanism), `placeholder` (entry exists for cross-referencing but content is stub).

### Body

Six required sections, in order:

1. **`# <Canonical name>, <year>`**: H1 title. Same as the frontmatter `name` plus the year.

2. **`## Date(s) and location`**: one paragraph. Specific date(s) of the event; specific location; specific operating conditions if relevant.

3. **`## Technical mechanism`**: one to three paragraphs. The canonical engineering description of what failed, how, and why. Sourced; every numerical claim or specific mechanism statement carries a parenthetical page or section pin to the primary source. This is the only place in the project where the mechanism is written; chapters quote `short_form` or paraphrase this section.

4. **`## Organisational / regulatory mechanism`**: one to three paragraphs. The non-technical mechanism: who decided what, what was overruled, what regulatory or institutional factors mattered, what cultural or contractual pressures contributed. Same sourcing discipline as the technical mechanism.

5. **`## Lessons by scale`**: bullet list. Each bullet names a chapter (volume number, chapter number, chapter title or slug) and the specific lesson that chapter draws from this case. The list is the registry's index of cross-chapter applications.

6. **`## Citation keys`**: explicit list of the keys that appear in the frontmatter, with one-line annotations. Example:
   - `acc:nasa-mco-mib`: primary; NASA Mishap Investigation Board Phase I Report, 1999.
   - `web:bipm-...`: secondary; institutional context.

7. **`## Short-form summaries`**: three to five drop-in summaries of different lengths (one sentence, two sentences, one paragraph). Each is a verbatim block a chapter may quote. Engineering register; no rhetoric.

8. **`## Provenance and verification`**: one paragraph. What sources were consulted, on what date, and what page or section pins support which claims. Date stamp at the end (`Verified: YYYY-MM-DD` or `Status: provisional, last reviewed YYYY-MM-DD`).

## What entries do not contain

- Speculation about what might have caused the accident beyond what the cited sources support.
- Narrative or literary framing. The body is engineering description and sourced fact.
- Cross-references to chapters that have not yet been written. Use `Lessons by scale` only to point at chapters where the case will be cited in the project's settled outline; do not invent new cross-references.
- Em-dashes (per `docs/voice.md`).
- Identifying details about specific individuals where the primary source does not name them and naming them is not load-bearing.
- Photographs, diagrams, or external assets. The registry is text; visual assets live with the chapters that use them.

## Status transitions

An entry is created at status `placeholder` (the chapter that needs it can cite the entry while it is being written). It moves to `provisional` when the primary or closest-equivalent source has been identified and the technical mechanism is at least one paragraph drawn from that source. It moves to `verified` when all six body sections are filled, every numerical claim has a page or section pin, the short-form summaries have been drafted, and the provenance section is dated.

A chapter prose review may downgrade an entry from `verified` to `provisional` if the reviewer finds a sourcing gap. The downgrade is recorded in the entry's provenance section, not deleted.

## Registry index

`docs/research/accidents/README.md` indexes every entry with its domain, year, status, and a one-line summary. The index is regenerated by hand when entries are added or upgraded; its consistency with the entries is checked by `make accidents` (which also verifies that every `\cite{acc:*}` key in chapter prose has a corresponding registry entry).
