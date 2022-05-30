'''
작성자 : MoonNote
블로그 주소 : MoonNote.tistory.com
'''

import nidaqmx
import numpy as np
import matplotlib.pyplot as plt

from ast import Break
from nidaqmx.constants import TerminalConfiguration, AcquisitionType, Edge

plt.grid()
plt.ylim(-10, 10)
plt.ion()

sampling_rate = 1000
Read_data = 100

i = 0
data = np.zeros((1,1), dtype = np.float64)

with nidaqmx.Task() as task :

    task.ai_channels.add_ai_voltage_chan("Dev1/ai0", "", terminal_config = TerminalConfiguration.RSE)
    task.timing.cfg_samp_clk_timing(sampling_rate, "", active_edge=Edge.RISING, sample_mode=AcquisitionType.CONTINUOUS, samps_per_chan=Read_data)
    task.start()
    
    try:
        while True:
            
            x = np.arange(i, i+Read_data, 1, dtype=float)
            data = task.read(Read_data, 10)

            plt.plot(x, data, color='b')
            plt.pause(0.001)

            i = i + Read_data
    except KeyboardInterrupt:
        Break
        print('close the program')

