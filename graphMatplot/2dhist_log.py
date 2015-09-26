# -*- coding: utf-8 -*-
"""
Created on Tue Sep 08 12:20:18 2015

@author: rajat
"""

from matplotlib.colors import LogNorm
from pylab import *

#normal distribution center at x=0 and y=5
x = randn(100000)
y = randn(100000)+5

hist2d(x, y, bins=40, norm=LogNorm())
colorbar()
show()