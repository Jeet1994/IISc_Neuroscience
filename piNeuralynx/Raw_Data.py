
# coding: utf-8

import neuralynxio
import os
import scipy.io

for filename in os.listdir(os.getcwd()):
    if filename.endswith(".ncs")and filename.startswith("CSC"): 
        channelname = filename.split('.')[0]
        
        rawData = []
        
        csc = neuralynxio.load_ncs(filename)
        
        rawData.append(csc['data'])
        header = csc['header']
        samplingRate = float(csc['sampling_rate'])
        
        scipy.io.savemat('_' + channelname + '_rawData.mat', mdict = {'rawData':rawData, 'samplingRate': samplingRate})