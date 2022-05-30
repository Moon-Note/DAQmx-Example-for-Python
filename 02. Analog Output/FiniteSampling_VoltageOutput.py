'''
Copyleft © MoonNote

작성자 : MoonNote
블로그 주소 : MoonNote.tistory.com
'''
import PyDAQmx
from PyDAQmx import Task


value = 0

task = Task()
task.CreateAOVoltageChan("/cDAQ1Mod2/ao0","",-10.0,10.0,PyDAQmx.DAQmx_Val_Volts,None)
task.StartTask()
task.WriteAnalogScalarF64(1,10.0,value,None)
task.StopTask()
