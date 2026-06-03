# Vol VI Ch 4 data assets

Files in this directory are read by the chapter's code assets and by the
exercises. Sources are noted per file.

- `amino_acid_properties.csv`: the twenty standard amino acids, with
  molecular weight (Da), side-chain pKa (where titratable), Kyte-Doolittle
  hydrophobicity index, formal charge at pH 7.4, structural class, and
  approximate frequency (%) in the Swiss-Prot 2024 release. Compiled from
  Lehninger 2017 Table 3-1 and the Swiss-Prot 2024 amino-acid composition
  statistics.

- `enzyme_kinetics.csv`: kcat, Km, and kcat/Km for ten representative
  enzymes. Values rounded to two significant figures. Compiled from the
  BRENDA database (release 2024-1) and the textbook values in Lehninger
  2017 Chapter 6.

- `motor_proteins.csv`: step size, stall force, velocity, ATP cost per
  step, processivity, and direction for the eight motor proteins
  discussed in the chapter. Sources: Howard 2001 (Motor Proteins);
  Svoboda et al. 1993 (kinesin); Finer et al. 1994 (myosin); Noji et al.
  1997 (F1 ATPase); Berg 2003 (flagellar motor).

- `mm_kinetics_example.csv`: a synthetic Michaelis-Menten dataset (v
  vs [S]) generated from Vmax = 46 uM/min, Km = 1.2e-4 M, with 5%
  multiplicative Gaussian noise. Used by `michaelis_menten_fit.py`.

- `hemoglobin_oxygen_binding.csv`: oxygen saturation curve for human
  haemoglobin and myoglobin as a function of partial pressure of oxygen
  (mmHg). Tabulated from Severinghaus 1979 (human Hb) and Antonini and
  Brunori 1971 (Mb). Used by `hill_cooperativity.py`.

- `pdb_excerpt_1aki.pdb`: backbone atoms (N, CA, C, O) for the first 12
  residues of hen egg-white lysozyme (PDB 1AKI). Used by
  `pdb_distance_calc.py`. The full 129-residue structure should be
  downloaded from the Protein Data Bank for the project work.
