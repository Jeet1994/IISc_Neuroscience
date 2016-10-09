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
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from scipy import ndimage as nd
import matplotlib.cm as cm

cdict = cm.get_cmap('jet')._segmentdata
red = ((0.0,0,0), (0.0, 0, 0), (0.35, 0, 0), (0.66, 1, 1), (0.89, 1, 1), (1, 0.5, 0.5))
blue = ((0.0,0,0), (0.0, 0.5, 0.5), (0.11, 1, 1), (0.34, 1, 1), (0.65, 0, 0), (1, 0, 0))
green = ((0.0, 0, 0), (0.125, 0, 0), (0.375, 1, 1), (0.64, 1, 1), (0.91, 0, 0), (1, 0, 0))
cdict['red'] = red
cdict['green'] = green
cdict['blue'] = blue
cmap = LinearSegmentedColormap('name', cdict)


#function to find the nearest value to a list
def nearestDate(dates, pivot):
    minimum = min(dates, key=lambda x: abs(x - pivot))
    minimum_index = dates.index(minimum)
    return minimum_index, minimum

def find_id(dates, pivot):
    minimum = min(dates, key=lambda x: abs(x - pivot))
    min_idx = dates.index(minimum)
    return min_idx
    
def rate_map(pos,spk,k=2):
    posx = pos["red_x"]
    posy = pos["red_y"]

    for idx, item in enumerate(posx):
        if item == -1:
            posx[idx] = 0
            
    for idx, item in enumerate(posy):
        if item == -1:
            posy[idx] = 0

    posSpikeX = []
    posSpikeY = []
    
    try:
        indx = [find_id(pos["pos_t"],t) for t in spk["SpikeTime"]]
        indy = [find_id(pos["pos_t"],t) for t in spk["SpikeTime"]]
        
        for x in indx:
            posSpikeX.append(posx[x])
        
        for y in indy:
            posSpikeY.append(posy[y])
    
        xbin_edges = np.arange(0,1280,5)
        ybin_edges = np.arange(0,960,5)
        im_s = np.histogram2d(posSpikeX, posSpikeY,  bins=(xbin_edges,ybin_edges))[0]
        im_all = np.histogram2d(posx, posy,  bins=(xbin_edges,ybin_edges))[0]
        im_s[0][0] = 0.0
        im_all[0][0] = 0.0
        im = im_s/im_all
        im = np.nan_to_num(im)
    except ValueError or TypeError:
        pass

    return im, im_s, im_all
   
"""MAIN_START_RECORDING: stores the timestamps when Clock started for Neuralynx
Here is the example of time to pick:
-* NOTICE  *-  16:26:25.503 - 0 - RealTimeClock::InitRealTimeClock() - CPU clock frequency for timestamp calculations is 3
 So MAIN_START_RECORDING = 16:26:25:503"""
Neuralynx_Start_Time = '11:40:59.337'   #is in the form of HH:MM:SS.Microseconds
#Events File Name
Events_File_Name = 'Events.nev'   
#dictionary to hold events info from events.nev file
events = {}
#list which hold picamera Date time from the raw text file
piCameraTime = []
# start maze time and end maze time (will be noted from events file)
StartMazeTime= -1
EndMazeTime = -1

#Neuralynx clock start time
MAIN_NLX_CLOCK_START = datetime.strptime(Neuralynx_Start_Time,'%H:%M:%S.%f').time()
#convert the main clock start time to timedelta object
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

#find the index and nearest value from the picamera time list to the start_time and end_time calculated above from nev file
piCameraStartMazeIndex, piCameraStartMazeTime = nearestDate(piCameraTime, StartMazeTime)
piCameraEndMazeIndex, piCameraEndMazeTime = nearestDate(piCameraTime, EndMazeTime)

print "Picamera Start Maze Index: %s and corresponding Time: %s" % (piCameraStartMazeIndex, piCameraStartMazeTime)
print "Picamera End Maze Index: %s and corresponding Time: %s" % (piCameraEndMazeIndex, piCameraEndMazeTime)
      
data = sio.loadmat('Day16_Pos.mat')
red_x = list(data['red_x'][0])
red_y = list(data['red_y'][0])
Pos = {}
Pos['red_x'] = red_x[piCameraStartMazeIndex:piCameraEndMazeIndex]
Pos['red_y'] = red_y[piCameraStartMazeIndex:piCameraEndMazeIndex]
Pos['pos_t'] = piCameraTime[piCameraStartMazeIndex:piCameraEndMazeIndex]
print "\nPosition Data loaded"

spikeFileName = 'cl-maze1.2.UpdatedTimestamps.p'
SpikeData = pickle.load(open(spikeFileName))
print "\nSpike Data loaded"

rateMap, spikeMap, occMap = rate_map(Pos,SpikeData)

plt.imshow(rateMap, cmap=cmap)
plt.colorbar()
rateMapImageFile = 'rateMap_raw_' + spikeFileName
pickle.dump([rateMap, spikeMap, occMap], open( rateMapImageFile, "wb" ) )