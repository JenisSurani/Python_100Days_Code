from typing import Union


#  Two types of function

# 1) Built in function:

# 2) User bulid function:

def greet(a):
    print(a,"Hello world")
    print(a,"Good morning")
    print(a,"Namste!!")
    print(end="\n")
    
greet("Jenish")
greet("Rahul")
greet("Shubham")

#  We know that python is dynamically typed meaning that fun can return diff types of value not any specified one
# Because if fun return value is holding by a , a will decided as int if fun retuns int , a as str if fun returns string so..

def example(x):
    if x>0:
        return "Positive" # returns string
    else:
        return -1

a=example(11)
b=example(-18)
print(a)
print(b) # means same function can return multiple type of data , because python is dynamically typed

#  if we dont provide any return type it returns None means void

def greet2():
    print("Good night")
    
s1=greet2()
print(s1) # means returning void that is none

#  for our info, we can use typehints for specifying parameters type and expected return type

def add(a:int,b:int)-> int:
    # print(a+b)
    return a+b

print(add(11,22)) # typehints tells a and b should be int and returun type should be int but not compulsory
print(add(18.92,17.25)) # this is also valid

# if your program gives diff returns type

def process(value:int) -> Union[int,str,float]: # means fun can return int or str or float
    if value>0:
        return value*2
    elif value==-12:
        return 12.25
    else:
        return "Negative value"
    
print(process(11))
print(process(-12))
print(process(-99))

a=[11,22]
print(type(a))


#  typehints for returning List,tuples,dictonaries

from typing import List

def get_num() -> List[int]: # means return list of int # List is just only used for typehints it is not wrapper class like java note that.
# def get_num() -> list[int]: # Python 3.9+, you can use list[int] instead.
    return [1,2,3,4,5,6,7,8]


print(get_num())

def get_value(a,b,d):
    pass #--> pass from here and start executing other code: 

# use this if you don't want to give body of function right now


# Author: Jenis Surani
# Topic: functions & typehints
# Date: 05/02/2025