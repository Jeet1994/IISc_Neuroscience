# -*- coding: utf-8 -*-
"""
Created on Thu Oct 01 14:48:28 2015

@author: rajat
"""
import matplotlib.pyplot as plt

times = []

with open("time1hr.txt") as f:    
    for line in f:
        timestamp = line.split(',')[0]
        times.append(float(timestamp))
                
diff_time = []
for s, t in zip(times[:-1], times[1:]):
    diff_time.append((float(t - s)))

plt.plot(diff_time)
plt.title('1hour 30fps/640*480')
plt.autoscale(enable=False, axis=u'both', tight=None)
plt.ylabel('Time')
plt.xlabel('Frameindex')
plt.show()    