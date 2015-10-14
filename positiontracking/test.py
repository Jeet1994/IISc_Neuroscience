import cv2
import cv
import numpy as np

capture1 = cv2.VideoCapture("video1.h264")
capture2 = cv2.VideoCapture("video2.h264")

while True:
    ret1, frame1 = capture1.read()
    ret2, frame2 = capture2.read()

    h1, w1, d1 = capture1.get(cv.CV_CAP_PROP_FRAME_HEIGHT), capture1.get(cv.CV_CAP_PROP_FRAME_WIDTH), 3
    h2, w2, d2 = capture1.get(cv.CV_CAP_PROP_FRAME_HEIGHT), capture1.get(cv.CV_CAP_PROP_FRAME_WIDTH), 3

    vis = np.zeros((max(h1,h2), w1+w2, 3), np.uint8)
    if frame1 is None:
    	frame1 = np.zeros((h1,w1,d1), np.uint8)
    if frame2 is None:
    	frame2 = np.zeros((h2,w2,d2), np.uint8)
    
    vis[:h1, :w1, :d1] = frame1
    vis[:h2, w1:w1+w2, :d2] = frame2
    
    print capture1.get(cv.CV_CAP_PROP_POS_FRAMES), capture2.get(cv.CV_CAP_PROP_POS_FRAMES)
    cv2.imshow('Merged Frame', vis)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 

print capture1.get(cv.CV_CAP_PROP_FRAME_COUNT), capture2.get(cv.CV_CAP_PROP_FRAME_COUNT)
capture1.release()
capture2.release()
cv2.destroyAllWindows()