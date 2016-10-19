import cv2
import numpy as np
import time
from videostitchutils import load_timestamps, getStitchedImage

#width and height of output video
WIDTH = 640
HEIGHT = 480

# Define the codec and create VideoWriter object
fourcc = cv2.cv.CV_FOURCC(*'mp4v')  
output = cv2.VideoWriter('output.avi',fourcc, 30.0, (WIDTH,HEIGHT))

#define all camera video files
CAMERA_1_VIDEO_FILE = '221.h264'
CAMERA_2_VIDEO_FILE = '222.h264'
CAMERA_3_VIDEO_FILE = '223.h264'
CAMERA_4_VIDEO_FILE = '224.h264'
CAMERA_5_VIDEO_FILE = '225.h264'
CAMERA_6_VIDEO_FILE = '226.h264'
CAMERA_7_VIDEO_FILE = '227.h264'
CAMERA_8_VIDEO_FILE = '228.h264'

#camera capture objects to load the video files
print "Loading all video files...\n"
capture_CAM1 = cv2.VideoCapture(CAMERA_1_VIDEO_FILE)
capture_CAM2 = cv2.VideoCapture(CAMERA_2_VIDEO_FILE)
capture_CAM3 = cv2.VideoCapture(CAMERA_3_VIDEO_FILE)
capture_CAM4 = cv2.VideoCapture(CAMERA_4_VIDEO_FILE)
capture_CAM5 = cv2.VideoCapture(CAMERA_5_VIDEO_FILE)
capture_CAM6 = cv2.VideoCapture(CAMERA_6_VIDEO_FILE)
capture_CAM7 = cv2.VideoCapture(CAMERA_7_VIDEO_FILE)
capture_CAM8 = cv2.VideoCapture(CAMERA_8_VIDEO_FILE)

print "All video files loaded\n"

#go through each camera frame by frame
while True:
    #fetch the current frame for each camera
    ret, camera1_frame = capture_CAM1.read()
    ret, camera2_frame = capture_CAM2.read()
    ret, camera3_frame = capture_CAM3.read()
    ret, camera4_frame = capture_CAM4.read()
    ret, camera5_frame = capture_CAM5.read()
    ret, camera6_frame = capture_CAM6.read()
    ret, camera7_frame = capture_CAM7.read()
    ret, camera8_frame = capture_CAM8.read()  

    #if any of the frame is None i.e. the video has reached its end, stop the recording 
    if (camera1_frame is None) or (camera2_frame is None) or (camera3_frame is None) or (camera4_frame is None) or (camera5_frame is None) or (camera6_frame is None) or (camera7_frame is None) or (camera8_frame is None):
        print "end of video!"
        break
  
    #get the final stitched image from all cameras
    finalStitchedImage = getStitchedImage(camera1_frame, camera2_frame, camera3_frame, camera4_frame, camera5_frame, camera6_frame, camera7_frame, camera8_frame)  
    #write the fetched stitched image to the output object 
    output.write(finalStitchedImage)

#close everything after the work is done
capture_CAM1.release()
capture_CAM2.release()
capture_CAM3.release()
capture_CAM4.release()
capture_CAM5.release()
capture_CAM6.release()
capture_CAM7.release()
capture_CAM8.release()
output.release()
cv2.destroyAllWindows()
