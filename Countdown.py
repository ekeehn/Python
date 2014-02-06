import os
import subprocess

wait = str(input("Press Enter to start countdown....."))
i = 5
while i > 0:
    print(i)
    i -= 1

print("BOOM!")
##subprocess.call('start "" "C:\\Program Files\\Notepad++\\notepad++.exe"')
os.system('start "" "C:\\Program Files\\Notepad++\\notepad++.exe"')
wait = str(input("Press Enter to continue....."))
