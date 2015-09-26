# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 19:03:32 2015

@author: rajat
"""

import csv
import matplotlib.pyplot as plt
import matplotlib
import datetime

f = open('output4hr.csv')
try:
    reader = csv.reader(f)
    times = []
    for row in reader:
        useconds = row[0].split('.')[1]
        hours =  row[0].split('.')[0].split(':')[0]
        mins =  row[0].split('.')[0].split(':')[1]
        seconds =  row[0].split('.')[0].split(':')[2]        
        my_day = datetime.date(2015, 9, 16)
        timestamp = datetime.time(int(hours), int(mins), int(seconds), int(useconds))        
        x_dt = [ datetime.datetime.combine(my_day, timestamp)]
        times.append(matplotlib.dates.date2num(x_dt))
finally:
    f.close()

diff_time= []
for s, t in zip(times[:-1], times[1:]):
    diff_time.append(t - s) 
  
plt.plot(times)
plt.title('4 hour/ 30fps/ 640*480')
plt.ylabel('Time(Fraction of days that have passed since jan 0,0000)')
plt.xlabel('index')
plt.show()

plt.plot(diff_time)
plt.title('4 hour/ 30fps/ 640*480')
plt.ylabel('Time(Fraction of days that have passed since jan 0,0000)')
plt.xlabel('index')
plt.show()