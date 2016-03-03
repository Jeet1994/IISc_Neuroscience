#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def loadNVT(filename):
    f = open(filename, 'rb')	
    header = str(f.read(2 ** 14)).strip('\x00')
    dt = np.dtype([('swstx', np.uint16), ('swid', np.uint16), ('swdata_size', np.uint16),
                ('qwTimestamp', np.uint64), ('dwPoints', np.int32, (512,)), ('sncrc', np.int16), 
                ('extractedX', np.int32 ), ('extractedY', np.int32), ('extractedAngle', np.int32),
                ('dwTargets', np.int32, (50,))])


    temp = np.fromfile(f, dt)

    return temp


data =  loadNVT('VT1.nvt') 
print data[0]
