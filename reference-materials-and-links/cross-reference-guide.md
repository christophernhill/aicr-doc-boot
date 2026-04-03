# Cross-Reference Guide

Maps each AICR documentation section to the best reference pages across all indexed reference sites. When drafting or revising a section, fetch the listed pages for style, structure, and content-depth calibration.

**Sites indexed**: MIT ORCD, Yale YCRC, UMass Unity, Kempner Institute (Harvard), Harvard FASRC, BU Research Computing, Northeastern RC

## Getting Started

The getting-started page should walk a new user from "I have an account" to "my first job completed." Match the progressive, tutorial-style approach of these references.

| Reference Page | Site | Why It's Useful |
|---------------|------|-----------------|
| [Getting Started Tutorial](https://orcd-docs.mit.edu/getting-started/) | MIT ORCD | Best single-page onboarding flow — covers architecture, Linux basics, modules, first job |
| [Get Started with HPC and Unity](https://docs.unity.rc.umass.edu/documentation/get-started/) | UMass Unity | Hub-page approach with links to quickstart, terminology, and theory |
| [Quick Start Guide](https://docs.unity.rc.umass.edu/documentation/get-started/quickstart/) | UMass Unity | Comprehensive quickstart covering resource selection, scheduling, monitoring, and storage |
| [Getting Started](https://docs.ycrc.yale.edu/clusters-at-yale/) | Yale YCRC | Orientation for new users — accounts, login, jobs, software, support |
| [Introduction to HPC Tutorials](https://docs.ycrc.yale.edu/resources/intro_to_hpc_tutorial/) | Yale YCRC | Three hands-on exercises: interactive jobs, batch jobs, Jupyter |
| [Common Terms](https://docs.unity.rc.umass.edu/documentation/get-started/common-terms/) | UMass Unity | Good model for an HPC glossary section |
| [Intro to Kempner AI Cluster Workshop](https://handbook.eng.kempnerinstitute.harvard.edu/s9_workshops_and_trainings/intro_to_kempner_ai_cluster/intro_to_kempner_ai_cluster.html) | Kempner | Workshop-style onboarding for a GPU-focused AI cluster at MGHPCC — closest analogue to AICR's user base |
| [User Quick Start Guide](https://docs.rc.fas.harvard.edu/kb/quickstart-guide/) | Harvard FASRC | Concise quickstart covering account, 2FA, VPN, and first cluster operations |

## Logging In / Access

| Reference Page | Site | Why It's Useful |
|---------------|------|-----------------|
| [Logging in with OnDemand](https://orcd-docs.mit.edu/accessing-orcd/ondemand-login/) | MIT ORCD | Clean OnDemand login walkthrough |
| [Logging in with SSH](https://orcd-docs.mit.edu/accessing-orcd/ssh-login/) | MIT ORCD | SSH access with OS-specific setup |
| [SSH Connection](https://docs.ycrc.yale.edu/clusters-at-yale/access/ssh/) | Yale YCRC | SSH key generation per platform (macOS, Linux, Windows) |
| [Connect via Unity OnDemand](https://docs.unity.rc.umass.edu/documentation/connecting/ondemand/) | UMass Unity | Web portal access without SSH keys |
| [SSH](https://docs.unity.rc.umass.edu/documentation/connecting/ssh/) | UMass Unity | SSH key setup and CLI connection |
| [Access the Web Portal](https://docs.ycrc.yale.edu/clusters-at-yale/access/ood/) | Yale YCRC | OnDemand shell, files, and interactive apps |
| [Multi-factor Authentication](https://docs.ycrc.yale.edu/clusters-at-yale/access/mfa/) | Yale YCRC | Duo MFA setup — reference if AICR adopts 2FA |
| [Connecting Desktop VS Code](https://docs.unity.rc.umass.edu/documentation/connecting/vscode/) | UMass Unity | VS Code Remote SSH setup |
| [VSCode Remote SSH](https://orcd-docs.mit.edu/recipes/vscode/) | MIT ORCD | VS Code through login nodes to compute nodes |
| [Accessing the Cluster](https://handbook.eng.kempnerinstitute.harvard.edu/s1_high_performance_computing/kempner_cluster/accessing_and_navigating_the_cluster.html) | Kempner | SSH + OnDemand + 2FA for an MGHPCC-based AI cluster — directly analogous to AICR access |
| [Connecting to the SCC](https://www.bu.edu/tech/support/research/system-usage/connect-scc/) | BU RC | Comprehensive connection overview: OnDemand, SSH, VNC, port forwarding |
| [Connecting on Mac](https://rc-docs.northeastern.edu/en/latest/connectingtocluster/mac.html) | Northeastern RC | Platform-specific SSH guide with screenshots — good template for per-OS instructions |

## Cluster / System Overview

| Reference Page | Site | Why It's Useful |
|---------------|------|-----------------|
| [Bouchet](https://docs.ycrc.yale.edu/clusters/bouchet/) | Yale YCRC | Best model for a cluster overview page — partitions, specs, storage, access, all in one |
| [Bouchet AMD Nodes](https://docs.ycrc.yale.edu/clusters/bouchet_amd/) | Yale YCRC | How to present mixed CPU/GPU architectures with cross-compilation notes |
| [AICR (at Yale)](https://docs.ycrc.yale.edu/clusters/aicr/) | Yale YCRC | Yale's own description of AICR — verify our docs are consistent |
| [ORCD Engaging System](https://orcd-docs.mit.edu/orcd-systems/) | MIT ORCD | Concise system overview for a mixed CPU/GPU cluster |
| [Unity Specifications](https://docs.unity.rc.umass.edu/documentation/cluster_specs/) | UMass Unity | Specs hub linking to nodes, partitions, storage, features |
| [Unity Nodes](https://docs.unity.rc.umass.edu/documentation/cluster_specs/nodes/) | UMass Unity | Comprehensive node inventory table |
| [Unity Partitions](https://docs.unity.rc.umass.edu/documentation/cluster_specs/partitions/) | UMass Unity | Partition listing with time limits and access restrictions |
| [Overview of Kempner Cluster](https://handbook.eng.kempnerinstitute.harvard.edu/s1_high_performance_computing/kempner_cluster/overview_of_kempner_cluster.html) | Kempner | GPU-focused AI cluster at MGHPCC with A100/H100 GPUs — closest hardware analogue to AICR |
| [Shared Computing Cluster (SCC)](https://www.bu.edu/tech/support/research/computing-resources/scc/) | BU RC | How BU presents a large heterogeneous cluster overview |

## Filesystem / Storage

| Reference Page | Site | Why It's Useful |
|---------------|------|-----------------|
| [General Use Filesystems](https://orcd-docs.mit.edu/filesystems-file-transfer/filesystems/) | MIT ORCD | Three-tier storage (home/pool/scratch) with quotas and backup status |
| [HPC Storage](https://docs.ycrc.yale.edu/data/hpc-storage/) | Yale YCRC | Home/Project/Scratch with quota monitoring and best practices |
| [Storage](https://docs.unity.rc.umass.edu/documentation/cluster_specs/storage/) | UMass Unity | Three-tier storage with snapshot restoration |
| [Disk Quotas](https://docs.unity.rc.umass.edu/documentation/managing-files/quotas/) | UMass Unity | Checking usage, finding large files, reducing bloat |
| [HPC Workspace (Scratch)](https://docs.unity.rc.umass.edu/documentation/managing-files/hpc-workspace/) | UMass Unity | Temporary scratch allocation model |
| [Backups and Snapshots](https://docs.ycrc.yale.edu/data/backups/) | Yale YCRC | Snapshot retrieval instructions — model for our Snapshots recipe |
| [Stage Data for Compute Jobs](https://docs.ycrc.yale.edu/data/staging/) | Yale YCRC | Data staging workflow for large datasets |
| [Share with Cluster Users](https://docs.ycrc.yale.edu/data/permissions/) | Yale YCRC | Linux permissions and ACLs for shared data |
| [Storage Options](https://handbook.eng.kempnerinstitute.harvard.edu/s1_high_performance_computing/storage_and_data_transfer/understanding_storage_options.html) | Kempner | Three-tier storage (home/lab/scratch) with 90-day scratch retention — AI cluster perspective |
| [Scratch Directory Purge](https://rc-docs.northeastern.edu/en/latest/best-practices/scratchpurge.html) | Northeastern RC | Clear documentation of monthly scratch purge procedures — good model for AICR scratch policy |
| [Storage Quotas](https://www.bu.edu/tech/support/research/system-usage/using-file-system/storage-quotas/) | BU RC | Quota enforcement documentation |
| [Recovering Lost Files](https://www.bu.edu/tech/support/research/system-usage/using-file-system/recovering-lost-files/) | BU RC | File recovery procedures — reference for our Snapshots recipe |

## Transferring Data

| Reference Page | Site | Why It's Useful |
|---------------|------|-----------------|
| [Transferring Files](https://orcd-docs.mit.edu/filesystems-file-transfer/transferring-files/) | MIT ORCD | OnDemand, Globus, scp, rsync, graphical tools |
| [Transfer to Cluster](https://docs.ycrc.yale.edu/data/transfer/) | Yale YCRC | scp, rsync, Globus, transfer nodes |
| [Large Transfers with Globus](https://docs.ycrc.yale.edu/data/globus/) | Yale YCRC | Detailed Globus guide including cloud storage |
| [Managing Files](https://docs.unity.rc.umass.edu/documentation/managing-files/) | UMass Unity | Overview of upload methods (OnDemand, FileZilla, Globus, CLI) |
| [Globus](https://docs.unity.rc.umass.edu/documentation/managing-files/globus/) | UMass Unity | Globus Connect setup for UMass |
| [FileZilla](https://docs.unity.rc.umass.edu/documentation/managing-files/filezilla/) | UMass Unity | GUI SFTP setup example |

## Software / Modules

| Reference Page | Site | Why It's Useful |
|---------------|------|-----------------|
| [Software Overview](https://orcd-docs.mit.edu/software/overview/) | MIT ORCD | Core/Community/Deprecated software categories |
| [Modules](https://orcd-docs.mit.edu/software/modules/) | MIT ORCD | module avail, load, purge walkthrough |
| [Software Modules (Lmod)](https://docs.ycrc.yale.edu/applications/modules/) | Yale YCRC | Hierarchical toolchains, module collections |
| [Introduction to Environment Modules](https://docs.unity.rc.umass.edu/documentation/software/modules/) | UMass Unity | Beginner-friendly explanation of how modules modify PATH |
| [Module Usage](https://docs.unity.rc.umass.edu/documentation/software/modules/module-usage/) | UMass Unity | Practical listing, searching, loading, unloading |
| [Python](https://orcd-docs.mit.edu/software/python/) | MIT ORCD | Virtual environments, conda, troubleshooting |
| [Conda Environments](https://docs.unity.rc.umass.edu/documentation/software/conda/) | UMass Unity | Conda on HPC: creation, activation, JupyterHub integration |
| [Containers (Apptainer)](https://orcd-docs.mit.edu/software/apptainer/) | MIT ORCD | Apptainer images, builds, definition files |
| [Containers (Apptainer)](https://docs.ycrc.yale.edu/clusters-at-yale/guides/containers/) | Yale YCRC | Pre-existing images, custom builds, Dockerfile conversion |
| [Building Software from Scratch](https://docs.unity.rc.umass.edu/documentation/software/softwarefromscratch/) | UMass Unity | Compiling from source on a cluster |
| [Conda Environment](https://handbook.eng.kempnerinstitute.harvard.edu/s1_high_performance_computing/development_and_runtime_envs/using_conda_env.html) | Kempner | Conda on an AI-focused HPC cluster: custom directories, Jupyter integration, export for reproducibility |
| [Containerization](https://handbook.eng.kempnerinstitute.harvard.edu/s1_high_performance_computing/development_and_runtime_envs/containerization.html) | Kempner | Docker-to-Singularity conversion for PyTorch on HPC — AI-focused container workflows |
| [Module Basics](https://www.bu.edu/tech/support/research/software-and-programming/software-and-applications/modules/) | BU RC | Lmod module system walkthrough with BU-specific examples |
| [Apptainer on Explorer](https://rc-docs.northeastern.edu/en/latest/containers/apptainer.html) | Northeastern RC | Apptainer with --bind, interactive/batch, pulling from Docker Hub |

## Running Jobs / Slurm

| Reference Page | Site | Why It's Useful |
|---------------|------|-----------------|
| [Scheduler Overview](https://orcd-docs.mit.edu/running-jobs/overview/) | MIT ORCD | Partitions, interactive/batch, monitoring, management |
| [Requesting Resources](https://orcd-docs.mit.edu/running-jobs/requesting-resources/) | MIT ORCD | CPUs, memory, GPUs — how to request each |
| [Run Jobs with Slurm](https://docs.ycrc.yale.edu/clusters-at-yale/job-scheduling/) | Yale YCRC | Common commands, resource options, interactive/batch |
| [Submission Script Examples](https://docs.ycrc.yale.edu/clusters-at-yale/job-scheduling/slurm-examples/) | Yale YCRC | Single/multi-thread, MPI, hybrid, GPU script templates |
| [Slurm Cheat Sheet](https://docs.unity.rc.umass.edu/documentation/jobs/slurm/) | UMass Unity | Quick-reference tables of Slurm commands and flags |
| [Batch Jobs](https://docs.unity.rc.umass.edu/documentation/jobs/sbatch/) | UMass Unity | sbatch walkthrough with parameters and monitoring |
| [Interactive CLI Jobs](https://docs.unity.rc.umass.edu/documentation/jobs/salloc/) | UMass Unity | salloc resource allocation and node access |
| [Job Arrays](https://orcd-docs.mit.edu/running-jobs/job-arrays/) | MIT ORCD | Arrays with Python, Julia, Bash examples |
| [Array Batch Jobs](https://docs.unity.rc.umass.edu/documentation/jobs/sbatch/arrays/) | UMass Unity | --array parameter and SLURM_ARRAY_TASK_ID |
| [Job Arrays / dSQ](https://docs.ycrc.yale.edu/clusters-at-yale/job-scheduling/dsq/) | Yale YCRC | Job arrays plus Dead Simple Queue tool |
| [Common Job Failures](https://docs.ycrc.yale.edu/clusters-at-yale/job-scheduling/common-job-failures/) | Yale YCRC | Troubleshooting guide — model for our troubleshooting section |
| [Priority & Wait Time](https://docs.ycrc.yale.edu/clusters-at-yale/job-scheduling/fairshare/) | Yale YCRC | How to explain fairshare to users |
| [GPUs on Unity](https://docs.unity.rc.umass.edu/documentation/tools/gpus/) | UMass Unity | GPU requests, available types, Slurm examples, troubleshooting |
| [GPUs and CUDA](https://docs.ycrc.yale.edu/clusters-at-yale/guides/gpus-cuda/) | Yale YCRC | GPU requests, nvidia-smi, CUDA modules, compiling CUDA |
| [MPI](https://docs.unity.rc.umass.edu/documentation/jobs/mpi/) | UMass Unity | Multi-node MPI job configuration and execution |
| [MPI Jobs](https://orcd-docs.mit.edu/recipes/mpi/) | MIT ORCD | MPI module loading, building, submission, hybrid jobs |
| [Job Submission Basics](https://handbook.eng.kempnerinstitute.harvard.edu/s1_high_performance_computing/general_hpc_concepts/job_submission_basics.html) | Kempner | salloc and sbatch with SLURM directive examples on a GPU-focused AI cluster |
| [Batch Script Examples](https://www.bu.edu/tech/support/research/system-usage/running-jobs/batch-script-examples/) | BU RC | Wide range of batch script examples including GPU and MPI jobs |
| [Interactive and Batch Mode](https://rc-docs.northeastern.edu/en/latest/runningjobs/interactiveandbatch.html) | Northeastern RC | srun for interactive and sbatch for batch with detailed parameter explanations |
| [Checkpointing Jobs](https://rc-docs.northeastern.edu/en/latest/best-practices/checkpointing.html) | Northeastern RC | Four checkpointing types with GROMACS, DMTCP, TensorFlow, and PyTorch examples |

## GPU / AI-ML Workloads

| Reference Page | Site | Why It's Useful |
|---------------|------|-----------------|
| [PyTorch on GPUs - I](https://orcd-docs.mit.edu/recipes/torch-gpu/) | MIT ORCD | Single-GPU, single-node multi-GPU, multi-node DDP |
| [PyTorch on GPUs - II](https://orcd-docs.mit.edu/recipes/torch-gpu-intermediate/) | MIT ORCD | FSDP and hybrid FSDP+Tensor Parallel |
| [Multi-GPU Submission Scripts](https://docs.ycrc.yale.edu/ai/miniconda-multigpu/) | Yale YCRC | torchrun single-node and multi-node with Conda |
| [Installing PyTorch](https://docs.unity.rc.umass.edu/documentation/tools/pytorch/) | UMass Unity | PyTorch/CUDA version matrix, GPU compute capability |
| [PyTorch](https://docs.ycrc.yale.edu/clusters-at-yale/guides/pytorch/) | Yale YCRC | Pre-installed modules and custom installs |
| [Hugging Face](https://docs.ycrc.yale.edu/ai/huggingface/) | Yale YCRC | LLM loading, GPU selection, multi-GPU |
| [RAG Model](https://orcd-docs.mit.edu/recipes/rag/) | MIT ORCD | Retrieval-Augmented Generation recipe |
| [AlphaFold 3](https://orcd-docs.mit.edu/recipes/af3/) | MIT ORCD | Protein structure prediction recipe |
| [Ollama](https://docs.ycrc.yale.edu/ai/ollama/) | Yale YCRC | Local LLM inference on cluster |
| [Distributed GPU Computing](https://handbook.eng.kempnerinstitute.harvard.edu/s5_ai_scaling_and_engineering/scalability/distributed_gpu_computing.html) | Kempner | Six distributed training strategies (DDP through FSDP) with PyTorch examples and NCCL — most relevant for AICR's multi-GPU B200 nodes |
| [Distributed Inference](https://handbook.eng.kempnerinstitute.harvard.edu/s3_ai_workflows/distributed_inference.html) | Kempner | Multi-GPU LLM inference with vLLM, pipeline/tensor parallelism for Llama 3.1 and DeepSeek-R1 |
| [GPU Profiling](https://handbook.eng.kempnerinstitute.harvard.edu/s5_ai_scaling_and_engineering/scalability/gpu_profiling.html) | Kempner | PyTorch Profiler, HTA, and NVIDIA Nsight for identifying GPU bottlenecks |
| [NeMo Workflow](https://handbook.eng.kempnerinstitute.harvard.edu/s3_ai_workflows/nemo_workflow.html) | Kempner | NVIDIA NeMo for LLM pretraining/finetuning with SLURM integration |
| [Shared Data/Model Repository](https://handbook.eng.kempnerinstitute.harvard.edu/s1_high_performance_computing/storage_and_data_transfer/shared_data_repository.html) | Kempner | Centralized read-only ML model and dataset repository — model for AICR if it offers pre-loaded datasets |
| [Quick Start Guide for H200s](https://rc-docs.northeastern.edu/en/latest/gpus/quickstart-h200.html) | Northeastern RC | Onboarding for new GPU hardware (H200) — useful template for AICR B200 quickstart |
| [IdleBot](https://rc-docs.northeastern.edu/en/latest/gpus/idlebot.html) | Northeastern RC | GPU idle-job monitoring and auto-cancellation — policy model if AICR implements similar |
| [GPU Computing](https://www.bu.edu/tech/support/research/software-and-programming/gpu-computing/) | BU RC | GPU resource allocation, batch submission, and best practices |
| [Academic ML Environment](https://www.bu.edu/tech/support/research/software-and-programming/common-languages/python/python-ml/academic-machine-learning-environment/) | BU RC | Pre-configured conda environments with popular ML libraries — model for AICR module design |

## Recipes / Application Guides

| Reference Page | Site | Why It's Useful |
|---------------|------|-----------------|
| [GROMACS](https://orcd-docs.mit.edu/recipes/gromacs/) | MIT ORCD | Compile + batch job recipe — good template for scientific recipes |
| [CryoSPARC](https://orcd-docs.mit.edu/recipes/cryosparc/) | MIT ORCD | User-space deployment recipe |
| [AlphaFold](https://docs.ycrc.yale.edu/clusters-at-yale/guides/alphafold/) | Yale YCRC | AF2 and AF3 with batch scripts |
| [ColabFold](https://docs.unity.rc.umass.edu/documentation/tools/colabfold/) | UMass Unity | Interactive and batch protein folding |
| [Nextflow](https://docs.ycrc.yale.edu/clusters-at-yale/guides/nextflow/) | Yale YCRC | Pipeline framework with Slurm executor |
| [Jupyter Notebooks](https://orcd-docs.mit.edu/recipes/jupyter/) | MIT ORCD | OnDemand, VS Code, and port-forwarding methods |
| [Advanced Job Array](https://orcd-docs.mit.edu/recipes/many-jobs/) | MIT ORCD | Combining serial/parallel/array to run thousands of jobs |
| [LLM Distributed Training Workshop](https://handbook.eng.kempnerinstitute.harvard.edu/s9_workshops_and_trainings/llm_distributed_training/llm_distributed_training.html) | Kempner | DDP, Model/Tensor/Pipeline Parallelism, FSDP — hands-on workshop format for advanced AI recipes |
| [Scalable Vision Workflows](https://handbook.eng.kempnerinstitute.harvard.edu/s3_ai_workflows/scalable_vision_workflows.html) | Kempner | Distributed training for ResNet/AlexNet with SLURM — template for non-LLM AI recipes |

## Policy Pages

| Reference Page | Site | Why It's Useful |
|---------------|------|-----------------|
| [Acceptable Use and Code of Conduct](https://orcd-docs.mit.edu/code-of-conduct/) | MIT ORCD | Professional policy language for HPC acceptable use |
| [Cluster Usage Policies](https://docs.ycrc.yale.edu/clusters-at-yale/policies/) | Yale YCRC | Fair use policies, GPU utilization monitoring |
| [Data Security and Privacy](https://orcd-docs.mit.edu/data-security/) | MIT ORCD | Data classification and security posture |
| [Acknowledging Us](https://orcd-docs.mit.edu/acknowledgements/) | MIT ORCD | Citation language template |
| [Accounts & Best Practices](https://docs.ycrc.yale.edu/clusters-at-yale/access/accounts/) | Yale YCRC | Account policies and responsibilities |
| [Kempner Cluster Usage Policies](https://handbook.eng.kempnerinstitute.harvard.edu/s1_high_performance_computing/kempner_cluster/kempner_policies_for_responsible_use.html) | Kempner | Responsible use policy for a GPU-focused AI cluster — relevant framing for AICR |
| [Fairshare Policy](https://handbook.eng.kempnerinstitute.harvard.edu/s1_high_performance_computing/efficient_use_of_resources/fair_use_and_prioritization_policies.html) | Kempner | How to explain fairshare to AI researchers — complements Yale's coverage |
| [Best Practices](https://www.bu.edu/tech/support/research/system-usage/running-jobs/best-practices/) | BU RC | Responsible SCC use: login node limits, storage, shorter runtimes |
| [Process Reaper](https://www.bu.edu/tech/support/research/system-usage/running-jobs/process-reaper/) | BU RC | Automatic process termination for policy enforcement — reference if AICR implements similar |
| [Cluster Usage](https://rc-docs.northeastern.edu/en/latest/best-practices/clusterusage.html) | Northeastern RC | Resource allocation guidance with seff/gpu-logs tools for measuring efficiency |
| [Publication and Grant Writing Resources](https://www.bu.edu/tech/support/research/rcs/publications-and-grants/) | BU RC | Acknowledgment language for publications and grants — model for AICR's Acknowledging page |

## Support / Getting Help

| Reference Page | Site | Why It's Useful |
|---------------|------|-----------------|
| [Getting Help](https://orcd-docs.mit.edu/getting-help/) | MIT ORCD | Three support channels: docs, email, office hours |
| [Help Requests](https://docs.ycrc.yale.edu/clusters-at-yale/help-requests/) | Yale YCRC | How to write an effective help request |
| [How to Ask for Help](https://docs.unity.rc.umass.edu/documentation/help/asking-questions/) | UMass Unity | Guidelines for support requests |
| [FAQ](https://docs.unity.rc.umass.edu/documentation/help/faq/) | UMass Unity | Common questions and answers |
| [FAQs](https://orcd-docs.mit.edu/faqs/) | MIT ORCD | GPU access, jobs, software, accounts |
| [Troubleshoot Login](https://docs.ycrc.yale.edu/clusters-at-yale/troubleshoot/) | Yale YCRC | Login troubleshooting checklist |
| [Troubleshooting](https://docs.unity.rc.umass.edu/documentation/help/troubleshooting/) | UMass Unity | SSH, auth, job, and storage troubleshooting |
| [Submitting a Support Request](https://www.bu.edu/tech/support/research/system-usage/support-request/) | BU RC | Guidelines for effective support requests — commands, errors, reproduction steps |

## Style and Structure Reference

These pages are useful not for their content but for how they present information — formatting patterns, page structure, and documentation conventions.

| Reference Page | Site | What to Learn From It |
|---------------|------|----------------------|
| [Glossary](https://orcd-docs.mit.edu/glossary/) | MIT ORCD | ~40 terms, 1–3 sentence definitions — model for AICR glossary |
| [Glossary](https://docs.ycrc.yale.edu/glossary/) | Yale YCRC | Alternative glossary approach |
| [Common Terms](https://docs.unity.rc.umass.edu/documentation/get-started/common-terms/) | UMass Unity | Beginner-oriented terminology page |
| [Contributing to These Docs](https://docs.unity.rc.umass.edu/documentation/contributing/) | UMass Unity | How Unity structures their docs process — useful for internal style guidance |
| [About](https://docs.unity.rc.umass.edu/about/) | UMass Unity | How to write an "About" page for a multi-institution cluster |
| [Contact Us](https://docs.unity.rc.umass.edu/contact/) | UMass Unity | Support page layout (Slack, office hours, tickets, requests) |
| [Documentation and Readability](https://handbook.eng.kempnerinstitute.harvard.edu/s2_swe_for_research/documentation_and_readibility.html) | Kempner | Best practices for documentation and readable code — Jupyter Book format as an alternative style model |
| [Reproducible Research](https://handbook.eng.kempnerinstitute.harvard.edu/s2_swe_for_research/reproducible_research.html) | Kempner | Environment management, data versioning, randomness control — good reference for recipes that emphasize reproducibility |
| [MGHPCC](https://www.bu.edu/tech/support/research/rcs/mghpcc/) | BU RC | BU's description of the MGHPCC partnership — useful for AICR's About page |
