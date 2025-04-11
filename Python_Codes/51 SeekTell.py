# to jump on the specific index

f=open("Myfile.txt",'w')

f.write("Hello i am good boy\ni am also doing code\ni am doing engineering")

f.close()

# ##############################################

f=open("Myfile.txt",'r')

f.seek(10) # jump on 10th byte of the file
data=f.read(5) # read 5 char from the current position
# " good" is output
print(data)

# to read backwards from the seek
list1=[]
for i in range(10,-1,-1): # From 10th byte to 0th byte
    f.seek(i)
    list1.append(f.read(1))

message="".join(list1) # means join all the elements of the list1 without any space
message=message[::-1] # reverse the message
print(message)
# print(message)

# or can do this


content=f.read() # read the whole file first    
# Extract the first 10 bytes and reverse them
backward_data = content[:10][::-1] # Extract the first 10 bytes and then reverse them
# evlautye like this first do this content[:10] and then reverse the string using [::-1] because content[:10] will return the styring as the string slicing returns the new string
print(backward_data)





# to know the current postion use tell fun

# current=f.tell()
# print(current)

f.close()


# f1=open("Myfile22.txt",'w')
# # f1.write("Hello i am good boy")
# f1.write("ijaiojs")
# f1.truncate(5)
# f1.close()


# f1=open("Myfile22.txt",'r')
# data=f1.read()
# print(data)

# Author: Jenis Surani
# Topic: Seek method and Tell method in files
# Date: 13/02/2025