# Research seeds: schema

This file defines the format every entry under `docs/research/seeds/` must take.

A seed is a captured thinking pass. It is the place where an idea, a framing, a quotable sentence, or a half-formed observation from external reading is distilled into a self-contained note, *after the source has been read and set aside*. A seed is neither finished research nor canon. Seeds are not cited from chapter prose. When a seed makes it into the book, the chapter cites the underlying source (per `docs/citation-policy.md`); the seed stays in place as genealogy.

Seeds differ from chapter dossiers (which carry the outline of a specific chapter) and from accident registry entries (which are the canonical record of a specific named event). A dossier is structural; an accident entry is factual; a seed is conceptual. Many seeds bear on more than one chapter; some bear on a whole volume; a few bear on the project as a whole.

## Filename convention

Entries live at `docs/research/seeds/<slug>.md`, where `<slug>` is the seed's idea in kebab-case, declarative, not a question. The slug names the claim the seed carries, not the source it came from.

Good: `freud-published-his-failures.md`, `failure-is-the-engine-of-design-knowledge.md`, `the-normalisation-of-deviance.md`.

Bad: `mcgowan-notes.md` (names the source, not the claim), `interesting-failure-ideas.md` (not a claim), `seed-001.md` (not searchable).

## Required structure

Every seed has YAML frontmatter followed by five required sections.

### Frontmatter

```
---
name: <kebab-case slug, matching the filename>
scope: <project | vol-NN>
status: <placeholder | provisional | integrated>
created: <YYYY-MM-DD>
anchor_texts:
  - <bibkey or placeholder>: <one-line note on what this text contributes>
sister_seeds:
  - <other-seed-slug>
cross_refs:
  - vol<NN>:ch<MM>
  - acc:<slug>-<year>
  - <decision-number>
---
```

Field notes:

- `name`: the seed's slug. Same as the filename without `.md`. Lowercase, kebab-case.
- `scope`: `project` for a seed that bears on the book as a whole; `vol-NN` (e.g., `vol-10`) for a seed that bears on a single volume. A seed that bears on two volumes is project-scope or is split into two seeds. Do not list multiple volumes.
- `status`: `placeholder` (idea captured; anchor texts not yet pinned to bibliography keys), `provisional` (anchor texts pinned to bibkeys; bibliography entries may still be missing), `integrated` (anchor texts present in `bibliography/references.bib` with page pins; seed referenced in at least one chapter dossier).
- `created`: ISO date the seed was first written, not the date of last edit.
- `anchor_texts`: the texts that ground the seed. A YAML list of one-line entries, each beginning with a bibkey (per the prefix conventions in `docs/citation-policy.md`) or a placeholder of the form `<prefix>:<author>-tba` when the source is known by name but the entry has not been added to the bibliography yet. The one-line note states what each text contributes, not what it argues in general.
- `sister_seeds`: other seeds the present seed builds on or talks back to. Empty list `[]` is allowed and common, especially for early seeds. The first seed in a chain has none.
- `cross_refs`: the dossiers, accident entries, and editorial decisions the seed bears on. Volumes and chapters use `vol<NN>:ch<MM>`; accident registry entries use the `acc:<slug>-<year>` form (the registry key, not a bibkey); editorial decisions use the decision number in the form `Q<N>` to match the shorthand already used in `CLAUDE.md`.

### Body

Five required sections, in this order:

1. **`# <Title>`**: H1. Declarative phrasing of the claim the seed carries (e.g., "Freud only published his failures"). The title and the slug carry the same claim; the title is the readable form.

2. **`## The claim`**: one paragraph. The seed distilled to a single breath. A reader who reads only this paragraph should be able to act on the seed.

3. **`## Why it matters here`**: one to three paragraphs. The engineering-side stakes. What chapter or argument the seed would feed; what the seed authorises a chapter writer to say; what it disqualifies.

4. **`## Sources and quotable sentences`**: bullets. Each quoted sentence is preserved verbatim with its bibkey and pin (page, section, or timestamp) once known. If a source is known by name but not yet pinned, mark the entry explicitly and tag the seed `status: placeholder`. Quotable sentences are the seed's main external load-bearing material; treat them as the primary asset.

5. **`## Sister seeds and cross-references`**: one or two paragraphs. Narrative prose linking to other seeds (using `[[seed-slug]]` syntax; the link is informational only, no linker is required), to chapter dossiers, to accident entries, and to editorial decisions. The paragraph states what each linked target receives from this seed, not just that it is related.

6. **`## Source disposal`**: one line. Stating that the originating chat, page, conversation, or passage has been captured into the seed file and that the source no longer needs to be re-read to use the seed. This is the seed's discipline: a seed that still requires the reader to go back to the source is not yet a seed.

## What seeds do not contain

- Citations from chapter prose. Seeds are dossier-side; chapter `\cite{...}` keys point at the bibliography, not at seeds.
- Em-dashes (per `docs/voice.md`).
- AI-tic vocabulary (per `docs/voice.md`).
- Self-announcing topic sentences ("This seed will examine...").
- Material that belongs in a chapter dossier (outline, sub-section breakdown, exercise count). If a seed starts becoming a chapter outline, split it: the outline material goes into the chapter dossier, the framing claim stays in the seed.
- Material that belongs in the accident registry (named-event mechanism, organisational analysis, citation keys). If a seed starts becoming an accident write-up, the accident entry is the destination; the seed retains only the framing claim, if any.

## Status transitions

A seed is created at `placeholder`. The author has the claim; the sources are named but not pinned to bibliography keys, or the bibliography entries do not yet exist. The seed is usable for editorial reasoning; it is not yet usable for chapter prose citation.

A seed moves to `provisional` when every anchor text in the frontmatter is pinned to a real bibkey (the bibliography entry may still need to be added, but the key is settled and the source is in hand) and every quotable sentence has a page or section pin.

A seed moves to `integrated` when every anchor text is present in `bibliography/references.bib` with full entry data, and the seed has been referenced in at least one chapter dossier's "Sources and seeds" section. Integration does not mean the seed has appeared in chapter prose; it means the seed has been wired into the project's research lane and is available to writers.

## Index

`docs/research/seeds/README.md` indexes every seed with its scope, status, created date, and a one-line summary. The index is regenerated by hand when seeds are added or upgraded; consistency with seed files is checked by reading.

No `make` target enforces the seeds lane at present. The discipline is editorial.
