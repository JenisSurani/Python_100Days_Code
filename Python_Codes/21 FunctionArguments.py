# # Default Arguments:

def name(str1="Jenis",str2="Surani"):
    print("Hello,",str1,str2)

# name() # --> will use default parameters
# name("Jethalal","Gada") #--> will override the default parameters
name("Jethalal") #--> this also possible

# # Keyword Arguments:

def name2(fname,mname,lname):
    print("Hello,",fname,mname,lname)
    
name2(lname="Surani",fname="Jenis",mname="Sureshbhai") # can change the order of args
# because we are calling fun with using key:pair value 

# Variable length of arguments:

#1) Arbitary Arguments:

def name3(*naam):
 # available as name with type tuple
 print(type(naam))
 print("Hello,",naam[0],naam[1],naam[2])
 
name3("Jenis","Sureshbhai","Surani")

#2)  Keywords Arbitary arguments:

def name4(**naaam):
    print(type(naaam)) # available as naaam with type dictionary
    print("hello,",naaam["fname"],naaam["mname"],naaam["lname"])
    # We must use naaam["fname"] because dictionary keys are stored as strings, not variable names.
    # If we write naaam[fname], Python thinks fname is a variable instead of a key, leading to an error.
    
    # Example:
    # dict1={"fname":"Jenis","lname":"Surani","mname":"Sureshbhai"}
    # print(dict1)
    # print(dict1["fname"]) 

name4(fname="Jenis",lname="Surani",mname="Sureshbhai")

#Required Arguments:
def sum(a,b):
    return a+b # return fun with some value

print(sum(11,22))




# Author: Jenis Surani
# Topic: Function-Arguments & returntype
# Date: 06/02/2025