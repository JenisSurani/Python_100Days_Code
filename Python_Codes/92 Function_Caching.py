# import functools
from functools import lru_cache
import time

@lru_cache(maxsize=None) # maxsize means how many no of cache (result ) you want to store in your memory
def myfunc(n:int)->int:
    time.sleep(5)
    return n*n

print(myfunc(5))
print(myfunc(6))
print(myfunc(7))
print("Printing Using Cache (Superfast Xpress)")
time.sleep(2)
print(myfunc(6))
print(myfunc(7))
    


# Author : Jenis Surani
# Topic  : Function Caching
# Date   : 03/03/2025