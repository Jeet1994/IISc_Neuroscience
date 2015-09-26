# -*- coding: utf-8 -*-
from  __future__ import unicode_literals

import io
import picamera
import time

with picamera.PiCamera() as camera:
	camera.resolution = (640,480)
	camera.framerate = 30
	#camera.vflip = True
	#camera.start_preview()
	camera.start_recording('basic_recording.h264')
	camera.wait_recording(120)
	camera.stop_recording()
