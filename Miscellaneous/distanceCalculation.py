# -*- coding: utf-8 -*-

import os
import scipy.io as sio
import numpy as np

def calculateDistance(x_prev, y_prev, x_next, y_next):
    distance  = np.sqrt((x_next - x_prev)**2 + (y_next - y_prev)**2)
    return distance 
    
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".mat"):
        distance = []
        distance.append(0)
        
        data = sio.loadmat(filename)
        red_x = list(data['red_x'][0])
        red_y = list(data['red_y'][0])
        green_x = list(data['green_x'][0])
        green_y = list(data['green_y'][0])
        
        for i in range(1,len(red_x)):
            if (red_x[i-1]==-1 or red_x[i]==-1):
                distancebwFrames = -1
            else:
                x_prev = red_x[i-1] + green_x[i-1]
                y_prev = red_y[i-1] + green_y[i-1]
                x_current = red_x[i] + green_x[i]
                y_current = red_y[i] + green_y[i]
                distancebwFrames = calculateDistance(x_prev, y_prev, x_current, y_current)
                
            distance.append(distancebwFrames)
        
        sio.savemat('distance.mat', mdict={'distance':distance})
