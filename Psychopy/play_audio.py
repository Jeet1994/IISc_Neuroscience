from psychopy import core, sound
s = sound.Sound(value='C', secs=0.5) 
 
s.play()
core.wait(4.0)
 
core.quit()