
#include <pybind11/pybind11.h>
#include <pybind11/eigen.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>
#include <arma.hpp>
#include <estimators.hpp>
#include <simulate.hpp>

namespace py = pybind11;
using namespace robarma;

PYBIND11_MODULE(_robarma, m)
{
    m.doc() = "Python bindings for the robarma C++ library";

    // Bind arma_params
    py::class_<arma_params>(m, "arma_params", R"pbdoc(
        Stores ARMA parameters (phi, theta, mu).
        
        Parameters
        ----------
        phi : numpy.ndarray
            AR coefficients
        theta : numpy.ndarray
            MA coefficients
        mu : float
            Mean parameter
    )pbdoc")
        .def(py::init<const Eigen::VectorXd &, const Eigen::VectorXd &, double>(),
             py::arg("phi"), py::arg("theta"), py::arg("mu"))
        .def_readwrite("phi", &arma_params::phi)
        .def_readwrite("theta", &arma_params::theta)
        .def_readwrite("mu", &arma_params::mu);

    // Bind estimation_result
    py::class_<estimation_result>(m, "estimation_result", R"pbdoc(
        Stores the outcome of an ARMA parameter estimation.
        
        Attributes
        ----------
        method : estimation_method
            Which estimation method was used
        convergence : bool
            Whether the optimizer converged
        final_cost : float
            Objective function value
        report : str
            Optional optimizer report
    )pbdoc")
        .def(py::init<>())
        .def_property(
            "method",
            [](const estimation_result &self)
            { return self.method; },
            [](estimation_result &self, estimation_method value)
            { self.method = value; },
            "Which estimation method was used (estimation_method)")
        .def_readwrite("convergence", &estimation_result::convergence)
        .def_readwrite("final_cost", &estimation_result::final_cost)
        .def_readwrite("report", &estimation_result::report)
        .def("__repr__", [](const estimation_result &self)
             {
		std::ostringstream oss;
		oss << self;
		return oss.str(); });

    // Bind arma_model
    py::class_<arma_model>(m, "arma_model", R"pbdoc(
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
    )pbdoc")
        .def(py::init<const Eigen::VectorXd &, int, int>(), py::arg("y"), py::arg("p"), py::arg("q"))
        .def_readwrite("y", &arma_model::y)
        .def_readwrite("p", &arma_model::p)
        .def_readwrite("q", &arma_model::q)
        .def_readwrite("n", &arma_model::n)
        .def_readwrite("r", &arma_model::r)
        .def_readwrite("num_params", &arma_model::num_params)
        .def_readwrite("sigma", &arma_model::sigma)
        .def_readwrite("mu", &arma_model::mu);

    // Bind arma_fit
    py::class_<arma_fit>(m, "arma_fit", R"pbdoc(
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
    )pbdoc")
        .def_property_readonly("model", [](const arma_fit &self)
                               { return &self.model; }, py::return_value_policy::reference)
        .def_readonly("params", &arma_fit::params)
        .def_readonly("result", &arma_fit::result)
        .def_readonly("initial_params", &arma_fit::initial_params)
        .def_readonly("initial_result", &arma_fit::initial_result)
        .def("__repr__", [](const arma_fit &self)
             {
		std::ostringstream oss;
		oss << self;
		return oss.str(); });

    // Bind estimation methods (as string for now)
    py::enum_<estimation_method>(m, "estimation_method")
        .value("hannan_rissanen", estimation_method::hannan_rissanen)
        .value("ols", estimation_method::ols)
        .value("mle", estimation_method::mle)
        .value("ftau", estimation_method::ftau)
        .value("s", estimation_method::s)
        .value("bs", estimation_method::bs)
        .value("mm", estimation_method::mm)
        .value("bmm", estimation_method::bmm);

    // Bind estimator functions with short names (no namespace conflict)
    m.def("ols", &estimators::ols, py::arg("model"), R"pbdoc(
        Fit an ARMA(p, q) process using the ordinary least squares (OLS) estimator.
        
        Parameters
        ----------
        model : arma_model
            The ARMA model to fit.
        
        Returns
        -------
        arma_fit
            The fit result, including estimated parameters and diagnostics.
    )pbdoc");
    m.def("mle", &estimators::mle, py::arg("model"), R"pbdoc(
        Fit an ARMA(p, q) process using the maximum likelihood estimator (MLE).
        
        Parameters
        ----------
        model : arma_model
            The ARMA model to fit.
        
        Returns
        -------
        arma_fit
            The fit result, including estimated parameters and diagnostics.
    )pbdoc");
    m.def("ftau", &estimators::ftau, py::arg("model"), R"pbdoc(
        Fit an ARMA(p, q) process using the filtered tau estimator.
        
        Parameters
        ----------
        model : arma_model
            The ARMA model to fit.
        
        Returns
        -------
        arma_fit
            The fit result, including estimated parameters and diagnostics.
    )pbdoc");
    m.def("s", &estimators::s, py::arg("model"), R"pbdoc(
        Fit an ARMA(p, q) process using the S estimator.
        
        Parameters
        ----------
        model : arma_model
            The ARMA model to fit.
        
        Returns
        -------
        arma_fit
            The fit result, including estimated parameters and diagnostics.
    )pbdoc");
    m.def("mm", &estimators::mm, py::arg("model"), R"pbdoc(
        Fit an ARMA(p, q) process using the MM estimator.
        
        Parameters
        ----------
        model : arma_model
            The ARMA model to fit.
        
        Returns
        -------
        arma_fit
            The fit result, including estimated parameters and diagnostics.
    )pbdoc");
    m.def("bip_mm", &estimators::bip_mm, py::arg("model"), R"pbdoc(
        Fit an ARMA(p, q) process using the BIP-MM estimator.
        
        Parameters
        ----------
        model : arma_model
            The ARMA model to fit.
        
        Returns
        -------
        arma_fit
            The fit result, including estimated parameters and diagnostics.
    )pbdoc");

    // Bind simulate
    m.def("simulate", &robarma::simulate,
          py::arg("phi") = Eigen::VectorXd{},
          py::arg("theta") = Eigen::VectorXd{},
          py::arg("mu") = 0.0,
          py::arg("n") = 100,
          py::arg("burn_in") = 100,
          py::arg("seed") = 0,
          R"pbdoc(
        Simulate an ARMA(p, q) process with normal errors.
        
        Parameters
        ----------
        phi : numpy.ndarray, optional
            AR parameters (default: empty)
        theta : numpy.ndarray, optional
            MA parameters (default: empty)
        mu : float, optional
            Location parameter (default: 0.0)
        n : int, optional
            Sample size (default: 100)
        burn_in : int, optional
            Burn-in period (default: 100)
        seed : int, optional
            Random seed (default: 0, uses current time)
        
        Returns
        -------
        numpy.ndarray
            Simulated time series.
    )pbdoc");
}
