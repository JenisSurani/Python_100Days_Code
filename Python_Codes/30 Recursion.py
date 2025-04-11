# function calling to itself

def factorial(n:int)->int:
    
    # base case:
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1) # calling this fucntion again after breaking to 5(problem) into sub-problem that is factorial(4) 
        # stop recursion when base case hits!
    
print(factorial(5))

def sumOfN(n:int)->int:
    
    if n==1:
        return 1
    else:
        return n + sumOfN(n-1)
    
print(sumOfN(5))


def fibonnaciNthterm(n: int)->int:
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonnaciNthterm(n-1) + fibonnaciNthterm(n-2)
    
print(fibonnaciNthterm(6))
        
        
# Author: Jenis Surani
# Topic: Recursion
# Date: 08/02/2025