# MonitorKill

A basic python script which moves programs from a monitor and can then disable it if the GPU begins to overheat.

It uses [OpenHardwareMonitor](https://openhardwaremonitor.org/) to monitor GPU (or hardware) temperature. Then it uses NirSoft's [Multi-Monitor-Tool](http://www.nirsoft.net/utils/multi_monitor_tool.html) to move all programs to the primary monitor (lessening load on GPU), if the monitor conitues to overheat it will be disabled until the GPU has cooled.

## Setup
1. Install [OpenHardwareMonitor](https://openhardwaremonitor.org/) and [Multi-Monitor-Tool](http://www.nirsoft.net/utils/multi_monitor_tool.html) to the directories where the script is located
2. Set script to be run at set intervals using Windows Scheduler

Currently all values such as monitor ID, GPU and threshold temperatures are **hard coded** in the script

**Use at own risk**

This was written to solve issues with passively cooled GPU's overheating, would not recommend long term use.
