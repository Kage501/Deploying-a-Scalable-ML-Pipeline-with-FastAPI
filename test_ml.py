import pytest
# TODO: add necessary import
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from ml.data import apply_label
from ml.model import compute_model_metrics, train_model

# TODO: implement the first test. Change the function name and input as needed
def test_one():
    """
    Test that apply_label returns the expected salary string.
    """
    assert apply_label([1]) == ">50K"
    assert apply_label([0]) == "<=50K"


# TODO: implement the second test. Change the function name and input as needed
def test_two():
    """
    Test that train_model returns a RandomForestClassifier.
    """
    X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
    y = np.array([0, 0, 1, 1])

    model = train_model(X, y)

    assert isinstance(model, RandomForestClassifier)


# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    Test that compute_model_metrics returns valid metric values.
    """
    y = np.array([1, 0, 1, 1])
    preds = np.array([1, 0, 0, 1])

    precision, recall, fbeta = compute_model_metrics(y, preds)

    assert isinstance(precision, float)
    assert isinstance(recall, float)
    assert isinstance(fbeta, float)
    assert 0 <= precision <= 1
    assert 0 <= recall <= 1
    assert 0 <= fbeta <= 1
