# -*- coding: utf-8 -*-
"""
Created on Mon Sep 07 20:08:07 2015

@author: rajat
"""

"""
In addition to the basic pie chart, this demo shows a few optional features:

    * slice labels
    * auto-labeling the percentage
    * offsetting a slice with "explode"
    * drop-shadow
    * custom start angle

Note about the custom start angle:

The default ``startangle`` is 0, which would start the "System Neuroscience" slice on the
positive x-axis. This example sets ``startangle = 90`` such that everything is
rotated counter-clockwise by 90 degrees, and the System Neuroscience slice starts on the
positive y-axis.
"""
from matplotlib import pyplot as plt
from matplotlib import font_manager as fm

fig = plt.figure(1, figsize=(6,6))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
plt.title('Neuroscience Divisions')

labels = 'Systems', 'Cognitive', 'Molecular', 'Computational'
fracs = [15,30,45, 10]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
explode = (0, 0.1, 0, 0) # only "explode" the 2nd slice

patches, texts, autotexts = ax.pie(fracs, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)

proptease = fm.FontProperties()
proptease.set_size('xx-small')
plt.setp(autotexts, fontproperties=proptease)
plt.setp(texts, fontproperties=proptease)

plt.show()