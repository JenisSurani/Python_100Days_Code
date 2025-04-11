# r1={}
info_candidate2={'name':'krunal','age':50,'Eligible':False,'Dob':1970}
info_candidate3={'name':'osama','age':1,'Eligible':True,'Dob':2024}


# # update():
# info_candidate2.update({'age':20})
# print(info_candidate2)

# info_candidate2.update({'nickname':"kalia"})
# print(info_candidate2)

# # if you want to add one single value,there is simple way to do that
# info_candidate2["height"]=120
# print(info_candidate2)

# # 1️⃣ Accessing a Non-Existent Key (Raises KeyError)
# # 2️⃣ Assigning a Value to a Non-Existent Key (Creates Key)

# # updating using dict also

# info_candidate2.update(info_candidate3)
# print(info_candidate2) # will override the same value

# # in dict if dup keys found last duplicate key ni value overide thase and treated as final

# # for dlting items

# info_candidate2.clear()
# print(info_candidate2)

# # info_candidate2.pop() # raise an error because pop method for dict requires one argument that is key if you want to pop the last iteem use popitem method
# info_candidate3.pop('age') # removes specific item from the dict
# print(info_candidate3)

# # info_candidate3.popitem() #
# #removes last items
# print(info_candidate3.popitem() )
# print(info_candidate3)

# using del

# del info_candidate3 # will dlt enitire dict
# print(info_candidate3) # raise NameError:

# using del with keyword:
del info_candidate3['name'] # raise KeyError if not found key in dict
print(info_candidate3)


# Author: Jenis Surani
# Topic: DictMethods
# Date: 09/02/2025