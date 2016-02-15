# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 02 14:25:11 2016

@author: rajat
"""

# The linux time represents the time as a floating point number expressed in seconds since the epoch, in UTC.
# is the number of seconds that have elapsed since January 1, 1970 (midnight UTC/GMT), not counting leap seconds.
# Literally speaking the epoch is Unix time 0 (midnight 1/1/1970)

import matplotlib.pyplot as plt
import numpy as np

raw_stc_timestamp = []
linux_timestamp = []
diff_raw_stc_linux = []

with open("timestamp_RAW_STC.txt") as f:    
    for line in f:
        timestamp1 = line.split(',')[0]
        timestamp2 = line.split(',')[1]
        diff_raw_stc_linux.append((float(timestamp2) - float(timestamp1)))
        raw_stc_timestamp.append(float(timestamp1))
        linux_timestamp.append(float(timestamp2))
                
raw_stc_timestamp_diff_time = []
linux_timestamp_diff_time = []

for s, t in zip(raw_stc_timestamp[:-1], raw_stc_timestamp[1:]):
    raw_stc_timestamp_diff_time.append((float(t - s))/1000.0)
    
for s, t in zip(linux_timestamp[:-1], linux_timestamp[1:]):
    linux_timestamp_diff_time.append((float(t - s))*1000)

print np.corrcoef(raw_stc_timestamp_diff_time, linux_timestamp_diff_time)

plt.plot(diff_raw_stc_linux)
plt.title('Difference between raw STC time and linux')
plt.ylabel('Time')
plt.xlabel('Frameindex')
plt.show()

plt.hist(diff_raw_stc_linux)
plt.title('Difference between raw STC time and linux')
plt.ylabel('Time')
plt.xlabel('Frameindex')
plt.show()

plt.plot(raw_stc_timestamp_diff_time)
plt.title('RAW STC timestamps')
plt.ylabel('Time(ms.)')
plt.xlabel('Frameindex')
plt.show()    

plt.hist(raw_stc_timestamp_diff_time)
plt.title('RAW STC timestamps')
plt.ylabel('Count')
plt.xlabel('Time(ms.)')
plt.show()

plt.plot(linux_timestamp_diff_time)
plt.title('linux timestamps( time.time())')
plt.ylabel('Time(ms.)')
plt.xlabel('Frameindex')
plt.show()    

plt.hist(system_timestamp_diff_time)
plt.title('linux timestamps( time.time())')
plt.ylabel('Count')
plt.xlabel('Time(ms.)')
plt.show()
