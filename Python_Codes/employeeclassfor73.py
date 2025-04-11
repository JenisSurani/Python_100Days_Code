class Employee:
    
    def __init__(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id
        
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    # def __repr__(self):
    #     return f"Employee({self.name},{self.age},{self.id})"
    
    def __len__(self):
        
        i=0
        for c in self.name:
            i+=1
            
        return i
    
    def __call__(self, *args, **kwds):
        print(args)
        print("I am callable object")   