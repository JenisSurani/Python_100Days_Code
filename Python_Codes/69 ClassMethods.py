class Example:
    
    def __init__(self,arg1,arg2):
        print(type(self))
        self.va1=arg1
        self.va2=arg2
    @classmethod
    def factory_method(cls,arg1,arg2):
        return cls(arg1,arg2) # automatically pass self as an 1st argu
    
    
obj1=Example.factory_method(11,22)
print(obj1) # it will say it is the object of the class example 

# # ❌ ERROR: TypeError: factory_method() missing 1 required positional argument: 'cls'
# 🔹 Why does this error happen?
# Because Python treats factory_method as a regular method and expects an instance (self), not a class if you don't use @classmethod decorator.

# it (@classmethod) forces python to pass class as an first argument



# 🔹 Example: Alternative Constructor
# Suppose we have a class that stores a person's birth year but we also want to create an object using their age instead.

# Here’s how we can define an alternative constructor using a class method:

# python
# Copy
# Edit
# from datetime import date

# class Person:
#     def __init__(self, name, birth_year):
#         self.name = name
#         self.birth_year = birth_year

#     @classmethod
#     def from_age(cls, name, age):  # Alternative constructor
#         current_year = date.today().year
#         birth_year = current_year - age  # Calculate birth year
#         return cls(name, birth_year)  # Return new object

# # Creating objects in two ways:
# p1 = Person("Alice", 1995)        # Using normal constructor
# p2 = Person.from_age("Bob", 25)   # Using alternative constructor

# print(p1.name, p1.birth_year)  # Alice 1995
# print(p2.name, p2.birth_year)  # Bob 1999
# ✔ The from_age() method allows us to create a Person object using age instead of birth year.
# ✔ It internally calculates the birth year and calls cls(name, birth_year).

# # 🔹 Key Differences
# Feature	Factory Method	Alternative Constructor
# Purpose	Creates objects with controlled logic	Provides different ways to create objects
# Use Case	Used when multiple steps or conditions are needed before creating an object	Used when object creation needs different input formats
# Example	Logging, validation, or caching before creating an object	Creating an object using different inputs (e.g., age instead of birth year)


# 🔹 Summary
# ✔ A factory method is a structured way to create objects instead of calling the constructor directly.
# ✔ An alternative constructor is a special case of a factory method, providing different ways to create an object.
# ✔ Both use @classmethod because they need access to the class (cls) to create new instances.


class company:
    company_name="GESHIP" # class variable
    
    @classmethod
    def change_company_name(cls,com_name):
        cls.company_name=com_name
        
        
obj11=company()
obj11.change_company_name("IDEA") # it changes for the obj11 company name means instance variable creates in method because we dont specify @classmethod 
# if we don't specify @classmethod self is passed and if we specify class is pass
print(company.company_name)




# Author : Jenis Surani
# Topic  : ClassMethod
# Date   : 22/02/2025