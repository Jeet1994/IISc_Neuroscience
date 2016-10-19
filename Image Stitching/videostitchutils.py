import numpy as np
from datetime import timedelta

def load_timestamps(filename):
    times = []
    with open(filename) as f:
        for line in f:
            timestamp = line.split(',')[0]
            times.append(timedelta(microseconds=float(timestamp)))
    f.close()
    return times


def getStitchedImage(image1, image2, image3, image4, image5, image6, image7, image8):
    return image1+image2+image3+image4+image5+image6+image7+image8

