# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 10:38:59 2016

@author: rajat
"""

"""
File contains data in this format:

|------------------------|
|  X coord     (Single)  |
|------------------------|
|  Y coord     (Single)  |
--------------------------
"""

import matplotlib.pyplot as plt
import numpy as np
import cv2
import scipy.io as sio

blank_image = np.zeros((720,720,3), np.uint8)

positionData = []

pos = sio.loadmat('Day7_square_cam2_output_2016-08-04 16_46_12.639959.mat')
x1 = pos['red_x'][0][38500:101000]
y1 = pos['red_y'][0][38500:]
for x,y in zip(x1,y1):
    positionData.append((x,y))

#loop over the set of tracked pts
for index in xrange(1, len(positionData)):
    if index == len(positionData)-1:
        cv2.imwrite('trajectory.jpg',blank_image)

    #if either of the tracked pts are (0,0), ignore them
    if positionData[index-1]==(0,0) or positionData[index]==(0,0):
        continue
    
    #otherwise, compute the thickness of the line and
	# draw the connecting lines
    print index, positionData[index - 1], positionData[index]
    cv2.line(blank_image, positionData[index - 1], positionData[index], (0, 0, 255), 1)
 
    # show the frame to our screen
    cv2.imshow("Frame", blank_image)

    key = cv2.waitKey(1) & 0xFF
 
    # if the 'q' key is pressed, stop the loop
    if key == ord("q"):
	    break
 
#close any open windows
cv2.destroyAllWindows()
          
