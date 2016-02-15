#TODO:
#--> have to convert seconds, microseconds.... recheck conversion... debug at each step

from dateutil.parser import parse
from datetime import datetime

camera1TimestampData = open('camera1.txt','r')
camera2TimestampData = open('camera2.txt', 'r')
camera3TimestampData = open('camera3.txt', 'r')
#camera4TimestampData = open('camera4.txt', 'r')

combinedTimestampFile = open('combinedTimestamp.txt','w')

camera1InterruptTimestamp = []
camera2InterruptTimestamp = []
camera3InterruptTimestamp = []
#camera4InterruptTimestamp = []

camera1Timestamps = camera1TimestampData.readline().split(',')
camera2Timestamps = camera2TimestampData.readline().split(',')
camera3Timestamps = camera3TimestampData.readline().split(',')
#camera4Timestamps = camera4TimestampData.readline().split(',')

camera1AbsoluteTimestamp = parse(camera1Timestamps[1])
camera2AbsoluteTimestamp = parse(camera2Timestamps[1])
camera3AbsoluteTimestamp = parse(camera3Timestamps[1])
#camera4AbsoluteTimestamp = parse(camera4Timestamps[1])

camera1AbsoluteTimestamp = (camera1AbsoluteTimestamp - datetime.utcfromtimestamp(0)).total_seconds()
camera2AbsoluteTimestamp = (camera2AbsoluteTimestamp - datetime.utcfromtimestamp(0)).total_seconds()
camera3AbsoluteTimestamp = (camera3AbsoluteTimestamp - datetime.utcfromtimestamp(0)).total_seconds()
#camera4AbsoluteTimestamp = (minimumFirstFrameTimestamp - datetime.utcfromtimestamp(0)).total_seconds()

minimumFirstFrameTimestamp = min(camera1AbsoluteTimestamp, camera2AbsoluteTimestamp, camera3AbsoluteTimestamp)

relativeC1FirstTimestamp = (camera1AbsoluteTimestamp - minimumFirstFrameTimestamp)
relativeC2FirstTimestamp = (camera2AbsoluteTimestamp - minimumFirstFrameTimestamp)
relativeC3FirstTimestamp = (camera3AbsoluteTimestamp - minimumFirstFrameTimestamp)
#relativeC4C1FirstTimestamp = camera4AbsoluteTimestamp - minimumFirstFrameTimestamp

camera1InterruptTimestamp.append(relativeC1FirstTimestamp)
camera2InterruptTimestamp.append(relativeC2FirstTimestamp)
camera3InterruptTimestamp.append(relativeC3FirstTimestamp)
#camera4InterruptTimestamp.append(relativeC4FirstTimestamp)

for line in camera1TimestampData:
    c1Timestamp = line.split(',')[0]
    if c1Timestamp is None:
        continue
    else:
        c1Timestamp = float(c1Timestamp) + relativeC1FirstTimestamp
    camera1InterruptTimestamp.append(c1Timestamp)

for line in camera2TimestampData:
    c2Timestamp = line.split(',')[0]
    if c2Timestamp is None:
        continue
    else:
        c2Timestamp = float(c2Timestamp) + relativeC2FirstTimestamp
    camera2InterruptTimestamp.append(c2Timestamp)

for line in camera3TimestampData:
    c3Timestamp = line.split(',')[0]
    if c3Timestamp is None:
        continue
    else:
        c3Timestamp = float(c3Timestamp) + relativeC3FirstTimestamp
    camera3InterruptTimestamp.append(c3Timestamp)

#for line in camera4TimestampData:
#    c4Timestamp = line.split(',')[0]
#    if c4Timestamp is None:
#        continue
#    else:
#        c4Timestamp = c4Timestamp + relativeC4C1FirstTimestamp
#    camera4InterruptTimestamp.append(c4Timestamp)

for ts1, ts2, ts3 in map(None, camera1InterruptTimestamp,camera2InterruptTimestamp,camera3InterruptTimestamp):
    combinedTimestampFile.write(str(ts1) + "," + str(ts2) + "," + str(ts3) +"\n")

combinedTimestampFile.close()
camera1TimestampData.close()
camera2TimestampData.close()
camera3TimestampData.close()