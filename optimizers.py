import time
import numpy as np
import matplotlib.pyplot as plt
from tools import MSE
from pyESN.pyESN import ESN


def grid_optimize(data, params, xset, yset=None, verbose=False, visualize=False , kwargs**):
    """
    This function optimizes the ESN parameters, x and y, over a specified
    range of values. The optimal values are determined by minimizing
    the mean squared error. Those optimal values are returned.

    Parameters:
    -----------
    data : numpy array
        This is the dataset that the ESN should train and predict.
        If the training length plus the future total exceed the
        length of the data, an error will be thrown.
        **The shape of the transpose of the data will determine
        the number of inputs and outputs.**
    params : dictionary
        A dictionary containing all of the parameters required to
        initialize an ESN.
        Required parameters are:
            "n_reservoir" : int, the reservoir size
            "sparsity" : float, the sparsity of the reservoir
            "rand_seed" : int or None, specifies the initial seed
            "rho" : float, the spectral radius
            "noise" : the noise used for regularization
            "trainlen" : int, the training length
            "future" : int, the total prediction length
            "window" : int or None, the window size
    xset : numpy array
        The first set of values to be tested.
    yset : numpy array or None
        The second set of values to be tested at the same
        time as the xset. Can be None.
    verbose : boolean
        Specifies if the simulation outputs should be printed.
        Useful for debugging.
    visualize : boolean
        Specifies if the results should be visualized.
    kwargs**:
        The keys of the ESN parameters that should be optimized.
        Correspond to xset and yset.

    Returns:
    --------
    loss : numpy array
        The array or matrix of loss values.
    """

    # get the number of inputs and outputs.
