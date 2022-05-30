'''
작성자 : MoonNote
블로그 주소 : MoonNote.tistory.com
'''

from pickle import TRUE
import nidaqmx
import matplotlib.pyplot as plt

from ast import Break
from nidaqmx.constants import TerminalConfiguration

# 초기 x 값
x = 0
# plot 그리드 설정 및 y 스케일 지정
plt.grid()
plt.ylim(-10, 10)

with nidaqmx.Task() as task :
    
    task.ai_channels.add_ai_voltage_chan("Dev1/ai0","",terminal_config = TerminalConfiguration.RSE)
    
    try:
        while True:
            x = x + 0.001  
            y = task.read(number_of_samples_per_channel=1)

            plt.scatter(x, y, color = 'b')
            plt.pause(0.001)

            # 명령창 출력
            # print(y)
            # time.sleep(0.1)
    except KeyboardInterrupt:
        Break

plt.show()

