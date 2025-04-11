# create file object first
# using open method

# READ MODE #DEFAULT MODE:
file_obj=open('MeriFile.txt','r') # gives an error if no file exist
print(type(file_obj))
# words=file_obj.read()

# print(words)

# # WRITE MODE 

# file_obj2=open('MeriFile.txt','w') # creates a file if not exist
# # overrides the content

# file_obj2.write("Hello jenish surani!")
# file_obj2.close()

# APPEND MODE:

# file_obj3=open('MeriFile.txt','a') # creates a file if not exist

# file_obj3.write("Hello jenish surani!")
# file_obj3.close()

# by default file is opening in text mode 

# to open file in binary format

# file=open('obj.jpg','wb')
# file.close()

# to manually close the file use with statement

# with open('MeriFile.txt','r') as d:
#     print(d.read())


# Author: Jenis Surani
# Topic: File I/O in python
# Date: 13/02/2025




