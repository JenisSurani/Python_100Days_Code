# s1={"j":"jenis",19:"shubham","k1":"k","m":"mahi"}
# print(s1[191])
# print(s1.get("k1"))

# dictionaries are ordered collection of data with key:value pairs sep by , and encolsed with {}

info_candidate={'name':'krunal','age':50,'Eligible':False,'Dob':1970}
print(info_candidate)

#  to acess items
print(info_candidate['age']) # raise KeyError if key not found
print(info_candidate.get('age')) # returns none if key not found 

# to acess all the keys:
print(info_candidate.keys())
# to acess all the values
print(info_candidate.values())
# to acess all the keys and values both at once
print(info_candidate.items())

# to print key and values using for loop

# for key in info_candidate.keys():
    # print(f"The value of {key} is {info_candidate[key]}",end="  ")
    
    
#  or

for key,value in info_candidate.items():
    print(f"The value of {key} is {value}",end="  ")
    
my_dict = {
    "a": 10,
    "b": 20,
    "a": 30  # This will overwrite the previous "a": 10
}
print(my_dict)
# Output: {'a': 30, 'b': 20}
# Not allowed because dictionaries use unique keys

my_dict = {
    "a": 10,
    "b": 20,
    "c": 10,  # Duplicate value (10) is allowed
    "d": 30
}
print(my_dict)  
# Output: {'a': 10, 'b': 20, 'c': 10, 'd': 30}
# No issue because values can be repeated.

# Key Rules:
# Keys must be unique – If a duplicate key is assigned a new value, it overwrites the existing one.
# Values can be duplicated – Different keys can store the same value.

# Author: Jenis Surani
# Topic: Dictionaries
# Date: 09/02/2025