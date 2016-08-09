# -*- coding: utf-8 -*-

import csv  
import sys
import numpy
import scipy.io
import os

for filename in os.listdir(os.getcwd()):
    if filename.endswith(".CSV"): 
        idno = filename.split('.')[0]
      
        data = [ ]
        reader = csv.reader(filename)
        
        for row in reader:
            print row
            rowData = [ float(elem) for elem in row ]
            data.append(rowData)

        matrix = numpy.array(data)
        scipy.io.savemat(idno+'.mat', {'csvmatrix':matrix})