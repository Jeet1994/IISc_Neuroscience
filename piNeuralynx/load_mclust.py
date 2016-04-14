#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Functions for loading spikes, clusters and LFP
'''

import numpy as np
from struct import unpack


def read_t_header(fid):
    '''Read the header of an MClust .t file
       TO DO: check beginheader and report if there is no header
    '''
    beginheader = '%%BEGINHEADER\n';
    endheader = '%%ENDHEADER\n';
    HeaderText = ''
    while True:
        line=fid.readline()
        HeaderText += line
        if line==endheader:
            break
    DataPosition = fid.tell()
    return (DataPosition,HeaderText)


def read_t(SpikesDataFileName,insec=True):
    '''Reads data from an MClust .t file.
       These files contain events/spikes data.
       Based on MClust-3.4/Matlab/SpecificUtils/ReadHeader.m
       If 'insec' is True, timestamps are given in seconds (float)
       otherwise they are given as tenths of msec (int32)
    '''
    fid = open(SpikesDataFileName,'rb')
    (DataPosition,HeaderText) = read_t_header(fid)
    fid.seek(DataPosition)
    ByteString = fid.read()
    Nsamples = len(ByteString)/4
    timestamps = np.empty(Nsamples,dtype=np.uint32)
    for inds in range(Nsamples):
        timestamps[inds] = unpack('>I', ByteString[4*inds:4*inds+4])[0]
    #timestamps = np.fromfile(fid,dtype='uint32')
    fid.close()
    if insec:
        timestamps = 1e-4*timestamps        # From 100usec to sec (see NSpike/MClust docs)
    return timestamps
