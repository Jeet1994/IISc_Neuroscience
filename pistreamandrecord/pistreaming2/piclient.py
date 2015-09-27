#!/usr/bin/env python

import io
import picamera
import socket
import time

WIDTH  = 640
HEIGHT = 480
FRAMERATE = 30
EXPOSURE_MODE = 'night'
BRIGHTNESS = 55
CONTRAST = 5
SHARPNESS = -5
SATURATION = 25
AWB_MODE = 'auto'

# An output (as far as picamera is concerned), is just a filename or an object
class MyOutput(object):
    def __init__(self, filename, sock):
        self.output_file = io.open(filename, 'wb')
        self.output_sock = sock.makefile('wb')

    def write(self, buf):
        self.output_file.write(buf)
        self.output_sock.write(buf)

    def flush(self):
        self.output_file.flush()
        self.output_sock.flush()

    def close(self):
        #self.output_file.close()
        self.output_sock.close()

client_socket = socket.socket()
client_socket.connect(('10.120.10.217', 8000))

try:
    with picamera.PiCamera() as camera:
        camera.resolution = (WIDTH, HEIGHT)
        camera.framerate = FRAMERATE
	time.sleep(2) #warmup time
	camera.exposure_mode = EXPOSURE_MODE
	camera.awb_mode = AWB_MODE
	camera.brightness = BRIGHTNESS
	camera.contrast = CONTRAST
	camera.sharpness = SHARPNESS
	camera.saturation = SATURATION	

        # Construct an instance of our custom output splitter with a filename
	# and a connected socket
	my_output = MyOutput('output.h264', client_socket)
	# Record video to the custom output (we need to specify the format as
	# the custom output doesn't pretend to be a file with a filename)
	camera.start_recording(my_output, format='h264')
        camera.wait_recording(30)
        camera.stop_recording()
finally:
    my_output.close()
    client_socket.close()
