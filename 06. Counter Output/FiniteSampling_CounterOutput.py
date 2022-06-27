'''
Copyleft © MoonNote

작성자 : MoonNote
블로그 주소 : MoonNote.tistory.com
'''

import nidaqmx

from nidaqmx.constants import FrequencyUnits, Level, AcquisitionType

with nidaqmx.Task() as task :

    task.co_channels.add_co_pulse_chan_freq("Dev1/ctr0","", units=FrequencyUnits.HZ, idle_state=Level.LOW, initial_delay=0.0, freq=10.0, duty_cycle=0.5)
    task.timing.cfg_implicit_timing(sample_mode=AcquisitionType.FINITE,samps_per_chan=10)
    task.start()
    task.wait_until_done(-1)
    task.stop