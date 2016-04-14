# -*- coding: utf-8 -*-

import lynxio
import fileSplitter
import matplotlib.pyplot as plt
import numpy as np
import os

def fft(datapoints):
    y = datapoints
    n = len(y) # length of the signal
    Y = np.fft.fft(y)/n # fft computing and normalization
    Y = Y[range(n/2)]    
    return max(abs(Y))

baseline_csc = lynxio.loadNcs('baseline.ncs')
baseline_eventTimestamps, baseline_eventId, baseline_nttl, baseline_eventNames = lynxio.loadNev('baseline_Events.nev')
baselinedatapoint = fileSplitter.fileSplitterUsingEvents(baseline_csc, baseline_eventTimestamps[1],
        								 baseline_eventNames[1], baseline_eventTimestamps[2], baseline_eventNames[2])[0:30000]        
baselinepostFFT = fft(baselinedatapoint)

for filename in os.listdir(os.getcwd()):
    if filename.endswith(".ncs") and filename.startswith("CSC"): 
        channelname = filename.split('.')[0]
        plotname = channelname +'FFT.png'
                
        csc = lynxio.loadNcs(filename)
        eventTimestamps, eventId, nttl, eventNames = lynxio.loadNev('Events.nev')
        print eventNames

        datapoints1e1hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[1],
        								 eventNames[1], eventTimestamps[2], eventNames[2])[0:30000]       
        datapoints3hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[3],
                								 eventNames[3], eventTimestamps[4], eventNames[4])[0:30000]     
        datapoints8hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[5],
                								 eventNames[5], eventTimestamps[6], eventNames[6])[0:30000]
        datapoints30hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[7],
                								 eventNames[7], eventTimestamps[8], eventNames[8])[0:30000]
        datapoints100hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[9],
                								 eventNames[9], eventTimestamps[10], eventNames[10])[0:30000]
        datapoints1khz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[11],
                								 eventNames[11], eventTimestamps[12], eventNames[12])[0:30000]
        datapoints5khz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[13],
                								 eventNames[13], eventTimestamps[14], eventNames[14])[0:30000]
        datapoints9khz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[15],
                								 eventNames[15], eventTimestamps[16], eventNames[16])[0:30000]      
        datapoints15khz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[17],
                								 eventNames[17], eventTimestamps[18], eventNames[18])[0:30000]
        
        data = [fft(datapoints1e1hz), fft(datapoints3hz), fft(datapoints8hz) , fft(datapoints30hz) , fft(datapoints100hz),
                   fft(datapoints1khz), fft(datapoints5khz), fft(datapoints9khz), fft(datapoints15khz)]
        
        x=[0,1,2,3,4,5,6,7,8,9,10]
        labels = ['0.1','3','8','30','100','1000', '5000', '9000', '15000']
        plt.xticks(x, labels)
        plt.ylabel('Amplitude after FFT')
        plt.xlabel('Freq')
        plt.ylim([0,180])
        plt.axhline(y=baselinepostFFT, xmin=0, xmax=10, hold=None, color='red')
        plt.plot(data, 'b--o')
        plt.plot()
        plt.savefig(plotname)
        plt.close()

