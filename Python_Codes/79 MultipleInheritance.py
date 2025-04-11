class Animal:
    
    def __init__(self,name,species):
        self.name=name
        self.species=species
        
    def walk(self):
        print("Animal is walking ")
 
class Mammal:
    def __init__(self, name, fur_color):
        self.name = name
        self.fur_color = fur_color
               
class Dog(Animal,Mammal): # example of multiple inheritance
    #because dog is inherited from the Animal and mammal class
    # python follows MRO to reslove attribute or function call
    
    def __init__(self, name, breed,fur_color):
        Animal.__init__(self,name, species="Dog")
        Mammal.__init__(self,name,fur_color)
        self.breed=breed
    
    def walk(self):
        print(f"{self.name} Dog is walking")
        

tm=Dog("kalu","Doggerman","Black")
tm.walk()

dd=Animal("Suvar","NotDefined")
dd.walk()

print(Dog.mro())
print(Dog.__mro__)



# Author : Jenis Surani
# Topic  : MultipleInheritance
# Date   : 23/02/2025