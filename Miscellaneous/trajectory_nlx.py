# -*- coding: utf-8 -*-

"""
Created on Wed Apr 28 11:41:43 2016

@author: rajat
"""

"""
File contains data in this format:

--------------------------
|  Timestamp   (Double)  |
|------------------------|
|  X coord     (Single)  |
|------------------------|
|  Y coord     (Single)  |
|------------------------|
|  Direction   (Single)  |
--------------------------

"""

import matplotlib.pyplot as plt
import numpy as np
import cv2

blank_image = np.zeros((640,640,3), np.uint8)

positionDataFile = open('ap1.txt', 'rb')
positionData = []

#read the data in positionData list
for data in positionDataFile:
    info = data.split(',')
    x,y = int(info[0]), int(info[1])
    positionData.append((x,y))

#loop over the set of tracked pts
for index in xrange(1, len(positionData)):
    if index == len(positionData):
        cv2.imwrite('trajectory_nlx.jpg',blank_image)

    #if either of the tracked pts are (0,0), ignore them
    if positionData[index-1]==(0,0) or positionData[index]==(0,0):
        continue
    
  #otherwise, compute the thickness of the line and
	# draw the connecting lines
    print positionData[index - 1], positionData[index]
    cv2.line(blank_image, positionData[index - 1], positionData[index], (0, 0, 255), 1)
 
    # show the frame to our screen
    cv2.imshow("Frame", blank_image)

    key = cv2.waitKey(1) & 0xFF
 
    # if the 'q' key is pressed, stop the loop
    if key == ord("q"):
	    break
 
#close any open windows
cv2.destroyAllWindows()
          
