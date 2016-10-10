# -*- coding: utf-8 -*-

"""
Created on Monday Oct 10 12:55:58 2016

@author: rajat
"""

import numpy as np


"""fetches the nlx clock start time 
MAIN_START_RECORDING: stores the timestamps when Clock started for Neuralynx
Here is the example of time to pick:
-* NOTICE  *-  16:26:25.503 - 0 - RealTimeClock::InitRealTimeClock() - CPU clock frequency for timestamp calculations is 3
 So MAIN_START_RECORDING = 16:26:25:503"""
def getNeuralynxStartTime(LogFileName):
    logFile = open(LogFileName,'r')
    for lineIndex, line in enumerate(logFile):
        #Header data can be skipped for now but if someone wants to store, ONE CAN
        if lineIndex==20:
            startTime = line[15:27]
    return startTime

#function to find the nearest value to a list of dates given pivot value
def nearestDate(dates, pivot):
    minimum = min(dates, key=lambda x: abs(x - pivot))
    minimum_index = dates.index(minimum)
    return minimum_index, minimum

#function to return index of closest matching date to a list of dates given pivot value
def find_id(dates, pivot):
    minimum = min(dates, key=lambda x: abs(x - pivot))
    min_idx = dates.index(minimum)
    return min_idx

#rateMap = spikeMap/occMap   
# takes position data and spikes data along with binning value (default: k=5)
# returns rate_Map, spikeMap, occupancy Map 
def generateRateMap(pos,spk,k=5):
    # red_x, red_y, width and height
    posx = pos["red_x"]
    posy = pos["red_y"]
    width = pos["width"]
    height = pos["height"]

    #change x,y location with no values = 0.0
    for idx, item in enumerate(posx):
        if item == -1:
            posx[idx] = np.nan
            
    for idx, item in enumerate(posy):
        if item == -1:
            posy[idx] = np.nan

    #list to stores x and y position when spikes occured
    posSpikeX = []
    posSpikeY = []
    
    try:
        #indexes for each x, y location where spikes happened
        indx = [find_id(pos["pos_t"],t) for t in spk["SpikeTime"]]
        indy = [find_id(pos["pos_t"],t) for t in spk["SpikeTime"]]
        
        for x in indx:
            posSpikeX.append(posx[x])
        
        for y in indy:
            posSpikeY.append(posy[y])
    
        #binnning on the basis of width and height defined along with K value
        xbin_edges = np.arange(0,height+1,k)
        ybin_edges = np.arange(0,width+1,k)
        spikeMap = np.histogram2d(posSpikeX, posSpikeY,  bins=(xbin_edges,ybin_edges))[0]
        occMap = np.histogram2d(posx, posy,  bins=(xbin_edges,ybin_edges))[0]
        #im_s[0][0] = 0.0
        #im_all[0][0] = 0.0
        rateMap = spikeMap/occMap
        #im = np.nan_to_num(im)
    except ValueError or TypeError:
        pass

    return rateMap, spikeMap, occMap