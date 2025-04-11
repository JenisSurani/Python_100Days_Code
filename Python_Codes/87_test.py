# your sir denied to give you pdf but you are programmer;)

import shutil
import os
import time

file_path="This PC\\OnePlus 9R\\Internal shared storage\\PDFelement\\file_2"
saved_location="D:\\Coding\\Python_for_temp\\Tut87"

# print(time.strftime("%H:%M:%S"))

while True:
 print(time.strftime("%H:%M:%S")) 
 if os.path.exists(file_path):
     try:
        shutil.copy2(file_path,saved_location)
        print("done")
        break
     except:
         print("failed")
# after 5 min break the program if fails
         
 if time.strftime("%H:%M:%S")=="17:52:50":
    break
    
    