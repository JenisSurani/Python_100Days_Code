import time

time.time() #method

def usingWhile():
    i=0
    while i<10000:
        print(i)
        i+=1
        
def usingFor():
    for i in range(10000):
        print(i)
     

# currenttime=time.time()
# usingFor()
# timeusingfor=time.time()-currenttime

# currenttimetime=time.time()
# usingWhile()
# timeusingwhile=time.time()-currenttimetime

# print(timeusingfor)
# print(timeusingwhile)


# #time.sleep() method

# print("Your 1minute timer starts from now:")

# for i in range(60):
#     time.sleep(1)
#     print(i+1)
    
# print("Times up!!")

#time.strftime():

# t=time.time() # returns time from epoch (January 1, 1970, 00:00:00)
tt=time.localtime() # returns tuple of local time in your computer
# print(t)
print(tt)

print(time.strftime("%d-%m-%y %H:%M:%S",tt)) # This  call always prints the time stored in tt.
print(time.strftime("%d-%m-%y %H:%M:%S")) # This call prints the latest current time at the moment of execution.


# shift + tab to remove indentation at once
# f11 for the full screen mode and exit as well 


# Author : Jenis Surani
# Topic  : TimeModule
# Date   : 24/02/2025