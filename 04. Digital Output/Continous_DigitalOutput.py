'''
Copyleft © MoonNote

작성자 : MoonNote
블로그 주소 : MoonNote.tistory.com
'''

import nidaqmx
import numpy as np

from ast import Break
from nidaqmx.constants import LineGrouping

data = np.array([False,False,False,False], dtype=np.bool8)

with nidaqmx.Task() as task :
    
    task.do_channels.add_do_chan("Dev1/port1/line0:3", "", line_grouping=LineGrouping.CHAN_PER_LINE)
    task.start()
    try:
        while True:
            task.write(data, auto_start=False, timeout=10)
    except KeyboardInterrupt:
        Break
        print('close the program')
    task.stop()

