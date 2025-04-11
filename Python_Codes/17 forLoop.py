for k in range(10): # means range 0 to 10 -->[0,1,2,3,4,5,6,7,8,9]
    print(k) 
    # range(10) does not create a actucal list in memory; it generates values one by one
# When you call range(10) ,iterator=iter(range(10)), it creates an iterator object.
    # iterator -> [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
    #              ↑  (not pointing to any value yet)
    
    # when k=next(iterator) called it move towards 0 and return 0
    # now k holds 0 
    # iterator -> [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
    #               ↑  (not pointing to any value yet)
    
for k in range(1,5): # goes till 1 to 4
    print(k)
    

    
for k in range(0,11,2): # start,end,step step=2 means 0,2,4,6..till 10 (if printable)
    print(k)
    

numbers=[11,22,44,66,77] # creating list as name numbers

for k in numbers:
    print(k)
    
#Internally python doing this:

# iterator = iter(numbers) # means give me iterator of numbers using iter fun
# while True:
    # try:
        # num = next(iterator) # move iterator to next one
        # print(num)
    # except StopIteration:
        # break


# can also use else with for loop also

# Author: Jenis Surani
# Topic: For loop
# Date: 05/02/2025