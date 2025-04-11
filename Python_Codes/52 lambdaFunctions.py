# lambda functions is one liner function

cube=lambda x: x**3
sum=lambda x,y: x+y
square= lambda a:a**2

print(cube(5))

# can also pass lambda function to another function as an argument

def func1(value,func):
    return 25 + func(value)

print(func1(5,lambda x:x**3))

#  lambda function is a small anonymous function without a name
# They are commonly used as arguments to higher-order functions, such as map, filter, and reduce.
# Lambda functions can also include multiple statements, but they are limited to a single expression. 

# Author: Jenis Surani
# Topic: Lambda function in python
# Date: 13/02/2025