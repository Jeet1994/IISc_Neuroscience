import lynxio
import fileSplitter
import matplotlib.pyplot as plt
import numpy as np
import math

def maximumabsolute(datapoints):
	return np.max(np.abs(datapoints))

channelname = 'CSC61'
filename = channelname + '.ncs'
plotname = channelname +'Gains.png'
        
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

datapoints15khz = fileSplitter.fileSplitterUsingEvents(csc, eventTimestamps[16],
								 eventNames[16], eventTimestamps[17], eventNames[17])
         
maxdata = [maximumabsolute(datapoints1e1hz),maximumabsolute(datapoints3hz), maximumabsolute(datapoints8hz),
		 maximumabsolute(datapoints30hz), maximumabsolute(datapoints100hz), maximumabsolute(datapoints1khz),
		 maximumabsolute(datapoints5khz), maximumabsolute(datapoints15khz)]

d = []
for i in maxdata:
    d.append(20*math.log(i/1000.0, 10))

x=[0,1,2,3,4,5,6,7,8]
labels = ['.1','3','8','30','100','1000','5000','15000']
plt.plot(d, 'bo', d, '--')
plt.xticks(x, labels)
plt.xlabel('frequency(hz)')
plt.ylabel('Gains :  20*log(Vout/Vin))')
plt.savefig(plotname)