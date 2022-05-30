'''
Copyleft © MoonNote

작성자 : MoonNote
블로그 주소 : MoonNote.tistory.com
'''

import PyDAQmx
import numpy as np
from PyDAQmx import Task


data = np.array([0,0,0,0,0,0,0,0], dtype=np.uint8)

task = Task()
task.CreateDOChan("/cDAQ1Mod3/port0/line0:7","",PyDAQmx.DAQmx_Val_ChanForAllLines)
task.StartTask()
task.WriteDigitalLines(1,1,10.0,PyDAQmx.DAQmx_Val_GroupByChannel,data,None,None)
task.StopTask()
