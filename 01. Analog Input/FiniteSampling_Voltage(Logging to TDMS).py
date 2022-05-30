import PyDAQmx
import numpy as np
import matplotlib.pyplot as plt

from PyDAQmx import Task, DAQmxResetDevice, int32
#파이썬용 외부 함수 라이브러리, C호환 데이터형을 제공하며 DLL 또는 공유 라이브러리에 있는 함수를 호출할 수 있음
from ctypes import byref
#TDMS 라이브러리 import
from nptdms import TdmsWriter, ChannelObject


class AIParameters(object):
    limits = (-10, 10)
    physicalChannel = ["/Dev1/ai0"]

    def __init__(self, sample_rate, sample_number, channels=None, limits=None):
        self.sampleRate = sample_rate
        self.sampleNumber = sample_number
        if limits is None:
            limits = self.limits
        self.limit_inf= limits[0]
        self.limit_sup= limits[1]
        if channels is not None:
            if type(channels) is str:
                physicalChannel = [channels]
            self.physicalChannel = channels

    @property
    def device_name(self):
        device_name = self.physicalChannel[0].split('/')[0]
        if device_name == '' :
            device_name = self.physicalChannel[0].split('/')[1]
        return device_name

class Trigger(object):
    def __init__(self, terminal):
        self.terminal = terminal

class RisingTrigger(Trigger):
    direction = PyDAQmx.DAQmx_Val_Rising
         
class FallingTrigger(Trigger):
    direction = PyDAQmx.DAQmx_Val_Falling


class AIVoltageChan(Task):
    def __init__(self, ai_param, reset=True, terminalConfig=PyDAQmx.DAQmx_Val_RSE, trigger=None):
        if reset:
            DAQmxResetDevice(ai_param.device_name)
        super(AIVoltageChan, self).__init__()
        self.sampleNumber = ai_param.sampleNumber
        self.sampleRate = ai_param.sampleRate
        self.limit_inf = ai_param.limit_inf
        self.limit_sup = ai_param.limit_sup
        self.physicalChannel = ai_param.physicalChannel
        self.numberOfChannel = len(ai_param.physicalChannel)
        if isinstance(terminalConfig, str):
            terminalConfig = getattr(PyDAQmx, terminalConfig)
        self.terminalConfig = terminalConfig
        self.trigger = trigger
        self.configure()
    def configure(self):
        channel_string = ','.join(self.physicalChannel)
        self.CreateAIVoltageChan(channel_string,"",self.terminalConfig,
                                 self.limit_inf,self.limit_sup,
                                 PyDAQmx.DAQmx_Val_Volts,None)
    def start(self):
        n = self.sampleNumber
        sampleRate = self.sampleRate
        self.CfgSampClkTiming("",sampleRate,PyDAQmx.DAQmx_Val_Rising,PyDAQmx.DAQmx_Val_FiniteSamps,n)
        if self.trigger is not None:
            self.CfgDigEdgeRefTrig(self.trigger.terminal,self.trigger.direction,10)
        self.StartTask()
    def read(self):
        n = self.sampleNumber
        data = np.zeros((n,self.numberOfChannel), dtype=np.float64)
        read = int32()
        self.ReadAnalogF64(n,10.0,PyDAQmx.DAQmx_Val_GroupByScanNumber,data,n*self.numberOfChannel,byref(read),None)
        return data
    def stop(self):
        self.StopTask()
    def wait(self, timeout=10):
        self.WaitUntilTaskDone(timeout)


if __name__=="__main__":  #['/dev1/ai0', '/dev1/ai1'], reset 옵션 사항으로 직접 추가
    ai = AIVoltageChan(ai_param=AIParameters(1000, 1000,['/dev1/ai0']), reset=False, 
                    terminalConfig="DAQmx_Val_RSE", #DAQmx_Val_Diff, DAQmx_Val_RSE, DAQmx_Val_NRSE,  DAQmx_Val_PseudoDiff
                    trigger=None)#RisingTrigger('/dev1/PFI0'))
    ai.start()
    ai.wait()
    #ai 읽기 데이터
    a = ai.read()
    #result 변수에 AI 값 1차원으로 변경하여 입력
    result = np.ravel(a, order='C')
    #명령창 출력
    #print(result, type(result))

    #AI 데이터 TDMS 저장
    with TdmsWriter("C:/Users/user/Desktop/PythonDAQmxAI.tdms") as tdms_writer:
        data_array = result                      #np.linespace(0, 1, 10)
        channel = ChannelObject('Group', 'AI 01', data_array)
        tdms_writer.write_segment([channel])

    # Matplotlib Pyplot 디스플레이
    x = np.linspace(0, 1000, 1000)
    y = result
    
    fig, ax = plt.subplots()
    ax.plot(x, y)

    plt.show()
    
    ai.stop()