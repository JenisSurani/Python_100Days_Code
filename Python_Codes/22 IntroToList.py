lst1=[1,22,33,"Jenis",-82,88.65,"Shubham","Rahul"]
#     0  1  2   3       4  5      6         7
#     -8 -7 -6  -5     -4   -3    -2        -1      negative index last thi -1 thi chalu thai

print(lst1)

# can access list item using index
print(lst1[1],lst1[3])

print(lst1[-4]) 
print(lst1[len(lst1)-4]) # all ans are same bcz all are same.
print(lst1[4])


#  To check wheter given value is present in list or not

if "Jenis" in lst1:
    print("Present")
else:
    print("Absent")
    
if 22 in lst1:
    print("Present")
else:
    print("Absent")
    
if "22" in lst1:
    print("Present")
else:
    print("Absent") # "22" is absent but 22 is present
    
# can do same thing in string also

a="Jenis Surani"

if "Sura" in a:
    print("Present in string")
else:
    print("Absent in string")
    
#  Range of index:
# List_name[start:end:jumpIndex] jumpIndex is optional

print(lst1[:5])
print(lst1[:5:2]) # jump by 2

print(lst1[:]) # == prt(lst1)
print(lst1[-6:-2]) # ==prt(lst1[2:4])


#  List Comprehension:

lst2=[j*j*j for j in range(10) if j%2==0]
print(lst2)


lst3=[2,22,11,222,33,2222]
print([k/2 for k in lst3 if k%2==0])

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
print([jj for jj in names if "o" in jj])

print([item for item in names if (len(item) > 4)])

print(lst3[1: : 3]) #means from 1 to end jump with 3

# Author: Jenis Surani
# Topic: IntroToList
# Date: 06/02/2025

'''
 # Step 1: Create an iterable
iterable = range(4)  # This produces numbers [0, 1, 2, 3]

# Step 2: Get an iterator from the iterable
iterator = iter(iterable)  # Creating an iterator

# Step 3: Use iteration manually to get values one by one
lst = []  # Empty list to store results

while True:
    try:
        i = next(iterator)  # Get next element from iterator
        lst.append(i * i)   # Compute square and store in list
    except StopIteration:
        break  # Stop when no more elements

# Step 4: Print the result
print(lst)  # Output: [0, 1, 4, 9]
'''
