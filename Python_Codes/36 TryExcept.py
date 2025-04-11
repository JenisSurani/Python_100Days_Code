# Exception handling is the process of responding to unwanted or unexpected events when a computer program runs. Exception handling deals with these events to avoid the program or system crashing, and without this process, exceptions would disrupt the normal operation of a program.

try:
    a=int(input("Enter the number: "))
    print(a*a)
except Exception as e:
    print(e)
    print("Please enter the correct number")
   
 
# try:
#     a=int(input("Enter the number: "))
#     print(a*a)
# except ValueError:
#     print("Please enter the correct number")
    
    

try:
    a=int(input("Enter the 1st number: "))
    b=int(input("Enter the 2nd number: "))
    list11=[a,b]
    print(list11[a])
    print(a/b)
except ZeroDivisionError as e:
    print(e)
    print("Please enter the correct number")
except IndexError as p:
    print(p)
except:
    print("for all the other exception print this")
    
    
try:
    a=int(input("Enter the 1st number: "))
    b=int(input("Enter the 2nd number: "))
    print(a/b)
except:
    print("Please enter the correct number")
     


# Python has many built-in exceptions that are raised when your program encounters an error

# Author: Jenis Surani
# Topic: Exception Handling,try-except block
# Date: 09/02/2025