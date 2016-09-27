import scipy.io as sio
import os 

red_x = []
red_y = []
green_x = []
green_y = []

for filename in os.listdir(os.getcwd()):
    if filename.endswith(".txt"):
        f = open(filename)
        for line in f:
            line = line.rstrip("\n").split(" ")
            redx, redy, greenx, greeny = int(line[0]), int(line[1]), int(line[2]), int(line[3])
            #print redx, redy, greenx, greeny
            red_x.append(redx)
            red_y.append(redy)
            green_x.append(greenx)
            green_y.append(greeny)
            
        matFileName = filename.split('.txt')[0] + '.mat'
            
        sio.savemat(matFileName, mdict={'red_x': red_x, 'red_y': red_y, 'green_x':green_x, 'green_y': green_y})           