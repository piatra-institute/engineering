# Engineering: project status

Last updated: 2026-04-29.

## Phase

**Phase 0.7: registry foundation and pilot prose.** In progress as of 2026-04-29. Includes:

- Volume I prose: all nine chapters at Stage 5 (Ch 1 "Why we measure", Ch 2 "Units and dimensions", Ch 3 "Calibration and traceability", Ch 4 "Error and uncertainty", Ch 5 "Sensors and instruments", Ch 6 "Time, frequency, and signals", Ch 7 "Length, area, volume, mass", Ch 8 "Statistics for engineers", Ch 9 "The discipline of estimation") with Codex reviews resolved across the full volume (~280 specific fixes applied). Volume I opener prose written; archetype list lists six Volume I archetypes (scaling, balance, failure, uncertainty, interface, transport). Citation policy now includes a `method:` prefix for research-methods literature (replication studies, p-hacking, HARKing, forking paths).
- Named-cases registry: schema (`docs/research/accidents/SCHEMA.md`); fifteen entries on disk (every accident cited in any Volume I chapter plus the original twelve foundation entries); index (`docs/research/accidents/README.md`); citation-policy update with closest-equivalent clause; reviewer-guide registry-check requirement (items 24-27); `make accidents` target with both cite-resolution and prose-name scan.
- Audit tooling: `make audit-docs` (stale references), `make accidents` (named-case discipline), `make exercise-counts` (per-chapter exercise count vs chapmeta target). All pass across the current state.

Phase 0.6 (curriculum expansion). Complete on 2026-04-28. Closed eleven substantive curriculum gaps (acoustics, mass transfer, plasma physics, bioinformatics, quantum computing, power electronics, MEMS, project management, user research, defence systems, space infrastructure) plus four naming/register fixes and the explicit stigmergy hook in Vol IX.

Previous phase: **Phase 0.5** (structural hardening). Complete on 2026-04-28.
Earlier phase: **Phase 0** (scaffolding + outline). Complete on 2026-04-26.

Next phase: **Phase 1** (production prose at scale, after Phase 0.7 completes).

## At a glance

| Metric | Count |
| --- | --- |
| Volumes | 12 |
| Chapter shells | 174 |
| Per-volume dossiers | 12 |
| `\chapmeta` blocks in chapter shells | 174 |
| Half-life: TBD remaining | 0 |
| TODO markers in TeX | ~1850 |
| Empty epigraphs in chapter shells | 174 |
| Section headings in chapter shells | ~1640 |
| Bibliography entries | 34 |
| `main.pdf` page count (last build) | ~696 |

Run `make stats` for the live numbers.

## What is complete

- Twelve-volume LaTeX project skeleton (`main.tex`, `preamble.tex`, `eng-macros.sty`).
- Frontmatter prose: cover, title page, preface, how-to-use, notation. All in authorial "we" voice.
- 174 chapter shells, generated from `scripts/generate_scaffolding.py`, with dossier-derived metadata in a `\chapmeta` block (half-life, archetypes, exercise target).
- 12 per-volume research dossiers under `docs/research/`, each with chapter-level scope, archetype, project, exercise count.
- Cross-volume landscape document at `docs/research/landscape.md`. Per-volume header dossiers at `docs/research/<NN>-<slug>/_volume.md`. Per-chapter dossiers at `docs/research/<NN>-<slug>/ch<MM>-<slug>.md` (174 total, mirroring the `volumes/` tree).
- Editorial decisions log at `docs/editorial-decisions.md` (50 settled questions; thesis pinned at top).
- Voice guide at `docs/voice.md`.
- Open questions log at `docs/open-questions.md` (Q51-Q56 active).
- Project diagnostic at `docs/diagnostic.md` (Codex, 2026-04-28).
- Interludes catalogue at `docs/interludes.md` (queued III-IV and IV-V revisions).
- Citation policy at `docs/citation-policy.md`.
- Case-study template at `docs/case-study-template.md`.
- Reviewer guide at `docs/reviewer-guide.md`.
- Release checklist at `docs/release-checklist.md`.
- Research pipeline at `docs/research-pipeline.md`.
- Build pipeline: `make`, `make watch`, `make scaffolding`, `make outline`, `make strict`, `make check`, `make stats`, `make clean`, `make distclean`.
- A working PDF build, currently around 696 pages including all nine Volume I chapters at Stage 5. Volume I prose is complete and reviewed.
- Post-expansion drift cleanup (2026-04-28): all eight expanded volumes' arc paragraphs and editorial-question chapter numbers refreshed to match the 174-chapter sequence; status, research-pipeline, landscape, generator comments, Makefile `outline`, and appD-reading-list paths updated; README anchor numbering fixed; new `make audit-docs` target enforces the cleanup.

## What is queued

Active items from `open-questions.md`:

- **Q51 reader-path model** (core / standard / mastery): not yet decided.
- **Q52 pilot chapter** (Volume I Chapter 1): not yet started; named as the next major editorial move.
- **Q53 license confirmation** (CC BY-NC-SA + MIT/Apache 2.0): tentative; requires explicit user confirmation.
- **Q54 companion-note architecture**: spine vs companion-notes vs code repo vs data repo vs errata: not yet decided.
- **Q55 per-chapter project track**: every chapter currently has `Project track: TBD`. Editorial pass needed, ideally per volume.
- **Q56 named-cases registry**: accident registry under `docs/research/accidents/` not yet created.

Queued from `interludes.md`:

- III → IV revision (Force into Energy) acknowledging the Force/Energy/Matter unity. Status: queued, not applied.
- IV → V revision (Energy into Matter) closing the unity. Status: queued, not applied.

## Risks

The diagnostic identified three top risks (`docs/diagnostic.md`). Phase 0.5 mitigates the first; the others remain.

1. **Source-of-truth drift between generator and dossiers.** **Mitigated.** The generator now reads dossiers as the canonical source of per-chapter metadata; `make check` enforces that every chapter shell carries a `\chapmeta` block.
2. **Scale honesty for the reader.** **Open.** Q51 (reader-path model) is the planned remediation.
3. **Verification (citation discipline, reproducible examples, table provenance).** **Partially mitigated.** Citation policy and case-study template now exist as documents. Bibliography category structure is scaffolded. Per-claim verification will land alongside prose.

## Build state

The current build runs cleanly:

```
make distclean && make
```

Produces `main.pdf` at approximately 696 pages. `make check`, `make audit-docs`, `make accidents`, and `make exercise-counts` all report `PASS`. `make stats` reports the at-a-glance counts above.

## Operational notes

- `main.pdf` is gitignored; build locally.
- Scaffolding regeneration via `make scaffolding` (uses uv).
- The dossiers under `docs/research/` are the canonical per-volume editorial source. The generator reads them. Edit dossiers there; do not edit chapter shells directly until prose work begins.
- File slugs (`volumes/01-quantity/`, `_volume.tex`, `chNN-slug/chapter.tex`, `\label{vol01:ch01}`) are stable and not renamed.

## What good progress looks like

A serious-pace next pass would:

1. Pick the pilot chapter (Volume I Chapter 1).
2. Land Q51 (reader-path model) and Q53 (license confirmation) in the same week.
3. Apply the queued III-IV and IV-V interlude revisions or explicitly leave them as Phase-1 work.
4. Begin the named-cases registry (Q56) with at least 10 entries.
5. Run the pilot through the reviewer-guide protocol before scaling.

The pilot is the gating decision. Until one chapter has been carried end-to-end at production standard, the rest of the project remains structural.
