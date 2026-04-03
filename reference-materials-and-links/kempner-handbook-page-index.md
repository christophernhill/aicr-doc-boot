# Kempner Institute Engineering Handbook -- Page Index

Source: https://handbook.eng.kempnerinstitute.harvard.edu/
Crawled: 2026-04-03

## Introduction

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://handbook.eng.kempnerinstitute.harvard.edu/intro.html | Kempner Computing Handbook | Comprehensive resource for researchers using Harvard's Kempner AI cluster, covering HPC basics, job scheduling, GPU computing, development environments, and performance optimization; the cluster ranks 32nd on Green500 and 85th on TOP500 (November 2024). | Getting Started |

## Kempner AI Cluster

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://handbook.eng.kempnerinstitute.harvard.edu/s1_high_performance_computing/kempner_cluster/README.html | Kempner AI Cluster | Introductory section guiding new users through the fundamentals of high-performance computing at the Kempner Institute, covering getting started, navigating the cluster, and understanding its architecture. | Getting Started |
| https://handbook.eng.kempnerinstitute.harvard.edu/s1_high_performance_computing/kempner_cluster/introduction_and_cluster_basics.html | Introduction and Basics | Introduces HPC concepts and provides instructions for requesting access to the Kempner AI cluster, including guidance for different user categories such as Kempner-affiliated researchers, graduate fellows, undergraduate students, and PIs. | Access |
| https://handbook.eng.kempnerinstitute.harvard.edu/s1_high_performance_computing/kempner_cluster/overview_of_kempner_cluster.html | Overview of Cluster | Describes the Kempner Institute AI Cluster, a GPU-based HPC resource comprising 144 A100 and 384 H100 GPUs housed at the Massachusetts Green High-Performance Computing Center, detailing eligibility, specifications, access policies, and reservation procedures. | Cluster Info |
| https://handbook.eng.kempnerinstitute.harvard.edu/s1_high_performance_computing/kempner_cluster/kempner_policies_for_responsible_use.html | Cluster Usage Policies | Outlines responsible usage guidelines for the Kempner AI cluster, specifying that access is restricted to Kempner-related research and establishing resource limits to prevent monopolization. | Policy |
| https://handbook.eng.kempnerinstitute.harvard.edu/s1_high_performance_computing/kempner_cluster/accessing_and_navigating_the_cluster.html | Accessing the Cluster | Explains how to connect to the Kempner AI cluster through SSH access and Open OnDemand, including setup requirements for OpenAuth 2FA and VPN configuration. | Access |
| https://handbook.eng.kempnerinstitute.harvard.edu/s1_high_performance_computing/kempner_cluster/accessing_gpu_by_fasrc_users.html | Access by FASRC Users | Explains how FASRC Cannon cluster users can access underutilized Kempner AI cluster GPU resources through the gpu_requeue partition, with preemption policies and command examples for interactive and batch job submissions on H100 and A100 GPUs. | Access |

## Efficient Use of Resources

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://handbook.eng.kempnerinstitute.harvard.edu/s1_high_performance_computing/efficient_use_of_resources/fair_use_and_prioritization_policies.html | Fairshare Policy | Describes the fairshare system that allocates resources fairly across user groups over time, where job priority is determined by fairshare scores and job age to ensure balanced resource distribution. | Policy |

## Job Submission and SLURM

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://handbook.eng.kempnerinstitute.harvard.edu/s1_high_performance_computing/general_hpc_concepts/README.html | Job Submission | Introduces high-performance computing concepts including resource allocation, job scheduling systems, and methods for enhancing computational efficiency on the Kempner AI cluster. | Running Jobs |
| https://handbook.eng.kempnerinstitute.harvard.edu/s1_high_performance_computing/general_hpc_concepts/understanding_slurm.html | Understanding SLURM | Introduces SLURM as a job scheduler and resource manager in HPC environments, covering partitions, accounts, and environment variables used on the Kempner cluster. | Running Jobs |
| https://handbook.eng.kempnerinstitute.harvard.edu/s1_high_performance_computing/general_hpc_concepts/job_submission_basics.html | Job Submission Basics | Explains how to submit jobs using either interactive allocation via salloc or batch job submission via sbatch, including SLURM directive specifications and example configurations. | Running Jobs |
| https://handbook.eng.kempnerinstitute.harvard.edu/s1_high_performance_computing/general_hpc_concepts/array_jobs.html | Array Jobs | Explains how to use SLURM array jobs to execute multiple instances of the same task in parallel, with practical applications like parameter sweeps, cross-validation, and hyperparameter tuning. | Running Jobs |
| https://handbook.eng.kempnerinstitute.harvard.edu/s1_high_performance_computing/general_hpc_concepts/job_dependencies.html | Job Dependencies | Explains how to use SLURM's --dependency option to schedule jobs in a specific sequence, ensuring tasks like data preprocessing, model training, and evaluation run in the correct order. | Running Jobs |
| https://handbook.eng.kempnerinstitute.harvard.edu/s1_high_performance_computing/general_hpc_concepts/advanced_slurm_features.html | Advanced SLURM Features | Covers five advanced SLURM techniques including exclusive node access, dependency chains with job arrays, resource constraints, email notifications, and optimizing compute resource requests to manage GPU fragmentation. | Running Jobs |
| https://handbook.eng.kempnerinstitute.harvard.edu/s1_high_performance_computing/general_hpc_concepts/open_ondemand.html | Open OnDemand | Explains how to use Open OnDemand, a web-based platform for accessing HPC resources, including submitting interactive Jupyter Notebook jobs and configuring custom Conda environments. | Running Jobs |

## Development Environment

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://handbook.eng.kempnerinstitute.harvard.edu/s1_high_performance_computing/development_and_runtime_envs/README.html | Development Environment | Provides guidance on setting up development environments, managing software modules, and implementing containerization to ensure consistent runtime configurations across the cluster. | Software |
| https://handbook.eng.kempnerinstitute.harvard.edu/s1_high_performance_computing/development_and_runtime_envs/software_module_and_environment_management.html | Software Modules | Explains how to use the module system on HPC clusters to manage software packages and their dependencies, covering commands for listing, loading, and unloading modules. | Software |
| https://handbook.eng.kempnerinstitute.harvard.edu/s1_high_performance_computing/development_and_runtime_envs/containerization.html | Containerization | Explains how Docker and Singularity enable consistent software environments, with practical guidance on converting PyTorch Docker images to Singularity format for use on HPC clusters. | Software |
| https://handbook.eng.kempnerinstitute.harvard.edu/s1_high_performance_computing/development_and_runtime_envs/using_vscode_for_remote_development.html | VSCode for Remote Dev | Explains how to set up Visual Studio Code with the Remote-SSH extension for development on the FASRC cluster, including configurations for both login and compute nodes and Jupyter notebook integration. | Software |
| https://handbook.eng.kempnerinstitute.harvard.edu/s1_high_performance_computing/development_and_runtime_envs/using_conda_env.html | Conda Environment | Explains how to create and manage conda environments on the Kempner AI Cluster, covering setup in default and custom directories, Jupyter integration, environment export for reproducibility, and troubleshooting. | Software |
| https://handbook.eng.kempnerinstitute.harvard.edu/s1_high_performance_computing/development_and_runtime_envs/handling_dependencies_with_spack.html | Spack Package Manager | Introduces Spack, a package management tool for HPC clusters, covering installation on shared lab directories, essential commands, and advanced environment configuration. | Software |
| https://handbook.eng.kempnerinstitute.harvard.edu/s1_high_performance_computing/development_and_runtime_envs/customizing_bashrc.html | Shell Configuration | Presents practical aliases and shortcuts for the ~/.bashrc file to streamline workflows on the Kempner AI Cluster, including navigation to storage directories, job monitoring, and interactive session management. | Software |

## Storage and Data Transfer

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://handbook.eng.kempnerinstitute.harvard.edu/s1_high_performance_computing/storage_and_data_transfer/README.html | Storage and Data Transfer | Introduces data management fundamentals, covering storage options (tiers) and techniques for transferring data to and from the cluster. | Filesystem |
| https://handbook.eng.kempnerinstitute.harvard.edu/s1_high_performance_computing/storage_and_data_transfer/understanding_storage_options.html | Storage Options | Describes three main storage solutions: a 100GB persistent home directory, a 4TB persistent lab directory, and 50TB of temporary high-performance scratch storage per lab with a 90-day retention policy. | Filesystem |
| https://handbook.eng.kempnerinstitute.harvard.edu/s1_high_performance_computing/storage_and_data_transfer/data_transfer.html | Data Transfer | Outlines four methods for transferring data: scp for small files, rsync for efficient synchronization with resume capability, fpsync for parallel directory synchronization, and Globus for large-scale transfers. | Data Transfer |
| https://handbook.eng.kempnerinstitute.harvard.edu/s1_high_performance_computing/storage_and_data_transfer/shared_data_repository.html | Shared Data/Model Repository | Documents the centralized, read-only repository of popular ML models and datasets accessible to all users, including CodeLlama, EleutherAI models, GPT-2, T5, and datasets like C4, Dolma, and ImageNet. | AI/ML |

## Software Engineering for Research

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://handbook.eng.kempnerinstitute.harvard.edu/s2_swe_for_research/collaborative_code_development.html | Collaborative Code Development | Covers essential practices for team-based research software development, including version control fundamentals, GitHub workflows, branching strategies, code review processes, and best practices for commits and repository organization. | Style reference |
| https://handbook.eng.kempnerinstitute.harvard.edu/s2_swe_for_research/software_design_principles.html | Software Design Principles | Outlines essential design principles for building maintainable, testable, and reproducible research software, covering modularity, abstraction, testing, reusability, design patterns, and architecture strategies. | Style reference |
| https://handbook.eng.kempnerinstitute.harvard.edu/s2_swe_for_research/documentation_and_readibility.html | Documentation and Readability | Covers best practices for creating clear documentation and readable code in research software, emphasizing how proper documentation ensures reproducibility and collaboration. | Style reference |
| https://handbook.eng.kempnerinstitute.harvard.edu/s2_swe_for_research/testing_and_continuous_integration.html | Testing and Continuous Integration | Covers strategies for implementing reliable testing and automated CI workflows in research software, including test types, frameworks, coverage analysis, and best practices. | Style reference |
| https://handbook.eng.kempnerinstitute.harvard.edu/s2_swe_for_research/package_development.html | Package Development | Explains how to structure, build, test, and distribute research software as a reusable package, emphasizing modularity, shareability, and reproducibility. | Style reference |
| https://handbook.eng.kempnerinstitute.harvard.edu/s2_swe_for_research/reproducible_research.html | Reproducible Research | Outlines essential practices for ensuring research reproducibility, covering version control, environment management, data versioning, randomness control, documentation, testing, and artifact archiving. | Style reference |

## AI Tools and Workflows

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://handbook.eng.kempnerinstitute.harvard.edu/s3_ai_workflows/testbed_and_tatm.html | Data Discovery and Tokenization | Documents the tatm Python library and testbed resources for discovering, exploring, and accessing datasets for AI/ML research, including integration with OLMo for model training. | AI/ML |
| https://handbook.eng.kempnerinstitute.harvard.edu/s3_ai_workflows/distributed_inference.html | Distributed Inference | Explains how to deploy large language models across multiple GPUs using vLLM, featuring pipeline parallelism and tensor parallelism techniques with deployment guides for Llama 3.1 and DeepSeek-R1. | AI/ML |
| https://handbook.eng.kempnerinstitute.harvard.edu/s3_ai_workflows/nemo_workflow.html | NVIDIA NeMo Workflow | Describes a modular, cluster-ready workflow built on the NVIDIA NeMo framework that enables pretraining and finetuning of large language models with support for distributed training via SLURM. | AI/ML |
| https://handbook.eng.kempnerinstitute.harvard.edu/s3_ai_workflows/scalable_vision_workflows.html | Scalable Vision Workflows | Presents PyTorch-based distributed training workflows optimized for vision models like ResNet-50 and AlexNet on the cluster, emphasizing SLURM integration and distributed training best practices. | AI/ML |
| https://handbook.eng.kempnerinstitute.harvard.edu/s3_ai_workflows/get_hf_model.html | Hugging Face Models | Provides best practices for downloading and working with Hugging Face models on the Kempner AI Cluster, including a SLURM submission script with configurable parameters for model storage and retrieval. | AI/ML |

## Neuro AI Workflows

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://handbook.eng.kempnerinstitute.harvard.edu/s4_neuro_ai_workflows/spike_sorting.html | Spike Sorting | Describes spike sorting as a neuroscience technique for identifying and classifying action potentials from extracellular recordings, with pipelines developed collaboratively with the Allen Institute. | AI/ML |

## Scalability

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://handbook.eng.kempnerinstitute.harvard.edu/s5_ai_scaling_and_engineering/scalability/README.html | Scalability | Addresses computational scaling approaches, covering parallel computing fundamentals through GPU-based computational optimization strategies. | GPU |
| https://handbook.eng.kempnerinstitute.harvard.edu/s5_ai_scaling_and_engineering/scalability/introduction_to_parallel_computing.html | Intro to Parallel Computing | Explains how parallel computing enhances computational speed by distributing tasks across multiple processors, covering MPI for distributed systems, OpenMP for shared-memory multi-threading, and CUDA for GPU processing. | GPU |
| https://handbook.eng.kempnerinstitute.harvard.edu/s5_ai_scaling_and_engineering/scalability/gpu_computing.html | GPU Computing | Explains how GPUs differ from CPUs and demonstrates practical methods for leveraging GPU acceleration through CuPy and PyTorch, with performance comparisons showing significant speedups for parallel workloads. | GPU |
| https://handbook.eng.kempnerinstitute.harvard.edu/s5_ai_scaling_and_engineering/scalability/gpu_profiling.html | GPU Profiling | Teaches how to identify and fix GPU performance bottlenecks using PyTorch Profiler, Holistic Trace Analysis (HTA), and NVIDIA Nsight tools through an iterative profiling, analysis, and optimization workflow. | GPU |
| https://handbook.eng.kempnerinstitute.harvard.edu/s5_ai_scaling_and_engineering/scalability/distributed_gpu_computing.html | Distributed GPU Computing | Covers methods for parallelizing ML workloads across multiple GPUs, including inter-GPU communication via NCCL and six distributed training strategies from data parallelism to fully sharded approaches with PyTorch examples. | GPU |
| https://handbook.eng.kempnerinstitute.harvard.edu/s5_ai_scaling_and_engineering/scalability/parallel_io.html | Parallel I/O | Provides guidance on handling input/output operations effectively in parallel computing environments, with best practices for managing I/O in parallel applications. | GPU |

## Efficiency

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://handbook.eng.kempnerinstitute.harvard.edu/s5_ai_scaling_and_engineering/efficiency/README.html | Efficiency | Introduces strategies for optimizing machine learning workflows, covering ML efficiency, performance monitoring, deployment and inference, and experiment management. | AI/ML |
| https://handbook.eng.kempnerinstitute.harvard.edu/s5_ai_scaling_and_engineering/efficiency/ml_scaling_and_efficiency.html | ML Efficiency | Covers optimization techniques for machine learning workflows on high-performance computing systems. | AI/ML |
| https://handbook.eng.kempnerinstitute.harvard.edu/s5_ai_scaling_and_engineering/efficiency/performance_monitoring_and_optimization.html | Performance Monitoring | Covers performance monitoring and optimization techniques as part of the AI scaling and engineering efficiency module. | AI/ML |
| https://handbook.eng.kempnerinstitute.harvard.edu/s5_ai_scaling_and_engineering/efficiency/efficient_deployment_and_inference.html | Deployment and Inference | Covers strategies and best practices for efficient deployment and inference of machine learning models on HPC systems. | AI/ML |
| https://handbook.eng.kempnerinstitute.harvard.edu/s5_ai_scaling_and_engineering/efficiency/experiment_management_and_reproducibility.html | Experiment Management | Covers experiment management and reproducibility techniques within the AI scaling and engineering efficiency module. | AI/ML |

## Experiment Management

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://handbook.eng.kempnerinstitute.harvard.edu/s5_ai_scaling_and_engineering/experiment_management/README.html | Experiment Management | Introductory hub for experiment management techniques, with links to guides on Weights and Biases for tracking and optimizing machine learning experiments. | AI/ML |
| https://handbook.eng.kempnerinstitute.harvard.edu/s5_ai_scaling_and_engineering/experiment_management/logging_and_monitoring.html | Weights and Biases - Intro | Introduces Weights and Biases for experiment tracking and visualization, walking users through setup, authentication, and basic tracking of metrics during model training. | AI/ML |
| https://handbook.eng.kempnerinstitute.harvard.edu/s5_ai_scaling_and_engineering/experiment_management/wandb_sweeps.html | Weights and Biases - Sweeps | Explains how to systematically explore hyperparameter combinations using W&B sweeps, including configuration setup, agent execution on SLURM clusters, visualization techniques, and real-time loss averaging. | AI/ML |

## Security and Compliance

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://handbook.eng.kempnerinstitute.harvard.edu/s6_security_and_compliance/README.html | Security and Compliance | Placeholder section for security and compliance guidelines for the Kempner AI cluster. | Policy |

## Open Source Hub

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://handbook.eng.kempnerinstitute.harvard.edu/s7_open_source_hub/README.html | Open Source Hub | Catalogs open-source projects from the Kempner Institute across AI, NeuroAI, and research software engineering, including tools like TMRC, TATM, minOLMo, and distributed inference workflows. | AI/ML |

## Support

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://handbook.eng.kempnerinstitute.harvard.edu/s8_support/README.html | Support and Troubleshooting | Directs users to various support resources including FASRC training programs, office hours, help desk assistance, and the Kempner Slack channel for resolving cluster-related issues. | Troubleshooting |
| https://handbook.eng.kempnerinstitute.harvard.edu/s8_support/faq.html | FAQ | Addresses common issues when working with GitHub on the HPC cluster, including resolving SSH key authentication errors and fixing HTTPS/SSH configuration problems during git operations. | Troubleshooting |

## Workshops and Trainings

| URL | Page Title | Content Summary | Useful For |
|-----|-----------|-----------------|------------|
| https://handbook.eng.kempnerinstitute.harvard.edu/s9_workshops_and_trainings/README.html | About Workshops @ Kempner | Introduces interactive workshop sessions designed to help participants develop practical skills across topics from cluster access to distributed ML and neural data processing. | Training |
| https://handbook.eng.kempnerinstitute.harvard.edu/s9_workshops_and_trainings/intro_to_kempner_ai_cluster/intro_to_kempner_ai_cluster.html | Intro to Kempner AI Cluster Workshop | Introductory workshop providing guidance on how to access and use the Kempner AI cluster, including cluster login, code development, data management, and job submission and monitoring. | Training |
| https://handbook.eng.kempnerinstitute.harvard.edu/s9_workshops_and_trainings/intro_to_distributed_computing/intro_to_distributed_computing.html | Intro to Distributed Computing Workshop | Workshop teaching distributed systems approaches, covering embarrassingly parallel processes and Distributed Data Parallel training across multiple GPUs using PyTorch. | Training |
| https://handbook.eng.kempnerinstitute.harvard.edu/s9_workshops_and_trainings/llm_distributed_training/llm_distributed_training.html | LLM Distributed Training Workshop | Workshop on parallelization techniques for training large language models, including DDP, Model Parallelism, Tensor Parallelism, Pipeline Parallelism, and FSDP with hands-on examples. | Training |
| https://handbook.eng.kempnerinstitute.harvard.edu/s9_workshops_and_trainings/transformer_from_scratch/transformer_from_scratch.html | Building a Transformer from Scratch Workshop | Workshop teaching participants to construct a basic language model by exploring transformer architecture components, training procedures, and end-to-end model development. | Training |
| https://handbook.eng.kempnerinstitute.harvard.edu/s9_workshops_and_trainings/llm_distributed_inference/llm_distributed_inference.html | LLM Distributed Inference Workshop | Workshop teaching how to deploy and run inference for large language models exceeding single GPU memory using vLLM, covering model prompting, logit extraction, and prompt parallelization. | Training |
| https://handbook.eng.kempnerinstitute.harvard.edu/s9_workshops_and_trainings/spike_sorting_on_hpc_cluster/spike_sorting_on_hpc_cluster.html | Spike Sorting on HPC Cluster Workshop | Workshop teaching spike sorting algorithms for neural data on HPC clusters, using GPU acceleration with tools like Kilosort4 for processing Neuropixels data. | Training |
| https://handbook.eng.kempnerinstitute.harvard.edu/s9_workshops_and_trainings/optimizing_ml_workflows/optimizing_ml_workflows.html | Optimizing ML Workflows Workshop | Workshop teaching how to streamline ML training pipelines on AI clusters, covering environment setup through deployment with emphasis on W&B experiment tracking and model checkpointing. | Training |

---

## Summary Statistics

| Section | Page Count |
|---------|-----------|
| Introduction | 1 |
| Kempner AI Cluster | 6 |
| Efficient Use of Resources | 1 |
| Job Submission and SLURM | 7 |
| Development Environment | 7 |
| Storage and Data Transfer | 4 |
| Software Engineering for Research | 6 |
| AI Tools and Workflows | 5 |
| Neuro AI Workflows | 1 |
| Scalability | 6 |
| Efficiency | 5 |
| Experiment Management | 3 |
| Security and Compliance | 1 |
| Open Source Hub | 1 |
| Support | 2 |
| Workshops and Trainings | 8 |
| **Total** | **64** |

### Pages by "Useful For" Tag

| Tag | Count |
|-----|-------|
| AI/ML | 16 |
| Running Jobs | 7 |
| Software | 7 |
| Training | 8 |
| GPU | 6 |
| Style reference | 6 |
| Access | 3 |
| Getting Started | 2 |
| Filesystem | 2 |
| Policy | 3 |
| Cluster Info | 1 |
| Data Transfer | 1 |
| Troubleshooting | 2 |
