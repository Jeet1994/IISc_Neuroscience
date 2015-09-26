#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.70.01), September 08, 2015, at 16:34
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'psychophysicsStaircase'  # from the Builder filename that created this script
expInfo = {'participant':'s_001', 'ori':10}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\user1\\Desktop\\psychopy_neuro-master\\Lesson_plan_Psychopy\\visneuro_demo\\PsychoPy2 Demos\\psychophysicsStaircase\\psychophysicsStaircase.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1920, 1080), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "instr"
instrClock = core.Clock()
instructions = visual.TextStim(win=win, ori=0, name='instructions',
    text="This exp measures your detection threshold using a staircase procedure.\n\nPress 'up' if you see the stimulus, 'down' if you didn't.\n\nAny key to start",    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
fixation = visual.GratingStim(win=win, name='fixation',units='pix', 
    tex=None, mask=None,
    ori=0, pos=[0, 0], size=[3, 3], sf=1, phase=0.0,
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=0.0)
gabor = visual.GratingStim(win=win, name='gabor',units='pix', 
    tex='sin', mask='gauss',
    ori=expInfo['ori'], pos=[0, 0], size=[128,128], sf=0.1, phase=1.0,
    color=1.0, colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-1.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "instr"-------
t = 0
instrClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
ready = event.BuilderKeyResponse()  # create an object of type KeyResponse
ready.status = NOT_STARTED
# keep track of which components have finished
instrComponents = []
instrComponents.append(instructions)
instrComponents.append(ready)
for thisComponent in instrComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instrClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions* updates
    if t >= 0 and instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions.tStart = t  # underestimates by a little under one frame
        instructions.frameNStart = frameN  # exact frame index
        instructions.setAutoDraw(True)
    
    # *ready* updates
    if t >= 0 and ready.status == NOT_STARTED:
        # keep track of start time/frame for later
        ready.tStart = t  # underestimates by a little under one frame
        ready.frameNStart = frameN  # exact frame index
        ready.status = STARTED
        # keyboard checking is just starting
        ready.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if ready.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            ready.keys = theseKeys[-1]  # just the last key pressed
            ready.rt = ready.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instr"-------
for thisComponent in instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if ready.keys in ['', [], None]:  # No response was made
   ready.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('ready.keys',ready.keys)
if ready.keys != None:  # we had a response
    thisExp.addData('ready.rt', ready.rt)
thisExp.nextEntry()
# the Routine "instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#--------Prepare to start Staircase "trials" --------
# set up handler to look after next chosen value etc
trials = data.StairHandler(startVal=0.5, extraInfo=expInfo,
    stepSizes=asarray([0.8,0.8,0.4,0.4,0.2]), stepType='log',
    nReversals=0, nTrials=30.0, 
    nUp=1, nDown=3,
    minVal=0.0, maxVal=1.0,
    originPath='C:\\Users\\user1\\Desktop\\psychopy_neuro-master\\Lesson_plan_Psychopy\\visneuro_demo\\PsychoPy2 Demos\\psychophysicsStaircase\\psychophysicsStaircase.psyexp', name='trials')
thisExp.addLoop(trials)  # add the loop to the experimentlevel = thisTrial = 0.5  # initialise some vals

for thisTrial in trials:
    currentLoop = trials
    level = thisTrial
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    gabor.setColor([level, level, level], colorSpace='rgb')
    resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    resp.status = NOT_STARTED
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(fixation)
    trialComponents.append(gabor)
    trialComponents.append(resp)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation* updates
        if t >= 0.0 and fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation.tStart = t  # underestimates by a little under one frame
            fixation.frameNStart = frameN  # exact frame index
            fixation.setAutoDraw(True)
        if fixation.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            fixation.setAutoDraw(False)
        
        # *gabor* updates
        if t >= 0.5 and gabor.status == NOT_STARTED:
            # keep track of start time/frame for later
            gabor.tStart = t  # underestimates by a little under one frame
            gabor.frameNStart = frameN  # exact frame index
            gabor.setAutoDraw(True)
        if gabor.status == STARTED and t >= (0.5 + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            gabor.setAutoDraw(False)
        if gabor.status == STARTED:  # only update if being drawn
            gabor.setPhase(trialClock.getTime()*2, log=False)
        
        # *resp* updates
        if t >= 0.5 and resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp.tStart = t  # underestimates by a little under one frame
            resp.frameNStart = frameN  # exact frame index
            resp.status = STARTED
            # keyboard checking is just starting
            resp.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if resp.status == STARTED and t >= (0.5 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            resp.status = STOPPED
        if resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['up', 'down'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                resp.keys = theseKeys[-1]  # just the last key pressed
                resp.rt = resp.clock.getTime()
                # was this 'correct'?
                if (resp.keys == str('up')) or (resp.keys == 'up'):
                    resp.corr = 1
                else:
                    resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if resp.keys in ['', [], None]:  # No response was made
       resp.keys=None
       # was no response the correct answer?!
       if str('up').lower() == 'none': resp.corr = 1  # correct non-response
       else: resp.corr = 0  # failed to respond (incorrectly)
    # store data for trials (StairHandler)
    trials.addResponse(resp.corr)
    trials.addOtherData('resp.rt', resp.rt)
    thisExp.nextEntry()
    
# staircase completed

trials.saveAsExcel(filename + '.xlsx', sheetName='trials')
win.close()
core.quit()
