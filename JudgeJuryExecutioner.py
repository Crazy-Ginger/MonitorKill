from os import system
from time import sleep

import clr

clr.AddReference('OpenHardwareMonitor/OpenHardwareMonitor')
from OpenHardwareMonitor.Hardware import Computer

c = Computer()
c.GPUEnabled = True
c.Open()
for hard in c.Hardware:
    if "NVIDIA NVIDIA GeForce GTX 660" == str(hard.Name):
        if hard.Sensors[0].Value > 87.0:
            system("MultiMonitorTool\\MultiMonitorTool.exe /MoveWindow Primary All")
            quit()
        elif hard.Sensors[0].Value > 92.0:
            system("MultiMonitorTool\\MultiMonitorTool.exe /disable 1")
            while hard.Sensors[0].Value > 85.0:
                sleep(4)
                hard.Update()
            system("MultiMonitorTool\\MultiMonitorTool.exe /enable 1")
            quit()
        else:
            quit()
