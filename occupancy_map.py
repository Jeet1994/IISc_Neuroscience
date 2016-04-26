# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 10:19:13 2016

@author: rajat
"""

import scipy.io as sio
import pylab as pl
import numpy as np
import scipy.ndimage as sim
    
#function to find mask of circular regions
def circular_mask(shape,centre,radius,angle_range):
    """
    Return a boolean mask for a circular sector. The start/stop angles in  
    `angle_range` should be given in clockwise order.
    """

    x,y = np.ogrid[:shape[0],:shape[1]]
    cx,cy = centre
    tmin,tmax = np.deg2rad(angle_range)

    # ensure stop angle > start angle
    if tmax < tmin:
            tmax += 2*np.pi

    # convert cartesian --> polar coordinates
    r2 = (x-cx)*(x-cx) + (y-cy)*(y-cy)
    theta = np.arctan2(x-cx,y-cy) - tmin

    # wrap angles between 0 and 2*pi
    theta %= (2*np.pi)

    # circular mask
    circmask = r2 <= radius*radius

    # angular mask
    anglemask = theta <= (tmax-tmin)

    return circmask*anglemask
    
#loading the occupancy map points
occupancy = sio.loadmat('occ.mat')

#save all the points from the dictionary above - returns a 2d array
occupancy =  occupancy['occupancy']

#center and radius for the mask calculated using brute force method 
(circle_x,circle_y) = (370,330)
radius = 180

mask = circular_mask(occupancy.shape,(circle_x, circle_y),radius,(0,360))

#make all the elements outisde the mask 0
occupancy[~mask] = 0

#mask all the area except our Region of Interest (ROI) i.e. ~mask 
final_occupancy = np.ma.MaskedArray(occupancy, mask=~mask)

#convolve filter test
test_convolve_filter = np.array([[1,1,1],[1,9,1],[1,1,1]])
test_convolve = sim.filters.convolve(final_occupancy, test_convolve_filter)

#Gaussian filter test
test_gaussian = sim.filters.gaussian_filter(final_occupancy, sigma=2.0)

pl.pcolor(test_gaussian)
pl.colorbar()
pl.show()