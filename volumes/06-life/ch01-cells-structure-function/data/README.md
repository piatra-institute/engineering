# Data assets — Volume VI, Chapter 1 (Cells: structure and function)

Reference datasets supporting the chapter's exercises and worked
examples.

## Files

| File | Source | Year | Used by |
|---|---|---|---|
| `cell_sizes.csv` | BioNumbers compendium (Milo & Phillips 2015); Alberts \emph{MBC} 7th ed. (2022). | 2015--2022 | Cell-size scaling figure; calculation exercises on SA/V; estimation exercises on cell number. |
| `ion_concentrations.csv` | Alberts \emph{MBC} ch.~11; Hodgkin & Huxley (1952) for squid; BioNumbers for \emph{E.\ coli}. | 1952--2022 | Nernst and GHK calculation; `membrane_voltage_nernst.py`; derivation exercises. |
| `mitochondria_counts.csv` | BioNumbers; Attwell & Laughlin (2001); Alberts \emph{MBC}. | 2001--2022 | Estimation exercise on mitochondria per cell; metabolic-cost discussions. |
| `apoptosis_vs_necrosis.csv` | Galluzzi et al.\ (2018) classification consensus; Kerr et al.\ (1972); Hayflick (1965). | 1965--2018 | Failure section diagnostic table; diagnosis exercises. |

## Provenance

Each row carries a `source` or `notes` field tagging the canonical
reference. Concentrations are quoted in millimolar (mM); sizes in
micrometres ($\mu$m) or cubic micrometres ($\mu$m$^3$); times where
relevant in seconds. Empirical numbers are within the spread reported
by the BioNumbers database; the reader should treat order-of-magnitude
correctness as the design intent.

## Use

Files are CSV (UTF-8, RFC 4180). The code under `../code/` reads these
files where relevant; the reader can substitute their own values while
preserving the file structure.
