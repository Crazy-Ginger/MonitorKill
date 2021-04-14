# MonitorKill

A basic python script the will move program from a monitor and disable it monitor if the GPU begins to overheat.

It uses [OpenHardwareMonitor](https://openhardwaremonitor.org/) to monitor GPU (or hardware) temperature. Then it uses NirSoft's [Multi-Monitor-Tool](http://www.nirsoft.net/utils/multi_monitor_tool.html) to move programs on the monitor to the primary monitor, if the monitor conitues to overheat the monitor will be disabled until the GPU has cooled.

## Setup
1. Install O[OpenHardwareMonitor](https://openhardwaremonitor.org/) and [Multi-Monitor-Tool](http://www.nirsoft.net/utils/multi_monitor_tool.html) to the directories where the script is located
2. Set script to be run at set intervals using Windows Scheduler

Currently all values such as monitor ID, GPU and threshold temperatures are **hard coded** in the script

**Use at own risk**
