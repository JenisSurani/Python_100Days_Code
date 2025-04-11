name="Jenis"
name1='Jenis'

# print(name)
# print(name1) # Both are same

#    +----------------+     +------------------+
#    |  name         | ---> |  "Jenis" (Heap)  |
#    +----------------+     +------------------+
#    |  name1        | ---^
#    +----------------+  
# 

#  to verify

print(id(name))
print(id(name1))

# If you want to use "" in your string use '' string
name='He said,"I am good".'
# print(name) # Output: He said,"I am good".

# Multiline String

# Error: 'str' is a built-in type in Python, but it is incorrectly used as a variable name.
# The correct approach is to use 'str1' instead of str, which is the defined variable.

str1="""
She: Hi,How are you?
He: Pehli,Fursat Me Nikal


"""
str11='''
She: Hi,How are you?
He: Pehli,Fursat Me Nikal
'''

print(str1)
print(str11)

#Both are same

# for loop for printitng char in String(Like Char array ):


# for character in str1:
# print(character) #Error:

# In Python, the statement inside a loop must be properly indented(anadar hovu pade for loop ni).
# print(character) should be indented under the for loop.

for a1 in str1:
    print(a1,end="    ") #Corrected
    


# Author: Jenis Surani
# Topic: Strings
# Date: 03/02/2025