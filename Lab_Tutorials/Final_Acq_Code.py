#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import io
import picamera
import socket
import time
import datetime as dt
import sys, getopt
from fractions import Fraction

WIDTH  = 640
HEIGHT = 480
FRAMERATE = 30
VIDEO_STABILIZATION = True
EXPOSURE_MODE = 'night'
BRIGHTNESS = 60
CONTRAST = 30
SHARPNESS = 30
AWB_MODE = 'off'
AWB_GAINS = 1.4

VIDEO_FILE_NAME = "cam1_output_" + str(dt.datetime.now()) + ".h264"
TIMESTAMP_FILE_NAME = "cam1_timestamp_" + str(dt.datetime.now()) + ".txt"
runningTimeHours, runningTimeMinutes, runningTimeSeconds = 0,0,0

# An output (as far as picamera is concerned), is just a filename or an object
# which implements a write() method (and optionally the flush() and close()
# methods)
class MyOutput(object):
    def __init__(self, camera, video_filename, pts_filename):
        self.camera = camera
        self.videoOutputFile = io.open(video_filename, 'wb')
        self.timestampOutputFile = io.open(pts_filename, 'w')
        self.start_time = None

    def write(self, buf):
        self.videoOutputFile.write(buf)
        if self.camera.frame.complete and self.camera.frame.timestamp:
            if self.start_time is None:
                self.start_time = self.camera.frame.timestamp
            self.timestampOutputFile.write(u'%f, %s\n' % (((self.camera.frame.timestamp-self.start_time)/1000.0), dt.datetime.now().strftime("%H:%M:%S.%f")))
	    #print self.camera.awb_gains, self.camera.digital_gain, self.camera.analog_gain, self.camera.brightness, self.camera.contrast, self.camera.saturation , camera.exposure_speed 
    
    def flush(self):
        self.videoOutputFile.flush()
        self.timestampOutputFile.flush()

    def close(self):
        self.videoOutputFile.close()
        self.timestampOutputFile.close()

try:
    opts, args = getopt.getopt(sys.argv[1:], 'r:m:s:h', ['help',"hour=", "min=", "sec="])
except getopt.GetoptError, err: 
    print err
    sys.exit(2)

for opt, arg in opts:
    if opt in ('-h', '--help'): 
        print "Acquire_code.py -hr <hours> -m <mins> -s <secs>"
    elif opt in ('-r','--hour'):
        runningTimeHours = arg
    elif opt in ('-m','--min'):
        runningTimeMinutes = arg
    elif opt in ('-s','--sec'):
        runningTimeSeconds = arg

runningTimeHours = float(runningTimeHours)
runningTimeMinutes = float(runningTimeMinutes)
runningTimeSeconds = float(runningTimeSeconds)

totalRunningTime = runningTimeHours*60*60 + runningTimeMinutes*60 + runningTimeSeconds

#print totalRunningTime

try:
    with picamera.PiCamera() as camera:
        camera.resolution = (WIDTH, HEIGHT)
        camera.framerate = FRAMERATE
        camera.brightness = BRIGHTNESS
        camera.contrast = CONTRAST
        camera.sharpness = SHARPNESS
	camera.video_stabilization = VIDEO_STABILIZATION			

        #warm-up time to camera to set its initial settings
        time.sleep(2)
    	
        camera.exposure_mode = EXPOSURE_MODE
        camera.awb_mode = AWB_MODE
        camera.awb_gains = AWB_GAINS

        #time to let camera change parameters according to exposure and AWB
        time.sleep(2)
    	
        camera.exposure_mode = 'off'
	camera.hflip = False
	camera.vflip = False	
	
	camera.start_preview()
        # Construct an instance of our custom output splitter with a filename  and a connected socket
        print 'Starting Re1cording'
        # Record video to the custom output (we need to specify the format as
        # the custom output doesn't pretend to be a file with a filename)
        camera.start_recording(MyOutput(camera, VIDEO_FILE_NAME, TIMESTAMP_FILE_NAME), format='h264')
        print 'Started Recording'
        camera.wait_recording(totalRunningTime)
        camera.stop_recording()
	camera.stop_preview()
        print 'Recording Stopped'
        print 'Output File Closed'
except KeyboardInterrupt:
	print 'Closing Output File'
	sys.exit(2)
