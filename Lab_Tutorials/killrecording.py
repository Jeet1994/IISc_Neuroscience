#!/usr/bin/python

import os, subprocess, signal

p = subprocess.Popen(['ps','-aux'], stdout = subprocess.PIPE)
out, err = p.communicate()

for line in out.splitlines():
    if 'Final_Acq_Code' in line:
        pid = int((line.split(None,1)[1]).split(" ")[0])
        os.kill(pid, signal.SIGKILL)

