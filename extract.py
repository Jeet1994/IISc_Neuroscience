import cv2
import cv2.cv as cv

vidcap = cv2.VideoCapture('cam7.h264')
success,image = vidcap.read()

if success:
	cv2.imwrite('cam711.jpg', image)
	#cv2.imshow('cam1', image)
	cv2.waitKey()
