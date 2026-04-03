# Draft Material Table of Contents

Catalog of all generated artifacts in `draft-material/`. Agents must keep this file up to date whenever they add, rename, or remove files.

## Documentation Pages

| File | Target Section | Status | Summary |
|------|---------------|--------|---------|
| `draft-software-overview.md` | Software | Draft | Module system (Lmod), GPU software, Apptainer containers, Python environments, compilers, software requests |
| `draft-running-jobs.md` | Running Jobs | Draft | Slurm partitions, batch/interactive/GPU/MPI/array jobs, monitoring, directives reference, troubleshooting |
| `draft-filesystem-overview.md` | Files > Overview | Draft | Home/scratch/work storage areas, quotas, snapshots, purge policy, performance, data management best practices |

## Example Code

| File | Used By | Summary |
|------|---------|---------|
| `train.py` | `draft-running-jobs.md` | Self-contained PyTorch training script. Synthetic regression task (SensorNet). Supports single-GPU, multi-GPU (DDP via torchrun), and job arrays (--seed). |

## Supplementary Documentation

| File | Explains | Summary |
|------|----------|---------|
| `README_train.md` | `train.py` | Detailed walkthrough of the training script: model architecture, synthetic data formula, training loop, DDP mechanics, data loading, checkpointing. Includes 5 Mermaid diagrams and references to PyTorch docs and ML foundations. |
