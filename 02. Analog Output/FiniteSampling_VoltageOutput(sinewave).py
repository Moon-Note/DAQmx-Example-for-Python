'''
Copyleft © MoonNote

작성자 : MoonNote
블로그 주소 : MoonNote.tistory.com
'''
import nidaqmx
import numpy as np
import math

from nidaqmx.constants import AcquisitionType, Edge

sampling_rate = 1000

with nidaqmx.Task() as task : 

    task.ao_channels.add_ao_voltage_chan("Dev1/ao0", "", -10, 10)
    task.timing.cfg_samp_clk_timing(sampling_rate, "", active_edge=Edge.RISING, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000)
    
    time = np.arange(0, 2*math.pi, 10*2*math.pi/sampling_rate)
    amplitude = 5*np.sin(time)
    
    task.write(amplitude, auto_start=False, timeout=10)
    task.start()
    task.wait_until_done(10)
    task.stop
