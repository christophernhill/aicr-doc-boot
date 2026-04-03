# MIT ORCD Documentation Site -- Page Index

**Source:** https://orcd-docs.mit.edu/
**Crawled:** 2026-04-03
**Total pages found:** 52 (including redirects/stubs)

---

## General / Top-Level Pages

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://orcd-docs.mit.edu/ | ORCD Docs Home | Landing page for the MIT Office of Research Computing and Data documentation site, with full navigation sidebar. | Style reference, Site structure |
| https://orcd-docs.mit.edu/orcd-systems/ | ORCD Engaging System | Introduces the Engaging HPC cluster as a mixed CPU/GPU system openly available to all MIT research projects, with account and resource overview. | Getting Started, Overview |
| https://orcd-docs.mit.edu/getting-started/ | Getting Started Tutorial | Step-by-step guide for new users covering account setup, cluster architecture, finding software, basic Linux commands, file management, and first job submission. | Getting Started |
| https://orcd-docs.mit.edu/getting-help/ | Getting Help | Outlines three support channels: documentation/FAQ, email support lists, and scheduled office hours. | Getting Started, Support |
| https://orcd-docs.mit.edu/faqs/ | FAQs | Addresses frequently asked questions about GPU access, job submission, software installation, account setup, and troubleshooting. | Getting Started, Running Jobs, Software |
| https://orcd-docs.mit.edu/glossary/ | Glossary | Defines roughly 40 HPC and cluster-related technical terms (jobs, partitions, storage types, software tools, etc.). | Style reference, Glossary |
| https://orcd-docs.mit.edu/tags/ | Index (Tags) | Tag-based topic index organizing content across categories like GPU, Python, MPI, and Getting Started. | Style reference, Navigation |
| https://orcd-docs.mit.edu/acknowledgements/ | Acknowledging Us | Provides recommended citation language for publications that used ORCD resources. | Policy |
| https://orcd-docs.mit.edu/data-security/ | Data Security and Privacy | States that ORCD systems are suitable only for low-security data and points to future secure infrastructure options. | Policy, Data Security |
| https://orcd-docs.mit.edu/code-of-conduct/ | Acceptable Use and Code of Conduct | Rules restricting usage to MIT-affiliated research, data legitimacy requirements, account security, and community conduct expectations. | Policy |
| https://orcd-docs.mit.edu/transition-guide-satori/ | Satori to Engaging Transition Guide | Migration instructions for users moving from the retiring Satori system to Engaging, including data transfer and software setup. | Getting Started, Migration |
| https://orcd-docs.mit.edu/transition-guide-supercloud/ | SuperCloud to Engaging Transition Guide | Helps researchers transition from SuperCloud to Engaging, documenting key system differences and data/workload migration steps. | Getting Started, Migration |

---

## Accessing the System

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://orcd-docs.mit.edu/accessing-orcd/ondemand-login/ | Logging in with OnDemand | Step-by-step instructions for accessing Engaging through the OnDemand web portal using Globus/MIT Kerberos authentication. | Getting Started, Access |
| https://orcd-docs.mit.edu/accessing-orcd/ssh-login/ | Logging in with SSH via Terminal | How to access Engaging via SSH terminal with OS-specific setup and the login command `ssh [username]@orcd-login.mit.edu`. | Getting Started, Access |
| https://orcd-docs.mit.edu/accessing-orcd/ssh-setup/ | SSH Key Setup | Generating SSH key pairs, uploading them to Engaging, and configuring key-based authentication. | Getting Started, Access |
| https://orcd-docs.mit.edu/accessing-orcd/control-channels/ | SSH Control Channels | Using OpenSSH ControlChannel to multiplex SSH sessions through a single two-factor authentication login. | Access |

---

## Filesystems and File Transfer

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://orcd-docs.mit.edu/filesystems-file-transfer/filesystems/ | General Use Filesystems | Describes the three storage spaces (home, pool, scratch) with their purposes, paths, quotas, and backup status. | Filesystem |
| https://orcd-docs.mit.edu/filesystems-file-transfer/transferring-files/ | Transferring Files | Methods for moving data to/from Engaging: OnDemand file browser, Globus, scp, rsync, and graphical tools. | Filesystem, Data Transfer |
| https://orcd-docs.mit.edu/filesystems-file-transfer/lustre-best-practices/ | Lustre Best Practices | Performance guidelines for the Lustre parallel filesystem, including avoiding `ls -l` and concurrent file access. | Filesystem |
| https://orcd-docs.mit.edu/filesystems-file-transfer/project-filesystems/ | Project Specific Filesystems | Redirect stub -- content moved to the Storage Services page. | Filesystem |

---

## Software

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://orcd-docs.mit.edu/software/overview/ | Software Overview | How to find and install software on Engaging; describes Core, Community, and Deprecated software categories. | Software |
| https://orcd-docs.mit.edu/software/modules/ | Modules | Using the module system (`module avail`, `module load`, `module purge`) to manage software versions and environments. | Software |
| https://orcd-docs.mit.edu/software/python/ | Python | Installing and managing Python packages via virtual environments and conda, plus troubleshooting common issues. | Software |
| https://orcd-docs.mit.edu/software/julia/ | Julia | Loading Julia modules, installing packages, version management with Juliaup, and Jupyter/VS Code integration. | Software |
| https://orcd-docs.mit.edu/software/R/ | R | Using R on Engaging via Conda, pre-installed modules, RStudio access, and Jupyter integration. | Software |
| https://orcd-docs.mit.edu/software/compile/ | Compiling Codes | Fundamentals of building C/C++ from source: compilation stages, multi-file projects, library linking, and GNU Make. | Software |
| https://orcd-docs.mit.edu/software/apptainer/ | Containers (Apptainer) | Using Apptainer/Singularity containers on ORCD: downloading images, building custom containers with definition files. | Software, Containers |
| https://orcd-docs.mit.edu/software/licensed/ | Licensed Software | Three-step process for using licensed software: obtaining a license, hosting/installing it, and restricting access. | Software, Policy |
| https://orcd-docs.mit.edu/software/building-software/ | Other Software (Building from Source) | Step-by-step workflow for compiling and installing software from source: configure, build, install, PATH setup. | Software |

---

## Running Jobs

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://orcd-docs.mit.edu/running-jobs/overview/ | Scheduler Overview | Using Slurm on Engaging: partitions, resource allocation, commands for interactive and batch jobs, monitoring and management. | Running Jobs |
| https://orcd-docs.mit.edu/running-jobs/requesting-resources/ | Requesting Resources | How to request cores, MPI processes, memory, and GPUs for computational jobs. | Running Jobs |
| https://orcd-docs.mit.edu/running-jobs/job-arrays/ | Job Arrays | Submitting and managing job arrays with different inputs; includes Python, Julia, and Bash examples. | Running Jobs |
| https://orcd-docs.mit.edu/running-jobs/available-resources/ | Available Resources | Catalog of node specs, processor types, memory configurations, and GPU availability across Engaging's five partitions. | Running Jobs, Hardware |
| https://orcd-docs.mit.edu/running-jobs/application-analysis/ | Application Analysis | Using `jobstats`, `htop`, `nvidia-smi`, and `nvtop` to monitor resource usage and optimize job efficiency. | Running Jobs, Monitoring |

---

## Services

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://orcd-docs.mit.edu/services/compute-services/ | Compute Services | Paid Standard and Advanced service tiers with higher resource limits, priority access, and advance rental reservations. | Services, Policy |
| https://orcd-docs.mit.edu/services/storage-services/ | Storage Services | Renting additional storage (Data and Compute tiers), pricing structure (min 20 TiB), and how to request it. | Services, Filesystem |
| https://orcd-docs.mit.edu/services/hosted-hardware/ | Hardware Purchases | Process for research groups to buy and host hardware on Engaging: vendor negotiation, installation, maintenance, and retirement. | Services, Hardware |
| https://orcd-docs.mit.edu/services/accessing-group-resources/ | Accessing Group Resources | Managing access to group storage and hardware via MIT Web Moira list membership. | Services, Access |

---

## Recipes -- AI/ML

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://orcd-docs.mit.edu/recipes/torch-gpu/ | PyTorch on GPUs - I | Installing and running PyTorch on GPUs: single-GPU, single-node multi-GPU, and multi-node multi-GPU data parallel configurations. | Software, GPU, AI/ML |
| https://orcd-docs.mit.edu/recipes/torch-gpu-intermediate/ | PyTorch on GPUs - II | Intermediate distributed deep learning: Fully Sharded Data Parallel (FSDP) and hybrid FSDP with Tensor Parallel for large models. | Software, GPU, AI/ML |
| https://orcd-docs.mit.edu/recipes/rag/ | Running Your Own RAG Model | Deploying a Retrieval-Augmented Generation model on Engaging using a Mistral LLM, with container and Python execution methods. | Software, AI/ML |
| https://orcd-docs.mit.edu/recipes/af3/ | Running AlphaFold 3 on Engaging | Setting up and running AlphaFold 3 protein structure prediction, including model weights, container images, and datasets. | Software, AI/ML, Science |
| https://orcd-docs.mit.edu/recipes/h100_getting_started/ | Getting Started on 8-way H100 Nodes (Satori) | Accessing and running jobs on IBM Watson AI Lab H100 GPU nodes, including PyTorch environment setup. | GPU, AI/ML, Hardware |

---

## Recipes -- Scientific Software

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://orcd-docs.mit.edu/recipes/gromacs/ | Installing and Using GROMACS | Compiling GROMACS with MPI support on Engaging and submitting molecular dynamics simulation batch jobs. | Software, Science |
| https://orcd-docs.mit.edu/recipes/cryosparc/ | Installing CryoSPARC on Engaging | Step-by-step user-space deployment of CryoSPARC for automated cryo-EM data processing and analysis. | Software, Science |
| https://orcd-docs.mit.edu/recipes/relion/ | Installing RELION on Engaging | Building RELION 5.0 for cryo-EM structure determination, including prerequisites, compilation, and usage examples. | Software, Science |
| https://orcd-docs.mit.edu/recipes/orca/ | Installing ORCA for Personal Use | Downloading, installing, and running the ORCA quantum chemistry package sequentially and with MPI parallelization. | Software, Science |
| https://orcd-docs.mit.edu/recipes/build-vasp-gcc-cpu/ | VASP | Compiling VASP quantum chemistry software on Rocky Linux, creating a module, and running it on Engaging. | Software, Science |
| https://orcd-docs.mit.edu/recipes/mujoco/ | Installing and Using MuJoCo | Archived guide for installing the MuJoCo physics engine and Python bindings for computational jobs. | Software, Science |
| https://orcd-docs.mit.edu/recipes/openclaw-engaging/ | Running OpenClaw AI Assistant on Engaging | Deploying the OpenClaw open-source AI assistant via Apptainer containers to connect to cloud LLM providers on the cluster. | Software, AI/ML, Containers |

---

## Recipes -- Parallel Computing & HPC Tools

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://orcd-docs.mit.edu/recipes/mpi/ | MPI Jobs | Using MPI for parallel computing: module loading, building MPI programs, job submission, and hybrid MPI+multithreading. | Running Jobs, Software |
| https://orcd-docs.mit.edu/recipes/mpi4py/ | MPI for Python (mpi4py) | Installing and using Python MPI bindings for parallel applications, with point-to-point communication examples and job scripts. | Running Jobs, Software |
| https://orcd-docs.mit.edu/recipes/nvhpc-a100-with-cuda-and-mpi-example/ | NVHPC with CUDA-aware MPI | Using NVIDIA NVHPC toolkit to compile and run multi-GPU MPI programs with GPU-to-GPU communication. | Running Jobs, GPU, Software |
| https://orcd-docs.mit.edu/recipes/intel/ | Intel Compiler | Setting up and using the Intel compiler for C/Fortran codes, including MPI support for multi-node parallel programs. | Software |
| https://orcd-docs.mit.edu/recipes/many-jobs/ | Advanced Job Array | Combining serial execution, parallel execution, and job arrays to submit thousands of programs within the 500-job limit. | Running Jobs |

---

## Recipes -- Development Tools & Access

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://orcd-docs.mit.edu/recipes/jupyter/ | Jupyter Notebooks | Running Jupyter on Engaging via OnDemand, VS Code, or port forwarding, with Python/Julia/R kernel setup. | Software, Getting Started |
| https://orcd-docs.mit.edu/recipes/vscode/ | VSCode Remote SSH | Setting up VS Code Remote SSH to develop on Engaging, connecting through login nodes to compute nodes. | Software, Access |
| https://orcd-docs.mit.edu/recipes/pycharm/ | PyCharm | Configuring PyCharm SSH remote development on Engaging, including compute node allocation. | Software, Access |
| https://orcd-docs.mit.edu/recipes/X11/ | X11 | Displaying graphical UIs from Engaging on local Mac/Linux machines via X11 forwarding. | Access |
| https://orcd-docs.mit.edu/recipes/julia_install/ | Julia Install | Redirect stub -- directs users to the main Julia software page. | Software |

---

## Summary Statistics

| Section | Page Count |
|---------|-----------|
| General / Top-Level | 12 |
| Accessing the System | 4 |
| Filesystems & File Transfer | 4 |
| Software | 9 |
| Running Jobs | 5 |
| Services | 4 |
| Recipes -- AI/ML | 5 |
| Recipes -- Scientific Software | 7 |
| Recipes -- Parallel Computing & HPC | 5 |
| Recipes -- Dev Tools & Access | 5 |
| **Total** | **60 entries (52 unique content pages, 2 redirects, 6 index/nav pages)** |
