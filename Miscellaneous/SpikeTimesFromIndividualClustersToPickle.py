# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 12:55:58 2016

@author: rajat
"""

import glob
import pickle

#input for directory
DIRECTORY = str(raw_input('Please enter the path to directory\n'))
print "Directory:- " + DIRECTORY + "\n"

# iterates over files starting with "cl-maze"
for name in glob.glob(DIRECTORY + "/TT[0-9]*-cl-maze[0-9]*.[0-9]"):
    if not name.endswith('.p'):
        spikeInfo = {} #spike firing time for each spike ID
        MazeStartTime = -1
        MazeEndTime = -1
        spikeDataFileName = str(name.split('\\')[1])
        print "Reading File:- " + spikeDataFileName
        spikeDataFile = open(name,'r')
        for lineIndex, line in enumerate(spikeDataFile):
            #Header data can be skipped for now but if someone wants to store, ONE CAN
            if line.startswith('%'):
                continue
            #reads the startTime for the particluar cluster, can be improved by using length function
            elif lineIndex==11:
                mazeStartTime = int(line)
                MazeStartTime = mazeStartTime
            #reads the endTime for the particluar cluster
            elif lineIndex==12:
                mazeEndTime = int(line)
                MazeEndTime = mazeEndTime
            else:
                line = line.rstrip('\n')
                line = line.split(',')
                
                spikeId = int(line[0])
                spikeFiringTime = int(line[17])
                #save the spiketime along with spikeId
                spikeInfo[spikeId] = spikeFiringTime
        
        #save the spike info related to particular cluster 
        print "Maze Start Time: " + str(MazeStartTime)
        print "Maze End Time: " + str(MazeEndTime)
        spikeDataPickleFileName = spikeDataFileName + '.p'
        print "Saving File:- " + spikeDataPickleFileName
        pickle.dump([spikeInfo, MazeStartTime, MazeEndTime], open( spikeDataPickleFileName, "wb"))
        print spikeDataPickleFileName + " File saved\n"
    else:
        continue
    
print "Finished processing all the files"