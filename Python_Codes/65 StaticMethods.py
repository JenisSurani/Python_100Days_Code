# you can also define the methods outside the class but if your method is related to your class and you want to give the utility to the your class user to use the method
# if someone import the from Mathclass import math
# so they can use math.sum() method directly if you specify the methd in the class


class Math:
    def __init__(self):
        self.myvar=10
        
    def sum(self , a,b):
        return a+b
    
    def subtraction(self,a,b):
        return a-b
    
    # if you don't want to use the instance data use static method
    @staticmethod
    def sayHello():
        print(f"Hello from the math class and sayHello()")
    
    
obj=Math()
print(obj.sum(11,22))
print(obj.subtraction(22,11))

# obj.sayHello(obj)
print(Math.sum(obj,11,22))
Math.sayHello()
        
# On an instance (obj.method()), Python first checks if the method is a static method:
# ✅ If static, Python does not pass self.
# ✅ If not static, Python passes self (the instance).
# On a class (Class.method()), Python does not pass self unless explicitly provided.


# Author: Jenis Surani
# Topic: Static Methods
# Date: 17/02/2025