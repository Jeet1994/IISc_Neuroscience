# -*- coding: utf-8 -*-
"""
Created on Fri Sep 09 14:22:22 2016

@author: rajat
"""

import numpy as np

REFERENCE_VECTOR = np.array([0,200]) - np.array([0,0])

def headDirectionAngle(redLEDCoords, greenLEDCoords, referenceVector= REFERENCE_VECTOR):

    greenRedLEDVector = np.array(greenLEDCoords) - np.array(redLEDCoords)
    angle = np.math.atan2(np.linalg.det([referenceVector,greenRedLEDVector]),np.dot(referenceVector,greenRedLEDVector))
    print np.degrees(angle)
        
angle = headDirectionAngle([100,100],[0,200])
