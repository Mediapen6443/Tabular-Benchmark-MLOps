import torch

from src.models import ModelWrapper


def test_model_wrapper_sklearn():
    model = ModelWrapper("sklearn", "classification", 10)
    assert model.model is not None


def test_model_wrapper_pytorch():
    model = ModelWrapper("pytorch", "regression", 10)
    assert isinstance(model.model, torch.nn.Module)
