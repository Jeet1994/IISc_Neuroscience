# -*- coding: utf-8 -*-
"""
Created on Sat May 07 16:46:02 2016

@author: rajat

Angular velocity definition used here is rate of change of direction angle of animals motion. 
This is assuming that the animal always walks forward
"""

import math

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

angular_direction = []


#atan2: finds the angle in radians between the positive x-axis and points given by coordinates (x,y)
for i in range(1,len(positionData)-1):
    angularDirection = (math.atan2(positionData[i+1][0] - positionData[i][0], positionData[i+1][1] - positionData[i][1]) - math.atan2(positionData[i+1][0] - positionData[i-1][0], positionData[i+1][1] - positionData[i-1][1]))/(t[i]- t[i-1])
    math.degrees(angularDirection)
    angular_direction.append(angularDirection)
