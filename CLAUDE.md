# Engineering — Claude context

A ~18,400-page, twelve-volume formation text for serious adult learners. A Piatra Institute project. The book is `Engineering`; the twelve internal divisions are `Volumes`, not "books." This file gives a Claude Code session everything it needs to be productive without re-reading old conversation history.

## Thesis

> Engineering is the discipline by which measured reality becomes reliable intervention under constraint, failure, scale, and responsibility. Engineering is not applied science. Engineering is disciplined intervention.

Pinned at the top of `docs/editorial-decisions.md`. Every chapter sits under this sentence.

## Repository layout

```
.
├── main.tex                       Master document; \part{} per volume; \input{} per chapter.
├── preamble.tex                   memoir, biblatex, tikz, theorem environments, \chapmeta, \pathtag, mastery.
├── eng-macros.sty                 Cross-domain notation (\R, \E, \dd, \pdv, \engterm, \TODO, etc.).
├── Makefile                       Build (latexmk + uv).
├── pyproject.toml                 Python tooling (uv).
├── frontmatter/                   Cover, title page, preface, how-to-use, notation.
├── volumes/                       12 volumes; each chapter is its own folder.
│   └── NN-<vol-slug>/
│       ├── _volume.tex            Volume opener prose.
│       └── chMM-<chapter-slug>/
│           ├── chapter.tex        (figures/, code/, data/ accumulate here as prose lands)
│           └── ...
├── appendices/                    Master appendices.
├── bibliography/references.bib    BibLaTeX, organised by category-key prefix.
├── docs/                          Editorial planning. Not part of the book.
│   ├── editorial-decisions.md     50+ settled editorial questions. Read first.
│   ├── status.md                  Current phase, counts, what's complete.
│   ├── voice.md                   House voice rules and ban-list.
│   ├── citation-policy.md         BibLaTeX prefix conventions, citation tiers, closest-equivalent.
│   ├── case-study-template.md     Seven-section accident case standard.
│   ├── reviewer-guide.md          Three-role reviewer protocol; 44-item checklist.
│   ├── review-prompt.md           Reusable template for handing a chapter to Codex / a reviewer.
│   ├── release-checklist.md       Structural / build / citation / voice gates for release.
│   ├── research-pipeline.md       Six-stage outline-to-released pipeline.
│   ├── interludes.md              Volume-to-volume bridge prose.
│   ├── diagnostic.md              Project diagnostic (Codex, 2026-04-28).
│   ├── open-questions.md          Q51 onward.
│   ├── reviews/                   Per-chapter Codex reviews and their resolutions.
│   └── research/
│       ├── landscape.md           Cross-volume landscape, archetype index, page budget.
│       ├── NN-<vol-slug>/
│       │   ├── _volume.md         Per-volume dossier (scope, arc, bridges, reading list).
│       │   └── chMM-<slug>.md     Per-chapter dossier (174 total, mirrors volumes/ tree).
│       ├── accidents/             Named-cases registry (Q56).
│       │   ├── SCHEMA.md          Required structure for every entry.
│       │   ├── README.md          Index by domain.
│       │   └── <slug>-<year>.md   Twelve initial entries.
│       └── seeds/                 Research seeds: captured ideas / framings from external reading.
│           ├── SCHEMA.md          Required structure for every seed.
│           ├── README.md          Index by scope (project / volume).
│           └── <slug>.md          One per idea; declarative slug.
└── scripts/
    └── generate_scaffolding.py    uv-runnable scaffolding generator (reads dossiers).
```

`main.pdf` is gitignored. Build it locally.

## Build commands

```
make           # build main.pdf (first build ~30-60 s)
make watch     # auto-rebuild on file change
make strict    # halt-on-error (CI-style verification)
make check     # structural invariants (every chapter has chapter+label+chapmeta)
make stats     # counts of volumes, chapters, TODOs, sections, bibliography entries
make audit-docs    # flags stale references (163, ~465, book-NN, /Users/, /home/, ...)
make accidents     # verifies every \cite{acc:*} key in chapter prose has a registry entry
make scaffolding   # regenerate chapter shells from dossiers (uv run)
make outline       # concatenate all dossiers into docs/outline.md
make clean         # remove auxiliary files (now also *.bcf-SAVE-ERROR, *.bbl-SAVE-ERROR, *.synctex.gz)
make distclean     # remove main.pdf and rebuild trackers
```

The `audit-docs`, `accidents`, and `check` targets are the project's discipline guards. Run them after any non-trivial edit.

## House conventions

These are the patterns most often violated and the ones whose violation a reviewer will flag immediately. They override generic engineering-writing instincts.

### Voice (read `docs/voice.md` for the full ban-list)

- **Authorial "we."** Not "I," not "the student," not "one." Settled Q21.
- **No em-dashes** (no `---` in source, no `—` Unicode) outside primary-source quotations. The most violated rule. Use commas, periods, or rewrite.
- **No negate-first-then-pivot.** Bad: "X is not Y. It is Z." Good: state Z directly. State both halves positively if both halves are needed.
- **No AI-tic vocabulary.** Cut on sight: `fundamentally`, `essentially`, `in essence`, `at its core`, `in many ways`, `notably`, `interestingly`, `crucially`, `delve`, `tapestry`, `landscape` (as metaphor), `lens` (as in "through the lens of"), `nuanced`, `multifaceted`, `intricate web`, `unpack`, `leveraging`, `robust` (as filler), `synergy`, `cutting-edge`, `revolutionary`, `breakthrough`. Plus the meta-tails: `it is worth noting`, `it should be emphasized`, `having shown X, we now turn to Y`.
- **No self-announcing topic sentences.** Do not say "this section will examine" or "in what follows." State the content.
- **No rhetorical questions immediately answered.** If the question and answer arrive in the same paragraph, just state the answer.
- **No "Now," as paragraph opener** more than once per chapter.
- **Numbers carry their year** for empirical claims that age. Use "current as of YYYY" inline, not just in the citation.
- **Estimation before calculation** in every chapter (Q20). Use the `estimation` environment.
- **Failure section in every chapter** (Q29). Name the mechanism by which the chapter's models, materials, or systems fail.
- **Half-life tag in every chapter** (Q43). Set in `\chapmeta{...}`.

### Naming

- **Engineering** is the book. The twelve divisions are **Volumes**. Never "books."
- File slugs (`volumes/01-quantity/`, `_volume.tex`, `chNN-slug/chapter.tex`, `\label{vol01:ch01}`) are stable. Do not rename.
- The path placeholder pattern is `volumes/<NN>-<vol-slug>/ch<MM>-<chapter-slug>/chapter.tex` and the dossier mirrors it under `docs/research/`.

### Reader-path tagging (settled Q51)

Every section is one of three reader paths, applied via `\pathtag{...}` after the section heading:

- **core** — the spine. Required for the reader to call the book read.
- **standard** — working-engineer depth. Default.
- **mastery** — optional advanced material. Inline `\begin{mastery} ... \end{mastery}` boxes are skippable.

A core-tagged project or exercise must not depend on a standard-tagged section. The Ch 2 review caught exactly that.

### Named accidents (settled Q56, in progress)

If a chapter mentions a named accident (Mars Climate Orbiter, Therac-25, Tacoma Narrows, etc.):

1. The accident must have a registry entry at `docs/research/accidents/<slug>-<year>.md` per the schema in `docs/research/accidents/SCHEMA.md`.
2. The chapter's `\chapmeta{... Named cases: ...}` block lists the accident.
3. The chapter's mechanism description aligns with the registry's `## Technical mechanism` or quotes one of the registry's `## Short-form summaries` verbatim.
4. The chapter's `\cite{...}` matches the registry's primary or closest-equivalent key.
5. `make accidents` must PASS.

If the chapter wants to name an accident with no registry entry, write the entry first (~30 minutes using the schema). Do not narrate from memory or from a textbook.

### Research seeds

Seeds live at `docs/research/seeds/<slug>.md` and capture a single idea or framing from external reading, distilled into a self-contained file *after the source has been set aside*. Schema in `docs/research/seeds/SCHEMA.md`; index in `docs/research/seeds/README.md`. A seed is not canon and is not cited from chapter prose; when a seed makes it into the book, the chapter cites the underlying source and the seed stays in place as genealogy. Status ladder mirrors the accident registry: `placeholder` → `provisional` → `integrated`. Use seeds for framings, claims, and quotable sentences that bear on a volume or the project; use chapter dossiers for outline material; use the accident registry for named events. No `make` target enforces the seeds lane; the discipline is editorial.

### Citation discipline (read `docs/citation-policy.md`)

- BibLaTeX keys carry a category prefix: `std:` `acc:` `law:` `hist:` `text:` `paper:` `data:` `web:` `gen:`.
- Primary sources are required for standards, laws, regulations, accident reports, historical claims, empirical performance claims.
- Closest-equivalent-to-primary path applies to cases like Therac-25 where no single official report exists. The closest-equivalent designation is per-case and is recorded in the registry entry, not asserted in chapter prose.
- Page or section pins are required for direct quotations and for empirical numbers.
- Tertiary explainers (Wikipedia, vendor whitepapers, blog posts) may not support load-bearing claims.

### Structure of a chapter

Every chapter follows this skeleton (derived from the Ch 1 and Ch 2 pilots):

```latex
\chapter{...}
\label{volNN:chMM}
\epigraph{...}{...with full citation pin if quoting}
\chapmeta{Half-life: ... . Archetypes: ... . Exercise target: N. Project track: ... . Hazard class: ... . Reader path default: standard, with sections explicitly tagged. Named cases: ... .}
\noindent
<one-paragraph orientation>
\section{...}\pathtag{core|standard|mastery}
...
\begin{archetype}[name]
...
\end{archetype}
\begin{estimation}
\textbf{Question.}
...
\end{estimation}
\begin{mastery}
<optional advanced box>
\end{mastery}
\section{Failure: ...}\pathtag{core}
...
\begin{principle}[Name]
...
\end{principle}
\section{Project}\pathtag{core}
\begin{project}[Title]
...
\end{project}
\section{Exercises}
\subsection*{Calculation}\pathtag{...}
\begin{exercise}...\end{exercise}
\subsection*{Derivation}\pathtag{...}
...
```

### Imperial / non-coherent units in LaTeX

`siunitx` does not define tokens for many imperial / non-SI units. Use plain text inside math mode rather than fighting the package:

- `\si{\foot}`, `\si{\inch}`, `\si{\pound}`, `\si{\psi}`, `\si{\atmosphere}`, `\si{\bar}`, `\si{\degF}`, `\si{\horsepower}`, `\si{\hg}`, `\si{\torr}`, `\si{\rayl}` all fail.
- Replace with: `1\,\text{ft}`, `1\,\text{in}`, `40\,\text{ft}\cdot\text{lbf}`, `32\,\text{psi}`, `1\,\text{atm}`, `25\,\text{bar}`, `300\,{}^{\circ}\mathrm{F}`, `5.0\,\text{L}/100\,\text{km}`, `120/80\,\text{mmHg}`, `415\,\text{rayl}`, etc.
- Do **not** nest `\degC` inside `\si{}`. The `\degC` macro expands to `\si{\degreeCelsius}`. Use one or the other:
  - inside `\si{...}`: `\si{\degreeCelsius}`
  - bare in math mode: `\degC` (which expands to `\si{\degreeCelsius}`)
- The `\joule`, `\kilo`, `\meter`, `\kilogram`, etc. tokens are siunitx-internal; they only work inside `\si{}` or `\SI{}{}`. Outside, write `\si{\joule}` or `\text{J}`.

### Exercise environment

`exercise` is defined as `\newtheorem{exercise}{Exercise}[chapter]`. It accepts an optional bracketed argument as a per-exercise label. Use this for path tagging or deferral notes:

```latex
\begin{exercise}[\textit{deferred to Chapter 4}]
...
\end{exercise>
```

The closing tag is `\end{exercise}` (closing brace, not angle bracket). A common typo.

## Workflow: how a chapter gets written and reviewed

1. **Stage 1 (Outline)** — chapter exists as a dossier under `docs/research/<NN>-<slug>/ch<MM>-<slug>.md` and as a generated shell under `volumes/.../chapter.tex` with TODO blocks. All 174 chapters are at Stage 1.
2. **Stage 2 (Source acquisition)** — the chapter's lead writer reads primary sources, identifies citations, adds BibLaTeX entries with page pins, and produces a chapter source ledger. No prose yet.
3. **Stage 3 (Drafting)** — the writer fills in the chapter shell: epigraph, opener, sections, archetype, estimation block, project, exercises, failure section, named cases. The chapter compiles via `make`. `make check` and `make accidents` PASS.
4. **Stage 4 (Review)** — three-role review (technical, pedagogical, voice) per `docs/reviewer-guide.md`. Use `docs/review-prompt.md` to commission the review (Codex or a domain reviewer). Set `Volume:` and `Chapter:` numbers at the top; the reviewer resolves slugs and paths from there. Output goes to `docs/reviews/vol<NN>-ch<MM>-review.md`.
5. **Stage 5 (Integration)** — fixes applied; bibliography consolidated; cross-references updated; landscape index updated if archetypes changed; review marked `Resolved: YYYY-MM-DD` at the top of the review file.
6. **Stage 6 (Released)** — chapter is part of an issued release; corrections flow through errata.

The pilot review of Vol I Ch 1 produced 40 fixes; the Ch 2 review produced 30. Both were applied; both reviews are resolved. The pattern is robust: reviews are unsparing, fixes are concrete and droppable in directly, and the editor applies them without re-deriving rationale.

## Where to read first

When in doubt, read these in order:

1. `docs/editorial-decisions.md` — fifty-plus settled editorial decisions, with the thesis pinned at the top.
2. `docs/status.md` — current phase, counts, what is complete, what is queued.
3. `docs/research/landscape.md` — cross-volume landscape, archetype index, page-budget table.
4. `docs/voice.md` — house voice rules. Read before writing prose.
5. The relevant volume opener and chapter dossier for whatever chapter is in scope.
6. The relevant chapter's review file (if one exists) to see what was caught last time.
7. `docs/research/accidents/SCHEMA.md` — if a chapter mentions any named accident.

## Common pitfalls

Concrete things that have already gone wrong in this codebase, with their fix:

- **Imperial units in `\si{}`** → use plain text (see above).
- **Em-dashes** → search before commit: `grep -n '\---' file.tex` and `grep -n '—' file.tex`. Both should return empty.
- **`/Users/`, `/home/` paths** in committed files → `make audit-docs` flags these.
- **Stale chapter counts** (163, ~465, `book-NN`, `book-XX`, `docs/research/book-`) → `make audit-docs` flags these.
- **Named accidents without a registry entry** → `make accidents` flags these.
- **Wrong citation for an accident** (e.g. citing the Challenger Commission for Hubble) → reviewer will catch; the registry's primary/closest-equivalent key is the canonical answer.
- **Self-announcing topic sentences** (e.g. "This chapter introduces measurement as a discipline.") → cut.
- **The `\foot` family of siunitx tokens** → see above.
- **Nested `\si{\degC}`** → use `\si{\degreeCelsius}` or `\degC`, not both.
- **Reader-path dependency violations** (a `core` project depending on a `standard` section) → either promote the section to `core` or demote the project.
- **Q16 leak in chapter prose** (mentioning "Q16" or other open-question identifiers in body text) → those identifiers belong in dossiers and editorial docs, not in reader-facing prose.
- **`exercise` typo** `\end{exercise>` → use `\end{exercise}`.
- **`main.bcf-SAVE-ERROR` lingering** → `make distclean` clears it (the file is in `ARTIFACTS`).

## Status

Run `make stats` for live counts. Read `docs/status.md` for the current phase. Latest:

- **Phase 0** (scaffolding + outline) **Complete** 2026-04-26.
- **Phase 0.5** (structural hardening) **Complete** 2026-04-28.
- **Phase 0.6** (curriculum expansion: 11 new chapters, 4 renames) **Complete** 2026-04-28.
- **Phase 0.7** (registry foundation and pilot prose) **Complete** 2026-04-29.
- **Phase 1** (production prose at scale) **In progress**. Volume II prose drafted in full on 2026-04-29 by two parallel-agent passes (Ch 1-9, then Ch 10-18). Volume I production-density pass and Volume III prose lane both open; Q57 (page density vs target) gates the production-density choice.

Verified at last edit (2026-04-29):

- 12 volumes / 174 chapters / 174 dossiers.
- ~1161-page PDF.
- 9 chapters at Stage 5 (all of Volume I, drafted 2026-04-28 to 2026-04-29 and carried through Codex review individually). Vol I prose ~220pp at first-draft density against a ~720pp target.
- 18 chapters at Stage 4 (all of Volume II, drafted 2026-04-29 by parallel agents). Vol II prose ~482pp at first-draft density against an ~1800pp target.
- 147 chapters at Stage 1 (all of Volumes III-XII).
- 94 bibliography entries.
- 15 named-case registry entries (`make accidents` PASS).
- Citation prefixes: `std:`, `acc:`, `law:`, `hist:`, `text:`, `paper:`, `method:`, `data:`, `web:`, `gen:`. The `method:` lane was introduced during Ch 8 review for replication-studies / p-hacking / HARKing literature.
- Math operators in `eng-macros.sty`: linear-algebra (`\spn`, `\col`, `\nul`, `\rank`, `\sgn`, `\proj`) added during Vol II Ch 9 integration; trace and diagonal (`\tr`, `\diag`) added during Vol II Ch 10-18 pre-flight; optimisation (`\argmin`, `\argmax` via `\DeclareMathOperator*`) added at the same time.
- `make check`, `make audit-docs`, `make accidents`, `make exercise-counts` all PASS. `make distclean && make strict` produces a clean 1161-page PDF with no undefined references.

## What not to do

- **Do not amend git commits** without explicit instruction; create new commits.
- **Do not skip git hooks** (`--no-verify`) without explicit instruction.
- **Do not commit `main.pdf`** — gitignored; build locally.
- **Do not commit machine-local paths** (`/Users/...`, `/home/...`) into any tracked file. `make audit-docs` flags these.
- **Do not write to `~/.claude/plans/*`** files except in plan mode and only the active plan file.
- **Do not edit chapter shells directly to add metadata** — edit the dossier and re-run `make scaffolding`.
- **Do not invent citation keys** that do not exist in `bibliography/references.bib`. Add the entry first.
- **Do not narrate a named accident from memory** — find or write the registry entry first.
- **Do not rename file slugs** (`volumes/01-quantity/`, `chNN-slug/`, `\label{vol01:ch01}`).
- **Do not write `Resolved:` on a review file** unless every G fix has actually been applied or addressed.
- **Do not assume a path that the reviewer prompt placeholders refer to** — the reviewer resolves them from `Volume: N` and `Chapter: M`.

## Operational defaults

- **uv** is the project's Python runner. The scaffolding generator carries PEP 723 inline metadata; no virtualenv management.
- **latexmk** drives the build. The Makefile defaults are correct.
- **biber** is the bibliography backend.
- **`SCRATCH.md`** at the repository root is reserved for personal working notes; it is gitignored.
