# Generators generate the value one by one (on the fly) rather than creating entire seq in memory

def my_gen():
    
    for i in range(100):
        yield i # means return i as generator that generates value from  0 to 99  and stop the execution of the current func until next value is called of the gen
        
        # 'yield' returns a value and pauses execution of the function 
        # until the next value is requested.
gen=my_gen() # generators object
print(gen)
# to retrive the next value of the generator use next() fucntion
print(next(gen)) # prints 0 

# use of generators:

for j in gen: # next(gen) is called in each iteration of the for loop internally
    print(j)


# Author : Jenis Surani
# Topic  : Generators
# Date   : 03/03/2025