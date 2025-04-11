# class Employee:
    
#     def __init__(self,name,age,id):
#         self.name=name
#         self.age=age
#         self.id=id
        
#     def __str__(self):
#         return f"{self.name} is {self.age} years old"
    
#     def __repr__(self):
#         return f"Employee({self.name},{self.age},{self.id})"
    
#     def __len__(self):
        
#         i=0
#         for c in self.name:
#             i+=1
            
#         return i
    
#     def __call__(self, *args, **kwds):
#         print("I am callable object")        


from employeeclassfor73 import Employee

obj1=Employee("Jenish",20,1)
# print(obj1) # calls the __str__ method internally of employee class if not found call __repr__

# print(str(obj1)) ## calls the __str__ method internally of employee class if not found call __repr__
# print(repr(obj1)) ## calls the __repr__ method internally of employee class

print(len(obj1)) #calls __len__ method internally of employee class # calls obj1.__len___() internally
print(obj1.__len__()) #calls __len__ method internally of employee class # calls obj1.__len___() internally
obj1("I can take any no of arguments") # calls __call__ method internally of employee class


# means 
# a=[1,2,3]
# print(len(a)) # it calls the list.__len__() of an list class

# b=(1,2,3)
# print(len(b)) # it calls the tuple.__len__() of an tuple class

# but when len(obj1) can't find __len__() in employee class it will raise a TypeError that says object of type employee has no len() 

# means len() is not a built in function , every class has it own __len__ when we call len(obj) obj inside len will decide to call which class len method,am i right? 

'''
Yes! You’ve understood it perfectly! 🚀

🔹 Breakdown of Your Understanding:
✅ Lists, tuples, and other built-in types (like strings, dictionaries) have their own __len__() method inside their class.
✅ When calling len(obj), Python internally calls obj.__len__() from that object's class.
✅ If obj does not have __len__() defined, Python raises a TypeError saying the object has no length.

🔹 Example to Confirm Your Understanding:
python
Copy
Edit
a = [1, 2, 3]
print(len(a))  # ✅ Calls __len__() of list → Output: 3

b = (1, 2, 3)
print(len(b))  # ✅ Calls __len__() of tuple → Output: 3

class Employee:
    def __init__(self, name):
        self.name = name

obj1 = Employee("Jenish")
print(len(obj1))  # ❌ TypeError: object of type 'Employee' has no len()
🔹 Why does len(obj1) fail?
Because Employee class does not have __len__() defined, so Python does not know how to get its length.

🔹 Final Key Understanding:
1️⃣ len() is a built-in function, but it does not compute length by itself.
2️⃣ Instead, it delegates the work to obj.__len__() inside the class.
3️⃣ If __len__() is not present, Python does not know how to compute length and raises TypeError.

✔ Yes, the object (obj) decides which class's __len__() method to call. 💡
'''

# You said:
# i recently revised about the magic and dunder method of python i have doubt that if 

# list1=[1,2,3]

# means list1 is the object of list class
# and when we print list1 using this like

# print(list1)

# it calls the list1.__str__() method internally that prints the entire list am i right?


'''
Yes, you're absolutely right, Jenish! Let’s break it down step-by-step to reinforce your understanding.

✅ Statement 1:
python
Copy
Edit
list1 = [1, 2, 3]
Correct interpretation:
list1 is an object (or instance) of the built-in Python list class.

You can confirm this with:

python
Copy
Edit
print(type(list1))  # Output: <class 'list'>
✅ Statement 2:
python
Copy
Edit
print(list1)
Correct interpretation:
This internally calls:

python
Copy
Edit
list1.__str__()
The __str__() magic method is defined in the list class, and it's responsible for returning a user-friendly string representation of the list — exactly what print() shows.

You can verify this with:

python
Copy
Edit
print(list1.__str__())  # Output: [1, 2, 3]
✅ So yes, you're spot on — Python internally does this:

python
Copy
Edit
print(list1)  
# becomes
print(list1.__str__())
🔍 Bonus Clarification: Difference Between __str__() and __repr__()
__str__() → Used for end-user friendly output (print() calls this).

__repr__() → Used for developers/debugging (repr() calls this or when no __str__ is defined).

You can try:

python
Copy
Edit
print(str(list1))   # Same as list1.__str__()
print(repr(list1))  # Same as list1.__repr__()
In the case of built-in types like list, both methods often return the same string — but in custom classes, you can override them differently.
'''

list1=[1,2,3]
print(str(list1)) # equivalent to the prt(list1.__str__())
print(repr(list1)) # equivalent to the prt(list1.__repr__())

# 🔎 Rule of Thumb
# If it’s a method (like __str__, __len__, __add__), call it with ().
# If it’s a property/attribute (like __class__, __name__, __doc__), just access it without ().


# Author : Jenis Surani
# Topic  : Magic/Dunder Method
# Date   : 22/02/2025
