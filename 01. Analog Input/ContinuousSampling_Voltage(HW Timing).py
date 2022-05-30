'''
작성자 : MoonNote
블로그 주소 : MoonNote.tistory.com
코드 참조 : https://stackoverflow.com/questions/60947373/continuous-analog-read-from-national-instruments-daq-with-nidaqmx-python-package
'''


import nidaqmx
import numpy as np
import matplotlib.pyplot as plt

from ast import Break
from nidaqmx.constants import TerminalConfiguration, AcquisitionType, Edge

# plot 그리드 설정 및 y 스케일 지정
plt.grid()
plt.ylim(-10, 10)
#Interative-ON 함수임, ioff()와 서로 상반된 기능
#ioff() - 데이터를 입력해도 따로 plt에 표시되지 않고 plt.show() 명령을 줄 때 한번만 그리게 됨
#ion() - 데이터 입력을 주면 실시간으로 업데이트 됨
plt.ion()

# 샘플링 속도 및 읽을 샘플 개수
sampling_rate = 1000
Read_data = 100

# 데이터 변수 생성
i = 0
data = np.zeros((1,1), dtype = np.float64)

with nidaqmx.Task() as task :
    # Device 설정
    task.ai_channels.add_ai_voltage_chan("Dev1/ai0", "", terminal_config = TerminalConfiguration.RSE)
    task.timing.cfg_samp_clk_timing(sampling_rate, "", active_edge=Edge.RISING, sample_mode=AcquisitionType.CONTINUOUS, samps_per_chan=Read_data)
    task.start()
    
    try:
        while True:

            # DAQ Read Data
            x = np.arange(i, i+Read_data, 1, dtype=float)
            # # x 배열 크기 확인용 print(x.size)
            data = task.read(Read_data, 10)
            #print(data)

            plt.plot(x, data, color='b')
            plt.pause(0.001)

            i = i + Read_data
    except KeyboardInterrupt:
        Break
        print('close the program')
        # ? While 루프 종료 후 자동으로 리소스가 삭제되었다고 메시지 뜸..
        # ? task close를 안해줘도 되는 것인지 조금 헷갈림..
        # ? task.close()
# plt.show() 




    



    # ? StackOverflow에 있던 자료..제대로 이해 못함(보류)
    # stream = stream_readers.AnalogMultiChannelReader(task.in_stream)
    # # num_samples is set to bufsize
    # num_samples = bufsize
    # def reading_task_callback(task_id, event_type, num_samples, callback_data=None):
    #     # probably better to define it here inside the callback
    #     buffer = np.zeros((1, num_samples), dtype = np.float32)
    #     stream.read_many_sample(buffer, num_samples, timeout = constants.WAIT_INFINITELY)
    #     # hopping to retrieve this data after the read is stopped
    #     data = np.append(data, buffer, axis = 1)

    # task.register_every_n_samples_acquired_into_buffer_event(bufsize, reading_task_callback)

