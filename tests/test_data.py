"""Tests for data generation."""

import numpy as np

from src.data import generate_data


def test_classification_shape():
    """Test classification data shape."""
    X_train, X_test, y_train, y_test, _ = generate_data("classification", 42, 0.2)
    assert X_train.shape[0] > 0
    assert len(np.unique(y_train)) > 1


def test_regression_shape():
    """Test regression data shape."""
    X_train, X_test, y_train, y_test, _ = generate_data("regression", 42, 0.2)
    assert X_train.shape[0] > 0
    assert y_train.dtype == np.float64
