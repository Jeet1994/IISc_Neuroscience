# import the necessary packages
import argparse
import cv2
 
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

#main loop
def main():
	global frame, roiPt
	# construct the argument parser and parse the arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-v", "--video", required=True, help="Path to the video file")
	args = vars(ap.parse_args())
	 
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
		frame_clone = frame.copy()

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
			roi = frame_clone[roiPt[0][1]:roiPt[1][1], roiPt[0][0]:roiPt[1][0]]
			# show the ROI
			cv2.imshow("ROI", roi)
			
			# wait for a keypress
			key = cv2.waitKey(1) & 0xFF
			# if the 'q' key is pressed, break from the loop
			if key == ord("q"):
				break
	 
	# close all open windows
	cv2.destroyAllWindows()

main()
