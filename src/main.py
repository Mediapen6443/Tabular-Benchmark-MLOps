import argparse
import sys
from pathlib import Path

import torch
import yaml

src_path = Path(__file__).resolve().parent
sys.path.insert(0, str(src_path.parent))

from src.data import generate_data
from src.train import train_pipeline
from src.utils import get_logger, set_seed, setup_logging

logger = get_logger(__name__)


def load_config(config_path: str) -> dict:
    """Load YAML configuration."""
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def parse_args():
    parser = argparse.ArgumentParser(description="Tabular Benchmark MLOps")
    parser.add_argument(
        "--task",
        type=str,
        choices=["classification", "regression"],
        default="classification",
    )
    parser.add_argument(
        "--model",
        type=str,
        choices=["sklearn", "xgboost", "pytorch", "all"],
        default="all",
    )
    parser.add_argument("--config", type=str, default="configs/default.yaml")
    parser.add_argument("--epochs", type=int, default=None)
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--offline", action="store_true", help="Run W&B offline")
    return parser.parse_args()


def main():
    args = parse_args()
    config = load_config(args.config)

    if args.epochs:
        config["epochs"] = args.epochs
    if args.seed:
        config["seed"] = args.seed

    set_seed(config["seed"])
    setup_logging()

    if args.offline:
        import os

        os.environ["WANDB_MODE"] = "offline"

    device = "cuda" if torch.cuda.is_available() else "cpu"
    logger.info(f"Using device: {device}")

    X_train, X_test, y_train, y_test, _ = generate_data(
        task=args.task, seed=config["seed"], test_size=config["test_size"]
    )

    models = ["sklearn", "xgboost", "pytorch"] if args.model == "all" else [args.model]

    for model_name in models:
        try:
            train_pipeline(
                model_name=model_name,
                task=args.task,
                X_train=X_train,
                X_test=X_test,
                y_train=y_train,
                y_test=y_test,
                config=config,
                device=device,
            )
        except Exception as e:
            logger.error(f"Failed training {model_name}: {e}")


if __name__ == "__main__":
    main()
