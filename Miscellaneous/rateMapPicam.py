# -*- coding: utf-8 -*-
"""
Created on Wed Oct 05 18:35:14 2016

@author: rajat
"""
import numpy as np
from datetime import timedelta, datetime
import lynxio
import os
import scipy.io as sio
import pickle
import rateMapUtils
   
CHEETAH_LOG_FILE_NAME = 'CheetahLogFile.txt'
NLX_START_TIME = rateMapUtils.getNeuralynxStartTime(CHEETAH_LOG_FILE_NAME)   #is in the form of HH:MM:SS.Microseconds
#Events File Name
EVENTS_FILE_NAME = 'Events.nev'   
#picamera position data filename 
PICAMERA_POSITION_FILE_NAME = 'Day7_Pos.mat'
PICAMERA_DISTANCE_FILE_NAME = 'Day7_distance.mat'
#winclust spike data filename 
SPIKE_FILE_NAME = 'TT16-cl-maze1.2.UpdatedTimestamps.p'
#raw rate map, spike map and occupancy map data
RAW_MAP_FILE_NAME = 'rawMaps_' + SPIKE_FILE_NAME.split('.p')[0] + '.mat'
RAW_MAP_K5_FILE_NAME = 'rawMaps_k5_' + SPIKE_FILE_NAME.split('.p')[0] + '.mat'
#dictionary to hold events info from events.nev file
events = {}
#list which hold picamera Date time from the raw text file
piCameraTime = []
# start maze time and end maze time (will be noted from events file)
StartMazeTime= -1
EndMazeTime = -1

#Neuralynx clock start time
MAIN_NLX_CLOCK_START = datetime.strptime(NLX_START_TIME,'%H:%M:%S.%f').time()
#convert the main clock start time to timedelta object
MAIN_NLX_CLOCK_START = timedelta(hours=MAIN_NLX_CLOCK_START.hour, minutes=MAIN_NLX_CLOCK_START.minute, 
                                 seconds=MAIN_NLX_CLOCK_START.second, microseconds=MAIN_NLX_CLOCK_START.microsecond)
print "Recording Start Time: %s \n" % (MAIN_NLX_CLOCK_START)

#load event timestamps, event names and Id from events.nev file
eventTimestamps, eventId, nttl, eventNames = lynxio.loadNev(EVENTS_FILE_NAME)

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
piCameraStartMazeIndex, piCameraStartMazeTime = rateMapUtils.nearestDate(piCameraTime, StartMazeTime)
piCameraEndMazeIndex, piCameraEndMazeTime = rateMapUtils.nearestDate(piCameraTime, EndMazeTime)

#find the index and nearest value from the picamera time list to the start_time and end_time calculated above from nev file
piCameraStartMazeIndex, piCameraStartMazeTime = rateMapUtils.nearestDate(piCameraTime, StartMazeTime)
piCameraEndMazeIndex, piCameraEndMazeTime = rateMapUtils.nearestDate(piCameraTime, EndMazeTime)

print "Picamera Start Maze Index: %s and corresponding Time: %s" % (piCameraStartMazeIndex, piCameraStartMazeTime)
print "Picamera End Maze Index: %s and corresponding Time: %s" % (piCameraEndMazeIndex, piCameraEndMazeTime)
      
#load the picamera position data
piCameraData = sio.loadmat(PICAMERA_POSITION_FILE_NAME)
red_x = piCameraData['red_x'][0]
red_y = piCameraData['red_y'][0]

#dicitonary to hold xpos, ypos, timestamp, width, height
Pos = {}
Pos['red_x'] = red_x[piCameraStartMazeIndex:piCameraEndMazeIndex]
Pos['red_y'] = red_y[piCameraStartMazeIndex:piCameraEndMazeIndex]
Pos['pos_t'] = np.array(piCameraTime[piCameraStartMazeIndex:piCameraEndMazeIndex])
Pos['width'] = piCameraData['width'][0]
Pos['height'] = piCameraData['height'][0]

distance = sio.loadmat(PICAMERA_DISTANCE_FILE_NAME)
distance = distance['distance'][0][piCameraStartMazeIndex:piCameraEndMazeIndex]
Pos['red_x'] = Pos['red_x'][distance>0.35]
Pos['red_y'] = Pos['red_y'][distance>0.35]
Pos['pos_t'] = Pos['pos_t'][distance>0.35]
print "\nPosition Data loaded"

# load the spikedata 
SpikeData = pickle.load(open(SPIKE_FILE_NAME))
print "\nSpike Data loaded"

#get the raw rateMap, spikeMap and occupancy map
rateMap, spikeMap, occMap = rateMapUtils.generateRateMap(Pos,SpikeData,k=1)
rateMap_k5, spikeMap_k5, occMap_k5 = rateMapUtils.generateRateMap(Pos,SpikeData,k=5)

#save the raw maps in .npy format
sio.savemat(RAW_MAP_FILE_NAME, mdict={'rateMap':rateMap, 'spikeMap': spikeMap, 'occMap': occMap})
sio.savemat(RAW_MAP_K5_FILE_NAME, mdict={'rateMap':rateMap_k5, 'spikeMap': spikeMap_k5, 'occMap': occMap_k5})