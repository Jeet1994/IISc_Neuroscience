
# coding: utf-8

from lynxio import *
import matplotlib.pyplot as plt
import scipy.io as sio
import numpy as np
import os
from math import log10

def custom_fft(datapoints, frequency, Fs=30000.0):
    
    #constants 
    fs = Fs
    N = float(len(datapoints))
    
    #fourier transform
    X = np.fft.fftshift(np.fft.fft2(datapoints)) ##fft2: 2d discrete fourier transform
    
    #frequency specification
    dF = fs/N
    f = np.arange(-fs/2, fs/2-dF, dF)
    
    X =X[:len(f)] #small hack for length adjustment
    
    #plotting the spectrum 
    plt.plot(f,np.abs(X)/N)
    plt.xlabel('Frequency (in hertz)');
    plt.title('Magnitude Response');
   
    return max(np.abs(X)/N)



plt.figure(figsize=(30,17))

for filename in os.listdir(os.getcwd()):
    if filename.endswith(".ncs") and filename.startswith("CSC"): 
        channelname = filename.split('.')[0]
        plotname = channelname +'FFT.png'
                
        csc = loadNcs(filename)
        eventTimestamps, eventId, nttl, eventNames = loadNev('Events.nev')
        
        samplingRate = float(csc[1]['freq'][0])
        
        print eventNames
        
        datapointsbaseline = fileSplitterUsingEvents(csc, eventTimestamps[1], eventNames[1], eventTimestamps[2], eventNames[2])
        datapoints1e1hz = fileSplitterUsingEvents(csc, eventTimestamps[3], eventNames[3], eventTimestamps[4], eventNames[4])    
        datapoints3hz = fileSplitterUsingEvents(csc, eventTimestamps[5], eventNames[5], eventTimestamps[6], eventNames[6])  
        datapoints8hz = fileSplitterUsingEvents(csc, eventTimestamps[7], eventNames[7], eventTimestamps[8], eventNames[8])
        datapoints30hz = fileSplitterUsingEvents(csc, eventTimestamps[9], eventNames[9], eventTimestamps[10], eventNames[10])
        datapoints100hz = fileSplitterUsingEvents(csc, eventTimestamps[11], eventNames[11], eventTimestamps[12], eventNames[12])
        datapoints1khz = fileSplitterUsingEvents(csc, eventTimestamps[13], eventNames[13], eventTimestamps[14], eventNames[14])
        datapoints5khz = fileSplitterUsingEvents(csc, eventTimestamps[15], eventNames[15], eventTimestamps[16], eventNames[16])
        datapoints9khz = fileSplitterUsingEvents(csc, eventTimestamps[17], eventNames[17], eventTimestamps[18], eventNames[18])
        
        min_length = min(len(datapointsbaseline), len(datapoints1e1hz), len(datapoints3hz),  len(datapoints8hz),  len(datapoints30hz),  
                         len(datapoints100hz),  len(datapoints1khz), len(datapoints5khz),  len(datapoints9khz))
        
        datapointsbaseline = datapointsbaseline[:min_length]
        datapoints1e1hz = datapoints1e1hz[:min_length]
        datapoints3hz = datapoints3hz[:min_length]
        datapoints8hz = datapoints8hz[:min_length]
        datapoints30hz = datapoints30hz[:min_length]
        datapoints100hz = datapoints100hz[:min_length]
        datapoints1khz = datapoints1khz[:min_length]
        datapoints5khz = datapoints5khz[:min_length]
        datapoints9khz = datapoints9khz[:min_length]
        
        #sio.savemat(channelname + '_data.mat', {'datapointsbaseline':datapointsbaseline, 'datapoints1e1hz':datapoints1e1hz, 'datapoints3hz':datapoints3hz, 'datapoints8hz':datapoints8hz, 'datapoints30hz':datapoints30hz, 'datapoints100hz':datapoints100hz, 'datapoints1khz':datapoints1khz, 'datapoints5khz':datapoints5khz, 'datapoints9khz':datapoints9khz})
        
        dataFFT = [custom_fft(datapoints1e1hz, 0.1, samplingRate), custom_fft(datapoints3hz, 3, samplingRate), custom_fft(datapoints8hz, 8, samplingRate), custom_fft(datapoints30hz, 30, samplingRate), custom_fft(datapoints100hz, 100, samplingRate), 
                   custom_fft(datapoints1khz, 1000, samplingRate), custom_fft(datapoints5khz, 5000, samplingRate), custom_fft(datapoints9khz, 9000, samplingRate)]
        
        baselinepostFFT = custom_fft(datapointsbaseline, 0) 
        
        #plotting part
        x=[log10(0.1),log10(3),log10(8),log10(30),log10(100),log10(1000),log10(5000),log10(9000)]
        labels = ['0.1','3','8','30','100','1000', '5000', '9000']
        plt.xticks(x, labels, fontsize = 16, fontweight = 'bold',rotation = 90)
        plt.yticks(fontsize = 16, fontweight = 'bold')
        plt.ylabel('Amplitude(uV) after norm',fontsize = 10, fontweight = 'bold')
        plt.xlabel('Log Freq(hz)',fontsize = 10, fontweight = 'bold')
        plt.axhline(y=baselinepostFFT, xmin=0, xmax=10, hold=None, color='red')
        plt.plot(x,dataFFT, 'b--o')   
        plt.savefig(plotname)
        plt.clf()
        plt.close()