# Gaussian Process Factor Analysis

This repository contains different methods for the Gaussian process model with Poisson observations. It has been developed and implemented with the goal of modelling spike-train recordings from neural populations, but some of the methods will be applicable more generally.

In particular, the repository includes methods for

 * Laplace approximation for state-inference
 * Variational method for state-inference
 * Expectation maximisation for parameter learning, using Laplace or Variational inference
     * Full EM, where all available trials are processed in each iteration
     * Variants of stochastic EM, where a subset of avilable trials are processed in each iteration

## Usage

To get started, run the example script either by `python test.py` in bash or`run test.py` in iPython. The software is developed within the Anaconda python 3 environment.

TODO:

-> Known regressors. 
Adding an option to include a number of known regressors. This can be useful if you want to include an external signal as a predictor into the model. Examples of such signals could be the local field potential or a stimulus with known temporal dynamics.


-> Estimation of residual covariance. 
Adding an option to estimate the residual covariance that remains after a certain number of latent factors have been accounted for. This can be useful if you want to estimate the covariance in the presence of some confounding variable(extraneous variable in a model correlated with both the dependent and independent variable), which is modeled by the latent factor.

## Motivated from https://github.com/mackelab/poisson-gpfa with source code Copyright (c) 2015, mackelab All rights reserved.