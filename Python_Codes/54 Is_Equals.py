# # == compares acutal value
# # is compares is element sharing same object or not!

# a=[11,22,33]
# b=[11,22,33]

# print(a==b)
# print(a is b)

# # #

# c="Jenish"
# d="Jenish"
# print(c==d)
# print(c is d)

# ##

# e=3
# f=3
# print(e==f)
# print(e is f)

# #  means imutable data items shares same object in the memory because they will not get changed ,cause they are immutable, so no sense to create sep objet for both e and f

# # but mutable object can be changed ,a and b can't share same object

# x=[1,2,3]
# y=x
# # now x and y is pointing to the same object
# print(x is y)
# print(x==y)

# y[0]=11
# print(x)
# print(y)

#  because x and y sharing the same object due to line 29

f=None
k=None

print(f==None)
print(f is None)
print(f is k)

# In java,

# int a = 11;
# a = 20;
# What Happens?
# int a = 11;
# The variable a is assigned the value 11.
# a = 20;
# The value 11 is replaced with 20, and a now holds 20.
# Is 11 Garbage?
# No, because int is a primitive data type in Java, and primitives are stored directly in memory (stack).
# When you reassign a = 20;, the value 11 is simply overwritten. It does not create garbage because it was never an object stored in the heap.

# Author: Jenis Surani
# Topic: Is and == operator in python
# Date: 14/02/2025