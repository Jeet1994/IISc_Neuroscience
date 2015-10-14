import lynxio
import fileSplitter
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft

def maximumabsolute(datapoints):
	return np.max(np.abs(datapoints))
        
csc = lynxio.loadNcs('CSC1.ncs')
eventTimestamps, eventId, nttl, eventNames = lynxio.loadNev('Events.nev')

datapoints250hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[1],
								 eventNames[1], eventTimestamps[2], eventNames[2]) 

datapoints300hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[3],
								 eventNames[3], eventTimestamps[4], eventNames[4])
        
datapoints450hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[5],
								 eventNames[5], eventTimestamps[6], eventNames[6])

datapoints500hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[7],
								 eventNames[7], eventTimestamps[8], eventNames[8])

datapoints600hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[9],
								 eventNames[9], eventTimestamps[10], eventNames[10])

datapoints750hz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[11],
								 eventNames[11], eventTimestamps[12], eventNames[12])

datapoints1khz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[13],
								 eventNames[13], eventTimestamps[14], eventNames[14])

datapoints2khz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[15],
								 eventNames[15], eventTimestamps[16], eventNames[16])

datapoints4khz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[17],
								 eventNames[17], eventTimestamps[18], eventNames[18])

datapoints6khz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[19],
								 eventNames[19], eventTimestamps[20], eventNames[20])

datapoints7khz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[21],
								 eventNames[21], eventTimestamps[22], eventNames[22])

datapoints8khz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[23],
								 eventNames[23], eventTimestamps[24], eventNames[24])

datapoints9khz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[25],
								 eventNames[25], eventTimestamps[26], eventNames[26])

datapoints10khz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[27],
								 eventNames[27], eventTimestamps[28], eventNames[28])

maxdata = [maximumabsolute(datapoints250hz),maximumabsolute(datapoints300hz), maximumabsolute(datapoints450hz),
		 maximumabsolute(datapoints500hz), maximumabsolute(datapoints600hz), maximumabsolute(datapoints750hz),
		 maximumabsolute(datapoints1khz), maximumabsolute(datapoints2khz), maximumabsolute(datapoints4khz),
		 maximumabsolute(datapoints6khz), maximumabsolute(datapoints7khz), maximumabsolute(datapoints8khz),
		 maximumabsolute(datapoints9khz), maximumabsolute(datapoints10khz)]

fftdatapoints250hz = fft(datapoints250hz)
fftdatapoints300hz = fft(datapoints300hz)
fftdatapoints450hz = fft(datapoints450hz)
fftdatapoints500hz = fft(datapoints500hz)
fftdatapoints600hz = fft(datapoints600hz)
fftdatapoints750hz = fft(datapoints750hz)
fftdatapoints1khz = fft(datapoints1khz)
fftdatapoints2khz = fft(datapoints2khz)
fftdatapoints4khz = fft(datapoints4khz)
fftdatapoints6khz = fft(datapoints6khz)
fftdatapoints7khz = fft(datapoints7khz)
fftdatapoints8khz = fft(datapoints8khz)
fftdatapoints9khz = fft(datapoints9khz)
fftdatapoints10khz = fft(datapoints10khz)

maxfft = [ maximumabsolute(fftdatapoints250hz),maximumabsolute(fftdatapoints300hz), maximumabsolute(fftdatapoints450hz),
		 maximumabsolute(fftdatapoints500hz), maximumabsolute(fftdatapoints600hz), maximumabsolute(fftdatapoints750hz),
		 maximumabsolute(fftdatapoints1khz), maximumabsolute(fftdatapoints2khz), maximumabsolute(fftdatapoints4khz),
		 maximumabsolute(fftdatapoints6khz), maximumabsolute(fftdatapoints7khz), maximumabsolute(fftdatapoints8khz),
		 maximumabsolute(fftdatapoints9khz), maximumabsolute(fftdatapoints10khz)]


x=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
labels = ['250','300','450','500','600','750','1k','2k','4k','6k','7k','8k','9k', '10k']
plt.plot(maxdata)
plt.xticks(x, labels)
plt.xlabel('frequency')
plt.show()