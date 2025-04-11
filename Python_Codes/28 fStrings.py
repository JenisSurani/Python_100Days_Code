
letter="Hey my name is {} and i am from {}"
name="jenish"
city="surat"

print(letter.format(name,city))

letter="Hey my name is {1} and i from {0}"

print(letter.format(city,name))


txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

#  pretty complex right
# prefix the string with the letter 'f'


val="Geeks"
# print("{val}for{val} is good website for {val}")
print(f"{val}for{val} is a portal for {val}")

# if you wan to print this same string 
# print("{val}for{val} is good website for {val}") use {{}}

print(f"{{val}}for{{val}} is good website for {{val}}")


name = 'Jenis'  
age = 20  
print(f"Hello, My name is {name} and I'm {age} years old.")
# In the above code, we have used the f-string to format the string. It evaluates at runtime; we can put all valid Python expressions in them

# We can use it in a single statement as well.
print(f"{2 * 2}") # returns 4 as string


# Author: Jenis Surani
# Topic: fstrings
# Date: 07/02/2025