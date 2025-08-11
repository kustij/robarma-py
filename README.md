# RobARMA Python

Python bindings for the [RobARMA](https://github.com/kustij/robarma) C++ library.

## About this repository

This repository provides a modern, pip-installable Python interface to the [RobARMA](https://github.com/kustij/robarma) C++ library, which implements robust and classical estimators ARMA(p, q) processes.

**Features:**

- Robust estimators:
  - S
  - FTAU (filtered tau)
  - MM
  - BIP-MM (bounded innovation propagation MM)
- Classic estimators:
  - OLS (ordinary least squares)
  - MLE (maximum likelihood via Kalman filter)

## Installation

Clone this repository and initialize submodules:

```sh
git clone https://github.com/kustij/robarma-py.git
cd robarma-py
git submodule update --init --recursive
```

Then install with pip (in a virtual environment):

```sh
pip install .
```

## Usage

```python
import robarma
import numpy as np

# Simulate an ARMA(1, 1) process
y = robarma.simulate(phi=np.array([0.5]), theta=np.array([0.2]), mu=1.0, n=100)

# Fit an ARMA(1, 1) model using OLS
model = robarma.arma_model(y, 1, 1)
fit = robarma.mm(model)
print(fit.params)
```

## Documentation

- Python docstrings are available for all major classes and functions.
- For full C++ API documentation, see the [robarma Doxygen docs](https://github.com/kustij/robarma).

## License

See LICENSE file. The underlying C++ library is licensed under the same terms as [robarma](https://github.com/kustij/robarma).
