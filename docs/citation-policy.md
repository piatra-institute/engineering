# Engineering: citation policy

This file translates settled question 26 (citation discipline) into operational rules for `bibliography/references.bib`, every chapter's prose, and the structural-check tooling.

## Citation tiers

A claim's citation tier follows the kind of claim being made. Settled question 26:

- **Primary sources** are *required* for: standards, laws, regulations, official accident investigation reports, historical dating and attribution, and empirical performance claims (cost figures, throughput numbers, failure rates, market shares, regulatory decisions, commercial benchmarks).
- **Classical handbooks and established textbooks** are *acceptable* for settled technical material whose primary derivation is older than fifty years and is reproduced consistently across the discipline (Maxwell's equations, Hooke's law, the Carnot cycle, the central limit theorem).
- **Tertiary explainers** (online tutorials, popular-science books, Wikipedia, vendor whitepapers) are *permitted as pedagogical support only*. They may not support a load-bearing claim. They may guide the reader to a primary source but do not stand in for one.

A claim that does not have a citation at the appropriate tier is either reframed (made conditional, attributed to a model rather than to data) or cut.

## Citation-key categories

`bibliography/references.bib` is organised by citation-key prefix. Every entry uses a prefix that names the source class. The prefix is the first segment of the BibLaTeX key:

| Prefix | Source class | Required where |
|---|---|---|
| `std:` | Standards (ISO, IEC, ASTM, IEEE, NIST, BIPM, CEN, EN, ASME, RFC) | Standards-driven claims |
| `acc:` | Accident investigation reports (NTSB, AAIB, BEA, NRC, EU EASA, MAIB, USCSB, equivalents) | Named-accident sections |
| `law:` | Laws, regulations, court decisions, regulatory rulings | Regulatory and legal claims |
| `hist:` | Historical primary sources, archival material, scholarly histories | Historical attribution |
| `text:` | Classical handbooks and established textbooks | Settled technical material |
| `paper:` | Peer-reviewed research papers, conference proceedings | Recent technical claims |
| `data:` | Datasets, public-record data, empirical compilations | Empirical performance claims |
| `web:` | Online primary or companion sources (institutional pages, official documentation) | Time-stamped current-state claims |

Examples of well-formed keys:

```
std:bipm-si2019
acc:ntsb-aar94-04   % Aloha 243
acc:bea-af447       % Air France 447
law:eu-mdr2017      % Medical Devices Regulation
hist:lavoisier1789
text:timoshenko-mechanics-of-materials
text:incropera-heat-transfer
paper:shannon1948
paper:vaughan-challenger
data:iea-energy-2024
web:nist-traceability-policy
```

The diagnostic recommends 5-10 entries per category as starter content, growing as chapters cite. Initial seeding is a Phase 0.5 follow-up activity.

## In-text citation rules

The book uses `\\cite{...}` and the biblatex authoryear style.

- **Multiple sources for one claim**: separate keys with comma. `\\cite{key1,key2}`.
- **Attribution within sentence**: `\\textcite{...}` to make the author the grammatical subject.
- **Specific page/section**: `\\cite[p.~42]{key}` or `\\cite[ch.~3]{key}`.
- **Direct quotation**: required for any verbatim text exceeding ten words; pin the page number.
- **Image, figure, or table reproduced from another source**: attribution in the caption plus citation; verify license terms.

A chapter that uses fewer than three citations is either too speculative for its claims or has missing citations. The reviewer-guide checks for this.

## Provenance for tables and figures

Every numerical table carries a `Source:` line directly underneath. The source is one of:

- A bibliography citation (preferred).
- "Computed by the authors from \\cite{...}" with the computation reproducible.
- "Authors' data, current as of YYYY" — only for measurements the project produced and committed to the data repository.

Tables with no provenance are an error class flagged by `make check` (planned).

Figures follow the same rule, in the caption.

## Half-life and the "current as of" convention

Settled question 28: contemporary statistics are time-stamped with their year in the sentence, not only in the citation.

- **Cost / performance / market figures**: "current as of YYYY" inline.
- **Regulatory citations**: cite the version-dated statute or regulation; the citation key carries the year.
- **Software / tool versions**: name the version explicitly; tag the section with `medium-life` or `fast-aging` half-life.
- **AI / ML benchmarks**: tag the section with `fast-aging` half-life; companion-note the specific model.

Half-life category is set in each chapter's `\chapmeta` block. Section-level half-life refinements are a future addition.

## Required for each named accident

A named accident (Bhopal, Chernobyl, Boeing 737 MAX, Therac-25, Tacoma Narrows, Aloha 243, Air France 447, Genoa Morandi Bridge, Volkswagen diesel-defeat, Mars Climate Orbiter, Knight Capital, etc.) requires:

1. The official primary investigation report (or the closest equivalent if no formal report exists), with its `acc:` key.
2. The applicable regulatory or legal context (with `law:` key) when relevant.
3. At least one independent secondary analysis (book, peer-reviewed paper, or major investigative journalism, with `text:` or `paper:` key).
4. The technical mechanism cited from the primary report.
5. The organisational mechanism cited from a source (often the same primary report, sometimes a separate study).
6. A "lessons by scale" summary (the part, the machine, the operator, the organisation, the regulator) drawn from the primary record.

Cases that lack a primary source are not cited as accidents; they are referred to as anecdotal and are handled in companion notes if at all.

The named-cases registry under `docs/research/accidents/` (Q56, deferred) collects these per-accident records and prevents shallow re-tellings across chapters.

## Citation prohibitions

Some patterns are not citations at all and are cut on sight:

- "Studies have shown..." with no citation. Either name the studies or cut the claim.
- "It is widely known that..." — name the discipline and a representative source, or cut.
- "Research suggests..." — same.
- Self-referential citation chains where the claimed primary source actually cites a secondary that cites a tertiary.
- Citations to tertiary explainers used to support load-bearing claims.

## Tooling support

The `make check` target validates structural metadata. Future additions:

- `make citations`: scan TeX source for orphan `\\cite{}` keys and dead references.
- `make accidents`: ensure every named accident in a chapter section heading has at least one `acc:` citation in the chapter body.
- `make tables`: ensure every table has a `Source:` line.

These targets are enumerated in `release-checklist.md` and become required for `make release`.

## Updating the bibliography

The bibliography file is appendable. New entries are added under the appropriate category-prefix comment header. Duplicates are detected by `make citations` (planned).

When the bibliography grows substantially (target: 800-1500 entries at full prose), it splits into per-category files (`bibliography/std.bib`, `bibliography/acc.bib`, ...) included from the master `references.bib`. This is a future structural pass.
