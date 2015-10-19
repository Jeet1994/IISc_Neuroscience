import neuralynxio
import matplotlib.pyplot as plt
import numpy as np

def maximumabsolute(datapoints):
	return np.max(np.abs(datapoints))

channelname = 'CSC47'
filename = channelname + '.ncs'

csc = neuralynxio.load_ncs(filename)

plt.plot(csc['data'],'b.')
plt.xlabel('index')
plt.ylabel('output voltage (microV.)')
plotname = channelname +'Rawdata.png'
plt.savefig(plotname)