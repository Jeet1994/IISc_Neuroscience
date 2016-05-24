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
    Y = Y[range(n/2)]    
    return max(abs(Y))


count = 1;
plt.figure(figsize=(30,17))
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".ncs") and filename.startswith("CSC"): 
        channelname = filename.split('.')[0]
        plotname = channelname +'FFT.png'
                
        csc = lynxio.loadNcs(filename)
        eventTimestamps, eventId, nttl, eventNames = lynxio.loadNev('Events.nev')
        print eventNames
        
        datapointsbaseline = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[1],
        								 eventNames[1], eventTimestamps[2], eventNames[2])[0:229888]
        datapoints1e1hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[3],
        								 eventNames[3], eventTimestamps[4], eventNames[4])[0:229888]     
        datapoints3hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[5],
                								 eventNames[5], eventTimestamps[6], eventNames[6])[0:229888]   
        datapoints8hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[7],
                								 eventNames[7], eventTimestamps[8], eventNames[8])[0:229888]
        datapoints30hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[9],
                								 eventNames[9], eventTimestamps[10], eventNames[10])[0:229888]
        datapoints100hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[11],
                								 eventNames[11], eventTimestamps[12], eventNames[12])[0:229888]
        datapoints1khz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[13],
                								 eventNames[13], eventTimestamps[14], eventNames[14])[0:229888]
        datapoints5khz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[15],
                								 eventNames[15], eventTimestamps[16], eventNames[16])[0:229888]
        datapoints9khz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[17],
                								 eventNames[17], eventTimestamps[18], eventNames[18])[0:229888]    
        datapoints15khz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[19],
                								 eventNames[19], eventTimestamps[20], eventNames[20])[0:30000]
        baselinepostFFT = fft(datapointsbaseline)
        data = [fft(datapoints1e1hz), fft(datapoints3hz), fft(datapoints8hz) , fft(datapoints30hz) , fft(datapoints100hz),
                   fft(datapoints1khz), fft(datapoints5khz), fft(datapoints9khz), fft(datapoints15khz)]
        
        x=[log10(0.1),log10(3),log10(8),log10(30),log10(100),log10(1000),log10(5000),log10(9000), log10(15000)]
        labels = ['0.1','3','8','30','100','1k', '5k', '9k', '15k']
        
        plt.subplot(4,4,count)
        plt.xticks(x, labels, fontsize = 16, fontweight = 'bold',rotation = 90)
        plt.yticks(fontsize = 16, fontweight = 'bold')
        plt.ylabel('Amplitude(uV) after norm',fontsize = 10, fontweight = 'bold')
        plt.xlabel('Log Freq(hz)',fontsize = 10, fontweight = 'bold')
        plt.ylim([0,140])
        plt.axhline(y=baselinepostFFT, xmin=0, xmax=10, hold=None, color='red')
        
        plt.plot(x,data, 'b--o')
        count = count +1

plotname = 'all plots.png'
plt.savefig(plotname)
plt.close()