# -*- coding: utf-8 -*-
"""
Created on Wed Oct 05 16:28:44 2016

@author: rajat
"""

import re
import math
import scipy.io as sio

combinedPosFile = open('combinedPos.txt','r')

r = re.compile(r'(?:[^,(]|\([^)]*\))+')
     
posData = []
     
for line in combinedPosFile:
     line.rsplit('\n')
     line = r.findall(line)
     data = [eval(line[2]), eval(line[3]), eval(line[4]), eval(line[5]), eval(line[6]), eval(line[7]), eval(line[8]), eval(line[9])]
     posData.append(data)

red_x = []
red_y = []

for pos in posData:
    pos_x = -1
    pos_y = -1
    if pos[0] != (-1,-1):
        pos_x = math.ceil((pos[0][0] + 1045.0)/2.0)
        pos_y = (pos[0][1] + 408.0)
    elif pos[3] != (-1,-1):
        pos_x = math.ceil((pos[3][0])/2.0)
        pos_y = (pos[3][1] + 400.0)
    elif pos[4] != (-1,-1):
        pos_x = math.ceil((pos[4][0] + 1065.0)/2.0)
        pos_y = (pos[4][1] + 38.0)
    elif pos[5] != (-1,-1):
        pos_x = math.ceil((pos[5][0] + 705.0)/2.0)
        pos_y = (pos[5][1] + 40.0)
    elif pos[6] != (-1,-1):
        pos_x = math.ceil((pos[6][0] + 400.0)/2.0)
        pos_y = (pos[6][1] + 28.0)
    elif pos[7] != (-1,-1):
        pos_x = math.ceil((pos[7][0] + 65.0)/2.0)
        pos_y = pos[7][1]
    elif pos[1] != (-1,-1):
        pos_x = math.ceil((pos[1][0] + 780.0)/2.0)
        pos_y = (pos[1][1] + 419.0)
    elif pos[2] != (-1,-1):
        pos_x = math.ceil((pos[2][0] + 390.0)/2.0)
        pos_y = (pos[2][1] + 418.0)
    else:
        pos_x = -1
        pos_y = -1
    if pos_y>830:
        pos_y = pos_y - 100
    red_x.append(int(pos_x))
    red_y.append(int(pos_y))
    
sio.savemat("Day21_Pos.mat",mdict={'red_x':red_x, 'red_y':red_y})