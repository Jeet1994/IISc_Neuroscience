import numpy as np
import cv2
import copy
from collections import deque
import csv

filename = 'Day13_CircularTrack_cam2_output_2016-08-10 15_36_08 064928.h264'
cap = cv2.VideoCapture(filename)

while(cap.isOpened()):
    #read the video frame by frame
    ret, frame = cap.read()
    if frame is None:
	break
    
    #copy of frame read just now 
    orig_image = frame.copy()
    
    #Median Blur: smoothening the images
    #makes median of all the pixels under kernel area and central element is replaced with this median value. 
    #highly effective against salt-and-pepper noise in the images.
    frame = cv2.medianBlur(frame,5)

    #convert color from BGR to HSV
    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #define lower and upper limit of hue range for red color
    lower_red_hue_range = cv2.inRange(hsv_image, np.array([0, 100, 100]), np.array([10, 255, 255]))
    upper_red_hue_range = cv2.inRange(hsv_image, np.array([160, 100, 100]), np.array([179, 255, 255]))

    #Calculates the weighted sum of two arrays.
    red_hue_image = cv2.addWeighted(lower_red_hue_range, 1.0, upper_red_hue_range, 2.0, 0.0)
    
    #Blurs an image using a Gaussian filter
    #The function convolves the source image with the specified Gaussian kernel
    red_hue_image = cv2.GaussianBlur(red_hue_image, (9, 9), 2, 2)

    #find contours in the red_hue_image formed after weighted adding of lower and upper ranges of red
    cnts = cv2.findContours(red_hue_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = (None, None)

    # only proceed if at least one contour was found
    if len(cnts) > 0:
	# find the largest contour in the mask, then use
	# it to compute the minimum enclosing circle and
	# centroid
	c = max(cnts, key=cv2.contourArea)
	((x, y), radius) = cv2.minEnclosingCircle(c)
	M = cv2.moments(c)
	center = int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"])
 
	# only proceed if the radius meets a minimum size
	if radius > 2:
	    # draw the circle and centroid on the frame,
	    # then update the list of tracked points
	    #cv2.circle(orig_image, (int(x), int(y)), int(radius),(0, 255, 255), 1)
	    cv2.circle(orig_image, center, 2, (0, 0, 255), -1)
    
    x,y = center[0], center[1] 
    if x==None and y==None:
	x, y = 0, 0
    currentFrameNum = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
    print currentFrameNum,x,y

    #cv2.imshow("Threshold lower image", lower_red_hue_range)
    #cv2.imshow("Threshold upper image", upper_red_hue_range)	
    #cv2.imshow("Combined threshold images", red_hue_image)
    cv2.imshow("LED positions", orig_image)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
