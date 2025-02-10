# WinBatteryHealth
WinBatteryHealth is a very basic Python module for getting the original maximum capacity, current maximum capacity and 
percentage battery health of your Windows laptop.

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
