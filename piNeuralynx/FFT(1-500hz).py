# -*- coding: utf-8 -*-

import lynxio
import fileSplitter
import matplotlib.pyplot as plt
import numpy as np
import os
from math import log
from math import log10
def fft(datapoints):
    y = datapoints
    n = len(y) # length of the signal
    Y = np.fft.fft(y)/n # fft computing and normalization
    #Y = Y[range(n/2)]    
    return max(abs(Y))

count = 1
plt.figure(figsize=(30,17))
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".ncs") and filename.startswith("CSC"): 
        channelname = filename.split('.')[0]
        plotname = channelname +'FFT.png'
                
        csc = lynxio.loadNcs(filename)
        eventTimestamps, eventId, nttl, eventNames = lynxio.loadNev('Events.nev')
        print eventNames
        datapointsbaseline = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[1],
        								 eventNames[1], eventTimestamps[2], eventNames[2]) [0:198144]
        datapoints1hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[3],
        								 eventNames[3], eventTimestamps[4], eventNames[4])[0:198144]       
        datapoints5hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[5],
                								 eventNames[5], eventTimestamps[6], eventNames[6])[0:198144]     
        datapoints10hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[7],
                								 eventNames[7], eventTimestamps[8], eventNames[8])[0:198144]
        datapoints50hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[9],
                								 eventNames[9], eventTimestamps[10], eventNames[10])[0:198144]
        datapoints100hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[11],
                								 eventNames[11], eventTimestamps[12], eventNames[12])[0:198144]
        datapoints250hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[13],
                								 eventNames[13], eventTimestamps[14], eventNames[14])[0:198144]
        datapoints300hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[15],
                								 eventNames[15], eventTimestamps[16], eventNames[16])[0:198144]
        datapoints350hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[17],
                								 eventNames[17], eventTimestamps[18], eventNames[18])[0:198144]     
        datapoints400hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[19],
                								 eventNames[19], eventTimestamps[20], eventNames[20])[0:198144]
        datapoints450hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[21],
                								 eventNames[21], eventTimestamps[22], eventNames[22])[0:198144]
        datapoints500hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[23],
                								 eventNames[23], eventTimestamps[24], eventNames[24])[0:198144]
        data = [fft(datapoints1hz), fft(datapoints5hz), fft(datapoints10hz) , fft(datapoints50hz) , fft(datapoints100hz),
                   fft(datapoints250hz), fft(datapoints300hz), fft(datapoints350hz), fft(datapoints400hz), fft(datapoints450hz),
                   fft(datapoints500hz)]
        baselinepostFFT = fft(datapointsbaseline)
        x=[1,5,10,50,100,250,300,350,400,450,500]
        labels = ['1','5','10','50','100','250','300','350', '400', '450', '500']
        plt.subplot(4,4,count)
        plt.xticks(x, labels, fontsize = 12, fontweight = 'bold', rotation = 90)
        plt.yticks(fontsize = 14, fontweight = 'bold')
        plt.ylabel('Amplitude in uV after norm)',fontsize = 10, fontweight = 'bold')
        plt.xlabel('Freq in hz',fontsize = 10, fontweight = 'bold')
        plt.ylim([0,140])
        plt.axhline(y=baselinepostFFT, xmin=0, xmax=10, hold=None, color='red')
        plt.plot(x,data, 'b--o')
        count = count +1
        

plotname = 'all plots2.png'
plt.savefig(plotname)
plt.close()