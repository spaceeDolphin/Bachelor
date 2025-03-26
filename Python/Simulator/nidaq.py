# python -m pip install nidaqmx
# check python support in ni installer
# documentation: https://github.com/ni/nidaqmx-python

import nidaqmx
import time
import pandas as pd
import csv
import numpy as np
from nidaqmx.constants import TerminalConfiguration
from datetime import datetime

sampleTime = 1
q_out_median = 16.6
q_max = 50.0
boost = 60
q_in_voltage = 1.5
simRuntime = 0

dataFrame_q_out = pd.read_csv('Simulator\hb402.csv')
#dataFrameLog = pd.DataFrame(columns=['Time', 'Qin', 'Qout', 'Level'])

# LOGGING
#def append_data_to_csv(time, qin, qout, level):
#    global dataFrameLog
#    new_row = pd.DataFrame({'Time': [time], 'Qin': [qin], 'Qout': [qout], 'Level': [level]})
#    dataFrameLog = pd.concat([dataFrameLog, new_row], ignore_index=True)
#    dataFrameLog.to_csv('Simulator\simLog.csv', index=False)

def append_data_to_csv(time, qin, qout, level):
    new_row = [time,qin,qout,level]
    file_name = "Simulator/simLog.csv"
    with open(file_name, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(new_row)

# TANK CLASS AND OBJECT DECLARATION
class Tank:
    def __init__(self, level, area):
        self.level = level
        self.area = area
        self.h = 4
        self.volume = self.h*area
        self.levelPercent = 100
        self.targetLevelPercent = 50
    
    def UpdateLevel(self, q_in, q_out):
        self.level += (1/self.area) * ((q_in/3600) - (q_out/3600)) * sampleTime * boost
        self.levelPercent = round(self.level/self.h * 100,1)

    def GetLevelVoltage(self):
        return self.level * (4/self.h) +1

hb = Tank(3, 170) # initial level, area m2

# LOOP INTERACTING WITH NI USB-6008
with nidaqmx.Task() as pump, nidaqmx.Task() as level, nidaqmx.Task() as flow:
    pump.ai_channels.add_ai_voltage_chan("Dev3/ai0", terminal_config=TerminalConfiguration.RSE, min_val=0.0, max_val=5.5)
    level.ao_channels.add_ao_voltage_chan("Dev3/ao0", min_val=1.0, max_val=5.0)
    flow.ao_channels.add_ao_voltage_chan("Dev3/ao1", min_val=1.0, max_val=5.0)

    while True:
        # INPUT
        data = pump.read()
        print("Spenning: ", round(data,2 ))
        q_in = (data-1) * (q_max/4) # voltage to m3/h
        if q_in < 0: q_in = 0

        # LOOKUP q_out from hb402.csv
        closest_index = (np.abs(dataFrame_q_out.iloc[:, 0] - simRuntime)).idxmin()
        q_out = dataFrame_q_out.iloc[closest_index, 1]

        hb.UpdateLevel(q_in, q_out)
        print(f"{simRuntime} Qin: {round(q_in,2)} Level: {round(hb.level,2)} ({hb.levelPercent}%) Qout: {round(q_out,2)}")
        #currentTime = datetime.now()
        append_data_to_csv(simRuntime, round(q_in,3), round(q_out,3), hb.levelPercent)

        # OUTPUT
        q_in_voltage = round(data,3)
        if (q_in_voltage < 1): q_in_voltage = 1
        elif (q_in_voltage > 5): q_in_voltage = 5
        level.write(hb.GetLevelVoltage())
        flow.write(q_in_voltage)

        # TIME
        simRuntime += sampleTime*boost
        if (simRuntime > 86400): simRuntime = 0
        time.sleep(sampleTime)