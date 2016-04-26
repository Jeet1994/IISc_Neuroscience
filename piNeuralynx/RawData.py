import neuralynxio
import os
import scipy.io

rawData = []

for filename in os.listdir(os.getcwd()):
    if filename.endswith(".ncs"): 
        csc = neuralynxio.load_ncs(filename)
        rawData.append(csc['data'])


scipy.io.savemat('rawData.mat', mdict = {'rawData':rawData})