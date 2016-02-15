# -*- coding: utf-8 -*-
"""
Created on Thu Oct 01 14:48:28 2015

@author: rajat
"""
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np

times = []

with open("time4hr.txt") as f:    
    for line in f:
        datetime = line.rstrip('\n').split(',')[1]
        date = dt.datetime.strptime(datetime, " %Y-%m-%d %H:%M:%S.%f")
        times.append(date)
                
diff_time = []
for s, t in zip(times[:-1], times[1:]):
    diff_time.append(((t - s).seconds*1000000000.0 + (t - s).microseconds)/1000.0)

binwidth = 5.0    
plt.hist(diff_time, bins=np.arange(min(diff_time), max(diff_time)+ binwidth, binwidth))
plt.title('4hour 30fps/640*480')
plt.ylabel('Count')
plt.xlabel('Time(ms.)')
plt.show()    