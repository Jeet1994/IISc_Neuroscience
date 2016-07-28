# -*- coding: utf-8 -*-
"""
Created on Sat May 08 18:49:02 2016

@author: rajat
"""

import numpy as np
from scipy.spatial import distance

positionDataFile = open('position.txt', 'rb')
positionData = []

for data in positionDataFile:
    info = data.split(' ')
    x,y = info[0], info[1]
    if x=='None' and y==' None':
        x,y = 0,0
    else:
        x,y = float(x), float(y)
    positionData.append([x,y])

linear_velocity = []


#atan2: finds the angle in radians between the positive x-axis and points given by coordinates (x,y)
for i in range(1,len(positionData)-1):
    point1 = np.asarray(positionData[i-1])
    point2 = np.asarray(positionData[i])
    distance = distance.euclidean(point1, point2)
    velocity = distance/(t[i]- t[i-1])
    linear_velocity.append(velocity)
                        
