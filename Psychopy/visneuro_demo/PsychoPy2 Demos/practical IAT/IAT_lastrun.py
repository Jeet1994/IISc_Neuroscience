#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.78.01), September 08, 2015, at 16:35
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
expName = 'IAT'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u'', u'side': u'1'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\user1\\Desktop\\psychopy_neuro-master\\Lesson_plan_Psychopy\\visneuro_demo\\PsychoPy2 Demos\\practical IAT\\IAT.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1920, 1080), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1.000,-1.000,-1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
Instr = visual.TextStim(win=win, ori=0, name='Instr',
    text="In the next task, you will be presented with a set of words or images. Your job is to classify each word as quickly as you can, while making as few mistakes as possible.\r\n\r\nKeep your index fingers on the 'e' and 'i' keys. Press the 'e' key to indicate that the word belongs in the category on the left, and press the 'i' key to indicate the category on the right. \r\n\r\nThe four categories and the words that go in each category are described on the next screen.\r\n\r\nPress the spacebar to continue.",    font='Arial',
    pos=[0.03, 0], height=0.08, wrapWidth=1.2,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
if expInfo['side'] == '1': expInfo['side'] = 1
else: expInfo['side'] = -1
side = expInfo['side']
# side flips categories R/L, affects scoring

def corr(letter, side, condition):
    # reverse e/i if side is -1
    if side == 1:
      return letter
    else:
        if condition == 'bad' or condition == 'good':
            return letter
        else:
            if letter == 'e': return 'i'
            if letter == 'i': return 'e'

# Initialize components for Routine "Instr_1"
Instr_1Clock = core.Clock()
Instr_1x = visual.TextStim(win=win, ori=0, name='Instr_1x',
    text='In the first set, you will be determining if a word is "creative" or "practical" as follows:\r\n\r\n"Creative": Creative, Novel, Inventive, Newfangled, Original, Different\r\n\r\n"Practical": Practical, Applied, Useful, Functional, Efficient, Constructive\r\n\r\nPress \'e\' to sort the word into the category on the left, and \'i\' to sort it into the category on the right.\r\n\r\nIf you press the wrong key, an \'X\' will appear on the screen. You should then press the other key.\r\n\r\nPosition your index fingers over the \'e\' and \'i\' keys. Press the spacebar with your thumb to begin the trials.',    font='Arial',
    pos=[0.03, 0], height=0.08, wrapWidth=1.2,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
Instr_Creat_1 = visual.TextStim(win=win, ori=0, name='Instr_Creat_1',
    text='Creative',    font='Arial',
    pos=[0,0], height=0.15, wrapWidth=None,
    color='skyblue', colorSpace='rgb', opacity=1,
    depth=-2.0)
Instr_Prac_1 = visual.TextStim(win=win, ori=0, name='Instr_Prac_1',
    text='Practical',    font='Arial',
    pos=[0,0], height=0.15, wrapWidth=None,
    color='skyblue', colorSpace='rgb', opacity=1,
    depth=-3.0)

# Initialize components for Routine "Block_1"
Block_1Clock = core.Clock()
Creative = visual.TextStim(win=win, ori=0, name='Creative',
    text='Creative',    font='Arial',
    pos=[0,0], height=0.15, wrapWidth=None,
    color='skyblue', colorSpace='rgb', opacity=1,
    depth=0.0)
Practical = visual.TextStim(win=win, ori=0, name='Practical',
    text='Practical',    font='Arial',
    pos=[0,0], height=0.15, wrapWidth=None,
    color='skyblue', colorSpace='rgb', opacity=1,
    depth=-1.0)
Word_1 = visual.TextStim(win=win, ori=0, name='Word_1',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.15, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-2.0)

Wrong_1 = visual.TextStim(win=win, ori=0, name='Wrong_1',
    text='X',    font='Arial',
    pos=[0, -.3], height=0.1, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-6.0)

# Initialize components for Routine "Instr_2"
Instr_2Clock = core.Clock()
Instru2 = visual.TextStim(win=win, ori=0, name='Instru2',
    text='In this next set, you will be determining if a word is "good" or "bad" as follows:\r\n\r\n"Good": Rainbow, Cake, Sunshine, Laughter, Peace, Heaven\r\n\r\n"Bad": Agony, Hell, Ugly, Vomit, Poison, Rotten\r\n\r\nRemember to press \'e\' to sort the word into the category on the left, and \'i\' to sort it into the category on the right.\r\n\r\nPress the spacebar to begin the trials',    font='Arial',
    pos=[0, 0], height=0.08, wrapWidth=1.2,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
Instr_Bad = visual.TextStim(win=win, ori=0, name='Instr_Bad',
    text='Bad',    font='Arial',
    pos=[-.8, 0.8], height=0.15, wrapWidth=None,
    color='limegreen', colorSpace='rgb', opacity=1,
    depth=-2.0)
Instr_Good = visual.TextStim(win=win, ori=0, name='Instr_Good',
    text='Good',    font='Arial',
    pos=[.8, 0.8], height=0.15, wrapWidth=None,
    color='limegreen', colorSpace='rgb', opacity=1,
    depth=-3.0)

# Initialize components for Routine "Block_2"
Block_2Clock = core.Clock()
Bad = visual.TextStim(win=win, ori=0, name='Bad',
    text='Bad',    font='Arial',
    pos=[-.8, 0.8], height=0.15, wrapWidth=None,
    color='limegreen', colorSpace='rgb', opacity=1,
    depth=0.0)
Good = visual.TextStim(win=win, ori=0, name='Good',
    text='Good',    font='Arial',
    pos=[.8, 0.8], height=0.15, wrapWidth=None,
    color='limegreen', colorSpace='rgb', opacity=1,
    depth=-1.0)
Word_2 = visual.TextStim(win=win, ori=0, name='Word_2',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.15, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-2.0)

Wrong_2 = visual.TextStim(win=win, ori=0, name='Wrong_2',
    text='X',    font='Arial',
    pos=[0, -.3], height=0.1, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-6.0)

# Initialize components for Routine "Instr_3"
Instr_3Clock = core.Clock()
Instr3 = visual.TextStim(win=win, ori=0, name='Instr3',
    text="The four categories you saw separately now appear together. Remember that each item belongs to only one group. For example, if the categories 'creative' and 'good' appeared on separate sides above, picutres or words meaning 'creative' would go in the 'creative' category, not the 'good' category.\r\n\r\nCreative/Practical are labeled blue and Good/Bad are labeled green to help you identify the appropriate category.\r\n\r\nPress the spacebar to begin the next set of trials.",    font='Arial',
    pos=[0, 0], height=0.08, wrapWidth=1.2,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
Instr_Creat_3 = visual.TextStim(win=win, ori=0, name='Instr_Creat_3',
    text='Creative',    font='Arial',
    pos=[-.8*side, 0.8], height=0.15, wrapWidth=None,
    color='skyblue', colorSpace='rgb', opacity=1,
    depth=-1.0)
Instr_or_3 = visual.TextStim(win=win, ori=0, name='Instr_or_3',
    text='or',    font='Arial',
    pos=[-.8, 0.7], height=0.1, wrapWidth=None,
    color='gray', colorSpace='rgb', opacity=1,
    depth=-2.0)
Instr_Bad_3 = visual.TextStim(win=win, ori=0, name='Instr_Bad_3',
    text='Bad',    font='Arial',
    pos=[-.8, 0.6], height=0.15, wrapWidth=None,
    color='limegreen', colorSpace='rgb', opacity=1,
    depth=-3.0)
Instr_Prac_3 = visual.TextStim(win=win, ori=0, name='Instr_Prac_3',
    text='Practical',    font='Arial',
    pos=[.8*side, 0.8], height=0.15, wrapWidth=None,
    color='skyblue', colorSpace='rgb', opacity=1,
    depth=-4.0)
Instr_or_3_2 = visual.TextStim(win=win, ori=0, name='Instr_or_3_2',
    text='or',    font='Arial',
    pos=[.8, 0.7], height=0.1, wrapWidth=None,
    color='gray', colorSpace='rgb', opacity=1,
    depth=-5.0)
Instr_Good_3 = visual.TextStim(win=win, ori=0, name='Instr_Good_3',
    text='Good',    font='Arial',
    pos=[.8, 0.6], height=0.15, wrapWidth=None,
    color='limegreen', colorSpace='rgb', opacity=1,
    depth=-6.0)

# Initialize components for Routine "Block_3"
Block_3Clock = core.Clock()
Creative_3 = visual.TextStim(win=win, ori=0, name='Creative_3',
    text='Creative',    font='Arial',
    pos=[-.8*side, 0.8], height=0.15, wrapWidth=None,
    color='skyblue', colorSpace='rgb', opacity=1,
    depth=0.0)
or_3 = visual.TextStim(win=win, ori=0, name='or_3',
    text='or',    font='Arial',
    pos=[-.8, 0.7], height=0.1, wrapWidth=None,
    color='gray', colorSpace='rgb', opacity=1,
    depth=-1.0)
Bad_3 = visual.TextStim(win=win, ori=0, name='Bad_3',
    text='Bad',    font='Arial',
    pos=[-.8, 0.6], height=0.15, wrapWidth=None,
    color='limegreen', colorSpace='rgb', opacity=1,
    depth=-2.0)
Practical_3 = visual.TextStim(win=win, ori=0, name='Practical_3',
    text='Practical',    font='Arial',
    pos=[.8*side, 0.8], height=0.15, wrapWidth=None,
    color='skyblue', colorSpace='rgb', opacity=1,
    depth=-3.0)
or_2_3 = visual.TextStim(win=win, ori=0, name='or_2_3',
    text='or',    font='Arial',
    pos=[0.8,0.7], height=0.1, wrapWidth=None,
    color='gray', colorSpace='rgb', opacity=1,
    depth=-4.0)
Good_3 = visual.TextStim(win=win, ori=0, name='Good_3',
    text='Good',    font='Arial',
    pos=[0.8,0.6], height=0.15, wrapWidth=None,
    color='limegreen', colorSpace='rgb', opacity=1,
    depth=-5.0)
Word_3 = visual.TextStim(win=win, ori=0, name='Word_3',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.15, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-6.0)

Wrong_3 = visual.TextStim(win=win, ori=0, name='Wrong_3',
    text='X',    font='Arial',
    pos=[0, -.3], height=0.1, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-10.0)

# Initialize components for Routine "Instr_4"
Instr_4Clock = core.Clock()
Instr4 = visual.TextStim(win=win, ori=0, name='Instr4',
    text='Sort the same four categories again. The same rules still apply.\r\n\r\nPress the spacebar to begin the next set of trials.',    font='Arial',
    pos=[0, 0], height=0.08, wrapWidth=1.2,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
Instr_Creat_4 = visual.TextStim(win=win, ori=0, name='Instr_Creat_4',
    text='Creative',    font='Arial',
    pos=[-0.8*side,0.8], height=0.15, wrapWidth=None,
    color='skyblue', colorSpace='rgb', opacity=1,
    depth=-2.0)
Instr_or_4 = visual.TextStim(win=win, ori=0, name='Instr_or_4',
    text='or',    font='Arial',
    pos=[-0.8,0.7], height=0.1, wrapWidth=None,
    color='gray', colorSpace='rgb', opacity=1,
    depth=-3.0)
Instr_Bad_4 = visual.TextStim(win=win, ori=0, name='Instr_Bad_4',
    text='Bad',    font='Arial',
    pos=[-0.8,0.6], height=0.15, wrapWidth=None,
    color='limegreen', colorSpace='rgb', opacity=1,
    depth=-4.0)
Instr_Prac_4 = visual.TextStim(win=win, ori=0, name='Instr_Prac_4',
    text='Practical',    font='Arial',
    pos=[0.8*side,0.8], height=0.15, wrapWidth=None,
    color='skyblue', colorSpace='rgb', opacity=1,
    depth=-5.0)
Instr_or_4_2 = visual.TextStim(win=win, ori=0, name='Instr_or_4_2',
    text='or',    font='Arial',
    pos=[0.8,0.7], height=0.1, wrapWidth=None,
    color='gray', colorSpace='rgb', opacity=1,
    depth=-6.0)
Instr_Good_4 = visual.TextStim(win=win, ori=0, name='Instr_Good_4',
    text='Good',    font='Arial',
    pos=[0.8,0.6], height=0.15, wrapWidth=None,
    color='limegreen', colorSpace='rgb', opacity=1,
    depth=-7.0)

# Initialize components for Routine "Block_4"
Block_4Clock = core.Clock()
Creative_4 = visual.TextStim(win=win, ori=0, name='Creative_4',
    text='Creative',    font='Arial',
    pos=[-.8*side, 0.8], height=0.15, wrapWidth=None,
    color='skyblue', colorSpace='rgb', opacity=1,
    depth=0.0)
or_4 = visual.TextStim(win=win, ori=0, name='or_4',
    text='or',    font='Arial',
    pos=[-.8, 0.7], height=0.1, wrapWidth=None,
    color='gray', colorSpace='rgb', opacity=1,
    depth=-1.0)
Bad_4 = visual.TextStim(win=win, ori=0, name='Bad_4',
    text='Bad',    font='Arial',
    pos=[-.8, 0.6], height=0.15, wrapWidth=None,
    color='limegreen', colorSpace='rgb', opacity=1,
    depth=-2.0)
Practical_4 = visual.TextStim(win=win, ori=0, name='Practical_4',
    text='Practical',    font='Arial',
    pos=[.8*side, 0.8], height=0.15, wrapWidth=None,
    color='skyblue', colorSpace='rgb', opacity=1,
    depth=-3.0)
or_2_4 = visual.TextStim(win=win, ori=0, name='or_2_4',
    text='or',    font='Arial',
    pos=[0.8,0.7], height=0.1, wrapWidth=None,
    color='gray', colorSpace='rgb', opacity=1,
    depth=-4.0)
Good_4 = visual.TextStim(win=win, ori=0, name='Good_4',
    text='Good',    font='Arial',
    pos=[0.8,0.6], height=0.15, wrapWidth=None,
    color='limegreen', colorSpace='rgb', opacity=1,
    depth=-5.0)
Word_4 = visual.TextStim(win=win, ori=0, name='Word_4',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.15, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-6.0)

Wrong_4 = visual.TextStim(win=win, ori=0, name='Wrong_4',
    text='X',    font='Arial',
    pos=[0, -.3], height=0.1, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-10.0)

# Initialize components for Routine "Instr_5"
Instr_5Clock = core.Clock()
Instr5 = visual.TextStim(win=win, ori=0, name='Instr5',
    text='Notice above that there are only two categories and they have switched positions. The category that was previously on the right is now on the left, and the category that was on the left is now on the right. Sort the words into their appropriate categories based on these new positions.\r\n\r\nPress the spacebar to begin the next set of trials.',    font='Arial',
    pos=[0, 0], height=0.08, wrapWidth=1.2,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
Instr_Prac_5 = visual.TextStim(win=win, ori=0, name='Instr_Prac_5',
    text='Practical',    font='Arial',
    pos=[-0.8*side,0.8], height=0.15, wrapWidth=None,
    color='skyblue', colorSpace='rgb', opacity=1,
    depth=-1.0)
Instr_Creat_5 = visual.TextStim(win=win, ori=0, name='Instr_Creat_5',
    text='Creative',    font='Arial',
    pos=[0.8*side,0.8], height=0.15, wrapWidth=None,
    color='skyblue', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "Block_5"
Block_5Clock = core.Clock()
Practical_5 = visual.TextStim(win=win, ori=0, name='Practical_5',
    text='Practical',    font='Arial',
    pos=[-0.8*side,0.8], height=0.15, wrapWidth=None,
    color='skyblue', colorSpace='rgb', opacity=1,
    depth=0.0)
Creative_5 = visual.TextStim(win=win, ori=0, name='Creative_5',
    text='Creative',    font='Arial',
    pos=[0.8*side,0.8], height=0.15, wrapWidth=None,
    color='skyblue', colorSpace='rgb', opacity=1,
    depth=-1.0)
Word_5 = visual.TextStim(win=win, ori=0, name='Word_5',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.15, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-2.0)

Wrong_5 = visual.TextStim(win=win, ori=0, name='Wrong_5',
    text='X',    font='Arial',
    pos=[0, -.3], height=0.1, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-6.0)

# Initialize components for Routine "Instr_6"
Instr_6Clock = core.Clock()
Instr6 = visual.TextStim(win=win, ori=0, name='Instr6',
    text='See above, the four categories now appear together in a new configuration. Remember that each item belongs to only one group.',    font='Arial',
    pos=[0, 0], height=0.08, wrapWidth=1.2,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
Instr_Prac_6 = visual.TextStim(win=win, ori=0, name='Instr_Prac_6',
    text='Practical',    font='Arial',
    pos=[-0.8*side,0.8], height=0.15, wrapWidth=None,
    color='skyblue', colorSpace='rgb', opacity=1,
    depth=-1.0)
Instr_or_6 = visual.TextStim(win=win, ori=0, name='Instr_or_6',
    text='or',    font='Arial',
    pos=[-0.8,0.7], height=0.1, wrapWidth=None,
    color='gray', colorSpace='rgb', opacity=1,
    depth=-2.0)
Instr_Bad_6 = visual.TextStim(win=win, ori=0, name='Instr_Bad_6',
    text='Bad',    font='Arial',
    pos=[-0.8,0.6], height=0.15, wrapWidth=None,
    color='limegreen', colorSpace='rgb', opacity=1,
    depth=-3.0)
Instr_Creat_6 = visual.TextStim(win=win, ori=0, name='Instr_Creat_6',
    text='Creative',    font='Arial',
    pos=[0.8*side,0.8], height=0.15, wrapWidth=None,
    color='skyblue', colorSpace='rgb', opacity=1,
    depth=-4.0)
Instr_or_6_2 = visual.TextStim(win=win, ori=0, name='Instr_or_6_2',
    text='or',    font='Arial',
    pos=[0.8,0.7], height=0.1, wrapWidth=None,
    color='gray', colorSpace='rgb', opacity=1,
    depth=-5.0)
Instr_Good_6 = visual.TextStim(win=win, ori=0, name='Instr_Good_6',
    text='Good',    font='Arial',
    pos=[0.8,0.6], height=0.15, wrapWidth=None,
    color='limegreen', colorSpace='rgb', opacity=1,
    depth=-6.0)

# Initialize components for Routine "Block_6"
Block_6Clock = core.Clock()
Practical_6 = visual.TextStim(win=win, ori=0, name='Practical_6',
    text='Practical',    font='Arial',
    pos=[-0.8*side,0.8], height=0.15, wrapWidth=None,
    color='skyblue', colorSpace='rgb', opacity=1,
    depth=0.0)
or_6 = visual.TextStim(win=win, ori=0, name='or_6',
    text='or',    font='Arial',
    pos=[-0.8,0.7], height=0.1, wrapWidth=None,
    color='gray', colorSpace='rgb', opacity=1,
    depth=-1.0)
Bad_6 = visual.TextStim(win=win, ori=0, name='Bad_6',
    text='Bad',    font='Arial',
    pos=[-0.8,0.6], height=0.15, wrapWidth=None,
    color='limegreen', colorSpace='rgb', opacity=1,
    depth=-2.0)
Creative_6 = visual.TextStim(win=win, ori=0, name='Creative_6',
    text='Creative',    font='Arial',
    pos=[0.8*side,0.8], height=0.15, wrapWidth=None,
    color='skyblue', colorSpace='rgb', opacity=1,
    depth=-3.0)
or_2_6 = visual.TextStim(win=win, ori=0, name='or_2_6',
    text='or',    font='Arial',
    pos=[0.8,0.7], height=0.1, wrapWidth=None,
    color='gray', colorSpace='rgb', opacity=1,
    depth=-4.0)
Good_6 = visual.TextStim(win=win, ori=0, name='Good_6',
    text='Good',    font='Arial',
    pos=[0.8,0.6], height=0.15, wrapWidth=None,
    color='limegreen', colorSpace='rgb', opacity=1,
    depth=-5.0)
Word_6 = visual.TextStim(win=win, ori=0, name='Word_6',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.15, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-6.0)

Wrong_6 = visual.TextStim(win=win, ori=0, name='Wrong_6',
    text='X',    font='Arial',
    pos=[0, -.3], height=0.1, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-10.0)

# Initialize components for Routine "Instr_7"
Instr_7Clock = core.Clock()
Instr7 = visual.TextStim(win=win, ori=0, name='Instr7',
    text='Sort the same four categories again. The same rules still apply.\r\n\r\nPress the spacebar to begin the next set of trials.',    font='Arial',
    pos=[0, 0], height=0.08, wrapWidth=1.2,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
Instr_Prac_7 = visual.TextStim(win=win, ori=0, name='Instr_Prac_7',
    text='Practical',    font='Arial',
    pos=[-0.8*expInfo['side'],0.8], height=0.15, wrapWidth=None,
    color='skyblue', colorSpace='rgb', opacity=1,
    depth=-2.0)
Instr_or_7 = visual.TextStim(win=win, ori=0, name='Instr_or_7',
    text='or',    font='Arial',
    pos=[-0.8,0.7], height=0.1, wrapWidth=None,
    color='gray', colorSpace='rgb', opacity=1,
    depth=-3.0)
Instr_Bad_7 = visual.TextStim(win=win, ori=0, name='Instr_Bad_7',
    text='Bad',    font='Arial',
    pos=[-0.8,0.6], height=0.15, wrapWidth=None,
    color='limegreen', colorSpace='rgb', opacity=1,
    depth=-4.0)
Instr_Creat_7 = visual.TextStim(win=win, ori=0, name='Instr_Creat_7',
    text='Creative',    font='Arial',
    pos=[0.8*side,0.8], height=0.15, wrapWidth=None,
    color='skyblue', colorSpace='rgb', opacity=1,
    depth=-5.0)
Instr_or_7_2 = visual.TextStim(win=win, ori=0, name='Instr_or_7_2',
    text='or',    font='Arial',
    pos=[0.8,0.7], height=0.1, wrapWidth=None,
    color='gray', colorSpace='rgb', opacity=1,
    depth=-6.0)
Instr_Good_7 = visual.TextStim(win=win, ori=0, name='Instr_Good_7',
    text='Good',    font='Arial',
    pos=[0.8,0.6], height=0.15, wrapWidth=None,
    color='limegreen', colorSpace='rgb', opacity=1,
    depth=-7.0)

# Initialize components for Routine "Block_7"
Block_7Clock = core.Clock()
Practical_7 = visual.TextStim(win=win, ori=0, name='Practical_7',
    text='Practical',    font='Arial',
    pos=[-0.8*side,0.8], height=0.15, wrapWidth=None,
    color='skyblue', colorSpace='rgb', opacity=1,
    depth=0.0)
or_7 = visual.TextStim(win=win, ori=0, name='or_7',
    text='or',    font='Arial',
    pos=[-0.8,0.7], height=0.1, wrapWidth=None,
    color='gray', colorSpace='rgb', opacity=1,
    depth=-1.0)
Bad_7 = visual.TextStim(win=win, ori=0, name='Bad_7',
    text='Bad',    font='Arial',
    pos=[-0.8,0.6], height=0.15, wrapWidth=None,
    color='limegreen', colorSpace='rgb', opacity=1,
    depth=-2.0)
Creative_7 = visual.TextStim(win=win, ori=0, name='Creative_7',
    text='Creative',    font='Arial',
    pos=[0.8*side,0.8], height=0.15, wrapWidth=None,
    color='skyblue', colorSpace='rgb', opacity=1,
    depth=-3.0)
or_2_7 = visual.TextStim(win=win, ori=0, name='or_2_7',
    text='or',    font='Arial',
    pos=[0.8,0.7], height=0.1, wrapWidth=None,
    color='gray', colorSpace='rgb', opacity=1,
    depth=-4.0)
Good_7 = visual.TextStim(win=win, ori=0, name='Good_7',
    text='Good',    font='Arial',
    pos=[0.8,0.6], height=0.15, wrapWidth=None,
    color='limegreen', colorSpace='rgb', opacity=1,
    depth=-5.0)
Word_7 = visual.TextStim(win=win, ori=0, name='Word_7',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.15, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-6.0)

Wrong_7 = visual.TextStim(win=win, ori=0, name='Wrong_7',
    text='X',    font='Arial',
    pos=[0, -.3], height=0.1, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-10.0)

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
Thanks = visual.TextStim(win=win, ori=0, name='Thanks',
    text='End of this part.\r\n\r\nPress space to end.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='gray', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "Instructions"-------
t = 0
InstructionsClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED

# keep track of which components have finished
InstructionsComponents = []
InstructionsComponents.append(Instr)
InstructionsComponents.append(key_resp_2)
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Instructions"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instr* updates
    if t >= 0.0 and Instr.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr.tStart = t  # underestimates by a little under one frame
        Instr.frameNStart = frameN  # exact frame index
        Instr.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        key_resp_2.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
   key_resp_2.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()

# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "Instr_1"-------
t = 0
Instr_1Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
Instr_key_resp_1x = event.BuilderKeyResponse()  # create an object of type KeyResponse
Instr_key_resp_1x.status = NOT_STARTED
Instr_Creat_1.setPos([-.8*side, 0.8])
Instr_Prac_1.setPos([0.8*side, 0.8])
# keep track of which components have finished
Instr_1Components = []
Instr_1Components.append(Instr_1x)
Instr_1Components.append(Instr_key_resp_1x)
Instr_1Components.append(Instr_Creat_1)
Instr_1Components.append(Instr_Prac_1)
for thisComponent in Instr_1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Instr_1"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = Instr_1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instr_1x* updates
    if t >= 0.0 and Instr_1x.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr_1x.tStart = t  # underestimates by a little under one frame
        Instr_1x.frameNStart = frameN  # exact frame index
        Instr_1x.setAutoDraw(True)
    
    # *Instr_key_resp_1x* updates
    if t >= 0.0 and Instr_key_resp_1x.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr_key_resp_1x.tStart = t  # underestimates by a little under one frame
        Instr_key_resp_1x.frameNStart = frameN  # exact frame index
        Instr_key_resp_1x.status = STARTED
        # keyboard checking is just starting
        Instr_key_resp_1x.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if Instr_key_resp_1x.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            Instr_key_resp_1x.keys = theseKeys[-1]  # just the last key pressed
            Instr_key_resp_1x.rt = Instr_key_resp_1x.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *Instr_Creat_1* updates
    if t >= 0.0 and Instr_Creat_1.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr_Creat_1.tStart = t  # underestimates by a little under one frame
        Instr_Creat_1.frameNStart = frameN  # exact frame index
        Instr_Creat_1.setAutoDraw(True)
    
    # *Instr_Prac_1* updates
    if t >= 0.0 and Instr_Prac_1.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr_Prac_1.tStart = t  # underestimates by a little under one frame
        Instr_Prac_1.frameNStart = frameN  # exact frame index
        Instr_Prac_1.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instr_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Instr_1"-------
for thisComponent in Instr_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Instr_key_resp_1x.keys in ['', [], None]:  # No response was made
   Instr_key_resp_1x.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('Instr_key_resp_1x.keys',Instr_key_resp_1x.keys)
if Instr_key_resp_1x.keys != None:  # we had a response
    thisExp.addData('Instr_key_resp_1x.rt', Instr_key_resp_1x.rt)
thisExp.nextEntry()
# the Routine "Instr_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath='C:\\Users\\user1\\Desktop\\psychopy_neuro-master\\Lesson_plan_Psychopy\\visneuro_demo\\PsychoPy2 Demos\\practical IAT\\IAT.psyexp',
    trialList=data.importConditions('Creat_Prac.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine "Block_1"-------
    t = 0
    Block_1Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    Creative.setPos([-.65*side, 0.65])
    Practical.setPos([.65*side, 0.65])
    Word_1.setColor(color, colorSpace='rgb')
    Word_1.setText(word)
    Response_1 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    Response_1.status = NOT_STARTED
    
    Keys_1 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    Keys_1.status = NOT_STARTED
    # keep track of which components have finished
    Block_1Components = []
    Block_1Components.append(Creative)
    Block_1Components.append(Practical)
    Block_1Components.append(Word_1)
    Block_1Components.append(Response_1)
    Block_1Components.append(Keys_1)
    Block_1Components.append(Wrong_1)
    for thisComponent in Block_1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Block_1"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = Block_1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Creative* updates
        if t >= 0.0 and Creative.status == NOT_STARTED:
            # keep track of start time/frame for later
            Creative.tStart = t  # underestimates by a little under one frame
            Creative.frameNStart = frameN  # exact frame index
            Creative.setAutoDraw(True)
        
        # *Practical* updates
        if t >= 0.0 and Practical.status == NOT_STARTED:
            # keep track of start time/frame for later
            Practical.tStart = t  # underestimates by a little under one frame
            Practical.frameNStart = frameN  # exact frame index
            Practical.setAutoDraw(True)
        
        # *Word_1* updates
        if t >= 0.3 and Word_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            Word_1.tStart = t  # underestimates by a little under one frame
            Word_1.frameNStart = frameN  # exact frame index
            Word_1.setAutoDraw(True)
        
        # *Response_1* updates
        if t >= 0.3 and Response_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            Response_1.tStart = t  # underestimates by a little under one frame
            Response_1.frameNStart = frameN  # exact frame index
            Response_1.status = STARTED
            # keyboard checking is just starting
            Response_1.clock.reset()  # now t=0
        if Response_1.status == STARTED and (Wrong_1.status == STARTED):
            Response_1.status = STOPPED
        if Response_1.status == STARTED:
            theseKeys = event.getKeys(keyList=['e', 'i'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if Response_1.keys == []:  # then this was the first keypress
                    Response_1.keys = theseKeys[0]  # just the first key pressed
                    Response_1.rt = Response_1.clock.getTime()
                    # was this 'correct'?
                    if (Response_1.keys == str(corr(thisTrial.key, side, thisTrial.condition))) or (Response_1.keys == corr(thisTrial.key, side, thisTrial.condition)):
                        Response_1.corr = 1
                    else:
                        Response_1.corr = 0
        if Response_1.status == STARTED:
            if len(theseKeys) > 0:
                if Response_1.corr == 1:
                    continueRoutine = False
                else:
                    Wrong_1.setAutoDraw(True)
                    Wrong_1.status = STARTED
        
        # *Keys_1* updates
        if (Wrong_1.status==STARTED) and Keys_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            Keys_1.tStart = t  # underestimates by a little under one frame
            Keys_1.frameNStart = frameN  # exact frame index
            Keys_1.status = STARTED
            # keyboard checking is just starting
            Keys_1.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if Keys_1.status == STARTED:
            theseKeys = event.getKeys(keyList=['e', 'i'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if Keys_1.keys == []:  # then this was the first keypress
                    Keys_1.keys = theseKeys[0]  # just the first key pressed
                    Keys_1.rt = Keys_1.clock.getTime()
                    # was this 'correct'?
                    if (Keys_1.keys == str(corr(thisTrial.key, side, thisTrial.condition))) or (Keys_1.keys == corr(thisTrial.key, side, thisTrial.condition)):
                        Keys_1.corr = 1
                    else:
                        Keys_1.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # *Wrong_1* updates
        if (len(theseKeys)>5) and Wrong_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            Wrong_1.tStart = t  # underestimates by a little under one frame
            Wrong_1.frameNStart = frameN  # exact frame index
            Wrong_1.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Block_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "Block_1"-------
    for thisComponent in Block_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Response_1.keys in ['', [], None]:  # No response was made
       Response_1.keys=None
       # was no response the correct answer?!
       if str(corr(thisTrial.key, side, thisTrial.condition)).lower() == 'none': Response_1.corr = 1  # correct non-response
       else: Response_1.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('Response_1.keys',Response_1.keys)
    trials.addData('Response_1.corr', Response_1.corr)
    if Response_1.keys != None:  # we had a response
        trials.addData('Response_1.rt', Response_1.rt)
    
    # check responses
    if Keys_1.keys in ['', [], None]:  # No response was made
       Keys_1.keys=None
       # was no response the correct answer?!
       if str(corr(thisTrial.key, side, thisTrial.condition)).lower() == 'none': Keys_1.corr = 1  # correct non-response
       else: Keys_1.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('Keys_1.keys',Keys_1.keys)
    trials.addData('Keys_1.corr', Keys_1.corr)
    if Keys_1.keys != None:  # we had a response
        trials.addData('Keys_1.rt', Keys_1.rt)
    # the Routine "Block_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2 repeats of 'trials'


#------Prepare to start Routine "Instr_2"-------
t = 0
Instr_2Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
Instr_key_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
Instr_key_2.status = NOT_STARTED
# keep track of which components have finished
Instr_2Components = []
Instr_2Components.append(Instr_key_2)
Instr_2Components.append(Instru2)
Instr_2Components.append(Instr_Bad)
Instr_2Components.append(Instr_Good)
for thisComponent in Instr_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Instr_2"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = Instr_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instr_key_2* updates
    if t >= 0.0 and Instr_key_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr_key_2.tStart = t  # underestimates by a little under one frame
        Instr_key_2.frameNStart = frameN  # exact frame index
        Instr_key_2.status = STARTED
        # keyboard checking is just starting
        Instr_key_2.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if Instr_key_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            Instr_key_2.keys = theseKeys[-1]  # just the last key pressed
            Instr_key_2.rt = Instr_key_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *Instru2* updates
    if t >= 0.0 and Instru2.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instru2.tStart = t  # underestimates by a little under one frame
        Instru2.frameNStart = frameN  # exact frame index
        Instru2.setAutoDraw(True)
    
    # *Instr_Bad* updates
    if t >= 0.0 and Instr_Bad.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr_Bad.tStart = t  # underestimates by a little under one frame
        Instr_Bad.frameNStart = frameN  # exact frame index
        Instr_Bad.setAutoDraw(True)
    
    # *Instr_Good* updates
    if t >= 0.0 and Instr_Good.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr_Good.tStart = t  # underestimates by a little under one frame
        Instr_Good.frameNStart = frameN  # exact frame index
        Instr_Good.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instr_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Instr_2"-------
for thisComponent in Instr_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Instr_key_2.keys in ['', [], None]:  # No response was made
   Instr_key_2.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('Instr_key_2.keys',Instr_key_2.keys)
if Instr_key_2.keys != None:  # we had a response
    thisExp.addData('Instr_key_2.rt', Instr_key_2.rt)
thisExp.nextEntry()
# the Routine "Instr_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath='C:\\Users\\user1\\Desktop\\psychopy_neuro-master\\Lesson_plan_Psychopy\\visneuro_demo\\PsychoPy2 Demos\\practical IAT\\IAT.psyexp',
    trialList=data.importConditions('Good_Bad.csv'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2.keys():
        exec(paramName + '= thisTrial_2.' + paramName)

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2.keys():
            exec(paramName + '= thisTrial_2.' + paramName)
    
    #------Prepare to start Routine "Block_2"-------
    t = 0
    Block_2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    Word_2.setColor(color, colorSpace='rgb')
    Word_2.setText(word)
    Response_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    Response_2.status = NOT_STARTED
    
    Keys_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    Keys_2.status = NOT_STARTED
    # keep track of which components have finished
    Block_2Components = []
    Block_2Components.append(Bad)
    Block_2Components.append(Good)
    Block_2Components.append(Word_2)
    Block_2Components.append(Response_2)
    Block_2Components.append(Keys_2)
    Block_2Components.append(Wrong_2)
    for thisComponent in Block_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Block_2"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = Block_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Bad* updates
        if t >= 0.0 and Bad.status == NOT_STARTED:
            # keep track of start time/frame for later
            Bad.tStart = t  # underestimates by a little under one frame
            Bad.frameNStart = frameN  # exact frame index
            Bad.setAutoDraw(True)
        
        # *Good* updates
        if t >= 0.0 and Good.status == NOT_STARTED:
            # keep track of start time/frame for later
            Good.tStart = t  # underestimates by a little under one frame
            Good.frameNStart = frameN  # exact frame index
            Good.setAutoDraw(True)
        
        # *Word_2* updates
        if t >= 0.3 and Word_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            Word_2.tStart = t  # underestimates by a little under one frame
            Word_2.frameNStart = frameN  # exact frame index
            Word_2.setAutoDraw(True)
        
        # *Response_2* updates
        if t >= 0.3 and Response_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            Response_2.tStart = t  # underestimates by a little under one frame
            Response_2.frameNStart = frameN  # exact frame index
            Response_2.status = STARTED
            # keyboard checking is just starting
            Response_2.clock.reset()  # now t=0
        if Response_2.status == STARTED and (Wrong_2.status==STARTED):
            Response_2.status = STOPPED
        if Response_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['e', 'i'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if Response_2.keys == []:  # then this was the first keypress
                    Response_2.keys = theseKeys[0]  # just the first key pressed
                    Response_2.rt = Response_2.clock.getTime()
                    # was this 'correct'?
                    if (Response_2.keys == str(thisTrial_2.key)) or (Response_2.keys == thisTrial_2.key):
                        Response_2.corr = 1
                    else:
                        Response_2.corr = 0
        if Response_2.status==STARTED:
            if len(theseKeys)>0:
                if Response_2.corr ==1:
                    continueRoutine=False
                else:
                    Wrong_2.setAutoDraw(True)
                    Wrong_2.status=STARTED
        
        # *Keys_2* updates
        if (Wrong_2.status==STARTED) and Keys_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            Keys_2.tStart = t  # underestimates by a little under one frame
            Keys_2.frameNStart = frameN  # exact frame index
            Keys_2.status = STARTED
            # keyboard checking is just starting
            Keys_2.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if Keys_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['e', 'i'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if Keys_2.keys == []:  # then this was the first keypress
                    Keys_2.keys = theseKeys[0]  # just the first key pressed
                    Keys_2.rt = Keys_2.clock.getTime()
                    # was this 'correct'?
                    if (Keys_2.keys == str(thisTrial_2.key)) or (Keys_2.keys == thisTrial_2.key):
                        Keys_2.corr = 1
                    else:
                        Keys_2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # *Wrong_2* updates
        if (len(theseKeys)>5) and Wrong_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            Wrong_2.tStart = t  # underestimates by a little under one frame
            Wrong_2.frameNStart = frameN  # exact frame index
            Wrong_2.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Block_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "Block_2"-------
    for thisComponent in Block_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Response_2.keys in ['', [], None]:  # No response was made
       Response_2.keys=None
       # was no response the correct answer?!
       if str(thisTrial_2.key).lower() == 'none': Response_2.corr = 1  # correct non-response
       else: Response_2.corr = 0  # failed to respond (incorrectly)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('Response_2.keys',Response_2.keys)
    trials_2.addData('Response_2.corr', Response_2.corr)
    if Response_2.keys != None:  # we had a response
        trials_2.addData('Response_2.rt', Response_2.rt)
    
    # check responses
    if Keys_2.keys in ['', [], None]:  # No response was made
       Keys_2.keys=None
       # was no response the correct answer?!
       if str(thisTrial_2.key).lower() == 'none': Keys_2.corr = 1  # correct non-response
       else: Keys_2.corr = 0  # failed to respond (incorrectly)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('Keys_2.keys',Keys_2.keys)
    trials_2.addData('Keys_2.corr', Keys_2.corr)
    if Keys_2.keys != None:  # we had a response
        trials_2.addData('Keys_2.rt', Keys_2.rt)
    # the Routine "Block_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2 repeats of 'trials_2'


#------Prepare to start Routine "Instr_3"-------
t = 0
Instr_3Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
Instr_key_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
Instr_key_3.status = NOT_STARTED
# keep track of which components have finished
Instr_3Components = []
Instr_3Components.append(Instr3)
Instr_3Components.append(Instr_Creat_3)
Instr_3Components.append(Instr_or_3)
Instr_3Components.append(Instr_Bad_3)
Instr_3Components.append(Instr_Prac_3)
Instr_3Components.append(Instr_or_3_2)
Instr_3Components.append(Instr_Good_3)
Instr_3Components.append(Instr_key_3)
for thisComponent in Instr_3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Instr_3"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = Instr_3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instr3* updates
    if t >= 0.0 and Instr3.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr3.tStart = t  # underestimates by a little under one frame
        Instr3.frameNStart = frameN  # exact frame index
        Instr3.setAutoDraw(True)
    
    # *Instr_Creat_3* updates
    if t >= 0.0 and Instr_Creat_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr_Creat_3.tStart = t  # underestimates by a little under one frame
        Instr_Creat_3.frameNStart = frameN  # exact frame index
        Instr_Creat_3.setAutoDraw(True)
    
    # *Instr_or_3* updates
    if t >= 0.0 and Instr_or_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr_or_3.tStart = t  # underestimates by a little under one frame
        Instr_or_3.frameNStart = frameN  # exact frame index
        Instr_or_3.setAutoDraw(True)
    
    # *Instr_Bad_3* updates
    if t >= 0.0 and Instr_Bad_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr_Bad_3.tStart = t  # underestimates by a little under one frame
        Instr_Bad_3.frameNStart = frameN  # exact frame index
        Instr_Bad_3.setAutoDraw(True)
    
    # *Instr_Prac_3* updates
    if t >= 0.0 and Instr_Prac_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr_Prac_3.tStart = t  # underestimates by a little under one frame
        Instr_Prac_3.frameNStart = frameN  # exact frame index
        Instr_Prac_3.setAutoDraw(True)
    
    # *Instr_or_3_2* updates
    if t >= 0.0 and Instr_or_3_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr_or_3_2.tStart = t  # underestimates by a little under one frame
        Instr_or_3_2.frameNStart = frameN  # exact frame index
        Instr_or_3_2.setAutoDraw(True)
    
    # *Instr_Good_3* updates
    if t >= 0.0 and Instr_Good_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr_Good_3.tStart = t  # underestimates by a little under one frame
        Instr_Good_3.frameNStart = frameN  # exact frame index
        Instr_Good_3.setAutoDraw(True)
    
    # *Instr_key_3* updates
    if t >= 0.0 and Instr_key_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr_key_3.tStart = t  # underestimates by a little under one frame
        Instr_key_3.frameNStart = frameN  # exact frame index
        Instr_key_3.status = STARTED
        # keyboard checking is just starting
        Instr_key_3.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if Instr_key_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            Instr_key_3.keys = theseKeys[-1]  # just the last key pressed
            Instr_key_3.rt = Instr_key_3.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instr_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Instr_3"-------
for thisComponent in Instr_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Instr_key_3.keys in ['', [], None]:  # No response was made
   Instr_key_3.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('Instr_key_3.keys',Instr_key_3.keys)
if Instr_key_3.keys != None:  # we had a response
    thisExp.addData('Instr_key_3.rt', Instr_key_3.rt)
thisExp.nextEntry()
# the Routine "Instr_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath='C:\\Users\\user1\\Desktop\\psychopy_neuro-master\\Lesson_plan_Psychopy\\visneuro_demo\\PsychoPy2 Demos\\practical IAT\\IAT.psyexp',
    trialList=data.importConditions('All.csv'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3.keys():
        exec(paramName + '= thisTrial_3.' + paramName)

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3.keys():
            exec(paramName + '= thisTrial_3.' + paramName)
    
    #------Prepare to start Routine "Block_3"-------
    t = 0
    Block_3Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    Word_3.setColor(color, colorSpace='rgb')
    Word_3.setText(word)
    Response_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    Response_3.status = NOT_STARTED
    
    Keys_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    Keys_3.status = NOT_STARTED
    # keep track of which components have finished
    Block_3Components = []
    Block_3Components.append(Creative_3)
    Block_3Components.append(or_3)
    Block_3Components.append(Bad_3)
    Block_3Components.append(Practical_3)
    Block_3Components.append(or_2_3)
    Block_3Components.append(Good_3)
    Block_3Components.append(Word_3)
    Block_3Components.append(Response_3)
    Block_3Components.append(Keys_3)
    Block_3Components.append(Wrong_3)
    for thisComponent in Block_3Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Block_3"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = Block_3Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Creative_3* updates
        if t >= 0.0 and Creative_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            Creative_3.tStart = t  # underestimates by a little under one frame
            Creative_3.frameNStart = frameN  # exact frame index
            Creative_3.setAutoDraw(True)
        
        # *or_3* updates
        if t >= 0.0 and or_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            or_3.tStart = t  # underestimates by a little under one frame
            or_3.frameNStart = frameN  # exact frame index
            or_3.setAutoDraw(True)
        
        # *Bad_3* updates
        if t >= 0.0 and Bad_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            Bad_3.tStart = t  # underestimates by a little under one frame
            Bad_3.frameNStart = frameN  # exact frame index
            Bad_3.setAutoDraw(True)
        
        # *Practical_3* updates
        if t >= 0.0 and Practical_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            Practical_3.tStart = t  # underestimates by a little under one frame
            Practical_3.frameNStart = frameN  # exact frame index
            Practical_3.setAutoDraw(True)
        
        # *or_2_3* updates
        if t >= 0.0 and or_2_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            or_2_3.tStart = t  # underestimates by a little under one frame
            or_2_3.frameNStart = frameN  # exact frame index
            or_2_3.setAutoDraw(True)
        
        # *Good_3* updates
        if t >= 0.0 and Good_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            Good_3.tStart = t  # underestimates by a little under one frame
            Good_3.frameNStart = frameN  # exact frame index
            Good_3.setAutoDraw(True)
        
        # *Word_3* updates
        if t >= 0.3 and Word_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            Word_3.tStart = t  # underestimates by a little under one frame
            Word_3.frameNStart = frameN  # exact frame index
            Word_3.setAutoDraw(True)
        
        # *Response_3* updates
        if t >= 0.3 and Response_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            Response_3.tStart = t  # underestimates by a little under one frame
            Response_3.frameNStart = frameN  # exact frame index
            Response_3.status = STARTED
            # keyboard checking is just starting
            Response_3.clock.reset()  # now t=0
        if Response_3.status == STARTED and (Wrong_3.status==STARTED):
            Response_3.status = STOPPED
        if Response_3.status == STARTED:
            theseKeys = event.getKeys(keyList=['e', 'i'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if Response_3.keys == []:  # then this was the first keypress
                    Response_3.keys = theseKeys[0]  # just the first key pressed
                    Response_3.rt = Response_3.clock.getTime()
                    # was this 'correct'?
                    if (Response_3.keys == str(corr(key, side, condition))) or (Response_3.keys == corr(key, side, condition)):
                        Response_3.corr = 1
                    else:
                        Response_3.corr = 0
        if Response_3.status == STARTED:
            if len(theseKeys) > 0:
                if Response_3.corr == 1:
                    continueRoutine=False
                else:
                    Wrong_3.setAutoDraw(True)
                    Wrong_3.status = STARTED
        
        # *Keys_3* updates
        if (Wrong_3.status==STARTED) and Keys_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            Keys_3.tStart = t  # underestimates by a little under one frame
            Keys_3.frameNStart = frameN  # exact frame index
            Keys_3.status = STARTED
            # keyboard checking is just starting
            Keys_3.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if Keys_3.status == STARTED:
            theseKeys = event.getKeys(keyList=['e', 'i'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if Keys_3.keys == []:  # then this was the first keypress
                    Keys_3.keys = theseKeys[0]  # just the first key pressed
                    Keys_3.rt = Keys_3.clock.getTime()
                    # was this 'correct'?
                    if (Keys_3.keys == str(corr(key, side, condition))) or (Keys_3.keys == corr(key, side, condition)):
                        Keys_3.corr = 1
                    else:
                        Keys_3.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # *Wrong_3* updates
        if (len(theseKeys)>5) and Wrong_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            Wrong_3.tStart = t  # underestimates by a little under one frame
            Wrong_3.frameNStart = frameN  # exact frame index
            Wrong_3.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Block_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "Block_3"-------
    for thisComponent in Block_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Response_3.keys in ['', [], None]:  # No response was made
       Response_3.keys=None
       # was no response the correct answer?!
       if str(corr(key, side, condition)).lower() == 'none': Response_3.corr = 1  # correct non-response
       else: Response_3.corr = 0  # failed to respond (incorrectly)
    # store data for trials_3 (TrialHandler)
    trials_3.addData('Response_3.keys',Response_3.keys)
    trials_3.addData('Response_3.corr', Response_3.corr)
    if Response_3.keys != None:  # we had a response
        trials_3.addData('Response_3.rt', Response_3.rt)
    
    # check responses
    if Keys_3.keys in ['', [], None]:  # No response was made
       Keys_3.keys=None
       # was no response the correct answer?!
       if str(corr(key, side, condition)).lower() == 'none': Keys_3.corr = 1  # correct non-response
       else: Keys_3.corr = 0  # failed to respond (incorrectly)
    # store data for trials_3 (TrialHandler)
    trials_3.addData('Keys_3.keys',Keys_3.keys)
    trials_3.addData('Keys_3.corr', Keys_3.corr)
    if Keys_3.keys != None:  # we had a response
        trials_3.addData('Keys_3.rt', Keys_3.rt)
    # the Routine "Block_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_3'


#------Prepare to start Routine "Instr_4"-------
t = 0
Instr_4Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
Instr_key_4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
Instr_key_4.status = NOT_STARTED
# keep track of which components have finished
Instr_4Components = []
Instr_4Components.append(Instr4)
Instr_4Components.append(Instr_key_4)
Instr_4Components.append(Instr_Creat_4)
Instr_4Components.append(Instr_or_4)
Instr_4Components.append(Instr_Bad_4)
Instr_4Components.append(Instr_Prac_4)
Instr_4Components.append(Instr_or_4_2)
Instr_4Components.append(Instr_Good_4)
for thisComponent in Instr_4Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Instr_4"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = Instr_4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instr4* updates
    if t >= 0.0 and Instr4.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr4.tStart = t  # underestimates by a little under one frame
        Instr4.frameNStart = frameN  # exact frame index
        Instr4.setAutoDraw(True)
    
    # *Instr_key_4* updates
    if t >= 0.0 and Instr_key_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr_key_4.tStart = t  # underestimates by a little under one frame
        Instr_key_4.frameNStart = frameN  # exact frame index
        Instr_key_4.status = STARTED
        # keyboard checking is just starting
        Instr_key_4.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if Instr_key_4.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            Instr_key_4.keys = theseKeys[-1]  # just the last key pressed
            Instr_key_4.rt = Instr_key_4.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *Instr_Creat_4* updates
    if t >= 0.0 and Instr_Creat_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr_Creat_4.tStart = t  # underestimates by a little under one frame
        Instr_Creat_4.frameNStart = frameN  # exact frame index
        Instr_Creat_4.setAutoDraw(True)
    
    # *Instr_or_4* updates
    if t >= 0.0 and Instr_or_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr_or_4.tStart = t  # underestimates by a little under one frame
        Instr_or_4.frameNStart = frameN  # exact frame index
        Instr_or_4.setAutoDraw(True)
    
    # *Instr_Bad_4* updates
    if t >= 0.0 and Instr_Bad_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr_Bad_4.tStart = t  # underestimates by a little under one frame
        Instr_Bad_4.frameNStart = frameN  # exact frame index
        Instr_Bad_4.setAutoDraw(True)
    
    # *Instr_Prac_4* updates
    if t >= 0.0 and Instr_Prac_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr_Prac_4.tStart = t  # underestimates by a little under one frame
        Instr_Prac_4.frameNStart = frameN  # exact frame index
        Instr_Prac_4.setAutoDraw(True)
    
    # *Instr_or_4_2* updates
    if t >= 0.0 and Instr_or_4_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr_or_4_2.tStart = t  # underestimates by a little under one frame
        Instr_or_4_2.frameNStart = frameN  # exact frame index
        Instr_or_4_2.setAutoDraw(True)
    
    # *Instr_Good_4* updates
    if t >= 0.0 and Instr_Good_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr_Good_4.tStart = t  # underestimates by a little under one frame
        Instr_Good_4.frameNStart = frameN  # exact frame index
        Instr_Good_4.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instr_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Instr_4"-------
for thisComponent in Instr_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Instr_key_4.keys in ['', [], None]:  # No response was made
   Instr_key_4.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('Instr_key_4.keys',Instr_key_4.keys)
if Instr_key_4.keys != None:  # we had a response
    thisExp.addData('Instr_key_4.rt', Instr_key_4.rt)
thisExp.nextEntry()
# the Routine "Instr_4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath='C:\\Users\\user1\\Desktop\\psychopy_neuro-master\\Lesson_plan_Psychopy\\visneuro_demo\\PsychoPy2 Demos\\practical IAT\\IAT.psyexp',
    trialList=data.importConditions('All.csv'),
    seed=None, name='trials_4')
thisExp.addLoop(trials_4)  # add the loop to the experiment
thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_4.rgb)
if thisTrial_4 != None:
    for paramName in thisTrial_4.keys():
        exec(paramName + '= thisTrial_4.' + paramName)

for thisTrial_4 in trials_4:
    currentLoop = trials_4
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4.keys():
            exec(paramName + '= thisTrial_4.' + paramName)
    
    #------Prepare to start Routine "Block_4"-------
    t = 0
    Block_4Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    Word_4.setColor(color, colorSpace='rgb')
    Word_4.setText(word)
    Response_4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    Response_4.status = NOT_STARTED
    
    Keys_4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    Keys_4.status = NOT_STARTED
    # keep track of which components have finished
    Block_4Components = []
    Block_4Components.append(Creative_4)
    Block_4Components.append(or_4)
    Block_4Components.append(Bad_4)
    Block_4Components.append(Practical_4)
    Block_4Components.append(or_2_4)
    Block_4Components.append(Good_4)
    Block_4Components.append(Word_4)
    Block_4Components.append(Response_4)
    Block_4Components.append(Keys_4)
    Block_4Components.append(Wrong_4)
    for thisComponent in Block_4Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Block_4"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = Block_4Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Creative_4* updates
        if t >= 0.0 and Creative_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            Creative_4.tStart = t  # underestimates by a little under one frame
            Creative_4.frameNStart = frameN  # exact frame index
            Creative_4.setAutoDraw(True)
        
        # *or_4* updates
        if t >= 0.0 and or_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            or_4.tStart = t  # underestimates by a little under one frame
            or_4.frameNStart = frameN  # exact frame index
            or_4.setAutoDraw(True)
        
        # *Bad_4* updates
        if t >= 0.0 and Bad_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            Bad_4.tStart = t  # underestimates by a little under one frame
            Bad_4.frameNStart = frameN  # exact frame index
            Bad_4.setAutoDraw(True)
        
        # *Practical_4* updates
        if t >= 0.0 and Practical_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            Practical_4.tStart = t  # underestimates by a little under one frame
            Practical_4.frameNStart = frameN  # exact frame index
            Practical_4.setAutoDraw(True)
        
        # *or_2_4* updates
        if t >= 0.0 and or_2_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            or_2_4.tStart = t  # underestimates by a little under one frame
            or_2_4.frameNStart = frameN  # exact frame index
            or_2_4.setAutoDraw(True)
        
        # *Good_4* updates
        if t >= 0.0 and Good_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            Good_4.tStart = t  # underestimates by a little under one frame
            Good_4.frameNStart = frameN  # exact frame index
            Good_4.setAutoDraw(True)
        
        # *Word_4* updates
        if t >= 0.3 and Word_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            Word_4.tStart = t  # underestimates by a little under one frame
            Word_4.frameNStart = frameN  # exact frame index
            Word_4.setAutoDraw(True)
        
        # *Response_4* updates
        if t >= 0.3 and Response_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            Response_4.tStart = t  # underestimates by a little under one frame
            Response_4.frameNStart = frameN  # exact frame index
            Response_4.status = STARTED
            # keyboard checking is just starting
            Response_4.clock.reset()  # now t=0
        if Response_4.status == STARTED and (Wrong_4.status==STARTED):
            Response_4.status = STOPPED
        if Response_4.status == STARTED:
            theseKeys = event.getKeys(keyList=['e', 'i'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if Response_4.keys == []:  # then this was the first keypress
                    Response_4.keys = theseKeys[0]  # just the first key pressed
                    Response_4.rt = Response_4.clock.getTime()
                    # was this 'correct'?
                    if (Response_4.keys == str(corr(key, side, condition))) or (Response_4.keys == corr(key, side, condition)):
                        Response_4.corr = 1
                    else:
                        Response_4.corr = 0
        if Response_4.status == STARTED:
            if len(theseKeys) > 0:
                if Response_4.corr ==1:
                    continueRoutine = False
                else:
                    Wrong_4.setAutoDraw(True)
                    Wrong_4.status = STARTED
        
        # *Keys_4* updates
        if (Wrong_4.status==STARTED) and Keys_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            Keys_4.tStart = t  # underestimates by a little under one frame
            Keys_4.frameNStart = frameN  # exact frame index
            Keys_4.status = STARTED
            # keyboard checking is just starting
            Keys_4.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if Keys_4.status == STARTED:
            theseKeys = event.getKeys(keyList=['e', 'i'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if Keys_4.keys == []:  # then this was the first keypress
                    Keys_4.keys = theseKeys[0]  # just the first key pressed
                    Keys_4.rt = Keys_4.clock.getTime()
                    # was this 'correct'?
                    if (Keys_4.keys == str(corr(key, side, condition))) or (Keys_4.keys == corr(key, side, condition)):
                        Keys_4.corr = 1
                    else:
                        Keys_4.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # *Wrong_4* updates
        if (len(theseKeys)>5) and Wrong_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            Wrong_4.tStart = t  # underestimates by a little under one frame
            Wrong_4.frameNStart = frameN  # exact frame index
            Wrong_4.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Block_4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "Block_4"-------
    for thisComponent in Block_4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Response_4.keys in ['', [], None]:  # No response was made
       Response_4.keys=None
       # was no response the correct answer?!
       if str(corr(key, side, condition)).lower() == 'none': Response_4.corr = 1  # correct non-response
       else: Response_4.corr = 0  # failed to respond (incorrectly)
    # store data for trials_4 (TrialHandler)
    trials_4.addData('Response_4.keys',Response_4.keys)
    trials_4.addData('Response_4.corr', Response_4.corr)
    if Response_4.keys != None:  # we had a response
        trials_4.addData('Response_4.rt', Response_4.rt)
    
    # check responses
    if Keys_4.keys in ['', [], None]:  # No response was made
       Keys_4.keys=None
       # was no response the correct answer?!
       if str(corr(key, side, condition)).lower() == 'none': Keys_4.corr = 1  # correct non-response
       else: Keys_4.corr = 0  # failed to respond (incorrectly)
    # store data for trials_4 (TrialHandler)
    trials_4.addData('Keys_4.keys',Keys_4.keys)
    trials_4.addData('Keys_4.corr', Keys_4.corr)
    if Keys_4.keys != None:  # we had a response
        trials_4.addData('Keys_4.rt', Keys_4.rt)
    # the Routine "Block_4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2 repeats of 'trials_4'


#------Prepare to start Routine "Instr_5"-------
t = 0
Instr_5Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
Instr_key_5 = event.BuilderKeyResponse()  # create an object of type KeyResponse
Instr_key_5.status = NOT_STARTED
# keep track of which components have finished
Instr_5Components = []
Instr_5Components.append(Instr5)
Instr_5Components.append(Instr_Prac_5)
Instr_5Components.append(Instr_Creat_5)
Instr_5Components.append(Instr_key_5)
for thisComponent in Instr_5Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Instr_5"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = Instr_5Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instr5* updates
    if t >= 0.0 and Instr5.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr5.tStart = t  # underestimates by a little under one frame
        Instr5.frameNStart = frameN  # exact frame index
        Instr5.setAutoDraw(True)
    
    # *Instr_Prac_5* updates
    if t >= 0.0 and Instr_Prac_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr_Prac_5.tStart = t  # underestimates by a little under one frame
        Instr_Prac_5.frameNStart = frameN  # exact frame index
        Instr_Prac_5.setAutoDraw(True)
    
    # *Instr_Creat_5* updates
    if t >= 0.0 and Instr_Creat_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr_Creat_5.tStart = t  # underestimates by a little under one frame
        Instr_Creat_5.frameNStart = frameN  # exact frame index
        Instr_Creat_5.setAutoDraw(True)
    
    # *Instr_key_5* updates
    if t >= 0.0 and Instr_key_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr_key_5.tStart = t  # underestimates by a little under one frame
        Instr_key_5.frameNStart = frameN  # exact frame index
        Instr_key_5.status = STARTED
        # keyboard checking is just starting
        Instr_key_5.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if Instr_key_5.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            Instr_key_5.keys = theseKeys[-1]  # just the last key pressed
            Instr_key_5.rt = Instr_key_5.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instr_5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Instr_5"-------
for thisComponent in Instr_5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Instr_key_5.keys in ['', [], None]:  # No response was made
   Instr_key_5.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('Instr_key_5.keys',Instr_key_5.keys)
if Instr_key_5.keys != None:  # we had a response
    thisExp.addData('Instr_key_5.rt', Instr_key_5.rt)
thisExp.nextEntry()
# the Routine "Instr_5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_5 = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath='C:\\Users\\user1\\Desktop\\psychopy_neuro-master\\Lesson_plan_Psychopy\\visneuro_demo\\PsychoPy2 Demos\\practical IAT\\IAT.psyexp',
    trialList=data.importConditions('Creat_Prac_rev.csv'),
    seed=None, name='trials_5')
thisExp.addLoop(trials_5)  # add the loop to the experiment
thisTrial_5 = trials_5.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_5.rgb)
if thisTrial_5 != None:
    for paramName in thisTrial_5.keys():
        exec(paramName + '= thisTrial_5.' + paramName)

for thisTrial_5 in trials_5:
    currentLoop = trials_5
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
    if thisTrial_5 != None:
        for paramName in thisTrial_5.keys():
            exec(paramName + '= thisTrial_5.' + paramName)
    
    #------Prepare to start Routine "Block_5"-------
    t = 0
    Block_5Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    Word_5.setColor(color, colorSpace='rgb')
    Word_5.setText(word)
    Response_5 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    Response_5.status = NOT_STARTED
    
    Keys_5 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    Keys_5.status = NOT_STARTED
    # keep track of which components have finished
    Block_5Components = []
    Block_5Components.append(Practical_5)
    Block_5Components.append(Creative_5)
    Block_5Components.append(Word_5)
    Block_5Components.append(Response_5)
    Block_5Components.append(Keys_5)
    Block_5Components.append(Wrong_5)
    for thisComponent in Block_5Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Block_5"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = Block_5Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Practical_5* updates
        if t >= 0.0 and Practical_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            Practical_5.tStart = t  # underestimates by a little under one frame
            Practical_5.frameNStart = frameN  # exact frame index
            Practical_5.setAutoDraw(True)
        
        # *Creative_5* updates
        if t >= 0.0 and Creative_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            Creative_5.tStart = t  # underestimates by a little under one frame
            Creative_5.frameNStart = frameN  # exact frame index
            Creative_5.setAutoDraw(True)
        
        # *Word_5* updates
        if t >= 0.3 and Word_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            Word_5.tStart = t  # underestimates by a little under one frame
            Word_5.frameNStart = frameN  # exact frame index
            Word_5.setAutoDraw(True)
        
        # *Response_5* updates
        if t >= 0.3 and Response_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            Response_5.tStart = t  # underestimates by a little under one frame
            Response_5.frameNStart = frameN  # exact frame index
            Response_5.status = STARTED
            # keyboard checking is just starting
            Response_5.clock.reset()  # now t=0
        if Response_5.status == STARTED and (Wrong_5.status==STARTED):
            Response_5.status = STOPPED
        if Response_5.status == STARTED:
            theseKeys = event.getKeys(keyList=['e', 'i'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                Response_5.keys = theseKeys[-1]  # just the last key pressed
                Response_5.rt = Response_5.clock.getTime()
                # was this 'correct'?
                if (Response_5.keys == str(corr(thisTrial_5.key, side, thisTrial_5.condition))) or (Response_5.keys == corr(thisTrial_5.key, side, thisTrial_5.condition)):
                    Response_5.corr = 1
                else:
                    Response_5.corr = 0
        if Response_5.status==STARTED:
            if len(theseKeys)>0:
                if Response_5.corr ==1:
                    continueRoutine=False
                else:
                    Wrong_5.setAutoDraw(True)
                    Wrong_5.status=STARTED
        
        # *Keys_5* updates
        if (Wrong_5.status==STARTED) and Keys_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            Keys_5.tStart = t  # underestimates by a little under one frame
            Keys_5.frameNStart = frameN  # exact frame index
            Keys_5.status = STARTED
            # keyboard checking is just starting
            Keys_5.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if Keys_5.status == STARTED:
            theseKeys = event.getKeys(keyList=['e', 'i'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if Keys_5.keys == []:  # then this was the first keypress
                    Keys_5.keys = theseKeys[0]  # just the first key pressed
                    Keys_5.rt = Keys_5.clock.getTime()
                    # was this 'correct'?
                    if (Keys_5.keys == str(corr(thisTrial_5.key, side, thisTrial_5.condition))) or (Keys_5.keys == corr(thisTrial_5.key, side, thisTrial_5.condition)):
                        Keys_5.corr = 1
                    else:
                        Keys_5.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # *Wrong_5* updates
        if (len(theseKeys)>5) and Wrong_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            Wrong_5.tStart = t  # underestimates by a little under one frame
            Wrong_5.frameNStart = frameN  # exact frame index
            Wrong_5.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Block_5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "Block_5"-------
    for thisComponent in Block_5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Response_5.keys in ['', [], None]:  # No response was made
       Response_5.keys=None
       # was no response the correct answer?!
       if str(corr(thisTrial_5.key, side, thisTrial_5.condition)).lower() == 'none': Response_5.corr = 1  # correct non-response
       else: Response_5.corr = 0  # failed to respond (incorrectly)
    # store data for trials_5 (TrialHandler)
    trials_5.addData('Response_5.keys',Response_5.keys)
    trials_5.addData('Response_5.corr', Response_5.corr)
    if Response_5.keys != None:  # we had a response
        trials_5.addData('Response_5.rt', Response_5.rt)
    
    # check responses
    if Keys_5.keys in ['', [], None]:  # No response was made
       Keys_5.keys=None
       # was no response the correct answer?!
       if str(corr(thisTrial_5.key, side, thisTrial_5.condition)).lower() == 'none': Keys_5.corr = 1  # correct non-response
       else: Keys_5.corr = 0  # failed to respond (incorrectly)
    # store data for trials_5 (TrialHandler)
    trials_5.addData('Keys_5.keys',Keys_5.keys)
    trials_5.addData('Keys_5.corr', Keys_5.corr)
    if Keys_5.keys != None:  # we had a response
        trials_5.addData('Keys_5.rt', Keys_5.rt)
    # the Routine "Block_5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2 repeats of 'trials_5'


#------Prepare to start Routine "Instr_6"-------
t = 0
Instr_6Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
Instr_key_6 = event.BuilderKeyResponse()  # create an object of type KeyResponse
Instr_key_6.status = NOT_STARTED
# keep track of which components have finished
Instr_6Components = []
Instr_6Components.append(Instr6)
Instr_6Components.append(Instr_Prac_6)
Instr_6Components.append(Instr_or_6)
Instr_6Components.append(Instr_Bad_6)
Instr_6Components.append(Instr_Creat_6)
Instr_6Components.append(Instr_or_6_2)
Instr_6Components.append(Instr_Good_6)
Instr_6Components.append(Instr_key_6)
for thisComponent in Instr_6Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Instr_6"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = Instr_6Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instr6* updates
    if t >= 0.0 and Instr6.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr6.tStart = t  # underestimates by a little under one frame
        Instr6.frameNStart = frameN  # exact frame index
        Instr6.setAutoDraw(True)
    
    # *Instr_Prac_6* updates
    if t >= 0.0 and Instr_Prac_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr_Prac_6.tStart = t  # underestimates by a little under one frame
        Instr_Prac_6.frameNStart = frameN  # exact frame index
        Instr_Prac_6.setAutoDraw(True)
    
    # *Instr_or_6* updates
    if t >= 0.0 and Instr_or_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr_or_6.tStart = t  # underestimates by a little under one frame
        Instr_or_6.frameNStart = frameN  # exact frame index
        Instr_or_6.setAutoDraw(True)
    
    # *Instr_Bad_6* updates
    if t >= 0.0 and Instr_Bad_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr_Bad_6.tStart = t  # underestimates by a little under one frame
        Instr_Bad_6.frameNStart = frameN  # exact frame index
        Instr_Bad_6.setAutoDraw(True)
    
    # *Instr_Creat_6* updates
    if t >= 0.0 and Instr_Creat_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr_Creat_6.tStart = t  # underestimates by a little under one frame
        Instr_Creat_6.frameNStart = frameN  # exact frame index
        Instr_Creat_6.setAutoDraw(True)
    
    # *Instr_or_6_2* updates
    if t >= 0.0 and Instr_or_6_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr_or_6_2.tStart = t  # underestimates by a little under one frame
        Instr_or_6_2.frameNStart = frameN  # exact frame index
        Instr_or_6_2.setAutoDraw(True)
    
    # *Instr_Good_6* updates
    if t >= 0.0 and Instr_Good_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr_Good_6.tStart = t  # underestimates by a little under one frame
        Instr_Good_6.frameNStart = frameN  # exact frame index
        Instr_Good_6.setAutoDraw(True)
    
    # *Instr_key_6* updates
    if t >= 0.0 and Instr_key_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr_key_6.tStart = t  # underestimates by a little under one frame
        Instr_key_6.frameNStart = frameN  # exact frame index
        Instr_key_6.status = STARTED
        # keyboard checking is just starting
        Instr_key_6.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if Instr_key_6.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            Instr_key_6.keys = theseKeys[-1]  # just the last key pressed
            Instr_key_6.rt = Instr_key_6.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instr_6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Instr_6"-------
for thisComponent in Instr_6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Instr_key_6.keys in ['', [], None]:  # No response was made
   Instr_key_6.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('Instr_key_6.keys',Instr_key_6.keys)
if Instr_key_6.keys != None:  # we had a response
    thisExp.addData('Instr_key_6.rt', Instr_key_6.rt)
thisExp.nextEntry()
# the Routine "Instr_6" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_6 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath='C:\\Users\\user1\\Desktop\\psychopy_neuro-master\\Lesson_plan_Psychopy\\visneuro_demo\\PsychoPy2 Demos\\practical IAT\\IAT.psyexp',
    trialList=data.importConditions('All_rev.csv'),
    seed=None, name='trials_6')
thisExp.addLoop(trials_6)  # add the loop to the experiment
thisTrial_6 = trials_6.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_6.rgb)
if thisTrial_6 != None:
    for paramName in thisTrial_6.keys():
        exec(paramName + '= thisTrial_6.' + paramName)

for thisTrial_6 in trials_6:
    currentLoop = trials_6
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_6.rgb)
    if thisTrial_6 != None:
        for paramName in thisTrial_6.keys():
            exec(paramName + '= thisTrial_6.' + paramName)
    
    #------Prepare to start Routine "Block_6"-------
    t = 0
    Block_6Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    Word_6.setColor(color, colorSpace='rgb')
    Word_6.setText(word)
    Response_6 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    Response_6.status = NOT_STARTED
    
    Keys_6 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    Keys_6.status = NOT_STARTED
    # keep track of which components have finished
    Block_6Components = []
    Block_6Components.append(Practical_6)
    Block_6Components.append(or_6)
    Block_6Components.append(Bad_6)
    Block_6Components.append(Creative_6)
    Block_6Components.append(or_2_6)
    Block_6Components.append(Good_6)
    Block_6Components.append(Word_6)
    Block_6Components.append(Response_6)
    Block_6Components.append(Keys_6)
    Block_6Components.append(Wrong_6)
    for thisComponent in Block_6Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Block_6"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = Block_6Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Practical_6* updates
        if t >= 0.0 and Practical_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            Practical_6.tStart = t  # underestimates by a little under one frame
            Practical_6.frameNStart = frameN  # exact frame index
            Practical_6.setAutoDraw(True)
        
        # *or_6* updates
        if t >= 0.0 and or_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            or_6.tStart = t  # underestimates by a little under one frame
            or_6.frameNStart = frameN  # exact frame index
            or_6.setAutoDraw(True)
        
        # *Bad_6* updates
        if t >= 0.0 and Bad_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            Bad_6.tStart = t  # underestimates by a little under one frame
            Bad_6.frameNStart = frameN  # exact frame index
            Bad_6.setAutoDraw(True)
        
        # *Creative_6* updates
        if t >= 0.0 and Creative_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            Creative_6.tStart = t  # underestimates by a little under one frame
            Creative_6.frameNStart = frameN  # exact frame index
            Creative_6.setAutoDraw(True)
        
        # *or_2_6* updates
        if t >= 0.0 and or_2_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            or_2_6.tStart = t  # underestimates by a little under one frame
            or_2_6.frameNStart = frameN  # exact frame index
            or_2_6.setAutoDraw(True)
        
        # *Good_6* updates
        if t >= 0.0 and Good_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            Good_6.tStart = t  # underestimates by a little under one frame
            Good_6.frameNStart = frameN  # exact frame index
            Good_6.setAutoDraw(True)
        
        # *Word_6* updates
        if t >= 0.3 and Word_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            Word_6.tStart = t  # underestimates by a little under one frame
            Word_6.frameNStart = frameN  # exact frame index
            Word_6.setAutoDraw(True)
        
        # *Response_6* updates
        if t >= 0.3 and Response_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            Response_6.tStart = t  # underestimates by a little under one frame
            Response_6.frameNStart = frameN  # exact frame index
            Response_6.status = STARTED
            # keyboard checking is just starting
            Response_6.clock.reset()  # now t=0
        if Response_6.status == STARTED and (Wrong_6.status==STARTED):
            Response_6.status = STOPPED
        if Response_6.status == STARTED:
            theseKeys = event.getKeys(keyList=['e', 'i'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if Response_6.keys == []:  # then this was the first keypress
                    Response_6.keys = theseKeys[0]  # just the first key pressed
                    Response_6.rt = Response_6.clock.getTime()
                    # was this 'correct'?
                    if (Response_6.keys == str(corr(key, side, condition))) or (Response_6.keys == corr(key, side, condition)):
                        Response_6.corr = 1
                    else:
                        Response_6.corr = 0
        if Response_6.status==STARTED:
            if len(theseKeys)>0:
                if Response_6.corr ==1:
                    continueRoutine=False
                else:
                    Wrong_6.setAutoDraw(True)
                    Wrong_6.status=STARTED
        
        # *Keys_6* updates
        if (Wrong_6.status==STARTED) and Keys_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            Keys_6.tStart = t  # underestimates by a little under one frame
            Keys_6.frameNStart = frameN  # exact frame index
            Keys_6.status = STARTED
            # keyboard checking is just starting
            Keys_6.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if Keys_6.status == STARTED:
            theseKeys = event.getKeys(keyList=['e', 'i'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if Keys_6.keys == []:  # then this was the first keypress
                    Keys_6.keys = theseKeys[0]  # just the first key pressed
                    Keys_6.rt = Keys_6.clock.getTime()
                    # was this 'correct'?
                    if (Keys_6.keys == str(corr(key, side, condition))) or (Keys_6.keys == corr(key, side, condition)):
                        Keys_6.corr = 1
                    else:
                        Keys_6.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # *Wrong_6* updates
        if (len(theseKeys)>5) and Wrong_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            Wrong_6.tStart = t  # underestimates by a little under one frame
            Wrong_6.frameNStart = frameN  # exact frame index
            Wrong_6.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Block_6Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "Block_6"-------
    for thisComponent in Block_6Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Response_6.keys in ['', [], None]:  # No response was made
       Response_6.keys=None
       # was no response the correct answer?!
       if str(corr(key, side, condition)).lower() == 'none': Response_6.corr = 1  # correct non-response
       else: Response_6.corr = 0  # failed to respond (incorrectly)
    # store data for trials_6 (TrialHandler)
    trials_6.addData('Response_6.keys',Response_6.keys)
    trials_6.addData('Response_6.corr', Response_6.corr)
    if Response_6.keys != None:  # we had a response
        trials_6.addData('Response_6.rt', Response_6.rt)
    
    # check responses
    if Keys_6.keys in ['', [], None]:  # No response was made
       Keys_6.keys=None
       # was no response the correct answer?!
       if str(corr(key, side, condition)).lower() == 'none': Keys_6.corr = 1  # correct non-response
       else: Keys_6.corr = 0  # failed to respond (incorrectly)
    # store data for trials_6 (TrialHandler)
    trials_6.addData('Keys_6.keys',Keys_6.keys)
    trials_6.addData('Keys_6.corr', Keys_6.corr)
    if Keys_6.keys != None:  # we had a response
        trials_6.addData('Keys_6.rt', Keys_6.rt)
    # the Routine "Block_6" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_6'


#------Prepare to start Routine "Instr_7"-------
t = 0
Instr_7Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
Instr_key_7 = event.BuilderKeyResponse()  # create an object of type KeyResponse
Instr_key_7.status = NOT_STARTED
# keep track of which components have finished
Instr_7Components = []
Instr_7Components.append(Instr7)
Instr_7Components.append(Instr_key_7)
Instr_7Components.append(Instr_Prac_7)
Instr_7Components.append(Instr_or_7)
Instr_7Components.append(Instr_Bad_7)
Instr_7Components.append(Instr_Creat_7)
Instr_7Components.append(Instr_or_7_2)
Instr_7Components.append(Instr_Good_7)
for thisComponent in Instr_7Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Instr_7"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = Instr_7Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instr7* updates
    if t >= 0.0 and Instr7.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr7.tStart = t  # underestimates by a little under one frame
        Instr7.frameNStart = frameN  # exact frame index
        Instr7.setAutoDraw(True)
    
    # *Instr_key_7* updates
    if t >= 0.0 and Instr_key_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr_key_7.tStart = t  # underestimates by a little under one frame
        Instr_key_7.frameNStart = frameN  # exact frame index
        Instr_key_7.status = STARTED
        # keyboard checking is just starting
        Instr_key_7.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if Instr_key_7.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            Instr_key_7.keys = theseKeys[-1]  # just the last key pressed
            Instr_key_7.rt = Instr_key_7.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *Instr_Prac_7* updates
    if t >= 0.0 and Instr_Prac_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr_Prac_7.tStart = t  # underestimates by a little under one frame
        Instr_Prac_7.frameNStart = frameN  # exact frame index
        Instr_Prac_7.setAutoDraw(True)
    
    # *Instr_or_7* updates
    if t >= 0.0 and Instr_or_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr_or_7.tStart = t  # underestimates by a little under one frame
        Instr_or_7.frameNStart = frameN  # exact frame index
        Instr_or_7.setAutoDraw(True)
    
    # *Instr_Bad_7* updates
    if t >= 0.0 and Instr_Bad_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr_Bad_7.tStart = t  # underestimates by a little under one frame
        Instr_Bad_7.frameNStart = frameN  # exact frame index
        Instr_Bad_7.setAutoDraw(True)
    
    # *Instr_Creat_7* updates
    if t >= 0.0 and Instr_Creat_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr_Creat_7.tStart = t  # underestimates by a little under one frame
        Instr_Creat_7.frameNStart = frameN  # exact frame index
        Instr_Creat_7.setAutoDraw(True)
    
    # *Instr_or_7_2* updates
    if t >= 0.0 and Instr_or_7_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr_or_7_2.tStart = t  # underestimates by a little under one frame
        Instr_or_7_2.frameNStart = frameN  # exact frame index
        Instr_or_7_2.setAutoDraw(True)
    
    # *Instr_Good_7* updates
    if t >= 0.0 and Instr_Good_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr_Good_7.tStart = t  # underestimates by a little under one frame
        Instr_Good_7.frameNStart = frameN  # exact frame index
        Instr_Good_7.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instr_7Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Instr_7"-------
for thisComponent in Instr_7Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Instr_key_7.keys in ['', [], None]:  # No response was made
   Instr_key_7.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('Instr_key_7.keys',Instr_key_7.keys)
if Instr_key_7.keys != None:  # we had a response
    thisExp.addData('Instr_key_7.rt', Instr_key_7.rt)
thisExp.nextEntry()
# the Routine "Instr_7" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_7 = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath='C:\\Users\\user1\\Desktop\\psychopy_neuro-master\\Lesson_plan_Psychopy\\visneuro_demo\\PsychoPy2 Demos\\practical IAT\\IAT.psyexp',
    trialList=data.importConditions('All_rev.csv'),
    seed=None, name='trials_7')
thisExp.addLoop(trials_7)  # add the loop to the experiment
thisTrial_7 = trials_7.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_7.rgb)
if thisTrial_7 != None:
    for paramName in thisTrial_7.keys():
        exec(paramName + '= thisTrial_7.' + paramName)

for thisTrial_7 in trials_7:
    currentLoop = trials_7
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_7.rgb)
    if thisTrial_7 != None:
        for paramName in thisTrial_7.keys():
            exec(paramName + '= thisTrial_7.' + paramName)
    
    #------Prepare to start Routine "Block_7"-------
    t = 0
    Block_7Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    Word_7.setColor(color, colorSpace='rgb')
    Word_7.setText(word)
    Response_7 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    Response_7.status = NOT_STARTED
    
    Keys_7 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    Keys_7.status = NOT_STARTED
    # keep track of which components have finished
    Block_7Components = []
    Block_7Components.append(Practical_7)
    Block_7Components.append(or_7)
    Block_7Components.append(Bad_7)
    Block_7Components.append(Creative_7)
    Block_7Components.append(or_2_7)
    Block_7Components.append(Good_7)
    Block_7Components.append(Word_7)
    Block_7Components.append(Response_7)
    Block_7Components.append(Keys_7)
    Block_7Components.append(Wrong_7)
    for thisComponent in Block_7Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Block_7"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = Block_7Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Practical_7* updates
        if t >= 0.0 and Practical_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            Practical_7.tStart = t  # underestimates by a little under one frame
            Practical_7.frameNStart = frameN  # exact frame index
            Practical_7.setAutoDraw(True)
        
        # *or_7* updates
        if t >= 0.0 and or_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            or_7.tStart = t  # underestimates by a little under one frame
            or_7.frameNStart = frameN  # exact frame index
            or_7.setAutoDraw(True)
        
        # *Bad_7* updates
        if t >= 0.0 and Bad_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            Bad_7.tStart = t  # underestimates by a little under one frame
            Bad_7.frameNStart = frameN  # exact frame index
            Bad_7.setAutoDraw(True)
        
        # *Creative_7* updates
        if t >= 0.0 and Creative_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            Creative_7.tStart = t  # underestimates by a little under one frame
            Creative_7.frameNStart = frameN  # exact frame index
            Creative_7.setAutoDraw(True)
        
        # *or_2_7* updates
        if t >= 0.0 and or_2_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            or_2_7.tStart = t  # underestimates by a little under one frame
            or_2_7.frameNStart = frameN  # exact frame index
            or_2_7.setAutoDraw(True)
        
        # *Good_7* updates
        if t >= 0.0 and Good_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            Good_7.tStart = t  # underestimates by a little under one frame
            Good_7.frameNStart = frameN  # exact frame index
            Good_7.setAutoDraw(True)
        
        # *Word_7* updates
        if t >= 0.3 and Word_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            Word_7.tStart = t  # underestimates by a little under one frame
            Word_7.frameNStart = frameN  # exact frame index
            Word_7.setAutoDraw(True)
        
        # *Response_7* updates
        if t >= 0.3 and Response_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            Response_7.tStart = t  # underestimates by a little under one frame
            Response_7.frameNStart = frameN  # exact frame index
            Response_7.status = STARTED
            # keyboard checking is just starting
            Response_7.clock.reset()  # now t=0
        if Response_7.status == STARTED and (Wrong_7.status==STARTED):
            Response_7.status = STOPPED
        if Response_7.status == STARTED:
            theseKeys = event.getKeys(keyList=['e', 'i'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if Response_7.keys == []:  # then this was the first keypress
                    Response_7.keys = theseKeys[0]  # just the first key pressed
                    Response_7.rt = Response_7.clock.getTime()
                    # was this 'correct'?
                    if (Response_7.keys == str(corr(key, side, condition))) or (Response_7.keys == corr(key, side, condition)):
                        Response_7.corr = 1
                    else:
                        Response_7.corr = 0
        if Response_7.status == STARTED:
            if len(theseKeys) > 0:
                if Response_7.corr == 1:
                    continueRoutine=False
                else:
                    Wrong_7.setAutoDraw(True)
                    Wrong_7.status=STARTED
        
        # *Keys_7* updates
        if (Wrong_7.status==STARTED) and Keys_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            Keys_7.tStart = t  # underestimates by a little under one frame
            Keys_7.frameNStart = frameN  # exact frame index
            Keys_7.status = STARTED
            # keyboard checking is just starting
            Keys_7.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if Keys_7.status == STARTED:
            theseKeys = event.getKeys(keyList=['e', 'i'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if Keys_7.keys == []:  # then this was the first keypress
                    Keys_7.keys = theseKeys[0]  # just the first key pressed
                    Keys_7.rt = Keys_7.clock.getTime()
                    # was this 'correct'?
                    if (Keys_7.keys == str(corr(key, side, condition))) or (Keys_7.keys == corr(key, side, condition)):
                        Keys_7.corr = 1
                    else:
                        Keys_7.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # *Wrong_7* updates
        if (len(theseKeys)>5) and Wrong_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            Wrong_7.tStart = t  # underestimates by a little under one frame
            Wrong_7.frameNStart = frameN  # exact frame index
            Wrong_7.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Block_7Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "Block_7"-------
    for thisComponent in Block_7Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Response_7.keys in ['', [], None]:  # No response was made
       Response_7.keys=None
       # was no response the correct answer?!
       if str(corr(key, side, condition)).lower() == 'none': Response_7.corr = 1  # correct non-response
       else: Response_7.corr = 0  # failed to respond (incorrectly)
    # store data for trials_7 (TrialHandler)
    trials_7.addData('Response_7.keys',Response_7.keys)
    trials_7.addData('Response_7.corr', Response_7.corr)
    if Response_7.keys != None:  # we had a response
        trials_7.addData('Response_7.rt', Response_7.rt)
    
    # check responses
    if Keys_7.keys in ['', [], None]:  # No response was made
       Keys_7.keys=None
       # was no response the correct answer?!
       if str(corr(key, side, condition)).lower() == 'none': Keys_7.corr = 1  # correct non-response
       else: Keys_7.corr = 0  # failed to respond (incorrectly)
    # store data for trials_7 (TrialHandler)
    trials_7.addData('Keys_7.keys',Keys_7.keys)
    trials_7.addData('Keys_7.corr', Keys_7.corr)
    if Keys_7.keys != None:  # we had a response
        trials_7.addData('Keys_7.rt', Keys_7.rt)
    # the Routine "Block_7" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2 repeats of 'trials_7'


#------Prepare to start Routine "thanks"-------
t = 0
thanksClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_10 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_10.status = NOT_STARTED
# keep track of which components have finished
thanksComponents = []
thanksComponents.append(Thanks)
thanksComponents.append(key_resp_10)
for thisComponent in thanksComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "thanks"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = thanksClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Thanks* updates
    if t >= 1.0 and Thanks.status == NOT_STARTED:
        # keep track of start time/frame for later
        Thanks.tStart = t  # underestimates by a little under one frame
        Thanks.frameNStart = frameN  # exact frame index
        Thanks.setAutoDraw(True)
    if Thanks.status == STARTED and t >= (1.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        Thanks.setAutoDraw(False)
    
    # *key_resp_10* updates
    if t >= 0.0 and key_resp_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_10.tStart = t  # underestimates by a little under one frame
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_10.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "thanks" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()








win.close()
core.quit()
