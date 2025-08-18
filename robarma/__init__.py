"""
RobARMA: Robust and classical ARMA estimators for Python.

This package provides a user-friendly Python interface to the RobARMA C++ library, including robust and classical ARMA(p, q) estimators and simulation tools.
"""

from ._robarma import (
    simulate,
    arma_model,
    arma_fit,
    ols,
    mle,
    ftau,
    s,
    mm,
    bip_mm,
)
