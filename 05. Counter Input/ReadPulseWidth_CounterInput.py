'''
Copyleft © MoonNote

작성자 : MoonNote
블로그 주소 : MoonNote.tistory.com
'''

import nidaqmx

from nidaqmx.constants import TimeUnits, Edge

with nidaqmx.Task() as task :

    task.ci_channels.add_ci_pulse_width_chan("Dev1/ctr0","",min_val=0.000001,max_val=1,units=TimeUnits.SECONDS,starting_edge=Edge.RISING,custom_scale_name="")
    task.start()
    data = task.read(number_of_samples_per_channel=1,timeout=10)
    task.stop()
    print('[NI DAQmx Example - Counter Input]')
    print('Read Pulse Width : ',data,'s')