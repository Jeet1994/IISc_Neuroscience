# -*- coding: utf-8 -*-
"""
Created on Wed Jan 06 18:40:42 2016

@author: rajat
"""

#TODO
#-> CSC file which you want to edit
#-> event file which you want to load
#-> layout

import sys
import os
import lynxio
import fileopening
from PyQt4.QtGui import *
from PyQt4.QtCore import * 

def main(): 
    app = QApplication(sys.argv) 
    w = PiNeuralynx() 
    w.show() 
    sys.exit(app.exec_()) 
 
class PiNeuralynx(QWidget): 
    def __init__(self, *args): 
        QWidget.__init__(self, *args) 
 
        cscLabel = QLabel(self.tr("Enter CSC file path"))
        self.cscFileAddress = QLineEdit()
        self.cscFileSearchButton = QPushButton("v")
        
        eventLabel = QLabel(self.tr("Enter CSC file path"))
        self.nevFileAddress = QLineEdit()
        self.nevFileSearchButton = QPushButton("v")
        
        self.loadFilesButton = QPushButton("Next>>")
        
        # layout
        layout = QVBoxLayout(self)
        
        layout.addWidget(cscLabel)
        layout.addWidget(self.cscFileAddress)
        layout.addWidget(self.cscFileSearchButton)
        
        layout.addWidget(eventLabel)
        layout.addWidget(self.nevFileAddress)
        layout.addWidget(self.nevFileSearchButton)
        
        self.setLayout(layout) 

        # create connection
       # self.connect(self.le, SIGNAL("returnPressed(void)"),
        #             self.run_command)

    def run_command(self):
        cmd = str(self.le.text())
        stdouterr = os.popen4(cmd)[1].read()
        self.te.setText(stdouterr)
  
if __name__ == "__main__": 
    main()