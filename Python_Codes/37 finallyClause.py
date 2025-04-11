# this block will executed no matter what!


try:
    num=int(input("Enter int number: ")) # int can convert 11.22 to 11 but not "11.22" to 11 so this will raise valueError
except ValueError:
    print("not a valid int")
else:
    print("num is accepted")
finally:
    print("I am always executed")
    
# one of the most use of the finally block is in function that is returning something

# def fun1()->int:
#     try:
#         ab=int(input("please enter your index: "))
#         my_list=[11,22]
#         abc=my_list[ab]
#         print(abc)
#         return 0 # if everything works fine
#     except:
#         print("some error occured")
#         return 1 # means error occured
#     finally:
#         print("i am always executed")
        
# acd=fun1()
# print(acd)

# finally executed if error happend or not
# try:
#     ab=int(input("please enter your index: "))
#     my_list=[11,22]
#     abc=my_list[ab]

#     print(abc)

# finally:
#     print("i am finally")
    

    
# Author: Jenis Surani
# Topic: finally clause
# Date: 10/02/2025