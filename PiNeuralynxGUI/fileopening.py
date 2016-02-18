# -*- coding: utf-8 -*-
"""
Created on Wed Jan 06 18:28:36 2016

@author: rajat
"""
import sys
from PyQt4.QtGui import *
    
def openfile():
    
    a = QApplication(sys.argv)
    w = QWidget()
    
    # Get filename using QFileDialog
    filename = QFileDialog.getOpenFileName(w, 'Open File', '/')     
    
    return filename