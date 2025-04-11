class parent1:
    
    # def show(self):
    #     print("I am show() of parent1")
    pass

class parent2:
    def show(self):
        print("I am show() of parent2")

class parent3:
    def show(self):
        print("I am show() of parent3")

class parent4:
   def show(self):
        print("I am show() of parent4")


class child(parent1,parent4,parent3,parent2):
    
    # def show(self):
    #     print("I am show() of child")
    
    def mymethod(self):
        
        # child.show(self) # or
        self.show() # it follows the mro means from child-->parent1-->parent4-->parent3--->parent2--->object
        super().show()
        # #this will skip the child class 
        # follows parent1-->paent4-->parent3--->parent2-->object
        
        # if you want that show method of child will to be executed why use of super because we can call it directly using self or child.show(obj) or using self.show()
        
        # Because super() does not look in the current class where it is called. It directly looks in the next class in MRO (Method Resolution Order).


myobj=child()
myobj.mymethod()   
    
# to print the mro of the child

print(child.mro())
print(child.__mro__)
# help(child) 




'''
Method Resolution Order (MRO) – Simple Notes
🔹 What is MRO?
MRO (Method Resolution Order) is the order in which Python looks for methods in a class hierarchy when calling super().

🔹 How MRO Works?

It follows C3 Linearization (C3 MRO).
The search order is left to right, as specified in the class definition.
The object class is always at the end in new-style classes.
🔹 How to Check MRO?
Use one of these:

python
Copy
Edit
print(ClassName.__mro__)  # Tuple format
print(ClassName.mro())    # List format
help(ClassName)           # Shows MRO along with class details
🔹 Example 1: MRO in Single Inheritance

python
Copy
Edit
class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    pass

print(Child.__mro__)  
# Output: (<class '__main__.Child'>, <class '__main__.Parent'>, <class 'object'>)
✔ Python looks in Child first, then Parent, then object.

🔹 Example 2: MRO in Multiple Inheritance

python
Copy
Edit
class Parent1:
    pass

class Parent2:
    pass

class Child(Parent1, Parent2):  
    pass

print(Child.__mro__)
✔ MRO Output:

kotlin
Copy
Edit
(<class '__main__.Child'>, <class '__main__.Parent1'>, <class '__main__.Parent2'>, <class 'object'>)
✔ Left-to-right order (Child → Parent1 → Parent2 → object).

🔹 How super() Uses MRO?

super() does not always refer to the immediate parent.
It follows MRO order to find the next method in line.
python
Copy
Edit
class Parent1:
    def show(self):
        print("Parent1 show")
        super().show()

class Parent2:
    def show(self):
        print("Parent2 show")

class Child(Parent1, Parent2):
    def show(self):
        print("Child show")
        super().show()

obj = Child()
obj.show()
✔ Output:

sql
Copy
Edit
Child show
Parent1 show
Parent2 show
✔ super().show() in Child calls Parent1.show(), then Parent1 calls Parent2.show().

🔹 Key Takeaways
✅ MRO follows a strict order (Child → First Parent → Second Parent → object).
✅ super() does not call just the immediate parent, it follows MRO.
✅ Use Class.__mro__ or Class.mro() to check the method resolution order.
'''



# Author : Jenis Surani
# Topic  : SuperKeyWord and MRO
# Date   : 22/02/2025