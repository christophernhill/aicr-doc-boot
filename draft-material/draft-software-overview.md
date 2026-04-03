# Software

AICR provides software through environment modules, containers, and user-managed environments. This page explains how to find, load, and manage software for your research workflows.

## Environment Modules (Lmod)

AICR uses [Lmod](https://lmod.readthedocs.io/) to manage software environments. Modules configure your shell so that the right compilers, libraries, and tools are available without conflicting with one another.

### Finding Available Software

List all available modules:

```bash
$ module avail
```

Search for a specific package:

```bash
$ module spider pytorch
```

`module spider` shows all versions of a package and any dependencies you need to load first.

### Loading and Unloading Modules

Load a module to add it to your environment:

```bash
$ module load cuda
```

Load a specific version:

```bash
$ module load cuda/12.8
```

<!-- TODO: verify exact CUDA module versions available on AICR -->

View your currently loaded modules:

```bash
$ module list
```

Unload a single module:

```bash
$ module unload cuda
```

Reset to a clean environment:

```bash
$ module purge
```

!!! tip
    Start job scripts with `module purge` followed by explicit `module load` commands. This ensures reproducible environments regardless of what you had loaded in your login session.

### Modules in Job Scripts

Always load modules inside your job script rather than relying on your login environment. The compute node starts with a clean module state.

```bash
#!/bin/bash
#SBATCH --job-name=my_analysis
#SBATCH --partition=rtx-batch
#SBATCH --gpus=1
#SBATCH --time=04:00:00

module purge
module load cuda
module load python

python train.py
```

<!-- TODO: verify exact module names available (e.g., python vs. python3, cuda version names) -->

## GPU Software

AICR compute nodes have NVIDIA GPU drivers and CUDA libraries pre-installed at the system level.

| Component | Details |
|-----------|---------|
| GPU driver | NVIDIA 580.x (datacenter branch) |
| GPU types | NVIDIA RTX PRO 6000 (`rtx-batch`, `rtx-devel`), NVIDIA B200 (`b200-batch`, `b200-devel`) |
| CUDA | Available via module or container |
| cuDNN, NCCL | Available for deep learning and multi-GPU communication |

To verify GPU availability on a compute node:

```bash
$ salloc --partition=rtx-devel --gpus=1 --time=00:15:00
$ nvidia-smi
```

!!! note
    GPU drivers are installed on all GPU nodes. You do not need to install drivers yourself. Load the appropriate CUDA toolkit module or use a container with CUDA to compile and run GPU code.

## Containers with Apptainer

[Apptainer](https://apptainer.org/) (formerly Singularity) is available on all compute nodes for running containerized applications. Containers let you bring a complete software environment — OS, libraries, and application — packaged into a single file.

### Why Use Containers?

- **Reproducibility**: The same container produces the same results on any system.
- **Complex dependencies**: Bundle software stacks that are difficult to install from source (e.g., TensorFlow with specific CUDA versions).
- **Portability**: Build once, run on AICR, your laptop, or another cluster.

### Running a Container

Run a command inside a container:

```bash
$ apptainer exec my_container.sif python train.py
```

Run with GPU support:

```bash
$ apptainer exec --nv my_container.sif python train.py
```

The `--nv` flag binds the host NVIDIA drivers and libraries into the container, giving your application access to the GPUs.

### Running Containers in a Job Script

```bash
#!/bin/bash
#SBATCH --job-name=container_job
#SBATCH --partition=b200-batch
#SBATCH --gpus=1
#SBATCH --time=08:00:00
#SBATCH --mem=64G

apptainer exec --nv /scratch/$USER/containers/my_app.sif python train.py
```

### Building Containers

You can build Apptainer containers from definition files using `--fakeroot` (no root privileges required):

```bash
$ apptainer build --fakeroot my_app.sif my_app.def
```

!!! tip
    Store container images (`.sif` files) in `/scratch/USERNAME`. They can be large and are easy to rebuild, making scratch storage a good fit.

A minimal definition file:

```
Bootstrap: docker
From: pytorch/pytorch:2.2.0-cuda12.1-cudnn8-runtime

%post
    pip install transformers datasets accelerate

%runscript
    python "$@"
```

!!! warning
    Build containers on a compute node via `salloc`, not on a login node. Container builds are CPU- and memory-intensive.

### MPI with Containers

For multi-node parallel jobs, use `srun` to launch the container with PMIx support:

```bash
#!/bin/bash
#SBATCH --job-name=mpi_job
#SBATCH --partition=cpu
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=4
#SBATCH --time=02:00:00

srun --mpi=pmix apptainer exec --nv my_mpi_app.sif ./my_application
```

The host InfiniBand stack (UCX, RDMA libraries) is automatically available inside the container for high-performance inter-node communication.

## Python Environments

For Python-based workflows, you have several options depending on your needs.

### Conda / Miniforge

<!-- TODO: verify whether conda/miniforge is available as a module on AICR or if users should install their own -->

Load the Conda module and create an isolated environment:

```bash
$ module load conda
$ conda create --name myenv python=3.12
$ conda activate myenv
$ conda install numpy pandas scikit-learn
```

!!! tip
    If your Conda environments grow large, create them on scratch or work storage to avoid filling your home directory quota:

    ```bash
    $ conda create --prefix /scratch/USERNAME/conda-envs/myenv python=3.12
    ```

### pip with Virtual Environments

For lightweight setups, use Python's built-in `venv`:

```bash
$ module load python
$ python -m venv ~/myenv
$ source ~/myenv/bin/activate
$ pip install torch torchvision
```

!!! warning
    Do not run `pip install` without an active virtual environment or Conda environment. Installing packages globally can conflict with system libraries and other users' workflows.

### Python in Containers

For complex dependency stacks (e.g., specific CUDA + PyTorch + custom libraries), a container is often the cleanest approach:

```bash
$ apptainer exec --nv pytorch_container.sif python train.py
```

Pre-built containers from [NVIDIA NGC](https://catalog.ngc.nvidia.com/) and [Docker Hub](https://hub.docker.com/) can be pulled directly:

```bash
$ apptainer pull pytorch_latest.sif docker://nvcr.io/nvidia/pytorch:24.01-py3
```

## Compilers

System compilers are available on all nodes without loading a module:

| Compiler | Command | Language |
|----------|---------|----------|
| GCC | `gcc` | C |
| G++ | `g++` | C++ |
| GFortran | `gfortran` | Fortran |

<!-- TODO: verify if additional compiler versions (e.g., newer GCC, Intel oneAPI, NVIDIA HPC SDK) are available as modules -->

To compile a simple C program:

```bash
$ gcc -O2 -o my_program my_program.c
```

To compile with GPU support using NVIDIA's compiler:

```bash
$ module load cuda
$ nvcc -o my_gpu_program my_gpu_program.cu
```

## Requesting Software

If you need software that is not available as a module or container, you have two options:

1. **Install it yourself** in your home or scratch directory, in a Conda environment, or in an Apptainer container. This is the fastest path for most research software.
2. **Request a system installation** by contacting [AICR support](../help.md). System-wide installations are appropriate for software that benefits many users.

!!! note
    Containers are the recommended approach for complex software stacks. They give you full control over your environment and do not require administrator intervention.

## See Also

- [Running Jobs](../running-jobs.md) — how to submit jobs that use the software described here
- [Getting Started](../getting-started.md) — first steps on AICR, including basic module usage
- [Filesystem Overview](../files/overview.md) — where to store software, environments, and containers
