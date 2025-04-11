import math
class Shape:
    
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    # def area(self):
        
    #     return self.x*self.y
class Shape2:
    
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def area(self):
        
        return self.x*self.y*self.x
    
class Circle(Shape,Shape2):
    
    def __init__(self,radius):
        super().__init__(radius,radius)
        
    
    #overriding the area method from the shape class
    # def area(self):
        
    #     return math.pi * super().area()
    

c1=Circle(5)
print(Circle.__mro__)
print(c1.area())


# mro have following rules:

# Python follows three rules when calculating MRO:

# 1.Children Before Parents (Always check the child class first).
# 2.Depth-First Search (Go as deep as possible before moving sideways).
# 3.Left-to-Right Order (If multiple parents exist, check the leftmost one first).
# 4. No Parent Should Be Revisited Before Its Subclasses Are Fully Checked (C3 Linearization Rule).

 

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B):
    def show(self):
        print("D")

class E(C):
    def show(self):
        print("E")

class F(D, E):  # Multiple Inheritance
    pass

obj = F()
print(F.__mro__)
obj.show()

# F-->D-->B-->E-->C-->A-->Object

  
# Author : Jenis Surani
# Topic  : Method-Overriding
# Date   : 23/02/2025