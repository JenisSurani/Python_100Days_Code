# # ✔ An alternative constructor is a special case of a factory method, providing different ways to create an object.

# when you have complex data use classmethod to create the object

class Person:
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    @classmethod
    # if you have complex data use this
    
    def fromstr(cls,string1:str):
        name,age=string1.split(",")
        return cls(name,age)
    

# if you have normal data use this

obj1=Person("Jenish surani",20)
print(obj1.name)         
print(obj1.age)      

# if you have complex data like "Jenish surani,20" at that time you cannot pass it to the constructor use @classmethod to initilizae the object

obj2=Person.fromstr("Jenish suranni,20")
print(obj2.name)         
print(obj2.age)  
   

# Author : Jenis Surani
# Topic  : @classmethod as an Alternative Constructors
# Date   : 22/02/2025