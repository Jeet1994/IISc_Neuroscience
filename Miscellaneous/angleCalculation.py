# -*- coding: utf-8 -*-
"""
Created on Fri Sep 09 14:22:22 2016

@author: rajat
"""

import numpy as np

REFERENCE = [0, 0]

def angleBwLED(redLEDCoords, greenLEDCoords, Reference= REFERENCE):
    
    points = np.array([redLEDCoords, greenLEDCoords, Reference])
    
    greenREdLEDVector = points[1] - points[0]
    referenceGreenLEDVector =  points[2] - points[1]
    referenceRedLEDVector = points[0] - points[2] 
    
    angles  = []
    for v1, v2 in ((greenREdLEDVector, -referenceGreenLEDVector), (referenceGreenLEDVector, -referenceRedLEDVector), (referenceRedLEDVector, -greenREdLEDVector)):
        cosang = np.dot(v1, v2)
        sinang = np.linalg.norm(v1) * np.linalg.norm(v2)
        angles.append(np.arccos(sinang/cosang) * 180 / np.pi)

    if sum(angles) == 180.0:
        return angles[0]
    else:
        raise 
        
angle = angleBwLED([2,0],[0,2])