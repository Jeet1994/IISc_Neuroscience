# -*- coding: utf-8 -*-

import scipy.io
import os

for filename in os.listdir(os.getcwd()):
    if filename.endswith(".CSV"): 
        idno = filename.split('.')[0]
        data = [ ]
        with open(filename, 'rb') as f:
            for row in f:
                row = row.split(',')
                time, ampl = float(row[3]), float(row[4])
                data.append(ampl)
                scipy.io.savemat(idno+'.mat', {'csvdata':data})
        f.close()