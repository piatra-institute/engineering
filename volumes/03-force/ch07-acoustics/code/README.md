# Code for Volume III, Chapter 7 (Acoustics)

Each script carries PEP 723 inline metadata and runs under `uv`:

```
uv run room_modes.py
uv run spl_octave.py
uv run wave_1d.py
uv run sabine_rt60.py
```

- `room_modes.py` enumerates and classifies the eigenmodes of a rigid
  rectangular room and writes `data/room_mode_count.csv`
  (consumed by `figures/fig-room-modes.tex`).
- `spl_octave.py` combines octave-band levels and applies A-weighting,
  writing `data/octave_spectrum.csv` (consumed by
  `figures/fig-spl-octave.tex`).
- `wave_1d.py` is an explicit finite-difference solver for the 1D
  acoustic wave equation in a closed tube; it recovers the standing-wave
  frequencies `f_n = n c / (2 L)`.
- `sabine_rt60.py` predicts reverberation time from room geometry and
  surface absorption (Sabine and Eyring).

The committed CSVs in `data/` are the reference outputs; rerunning the
scripts regenerates them.
