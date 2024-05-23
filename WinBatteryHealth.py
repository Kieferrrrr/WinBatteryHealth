# Importable Battery Health Monitor Module

# https://github.com/Kieferrrrr/WinBatteryHealth

import math
import subprocess

def OriginalMaxCapacity():
    OMC = int(subprocess.check_output("powershell.exe Get-WmiObject -Namespace 'root/wmi' -Query 'select DesignedCapacity from BatteryStaticData' | Select-Object -ExpandProperty DesignedCapacity").rstrip().decode())
    return OMC

def CurrentMaxCapacity():
    CMC = int(subprocess.check_output("powershell.exe Get-WmiObject -Namespace 'root/wmi' -Query 'select FullChargedCapacity from BatteryFullChargedCapacity' | Select-Object -ExpandProperty FullChargedCapacity").rstrip().decode())
    return CMC

def CurrentHealthPercentage():
    CHP = math.floor((CurrentMaxCapacity() / OriginalMaxCapacity()) * 100)
    return CHP
