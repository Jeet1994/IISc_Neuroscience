import cv2
import numpy as np
import time
from videostitchutils import load_timestamps, getStitchedImage
from datetime import datetime, timedelta

#width and height of output video
WIDTH = 640
HEIGHT = 480

# Define the codec and create VideoWriter object
fourcc = cv2.cv.CV_FOURCC(*'mp4v')  
output = cv2.VideoWriter('output.avi',fourcc, 30.0, (WIDTH,HEIGHT))

#define each camera index for ease of coding
CAMERA_1 = 0
CAMERA_2 = 1
CAMERA_3 = 2
CAMERA_4 = 3
CAMERA_5 = 4
CAMERA_6 = 5
CAMERA_7 = 6
CAMERA_8 = 7

#video files from each camera
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

#list of all cpture objects
captures = [capture_CAM1, capture_CAM2, capture_CAM3, capture_CAM4, capture_CAM5, capture_CAM6, capture_CAM7, capture_CAM8]

#timestamps sile for each camera
CAMERA_1_TIMESTAMP_FILE = 'timestamp_cam1.txt'
CAMERA_2_TIMESTAMP_FILE = 'timestamp_cam2.txt'
CAMERA_3_TIMESTAMP_FILE = 'timestamp_cam3.txt'
CAMERA_4_TIMESTAMP_FILE = 'timestamp_cam4.txt'
CAMERA_5_TIMESTAMP_FILE = 'timestamp_cam5.txt'
CAMERA_6_TIMESTAMP_FILE = 'timestamp_cam6.txt'
CAMERA_7_TIMESTAMP_FILE = 'timestamp_cam7.txt'
CAMERA_8_TIMESTAMP_FILE = 'timestamp_cam8.txt'

#list of all camera timestamps, load_timestamps loads timestamps for each camera 
timestamps = [load_timestamps(CAMERA_1_TIMESTAMP_FILE), load_timestamps(CAMERA_2_TIMESTAMP_FILE), load_timestamps(CAMERA_1_TIMESTAMP_FILE), load_timestamps(CAMERA_2_TIMESTAMP_FILE), load_timestamps(CAMERA_1_TIMESTAMP_FILE),  load_timestamps(CAMERA_2_TIMESTAMP_FILE), load_timestamps(CAMERA_1_TIMESTAMP_FILE), load_timestamps(CAMERA_2_TIMESTAMP_FILE)]

#set the start time to None
start_time = None

#starting frame index is 0
frame_index = [0, 0, 0, 0,]
#flag to check if video is finished or not
video_done = [False, False, False, False, False, False, False, False]

# Make those default blank images the size of your video...
# Adjust number of channels if you're using grayscale
image =  [np.zeros((640,480,3),np.uint8)] * 8

while True:
    #fetch the current time
    real_time = datetime.now()
    if start_time is None: # First iteration only
        start_time = real_time
    #get current timestamps after subtracting start time from current time
    current_ts = real_time - start_time

    # Advance both cameras up to current_ts
    for i in [CAMERA_1, CAMERA_2]:
        while True:
            # Get timestamp of the frame at current position
            current_index = frame_index[i]
            #check if the current index is greater than the number of frames for particular camera video 
            if current_index >= len(timestamps[i]):
                video_done[i] = True
                break # End of the video
            #set vidoe timestamp equal to camera fetched time
            video_ts = timestamps[i][current_index]
            if current_ts < video_ts:
                break # The frame is in future, stop
            # The frame is in the past or present
            print(" camera %d: frame %d" % (i+1, frame_index[i]))
            image[i] = image[i]
	    frame_index[i] += 1

    #get the final stitched image from all cameras
    finalStitchedImage = getStitchedImage(image[0],image[1],image[2],image[3],image[4],image[5],image[6],image[7])  
    #write the fetched stitched image to the output object 
    output.write(finalStitchedImage)
    
    if video_done[CAMERA_1] or video_done[CAMERA_2] or video_done[CAMERA_3] or video_done[CAMERA_4] or video_done[CAMERA_5] or video_done[CAMERA_6] or video_done[CAMERA_7] or video_done[CAMERA_8]:
        break

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