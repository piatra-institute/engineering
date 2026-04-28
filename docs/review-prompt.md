# Engineering: chapter review prompt template

A self-contained prompt for handing a chapter to an external reviewing
agent (Codex, a domain reviewer running with read access to the
repository, or a future automated reviewer). The prompt is intended to
produce a consolidated written review that an editor can apply.

The prompt is paired with `docs/reviewer-guide.md` (the protocol the
review follows) and `docs/voice.md` (the voice rules the review checks
against). A reviewer who does not read those two documents will not be
able to produce a useful report; the prompt names them as required
reading.

## When to use this prompt

Use the prompt to commission a review of any chapter at Stage 3
(drafting complete) of the research pipeline (`docs/research-pipeline.md`).
Also use it for the pilot chapter (Vol I Ch 1) before any second chapter
begins. Reuse it for every chapter that reaches Stage 4 thereafter.

Do not use it for the volume opener prose alone (a lighter pass suffices)
or for frontmatter, appendices, or interludes (which follow a separate
checklist in `docs/release-checklist.md`).

## How to use this prompt

1. Identify the chapter coordinates: volume number, volume slug, chapter
   number, chapter slug, chapter title. For the pilot chapter the values
   are: `01`, `quantity`, `01`, `why-we-measure`, `Why we measure`.
2. Copy the **Prompt** section below verbatim.
3. Substitute every `{PLACEHOLDER}` with the chapter's value.
4. Hand the substituted prompt to the reviewing agent.
5. When the agent writes its report at the named output path, read it,
   apply the fixes, and record the review in `docs/reviews/`.

The agent does not see the conversation in which the prompt was
written. Anything the reviewer needs must be in the prompt or in the
files the prompt names.

## Prompt

```
You are reviewing a chapter of a 12-volume engineering formation text
called Engineering. The repository is at:

  /Users/ly3xqhl8g9/Data/i/theings/piatra/content/piatra-press/engineering

The chapter to review is:

  Volume {VOLUME_NUM}: {VOLUME_NAME}
  Chapter {CHAPTER_NUM}: {CHAPTER_TITLE}

Source files:

  Chapter prose: volumes/{VOLUME_NUM}-{VOLUME_SLUG}/ch{CHAPTER_NUM}-{CHAPTER_SLUG}/chapter.tex
  Chapter dossier: docs/research/{VOLUME_NUM}-{VOLUME_SLUG}/ch{CHAPTER_NUM}-{CHAPTER_SLUG}.md
  Volume opener: volumes/{VOLUME_NUM}-{VOLUME_SLUG}/_volume.tex
  Volume dossier: docs/research/{VOLUME_NUM}-{VOLUME_SLUG}/_volume.md

Read this background before reading the chapter:

  1. docs/editorial-decisions.md  (settled editorial questions; thesis at top)
  2. docs/voice.md                (house voice rules; AI-tic ban list)
  3. docs/citation-policy.md      (BibLaTeX prefix conventions, citation tiers)
  4. docs/reviewer-guide.md       (three-role review protocol)
  5. docs/case-study-template.md  (named-accident format)
  6. docs/research/landscape.md   (cross-volume landscape, archetype index)

Then read the chapter dossier, then the volume opener, then the chapter
prose. Then read every BibLaTeX entry the chapter cites in
bibliography/references.bib.

Run all three reviewer roles from docs/reviewer-guide.md (technical,
pedagogical, voice) on the chapter. Write a single consolidated report at:

  docs/reviews/vol{VOLUME_NUM}-ch{CHAPTER_NUM}-{CHAPTER_SLUG}-review.md

Be unsparing. The reviewer's job is to find what would embarrass an
external reader. Do not be reverent; the chapter is a draft.

The report has eight sections, A through H. Each is required.

A. Verdicts. One line per role: technical, pedagogical, voice. Each is
   approved / approved-with-corrections / blocked. If blocked, name the
   one or two issues that block it.

B. Voice review. Walk the chapter end to end. Flag every sentence that
   reads as AI-generic, hyped, equivocating, or violates a docs/voice.md
   ban pattern. Quote the offending sentence verbatim and propose a
   concrete rewrite. Do not generalise; quote. Look in particular for:
   em-dashes (banned outside primary-source quotations), the
   negate-first-then-pivot construction, AI-tic vocabulary
   ("fundamentally," "essentially," "in essence," "delve," "tapestry,"
   "landscape" as metaphor, "leveraging," "robust" as filler), rhetorical
   questions immediately answered, "Now," as paragraph opener used more
   than once, generic intensifiers and hedges as filler, generic male
   default for unspecified actors, performatively humble qualifiers,
   self-announcing topic sentences, meta-explanation tails. Cite the
   docs/voice.md rule the sentence violates.

C. Technical review. Verify the chapter's engineering claims. For every
   numerical figure, check the units, the order of magnitude, and the
   provenance. For every named accident, verify against the primary
   investigation report (which the chapter must cite). For every
   derivation, verify the steps. For every equation, check that the
   dimensions cancel. For every cross-reference (\\cref, \\autoref,
   \\ref), verify that the referenced item exists. List every claim that
   is wrong, imprecise, miscited, or uncitable. Where a claim is correct
   but reads as overstated, say so.

D. Pedagogical review. Does the chapter build the habit it promises in
   its dossier? Are the exercises balanced across the types named in
   editorial-decisions Q16 (calculation, derivation, estimation,
   simulation, design, diagnosis, failure analysis, judgment)? Are they
   calibrated to difficulty? Are any padded, redundant, unanswerable as
   written, or insulting to a serious adult reader? Does the project (per
   the chapter's Q55 ruling, or per the dossier's project brief if Q55 is
   not yet resolved for this chapter) match the chapter's argument? Does
   the estimation block (settled Q20) work as a model? Does the failure
   section (settled Q29) close the chapter's main mechanism? Does the
   archetype invocation (settled Q37) recur from earlier chapters or
   introduce a new one cleanly? Does the chapter respect engineering
   depth without drifting into science-undergraduate depth or hand-waving
   (settled Q9)?

E. Citation discipline. Every load-bearing empirical, historical, or
   institutional claim should carry a citation. Identify any that does
   not. Identify any citation that does not match the citation-policy
   tier for the kind of claim it supports. For named accidents, verify
   that the citation is to the primary investigation report and not to a
   tertiary explainer.

F. Reader-path tagging. Are the \\pathtag{core|standard|mastery}
   assignments defensible? Should any section change tier? Are mastery
   boxes used where they should be used and avoided where they should be
   avoided?

G. Specific concrete fixes. Number each fix. Each fix names the file, the
   line range, the current text, and the proposed replacement. Aim for 20
   to 50 fixes; quality over count. The editor will apply these directly
   without re-deriving the rationale, so the proposed replacement must be
   complete enough to drop in.

H. Structural risks for the larger project. Top three risks this chapter
   reveals about the larger architecture: dossier schema, reviewer
   protocol, release checklist, voice rules, citation policy, exercise
   architecture. Be specific. These are what should change before the
   next chapter is reviewed.

Length: 4,000 to 8,000 words. Do not pad. Section G (specific fixes) is
the most valuable part of the report; spend the most words there.

Voice: write the report in the same authorial "we" as the book, in a
working-engineer register, with no em-dashes. The report itself is read
by the editor, by the writer, and by future reviewers; it should model
the voice it is auditing.

Output: a single file at docs/reviews/vol{VOLUME_NUM}-ch{CHAPTER_NUM}-{CHAPTER_SLUG}-review.md
with the sections A through H above. Do not edit the chapter itself; the
editor applies fixes after reading the report. If the chapter has obvious
build-breaking errors (undefined macros, missing citations, unresolvable
cross-references), say so at the top of the report so the editor fixes
those before applying the substantive comments.
```

## Review-target hierarchy

A reviewer who is short on time should prioritise these in order:

1. Build-breaking issues (undefined macros, missing citations,
   unresolvable cross-references). The editor cannot ship a chapter with
   these.
2. Technical errors (wrong numbers, wrong unit conversions, wrong
   citations to accident reports). These embarrass the project.
3. Voice violations (em-dashes, AI-tic vocabulary, negate-first-pivot,
   etc.). These embarrass the project at a different level.
4. Pedagogical gaps (poorly calibrated exercises, weak estimation block,
   thin failure section, weak project).
5. Reader-path tagging (least urgent; the editor can adjust).

Section G of the report should reflect this hierarchy: the first fixes
are build-breakers, then technical, then voice, then pedagogy.

## Recording the review

Once the reviewer's report is written:

1. Open the report at `docs/reviews/vol{NN}-ch{MM}-{slug}-review.md`.
2. Apply the fixes from section G in order.
3. Where a fix is contested or wrong, add a `### Editor's response`
   block at the bottom of the report explaining the disagreement.
4. Mark the review as resolved by adding a `Resolved: YYYY-MM-DD` line at
   the top of the report when all section G fixes have been applied or
   addressed.
5. Do not delete the report. The history is part of the record.

A chapter that has been through one review at this protocol is at
research-pipeline Stage 4 (`docs/research-pipeline.md`). It moves to
Stage 5 (integration) only after the editor has applied or addressed
every fix.

## Calibration: the pilot review

The pilot review (Vol I Ch 1, "Why we measure") is the first execution
of this protocol. It is the calibration run. After the pilot review is
complete, the editor compares the report's findings against this
template and revises the prompt if the report missed obvious issues or
spent words on issues the editor would not have asked for. The revised
prompt becomes the production template.

Subsequent chapters use the production template without revision unless
the project's voice rules, citation policy, or release checklist change.
A change to any of those triggers a sweep of recent reviews to confirm
they would still hold.
