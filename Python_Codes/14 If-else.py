a=int(input("Please Enter your age: "))

if a>=18:
    print("You can vote:") # 1st level of indent 

    # in python there is no {} for code block of if else
    # python have indenation ( 4 space per level)


elif 0<=a<10: # for ranges use this type of conditions
    #() are not required for the condition statements  but you can also add it if you want
    
    if a==0:
        print("Age cannot be 0") # 2nd level of indent (Nested if statements)
    else:
        print("You are too young!") # 2nd level of indent
else:
    print("You cannot vote")


# Author: Jenis Surani
# Topic: If else , elif , nested if
# Date: 04/02/2025
