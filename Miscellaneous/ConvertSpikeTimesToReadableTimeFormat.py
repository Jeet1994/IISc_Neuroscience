# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 12:55:58 2016

@author: rajat
"""

import glob
import pickle
from datetime import timedelta, datetime

"""MAIN_START_RECORDING: stores the timestamps when Clock started for Neuralynx
Here is the example of time to pick:
-* NOTICE  *-  16:26:25.503 - 0 - RealTimeClock::InitRealTimeClock() - CPU clock frequency for timestamp calculations is 3
 So MAIN_START_RECORDING = 16:26:25:503"""
MAIN_NLX_CLOCK_START  = datetime.strptime('16:26:25.503','%H:%M:%S.%f').time()

#convert the main clock start time to timedelta object
MAIN_NLX_CLOCK_START = timedelta(hours=MAIN_NLX_CLOCK_START .hour, minutes=MAIN_NLX_CLOCK_START .minute, 
                                 seconds=MAIN_NLX_CLOCK_START .second, microseconds=MAIN_NLX_CLOCK_START .microsecond)

#input for directory
DIRECTORY = str(raw_input('Please enter the path to directory\n'))
print "Directory:- " + DIRECTORY + "\n"

# iterates over files starting with "cl-maze"
for name in glob.glob(DIRECTORY + "/cl-maze[0-9].[0-9].p"):
    #dictionary to hold the updated data
    spikeInfoUpdated = {}
    if "UpdatedTimestamps" not in name:
        #read the filename
        spikeDataFileName = str(name.split('\\')[1])
        print "Reading File:- " + spikeDataFileName
        #load the data from spike file
        spikeInfo = dict(pickle.load(open(spikeDataFileName, "rb")))
        
        #for each spike, update the timestamps to delta time object and add the clock start time
        for spikeId, spikeTimestamp in spikeInfo.items():
            spikeInfoUpdated[spikeId] = MAIN_NLX_CLOCK_START  + (timedelta(microseconds=spikeTimestamp))
        
        #add the clock start time to maze start time and maze end time
        spikeInfoUpdated['MazeStartTime'] = MAIN_NLX_CLOCK_START  + timedelta(microseconds=spikeInfo['MazeStartTime'])
        spikeInfoUpdated['MazeEndTime'] = MAIN_NLX_CLOCK_START  + timedelta(microseconds=spikeInfo['MazeEndTime']) 
        
        # save the updated spike data (timestamps as deltatimeobject) in a pickle file
        print "Maze Start Time: " + str(spikeInfoUpdated['MazeStartTime'])
        print "Maze End Time: " + str(spikeInfoUpdated['MazeEndTime'])
        spikeUpdatedDataPickleFileName = spikeDataFileName.split('.p')[0] + '.UpdatedTimestamps.p'
        print "Saving File:- " + spikeUpdatedDataPickleFileName
        pickle.dump( spikeInfoUpdated, open( spikeUpdatedDataPickleFileName, "wb" ) )
        print spikeUpdatedDataPickleFileName + " File saved\n"
    else:
        continue
    
print "Finished processing all the files"