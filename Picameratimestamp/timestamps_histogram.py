# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

times = []

with open("time4hr.txt") as f:    
    for line in f:
        timestamp = line.split(',')[0]
        times.append(float(timestamp))
                
diff_time = []
for s, t in zip(times[:-1], times[1:]):
    diff_time.append((float(t - s)))

plt.hist(diff_time)
plt.title('4hour 30fps/640*480')
plt.autoscale(enable=False, axis=u'both', tight=None)
plt.ylabel('Count')
plt.xlabel('Time(ms.)')
plt.show()    