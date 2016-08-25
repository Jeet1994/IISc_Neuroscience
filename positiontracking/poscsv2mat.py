import csv
import scipy.io as sio

x1 = []
y1 = []
with open('day2.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    #print fum, x1, y1
    for row in reader:
	x1.append(int(row[1]))
	y1.append(int(row[2]))

sio.savemat('Day2_cam1_output_2016-07-30 12_13_58 257633.mat', mdict={'red_x':x1, 'red_y':y1})
