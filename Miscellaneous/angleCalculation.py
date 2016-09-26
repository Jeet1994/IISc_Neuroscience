# -*- coding: utf-8 -*-
"""
Created on Fri Sep 09 14:22:22 2016
@author: rajat
"""

import numpy as np
import scipy.io as sio

REFERENCE_VECTOR = np.array([0,200]) - np.array([0,0])

def headDirectionAngle(redLEDCoords, greenLEDCoords, referenceVector= REFERENCE_VECTOR):
    greenRedLEDVector = np.array(greenLEDCoords) - np.array(redLEDCoords)
    angle = np.math.atan2(np.linalg.det([referenceVector,greenRedLEDVector]),np.dot(referenceVector,greenRedLEDVector))
    return np.degrees(angle)
        
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".mat"):
        anglebwLED = []
        
        data = sio.loadmat(filename)
        red_x = list(data['red_x'][0])
        red_y = list(data['red_y'][0])
        green_x = list(data['green_x'][0])
        green_y = list(data['green_y'][0])
        
        for i in range(len(red_x)):
            if (red_x[i]!=-1 and green_x[i]!=-1):
                angle = headDirectionAngle([red_x[i], red_y[i]], [green_x[i], green_y[i]], referenceVector= REFERENCE_VECTOR)
            else:
                angle = -1
            anglebwLED.append(angle)
    
    sio.savemat('angle.mat', mdict={'angle':anglebwLED})
