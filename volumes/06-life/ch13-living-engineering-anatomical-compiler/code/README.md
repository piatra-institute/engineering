# Code assets: Vol VI Ch 13

Living engineering: regenerative medicine, the anatomical compiler.

All scripts use NumPy only. Run with `python <name>.py`. No external
data required; outputs go to stdout.

| file | purpose | exercise |
|------|---------|----------|
| `voltage_gradient_1d.py` | 1D reaction-diffusion model of tissue voltage; tests $\lambda = \sqrt{D/k}$ scaling | Ex 13.6 (simulation) |
| `wound_healing_growth.py` | 2D Fisher-KPP wound-healing simulation; compares numerical wave speed to $c = 2\sqrt{Dr}$ | Ex 13.7 (simulation) |
| `pattern_information.py` | Shannon-entropy estimate for voxel-grid morphology specification | Section 13.3 estimation |
| `target_morphology_match.py` | Image-similarity metrics (IoU, Hausdorff, centroid offset) for morphology scoring | Section 13.4 verification |
| `cerb_pipeline_sim.py` | Toy three-stage compiler pipeline (spec, translate, execute) | Chapter project |

Each script's docstring states the published reference behind the
model and the chapter cross-reference. The scripts are illustrative,
not engineering tools: they model orders of magnitude, not biology.
