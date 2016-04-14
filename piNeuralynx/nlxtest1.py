# -*- coding: utf-8 -*-
"""
Created on Wed Apr 06 11:33:47 2016

@author: rajat
"""

import lynxio
import matplotlib.pyplot as plt
import numpy as np
import pickle
import os


rawData= []

def processingNlxData(filename):
    csc = lynxio.loadNcs(filename)
    rawData.append(csc)

for filename in os.listdir(os.getcwd()):
    if filename.endswith(".ncs"): 
        processingNlxData(filename)
        continue
    elif filename.endswith(".nev"):
        eventTimestamps, eventId, nttl, eventNames = lynxio.loadNev(filename)
        continue
    else:
        continue

with open('RawData_withTimestamps.p', 'w') as f:
    pickle.dump([rawData, eventTimestamps, eventNames], f)
            
#with open('Events.p') as f:
#    obj0, obj1 = pickle.load(f)
#    
#print obj1
#
#print obj0    