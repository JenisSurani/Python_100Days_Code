# x=[12,13,14]
# # #returns the all the attributes and method present in the class list
# # print(dir(x))

# # #can know which function do what?
# print(x.reverse.__doc__)
# print(x.remove.__doc__)
# print(x.pop.__doc__)

# #to know object attributes only of an class use __dict__ attribute

class mine:
    
    def __init__(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id
        
mineobj=mine("Jenish",20,1)       
# print(mineobj.__dict__)


# to know the full details of the class use help method
# that prints the help documentation

# help(mineobj) #presss enter to see more in terminal

# in python every class extends object class############

# print(issubclass(mine,object))

# to know the base class of any class use __bases__ attribute

print(mine.__bases__)



class EmptyClass:
    pass

help(EmptyClass)


# Author : Jenis Surani
# Topic  : dir(),__dict__ & help()
# Date   : 22/02/2025