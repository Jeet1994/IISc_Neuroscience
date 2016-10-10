import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.cm as cm

cdict = cm.get_cmap('jet')._segmentdata
red = ((0.0,0.0,0.0), (0.0, 0, 0), (0.35, 0, 0), (0.66, 1, 1), (0.89, 1, 1), (1, 0.5, 0.5))
blue = ((0.0,0.0,0.0), (0.0, 0.5, 0.5), (0.11, 1, 1), (0.34, 1, 1), (0.65, 0, 0), (1, 0, 0))
green = ((0.0, 0.0, 0.0), (0.125, 0, 0), (0.375, 1, 1), (0.64, 1, 1), (0.91, 0, 0), (1, 0, 0))
cdict['red'] = red
cdict['green'] = green
cdict['blue'] = blue
cmap = LinearSegmentedColormap('name', cdict)

rawMapsFileName = 'rawMaps_cl-maze1.1.UpdatedTimestamps.npy'
rateMap, occMap, spikeMap = np.load(rawMapsFileName)


fig, ax = plt.subplots()
#im = nd.gaussian_filter(rateMap, 2, order=0)
im = ax.imshow(rateMap, cmap=cmap, interpolation='None')
fig.colorbar(im)
plt.show()