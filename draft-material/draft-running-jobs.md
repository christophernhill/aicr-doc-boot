# Running Jobs

AICR uses [Slurm](https://slurm.schedmd.com/) to manage compute resources and schedule jobs. This page covers everything you need to submit, monitor, and manage your work on the cluster.

!!! danger
    Do not run compute-intensive work on login nodes. Login nodes are shared and have strict resource limits (4 CPU cores, 8 GB memory per user). Jobs that exceed these limits will be terminated. Use Slurm to run your work on compute nodes.

## Partitions

A partition is a group of compute nodes with a shared purpose and set of resource limits. Choose a partition based on the type of work you need to do.

| Partition | Hardware | GPU | Max Wall Time | Default Time | Use Case |
|-----------|----------|-----|---------------|--------------|----------|
| `cpu` | w-series (128 cores, 1 TB memory) | — | 24 hours | 15 min | CPU-only computation |
| `rtx-batch` | a-series | NVIDIA RTX PRO 6000 | 24 hours | 1 hour | RTX GPU batch workloads |
| `rtx-devel` | a-series | NVIDIA RTX PRO 6000 | 4 hours | 15 min | RTX GPU development and testing |
| `b200-batch` | b-series | NVIDIA B200 | 24 hours | 1 hour | B200 GPU batch workloads |
| `b200-devel` | b-series | NVIDIA B200 | 4 hours | 15 min | B200 GPU development and testing |

Check current partition availability:

```bash
$ sinfo
```

!!! note
    The `devel` partitions are for short interactive and debugging work. They have a 4-hour maximum wall time and a limit of 4 concurrent jobs per user.

## Submitting a Batch Job

Batch jobs run unattended after submission. Write a job script, submit it with `sbatch`, and collect the results when it finishes.

### Basic Job Script

```bash
#!/bin/bash
#SBATCH --job-name=my_analysis
#SBATCH --partition=cpu
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=02:00:00
#SBATCH --account=ACCOUNT_NAME
#SBATCH --output=%x-%j.out

# Load required software
module purge
module load python

# Run the program
python my_script.py
```

Submit the job:

```bash
$ sbatch my_job.sh
Submitted batch job 12345
```

!!! tip
    Always specify `--account`. Valid account names correspond to your institution: `bu`, `hu`, `mit`, `neu`, `umass`, `uml`, `umb`, `umassd`, `umassmed`, `yale`, `ma`, or `aihub`. If you are unsure which account to use, check with your PI or contact [AICR support](../help.md).

### Output Files

By default, Slurm writes job output to `slurm-JOBID.out` in the directory where you submitted the job. Customize this with `--output` and `--error`:

```bash
#SBATCH --output=%x-%j.out    # JOBNAME-JOBID.out
#SBATCH --error=%x-%j.err     # JOBNAME-JOBID.err
```

Common filename patterns:

| Pattern | Expands To |
|---------|-----------|
| `%j` | Job ID |
| `%x` | Job name |
| `%a` | Array task ID |
| `%N` | Short hostname of first node |

## GPU Jobs

Request GPUs with the `--gpus` or `--gres` directive and submit to a GPU partition.

### Single-GPU Job

```bash
#!/bin/bash
#SBATCH --job-name=gpu_training
#SBATCH --partition=rtx-batch
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --gpus=1
#SBATCH --mem=32G
#SBATCH --time=08:00:00
#SBATCH --account=ACCOUNT_NAME
#SBATCH --output=%x-%j.out

module purge
module load cuda

python train.py
```

### Multi-GPU Job

Request multiple GPUs on a single node:

```bash
#!/bin/bash
#SBATCH --job-name=multi_gpu
#SBATCH --partition=b200-batch
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --gpus-per-node=4
#SBATCH --cpus-per-task=32
#SBATCH --mem=128G
#SBATCH --time=12:00:00
#SBATCH --account=ACCOUNT_NAME
#SBATCH --output=%x-%j.out

module purge
module load cuda

torchrun --nproc_per_node=4 train.py
```

### Requesting a Specific GPU Type

Use GRES syntax to request a particular GPU model:

```bash
#SBATCH --gres=gpu:rtx6000:2    # 2 RTX PRO 6000 GPUs
#SBATCH --gres=gpu:b200:4       # 4 B200 GPUs
```

<!-- TODO: verify exact GRES type names (rtx6000 vs rtx_pro_6000 vs other) from gres.conf -->

!!! tip
    Match your partition to your GPU type. Use `rtx-batch` or `rtx-devel` for RTX GPUs, and `b200-batch` or `b200-devel` for B200 GPUs.

## Interactive Jobs

Interactive jobs give you a shell on a compute node for development, debugging, and testing.

### Quick Interactive Session

```bash
$ salloc --partition=rtx-devel --gpus=1 --cpus-per-task=4 --mem=16G --time=01:00:00 --account=ACCOUNT_NAME
```

This allocates resources and drops you into a shell on a compute node. When you are done, type `exit` to release the resources.

### Interactive Session with srun

Alternatively, use `srun` with `--pty` to get a shell:

```bash
$ srun --partition=b200-devel --gpus=1 --time=00:30:00 --account=ACCOUNT_NAME --pty bash
```

!!! warning
    Interactive `devel` partitions are limited to 4 concurrent jobs per user and a maximum wall time of 4 hours. Use them for testing, then switch to a batch partition for production runs.

## Multi-Node Jobs

For jobs that span multiple nodes, use `srun` to launch your application across the allocation.

### MPI Job

```bash
#!/bin/bash
#SBATCH --job-name=mpi_run
#SBATCH --partition=cpu
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=32
#SBATCH --time=04:00:00
#SBATCH --account=ACCOUNT_NAME
#SBATCH --output=%x-%j.out

module purge
module load openmpi

srun --mpi=pmix ./my_mpi_application
```

AICR uses PMIx for MPI process management. Always pass `--mpi=pmix` to `srun` when launching MPI applications.

### Multi-Node GPU Job

```bash
#!/bin/bash
#SBATCH --job-name=distributed_training
#SBATCH --partition=b200-batch
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=1
#SBATCH --gpus-per-node=8
#SBATCH --cpus-per-task=64
#SBATCH --mem=0
#SBATCH --time=24:00:00
#SBATCH --account=ACCOUNT_NAME
#SBATCH --output=%x-%j.out

module purge
module load cuda

srun torchrun \
    --nnodes=$SLURM_NNODES \
    --nproc_per_node=8 \
    --rdzv_backend=c10d \
    --rdzv_endpoint=$(hostname):29500 \
    train.py
```

!!! note
    Use `--mem=0` to request all available memory on the allocated nodes. This is useful for exclusive multi-node jobs where you need the full machine.

## Job Arrays

Job arrays submit many similar jobs from a single script — useful for parameter sweeps, processing multiple input files, or running repeated experiments.

```bash
#!/bin/bash
#SBATCH --job-name=sweep
#SBATCH --partition=rtx-batch
#SBATCH --gpus=1
#SBATCH --time=02:00:00
#SBATCH --account=ACCOUNT_NAME
#SBATCH --array=0-49
#SBATCH --output=%x-%a-%j.out

module purge
module load cuda python

python train.py --seed=$SLURM_ARRAY_TASK_ID
```

Submit once, and Slurm creates 50 independent jobs (task IDs 0 through 49). Each job can read `$SLURM_ARRAY_TASK_ID` to vary its behavior.

Limit concurrency to avoid monopolizing resources:

```bash
#SBATCH --array=0-99%10    # Run at most 10 tasks at a time
```

!!! note
    The maximum array size is 10,000 tasks.

## Monitoring Jobs

### Check Job Status

View your running and pending jobs:

```bash
$ squeue -u $USER
```

View all jobs on a specific partition:

```bash
$ squeue -p rtx-batch
```

### Detailed Job Information

Inspect a running or pending job:

```bash
$ scontrol show job JOBID
```

### Job History and Accounting

View completed jobs and their resource usage:

```bash
$ sacct -j JOBID --format=JobID,JobName,Partition,Elapsed,MaxRSS,State
```

Check your recent job history:

```bash
$ sacct -u $USER --starttime=now-7days --format=JobID,JobName,Partition,Elapsed,State,ExitCode
```

!!! tip
    Use `sacct` to check whether your jobs are using the resources you requested. If `MaxRSS` is much lower than the memory you requested, reduce `--mem` in future jobs so others can use those resources.

### Cancel a Job

```bash
$ scancel JOBID
```

Cancel all your jobs:

```bash
$ scancel -u $USER
```

Cancel a specific array task:

```bash
$ scancel JOBID_TASKID
```

## Common Slurm Directives Reference

| Directive | Description | Example |
|-----------|-------------|---------|
| `--job-name` | Name your job for easy identification | `--job-name=my_training` |
| `--partition` | Target partition | `--partition=rtx-batch` |
| `--account` | Institution account for fairshare | `--account=mit` |
| `--nodes` | Number of nodes | `--nodes=2` |
| `--ntasks` | Total number of tasks (processes) | `--ntasks=8` |
| `--ntasks-per-node` | Tasks per node | `--ntasks-per-node=4` |
| `--cpus-per-task` | CPU cores per task | `--cpus-per-task=8` |
| `--mem` | Total memory per node | `--mem=64G` |
| `--mem-per-cpu` | Memory per CPU core | `--mem-per-cpu=4G` |
| `--gpus` | Total GPU count | `--gpus=2` |
| `--gpus-per-node` | GPUs per node | `--gpus-per-node=4` |
| `--gres` | Generic resource request | `--gres=gpu:b200:4` |
| `--time` | Maximum wall time (HH:MM:SS) | `--time=12:00:00` |
| `--output` | Standard output file path | `--output=%x-%j.out` |
| `--error` | Standard error file path | `--error=%x-%j.err` |
| `--array` | Job array specification | `--array=0-99%10` |
| `--exclusive` | Exclusive node access | `--exclusive` |
| `--dependency` | Job dependency | `--dependency=afterok:JOBID` |
| `--mail-type` | Email notifications | `--mail-type=END,FAIL` |
| `--mail-user` | Email address | `--mail-user=USER@example.edu` |

## Resource Defaults and Limits

Understanding the defaults helps you write efficient job scripts.

| Setting | Value |
|---------|-------|
| Default memory per CPU | 1 GB |
| Batch partition max wall time | 24 hours |
| Devel partition max wall time | 4 hours |
| Batch partition default time | 1 hour (`rtx-batch`, `b200-batch`) |
| CPU/devel partition default time | 15 minutes |
| Max concurrent interactive jobs (devel) | 4 per user |
| Max job array size | 10,000 tasks |

!!! tip
    Request only the resources you need. Slurm's fairshare scheduler gives higher priority to users and accounts that use fewer resources relative to their allocation. Over-requesting memory or time slows down your future jobs.

## Fairshare and Job Priority

AICR allocates resources fairly across institutions using Slurm's multifactor priority system. Your job's priority depends on:

1. **Fairshare** (highest weight) — How much your institution has used recently relative to its share. If your group has used less than its fair share, your jobs get higher priority.
2. **Queue time** — Jobs waiting longer get a priority boost.
3. **Job size and partition** — Minor factors compared to fairshare.

You do not need to manage fairshare yourself. Specify your `--account` correctly, and Slurm handles the rest.

## Useful Environment Variables

Inside a running job, Slurm sets these variables automatically:

| Variable | Contents |
|----------|----------|
| `$SLURM_JOB_ID` | Unique job ID |
| `$SLURM_JOB_NAME` | Job name from `--job-name` |
| `$SLURM_ARRAY_TASK_ID` | Array index (array jobs only) |
| `$SLURM_NNODES` | Number of allocated nodes |
| `$SLURM_NTASKS` | Total number of tasks |
| `$SLURM_CPUS_PER_TASK` | CPUs per task |
| `$SLURM_NODELIST` | List of allocated nodes |
| `$SLURM_SUBMIT_DIR` | Directory where `sbatch` was called |
| `$SLURM_GPUS_ON_NODE` | Number of GPUs on this node |

## Troubleshooting

| Problem | Likely Cause | Solution |
|---------|-------------|----------|
| Job stays `PENDING` | Requested resources exceed what is available or fairshare is low | Check `squeue -j JOBID` for the reason code. Reduce resource requests or wait for fairshare to recover. |
| `error: Batch job submission failed: Invalid account` | Wrong `--account` value | Use your institution's account name (e.g., `mit`, `umass`). Run `sacctmgr show associations user=$USER` to see your valid accounts. |
| Job killed with `OUT_OF_MEMORY` | Program exceeded requested memory | Increase `--mem` or `--mem-per-cpu` and resubmit. Check actual usage with `sacct -j JOBID --format=MaxRSS`. |
| `error: Unable to allocate resources` | Partition name misspelled or unavailable | Verify partition name with `sinfo`. Use one of: `cpu`, `rtx-batch`, `rtx-devel`, `b200-batch`, `b200-devel`. |
| Job timeout (`TIMEOUT` state) | Wall time too short | Increase `--time`. Check how long similar jobs take with `sacct`. |
| `FAILED` with exit code 1 | Your program crashed | Check the output/error files. Debug interactively on a `devel` partition. |
| GPUs not visible in job | Missing `--gpus` or wrong partition | Ensure you requested GPUs and submitted to a GPU partition. Verify with `nvidia-smi` inside the job. |

## See Also

- [Software](../software.md) — loading modules and using containers in your jobs
- [Filesystem Overview](../files/overview.md) — where to read and write job data
- [Getting Started](../getting-started.md) — submitting your first job
