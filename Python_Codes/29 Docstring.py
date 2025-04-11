# python doc string are like string literals that provides documentation of function ,class or module.
# python docstring only be writeen right after the function ,class or module.
# can acess using __doc__ attribute
# because Whenever string literals are present just after the definition of a function, module, class or method, they are associated with the object as their doc attribute. We can later use this attribute to retrieve this docstring.


def cube(n:int)->int:
    # print(n) # if you write this and then print doc it will print none because doc only appear after  function ,class or module. defination and before the body of function ,class or module.
    '''
    This function takes input n as int:   
    and return cube of n as int.
    '''
    # # they are associated with the objectof cube as their doc attribute.
    return (n**3)

print(cube(3))
# to access doc
print(cube.__doc__)

# comments are totally ignored by the python interpreter but docstring are not


# PEP 8 is a document that provides guidelines and best practices on how to write Python code. 
# focus of PEP 8 is to improve the readability and consistency of Python code.

# What is an Easter Egg in Programming?
# An Easter egg in software or programming refers to a hidden feature, joke, or secret message placed intentionally by developers inside a program, which is usually not documented officially.

# The Zen of Python is like a poetic set of guiding principles for Python’s design philosophy, written by Tim Peters. It is hidden as an Easter egg inside Python, and you can reveal it by running:import this

# When you run this in Python, it prints 19 aphorisms (short guiding principles) about Python’s design philosophy. These include:

# The Zen of Python, by Tim Peters

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!

# Author: Jenis Surani
# Topic: docstrings,PEP 8, Zen of python
# Date: 08/02/2025