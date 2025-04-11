import time
time1=time.strftime("%H:%M:%S")
print("Time in your area is:",time1)

time2=int(time.strftime("%H"))
# print(type(time.strftime("%H"))) # it returns string as time so we need to typecast it into int
# print(time2)

time3=int(time.strftime("%M"))
# print(time3)

time4=int(time.strftime("%S"))
# print(time4)


if (5 <= time2 <= 11):
    print("Good Morning! 🌅 ,Jenis: Let's Start Work")
elif 12 <= time2 <= 16:
    print("Good Afternoon! ☀️ ,Jenis: Let's have cup of tea")
elif 17 <= time2 <= 20:
    print("Good Evening! 🌆 ,Jenis: Let's start doing work again")
else:
    print("Good Night! 🌙 ,Jenis Sweet Dreams!!")


# Author: Jenis Surani
# Topic: Exercise-2:
# Date: 04/02/2025