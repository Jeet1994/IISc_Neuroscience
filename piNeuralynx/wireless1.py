import lynxio
import fileSplitter
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft

def maximumabsolute(datapoints):
	return np.max(np.abs(datapoints))
        
csc = lynxio.loadNcs('CSC3.ncs')
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

datapoints15khz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[15],
								 eventNames[15], eventTimestamps[16], eventNames[16])
    
maxdata = [maximumabsolute(datapoints1e1hz),maximumabsolute(datapoints3hz), maximumabsolute(datapoints8hz),
		 maximumabsolute(datapoints30hz), maximumabsolute(datapoints100hz), maximumabsolute(datapoints1khz),
		 maximumabsolute(datapoints5khz), maximumabsolute(datapoints15khz)]

fftdatapoints1e1hz = fft(datapoints1e1hz)
fftdatapoints3hz = fft(datapoints3hz)
fftdatapoints8hz = fft(datapoints8hz)
fftdatapoints30hz = fft(datapoints30hz)
fftdatapoints100hz = fft(datapoints100hz)
fftdatapoints1khz = fft(datapoints1khz)
fftdatapoints5khz = fft(datapoints5khz)
fftdatapoints15khz = fft(datapoints15khz)         

maxfft = [ maximumabsolute(fftdatapoints1e1hz),maximumabsolute(fftdatapoints3hz), maximumabsolute(fftdatapoints8hz),
		 maximumabsolute(fftdatapoints30hz), maximumabsolute(fftdatapoints100hz), maximumabsolute(fftdatapoints1khz),
		 maximumabsolute(fftdatapoints5khz), maximumabsolute(fftdatapoints15khz)]


x=[0,1,2,3,4,5,6,7,8]
labels = ['.1','3','8','30','100','1k','5k','15k']
#plt.plot(maxfft)
plt.plot(maxdata)
plt.xticks(x, labels)
plt.xlabel('frequency')
plt.show()