# Yale YCRC Documentation Site - Page Index

Source: https://docs.ycrc.yale.edu/ (sitemap + navigation crawl, 2026-04-03)

## About / Overview Pages

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://docs.ycrc.yale.edu/ | Yale Center for Research Computing - Introduction | Homepage and entry point for all YCRC documentation, with navigation to all major sections. | Style reference, Getting Started |
| https://docs.ycrc.yale.edu/glossary/ | Glossary | Definitions of technical terms used across YCRC HPC documentation, covering infrastructure, scheduling, storage, and administration concepts. | Style reference, Getting Started |
| https://docs.ycrc.yale.edu/news/ | News | Chronological news and announcements about YCRC clusters, maintenance, and changes. | Reference only |
| https://docs.ycrc.yale.edu/user-group/ | YCRC User Group | Information about the YCRC user group community. | Reference only |

## Cluster Descriptions

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://docs.ycrc.yale.edu/clusters/ | HPC Clusters Overview | Overview of Yale's HPC infrastructure, listing active clusters (Bouchet, Grace, McCleary) and specialized systems with their storage. | Getting Started, Cluster Info |
| https://docs.ycrc.yale.edu/clusters/bouchet/ | Bouchet | Describes the Bouchet cluster (replacing Grace/McCleary), with access methods, software modules, partition specs, resource limits, and storage. | Cluster Info, Running Jobs |
| https://docs.ycrc.yale.edu/clusters/bouchet_amd/ | Bouchet AMD Nodes | Documents new AMD-based compute nodes on Bouchet (26 CPU nodes, 8 RTX Pro 6000 GPU nodes, 3 B200 GPU nodes) with cross-architecture compilation guidance. | Cluster Info, Software |
| https://docs.ycrc.yale.edu/clusters/bouchet_getting_started/ | Bouchet Getting Started | Explains key differences between Bouchet and other clusters regarding group structure, partitions, storage, and software. | Getting Started, Cluster Info |
| https://docs.ycrc.yale.edu/clusters/grace/ | Grace | Describes Grace, a shared-use cluster for FAS researchers, with access info, software modules, partition allocations, and storage. | Cluster Info, Running Jobs |
| https://docs.ycrc.yale.edu/clusters/mccleary/ | McCleary | Details the McCleary cluster for School of Medicine/life science researchers, including partitions, modules, and job submission. | Cluster Info, Running Jobs |
| https://docs.ycrc.yale.edu/clusters/milgram/ | Milgram | Describes Milgram, the cluster for projects involving sensitive data, with access requirements, hardware specs, and partitions. | Cluster Info, Security |
| https://docs.ycrc.yale.edu/clusters/hopper/ | Hopper | Documents Hopper, Yale's secure HPC cluster for ePHI and controlled research data, covering access, data transfer, hardware, and pricing. | Cluster Info, Security |
| https://docs.ycrc.yale.edu/clusters/misha/ | Misha | Describes Misha, the cluster for Wu Tsai Institute projects, with access, hardware, modules, partitions, and storage. | Cluster Info |
| https://docs.ycrc.yale.edu/clusters/aicr/ | AICR | Describes the AICR multi-institution AI computing cluster at MGHPCC with 248 B200 GPUs and 152 RTX6000 Pro Blackwell GPUs, coming Spring 2026. | Cluster Info, AI/ML |
| https://docs.ycrc.yale.edu/clusters/grace-mccleary-decommission/ | Grace & McCleary Decommission | Outlines the phased migration plan from Grace/McCleary to the Bouchet cluster, with Phase 1 in first half of 2026. | Cluster Info, Migration |
| https://docs.ycrc.yale.edu/clusters/maintenance/ | Cluster Maintenance | Documents the twice-yearly, three-day maintenance schedule and how to submit jobs around maintenance windows. | Running Jobs, Policies |

## Access & Getting Started

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://docs.ycrc.yale.edu/clusters-at-yale/ | Getting Started | Orientation for new users covering account creation, login methods, job submission, software access, file transfer, and support resources. | Getting Started |
| https://docs.ycrc.yale.edu/clusters-at-yale/access/accounts/ | Accounts & Best Practices | Account policies, responsibilities, and procedures including guidelines on sharing, job submission, storage, and external collaborator access. | Getting Started, Policies |
| https://docs.ycrc.yale.edu/clusters-at-yale/access/ | Log on to the Clusters | Explains the two primary access methods: Open OnDemand web portal and SSH, with prerequisites. | Getting Started, Access |
| https://docs.ycrc.yale.edu/clusters-at-yale/access/ood/ | Access the Web Portal | How to use Open OnDemand for shell access, file management, and interactive apps (Jupyter, RStudio) without SSH. | Getting Started, Access |
| https://docs.ycrc.yale.edu/clusters-at-yale/access/ood-remote-desktop/ | Remote Desktop | How to access graphical remote desktop sessions through HPC cluster web portals with graphics quality and clipboard management. | Access |
| https://docs.ycrc.yale.edu/clusters-at-yale/access/ood-jupyter/ | Jupyter | Launching Jupyter Notebook/Lab through the web portal, conda environments, Papermill execution, and troubleshooting. | Software, Access |
| https://docs.ycrc.yale.edu/clusters-at-yale/access/ood-rstudio/ | RStudio | Accessing RStudio through HPC web portals with configuration options, troubleshooting, and remote desktop alternatives. | Software, Access |
| https://docs.ycrc.yale.edu/clusters-at-yale/access/ood-vscode/ | VSCode | Three methods for using VS Code with clusters: Code Server (web), Remote Tunnel (GitHub auth), and Remote SSH. | Software, Access |
| https://docs.ycrc.yale.edu/clusters-at-yale/access/ssh/ | SSH Connection | Instructions for SSH connections including key pair generation on macOS, Linux, and Windows, and public key upload. | Getting Started, Access |
| https://docs.ycrc.yale.edu/clusters-at-yale/access/x11/ | Graphical Interfaces (X11) | Setting up X11 forwarding on macOS/Windows to display graphical apps from HPC clusters locally. | Access |
| https://docs.ycrc.yale.edu/clusters-at-yale/access/advanced-config/ | Advanced SSH Configuration | SSH config files, passphrase storage on macOS, and SSH agent setup for Windows. | Access |
| https://docs.ycrc.yale.edu/clusters-at-yale/access/vpn/ | Access from Off Campus (VPN) | Connecting via Cisco AnyConnect or OpenConnect VPN from off campus, with MFA requirements. | Getting Started, Access |
| https://docs.ycrc.yale.edu/clusters-at-yale/access/mfa/ | Multi-factor Authentication | Setting up Duo MFA for cluster access, with troubleshooting and file transfer client configuration. | Getting Started, Access |
| https://docs.ycrc.yale.edu/clusters-at-yale/access/vnc/ | VNC | Using VNC as an alternative to X11 for graphically intensive apps, with setup for macOS, Linux, and Windows. | Access |
| https://docs.ycrc.yale.edu/clusters-at-yale/access/courses/ | Courses | Using YCRC clusters for coursework: account creation, storage allocation, compute partitions, and end-of-semester data retention. | Policies, Getting Started |
| https://docs.ycrc.yale.edu/clusters-at-yale/help-requests/ | Help Requests | How to submit effective help requests to YCRC staff, including what info to include (cluster name, errors, job IDs). | Getting Started, Support |
| https://docs.ycrc.yale.edu/clusters-at-yale/troubleshoot/ | Troubleshoot Login | Checklist for resolving common login issues including SSH keys, network connectivity, and specific error messages. | Getting Started, Troubleshooting |
| https://docs.ycrc.yale.edu/clusters-at-yale/policies/ | Cluster Usage Policies | Policies for fair use of shared HPC resources with emphasis on GPU utilization monitoring and idle resource prevention. | Policies |

## Job Scheduling (Slurm)

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://docs.ycrc.yale.edu/clusters-at-yale/job-scheduling/ | Run Jobs with Slurm | How to use Slurm to schedule jobs: common commands, resource options, interactive and batch submission. | Running Jobs |
| https://docs.ycrc.yale.edu/clusters-at-yale/job-scheduling/resource-requests/ | Request Compute Resources | Requesting CPUs, memory, and GPUs via Slurm for multi-threaded, multi-process, and MPI applications. | Running Jobs |
| https://docs.ycrc.yale.edu/clusters-at-yale/job-scheduling/resource-usage/ | Monitor CPU and Memory | Measuring CPU/memory usage with /usr/bin/time, ps, top, seff, and sacct for efficient resource allocation. | Running Jobs, Troubleshooting |
| https://docs.ycrc.yale.edu/clusters-at-yale/job-scheduling/common-job-failures/ | Common Job Failures | Typical job errors and solutions: insufficient memory, disk quotas, submission rate limits, module conflicts, conda issues. | Running Jobs, Troubleshooting |
| https://docs.ycrc.yale.edu/clusters-at-yale/job-scheduling/slurm-examples/ | Submission Script Examples | Sample Slurm scripts for single-threaded, multi-threaded, multi-process, hybrid MPI+OpenMP, and GPU jobs. | Running Jobs |
| https://docs.ycrc.yale.edu/clusters-at-yale/job-scheduling/dsq/ | Job Arrays | Submitting large batches of independent jobs using Slurm job arrays and the dSQ (Dead Simple Queue) tool. | Running Jobs |
| https://docs.ycrc.yale.edu/clusters-at-yale/job-scheduling/scavenge/ | Scavenge Partition | Running jobs beyond normal limits using the scavenge partition, with caveat that jobs may be preempted. | Running Jobs |
| https://docs.ycrc.yale.edu/clusters-at-yale/job-scheduling/fairshare/ | Priority & Wait Time | How job priority is determined through fairshare allocation, queue time, concurrent limits, and backfill. | Running Jobs, Policies |
| https://docs.ycrc.yale.edu/clusters-at-yale/job-scheduling/priority-tier/ | Priority Tier | Opt-in fast-lane for jobs using Service Unit pricing at $0.004/SU/hour (since Dec 2024). | Running Jobs, Policies |
| https://docs.ycrc.yale.edu/clusters-at-yale/job-scheduling/dependency/ | Jobs with Dependencies | Using Slurm's --dependency flag to create job pipelines where tasks wait for predecessors to complete. | Running Jobs |
| https://docs.ycrc.yale.edu/clusters-at-yale/job-scheduling/scrontab/ | Recurring Jobs | Using scrontab to schedule recurring jobs with cron syntax, with differences from traditional crontab. | Running Jobs |
| https://docs.ycrc.yale.edu/clusters-at-yale/job-scheduling/mpi/ | MPI Partition | The special MPI partition on Grace/Bouchet for tightly-coupled multi-node MPI applications needing exclusive node access. | Running Jobs |
| https://docs.ycrc.yale.edu/clusters-at-yale/job-scheduling/jobstats/ | Job Performance Monitoring | Using jobstats to report CPU, memory, and GPU utilization for in-progress and completed jobs. | Running Jobs, Troubleshooting |
| https://docs.ycrc.yale.edu/clusters-at-yale/job-scheduling/job_defense/ | Automated Detection of Idle Resources | Automated system on Bouchet that detects idle GPU resources, warns users, and cancels wasteful jobs. | Running Jobs, Policies |
| https://docs.ycrc.yale.edu/clusters-at-yale/job-scheduling/getusage/ | Monitor Overall Slurm Usage | Tracking resource consumption in Service Unit-hours via Open OnDemand or the getusage CLI tool. | Running Jobs |
| https://docs.ycrc.yale.edu/clusters-at-yale/job-scheduling/cmd-line-args/ | Pass Values into Jobs | Passing variables via environment variables and CLI arguments in Python/R, plus Slurm environment variables. | Running Jobs |
| https://docs.ycrc.yale.edu/clusters-at-yale/job-scheduling/slurm-account/ | Slurm Account Coordinator | Commands for managing Slurm accounts/jobs: adding/removing users, account info, job control. | Running Jobs, Administration |
| https://docs.ycrc.yale.edu/clusters-at-yale/job-scheduling/simplequeue/ | SimpleQueue (Deprecated) | Deprecated tool for batch job submission, replaced by dSQ for job array management. | Running Jobs |
| https://docs.ycrc.yale.edu/clusters-at-yale/glossary/ | Glossary (User Guide) | Glossary of terms specific to the User Guide section. | Style reference |

## Data & Storage

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://docs.ycrc.yale.edu/data/ | Data Storage | Overview of storage options: HPC cluster storage, Google Drive, Storage@Yale, Teams/SharePoint, Dropbox, Box with capacity and cost info. | Filesystem |
| https://docs.ycrc.yale.edu/data/hpc-storage/ | HPC Storage | Three storage quotas (Home, Project, 60-Day Scratch), monitoring usage, purchasing additional storage, and best practices. | Filesystem |
| https://docs.ycrc.yale.edu/data/transfer/ | Transfer to Cluster | Transferring data via Open OnDemand, Globus, scp, rsync, and dedicated transfer nodes for on/off campus. | Filesystem, Data Transfer |
| https://docs.ycrc.yale.edu/data/globus/ | Large Transfers with Globus | Using Globus to move large data between clusters, personal computers, and cloud (OneDrive, Dropbox, Google Drive, S3). | Data Transfer |
| https://docs.ycrc.yale.edu/data/backups/ | Backups and Snapshots | Retrieving deleted/modified files from Home backups and nightly filesystem snapshots. | Filesystem |
| https://docs.ycrc.yale.edu/data/staging/ | Stage Data for Compute Jobs | Temporarily transferring large datasets to scratch for computation using rsync/cp for interactive and Storage@Yale. | Filesystem, Running Jobs |
| https://docs.ycrc.yale.edu/data/permissions/ | Share with Cluster Users | Sharing data within groups, with individuals, and across groups using Linux permissions and setfacl. | Filesystem |
| https://docs.ycrc.yale.edu/data/archive/ | Archive Your Data | Best practices for archiving: cleaning files, compressing data, using Storage@Yale archive/backup tiers. | Filesystem |
| https://docs.ycrc.yale.edu/data/external/ | Share Data Outside Yale | External sharing via OneDrive, Yale Spinup, and Globus for private data sharing. | Filesystem, Data Transfer |
| https://docs.ycrc.yale.edu/data/google-drive/ | Google Drive | EliApps Google Drive storage: quotas, shared drives, local access, and Rclone/Globus transfer. | Filesystem, Data Transfer |
| https://docs.ycrc.yale.edu/data/ycga-data/ | YCGA Data | Accessing YCGA sequencing data: policies, retention, and retrieving current/archived files on McCleary. | Filesystem, Domain-specific |
| https://docs.ycrc.yale.edu/data/ycga-permissions/ | YCGA Data Permissions | Access restrictions for YCGA sequencing data with tools like ycgaFastq and URLFetch for archived data. | Filesystem, Domain-specific |
| https://docs.ycrc.yale.edu/data/group-change/ | Group Change | Rebuilding Conda environments and R packages after primary group changes, with file migration details. | Filesystem, Software |
| https://docs.ycrc.yale.edu/data/hosting-UCSC-trackhub/ | UCSC Track Hub Hosting | Setting up a custom track hub to share genomic data through the UCSC Genome Browser via Yale cloud. | Domain-specific |
| https://docs.ycrc.yale.edu/data/glossary/ | Glossary (Data) | Data and storage-related terminology definitions. | Style reference |

## Applications & Software Framework

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://docs.ycrc.yale.edu/applications/ | Software Overview | Introduction to cluster software: managed modules, self-install (Conda/Python/R), and compiling custom software. | Software |
| https://docs.ycrc.yale.edu/applications/modules/ | Software Modules | Using the Lmod module system to access, load, and manage pre-compiled software via hierarchical toolchains and collections. | Software |
| https://docs.ycrc.yale.edu/applications/compile/ | Build Software | Compiling and installing software: Autotools, CMake, hardware compatibility, and local installation without admin privileges. | Software |
| https://docs.ycrc.yale.edu/applications/toolchains/ | Software Module Toolchains | EasyBuild toolchains (foss and intel families) used to build software modules with pre-configured compilers/libraries. | Software |
| https://docs.ycrc.yale.edu/applications/lifecycle/ | Software Module Lifecycle | How YCRC manages module deprecation and the rolling two-version toolchain support model. | Software, Policies |

## Software Guides - Languages & Frameworks

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://docs.ycrc.yale.edu/clusters-at-yale/guides/python/ | Python | Setting up and running Python: module loading, Conda packages, interactive jobs, batch processing, Jupyter. | Software |
| https://docs.ycrc.yale.edu/clusters-at-yale/guides/conda/ | Conda | Using Conda for package/environment management: setup, environment creation, installation, and troubleshooting. | Software |
| https://docs.ycrc.yale.edu/clusters-at-yale/guides/pytorch/ | PyTorch | Using PyTorch on clusters: pre-installed modules and custom miniconda installations. | Software, AI/ML |
| https://docs.ycrc.yale.edu/clusters-at-yale/guides/tensorflow/ | TensorFlow | Using TensorFlow: finding modules, installing with proper CUDA/cuDNN config, GPU detection, troubleshooting. | Software, AI/ML |
| https://docs.ycrc.yale.edu/clusters-at-yale/guides/r/ | R | Using R for statistical computing: module loading, packages, interactive/batch jobs, RStudio, parallel computing. | Software |
| https://docs.ycrc.yale.edu/clusters-at-yale/guides/matlab/ | MATLAB | Running MATLAB: GUI via Open OnDemand, CLI, interactive sessions, batch jobs, multi-core usage. | Software |
| https://docs.ycrc.yale.edu/clusters-at-yale/guides/matlab_compile/ | Compile MATLAB Program | Compiling MATLAB code into standalone executables with mcc for performance and portability. | Software |
| https://docs.ycrc.yale.edu/clusters-at-yale/guides/mathematica/ | Mathematica | Accessing Mathematica via Open OnDemand or interactive jobs, including parallel jobs with up to 450 kernels. | Software |
| https://docs.ycrc.yale.edu/clusters-at-yale/guides/mpi4py/ | MPI with Python | Using mpi4py for message-passing parallel computing with concepts like ranks and communicators. | Software, Running Jobs |

## Software Guides - Domain Applications

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://docs.ycrc.yale.edu/clusters-at-yale/guides/gaussian/ | Gaussian | Running Gaussian 16 for electronic structure modeling with GaussView 6 visualization. | Software, Domain-specific |
| https://docs.ycrc.yale.edu/clusters-at-yale/guides/namd/ | NAMD | Running NAMD for molecular dynamics simulation of biomolecular systems with parallelization and GPU acceleration. | Software, Domain-specific |
| https://docs.ycrc.yale.edu/clusters-at-yale/guides/vasp/ | VASP | Configuring VASP computational jobs with Slurm: NCORE, MPI tasks, and partition optimization. | Software, Domain-specific |
| https://docs.ycrc.yale.edu/clusters-at-yale/guides/comsol/ | COMSOL | Using COMSOL Multiphysics 5.2a on Grace: GUI, batch mode, physics modules, and license limitations. | Software, Domain-specific |
| https://docs.ycrc.yale.edu/clusters-at-yale/guides/cesm/ | CESM/CAM | Running the Community Earth System Model on Grace: module loading, case creation, building, and troubleshooting. | Software, Domain-specific |
| https://docs.ycrc.yale.edu/clusters-at-yale/guides/isca/ | Isca | Installing Isca (idealized global circulation modelling framework) with conda and Fortran compilers. | Software, Domain-specific |
| https://docs.ycrc.yale.edu/clusters-at-yale/guides/atlas/ | ATLAS Computing Environment | Setting up ATLAS experiment software via CVMFS with .bashrc configuration. | Software, Domain-specific |
| https://docs.ycrc.yale.edu/clusters-at-yale/guides/nextflow/ | Nextflow | Installing/configuring Nextflow with SLURM executor, job management, and Sarek bioinformatics pipeline example. | Software, Running Jobs |
| https://docs.ycrc.yale.edu/clusters-at-yale/guides/alphafold/ | AlphaFold | Running AlphaFold 2 and 3 for protein structure prediction with batch scripts and cluster configs. | Software, Domain-specific |
| https://docs.ycrc.yale.edu/clusters-at-yale/guides/cryoem/ | Cryo-EM on McCleary | Cryo-EM computational workflows on McCleary: storage, GPU scheduling, RELION, EMAN2, and CryoSPARC. | Software, Domain-specific |
| https://docs.ycrc.yale.edu/clusters-at-yale/guides/cryosparc/ | CryoSPARC | Installing and running CryoSPARC on clusters: port setup, installation, job submission, and troubleshooting. | Software, Domain-specific |

## Software Guides - Tools & Utilities

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://docs.ycrc.yale.edu/clusters-at-yale/guides/containers/ | Containers | Using Apptainer (Singularity) containers: pre-existing images, custom builds with definition files, Dockerfile conversion. | Software |
| https://docs.ycrc.yale.edu/clusters-at-yale/guides/gpus-cuda/ | GPUs and CUDA | Requesting GPUs, nvidia-smi monitoring, CUDA/cuDNN/TF/PyTorch modules, and compiling CUDA code. | Software, Running Jobs |
| https://docs.ycrc.yale.edu/clusters-at-yale/guides/parallel/ | GNU Parallel | Using GNU Parallel for independent tasks: loops, file processing, and parameter sweeps. | Running Jobs, Software |
| https://docs.ycrc.yale.edu/clusters-at-yale/guides/tmux/ | tmux | Using tmux to maintain interactive sessions after disconnecting, with proper login node usage. | Software, Access |
| https://docs.ycrc.yale.edu/clusters-at-yale/guides/mysql/ | MySQL | Running MySQL database server via Apptainer containers for temporary, application-specific needs. | Software |
| https://docs.ycrc.yale.edu/clusters-at-yale/guides/spark/ | Spark | Setting up Apache Spark for distributed processing: interactive and batch configs with resource examples. | Software, Running Jobs |
| https://docs.ycrc.yale.edu/clusters-at-yale/guides/rclone/ | Rclone | Configuring Rclone to sync files between clusters and cloud storage (Google Drive, OneDrive, Box, S3). | Data Transfer, Software |
| https://docs.ycrc.yale.edu/clusters-at-yale/guides/github/ | Git and GitHub | Using Git for version control and GitHub for collaboration with SSH authentication. | Software |
| https://docs.ycrc.yale.edu/clusters-at-yale/guides/github_pages/ | GitHub Pages | Creating and hosting static websites using GitHub Pages with setup and deployment instructions. | Software |
| https://docs.ycrc.yale.edu/clusters-at-yale/guides/checkpointing/ | Checkpoint Long-running Jobs | Using DMTCP to save/restart long-running jobs, allowing recovery from timeouts and preemptions. | Running Jobs |
| https://docs.ycrc.yale.edu/clusters-at-yale/guides/easybuild/ | EasyBuild | Using EasyBuild to build/install software: configuration, package search, installation, and local modules. | Software |
| https://docs.ycrc.yale.edu/clusters-at-yale/guides/clustershell/ | ClusterShell | Using ClusterShell (nodeset, clush) to run commands on job nodes and collect results. | Running Jobs, Software |
| https://docs.ycrc.yale.edu/clusters-at-yale/guides/virtualgl/ | VirtualGL | Remote 3D rendering with hardware acceleration using EGL and GLX back ends. | Software, Access |
| https://docs.ycrc.yale.edu/clusters-at-yale/guides/xvfb/ | Virtual Frame Buffer (XVFB) | Using xvfb for virtual displays to run graphical programs (e.g., R plots) in batch mode. | Software, Running Jobs |
| https://docs.ycrc.yale.edu/clusters-at-yale/guides/jupyter_ssh/ | Jupyter over SSH Port Forwarding | Manually setting up Jupyter via batch job + SSH tunnel as alternative to Open OnDemand. | Software, Access |

## AI & Machine Learning

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://docs.ycrc.yale.edu/ai/ | AI & ML Overview | Navigation hub for LLM and AI tool workflows: open-source inference, GPU monitoring, multi-GPU, closed-source models. | AI/ML |
| https://docs.ycrc.yale.edu/ai/gpu-jobstats/ | GPU Monitoring with Jobstats | Using Jobstats to monitor GPU/CPU utilization and identify performance bottlenecks in AI/ML workflows. | AI/ML, Running Jobs |
| https://docs.ycrc.yale.edu/ai/resources/ | LLMs and GPU Availability | GPU resources across clusters for LLMs: hardware specs, scheduling, and memory requirements by model size. | AI/ML, Cluster Info |
| https://docs.ycrc.yale.edu/ai/ollama/ | Ollama | Using Ollama for local LLM inference: interactive/batch usage, GPU config, and YCRC module wrapper for isolation. | AI/ML, Software |
| https://docs.ycrc.yale.edu/ai/exercises/ | Ollama Exercises | GitHub exercises for Ollama inference in terminals/Jupyter and modifying LLM parameters. | AI/ML, Training |
| https://docs.ycrc.yale.edu/ai/huggingface/ | Hugging Face | Running LLMs via Hugging Face on clusters: environment setup, GPU selection, model loading, multi-GPU workflows. | AI/ML, Software |
| https://docs.ycrc.yale.edu/ai/miniconda-multigpu/ | Multi-GPU Submission Scripts | Multi-GPU AI/ML workloads with Conda: single-node and multi-node approaches using PyTorch torchrun. | AI/ML, Running Jobs |
| https://docs.ycrc.yale.edu/ai/nairr/ | NAIRR | Accessing National AI Research Resource compute through proposals, with help for proposal development. | AI/ML, External Resources |
| https://docs.ycrc.yale.edu/ai/pythonpackages/ | AI/ML Python Package Installation | Installation recipes and troubleshooting for Flash Attention, vllm, esmfold, and other AI/ML packages. | AI/ML, Software |
| https://docs.ycrc.yale.edu/ai/aicodingtools/ | AI Coding Tools | Security risks of AI coding agents on clusters (data exposure, credential leaks, code execution) and mitigation best practices. | AI/ML, Security |
| https://docs.ycrc.yale.edu/ai/clarity/ | Closed-Source Models & Clarity | Yale's Clarity platform for closed-source AI models, data privacy risks of API keys, and recommendations for research. | AI/ML, Security |

## Training & Resources

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://docs.ycrc.yale.edu/resources/ | Training & Other Resources | Overview of YCRC educational offerings and training sessions on research computing topics. | Training |
| https://docs.ycrc.yale.edu/resources/intro_to_hpc_tutorial/ | Introduction to HPC Tutorials | Three foundational exercises: interactive jobs with Conda, batch jobs with Slurm, and Jupyter via Open OnDemand. | Getting Started, Training |
| https://docs.ycrc.yale.edu/resources/online-tutorials/ | Online Tutorials | Collection of external tutorials on Linux/Unix CLI, Python, R, MATLAB, and Singularity/Apptainer. | Training |
| https://docs.ycrc.yale.edu/resources/national-hpcs/ | National HPCs | Accessing national HPC resources: ACCESS, DOE programs (INCITE, ALCC), NCSA Blue Waters, Open Science Grid. | External Resources |
| https://docs.ycrc.yale.edu/resources/yale_library/ | Yale Library | Yale Library resources for cluster users, particularly the O'Reilly Safari eBooks collection. | Training |
| https://docs.ycrc.yale.edu/resources/sw_carpentry/ | Software Carpentry | Links to Software Carpentry lessons in Unix, Git, Python, and R plus Carpentries Lab materials. | Training |
| https://docs.ycrc.yale.edu/resources/glossary/ | Glossary (Resources) | Resource-related terminology definitions. | Style reference |

---

**Total substantive pages indexed: 100** (excluding ~45 monthly news/announcement pages)

### Summary by AICR "Useful For" Category

| Category | Count | Key Pages |
|----------|-------|-----------|
| Getting Started | 12 | clusters-at-yale/, access/, accounts/, ssh/, vpn/, intro_to_hpc_tutorial/ |
| Running Jobs | 25 | job-scheduling/ and all sub-pages, slurm-examples/, resource-requests/, checkpointing/ |
| Software | 35 | applications/, modules/, all guides/ pages, containers/, conda/, python/ |
| Filesystem | 12 | data/, hpc-storage/, transfer/, globus/, backups/, permissions/, staging/ |
| Cluster Info | 12 | clusters/, bouchet/, grace/, mccleary/, milgram/, hopper/, aicr/ |
| AI/ML | 14 | ai/ and all sub-pages, pytorch/, tensorflow/, gpus-cuda/ |
| Policies | 7 | policies/, accounts/, fairshare/, priority-tier/, lifecycle/, job_defense/ |
| Style reference | 5 | glossary/ pages, homepage |
| Training | 6 | resources/ and all sub-pages |
| Access | 11 | All access/ sub-pages |
| Data Transfer | 5 | transfer/, globus/, rclone/, google-drive/, external/ |
| Troubleshooting | 4 | troubleshoot/, common-job-failures/, resource-usage/, jobstats/ |
