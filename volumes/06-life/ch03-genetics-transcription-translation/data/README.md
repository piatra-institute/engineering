# Data assets, Volume VI Chapter 3

Five CSV tables supporting the chapter prose and the code scripts.
Each table is small enough to read in full; the headers are documented
here, with provenance.

## Tables

### `genetic-code.csv`

The standard nuclear genetic code. One row per codon (64 rows), with
the three-letter and one-letter amino-acid abbreviations, a coarse
chemical-property classification (hydrophobic, polar uncharged, basic,
acidic, stop), and start/stop flags.

Source: NCBI Translation Table 1 (Standard Code), accessed via
`https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi`,
verified 2024-12. Chemical-property classification follows the IUPAC
convention used in Lehninger.

### `mutation-rates.csv`

Per-base and per-genome mutation rates for twelve organisms, ranging
from RNA viruses to mammalian germline. Each row records the genome
size, the method by which the rate was measured (fluctuation test,
mutation-accumulation experiment, parent-offspring trio sequencing,
laser-capture microdissection, replication assay, phylogenetic
estimate), and a short citation tag.

Sources, by row, abbreviated:

- bacteriophage lambda, Drake 1991
- E. coli K-12, Lee et al. 2012, *PNAS*
- yeast, Lynch 2008 *MBE* and Farlow et al. 2015
- C. elegans, Denver et al. 2009 *Nature*
- D. melanogaster, Keightley et al. 2009 *Genome Res.*
- mouse germline, Uchimura et al. 2015 *Genome Res.*
- human germline, Kong et al. 2012 *Nature* (`paper:v6c03-kong-2012`)
- human somatic, Blokzijl et al. 2016 *Nature*
- HIV-1, Mansky and Temin 1995 *J Virol*
- SARS-CoV-2, Amicone et al. 2022 *Evol Med Public Health*

All rates are per base pair per cell division (germline) or per
replication cycle (viruses), current as of 2024.

### `sequencing-costs-nhgri.csv`

Cost per human genome and cost per megabase by year, 2001-2023. The
canonical NHGRI series, compiled and maintained by the NHGRI Large-Scale
Sequencing Program at `https://www.genome.gov/sequencingcostsdata`.
Values are project-cost approximations (machine time, reagents,
labour), not list prices. The dominant-platform column records the
sequencing technology that supplied most of the year's cost-quoted
data. The series is plotted in `figures/fig-sequencing-cost.tex`.

Source: NHGRI Cost Tables, last accessed 2024-08. Cited in prose as
`paper:v6c03-nhgri-cost-2023`.

### `human-chromosomes.csv`

Per-chromosome statistics for the human genome (GRCh38.p14, current as
of 2024). Size in megabases, number of protein-coding genes, number of
non-coding genes (lincRNAs, miRNAs, snoRNAs, etc., combined), and the
count of monogenic diseases mapped to that chromosome in OMIM.

Source: Ensembl 110, Genome Reference Consortium GRCh38.p14;
OMIM gene-map statistics, accessed 2024-08. Cited as
`web:v6c03-ensembl-grch38` and `web:v6c03-omim-2024`.

### `hereditary-disease-incidence.csv`

Fifteen representative monogenic diseases, with their mode of
inheritance, causative gene(s), chromosome, incidence per live births
in the indicated population, carrier frequency where applicable, and
typical age of onset. The table is illustrative, not exhaustive.

Sources, by row, abbreviated:

- Huntington, Marfan, BRCA1, Lynch, FAP: OMIM and Bates et al. 2015
  for HD epidemiology.
- Cystic fibrosis, sickle cell, PKU, Tay-Sachs, SMA: CDC ACOG carrier
  screening data, current as of 2024.
- Duchenne, haemophilia A, fragile X, LHON: GeneReviews (NCBI),
  accessed 2024-09.

The two sickle-cell rows separate US and sub-Saharan Africa incidence
to make explicit the order-of-magnitude variation across populations
under malaria selection. Cited as `web:v6c03-omim-2024` and
`web:v6c03-genereviews-2024`.

## Conventions

- All files are UTF-8 CSV with a header row.
- Genome sizes are in base pairs unless an explicit `_mb` suffix.
- Rates are in scientific notation (`1.2e-8`) for readability.
- Years are calendar years (snapshot value for that year).
- Missing values use the literal string `N/A`.
