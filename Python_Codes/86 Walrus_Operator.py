# The Walrus Operator is a new addition to Python 3.8 and allows you to assign a value to a variable within an expression.

# The Walrus Operator is represented by the := syntax



# foods=[]

# while True:
#     food=input("Enter your fav food:")
    
#     if food=="quit":
#         break
#     foods.append(food)
    
# print(foods)

# Aam zindagi


foods=[]

# while(food=input("Enter your fav food:"))!="quit": # You are trying to assign a value to food inside the while loop condition using the = operator. But in Python, assignments like this inside a condition are not allowed — = is not an expression, it just performs an action. Therefore, you’ll get a SyntaxError.
while(food:=input("Enter your fav food:"))!="quit":
    foods.append(food)

print(foods)  

# Mentos Zindagi  



# Author : Jenis Surani
# Topic  : Walrus_Operator
# Date   : 25/02/2025