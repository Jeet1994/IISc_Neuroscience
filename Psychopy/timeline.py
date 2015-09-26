from psychopy import core, visual, event
import csv, random, time
 
## Setup Section
win = visual.Window([800,600], fullscr=False, monitor="testMonitor", units='cm')
 
# turn the text strings into stimuli
textStimuli = []
for iTrial in range(10):
    # append this stimulus to the list of prepared stimuli
    text = "number: {}".format(iTrial)
    textStimuli.append(visual.TextStim(win, text=text)) 
 
# make a question stimulus
questionStimulus = visual.TextStim(win, text="Was this number larger than 4?")
 
# fixation cross
fixation = visual.ShapeStim(win, 
    vertices=((0, -0.5), (0, 0.5), (0,0), (-0.5,0), (0.5, 0)),
    lineWidth=5,
    closeShape=False,
    lineColor='white'
)
 
# open data output file
datafile = open("/tmp/datafile.csv", "wb")
# connect it with a csv writer
writer = csv.writer(datafile, delimiter=";")
# create output file header
writer.writerow([
    "number", 
    "response", 
    "responseTime",
    ])
 
  
## Experiment Section
n = len(textStimuli)
for i in random.sample(range(n), n):
    # present fixation
    fixation.draw()
    win.flip()
    core.wait(0.980) # note how the real time will be very close to a multiple of the refresh time
     
    # present stimulus text and wait a maximum of 2 second for a response
    textStimuli[i].draw()
    win.flip()
    textTime = time.time()
    wait = random.uniform(0.100, 0.500)
    core.wait(wait)
 
    # ask wheter the number was larger than 4
    questionStimulus.draw()
    win.flip()
    key = event.waitKeys(2.000, ['y','n', 'escape'])
    responseTime = time.time()
 
    # write result to data file
    if key==None:
        key=[]
        key.append("no key")
         
    writer.writerow([
        i, 
        key[0], 
        "{:.3f}".format(responseTime - textTime),
        ])
     
    if key[0]=='escape':
        break
datafile.close()
 
## Closing Section
win.close()
core.quit()