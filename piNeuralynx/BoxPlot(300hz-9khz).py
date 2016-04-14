# -*- coding: utf-8 -*-

import lynxio
import fileSplitter
import matplotlib.pyplot as plt
import os
    
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".ncs"): 
        channelname = filename.split('.')[0]
        plotname = channelname +'BoxPlot.png'
                
        csc = lynxio.loadNcs(filename)
        eventTimestamps, eventId, nttl, eventNames = lynxio.loadNev('Events.nev')
        print eventNames

        datapoints100hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[1],
        								 eventNames[1], eventTimestamps[2], eventNames[2]) 
        datapoints250hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[3],
        								 eventNames[3], eventTimestamps[4], eventNames[4])        
        datapoints300hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[5],
        								 eventNames[5], eventTimestamps[6], eventNames[6])
        datapoints450hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[7],
        								 eventNames[7], eventTimestamps[8], eventNames[8])
        datapoints500hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[9],
        								 eventNames[9], eventTimestamps[10], eventNames[10])
        datapoints600hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[11],
        								 eventNames[11], eventTimestamps[12], eventNames[12])
        datapoints750hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[13],
        								 eventNames[13], eventTimestamps[14], eventNames[14])
        datapoints1khz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[15],
        								 eventNames[15], eventTimestamps[16], eventNames[16])
        datapoints2khz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[17], 
                                                               eventNames[17], eventTimestamps[18], eventNames[18])
        datapoints4khz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[19],
        								 eventNames[19], eventTimestamps[20], eventNames[20])
        datapoints6khz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[21],
        								 eventNames[21], eventTimestamps[22], eventNames[22])
        datapoints7khz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[23],
        								 eventNames[23], eventTimestamps[24], eventNames[24])
        datapoints8khz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[25],
        								 eventNames[25], eventTimestamps[26], eventNames[26])
        datapoints9khz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[27],
        								 eventNames[27], eventTimestamps[28], eventNames[28])         
        datapoints10khz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[29],
        								 eventNames[29], eventTimestamps[30], eventNames[30])
                 
        data = [datapoints100hz,datapoints250hz,datapoints300hz, datapoints450hz, datapoints500hz,datapoints600hz,datapoints750hz,datapoints1khz,datapoints2khz, 
                   datapoints4khz, datapoints6khz, datapoints7khz, datapoints8khz, datapoints9khz, datapoints10khz]
        
        x=[1,2,3,4,5,6,7,8, 9 ,10, 11, 12, 13, 14, 15, 16]
        labels = ['250','300','450','500','600','750','1k', '2k', '4k', '6k', '7k', '8k', '9k', '10k']
        plt.boxplot(data)
        plt.xticks(x, labels)
        plt.xlabel('frequency(hz)')
        plt.ylabel('output voltage variation')
        plt.ylim((-1500,1500))
        plt.savefig(plotname)
        plt.close()

