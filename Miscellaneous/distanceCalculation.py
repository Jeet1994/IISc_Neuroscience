# -*- coding: utf-8 -*-

import os
import scipy.io as sio
import numpy as np

def calculateDistance(red_x_prev, red_y_prev, red_x_next, red_y_next):
    distance  = np.sqrt((red_x_next - red_x_prev)**2 + (red_y_next - red_y_prev)**2)
    return distance 
    
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".mat"):
        distance = []
        distance.append(0)
        
        data = sio.loadmat(filename)
        red_x = data['red_x'][0]
        red_y = data['red_y'][0]
        
        for i in range(1,len(red_x)):
            if (red_x[i-1]==0 or red_y[i-1]==0) and (red_x[i]==0 or red_y[i]==0):
                distancebwFrames = 640
            else:
                distancebwFrames = (calculateDistance(red_x[i-1], red_y[i-1], red_x[i], red_y[i]))
            distance.append(distancebwFrames)
        
        sio.savemat(filename, mdict={'red_x':red_x, 'red_y':red_y,'distance':distance})
