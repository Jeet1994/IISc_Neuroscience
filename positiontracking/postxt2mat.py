import scipy.io as sio
import os 
import cv2

VIDEO_FILE_NAME = '******.h264'
cap = cv2.VideoCapture(VIDEO_FILE_NAME)
width = cap.get(3)
height = cap.get(4)

red_x = []
red_y = []
green_x = []
green_y = []

for filename in os.listdir(os.getcwd()):
    if filename.endswith("_Pos.txt"):
        f = open(filename)
        for line in f:
            line = line.rstrip("\n").split(" ")
            redx, redy, greenx, greeny = int(line[0]), int(line[1]), int(line[2]), int(line[3])
            #print redx, redy, greenx, greeny
            red_x.append(redx)
            red_y.append(redy)
            green_x.append(greenx)
            green_y.append(greeny)
            
        matFileName = filename.split('.txt')[0] + '.mat'
            
        sio.savemat(matFileName, mdict={'width': width, 'height' : height,'red_x': red_x, 'red_y': red_y, 'green_x':green_x, 'green_y': green_y})           