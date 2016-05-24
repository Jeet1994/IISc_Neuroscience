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

#baseline_csc = lynxio.loadNcs('baseline.ncs')
#baseline_eventTimestamps, baseline_eventId, baseline_nttl, baseline_eventNames = lynxio.loadNev('baseline_Events.nev')
#baselinedatapoint = fileSplitter.fileSplitterUsingEvents(baseline_csc, baseline_eventTimestamps[1],
#        								 baseline_eventNames[1], baseline_eventTimestamps[2], baseline_eventNames[2])[0:30000]        
#baselinepostFFT = fft(baselinedatapoint)
count = 1;
plt.figure(figsize=(30,17))
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".ncs") and filename.startswith("CSC"): 
        channelname = filename.split('.')[0]
        plotname = channelname +'FFT.png'
                
        csc = lynxio.loadNcs(filename)
        eventTimestamps, eventId, nttl, eventNames = lynxio.loadNev('Events.nev')
        print eventNames    

        #datapoints100hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[1],
        #								 eventNames[1], eventTimestamps[2], eventNames[2])[0:30000] 
        datapointsbaseline = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[1],
        								 eventNames[1], eventTimestamps[2], eventNames[2])[0:197120]     
        datapoints300hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[3],
        								 eventNames[3], eventTimestamps[4], eventNames[4])[0:197120] 
        datapoints450hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[5],
        								 eventNames[5], eventTimestamps[6], eventNames[6])[0:197120] 
        datapoints500hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[7],
        								 eventNames[7], eventTimestamps[8], eventNames[8])[0:197120] 
        datapoints600hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[9],
        								 eventNames[9], eventTimestamps[10], eventNames[10])[0:197120] 
        datapoints750hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[11],
        								 eventNames[11], eventTimestamps[12], eventNames[12])[0:197120] 
        datapoints1khz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[13],
        								 eventNames[13], eventTimestamps[14], eventNames[14])[0:197120] 
        datapoints5khz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[15], 
                                                    eventNames[15], eventTimestamps[16], eventNames[16])[0:197120] 
        datapoints9khz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[17],
        								 eventNames[17], eventTimestamps[18], eventNames[18])[0:197120] 
        
        data = [fft(datapoints300hz) , fft(datapoints450hz) , fft(datapoints500hz),
                fft(datapoints600hz), fft(datapoints750hz), fft(datapoints1khz), fft(datapoints5khz), fft(datapoints9khz)]

        baselinepostFFT = fft(datapointsbaseline)
        x=[log10(300),log10(450),log10(500),log10(600),log10(750),log10(1000),log10(5000),log10(9000)]
        labels = ['300','450','500','600','750','1k', '5k', '9k']
        #plt.figure(figsize=(20,10))
        plt.subplot(4,4,count)
        plt.xticks(x, labels, fontsize = 12, fontweight = 'bold', rotation = 90)
        plt.yticks(fontsize = 14, fontweight = 'bold')
        plt.ylabel('Amplitude in uV after norm)',fontsize = 10, fontweight = 'bold')
        plt.xlabel('Log Freq in hz',fontsize = 10, fontweight = 'bold')
        plt.ylim([0,140])
        plt.axhline(y=baselinepostFFT, xmin=0, xmax=10, hold=None, color='red')
        plt.plot(x,data, 'b--o')
        
        
        
        count = count +1
plotname = 'all plots.png'
plt.savefig(plotname)
plt.close()