#!/usr/bin/env python
## Setup Section
from psychopy import visual, event, data, logging
import random, datetime, time
 
## Setup section
# experiment specific
#win = visual.Window([400,400], units='height', winType='pyglet', fullscr=True)
win = visual.Window([400,400], units='height', winType='pyglet')
width = float(win.size[0])/win.size[1] # actual width in units of height
logging.console.setLevel(logging.WARNING) # default, only Errors and Warnings are shown on the console
# run  specific
fileName = "data/simon"+datetime.datetime.now().strftime("%Y-%m-%dT%H_%M_%S")+".dat"
dataFile = open(fileName, 'w') # note that MS Excel has only ASCII .csv, other spreadsheets do support UTF-8
dataFile.write("#{}, {}, {}\n".format("position", "time", "response"))
 
 
instruction = visual.TextStim(win, 
        text='Press ← if you see a rectangle left of the fixation cross. '\
        'Press → if you see one on the right. Press Escape to stop the '\
        'experiment, or continue to the end. It takes about a minute.'.decode("utf-8") 
    )
# fixation cross
fixation = visual.ShapeStim(win, 
        vertices=((0, -3), (0, 3), (0,0), (-3,0), (3, 0)),
        lineWidth=10,
        size=.01,
        closeShape=False,
        lineColor='blue'
    )
 
# stimulus rectangle
stimulus = visual.Rect(win, 
        width     = 0.1,
        height    = 0.1,
        fillColor = 'red',
        lineColor = 'red'
    )
 
## Experiment section
for i in range(50):
    # fixation
    fixation.draw()
    win.flip()
    presses = event.waitKeys(1.0)
    if presses and presses[0] == 'escape':
        break
 
    # stimulus
    x = -(width-0.1)/2 +(width-0.1)*random.random()
    stimulus.setPos((x, 0))
    stimulus.draw()
    win.flip()
    timeBefore = time.time()
    presses = event.waitKeys(3) # wait a maximum of 3 seconds for keyboard input
    timeAfter = time.time()
     
    #handle keypress
    if not presses:
        # no keypress
        print "none"
        p = 0
    elif presses[0]=="left":
        p = -1
    elif presses[0]=="right":
        p = 1
    elif presses[0]=="escape":
        break
    else:
        # some other keypress
        print "other"
        p = 0
    dataFile.write("{}, {}, {}\n".format(x, timeAfter-timeBefore, p))
    #print x, timeAfter-timeBefore, p
 
## Cleanup section
win.close()
core.quit()