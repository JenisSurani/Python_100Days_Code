f=open("Merifile.txt",'r')

while True:
    line=f.readline() # it returns an empty string when it reaches the end of file that is EOF
    # The readline() function reads one line from the file at a time. When it reaches the end of the file (EOF), it returns an empty string ("").
    if not line:
        break
    print(line,end="")
    
print(f.tell())
# here file pointer is pointing to the end of the file
    
# readline() → Reads one line at a time and returns it as a string.
# readlines() → Reads all lines at once and returns them as a list of strings.

f.seek(0) # move the file pointer to the starting of the file to read from the starting
lines=f.readlines() # if you call without f.seek pointer is pointing to the end of file as there is nothing to read means it returns [] if you don't use f.seek(0)
print(lines)

    
'''
Python considers certain values Falsy, meaning they evaluate to False when used in an if condition. These include:

Value   Type
0	      Integer
0.0	      Float
""      (empty string)	String
[]      (empty list)	List
{}      (empty dictionary)	Dictionary
set()       (empty set)	Set
None	      NoneType
False	      Boolean
'''
def trueorfalse():
  return {}

if not trueorfalse():
  print("This is falsy")
# python cosider this all value as false in boolean
    
# f.close()

# with open('Merifile.txt','w') as d:
    
#     list1=["line1\n","line2\n","line3\n","line4\n"]
#     d.writelines(list1)

# if you don't want to add \n manually

# list2=["line11","line22","line33","line44"]
# f=open('Merifile.txt','w')
# for line in list2:
# #   f.writelines(line+'\n')
#   f.write(line+'\n')
  
# f.close()



# with open("Jenish.txt",'r') as df:
  
  
#   for i in range(3):
#     line=df.readline()
#     m1=int(line.split(",")[0]) # acessing the 0th index of list [ , , ]
#     m2=int(line.split(",")[1]) # note that 1st index of the list is string we have to typecast it
#     m3=int(line.split(",")[2])
    
#     print(f"Marks in chemistry of student {i+1}:{m1}")
#     print(f"Marks in physics of student {i+1}:{m2}")
#     print(f"Marks in maths of student {i+1}:{m3}")
    
# Author: Jenis Surani
# Topic: IO-Methods
# Date: 13/02/2025