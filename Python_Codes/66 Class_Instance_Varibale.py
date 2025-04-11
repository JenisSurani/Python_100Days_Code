class Employee:
    
    No_of_emp=0 # class variable # static variable
    
    def __init__(self,kk,dd):
        self.Name=kk
        self.id=dd # instance variable
        Employee.No_of_emp +=1
        
    def Details(self):
        print(f"Name is {self.Name} Id is {self.id} and no of emp is {self.No_of_emp}")
obj1=Employee("Rahul",1)
obj2=Employee("Nishant",2)
obj3=Employee("Kamlesh",3)

obj1.Details()
obj2.Details()
obj3.Details()

obj1.No_of_emp=100000
print(obj1.No_of_emp) # reflected on the only obj1
print(obj1.__dict__) # new instance variable is created for obj1 only 
print(obj2.__dict__) 
print(obj3.__dict__)  

# when obj.No_of_emp will be called in details method python looks for instance variable first means self.No_of_emp if found then print them if  not found then look for the class varibale Employee.No_of_emp  and print them
Employee.No_of_emp=11 # reflected on the all objects 
print(Employee.No_of_emp)
obj1.Details()
obj2.Details()
obj3.Details()


# Class variables (static variables) are shared across all instances unless overridden.
# If you access obj1.No_of_emp before assigning it, Python looks up the class variable Employee.No_of_emp hence no new instance variable is created .
# However, if you assign obj1.No_of_emp = 100000, Python creates a new instance variable (No_of_emp) specific to obj1.
# This new instance variable shadows the class variable only for obj1.
# # when obj.No_of_emp will be called in details method python looks for instance variable first means self.No_of_emp if found then print them if  not found then look for the class varibale Employee.No_of_emp  and print them
# Other objects (obj2, obj3) and the class Employee remain unchanged.



# Before obj1.No_of_emp = 100000

# No_of_emp is a class variable.
# All objects share the same value (3 at that point).

# After obj1.No_of_emp = 100000

# Python creates a new instance variable No_of_emp for obj1 only.
# obj1.No_of_emp now refers to the instance variable instead of the class variable.
# After Employee.No_of_emp = 11
# 
# The class variable changes, affecting all objects except obj1, since it has its own No_of_emp


# Author: Jenis Surani
# Topic: Class Variable VS Instance Variable
# Date: 17/02/2025