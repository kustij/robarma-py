"""
Python bindings for the robarma C++ library
"""
from __future__ import annotations
import numpy
import numpy.typing
import typing
__all__: list[str] = ['arma_fit', 'arma_model', 'arma_params', 'bip_mm', 'estimation_method', 'estimation_result', 'ftau', 'mle', 'mm', 'ols', 's', 'simulate']
class arma_fit:
    """
    
            Stores the result of an ARMA estimation, including final and initial values.
            
            Attributes
            ----------
            model : arma_model
                The fitted model
            params : arma_params
                Estimated parameters
            result : estimation_result
                Estimation result and diagnostics
            initial_params : arma_params
                Initial parameter estimates
            initial_result : estimation_result
                Initial estimation result
        
    """
    def __repr__(self) -> str:
        ...
    @property
    def initial_params(self) -> robarma._robarma.arma_params | None:
        ...
    @property
    def initial_result(self) -> robarma._robarma.estimation_result | None:
        ...
    @property
    def model(self) -> arma_model:
        ...
    @property
    def params(self) -> arma_params:
        ...
    @property
    def result(self) -> estimation_result:
        ...
class arma_model:
    """
    
            Represents an ARMA model and its associated time series data.
            
            Parameters
            ----------
            y : numpy.ndarray
                Observed time series
            p : int
                AR order
            q : int
                MA order
            
            Attributes
            ----------
            y : numpy.ndarray
                Observed time series
            p : int
                AR order
            q : int
                MA order
            n : int
                Length of time series
            r : int
                max(p, q)
            num_params : int
                Number of parameters
            sigma : float
                Scale estimate
            mu : float
                Mean estimate
        
    """
    def __init__(self, y: typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[m, 1]"], p: typing.SupportsInt, q: typing.SupportsInt) -> None:
        ...
    @property
    def mu(self) -> float:
        ...
    @mu.setter
    def mu(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def n(self) -> int:
        ...
    @n.setter
    def n(self, arg0: typing.SupportsInt) -> None:
        ...
    @property
    def num_params(self) -> int:
        ...
    @num_params.setter
    def num_params(self, arg0: typing.SupportsInt) -> None:
        ...
    @property
    def p(self) -> int:
        ...
    @p.setter
    def p(self, arg0: typing.SupportsInt) -> None:
        ...
    @property
    def q(self) -> int:
        ...
    @q.setter
    def q(self, arg0: typing.SupportsInt) -> None:
        ...
    @property
    def r(self) -> int:
        ...
    @r.setter
    def r(self, arg0: typing.SupportsInt) -> None:
        ...
    @property
    def sigma(self) -> float:
        ...
    @sigma.setter
    def sigma(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def y(self) -> typing.Annotated[numpy.typing.NDArray[numpy.float64], "[m, 1]"]:
        ...
    @y.setter
    def y(self, arg0: typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[m, 1]"]) -> None:
        ...
class arma_params:
    """
    
            Stores ARMA parameters (phi, theta, mu).
            
            Parameters
            ----------
            phi : numpy.ndarray
                AR coefficients
            theta : numpy.ndarray
                MA coefficients
            mu : float
                Mean parameter
        
    """
    def __init__(self, phi: typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[m, 1]"], theta: typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[m, 1]"], mu: typing.SupportsFloat) -> None:
        ...
    @property
    def mu(self) -> float:
        ...
    @mu.setter
    def mu(self, arg0: typing.SupportsFloat) -> None:
        ...
    @property
    def phi(self) -> typing.Annotated[numpy.typing.NDArray[numpy.float64], "[m, 1]"]:
        ...
    @phi.setter
    def phi(self, arg0: typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[m, 1]"]) -> None:
        ...
    @property
    def theta(self) -> typing.Annotated[numpy.typing.NDArray[numpy.float64], "[m, 1]"]:
        ...
    @theta.setter
    def theta(self, arg0: typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[m, 1]"]) -> None:
        ...
class estimation_method:
    """
    Members:
    
      hannan_rissanen
    
      ols
    
      mle
    
      ftau
    
      s
    
      bs
    
      mm
    
      bmm
    """
    __members__: typing.ClassVar[dict[str, estimation_method]]  # value = {'hannan_rissanen': <estimation_method.hannan_rissanen: 0>, 'ols': <estimation_method.ols: 1>, 'mle': <estimation_method.mle: 2>, 'ftau': <estimation_method.ftau: 3>, 's': <estimation_method.s: 4>, 'bs': <estimation_method.bs: 5>, 'mm': <estimation_method.mm: 6>, 'bmm': <estimation_method.bmm: 7>}
    bmm: typing.ClassVar[estimation_method]  # value = <estimation_method.bmm: 7>
    bs: typing.ClassVar[estimation_method]  # value = <estimation_method.bs: 5>
    ftau: typing.ClassVar[estimation_method]  # value = <estimation_method.ftau: 3>
    hannan_rissanen: typing.ClassVar[estimation_method]  # value = <estimation_method.hannan_rissanen: 0>
    mle: typing.ClassVar[estimation_method]  # value = <estimation_method.mle: 2>
    mm: typing.ClassVar[estimation_method]  # value = <estimation_method.mm: 6>
    ols: typing.ClassVar[estimation_method]  # value = <estimation_method.ols: 1>
    s: typing.ClassVar[estimation_method]  # value = <estimation_method.s: 4>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class estimation_result:
    """