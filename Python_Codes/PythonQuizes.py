# list1=[1,2,3,4]
# list1[1:3]=[]
# print(list1)

# x=list("Pyhton")
# for i in enumerate(x):
#     print(i,end=" ")
    
List1=[[1,2,3],[4,5],[6,7,8,9]]
result=sorted(List1,key=len)
print(result)
print(List1)

x={}
y=[1,2]
z=[3,4]
print(x.fromkeys(y,z))
print(x.fromkeys.__doc__)        


# Tuple unpacking is a feature in Python that allows multiple variables to be assigned values from a tuple (or any iterable) in a single statement.
# Strings are iterables, meaning they can also be unpacked like tuples.
a,b="12"
# Python interprets '12' as a sequence of characters because str is seq of char:
# thinks that you want to assign the value a and b from seq of char "12"
print(a)
print(b)

c=d='12'
print(c)
print(d)


# Extended Unpacking (* Operator)
# If there are more values than variables, you can use * to capture extra values.
x,y,*z="123456"
print(x,y,z)
d,*e = (1, 2, 3, 4)
print(d, e)  # Output: 1 [2, 3, 4]

# Key Takeaways
# Tuple unpacking assigns multiple values at once.
# It works with tuples, lists, strings, and other iterables.
# The number of variables must match the number of elements unless * is used.
# It's useful for returning multiple values from functions and swapping values.


def get_string():
    return "AB"  # String behaves like a tuple of characters

for x, y in [get_string()]:  # Unpacking each character
    print(x, y)  # Output: A B
    
    
    
def get_strings():
    return ["12", "34", "56"]  # List of two-character strings

for x, y in get_strings():  # Each string unpacks into two variables
    print(x, y)

# Strings are iterables (like tuples), so they support unpacking.


# list1=[1,2,3]
# l2=tuple(list)
# l2[0]=2
# print(l2) # prodcues an error



# new quiz:

List=list("Python")
values=(List[0],List[1:3]) # means create tuple with this values
# values=(P,ref1) # not [p] because we are not slicing we are acessing the value means return string/char whatever type it has
          #  |
          #  |
          #  |
          #  v
          #  ['y','t']
          
values=(List[0],List[1:3],List[1]) # in that case we have 3 arguments but python will send only 2 arguments as requiremnt of the format method
# if string demands 3 argu .format will demand three agru and *list will give 3 argu instead of2
# so all depends on the string needs
# *List will send the no  of arguments format method will need to format the string


          
# print('v1={0},v2={1}'.format(values)) # prodcues error because values have only one tuple
print('v1={0},v2={1}'.format(*values)) # telling that unpack the tuple and assign value corosponding to the {0} and {1}
print('v1={0},v2=Nothing'.format(values)) # means assign the whole tuple to {0}

# format() expects multiple arguments (one for {0}, one for {1}). because we use two variable in the string that is {0} and {1}
# by addinf  * we are giving required arguments to the string for format

# The * operator in format(*values) is used for unpacking the iterable values. Let's break it down.
#  * means asterisk



# List = [1, 2]
# a, b = List

# Here Python allows unpacking directly when assigning multiple variables:

# a, b = List assigns:
# a = 1
# b = 2
# We don’t need * because Python automatically matches the number of variables on the left (a, b) with the elements in the list.

# recall at that time of quiz we use * also line:36



# SWAPPING TWO NUMBERS: 5 WAYS:
a=10
b=20

# Using temp
# temp=a
# a=b
# b=temp

# print(a)
# print(b)


# Using arithmetic operations:

# a=a+b
# b=a-b # means b=a+b-b-->means b=a
# a=a-b # means a+b-a --> a=b

# print(a)
# print(b)

# using tuple unpacking
# a,b=b,a
# # first right hand side creates tuple (20,10) then assigment of the tuple to multiple variables means tuple unpacking
# print(a)
# print(b)

# a, b = b, a #,right side will  creates a temporary tuple (b, a) → (20, 10).
# The left-hand variables a, b receive these values simultaneously.

# General Rule:
# Whenever Python sees multiple values separated by commas, it implicitly creates a tuple.

# aa=11,22,33
# print(type(aa))


# Using Xor (^) operator

# Xor need one 0 and one 1 to be true (1):

# X^X is 0 because X CAN BE 1 or 0 check for both
#  X^0 is X because X=0 or 1 , if x is 1 1^0-->1 means x , if x is 0 0^0-> means 0 means x itslef

# a=a^b
# b=a^b # b=a^b^b--> b=a^0 --> b=a
# a=a^b # a=a^b^a--> a=0^b--> a=b


# using airthmetic operation:

#  // means it will return int if both are int
a=a*b
b= a//b # b=a*b/b --> b=a
a= a//b # a=a*b/a --> a=b
# If b = 0, a = a * b makes a = 0, leading to a division by zero error.
print(a)
print(b)

# all numbers are made within 0-9

# Decimal	Binary	      Even/Odd
# 0	        0000	        Even
# 1	        0001	        Odd
# 2	        0010	        Even
# 3	        0011	        Odd
# 4	        0100	        Even
# 5	        0101	        Odd
# 6	        0110	        Even
# 7	        0111	        Odd
# ..

# if num is even it's LSB would always 0 means LSB ALWAYS HOLDING FALSE IF NUM IS EVEN
#  if num is odd it's LSB would always 1 means LSB ALWAYS HOLDING TRUE IF NUM IS ODD

# num & 1 --> means whatever binary numer & ....0000001
# if 1 ka binary have only one T and all other false why to check false value beacuse & returns true if both are true
# check only LSB IN BOTH NUMBER

# even ni lsb 0
# odd ni lsb 1

# 0&1-->false 0
# 1&1-->true 1

def iseven(num):
    return num&1==0
def isodd(num):
    return num&1==1


text="hello"
text[1]='i'
print(text)

#string are immutable