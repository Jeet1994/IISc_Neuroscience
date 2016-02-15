# -*- coding: utf-8 -*-
"""
Created on Thu Oct 01 14:48:28 2015

@author: rajat
"""
import matplotlib.pyplot as plt
import datetime as dt

times = []

with open("time4hr.txt") as f:    
    for line in f:
        datetime = line.rstrip('\n').split(',')[1]
        date = dt.datetime.strptime(datetime, " %Y-%m-%d %H:%M:%S.%f")
        times.append(date)
                
diff_time = []
for s, t in zip(times[:-1], times[1:]):
    diff_time.append(((t - s).seconds*1000000000.0 + (t - s).microseconds)/1000.0)
    
plt.plot(diff_time)
plt.title('4hour 30fps/640*480')
plt.autoscale(enable=False, axis=u'both', tight=None)
plt.ylabel('Time(milli seconds)')
plt.xlabel('Frameindex')
plt.show()    