'''
Copyleft © MoonNote

작성자 : MoonNote
블로그 주소 : MoonNote.tistory.com
'''

import nidaqmx
import numpy as np

from nidaqmx.constants import TimeUnits, AcquisitionType

with nidaqmx.Task() as task :

    task.ci_channels.add_ci_semi_period_chan("Dev1/ctr0","", min_val=0.000001, max_val=0.1, units=TimeUnits.SECONDS, custom_scale_name="")
    task.timing.cfg_implicit_timing(sample_mode=AcquisitionType.FINITE, samps_per_chan=6)
    task.start()
    data = task.read(6, timeout=10)
    disp_data = np.round(data, 3)
    task.stop()
    
    print('[NI DAQmx Example - Counter Input]')
    print('Read Pulse Semi-Period : ')
    print(disp_data)