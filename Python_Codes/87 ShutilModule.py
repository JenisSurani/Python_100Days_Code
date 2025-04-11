# this will create 100 directory in the specified location
import shutil
import os

#freelancing task:
# Create 100 folder with day1,day2..day100 and in each folder include main.py

# for i in range(0,100):
#     os.mkdir(f"D:\\Coding\\Python_for_temp\\Tut87\\Day{i+1}")
#     shutil.copy("D:\\Coding\\Python_Codes\\main.py",f"D:\\Coding\\Python_for_temp\\Tut87\\Day{i+1}")
    

# to dlt those file
for i in range(100):
   shutil.rmtree(f"D:\\Coding\\Python_for_temp\\Tut87{i+1}")


# Author : Jenis Surani
# Topic  : ShutilModule
# Date   : 25/02/2025