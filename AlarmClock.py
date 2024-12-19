import time
from datetime import datetime
def setalarm(t):
    print(f"Alarm time set to {t} done")
    while True:
        current = datetime.now().strftime("%H:%M:%S")
        
        if current == t:
            print("Wake up")
            break
        time.sleep(2)
Atime = input("Enter the time in HH:MM:SS format: ")
print(setalarm(Atime) )