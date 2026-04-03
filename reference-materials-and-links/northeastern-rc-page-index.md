# Northeastern University Research Computing -- Page Index

Source: https://rc-docs.northeastern.edu/en/latest/
Crawled: 2026-04-03

---

## Home / Top-Level

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://rc-docs.northeastern.edu/en/latest/index.html | Explorer User Guides | Landing page for Northeastern's Explorer HPC cluster documentation with navigation to all sections including connecting, running jobs, GPUs, data management, software, and best practices. | Getting Started |
| https://rc-docs.northeastern.edu/en/latest/glossary.html | Glossary | Defines HPC-related terminology and abbreviations such as backfilling, cluster, GPU acceleration, and Slurm relevant to cluster computing. | Getting Started |
| https://rc-docs.northeastern.edu/en/latest/faq.html | Frequently Asked Questions (FAQs) | Addresses common questions about the HPC cluster including OOD job failures, account access after graduation, software installation, and technical configurations. | Troubleshooting |

## Connecting to Explorer

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://rc-docs.northeastern.edu/en/latest/connectingtocluster/index.html | Connecting To Explorer | Overview of methods for accessing the Explorer HPC cluster through terminal SSH connections and the Open OnDemand web interface, with platform-specific links. | Access |
| https://rc-docs.northeastern.edu/en/latest/connectingtocluster/mac.html | Connecting on a Mac | Step-by-step instructions for Mac users to connect to Explorer via SSH, configure passwordless authentication, and enable X11 forwarding for GUI applications. | Access |
| https://rc-docs.northeastern.edu/en/latest/connectingtocluster/windows.html | Connecting on Windows | Step-by-step instructions for Windows users to connect using SSH terminal programs with detailed guidance on MobaXterm, passwordless authentication, and X11 forwarding. | Access |
| https://rc-docs.northeastern.edu/en/latest/connectingtocluster/linux.html | Connecting on Linux | Step-by-step instructions for Linux users to connect to Explorer via SSH, including passwordless authentication setup and X11 forwarding for GUI applications. | Access |

## Running Jobs

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://rc-docs.northeastern.edu/en/latest/runningjobs/index.html | Running Jobs | Overview of executing computational tasks on the HPC cluster covering job scheduling, submission methods, and management through the Slurm workload manager. | Running Jobs |
| https://rc-docs.northeastern.edu/en/latest/runningjobs/understandingqueuing.html | Understanding the Queuing System | Explains how Slurm manages job scheduling using fair-share policies that balance resources based on historical usage, job size, and queue wait time. | Running Jobs |
| https://rc-docs.northeastern.edu/en/latest/runningjobs/slurmmonitoringandmanaging.html | Monitoring and Managing Jobs | Guide to using Slurm commands (sinfo, squeue, scancel) to check cluster/partition status, monitor job queues, and cancel running or pending jobs. | Running Jobs |
| https://rc-docs.northeastern.edu/en/latest/runningjobs/interactiveandbatch.html | Interactive and Batch Mode | Explains how to submit jobs using srun for real-time interactive sessions and sbatch for passive script execution, with detailed examples and parameter explanations. | Running Jobs |
| https://rc-docs.northeastern.edu/en/latest/runningjobs/runningsjob.html | Running Jobs with job-assist | Documents the job-assist command-line tool for streamlined job submission through default, interactive, and batch operational modes. | Running Jobs |
| https://rc-docs.northeastern.edu/en/latest/runningjobs/slurmarray.html | Slurm Jobs Array | Explains how to use Slurm job arrays to efficiently submit and manage multiple similar jobs, including resource allocation, environment variables, and index ranges. | Running Jobs |

## Working with GPUs

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://rc-docs.northeastern.edu/en/latest/gpus/index.html | Working with GPUs | Overview of GPU resources for computational acceleration on the HPC cluster covering access methods, job submission, and optimization strategies. | GPU |
| https://rc-docs.northeastern.edu/en/latest/gpus/gpuoverview.html | GPUs on the HPC | Details the GPU resources available on Explorer, including the gpu and multigpu partitions with their access requirements, job limits, and usage guidelines. | GPU |
| https://rc-docs.northeastern.edu/en/latest/gpus/accessinggpus.html | GPU Access | Instructions for submitting GPU jobs using srun and sbatch commands with guidance on specifying GPU types and partition options. | GPU |
| https://rc-docs.northeastern.edu/en/latest/gpus/gpujobsubmission.html | GPU Job Submission | Instructions for submitting GPU jobs including how to access and load CUDA toolkits and install deep learning frameworks like PyTorch and TensorFlow with GPU support. | GPU, AI/ML |
| https://rc-docs.northeastern.edu/en/latest/gpus/multigpu-partition-access.html | Access to Multi-GPU Partition | Step-by-step guide for requesting multi-GPU partition access including application submission, testing on temporary reservations, and demonstrating scaling efficiency. | GPU, Policy |
| https://rc-docs.northeastern.edu/en/latest/gpus/quickstart-h200.html | Quick Start Guide for H200s | Instructions for accessing and using H200 GPUs on Explorer through srun, sbatch, and Open OnDemand interfaces with specific resource request parameters. | GPU, AI/ML |
| https://rc-docs.northeastern.edu/en/latest/gpus/idlebot.html | IdleBot | Explains the IdleBot monitoring system that tracks GPU utilization, sends warning emails after 15 minutes of underuse, and cancels jobs after one hour of idleness. | GPU, Policy |

## Data Management

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://rc-docs.northeastern.edu/en/latest/datamanagement/index.html | Data Management | Overview of data management as a critical aspect of HPC usage, covering secure data transfers and storage guidance for the cluster. | Data Transfer |
| https://rc-docs.northeastern.edu/en/latest/datamanagement/transferringdata.html | Transfer Data | Comprehensive instructions for transferring files using the dedicated transfer node (xfer.discovery.neu.edu) via SCP, rsync, rclone, FileZilla, and MobaXterm. | Data Transfer |
| https://rc-docs.northeastern.edu/en/latest/datamanagement/globus.html | Using Globus | Setup and usage instructions for Globus data management including account creation, installing Globus Connect Personal, and performing file transfers between Explorer and personal computers. | Data Transfer |

## Managing /projects

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://rc-docs.northeastern.edu/en/latest/managingprojects/index.html | Managing /projects | Describes custom software for the Explorer cluster enabling PIs to manage research group access, user permissions, guest accounts, and directory controls. | Filesystem |
| https://rc-docs.northeastern.edu/en/latest/managingprojects/terminology.html | Terminology | Defines key vocabulary for managing /projects on Explorer, explaining five user types with different access levels and the TTL (Time To Live) concept. | Filesystem |
| https://rc-docs.northeastern.edu/en/latest/managingprojects/cheatsheet.html | Projects Cheatsheet | Provides a downloadable PDF cheatsheet summarizing commands and best practices for managing /projects on the Explorer cluster. | Filesystem |
| https://rc-docs.northeastern.edu/en/latest/managingprojects/commands.html | Commands | Detailed instructions for managing research group access using the project command interface, including viewing members, adding/removing users, and updating group information. | Filesystem |

## Software

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://rc-docs.northeastern.edu/en/latest/software/index.html | Software | Overview of software options on Explorer describing system-wide modules, package managers, and source compilation methods. | Software |

### System Wide

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://rc-docs.northeastern.edu/en/latest/software/systemwide/index.html | System Wide | Hub page for system-wide software on the cluster with quick access to guides for modules, MPI, R, and MATLAB. | Software |
| https://rc-docs.northeastern.edu/en/latest/software/systemwide/modules.html | Using Module | Comprehensive guidance on the module system for managing software environments, including commands, examples, best practices, and troubleshooting. | Software |
| https://rc-docs.northeastern.edu/en/latest/software/systemwide/module_list.html | Northeastern RC Software Modules | Reference table of all software applications available on Explorer with descriptions and version numbers loadable through the module system. | Software |
| https://rc-docs.northeastern.edu/en/latest/software/systemwide/mpi.html | Using MPI | Guidance on implementing MPI for parallel computing including module loading, job submission, performance optimization, debugging, and code examples in C/C++ and Python. | Software, Running Jobs |
| https://rc-docs.northeastern.edu/en/latest/software/systemwide/r.html | Using R | Instructions for running R on Explorer through Open OnDemand's interactive RStudio application or as batch jobs using Apptainer containers. | Software |
| https://rc-docs.northeastern.edu/en/latest/software/systemwide/matlab.html | Using MATLAB | Comprehensive instructions for installing MATLAB toolboxes, configuring MATLAB Parallel Server, and submitting interactive and batch jobs using the Parallel Computing Toolbox. | Software |

### Package Managers

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://rc-docs.northeastern.edu/en/latest/software/packagemanagers/index.html | Package Managers | Introduction to package managers as tools for creating customized computational environments on Explorer. | Software |
| https://rc-docs.northeastern.edu/en/latest/software/packagemanagers/conda.html | Conda | Comprehensive instructions for using Conda on Explorer covering environment creation in /projects, management, Miniconda installation, and best practices for storage. | Software |
| https://rc-docs.northeastern.edu/en/latest/software/packagemanagers/spack.html | Spack | Step-by-step instructions for installing and using Spack to deploy software packages locally on Explorer, with a detailed LAMMPS installation example. | Software |

### From Source

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://rc-docs.northeastern.edu/en/latest/software/fromsource/index.html | From Source | Index page for building software from source on Explorer providing access to Make and CMake guides. | Software |
| https://rc-docs.northeastern.edu/en/latest/software/fromsource/makefile.html | Make | Step-by-step instructions for compiling software from source using makefiles, with practical examples using FFTW and LAMMPS. | Software |
| https://rc-docs.northeastern.edu/en/latest/software/fromsource/cmake.html | CMake | Instructions for building LAMMPS from source using CMake on Explorer covering serial and parallel (MPI-enabled) build configurations with example job scripts. | Software |

## Courses on Explorer

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://rc-docs.northeastern.edu/en/latest/classroom/index.html | Courses on Explorer | Resources for instructors and students integrating HPC capabilities into classroom instruction at Northeastern University. | Training |
| https://rc-docs.northeastern.edu/en/latest/classroom/class_guide.html | Course Guide | Explains how instructors can access HPC resources for classroom use, detailing course directory setup, computing partitions, job submission, and software options. | Training |
| https://rc-docs.northeastern.edu/en/latest/classroom/cheatsheet.html | Courses Cheatsheet | Downloadable PDF cheatsheet for quickly accessing key information and commands related to running courses on the Explorer cluster. | Training |

## Containers on Explorer

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://rc-docs.northeastern.edu/en/latest/containers/index.html | Containers on Explorer | Explains that containers are packaged software solutions for reproducible workflows, with Explorer supporting Apptainer/Singularity technology. | Software |
| https://rc-docs.northeastern.edu/en/latest/containers/apptainer.html | Apptainer on Explorer | Instructions for running container images using Apptainer including the --bind flag for mounting directories, interactive/batch submission, and pulling images from Docker Hub. | Software |
| https://rc-docs.northeastern.edu/en/latest/containers/containers_list.html | Containers | Directory of 15 containerized scientific software applications available in Explorer's container repository with descriptions and version numbers. | Software |

## Best Practices

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://rc-docs.northeastern.edu/en/latest/best-practices/index.html | Best Practices | Overview of essential best practices for managing HPC resources on Explorer covering storage quotas, job checkpointing, and cluster usage guidelines. | Policy |
| https://rc-docs.northeastern.edu/en/latest/best-practices/homequota.html | Home Directory Storage Quota | Best practices for managing /home storage quotas including checking quotas, analyzing disk usage, cleaning files, and using /projects and /scratch alternatives. | Filesystem |
| https://rc-docs.northeastern.edu/en/latest/best-practices/workquota.html | Projects Directory Storage Quota | Guidance on managing /projects storage quotas including monitoring usage, compressing unused directories, and deleting intermediate files. | Filesystem |
| https://rc-docs.northeastern.edu/en/latest/best-practices/scratchpurge.html | Scratch Directory Purge | Explains monthly /scratch purge procedures and how to prepare by transferring important files to /projects or /home with command examples. | Filesystem |
| https://rc-docs.northeastern.edu/en/latest/best-practices/checkpointing.html | Checkpointing Jobs | Explains four checkpointing types (application-level, user-level, system-level, model-level) with examples using GROMACS, DMTCP, TensorFlow, and PyTorch. | Running Jobs, AI/ML |
| https://rc-docs.northeastern.edu/en/latest/best-practices/shell_environment.html | Shell Environment on the Cluster | Guidance on managing .bashrc on Explorer's Linux system including risks, editing procedures, and safer alternatives like sourcing shell scripts within jobs. | Cluster Info |
| https://rc-docs.northeastern.edu/en/latest/best-practices/clusterusage.html | Cluster Usage | Guidance on appropriate resource allocation including when to use compute vs. login nodes, data transfer procedures, and tools (seff, historical-seff, gpu-logs) for measuring job efficiency. | Running Jobs, Policy |
| https://rc-docs.northeastern.edu/en/latest/best-practices/transition.html | Quick Start to Explorer | Outlines differences between Discovery and Explorer clusters with transition guidance on login procedures, /projects storage paths, module changes, and conda environment migration. | Getting Started |

---

## Summary Statistics

| Section | Page Count |
|---------|-----------|
| Home / Top-Level | 3 |
| Connecting to Explorer | 4 |
| Running Jobs | 6 |
| Working with GPUs | 7 |
| Data Management | 3 |
| Managing /projects | 4 |
| Software (top-level) | 1 |
| Software -- System Wide | 6 |
| Software -- Package Managers | 3 |
| Software -- From Source | 3 |
| Courses on Explorer | 3 |
| Containers on Explorer | 3 |
| Best Practices | 8 |
| **Total** | **54** |
