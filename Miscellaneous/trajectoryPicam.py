import numpy as np
from datetime import timedelta, datetime
import lynxio
import os
import scipy.io as sio
import cv2
import rateMapUtils

#function to find the nearest value to a list
def nearestDate(dates, pivot):
    minimum = min(dates, key=lambda x: abs(x - pivot))
    minimum_index = dates.index(minimum)
    return minimum_index, minimum
    
#read the cheetah clock start time 
CHEETAH_LOG_FILE_NAME = 'CheetahLogFile.txt'
MAIN_NLX_CLOCK_START = rateMapUtils.getNeuralynxStartTime(CHEETAH_LOG_FILE_NAME)   #is in the form of HH:MM:SS.Microseconds
#Events File Name
Events_File_Name = 'Events.nev'   
#dictionary to hold events info from events.nev file
events = {}
#list which hold picamera Date time from the raw text file
piCameraTime = []
# start maze time and end maze time (will be noted from events file)
StartMazeTime= -1
EndMazeTime = -1
#blank black image to draw trajcectory
blank_image = np.zeros((720,720,3), np.uint8)

#convert the main clock start time to timedelta object
MAIN_NLX_CLOCK_START = datetime.strptime(MAIN_NLX_CLOCK_START,'%H:%M:%S.%f').time()
MAIN_NLX_CLOCK_START = timedelta(hours=MAIN_NLX_CLOCK_START.hour, minutes=MAIN_NLX_CLOCK_START.minute, 
                                 seconds=MAIN_NLX_CLOCK_START.second, microseconds=MAIN_NLX_CLOCK_START.microsecond)
print "Recording Start Time: %s \n" % (MAIN_NLX_CLOCK_START)

#load event timestamps, event names and Id from events.nev file
eventTimestamps, eventId, nttl, eventNames = lynxio.loadNev(Events_File_Name)

#save the events info in the dictionary initialized above with events timestamps as key and [name, timestamp timedelta object] as items
for ts, eventName in zip(eventTimestamps, eventNames):
    events[ts] = [eventName, timedelta(microseconds=int(ts))+ MAIN_NLX_CLOCK_START]

#print each event stored in the .nev events file
print "Events logged are: "
for key in sorted(events.keys()):
    print key, events[key]

#assign the start and end maze time variable from the events dictionary, used to find index for picamera date time from raw txt file stored    
StartMazeTime = events[np.uint64(raw_input("please enter the eventID for start Maze \n"))][1]
EndMazeTime = events[np.uint64(raw_input("please enter the eventID for End Maze \n"))][1]
 
print "\nStart Maze Time: %s"  % (StartMazeTime)   
print "End Maze Time: %s \n"  % (EndMazeTime)

#load the picamera date time from raw txt file and store it in a list
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".txt") and "timestamp" in filename:
        with open(filename) as f:  
            StartTime = f.readline().rstrip('\n').split(',')[1].split(' ')[1]
            StartTime = datetime.strptime(StartTime,'%H:%M:%S.%f').time()
            StartTime = timedelta(hours=StartTime.hour, minutes=StartTime.minute, 
                                 seconds=StartTime.second, microseconds=StartTime.microsecond)                  
            for line in f:
                timestamp = eval(line.rstrip('\n').split(',')[0])
                timestamp = timedelta(microseconds=(float(timestamp)*1000)) + StartTime
                piCameraTime.append(timestamp)

#find the index and nearest value from the picamera time list to the start_time and end_time calculated above from nev file
piCameraStartMazeIndex, piCameraStartMazeTime = nearestDate(piCameraTime, StartMazeTime)
piCameraEndMazeIndex, piCameraEndMazeTime = nearestDate(piCameraTime, EndMazeTime)

print "Picamera Start Maze Index: %s and corr. Time: %s" % (piCameraStartMazeIndex, piCameraStartMazeTime)
print "Picamera End Maze Index: %s and corr. Time: %s" % (piCameraEndMazeIndex, piCameraEndMazeTime)
        
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".mat"):
        imageFileName = filename.split("_Pos.mat")[0] + "_trajectory.jpg"
        data = sio.loadmat(filename)
        red_x = list(data['red_x'][0])[piCameraStartMazeIndex:piCameraEndMazeIndex]
        red_y = list(data['red_y'][0])[piCameraStartMazeIndex:piCameraEndMazeIndex]
        green_x = list(data['green_x'][0])[piCameraStartMazeIndex:piCameraEndMazeIndex]
        green_y = list(data['green_y'][0])[piCameraStartMazeIndex:piCameraEndMazeIndex]
        positionData = []
        
        x1 = red_x
        y1 = red_y
        for x,y in zip(x1,y1):
            positionData.append((x,y))
            
        #loop over the set of tracked pts
        for index in xrange(1, len(positionData)):
            if index == len(positionData)-1:
                cv2.imwrite(imageFileName,blank_image)
            
            #if either of the tracked pts are (0,0), ignore them
            if positionData[index-1]==(-1,-1) or positionData[index]==(-1,-1):
                continue
                
            #otherwise, compute the thickness of the line and draw the connecting lines
            cv2.line(blank_image, positionData[index - 1], positionData[index], (0, 0, 255), 1)
            # show the frame to our screen
            cv2.imshow("Frame", blank_image)
            key = cv2.waitKey(1) & 0xFF
            # if the 'q' key is pressed, stop the loop
            if key == ord("q"):
		    break
        cv2.imwrite(imageFileName,blank_image); cv2.destroyAllWindows()