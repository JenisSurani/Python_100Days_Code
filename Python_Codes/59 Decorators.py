def greet(func):
    def myNewFunc(*ab,**bc):
        print("Starting of function")
        func(*ab,**bc)
        print("Ending of the function")
        
    return myNewFunc


@greet
def hello(a:int,b:int)->int:
    print(f"hello from hello(a,b),a is {a} and b is {b}")

# def master():
#     print("I am master method")

# hello=master
# hello()

# proof that it actually works


#greet khali hello nu nahi badha func nu dhyaan rakhe tethi varags le che argument ma

hello(1,2)
# means call hello=greet(hello)
# means:

# def greet(hello):
#     def myNewFunc(*ab,**bc):
#         print("Starting of function")
#         hello(*ab,**bc)
#         print("Ending of the function")
        
#     # return myNewFunc

#  so greet(hello) returned myNewfunc back to the 26 line

# hello=mynewFunc

# back to 25 line
# mynewfunc(1,2)

# okay now execute mynewfunc as follows:

# myNewFunc(1,2):
#         print("Starting of function")
#         hello(1,2)
#         print("Ending of the function")


# same process for all remaing 999 functions

# Always use *args, **kwargs in decorators to handle all function types.
# ✔ *args → Handles positional arguments (like 10, 20).
# ✔ **kwargs → Handles keyword arguments (like a=10, b=20).

# https://chatgpt.com/share/67b06a56-4b94-800f-85f6-8d1a83b3e23a


# Author: Jenis Surani
# Topic: Decorators
# Date: 15/02/2025