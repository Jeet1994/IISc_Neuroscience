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

system_timestamp = []
linux_timestamp = []
diff_system_linux = []

with open("timestamp_SYSTEM_TIME.txt") as f:    
    for line in f:
        timestamp1 = line.split(',')[0]
        timestamp2 = line.split(',')[1]
        diff_system_linux.append((float(timestamp2) - float(timestamp1)))
        system_timestamp.append(float(timestamp1))
        linux_timestamp.append(float(timestamp2))
                
system_timestamp_diff_time = []
linux_timestamp_diff_time = []

for s, t in zip(system_timestamp[:-1], system_timestamp[1:]):
    system_timestamp_diff_time.append((float(t - s))/1000.0)
    
for s, t in zip(linux_timestamp[:-1], linux_timestamp[1:]):
    linux_timestamp_diff_time.append((float(t - s))*1000)

print np.corrcoef(system_timestamp_diff_time, linux_timestamp_diff_time)

plt.plot(diff_system_linux)
plt.title('Difference between system time and linux')
plt.ylabel('Time')
plt.xlabel('Frameindex')
plt.show()

plt.hist(diff_system_linux)
plt.title('Difference between system time and linux')
plt.ylabel('Time')
plt.xlabel('Frameindex')
plt.show()

plt.plot(system_timestamp_diff_time)
plt.title('system timestamps( SYSTEM_TIME)')
plt.ylabel('Time(ms.)')
plt.xlabel('Frameindex')
plt.show()    

plt.hist(system_timestamp_diff_time)
plt.title('system timestamps( SYSTEM_TIME)')
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
