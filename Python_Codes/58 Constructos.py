# Main Purpose of the constructor is to initilizae or assign the values to the data members of the class

class Person:
    # name="Pushpa"
    # occupation="Lal-chandan"
    # netWorth=10000
    
    def PersonDetails(self):
        print(f"I am {self.name},I do {self.occupation},My networth is {self.netWorth}")
    
    def __init__(self,name:str,occupation:str,networth:int):
        self.name=name
        self.occupation=occupation
        self.netWorth=networth
        
    # def __init__(self):
    #     pass
    
    def Example(self,a,b,c):
        pass
    
# when you don't specify any construtor defalut will be called:

# that's look like:

# Equivalent Default Constructor (Implicitly Provided by Python)
# def __init__(self):
    # pass
    
# if you specify your own Constructor you have to give satisfying arguments to the constructor while creating an object

# Jenis=Person()
# will be called like Jenis=Person(self) --> implicitly called __def__(self)

# but if you provide parameterized constructor then:

# Jenis=Person() you can't call it until and unless you manually specify like 
# Error: TypeError: Person.__init__() missing 3 required positional arguments: 'name', 'occupation', and 'networth'

# Equivalent Default Constructor (Implicitly Provided by Python)
# def __init__(self):
    # pass 
    
    
    
# this construcor

Jenis=Person("Jenis","COding","1000000000")

print(Jenis.PersonDetails())

# print(Jenis.Example(1,2,3,4)) # you see that acutal fun accept 4 para , but we can pass exact 3 argu because self is passed automatically when function call is happen
print(Jenis.Example(1,2,3)) # allowed

# TypeError: Person.Example() takes 4 positional arguments but 5 were given
# if you give 4 argu interpreter shows 5 argu as shown in error , so one argu is self(ref of the current object)


# so when fun or constructor call is happend , self will be automaticcally passed as an argu in the func or constuctor
# so we need to specify the self when initilizing the construtor or func
# otherwise use @statcimethod

# __def__ is a dunder method to initilizae object






# Is self Always the First Parameter in a Class Method?

'''
Yes, self is always required in instance methods, but it does not have to be the first parameter—although it's strongly recommended to keep it first for readability and convention.

Can self Be at 2nd or 3rd Position?
Yes, technically, you can place self anywhere, but calling the method normally will cause errors because Python implicitly passes the instance (self) as the first argument.

Example (Incorrect Placement - Causes Error)
python
Copy
Edit
class Example:
    def show_message(msg, self):  # ❌ 'self' is not first
        print(f"Message: {msg}")

obj = Example()
obj.show_message("Hello")  
# ❌ TypeError: show_message() missing 1 required positional argument: 'self'
🔴 Why does this fail?

When calling obj.show_message("Hello"), Python automatically passes self as the first argument.
But here, the method expects msg first, so it misplaces arguments.
Correct Way: self First
python
Copy
Edit
class Example:
    def show_message(self, msg):  # ✅ 'self' first
        print(f"Message: {msg}")

obj = Example()
obj.show_message("Hello")  # ✅ Works fine
# Output: Message: Hello
✅ Why does this work?

self receives the instance reference automatically, and msg correctly gets "Hello".
Can We Use self at a Different Position & Still Make It Work?
Yes! But you'd have to manually pass self when calling the method.

Example: self at 2nd Position (Manual Calling)
python
Copy
Edit
class Example:
    def show_message(msg, self):  # 'self' at 2nd position
        print(f"Message: {msg}")

obj = Example()
Example.show_message("Hello", obj)  # ✅ Works, but not recommended
⚠️ This works, but it's unnatural and confusing. You must call the method using the class name and manually pass the instance (obj), which defeats the purpose of using instance methods.

'''

# Author: Jenis Surani
# Topic: Constructors
# Date: 15/02/2025