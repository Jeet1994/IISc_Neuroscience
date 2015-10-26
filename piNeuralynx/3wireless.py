import lynxio
import fileSplitter
import matplotlib.pyplot as plt
import numpy as np
    
channelname = 'CSC1'
filename = channelname + '.ncs'
plotname = channelname +'FFT.png'
        
csc = lynxio.loadNcs(filename)
eventTimestamps, eventId, nttl, eventNames = lynxio.loadNev('Events.nev')
print eventNames

def fft(datapoints):
    y = datapoints
    n = len(y) # length of the signal
    Y = np.fft.fft(y)/n # fft computing and normalization

    return np.max(np.abs(Y))    
    
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

datapoints15khz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[16],
								 eventNames[16], eventTimestamps[17], eventNames[17])
         
data = [fft(datapoints1e1hz), fft(datapoints3hz), fft(datapoints8hz) , fft(datapoints30hz) , fft(datapoints100hz),
            fft(datapoints1khz), fft(datapoints5khz), fft(datapoints15khz)]

x=[0,1,2,3,4,5,6,7,8, 9 ,10, 11, 12, 13]
labels = ['.1','1','5','10','50','100','250','300', '350', '400', '450', '500', '600']
plt.xticks(x, labels)
plt.xlabel('frequency(hz)')
plt.ylabel('Amplitude')
plt.plot(data,'b--o',)
plt.savefig(plotname)