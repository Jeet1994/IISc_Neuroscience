import cv2
import cv
import numpy as np

capture1 = cv2.VideoCapture("video1.h264")
capture2 = cv2.VideoCapture("video2.h264")

while True:
    ret1, frame1 = capture1.read()
    ret2, frame2 = capture2.read()

    merged_frame = cv2.bitwise_and(frame1, frame2)
    
    print capture1.get(cv.CV_CAP_PROP_POS_FRAMES), capture2.get(cv.CV_CAP_PROP_POS_FRAMES)
    cv2.imshow('Merged Frame', merged_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 

print capture1.get(cv.CV_CAP_PROP_FRAME_COUNT), capture2.get(cv.CV_CAP_PROP_FRAME_COUNT)
capture1.release()
capture2.release()
cv2.destroyAllWindows()