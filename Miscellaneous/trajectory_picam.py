import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
import scipy.io as sio

blank_image = np.zeros((720,720,3), np.uint8)

for filename in os.listdir(os.getcwd()):
    if filename.endswith(".mat"):
	imageFileName = filename.split("_Pos.mat")[0] + "_trajectory.jpg"
        data = sio.loadmat(filename)
        red_x = list(data['red_x'][0])
        red_y = list(data['red_y'][0])
        green_x = list(data['green_x'][0])
        green_y = list(data['green_y'][0])
	positionData = []

	x1 = red_x
	y1 = red_y
	for x,y in zip(x1,y1):
    	    positionData.append((x,y))

	#loop over the set of tracked pts
	for index in xrange(1, len(positionData)):
	    if index == len(positionData)-1:
		cv2.imwrite(imageFileName,blank_image)

	    #if either of the tracked pts are (0,0), ignore them
	    if positionData[index-1]==(-1,-1) or positionData[index]==(-1,-1):
		continue
	    
	    #otherwise, compute the thickness of the line and draw the connecting lines
	    cv2.line(blank_image, positionData[index - 1], positionData[index], (0, 0, 255), 1)
	 
	    # show the frame to our screen
	    cv2.imshow("Frame", blank_image)

	    key = cv2.waitKey(1) & 0xFF
	 
	    # if the 'q' key is pressed, stop the loop
	    if key == ord("q"):
		    break
	 
	#close any open windows
	cv2.destroyAllWindows()
          
