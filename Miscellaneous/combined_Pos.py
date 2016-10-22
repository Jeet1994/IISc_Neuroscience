# -*- coding: utf-8 -*-
"""
Created on Fri Mar 04 12:06:21 2016

@author: rajat
"""

from datetime import datetime, timedelta

camera1PosData = open('cam1.txt','r')
camera2PosData = open('cam2.txt', 'r')
camera3PosData = open('cam3.txt', 'r')
camera4PosData = open('cam4.txt', 'r')
camera5PosData = open('cam5.txt','r')
camera6PosData = open('cam6.txt', 'r')
camera7PosData = open('cam7.txt', 'r')
camera8PosData = open('cam8.txt', 'r')

combinedPosFile = open('combinedPos.txt','w')

camera1TimestampData = open('cam1_timestamp.txt','r')

TimestamppicamData = []
TimestamppythonData = []

for line in camera1TimestampData:
    c1Timestamp = line.split(',')
    c1picamTime, c1pythonTime  = timedelta(microseconds= float(c1Timestamp[0])), datetime.strptime(c1Timestamp[1].rstrip('\n').split(' ')[1],'%H:%M:%S.%f').time()
    c1pythonTime = timedelta(hours=c1pythonTime.hour, minutes=c1pythonTime.minute, seconds=c1pythonTime.second, microseconds=c1pythonTime.microsecond)
    TimestamppicamData.append(c1picamTime)
    TimestamppythonData.append(c1pythonTime)

camera1Position = []
camera2Position = []
camera3Position = []
camera4Position = []
camera5Position = []
camera6Position = []
camera7Position = []
camera8Position = []

for line in camera1PosData:
    line = line.rstrip('\n')
    line = line.split(' ')
    x = line[0]
    y = line[1]
    z = (int(x), int(y))
    camera1Position.append(z)

for line in camera2PosData:
    line = line.rstrip('\n')
    line = line.split(' ')
    x = line[0]
    y = line[1]
    z = (int(x), int(y))
    camera2Position.append(z)

for line in camera3PosData:
    line = line.rstrip('\n')
    line = line.split(' ')
    x = line[0]
    y = line[1]
    z = (int(x), int(y))
    camera3Position.append(z)

for line in camera4PosData:
    line = line.rstrip('\n')
    line = line.split(' ')
    x = line[0]
    y = line[1]
    z = (int(x), int(y))
    camera4Position.append(z)

for line in camera5PosData:
    line = line.rstrip('\n')
    line = line.split(' ')
    x = line[0]
    y = line[1]
    z = (int(x), int(y))
    camera5Position.append(z)
    
for line in camera6PosData:
    line = line.rstrip('\n')
    line = line.split(' ')
    x = line[0]
    y = line[1]
    z = (int(x), int(y))
    camera6Position.append(z)

for line in camera7PosData:
    line = line.rstrip('\n')
    line = line.split(' ')
    x = line[0]
    y = line[1]
    z = (int(x), int(y))
    camera7Position.append(z)

for line in camera8PosData:
    line = line.rstrip('\n')
    line = line.split(' ')
    x = line[0]
    y = line[1]
    z = (int(x), int(y))
    camera8Position.append(z)

for ts1,ts2,pos1,pos2,pos3,pos4,pos5,pos6,pos7,pos8 in map(None,TimestamppicamData,TimestamppythonData, camera1Position,camera2Position,camera3Position,camera4Position,camera5Position,camera6Position,camera7Position,camera8Position):    
    combinedPosFile.write(str(ts1) + "," + str(ts2) + "," + str(pos1) + "," + str(pos2) + ","+ str(pos3) + "," + str(pos4) + "," + str(pos5) + "," + str(pos6) + "," + str(pos7) + "," + str(pos8)+"\n")
                                          
combinedPosFile.close()
camera1PosData.close()
camera2PosData.close()
camera3PosData.close()
camera4PosData.close()
camera5PosData.close()
camera6PosData.close()
camera7PosData.close()
camera8PosData.close()
