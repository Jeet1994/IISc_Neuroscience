# -*- coding: utf-8 -*-
"""
Created on Fri Mar 04 10:33:41 2016

@author: rajat
"""
import scipy.signal
import numpy as np
import scipy.io
import pylab as pl

mat = scipy.io.loadmat('matlab.mat')

t = 1 - np.abs(np.linspace(-1, 1, 21))
kernel = t.reshape(21, 1) * t.reshape(1, 21)

final = scipy.signal.convolve2d(mat['final_map'], kernel)
occupancy = scipy.signal.convolve2d(mat['occupancy2'], kernel)
spike_map = scipy.signal.convolve2d(mat['spike_map'], kernel)

pl.pcolor(final)
pl.colorbar()
pl.show()

pl.pcolor(occupancy)
pl.colorbar()
pl.show()

pl.pcolor(spike_map)
pl.colorbar()
pl.show()