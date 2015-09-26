# -*- coding: utf-8 -*-
"""
Created on Tue Sep 08 11:56:46 2015

@author: rajat
"""

"""
Simple demo of a horizontal bar chart.
"""

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


# Example data
fields = ('Systems', 'Compuatational', 'Cognitive', 'Molecular', 'Behavioral')
y_pos = np.arange(len(fields))
performance = 3 + 10 * np.random.rand(len(fields))
error = np.random.rand(len(fields))

plt.barh(y_pos, performance, xerr=error, align='center', alpha=0.4)
plt.yticks(y_pos, fields)
plt.xlabel('Performance')
plt.title('Which field?')

plt.show()