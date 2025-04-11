s1={ True,False,11,22,33.266,-888,"Jenis","Mahesh",2}
print(s1)

#  Sets are:
# unordered
# unchangeable
# don't contain any duplicate value

s2={22,22,22,22,22}
print(s2) # will only print 22 once because set donot contain any duplicate value

s3={}
print(type(s3)) # this will give type dict

# to create empty set
s4=set() # use set method to create empty set 
print(type(s4)) 

# ordered of printing set value genrates randomly so you cannot access set value with index
#  you can print them using for in loop

for items in s1:
    print(items,end=" ")
    
# In maths the defenation of set is like that:
# set is collection of well define objects , in python everyhing is oject so this def suits!!

# If you want to collects item without any repetation use sets for that work


# Author: Jenis Surani
# Topic: Sets
# Date: 08/02/2025