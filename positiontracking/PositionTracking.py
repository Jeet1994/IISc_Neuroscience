# import the necessary packages
import argparse
import cv2
import numpy as np
import scipy.io as sio
 
# initialize the list of Region of Ineterest points and boolean indicating
# whether selection of Region of Interest is being performed or not
roiPt = []
selectingROI = True
frame = None
 
#mouse callback function: allows you to draw a Region of Interest
# by draw a rectangle around an area.
def selectROI(event, x, y, flags, param):
    # grab references to the global variables
    global roiPt, selectingROI, frame
 
    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that selection is being
    # performed
    if event == cv2.EVENT_LBUTTONDOWN:
        roiPt = [(x, y)]
 
    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates and indicate that
        # the selection operation is finished
        roiPt.append((x, y))
 
        # draw a rectangle around the region of interest
        cv2.rectangle(frame, roiPt[0], roiPt[1], (255,255,255), 1)
        cv2.imshow("VideoFrame", frame)
 
        selectingROI = False
 
def redColorTracking(thresholdedImage, originalImage):
    # red LED position     
    redLEDPos = (-1,-1)
 
    #convert color from BGR to HSV
    hsvThresholdedImage = cv2.cvtColor(thresholdedImage, cv2.COLOR_BGR2HSV)
   
    #define lower and upper limit of hue range for red color
    lowerRedHueRange = cv2.inRange(hsvThresholdedImage, np.array([0, 100, 100]), np.array([10, 255, 255]))
    upperRedHueRange = cv2.inRange(hsvThresholdedImage, np.array([160, 100, 100]), np.array([179, 255, 255]))
 
    #Calculates the weighted sum of two arrays.
    redHueThresholdedImage = cv2.addWeighted(lowerRedHueRange, 1.0, upperRedHueRange, 1.0, 0.0)
   
    #Blurs an image using a Gaussian filter
    redHueThresholdedImage = cv2.GaussianBlur(redHueThresholdedImage, (9, 9), 2, 2)
 
    #find contours in the red hue image formed after weighted adding of lower and upper ranges of red
    contours = cv2.findContours(redHueThresholdedImage.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
   
    # only proceed if at least one contour was found
    if len(contours) > 0:
        # find the largest contour in the mask, then use it to compute the minimum enclosing circle and centroid
        maxContour = max(contours, key=cv2.contourArea)
        M = cv2.moments(maxContour)
        redLEDPos = int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"])
 
    return redLEDPos
 
def greenColorTracking(thresholdedImage, originalImage):   
    #green LED positions       
    greenLEDPos = (-1,-1)
 
    # Convert BGR to HSV
    greenHSV = cv2.cvtColor(thresholdedImage, cv2.COLOR_BGR2HSV)
 
    #Hue Range for Green
    lowerGreenHue = np.array([50, 50, 120])
    upperGreenHue = np.array([70, 255, 255])
    greenMask = cv2.inRange(greenHSV, lowerGreenHue, upperGreenHue)
 
    #Blurs an image using a Gaussian filter
    greenHueThresholdedImage = cv2.GaussianBlur(greenMask, (9, 9), 2, 2)
 
    #find contours in the green hue image formed
    contours = cv2.findContours(greenHueThresholdedImage.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
   
    # only proceed if at least one contour was found
    if len(contours) > 0:
        # find the largest contour in the mask, then use it to compute the minimum enclosing circle and centroid
        maxContour = max(contours, key=cv2.contourArea)
        M = cv2.moments(maxContour)
        greenLEDPos = int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"])
 
    return greenLEDPos
 
 
#main loop
def main():
    global frame, roiPt
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--video", required=True, help="Path to the video file")
    args = vars(ap.parse_args())

    red_x = red_y = green_x = green_y = []
 
    # load the video,and setup the mouse callback function
    cap = cv2.VideoCapture(args["video"])
    if not cap.isOpened():
        print "Fatal Error: Could not open the specified file."
        exit(-1)
    cv2.namedWindow("VideoFrame")
    cv2.setMouseCallback("VideoFrame", selectROI)
     
    # keep looping until the 'q' key is pressed
    while True:
        #read the vide frame by frame
        ret, frame = cap.read()
        frameClone = frame.copy()
 
        #display the frame and wait for a keypress
        cv2.imshow("VideoFrame", frame)
        key = cv2.waitKey(1) & 0xFF
     
        # if the 'r' key is pressed, select the Region of Interest
        if key == ord("r") and selectingROI:
            cv2.imshow("VideoFrame", frame)
            cv2.waitKey(0)
     
        # if the 'q' key is pressed, break from the loop
        elif key == ord("q"):
            break
 
        # if the ROI has been selected, display the ROI along with main frame
        # and apply further image processing on ROI
        if len(roiPt) == 2:
            roi = frameClone[roiPt[0][1]:roiPt[1][1], roiPt[0][0]:roiPt[1][0]]
            #Median Blur: smoothening the images makes median of all the pixels under kernel area and central element= median value.
            roi = cv2.medianBlur(roi,5)
            #Intensity threholding the ROI
            thresholdedRoi = cv2.threshold(roi, 180, 255, cv2.THRESH_BINARY)[-1]
            #red and green LED position in ROI
            redLED = redColorTracking(thresholdedRoi, frame)
            greenLED = greenColorTracking(thresholdedRoi, frame)
            #draw a circle at red and green LED
            cv2.circle(thresholdedRoi, redLED, 2, (0, 0, 255), -1)
            cv2.circle(thresholdedRoi, greenLED, 2, (0, 255, 0), -1)

	    #if greenLED is tracked, make the transformation from ROI to Main Frame
	    if greenLED[0] != -1 and greenLED[1] != -1:
		greenLED = (greenLED[0]+roiPt[0][0], greenLED[1]+roiPt[0][1])
            if redLED[0] != -1 and redLED[1] != -1:
		redLED = (redLED[1]+roiPt[0][0], redLED[1]+roiPt[0][1])

            # show the ROI
            cv2.imshow("ROI", roi)
            cv2.imshow("Thresholded ROI", thresholdedRoi)
 
            # wait for a keypress
            key = cv2.waitKey(1) & 0xFF
            # if the 'q' key is pressed, break from the loop
            if key == ord("q"):
                break
 
        else:
            #Median Blur: smoothening the images makes median of all the pixels under kernel area and central element= median value.
            frame = cv2.medianBlur(frame,5)
            #Intensity threholding the Main Frame
            thresholdedFrame = cv2.threshold(frame, 160, 255, cv2.THRESH_BINARY)[-1]
            #red and green LED position in Main Video
            redLED = redColorTracking(thresholdedFrame, frame)
            greenLED = greenColorTracking(thresholdedFrame, frame)
            #draw a circle at red and green LED
            cv2.circle(thresholdedFrame, redLED, 2, (0, 0, 255), -1)
            cv2.circle(thresholdedFrame, greenLED, 2, (0, 255, 0), -1)
            cv2.imshow("Thresholded Frame", thresholdedFrame)
 
            # wait for a keypress
            key = cv2.waitKey(1) & 0xFF
            # if the 'q' key is pressed, break from the loop
            if key == ord("q"):
                break

	print redLED[0], redLED[1], greenLED[0], greenLED[1]

	red_x.append(redLED[0])
	red_y.append(redLED[1])
	green_x.append(greenLED[0])
	green_y.append(greenLED[1])
     
    # close all open windows
    cv2.destroyAllWindows()

    sio.savemat("Pos.mat", mdict={'red_x':red_x, 'red_y':red_y, 'green_x':green_x, 'green_y':green_y})
 
main()
