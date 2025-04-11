# Tuples are immutable

tup1=(1)
print(type(tup1)) # returns int because of confusion so avoiding this use , to tell it is tuple not int

tup1=(1,)
print(type(tup1)) # returns tuple

# can acess tuple using positive , negative indec like list:

# cam slice tuple using this syntax
#  tuple[start:end:jumpIndex] # same as the list
#  remember orignal tuple can't change so it's returning new tuple bcz tuple are immutable

country=("India","Spain","USA","China","Japan","Italy")

if "Spain" in country:
    print("Spain is present")
else:
    print("Spain is absent")


# A tuple in Python is immutable, meaning once it is created, its elements cannot be changed, added, or removed. This is by design because tuples are meant to be hashable (if they contain only hashable types) and used as dictionary keys or in sets.

# Strings are also immutable, but Python provides methods like .replace(), .upper(), etc., which return a new string with the modifications.

 #Tuples, however, do not provide methods like .replace() or .append() because their primary purpose is to be fixed collections of elements. The lack of modification methods ensures that they remain truly immutable.
 
#  Tuples are immutable to ensure hashability and safe usage as dictionary keys.

# Author: Jenis Surani
# Topic: Tuples
# Date: 06/02/2025