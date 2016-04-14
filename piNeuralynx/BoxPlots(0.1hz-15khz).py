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
        
        datapoints1e1hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[1],
        								 eventNames[1], eventTimestamps[2], eventNames[2])       
        datapoints3hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[3],
        								 eventNames[3], eventTimestamps[4], eventNames[4])     
        datapoints8hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[5],
        								 eventNames[5], eventTimestamps[6], eventNames[6])
        datapoints30hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[7],
        								 eventNames[7], eventTimestamps[8], eventNames[8])
        datapoints100hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[9],
        								 eventNames[9], eventTimestamps[10], eventNames[10])
        datapoints1khz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[11],
        								 eventNames[11], eventTimestamps[12], eventNames[12])
        datapoints5khz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[13],
        								 eventNames[13], eventTimestamps[14], eventNames[14])
        datapoints9khz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[15],
        								 eventNames[15], eventTimestamps[16], eventNames[16])      
        datapoints15khz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[17],
        								 eventNames[17], eventTimestamps[18], eventNames[18])
            
        data = [datapoints1e1hz,datapoints3hz,datapoints8hz, datapoints30hz,datapoints100hz,datapoints1khz,datapoints5khz,datapoints15khz]
        
        x=[0,1,2,3,4,5,6,7, 8,9]
        labels = ['0' , '.1','3','8','30','100','1000','5000','9000','15000']
        plt.boxplot(data)
        plt.xticks(x, labels)
        plt.xlabel('frequency(hz)')
        plt.ylabel('output voltage variation')
        plt.ylim((-1500,1500))
        plt.savefig(plotname)
        plt.close()
         
        

