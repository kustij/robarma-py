import pytest
import numpy as np
import robarma


def test_import():
    assert hasattr(robarma, "arma_model")
    assert hasattr(robarma, "simulate")


def test_arma_model_creation():
    y = np.zeros(10)
    model = robarma.arma_model(y, 1, 1)
    assert model.p == 1
    assert model.q == 1
    assert hasattr(model, "y")


def test_simulate():
    phi = np.array([0.5])
    theta = np.array([0.2])
    mu = 1.0
    n = 50
    e = np.random.standard_cauchy(n)
    result = robarma.simulate(phi=phi, theta=theta, mu=mu, n=n, e=e)
    assert isinstance(result, np.ndarray)
    assert result.shape == (n,)


def test_ols():
    y = np.random.randn(100)
    model = robarma.arma_model(y, 1, 1)
    result = robarma.mm(model)
    assert hasattr(result, "params")
    assert hasattr(result, "result")
