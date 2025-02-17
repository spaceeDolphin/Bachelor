# python -m pip install nidaqmx
# check python support in ni installer
# documentation: https://github.com/ni/nidaqmx-python

import nidaqmx

with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("Dev1/ai0", min_val=1.0, max_val=5.0)
    task.read()