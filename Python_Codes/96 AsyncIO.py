# asyncio: A Python module for asynchronous programming.
import asyncio

# this module helps to achieve concurrent programming.
# Concurrency = Multiple tasks start, run, and complete in overlapping time periods.

# async ensure that it is asynchronous function. meaning it can be paused using await.

async def make_coffee():
    print("Ordered Coffee..")
    await asyncio.sleep(5)
    print("Coffee is ready!")
    
async def make_pizza():
    print("Ordered Pizza..")
    await asyncio.sleep(3)
    print("pizza is ready!")
    

async def main():
    # asyncio.create_task() starts tasks in parallel (non-blocking).
    
    task1=asyncio.create_task(make_coffee()) # start making coffee
    task2=asyncio.create_task(make_pizza()) # start making pizza
    #dono saath me hi start honge
    
    # when main is called this two line will stop main to exit function call before task1 and task2 completes
    await task1 # before moving forward check that task1 is complete or not?
    await task2 # before moving forward check that task2 is complete or not?
    
    #similar concept can be achievd using gather function
    L= await asyncio.gather(
    make_coffee(),
    make_pizza()
    )
    print(L) # prints return value of each function in gather    

# you cannot directly use await in the global scope.
# Instead, we define main() and call it using:
asyncio.run(main())





# # 🔹 When to Use Asynchronous Programming?
# Making API calls (Fetching data from a website)
# Downloading files (So the program doesn't freeze)
# Handling user input in GUI applications (Avoiding UI lag)
# Running multiple tasks together (Efficient use of time)

# It achieves multiprogramming run each task on  different CPUs or cores within a multicore CPU.


# Author : Jenis Surani
# Topic  : Async IO Module
# Date   : 03/03/2025