# UMass Unity Documentation Site -- Page Index

Generated 2026-04-03. Source: https://docs.unity.rc.umass.edu/

## Site-Wide / Non-Documentation Pages

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|----------------|------------|
| https://docs.unity.rc.umass.edu/ | Unity Home | Landing page with links to account settings, OnDemand, software/dataset request forms, and system status. | Getting Started |
| https://docs.unity.rc.umass.edu/about/ | About | Introduces Unity as a collaborative research computing platform, detailing compute resources, storage infrastructure, team structure, and institutional partners. | Getting Started, Style reference |
| https://docs.unity.rc.umass.edu/contact/ | Contact Us | Provides support channels including Slack, weekly office hours, help tickets via email, software installation requests, and partnership inquiries. | Getting Started, Style reference |

## Getting Access

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|----------------|------------|
| https://docs.unity.rc.umass.edu/documentation/getting-access/ | Requesting a Unity Account | Eligibility requirements and step-by-step instructions for obtaining PI accounts, student/collaborator accounts, and affiliate accounts across affiliated universities. | Getting Started |

## Get Started

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|----------------|------------|
| https://docs.unity.rc.umass.edu/documentation/get-started/ | Get Started with HPC and Unity | Hub page for beginners covering quick starts, terminology, HPC theory, and version control with Git. | Getting Started |
| https://docs.unity.rc.umass.edu/documentation/get-started/quickstart/ | Quick Start Guide | Comprehensive introduction covering computational needs assessment, CPU/GPU resource selection, job scheduling with Slurm, monitoring tools, and storage best practices. | Getting Started |
| https://docs.unity.rc.umass.edu/documentation/get-started/common-terms/ | Common Terms | Definitions of HPC terminology including infrastructure concepts, software management, Linux systems, and filesystem operations. | Getting Started, Style reference |
| https://docs.unity.rc.umass.edu/documentation/get-started/hpc-resources/ | HPC Resources | Curated external learning resources for HPC, Linux, and scientific software development, organized by experience level. | Getting Started |
| https://docs.unity.rc.umass.edu/documentation/get-started/hpc-theory/ | Theory of HPC | Introductory section covering foundational HPC concepts with focus on threads, cores, and sockets in Slurm workflows. | Getting Started, Running Jobs |
| https://docs.unity.rc.umass.edu/documentation/get-started/hpc-theory/threads-cores-processes-sockets/ | Overview of Threads, Cores, and Sockets in Slurm | Explains threads, cores, sockets, and processes and how they relate to Slurm job scheduling, with guidance on critical Slurm flags for CPU parallel programs. | Running Jobs |
| https://docs.unity.rc.umass.edu/documentation/get-started/git-guide/ | Git Guide | Instructions for installing Git, configuring it, creating/cloning repositories, committing changes, and using stashing for version control. | Getting Started |

## Connecting to Unity

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|----------------|------------|
| https://docs.unity.rc.umass.edu/documentation/connecting/ | Connecting to Unity | Overview of graphical and command-line methods for connecting to login and compute nodes via SSH, OnDemand, and VS Code. | Getting Started |
| https://docs.unity.rc.umass.edu/documentation/connecting/ssh/ | SSH | How to establish SSH connections by generating/storing SSH keys and connecting via CLI or PuTTY. | Getting Started |
| https://docs.unity.rc.umass.edu/documentation/connecting/ondemand/ | Connect via Unity OnDemand | Accessing the cluster through a web browser using organizational identity provider sign-in, without SSH keys or additional software. | Getting Started |
| https://docs.unity.rc.umass.edu/documentation/connecting/vscode/ | Connecting Desktop VS Code | Configuring VS Code to connect to Unity via SSH, starting interactive jobs, and establishing remote development sessions. | Getting Started, Software |

## Get Help

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|----------------|------------|
| https://docs.unity.rc.umass.edu/documentation/help/ | Get Help | Hub for user assistance with links to FAQ, troubleshooting, and guidelines for asking support questions. | Getting Started, Style reference |
| https://docs.unity.rc.umass.edu/documentation/help/faq/ | Frequently Asked Questions | Answers to common questions about connection methods, software availability, storage allocation, and job management. | Getting Started, Style reference |
| https://docs.unity.rc.umass.edu/documentation/help/troubleshooting/ | Troubleshooting | Solutions for common issues including SSH connection errors, authentication problems, job submission failures, and storage management challenges. | Getting Started, Running Jobs |
| https://docs.unity.rc.umass.edu/documentation/help/asking-questions/ | How to Ask for Help | Guidelines for submitting effective support requests, emphasizing error messages, commands, environment details, and reproducible examples. | Style reference |

## Cluster Specifications

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|----------------|------------|
| https://docs.unity.rc.umass.edu/documentation/cluster_specs/ | Unity Specifications | Overview of compute and storage hardware with navigation to detailed technical specs for nodes, partitions, storage, and GPU/CPU resources. | Getting Started |
| https://docs.unity.rc.umass.edu/documentation/cluster_specs/nodes/ | Unity Nodes | Comprehensive inventory of computing nodes with CPU type, core count, RAM, GPU models, VRAM, and partition assignments. | Running Jobs |
| https://docs.unity.rc.umass.edu/documentation/cluster_specs/partitions/ | Unity Partitions | Listing of all computational partitions with node counts, time limits, and access restrictions. | Running Jobs |
| https://docs.unity.rc.umass.edu/documentation/cluster_specs/storage/ | Storage | Describes three storage tiers (high-performance, mid-performance project, archival tape), requesting additional capacity, and file restoration from snapshots. | Filesystem |
| https://docs.unity.rc.umass.edu/documentation/cluster_specs/features/ | Node Features (Constraints) | Reference guide for Slurm `--constraint` flag options organized by CPU architecture, GPU models, memory, and networking capabilities. | Running Jobs |
| https://docs.unity.rc.umass.edu/documentation/cluster_specs/features/nvlink/ | NVLink and NVSwitch | Explains GPU interconnects (NVLink for pairs, NVSwitch for larger groups) and how to request/use these nodes with PyTorch. | Running Jobs, Software |
| https://docs.unity.rc.umass.edu/documentation/cluster_specs/cpu_summary/ | CPU Summary List | Table of CPU configurations across partitions and research groups, including processor models, node counts, core counts, and RAM. | Running Jobs |
| https://docs.unity.rc.umass.edu/documentation/cluster_specs/gpu_summary/ | GPU Summary List | Inventory of GPU hardware across partitions with GPU model, quantity, VRAM, cores per GPU, and system RAM per GPU. | Running Jobs |

## Managing Files

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|----------------|------------|
| https://docs.unity.rc.umass.edu/documentation/managing-files/ | Managing Files | Overview of file upload methods (OnDemand, FileZilla, Globus, CLI) with SSH key setup guidance. | Filesystem |
| https://docs.unity.rc.umass.edu/documentation/managing-files/cli/ | Command Line Interface (CLI) | Using CLI to navigate directories and copy files via `scp` and `rsync` after connecting with OpenSSH. | Filesystem |
| https://docs.unity.rc.umass.edu/documentation/managing-files/quotas/ | Disk Quotas | Managing disk quota usage: checking space, identifying large files, reducing storage via deletion/compression, handling HuggingFace and Conda cache bloat. | Filesystem |
| https://docs.unity.rc.umass.edu/documentation/managing-files/filezilla/ | FileZilla | Configuring FileZilla for SFTP file transfers to Unity using SSH keys with correct default remote directory. | Filesystem |
| https://docs.unity.rc.umass.edu/documentation/managing-files/globus/ | Globus | Joining UMass's Globus subscription and using Globus Connect for file transfers between HPC collections. | Filesystem |
| https://docs.unity.rc.umass.edu/documentation/managing-files/rstor/ | RStor Research Storage System | Mid-performance, low-cost research storage (launched 2025) for non-sensitive data, accessible via NFS on Unity batch cluster and SMB on desktops. | Filesystem |
| https://docs.unity.rc.umass.edu/documentation/managing-files/rstor/allocations/ | Managing RStor Shares | Instructions for requesting and managing RStor allocations through the Unity Allocation Portal, including PI registration and user access grants. | Filesystem |
| https://docs.unity.rc.umass.edu/documentation/managing-files/rstor/usage/ | RStor Usage | Accessing RStor storage on Unity and mounting shares on desktop computers via SMB for macOS and Windows. | Filesystem |
| https://docs.unity.rc.umass.edu/documentation/managing-files/rstor/portal/ | The Allocation Portal | How the portal manages resource allocation tracking across projects, explaining relationships between projects, resources, and allocations. | Filesystem |
| https://docs.unity.rc.umass.edu/documentation/managing-files/hpc-workspace/ | HPC Workspace (Scratch) | Creating, managing, and sharing temporary high-performance storage allocations (up to 15TB per user) with extensions, reminders, and collaborative access. | Filesystem |
| https://docs.unity.rc.umass.edu/documentation/managing-files/ondemand/ | Unity OnDemand File Browser | Using OnDemand's graphical file manager for navigating, uploading, downloading, and editing files without CLI. | Filesystem |

## Submitting Jobs

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|----------------|------------|
| https://docs.unity.rc.umass.edu/documentation/jobs/ | Introduction to Slurm | Introduces Slurm job scheduler covering core resource limits, cluster partitions, and the two primary submission methods (`salloc` and `sbatch`). | Running Jobs |
| https://docs.unity.rc.umass.edu/documentation/jobs/sbatch/ | Batch Jobs | Creating batch scripts with Slurm parameters and commands, submitting via `sbatch`, monitoring status, and receiving email notifications. | Running Jobs |
| https://docs.unity.rc.umass.edu/documentation/jobs/sbatch/arrays/ | Array Batch Jobs | Submitting and managing array jobs with `--array` parameter and `$SLURM_ARRAY_TASK_ID` for running multiple instances with different data/parameters. | Running Jobs |
| https://docs.unity.rc.umass.edu/documentation/jobs/sbatch/large-count/ | Large Job Counts | Submitting large numbers of jobs (up to 2,000 at once, 1,000 concurrent max) with recommendations to use array jobs for efficiency. | Running Jobs |
| https://docs.unity.rc.umass.edu/documentation/jobs/sbatch/monitoring/ | Monitor a Batch Job | Tracking job progress and resource utilization via log tailing (`tail -F`), `sstat` for resource usage, and `srun` for interactive node inspection. | Running Jobs |
| https://docs.unity.rc.umass.edu/documentation/jobs/helper_scripts/ | Helper Scripts | Command-line utilities for optimizing job scheduling by showing resource availability, GPU usage, node capacity, and account allocation limits. | Running Jobs |
| https://docs.unity.rc.umass.edu/documentation/jobs/salloc/ | Interactive CLI Jobs (salloc) | Using `salloc` to allocate resources and request compute nodes in real-time, with guidance on when to choose interactive vs. batch jobs. | Running Jobs |
| https://docs.unity.rc.umass.edu/documentation/jobs/ondemand/ | Submit Jobs with Unity OnDemand | Using OnDemand's Job Composer, Job Templater, and Active Job Viewer to submit and manage batch jobs without the command line. | Running Jobs |
| https://docs.unity.rc.umass.edu/documentation/jobs/mpi/ | Message Passing Interface (MPI) | Running distributed computing jobs across multiple nodes, covering MPI implementations, compilation, job configuration, and execution. | Running Jobs |
| https://docs.unity.rc.umass.edu/documentation/jobs/slurm/ | Slurm Cheat Sheet | Quick reference for common Slurm commands and arguments for submitting, monitoring, and managing computational jobs. | Running Jobs |
| https://docs.unity.rc.umass.edu/documentation/jobs/coordinator/ | Managing Group Resource Use | How Slurm Coordinators oversee group resource allocation by managing jobs and setting user limits on CPUs, GPUs, memory, and concurrent jobs. | Running Jobs |

## Software Management

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|----------------|------------|
| https://docs.unity.rc.umass.edu/documentation/software/ | Software Management | Overview of software installation methods: apt, environment modules, Conda, Python venvs, R package management, and Apptainer containers. | Software |
| https://docs.unity.rc.umass.edu/documentation/software/modules/ | Introduction to Environment Modules | How modules manage shell variables and `$PATH` to control available software executables and prevent conflicts. | Software |
| https://docs.unity.rc.umass.edu/documentation/software/modules/module-usage/ | Module Usage | Instructions for listing, searching, loading, and unloading software modules to enable version-specific tools. | Software |
| https://docs.unity.rc.umass.edu/documentation/software/conda/ | Conda Environments | Using conda on Unity: environment creation, activation, package installation, and JupyterHub integration. | Software |
| https://docs.unity.rc.umass.edu/documentation/software/venv/ | Virtual Environments in Python | Creating isolated Python environments with venv, managing dependencies, and submitting jobs using virtual environments. | Software |
| https://docs.unity.rc.umass.edu/documentation/software/renv/ | Virtual Environments in R | Using the renv package to create isolated, project-level R package environments with reproducibility and portability. | Software |
| https://docs.unity.rc.umass.edu/documentation/software/softwarefromscratch/ | Building Software from Scratch | Obtaining source code, identifying build systems, compiling software, and installing to a designated directory on Unity. | Software |
| https://docs.unity.rc.umass.edu/documentation/software/ondemand/ | Manage Software in Unity OnDemand | Using Batch Connect in OnDemand to run graphical apps (VSCode, JupyterLab, Matlab, RStudio) as batch jobs via VNC. | Software |
| https://docs.unity.rc.umass.edu/documentation/software/ondemand/jupyterlab-ondemand/ | JupyterLab on Unity OnDemand | Accessing JupyterLab via OnDemand, configuring interactive sessions, and executing notebooks non-interactively with `nbconvert` or `papermill`. | Software |

## Tools & Software

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|----------------|------------|
| https://docs.unity.rc.umass.edu/documentation/tools/ | Tools & Software | Hub page linking to guides for specific software: ColabFold, PyTorch, R, and GPU resources. | Software |
| https://docs.unity.rc.umass.edu/documentation/tools/colabfold/ | Introduction to ColabFold on Unity | Using ColabFold for 3D protein structure prediction via interactive Jupyter notebooks (single sequences) or batch scripts (multiple sequences). | Software |
| https://docs.unity.rc.umass.edu/documentation/tools/pytorch/ | Installing PyTorch | Installing PyTorch on Unity with details on PyTorch/CUDA version relationships, NVIDIA drivers, and GPU compute capability. | Software |
| https://docs.unity.rc.umass.edu/documentation/tools/r/ | Introduction to R on Unity | Accessing R through RStudio OnDemand or CLI, installing packages, and submitting R scripts as batch jobs. | Software |
| https://docs.unity.rc.umass.edu/documentation/tools/r/run-r-in-parallel/ | Run R in Parallel | Approaches to parallelizing R code: independent tasks, `foreach`, `future` with `batchtools`, and `furrr`. | Software, Running Jobs |
| https://docs.unity.rc.umass.edu/documentation/tools/gpus/ | GPUs on Unity | Requesting and using GPU resources: available GPU types, Slurm submission examples, software configuration, and troubleshooting. | Running Jobs, Software |

## Datasets

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|----------------|------------|
| https://docs.unity.rc.umass.edu/documentation/datasets/ | Datasets | Catalog of publicly available datasets on Unity organized into AI/ML and bioinformatics categories. | Software |
| https://docs.unity.rc.umass.edu/documentation/datasets/ai/ | AI and ML Datasets | Index of AI/ML datasets and models (Llama, GPT, Gemma, Whisper, etc.) with paths and specifications. | Software |
| https://docs.unity.rc.umass.edu/documentation/datasets/bio/ | Bioinformatics Datasets | Index of bioinformatics datasets including protein structure databases, sequence alignment tools, and annotation resources. | Software |
| https://docs.unity.rc.umass.edu/documentation/datasets/using-huggingface-datasets/ | Using HuggingFace Datasets | Configuring and loading HuggingFace models on Unity via environment variables or absolute paths, with three implementation methods. | Software |

## Contributing

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|----------------|------------|
| https://docs.unity.rc.umass.edu/documentation/contributing/ | Contributing to These Docs | Guide for contributing via GitLab: opening issues, writing documentation, and submitting merge requests. | Style reference |

---

## Summary Statistics

- **Total unique pages indexed:** 62 (excluding individual dataset detail pages)
- **Individual AI/ML dataset pages:** ~70 (listed under /documentation/datasets/ai/*)
- **Individual bioinformatics dataset pages:** ~35 (listed under /documentation/datasets/bio/*)
- **Major documentation sections:** 10 (Getting Access, Get Started, Connecting, Help, Cluster Specs, Managing Files, Jobs, Software, Tools, Datasets)

## Section-Level Navigation Structure

```
/documentation/
  getting-access/
  get-started/
    quickstart/
    common-terms/
    hpc-resources/
    hpc-theory/
      threads-cores-processes-sockets/
    git-guide/
  connecting/
    ssh/
    ondemand/
    vscode/
  help/
    faq/
    asking-questions/
    troubleshooting/
  cluster_specs/
    nodes/
    partitions/
    storage/
    features/
      nvlink/
    cpu_summary/
    gpu_summary/
  managing-files/
    cli/
    quotas/
    filezilla/
    globus/
    rstor/
      allocations/
      usage/
      portal/
    hpc-workspace/
    ondemand/
  jobs/
    sbatch/
      arrays/
      large-count/
      monitoring/
    helper_scripts/
    salloc/
    ondemand/
    mpi/
    slurm/
    coordinator/
  software/
    softwarefromscratch/
    conda/
    modules/
      module-usage/
    renv/
    ondemand/
      jupyterlab-ondemand/
    venv/
  tools/
    colabfold/
    pytorch/
    r/
      run-r-in-parallel/
    gpus/
  datasets/
    ai/  (70+ individual dataset pages)
    bio/ (35+ individual dataset pages)
    using-huggingface-datasets/
  contributing/
```
