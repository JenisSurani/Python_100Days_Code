# # first thing to keep in mind that strings are immutable

# a1="Jenis"
# a2="        Jenis           "
# print(a1.upper())
# print(a1.lower())
# print(a2)
# print(a2.strip()) 

# # Removes any specific char at trailing only (means can't remove from front only removes from end)
a3="Jenis !!!!!"
# print(a3)W
# print(a3.rstrip("!"))

print(a3.replace("Je","Ta").strip("!"))

# a4="Jenis Surani Is Good Boy"
# print(a4.split(" ")) # returns List of splited words

# a5="jenis SuRani"
# print(a5.capitalize())

# a6="Jenis"
# print(a6.center(20,"*")) # 20-5=15 means 7 left and 8 right , If the total padding space is odd, Python places more padding on the right.
# # The padding character ('*') is used instead of spaces.

# # string.center(width, fillchar)
# # width → (Required) The total width of the resulting string.
# # fillchar → (Optional) The character to use for padding. Default is a space (' ')

# #If width is less than or equal to the length of the original string, it returns the original string unchanged.
# print(a6.center(1))

# a7="AbesaleAbe"
# print(a7.count("Abe"))
# print(a7.count("Abe",3))
# print(a7.count("Abe",3,7)) # end is exclusive you know that

# a8="Jenisis"
# print(a8.endswith("nisis"))
# print(a8.startswith("Je"))

# print(a8.count("is"))
# print(a8.find("is"))
# print(a8.find("is",0))
# print(a8.find("is",0,4))

# print(a8.index("is"))
# print(a8.index("is",0))
# print(a8.index("is",0,4))  # Exception will be thrown if given string is not found
# print(a8.index("is"))

# a10="jenis007"
# print(a10.isalnum())
# print(a10.isalpha())
# print(a10.islower()) # returns true if all char are in lowercase
# print(a10.isupper())

# a11="Hello i am jenis\n"
# print(a11.isprintable()) # because of \n

a12="  Jenis  "
a13="    "
print(a12.isspace()) # retuns true if string contains only spaces
print(a13.isspace())

a14="alice in borderland"
print(a14.istitle())
print(a14.title())

print(a14.isupper())
print(a14.islower())

a15="aLICE iN bORDERLAND"
print(a15.swapcase())


# In python we ca  also override variable also
a="jenis surani"
a="jenis surani" # in java , c that is not allowed


print(a)
# Author: Jenis Surani
# Topic: String Methods
# Date: 04/02/2025