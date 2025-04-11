class base:
    def __init__(self,nm,time):
        self.name=nm
        self.workingTime=time
        
    def baseMeth(self):
        print("I am the method of the baseClass")
        
class derived(base): # similar to class derived extends base in java:
    
    def derivedMeth(self):
        print("I am the method of the  derivedClass")
        
BaseClassObj=base("Base_class_ka_object",5)
BaseClassObj.baseMeth()
# BaseClassObj.derivedMeth() # not allowed

# DerivedClassObj=derived() # Error: TypeError: base.__init__() missing 2 required positional arguments: 'nm' and 'time'
DerivedClassObj=derived("Derived_ka_obj",100)
DerivedClassObj.baseMeth()
DerivedClassObj.derivedMeth()


# Author: Jenis Surani
# Topic:Inheritance
# Date: 16/02/2025
    
    

