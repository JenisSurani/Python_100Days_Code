class MyCustomError(Exception): # this class inherits exception class
    pass

try:
    # if something happend wrong
    a=int(input("Enter your salary: "))
    if not 20000<a<30000:
        raise MyCustomError
    print("correct!")
except MyCustomError:
    print("Some error occured")
    # if mycustomerror occurs 
    # send this error to admin
    # call an api
    

# Author: Jenis Surani
# Topic: Custom error
# Date: 10/02/2025