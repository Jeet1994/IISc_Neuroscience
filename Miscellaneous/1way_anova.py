# -*- coding: utf-8 -*-

import os

diff_time = []
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".txt"):
        times = []
        
        with open(filename) as f:    
            for line in f:
                timestamp = line.split(',')[0]
                times.append(float(timestamp))
                        
        diff_time.append(times)
        
# compute one-way ANOVA P value   
from scipy import stats  

minimum = min(map(len, diff_time))

for i in range(len(diff_time)):
    diff_time[i] = diff_time[i][:minimum] 
      
f_val, p_val = stats.f_oneway(diff_time[0],diff_time[1],diff_time[2],diff_time[3],diff_time[4],diff_time[5],diff_time[6],diff_time[7])  
  
print "One-way ANOVA P =", p_val   