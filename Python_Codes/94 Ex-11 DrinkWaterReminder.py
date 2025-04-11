import asyncio
from desktop_notifier import DesktopNotifier
from pathlib import Path  # Import Path
import time

notifier = DesktopNotifier(app_name="Jenish surani",app_icon=Path("D:\\photo.jpg"))

async def main():
    await notifier.send(title="Drinking Water Reminder", message="Please Hydrate Yourself!")

def reminder():
    for i in range(5):
        time.sleep(60)
        print(f"Notification {i} is sended sucessfully to user")
        #reminds after 1min for 5 times
        asyncio.run(main())
    
reminder()

# you can also schedule task in task scheduler
    
# Author : Jenis Surani
# Topic  : Ex-11 DrinkingWaterReminder
# Date   : 03/03/2025

