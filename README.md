# WinBatteryHealth
WinBatteryHealth is a very basic Python module for getting the original maximum capacity, current maximum capacity and 
percentage battery health of your Windows laptop.
![image](https://github.com/Kieferrrrr/WinBatteryHealth/assets/157843487/98d3c5cf-efa4-4195-9417-6f49648078e4)

## BHM.py
WinBatteryHealth comes with the BHM.py file which demonstrates the simple use of this module

## Installation Through Git Clone
```shell
git clone https://github.com/Kieferrrrr/WinBatteryHealth
```

## Download the Module Alone
```python
import requests

moduleContent = requests.get("https://raw.githubusercontent.com/Kieferrrrr/WinBatteryHealth/main/WinBatteryHealth.py")

pyFile = open("WinBatteryHealth.py")
pyFile.write(moduleContent)
pyfile.close()
```

## Module Use
```python
import WinBatteryHealth

print(WinBatteryHealth.OriginalMaxCapacity())     # e.g. 60000 
print(WinBatteryHealth.CurrentMaxCapacity())      # e.g. 30000
print(WinBatteryHealth.CurrentHealthPercentage()) # e.g. 50
```
