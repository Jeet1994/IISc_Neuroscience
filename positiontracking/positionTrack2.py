# USAGE : python motion_detector.py

# import the necessary packages
import numpy as np
import cv2

"""
Function to find the contour closest to the previous position of animals, 
helps in faster processing of animal position
"""
def minimumDistanceContour(contours, center):
    distances = []
    for i in range(0,len(contours)):
	distance = cv2.pointPolygonTest(contours[i], center, True)
    	distances.append(np.fabs(distance))
    index = distances.index(min(distances))
    return index

"""
Function to track red color on the basis of hue value, 
does a weighted summation of lower red hue range and 
upper red hue range.
"""	
def hueBasedTracking(frame):
    #useful for smoothening the images, median of all the pixels under kernel 
    #area and central element is replaced with this median value. 
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
    center = None

    # only proceed if at least one contour was found
    if len(cnts) > 0:
	    # find the largest contour in the mask, then use it to compute the minimum enclosing circle and centroid
	    c = max(cnts, key=cv2.contourArea)
	    ((x, y), radius) = cv2.minEnclosingCircle(c)
	    M = cv2.moments(c)
	    #gives x and y coordinates of center
	    center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
    return center #returns the centroid for th image

"""
Function to perform background subtraction 
"""
def backGroundSubtraction(animalPosition, contours, frame):
	#if no contours found, object is stable hence run hue based tracking 
	if len(contours)==0:
		animalPosition = hueBasedTracking(frame)
	#if contour is found, then fing the index of closest contour 
	else:
		indexMinDistanceContour = minimumDistanceContour(contours, center)
		for i in range(0,len(contours)):
			distance = cv2.pointPolygonTest(contours[i], center, True) #find distance of all contours from animal position
			#if animalposition is inside contour, then print center
			if distance >= 0:
				animalPosition = center
			#else find the closest contour center to previous animal position
			else:	
				M = cv2.moments(contours[indexMinDistanceContour])
				animalPosition = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
	return animalPosition


camera = cv2.VideoCapture('motion.h264')

animalPositionFile = open('animalPositionTrack.txt','w')

# initialize the first frame in the video stream
firstFrame = None
animalPosition = None

# loop over the frames of the video
while True:
	# grab the current frame
	(grabbed, frame) = camera.read()
	
	# if the frame could not be grabbed, then we have reached the end of the video
	if not grabbed:
		break

	# resize the frame, convert it to grayscale, and blur it
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (21, 21), 0)

	# if the first frame is None, initialize it
	if firstFrame is None:
		firstFrame = gray
		continue

	# compute the absolute difference between the current frame and first frame
	frameDelta = cv2.absdiff(firstFrame, gray)


	thresh = cv2.adaptiveThreshold(frameDelta, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
	#thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[-1]

	# dilate the thresholded image to fill in holes, then find contours on thresholded image
	thresh = cv2.dilate(thresh, None, iterations=2)

	#find contours 
	(contours, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	
	position = None

	center = hueBasedTracking(frame)

	if animalPosition is None:
		animalPosition = center

	#if no movement or the animal is stable, no contours will be found
	#then in that case use the hue based tracking code 
	animalPosition = backGroundSubtraction(animalPosition, contours, frame)
				
	animalPositionFile.write( camera.get(1), animalPosition )
	
	cv2.circle(frame, animalPosition, 5, (255,0,0), 2)
	cv2.imshow('Tracking', frame)

	# if the `q` key is pressed, break from the lop
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break

# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()

animalPositionFile.close()
