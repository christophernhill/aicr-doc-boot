"""
train.py — Self-contained example for AICR documentation.

Trains a small neural network on synthetic data. Works with all the Slurm
job scripts in the Running Jobs documentation:

    python train.py                              # single GPU or CPU
    torchrun --nproc_per_node=4 train.py         # multi-GPU (DDP)
    python train.py --seed=42                     # job array with seed

The task: predict a material's thermal conductivity from 16 simulated
sensor readings. This is a regression problem typical of scientific ML
workloads — simple enough to finish in minutes, realistic enough to
exercise the GPU and demonstrate standard training patterns.
"""

import argparse
import os
import time

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset


# ---------------------------------------------------------------------------
# Model
# ---------------------------------------------------------------------------

class SensorNet(nn.Module):
    """Three-layer network for regression on tabular sensor data."""

    def __init__(self, input_dim=16, hidden_dim=128):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, 1),
        )

    def forward(self, x):
        return self.net(x).squeeze(-1)


# ---------------------------------------------------------------------------
# Synthetic data
# ---------------------------------------------------------------------------

def make_dataset(n_samples, input_dim=16, seed=0):
    """Generate synthetic sensor-to-conductivity data.

    The target is a nonlinear function of the inputs so the network
    has something meaningful to learn, but the exact formula is not
    important — this is a documentation example.
    """
    gen = torch.Generator().manual_seed(seed)
    X = torch.randn(n_samples, input_dim, generator=gen)
    # Nonlinear target: sum of pairwise products plus noise
    y = (X[:, :8] * X[:, 8:]).sum(dim=1) + 0.1 * torch.randn(n_samples, generator=gen)
    return TensorDataset(X, y)


# ---------------------------------------------------------------------------
# Training
# ---------------------------------------------------------------------------

def train(args):
    # --- Distributed setup (safe to call even without torchrun) -----------
    distributed = "RANK" in os.environ
    if distributed:
        torch.distributed.init_process_group(backend="nccl")
        local_rank = int(os.environ["LOCAL_RANK"])
        rank = int(os.environ["RANK"])
        world_size = int(os.environ["WORLD_SIZE"])
        torch.cuda.set_device(local_rank)
        device = torch.device("cuda", local_rank)
    else:
        rank = 0
        world_size = 1
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    if rank == 0:
        print(f"Device: {device}  |  World size: {world_size}  |  Seed: {args.seed}")

    # --- Data -------------------------------------------------------------
    torch.manual_seed(args.seed)
    train_set = make_dataset(n_samples=args.train_samples, seed=args.seed)
    val_set = make_dataset(n_samples=args.val_samples, seed=args.seed + 1)

    if distributed:
        train_sampler = torch.utils.data.distributed.DistributedSampler(train_set)
    else:
        train_sampler = None

    train_loader = DataLoader(
        train_set,
        batch_size=args.batch_size,
        shuffle=(train_sampler is None),
        sampler=train_sampler,
        num_workers=2,
        pin_memory=True,
    )
    val_loader = DataLoader(val_set, batch_size=args.batch_size, num_workers=2, pin_memory=True)

    # --- Model ------------------------------------------------------------
    model = SensorNet().to(device)
    if distributed:
        model = torch.nn.parallel.DistributedDataParallel(model, device_ids=[local_rank])

    optimizer = torch.optim.Adam(model.parameters(), lr=args.lr)
    loss_fn = nn.MSELoss()

    # --- Training loop ----------------------------------------------------
    start = time.time()
    for epoch in range(1, args.epochs + 1):
        model.train()
        if distributed:
            train_sampler.set_epoch(epoch)

        epoch_loss = 0.0
        for X_batch, y_batch in train_loader:
            X_batch, y_batch = X_batch.to(device), y_batch.to(device)
            pred = model(X_batch)
            loss = loss_fn(pred, y_batch)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            epoch_loss += loss.item() * X_batch.size(0)

        epoch_loss /= len(train_set)

        # Validate on rank 0
        if rank == 0 and epoch % args.log_every == 0:
            model.eval()
            val_loss = 0.0
            with torch.no_grad():
                for X_batch, y_batch in val_loader:
                    X_batch, y_batch = X_batch.to(device), y_batch.to(device)
                    val_loss += loss_fn(model(X_batch), y_batch).item() * X_batch.size(0)
            val_loss /= len(val_set)
            elapsed = time.time() - start
            print(f"Epoch {epoch:>3d}/{args.epochs}  "
                  f"train_loss={epoch_loss:.4f}  val_loss={val_loss:.4f}  "
                  f"[{elapsed:.1f}s]")

    # --- Save checkpoint --------------------------------------------------
    if rank == 0:
        ckpt_path = os.path.join(args.output_dir, f"checkpoint_seed{args.seed}.pt")
        state = model.module.state_dict() if distributed else model.state_dict()
        torch.save({"epoch": args.epochs, "model_state_dict": state}, ckpt_path)
        print(f"Checkpoint saved to {ckpt_path}")

    if distributed:
        torch.distributed.destroy_process_group()


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train SensorNet on synthetic data")
    parser.add_argument("--seed", type=int, default=0, help="Random seed (useful for job arrays)")
    parser.add_argument("--epochs", type=int, default=20, help="Number of training epochs")
    parser.add_argument("--batch-size", type=int, default=256, help="Batch size per GPU")
    parser.add_argument("--lr", type=float, default=1e-3, help="Learning rate")
    parser.add_argument("--train-samples", type=int, default=50000, help="Number of training samples")
    parser.add_argument("--val-samples", type=int, default=10000, help="Number of validation samples")
    parser.add_argument("--log-every", type=int, default=5, help="Print metrics every N epochs")
    parser.add_argument("--output-dir", type=str, default=".", help="Directory for checkpoints")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    train(args)
