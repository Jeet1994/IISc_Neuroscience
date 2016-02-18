# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

times = []

with open("timestamp_cam8.txt") as f:    
    for line in f:
        timestamp = line.split(',')[0]
        times.append(float(timestamp))
                
diff_time = []
for s, t in zip(times[:-1], times[1:]):
    diff_time.append((float(t - s)))

plt.hist(diff_time)
plt.title('Camera-8 1hour 30fps/640*480')
plt.xlim(33.28,33.34)
plt.autoscale(enable=False, axis=u'both', tight=None)
plt.ylabel('Count')
plt.xlabel('Time(ms.)')
plt.show()    