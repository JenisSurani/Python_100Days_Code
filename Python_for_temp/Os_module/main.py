import os
import shutil

# both module are for the operating system

# this will create directory in the current directory
# os.mkdir("Jenish")


# this will create 100 directory in the specified location
# for i in range(0,100):
#     os.mkdir(f"Jenish/Day{i+1}")


# this will delete the empty directory specified in the location 
shutil.rmtree
for i in range(22,30):
    os.rmdir(f"Jenish/Tutorial-{i+1}")
    

#  if you want to rename the dicectory name then use this
# for i in range(0,100):
#     os.rename(f"Jenish/Tutorial{i+1}",f"Jenish/Tutorial-{i+1}")
#     #            source                    Destination


# this needs permission in your OS because this will dlt the directory
# for i in range(0,100):   
#     os.remove(f"Jenish/Day{i+1}")

# list all the directory present in the specified directory/location returns as List of all directory
# folder=os.listdir("Jenish")
# print(folder)


# for folder in os.listdir("D:/2nd year/4th sem"):
#     print(folder)
#     print(os.listdir(f"D:/2nd year/4th sem/{folder}"))
    

# print(os.listdir(f"D:/2nd year/4th sem/CN/Darshan Material"))

# to get your current direcotry
# print(os.getcwd())

# to change your current directory
# os.chdir("D:/2nd year")

# print(os.getcwd())



# import os
# 
# cmd='date'
# 
# os.system(cmd)
# this method will be used in the cmd prompt


    