# in c,c++,java there is statement called switch statment
# in python there is match case statement
# in python , in match case in every case there is implicitly break statement
# meaning that if any one case matches rest of all cases will ignored
# means only one case will be excute in match case statmenets


a=int(input("Please Enter your choice:"))

match a:
    case 1:
        print("you choose no 1")
    case 2:
        print("You choose no 2")
    case 3:
        print("You choose no 3")
    case 4 if a%2==0: # if a=4 and a%2==0 then excute this case:
        print("Your num is 4 and even")
    case _ if a%2==0:  # this if condition is known as Guard Clause 
            # A guard clause is an extra condition inside a case statement that must be True for that case to execute.
            # check condition 4
        print("you choose even number")
    case _ if a%2!=0:
        print("you choose odd number")
    case _ : # _ is used as a wildcard or default case to handle all cases not explicitly mentioned.
        
        # for defalut case we use _ , we are saying that this _ can hold any value (meaning that any default value)
        # we can also have many defalut cases as well
        print("You not choose 1,2 or 3")            
        
        
# Author: Jenis Surani
# Topic: Match case statement (switch statement)
# Date: 04/02/2025