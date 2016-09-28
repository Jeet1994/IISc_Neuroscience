# -*- coding: utf-8 -*-

import csv
import scipy.io as sio
import os

for filename in os.listdir(os.getcwd()):
    if filename.endswith(".CSV"):
        time = []
        data = []

        with open(filename) as csvfile:
            for i in range(17):
                csvfile.next()
            reader = csv.reader(csvfile, delimiter=',')
            next(reader, 10)
            for row in reader:
                time.append(float(row[3]))
                data.append(float(row[4]))
        fname = filename.split('.')[0]
        sio.savemat(fname + '.mat', mdict={'time':time,'data':data})