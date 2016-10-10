# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 12:55:58 2016

@author: rajat
"""

import glob
import pickle
from datetime import timedelta, datetime
import rateMapUtils

#read the cheetah clock start time 
CHEETAH_LOG_FILE_NAME = 'CheetahLogFile.txt'
MAIN_NLX_CLOCK_START = rateMapUtils.getNeuralynxStartTime(CHEETAH_LOG_FILE_NAME)
MAIN_NLX_CLOCK_START = datetime.strptime(MAIN_NLX_CLOCK_START,'%H:%M:%S.%f').time()

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
    spikeTime = []
    if "UpdatedTimestamps" not in name:
        #read the filename
        spikeDataFileName = str(name.split('\\')[1])
        print "Reading File:- " + spikeDataFileName
        
        #load the data from spike file
        data, MazeStartTime, MazeEndTime = pickle.load(open(spikeDataFileName, "rb"))
        spikeInfo = dict(data)
        
        #for each spike, update the timestamps to delta time object and add the clock start time
        for spikeId, spikeTimestamp in spikeInfo.items():
            spikeTime.append(MAIN_NLX_CLOCK_START  + (timedelta(microseconds=spikeTimestamp)))
        
        #add the clock start time to maze start time and maze end time
        spikeInfoUpdated['MazeStartTime'] = MAIN_NLX_CLOCK_START  + timedelta(microseconds=MazeStartTime)
        spikeInfoUpdated['MazeEndTime'] = MAIN_NLX_CLOCK_START  + timedelta(microseconds=MazeEndTime) 
        spikeInfoUpdated['SpikeTime'] = spikeTime
        
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