class Person:
    name="Pushpa"
    occupation="Lal-chandan"
    netWorth=10000
    
    def PersonDetails(self):
        # print(f"I am {self.name},I do {self.occupation},My networth is {self.netWorth}")
        pass
    
Jenis=Person() # creating an object of the person class


Jenis.name="Jenis"
Jenis.occupation="Coding"
Jenis.netWorth=1000000000000000



# print(Jenis.name)
# print(Jenis.occupation)
# print(Jenis.netWorth)

Jenis.PersonDetails()
# if your method is def PersonDetails() means with 0 parameeters this will cause an error:
# # ❌ TypeError: Person.PersonDetails() takes 0 positional arguments but 1 was given 
#  1 argument was self (Ref of the object) that is given as an argument of the function call by the python implicitly when func of the object is called


# Author: Jenis Surani
# Topic: Class-Objects
# Date: 15/02/2025