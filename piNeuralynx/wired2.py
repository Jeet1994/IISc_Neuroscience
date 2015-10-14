import lynxio
import fileSplitter
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft

def maximumabsolute(datapoints):
	return np.max(np.abs(datapoints))
        
csc = lynxio.loadNcs('CSC1.ncs')
eventTimestamps, eventId, nttl, eventNames = lynxio.loadNev('Events.nev')


datapoints1e1hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[1],
								 eventNames[1], eventTimestamps[2], eventNames[2]) 

datapoints1hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[3],
								 eventNames[3], eventTimestamps[4], eventNames[4])
        
datapoints5hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[5],
								 eventNames[5], eventTimestamps[6], eventNames[6])

datapoints10hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[7],
								 eventNames[7], eventTimestamps[8], eventNames[8])

datapoints50hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[9],
								 eventNames[9], eventTimestamps[10], eventNames[10])

datapoints100hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[11],
								 eventNames[11], eventTimestamps[12], eventNames[12])

datapoints250hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[13],
								 eventNames[13], eventTimestamps[14], eventNames[14])

datapoints300hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[15],
								 eventNames[15], eventTimestamps[16], eventNames[16])

datapoints350hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[17],
								 eventNames[17], eventTimestamps[18], eventNames[18])

datapoints400hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[19],
								 eventNames[19], eventTimestamps[20], eventNames[20])

datapoints450hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[21],
								 eventNames[21], eventTimestamps[22], eventNames[22])

datapoints500hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[23],
								 eventNames[23], eventTimestamps[24], eventNames[24])

datapoints600hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[25],
								 eventNames[25], eventTimestamps[26], eventNames[26])

maxdata = [maximumabsolute(datapoints1e1hz),maximumabsolute(datapoints1hz), maximumabsolute(datapoints5hz),
		 maximumabsolute(datapoints10hz), maximumabsolute(datapoints50hz), maximumabsolute(datapoints100hz),
		 maximumabsolute(datapoints250hz), maximumabsolute(datapoints300hz), maximumabsolute(datapoints350hz),
		 maximumabsolute(datapoints400hz), maximumabsolute(datapoints450hz), maximumabsolute(datapoints500hz),
		 maximumabsolute(datapoints600hz)]

fftdatapoints1e1hz = fft(datapoints1e1hz)
fftdatapoints1hz = fft(datapoints1hz)
fftdatapoints5hz = fft(datapoints5hz)
fftdatapoints10hz = fft(datapoints10hz)
fftdatapoints50hz = fft(datapoints50hz)
fftdatapoints100hz = fft(datapoints100hz)
fftdatapoints250hz = fft(datapoints250hz)
fftdatapoints300hz = fft(datapoints300hz)
fftdatapoints350hz = fft(datapoints350hz)
fftdatapoints400hz = fft(datapoints400hz)
fftdatapoints450hz = fft(datapoints450hz)
fftdatapoints500hz = fft(datapoints500hz)
fftdatapoints600hz =fft(datapoints600hz)

maxfft = [ maximumabsolute(fftdatapoints1e1hz),maximumabsolute(fftdatapoints1hz), maximumabsolute(fftdatapoints5hz),
		 maximumabsolute(fftdatapoints10hz), maximumabsolute(fftdatapoints50hz), maximumabsolute(fftdatapoints100hz),
		 maximumabsolute(fftdatapoints250hz), maximumabsolute(fftdatapoints300hz), maximumabsolute(fftdatapoints350hz),
		 maximumabsolute(fftdatapoints400hz), maximumabsolute(fftdatapoints450hz), maximumabsolute(fftdatapoints500hz),
		 maximumabsolute(fftdatapoints600hz)]


x=[0,1,2,3,4,5,6,7,8,9,10,11,12,13]
labels = ['.1','1','5','10','50','100','250','300','350','400','450','500','600']
plt.plot(maxdata)
plt.xticks(x, labels)
plt.xlabel('frequency')
plt.show()