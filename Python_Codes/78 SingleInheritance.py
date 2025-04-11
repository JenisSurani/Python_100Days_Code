class Animal:
    
    def __init__(self,name,species):
        self.name=name
        self.species=species
        
    def walk(self):
        print("Animal is walking ")
        
class Dog(Animal): # example of single inheritance
    
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed=breed
    
    def walk(self):
        print(f"{self.name} Dog is walking")
        

tm=Dog("kalu","Doggerman")
tm.walk()

dd=Animal("Suvar","NotDefined")
dd.walk()

# Author : Jenis Surani
# Topic  : SingleInheritance
# Date   : 24/02/2025