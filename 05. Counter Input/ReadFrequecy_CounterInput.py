'''
Copyleft © MoonNote

작성자 : MoonNote
블로그 주소 : MoonNote.tistory.com
'''

import nidaqmx
import time

from ast import Break
from nidaqmx.constants import FrequencyUnits, Edge, CounterFrequencyMethod

with nidaqmx.Task() as task :
    
    task.ci_channels.add_ci_freq_chan("Dev1/ctr0","",min_val=2,max_val=1000,units=FrequencyUnits.HZ,edge=Edge.RISING,meas_method=CounterFrequencyMethod.LOW_FREQUENCY_1_COUNTER,meas_time=0.1,divisor=4,custom_scale_name="")
    task.start()
    try:
        while True:
            data = task.read(1,timeout=10)
            print('[NI DAQmx Example - Measure Frequency]')
            print('Freq :',data,' Hz')
            time.sleep(1)
    except KeyboardInterrupt:
        Break
        print('close the program')
    task.stop()