# Map function

List1=[1,2,3,4,5,6,7,8]

cube=list(map(lambda x: x**3,List1))  # typecast the map object to the lists
print(cube)

print(type(map(lambda x: x**3,List1))) ## returns the map object

# Filter Function:

List2=[1,2,3,4,5,6]

# filter out the even number in the list2

even=list(filter(lambda x: x&1==0,List2)) # typecast the filter object to the list
print(even)
print(type(filter(lambda x: x&1==0,List2)))

# filter function takes predicate as an argument means function who returns the boolean value

# Reduce function

# to use this function we have to import it first from the module functools

from functools import reduce 

List3=[11,22,33,44,55,66]

SumOfList= reduce(lambda x,y: x+y , List3) # returns the int
print(type(SumOfList))
print(type(reduce(lambda x,y: x+y , List3)))
print("The sum of the list is:",SumOfList)


# we can use map,flter,reduce with any iterable not only list
# Higher order function means function who takes function as an arguments so map , filter and redcue are the higher-order function

# filter ma function (predicate) means boolean return kare tevu hovu pde




# Author: Jenis Surani
# Topic: Map_Filter_Reduce in python
# Date: 14/02/2025