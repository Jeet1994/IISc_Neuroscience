# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

times = []

with open("cam7_timestamp.txt") as f:    
    for line in f:
        timestamp = line.split(',')[0]
        times.append(float(timestamp))
                
diff_time = []
for s, t in zip(times[:-1], times[1:]):
    diff_time.append((float(t - s)))

data = diff_time
plt.title('Camera-7 1hour 30fps/640*480')
plt.ticklabel_format(useOffset=False, style='plain')
plt.axis([33.296, 33.34, 0, 100000])
plt.grid(True)
plt.autoscale(enable=False, axis=u'both', tight=None)
plt.ylabel('Count')
plt.xlabel('Time(ms.)')
counts, bins, patches = plt.hist(data, facecolor='blue', edgecolor='gray')
print counts, bins
plt.xticks(bins)

# Label the raw counts and the percentages below the x-axis...
bin_centers = 0.5 * np.diff(bins) + bins[:-1]
for count, x in zip(counts, bin_centers):
    # Label the raw counts
    plt.annotate(str(count), xy=(x, 0), xycoords=('data', 'axes fraction'),
        xytext=(0, -18), textcoords='offset points', va='top', ha='center')

    # Label the percentages
    percent = '%0.0f%%' % (100 * float(count) / counts.sum())
    plt.annotate(percent, xy=(x, 0), xycoords=('data', 'axes fraction'),
        xytext=(0, -32), textcoords='offset points', va='top', ha='center')


# Give ourselves some more room at the bottom of the plot
plt.subplots_adjust(bottom=0.15)
plt.show()
