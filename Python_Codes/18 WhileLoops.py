# while loops
a=0
while a<5:
    print(a)
    # a++ cannot use this shit instead of use this
    # a=a+1 Or this:
    a +=1
    
    

print(end="\n")
a=10
while (a>0):
    print(a)
    a=a-1
    
# python do not have do while loop but we can create it
print(end="\n")

b=10
while True:
    print(b)
    b=b-1
    if b==0:
        break
# can also use else with while loop & for loop 
else:
    print("Else block is executed") # not exectuable because we are using break in loop means next print line pase control jase
    
print(end="\n")
i=0
while i<10:
    print(i)
    i +=1
else:
    print("Else block is executed")
    # the else block is executed when while condition  become false

# Author: Jenis Surani
# Topic: While Loop
# Date: 05/02/2025