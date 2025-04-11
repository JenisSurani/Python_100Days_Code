# Sets in python more or less work in the same way as sets in mathematics.
# We can perform operations like union and intersection on the sets just like in mathematics.

# union() and update():

cities={"surat","ahmedabad","mehsana","rajkot","jamnagar","amreli"}
cities2={"surat","amreli","bhavnagar","rajkot","mumbai"}

# cities3=cities.union(cities2) # cities3 holding A U B
# print(cities3)
# print(cities)

# if you want to update orignal cities with union of cities and cities2 use update() method

# cities.update(cities2)
# print(cities)
# now cities hold A U B


#  intersection and intersection_update():
#  (ched gan)

# cities4=cities.intersection(cities2) # now cities4 hold A ∩ B
# print(cities4) 

# if you want to update orignal cities with intersection of cities and cities2 use intersection_update() method:

# cities.intersection_update(cities2)
# print(cities) # now cities hold A ∩ B



# symmetric_difference and symmetric_difference_update():

#  means will give = union of A-A ∩ B and B- A ∩ B:
# A Δ B = (A - B) U (B - A).

# cities5=cities.symmetric_difference(cities2)
# print(cities5) # unioun without common values

# if you want to update orignal cities with symmetric_difference of cities and cities2 use symmetric_difference_update() method:

# cities.symmetric_difference_update(cities2)
# print(cities)



# difference() and difference_update():
# A - B and B-A

# cities6=cities.difference(cities2)
# print(cities6) # this is A - B

cities7=cities2.difference(cities)
print(cities7) # this is A - B


# if you want to update orignal cities with difference of cities and cities2 use difference_update() method:

# cities.difference_update(cities2)
# print(cities) # updated citites with cities-cities2

cities2.difference_update(cities)
print(cities2) # updated citites2 with cities2-cities


# isdisjoint():

#  if A and B both are unique then-->True
#  if A and B have any one element common then--> False

citiesx={"chennai","surat","mumbai"}
citiesy={"rajkot","berlin","delhi"}#,"chennai"}

print(citiesx.isdisjoint(citiesy))

# issuperset():

#  if A.issuperset(B) means if B is subset A or A contains all value of B then-->true
#  if B.issuperset(A) means if A is subset of B or B contains all value of A then-->true
#  otherwise-->false

citiesz={"chennai"}
print(citiesx.issuperset(citiesy)) # false
print(citiesx.issuperset(citiesz)) # true

# issubset():

print(citiesz.issubset(citiesx)) # true
print(citiesy.issubset(citiesx)) # false

# add()

# If you want to add a single item to the set use the add() method.

cities111 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities111.add("surat")
print(cities111)

# update()

# If you want to add more than one item, simply create another set or any other iterable object(list, tuple, dictionary), and use the update() method to add it into the existing set.

ct=["kalupur","nagpur"]
print(type(ct))
cities111.update(ct)
print(cities111)



# some chatgpt writing here


# remove()/discard()

# The main difference between remove and discard is that, if we try to delete an item which is not present in set, then remove() raises an error, whereas discard() does not raise any error.

cities22 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities22.remove("Tokyoo") # will raise an error
# cities22.remove("Tokyo")
# print(cities22)

# cities22.discard("Tokpyo") # will not raise any error if element not found
# cities22.discard("Tokyo") 
# print(cities22)

# pop()
# This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered.

# However, you can access the popped item if you assign the pop() method to a variable.
popedItem=cities22.pop()
print(cities22)
print(popedItem)


# del
# del is not a method, rather it is a keyword which deletes the set entirely.

# meaning that variable set_name stop ref to set and after that the variable set_name is removed from the local or global namespace
# If there are no more references to that set object, Python’s garbage collector (GC) will free the memory occupied by the set.
# del cities22
# print(cities22) # raise an error

# NameError: name 'cities22' is not defined We get an error because our entire set has been deleted and there is no variable called cities22 which contains a set.


# What if we don’t want to delete the entire set, we just want to delete all items within that set?

# clear():
# This method clears all items in the set and prints an empty set.

cities22.clear()
print(cities22) # returns an empty set that is set() not {} we saw it earlier

# Check if item exists
# You can also check if an item exists in the set or not.

if "surat" in cities:
    print("surat is present")
else:
    print("surat is absent")
    
 # set it self is m mutable means you can add items/remove items
ab={"ss","dd","mm"}
print(ab.add("jenis"))
print(ab)

#  but items it self is immutable means you can't add those items that is mutable
# a={"string",[11,22]}
# ab={"ssd",{11,22}} # set items it self is imutable means error:


# print(ab)
# print(a)

#  Let's talk about tuple then
# tuple itself is immutable but items are mutable

# tuple is imuutable means you can't add or remove items from tuple until and unless you convert the tuple into list and then create new tuple and reasign to the same variable
# that is true.

# tuple items are mutable means only those items are mutable that type is mutable itself
#  means you can't change or modify the tuple inside the tuple because you say items of tuple is mutable
#  only those item who is natrually mutable we can only modify it


b=(1,2,"string",[11,22]) # we can add mutable & immutable items because item of tuple is mutavkle itself
print(b)
b[3][0]=66 # we can also change them because item inside tuple is mutable if it is natrually mutable
print(b) # that prints (1, 2, 'string', [66, 22]) 

#  means acutal tuple is not changed:

# my_tuple  -->  (  1   ,   2   ,   ref  )  
                        #            |
                        #            v
                        #           [3, 4]   # List (mutable object)
                        
 # # my_tuple  -->  (  1   ,   2   ,   ref  )  
#                                       |
#                                       v
 #                                      [5, 4]   # List (mutable object)
 
#   Actual tuple is still imutable see:
# The tuple stores a reference (memory address) to this list, not the list's actual values.

# If you try to reassign my_tuple[2], Python will throw an error:

# my_tuple[2] = [5, 6]  # ❌ TypeError: 'tuple' object does not support item assignment
# This fails because tuples cannot change their structure—you can't replace an element.

# int, float, bool, str, tuple, frozenset, bytes--->	Immutable
# list, dict, set, bytearray-->	Mutable
# Tuple containing mutable objects-->	Partially mutable
                        
       
# Author: Jenis Surani
# Topic: SetsMethods
# Date: 08/02/2025











