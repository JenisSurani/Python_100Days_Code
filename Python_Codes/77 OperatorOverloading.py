class vector:
    
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def __add__(self,other):
        
        return vector(self.x+other.x,self.y+other.y)
    # return type must be object of the vector because of two vector addition gives also vector
    
    def __str__(self):
        return f"{self.x,self.y}"
    
    #f"{self.x, self.y}" returns a tuple because Python interprets it as f"{(self.x, self.y)}".
# Fix it by using f"({self.x}, {self.y})" to format it correctly.
# Always test __str__() separately to check the output.
    
    
a=vector(5,2)
print(a) # calls __str__ method
b=vector(11,4)
print(b)

c=a+b # it will check type of a is it bulit in type or custom class
# # a is type of vector class so call __add method of vector class instead of bulit in data type like,int,float
# #resolve as a.__add__(a,b)
print(c)
print(type(c))



# scroll down



# It's important to note that operator overloading is not limited to the built-in operators, you can overload any user-defined operator as well.

# means + simply calling __add__ of left operand class
# but we also define __add__ method of our own class
#hence operator overloading

#int class in __add__ hoy , float ni pan hoy,char ni pan hoy
# kone call karvu te left operand na hath ma che

# example: a+b here a is vector object means call __add__ on vector using a.__add__(a,b) for c=a+b

#built in operator--> +,-,*,/
# userdefine operators like--> @ , | &

# let override @ means matrixmultiplication

class Matrix:
    
    def __init__(self,value):
        self.value=value ## Storing a 2D list as a matrix
        self.row=len(value)
        self.column=len(value[0])
        
    def __matmul__(self,other): ## Overloading '@' operator for matrix multiplication
        
        if self.column!=other.row:
            print("Matrix multiplication not allowed")
            
        # create empty list
        result=[[0]*other.column for _ in range(self.row)]
        
        for i in range(self.row):
            for j in range(other.column):
                for k in range(self.column): # means other.row
                    
                    result[i][j] += self.value[i][k] * other.value[k][j]
        
        return Matrix(result)
    # returns matrix object so that we can use cc with dd matrix later
    
    def __or__(self,other):
        
        result=[[self.value[i][j] + other.value[i][j] for j in range(len(self.value[0]))] for i in range(len(self.value))]
        
        return Matrix(result)
    
    def __str__(self):
        return "\n".join([' '.join(map(str,row)) for row in self.value])
    

A=Matrix([[1,2,3],[4,5,6],[7,8,9]])
B=Matrix([[11,22,33],[55,66,77],[1,2,3]])

C=A @ B # will call A.__matmul__(A,B)
D=A|B # will call A.__or__(A,B)
print(C)
print("\n",D,sep="")
            
            
            
# In Python, each operator has a corresponding special method that we need to define in a class to overload it.

# For + (Addition) → We use __add__()
# For @ (Matrix Multiplication) → We use __matmul__()
# For | (bitwise addition) → We use __or__()
# For - (Subtraction) → We use __sub__()
# For * (Multiplication) → We use __mul__()
# For / (Division) → We use __truediv__()
# For % (Modulus) → We use __mod__()
# For ** (Power) → We use __pow__()
# For @ (Matrix Multiplication) → We use __matmul__() (as introduced in Python 3.5)



# Case 1: 5 + 2 (Built-in Addition)
#
# result = 5 + 2
# Internally, Python does the following:

# The + operator calls the __add__ method of the first operand's class (int in this case).
# Since 5 is an integer, Python internally executes:
# python
# Copy
# Edit
# result = int.__add__(5, 2)
# The int class has a built-in implementation of __add__, which performs integer addition and returns 7.
# So, 5 + 2 does not call any custom __add__ method because int has its own built-in version.



# Case 2: Overloading + in a Custom Class
# Now, let's say we define our own Vector class and overload +:

# python
# Copy
# Edit
# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):  # Overloading +
#         return Vector(self.x + other.x, self.y + other.y)

#     def __str__(self):
#         return f"Vector({self.x}, {self.y})"

# v1 = Vector(2, 3)
# v2 = Vector(4, 5)

# result = v1 + v2  # Calls __add__
# print(result)  # Output: Vector(6, 8)
# What Happens Internally for v1 + v2?
# Python sees v1 + v2 and checks the class of v1 (Vector).
# Since Vector defines __add__(), Python calls:
# python
# Copy
# Edit
# result = Vector.__add__(v1, v2)
# Inside __add__(), the new Vector object is created with the sum of x and y.
# The result is returned as a new Vector object.
# ✅ Python knows to call Vector.__add__ instead of int.__add__ because v1 is an instance of Vector, not int.


# # 🔍 What If the Method Is Missing?
# If we try v1 + v2 without defining __add__(), Python will throw an error:

# python
# Copy
# Edit
# TypeError: unsupported operand type(s) for +: 'Vector' and 'Vector'
# That’s because Python couldn’t find __add__() in Vector, and since Vector isn’t a built-in type, there's no default behavior for +.
        
        
        
# 🔹 Example: Overloading Reverse Addition (__radd__)
# If we try:

# python
# Copy
# Edit
# v1 + 5
# Python will first try:

# python
# Copy
# Edit
# Vector.__add__(v1, 5)
# Since __add__ isn’t defined for Vector + int, Python will check the reverse method:

# python
# Copy
# Edit
# int.__radd__(5, v1)
# If Vector defines __radd__, Python will call that.

class Vector:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __add__(self, other):  # Normal addition (Vector + something)
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        elif isinstance(other, int):  # Vector + int
            return Vector(self.x + other, self.y + other)
        return NotImplemented  # Tell Python to try __radd__
    
    def __radd__(self, other):  # Reverse addition (int + Vector)
        return self.__add__(other)  # Call __add__ to reuse logic

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)

print(v1 + v2)  # Calls __add__ → Vector(6, 8)
print(v1 + 10)  # Calls __add__ → Vector(12, 13)
print(10 + v1)  # Calls__add__ first then it returns (int class) line 225 to 233 Notimplemented means call __radd__ with switch of arguments
# resolve it print(10 + v1) --> not implemented --> use __radd__ so --> like prt(v1+10) v1.__radd__(v1,10)-->calling add inside it→ Vector(12, 13)

        
        
# 🔹 What is int.__add__()?
# Python's int class has an internal __add__() method that looks something like this (simplified version):

# python
# Copy
# Edit
# class int:
#     def __add__(self, other):
#         if isinstance(other, int):  # Normal integer addition
#             return self + other  # This is a low-level C operation
#         return NotImplemented  # If other is not int, let Python try __radd__
# Since int.__add__() returns NotImplemented for non-int types, Python tries other.__radd__().
  
  
#   __radd__() is the reverse addition method in Python.

# It is used when the left operand does not know how to handle the addition operation, so Python tries calling the right operand’s __radd__() method instead.

#   🔍 When Does Python Call __radd__()?
# Python first tries left_operand.__add__(right_operand).

# If __add__() is not defined or returns NotImplemented, Python then tries right_operand.__radd__(left_operand).

# If __radd__() is also not implemented, Python raises a TypeError
  
  
#    How Python Resolves an Operator Overload
# Check if the left operand’s class (v1) has the corresponding dunder method (__add__).

# If not found, check if the right operand’s class (v2) has __radd__ (reverse addition).

# If neither class has the method, Python raises a TypeError.

# ✅ This is why 5 + 2 calls int.__add__(), but v1 + v2 calls Vector.__add__() if defined.

      # 
# https://chatgpt.com/share/67f5b74e-ef30-800f-b1d8-3fa899199c81


# Author : Jenis Surani
# Topic  : OperatorOverloading
# Date   : 23/02/2025