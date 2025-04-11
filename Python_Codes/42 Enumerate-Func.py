# Enumerate function returns tuple as (index,value) value pair from any iterable

# list1=[11,22,33,44,55,66]
# for index,value in enumerate(list1):
#     print(f"Index:{index}   ,   Value:{value}")
    
# you can also specify the start index
# the loop will start counting index from the start index and goes till end

list2=[11,22,33,44,55,66]
for index,value in enumerate(list2,1):
    print(f"Index:{index}   ,   Value:{value}")

print(list(enumerate(list2))) # because print(enumerate(list2)) it returns enumerate object we need to typecast it
# now this will count from 11 as index 1 and goes till 66
# it will not count the index from 0 because start with 1 is specified means not start with index value 1 that is 22 #point to be noted

# it returns tuple as index value pair if you want it packed use single variable like

# for x in enumerate(list2):
#     print(x,end=" ")
    
# print(enumerate(list2))
    
# Author: Jenis Surani
# Topic:Enumerate function in python
# Date: 11/02/2025