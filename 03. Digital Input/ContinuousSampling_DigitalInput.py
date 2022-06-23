'''
Copyleft © MoonNote

작성자 : MoonNote
블로그 주소 : MoonNote.tistory.com
'''

import nidaqmx
import time
import numpy as np

from ast import Break
from nidaqmx.constants import LineGrouping

data = np.zeros(4)

with nidaqmx.Task() as task :

    task.di_channels.add_di_chan("Dev1/port2/line0:3", "", line_grouping=LineGrouping.CHAN_PER_LINE)
    task.start()
    try:
        while True:
            data = task.read(1, timeout=10)
            print('port0/line0:3 data =', data)
            time.sleep(0.5)
    except KeyboardInterrupt:
        Break
        print('close the program')
    task.stop()
