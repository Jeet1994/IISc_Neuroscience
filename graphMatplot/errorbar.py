# -*- coding: utf-8 -*-
"""
Created on Tue Sep 08 12:04:52 2015

@author: rajat
"""

"""
Demo of the errorbar function.
"""
import numpy as np
import matplotlib.pyplot as plt

# example data
x = np.arange(0.1, 4, 0.5)
y = np.exp(-x)

plt.errorbar(x, y, xerr=0.2, yerr=0.4)
plt.show()