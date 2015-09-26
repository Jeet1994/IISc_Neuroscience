import lynxio
import fileSplitter
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft

def maximumabsolute(datapoints):
    for i in datapoints:
        return max(abs(i))
        
csc = lynxio.loadNcs('CSC2.ncs')
eventTimestamps, eventId, nttl, eventNames = lynxio.loadNev('Events2.nev')
#print eventTimestamps, eventNames

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
    
data = [datapoints1e1hz, datapoints3hz, datapoints8hz, datapoints30hz, datapoints100hz,
        datapoints1khz, datapoints5khz, datapoints1khz]

fftdatapoints1e1hz = fft(datapoints1e1hz)
fftdatapoints3hz = fft(datapoints3hz)
fftdatapoints8hz = fft(datapoints8hz)
fftdatapoints30hz = fft(datapoints30hz)
fftdatapoints100hz = fft(datapoints100hz)
fftdatapoints1khz = fft(datapoints1khz)
fftdatapoints5khz = fft(datapoints5khz)
fftdatapoints15khz = fft(datapoints15khz)

fftdata = [np.abs(fftdatapoints1e1hz),np.abs(fftdatapoints3hz),np.abs(fftdatapoints8hz),np.abs(fftdatapoints30hz),
       np.abs(fftdatapoints100hz),np.abs(fftdatapoints1khz),np.abs(fftdatapoints5khz),np.abs(fftdatapoints15khz)]            

#freqs = np.fft.fftfreq(len(datapoints1khz))
#maxfft = max(np.abs(fftdatapoints1khz))
#print maxfft
#for coef,freq in zip(fftdatapoints1khz,freqs):
#    if np.abs(coef) == maxfft:
#        print freq
        
f, axarr = plt.subplots(4, 2)
axarr[0, 0].plot(np.abs(datapoints1e1hz))
axarr[0, 0].set_title('0.1hz')
axarr[0, 0].set_ylim([0,35000])

axarr[0, 1].plot(np.abs(datapoints3hz))
axarr[0, 1].set_title('3hz')
axarr[0, 1].set_ylim([0,35000])

axarr[1, 0].plot(np.abs(datapoints8hz))
axarr[1, 0].set_title('8hz')
axarr[1, 0].set_ylim([0,35000])

axarr[1, 1].plot(np.abs(datapoints30hz))
axarr[1, 1].set_title('30hz')
axarr[1, 1].set_ylim([0,35000])

axarr[2, 0].plot(np.abs(datapoints100hz))
axarr[2, 0].set_title('100hz')
axarr[2, 0].set_ylim([0,35000])

axarr[2, 1].plot(np.abs(datapoints1khz))
axarr[2, 1].set_title('1khz')
axarr[2, 1].set_ylim([0,35000])

axarr[3, 0].plot(np.abs(datapoints5khz))
axarr[3, 0].set_title('5khz')
axarr[3, 0].set_ylim([0,35000])

axarr[3, 1].plot(np.abs(datapoints15khz))
axarr[3, 1].set_title('15khz')
axarr[3, 1].set_ylim([0,35000])
plt.show()      

f, axarr = plt.subplots(4, 2)
axarr[0, 0].plot(np.abs(fftdatapoints1e1hz))
axarr[0, 0].set_title('0.1hz')
axarr[0, 0].set_ylim([0,5e9])
axarr[0, 0].set_xlim([0,200000])

axarr[0, 1].plot(np.abs(fftdatapoints3hz))
axarr[0, 1].set_title('3hz')
axarr[0, 1].set_ylim([0,5e9])
axarr[0, 1].set_xlim([0,200000])

axarr[1, 0].plot(np.abs(fftdatapoints8hz))
axarr[1, 0].set_title('8hz')
axarr[1, 0].set_ylim([0,5e9])
axarr[1, 0].set_xlim([0,200000])

axarr[1, 1].plot(np.abs(fftdatapoints30hz))
axarr[1, 1].set_title('30hz')
axarr[1, 1].set_ylim([0,5e9])
axarr[1, 1].set_xlim([0,200000])

axarr[2, 0].plot(np.abs(fftdatapoints100hz))
axarr[2, 0].set_title('100hz')
axarr[2, 0].set_ylim([0,5e9])
axarr[2, 0].set_xlim([0,20000])

axarr[2, 1].plot(np.abs(fftdatapoints1khz))
axarr[2, 1].set_title('1khz')
axarr[2, 1].set_ylim([0,5e9])
axarr[2, 1].set_xlim([0,200000])

axarr[3, 0].plot(np.abs(fftdatapoints5khz))
axarr[3, 0].set_title('5khz')
axarr[3, 0].set_ylim([0,5e9])
axarr[3, 0].set_xlim([0,200000])

axarr[3, 1].plot(np.abs(fftdatapoints15khz))
axarr[3, 1].set_title('15khz')
axarr[3, 1].set_ylim([0,5e9])
axarr[3, 1].set_xlim([0,200000])

plt.show() 

#f, axarr = plt.subplots(2, sharex=True)
#axarr[0].boxplot(data)
#axarr[0].set_title('Data')
#axarr[0].set_ylabel('Amplitude')
#
#axarr[1].boxplot(fftdata)
#axarr[1].set_title('After FFT')
#
#x=[1,2,3,4,5,6,7,8]
#labels = ['.1','3','8','30','100','1k','5k','15k']
#plt.xticks(x, labels)
#plt.xlabel('frequency')
#plt.show()