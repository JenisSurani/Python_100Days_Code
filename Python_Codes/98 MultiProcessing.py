import multiprocessing
import requests
from concurrent.futures import ProcessPoolExecutor
import os

def downloadfile(url,name):
    # to download a file from internet:
    print(f"file{name} {os.getpid()} is started to download sucessfully")
    response = requests.get(url)
    open(f"D:\\Coding\\Python_for_temp\\Tut98\\file{name}.jpg", "wb").write(response.content)
    print(f"file{name} is downloaded sucessfully")
    
#You're running your script on Windows, and Windows does not support forking like Linux/macOS does.
# On Windows, every new process re-imports the main script, which can cause the RuntimeError.
# Solution: ✅ Wrap Your Code Inside if __name__ == '__main__':

   
if __name__ == '__main__':
    url="https://picsum.photos/1920/1200"


    # for i in range(5):
    #     downloadfile(url,i) # this is slow use multiprocessing
    # processes=[]
    # for i in range(50):   
    #     process=multiprocessing.Process(target=downloadfile,args=(url,i))
    #     process.start()
    #     processes.append(process)

    # for process in processes:
    #     process.join()        
 # let's make it more eaiser in syntax using from concurrent.futures import ThreadPoolExecutor
# Python creates multiple child processes that run in parallel
    with ProcessPoolExecutor() as Executor:
        URL=[url for _ in range(50)]
        l=[i for i in range(50)]
        results = Executor.map(downloadfile,URL,l)
    
    for i in results:
        print(i)
        
        
# you can locate this processes in task manager in details as python.exe set cpu in decrasing
# Multithreading (ThreadPoolExecutor) is the best choice for downloading files because:

# It efficiently handles multiple concurrent downloads.
# Threads have low overhead and share memory.
# Network I/O is NOT CPU-intensive, so the GIL is not an issue.
# 🚀 Multiprocessing is useful for CPU-heavy tasks (e.g., processing images after downloading), but not for the download itself.



# '''
# 1️⃣ multiprocessing.Pool(processes): Running Tasks in Parallel
# 🔹 Think of it like a Restaurant Kitchen
# Imagine you own a restaurant and customers place 10 food orders.
# If you have only one chef, they will cook one dish at a time, taking longer.
# Instead, you hire 4 chefs (workers) to cook multiple orders at the same time.
# Now, all chefs cook together, and orders are completed faster!
# This is exactly what multiprocessing.Pool(processes) does—it creates multiple worker processes to handle tasks in parallel.

# Python Example:
# python
# Copy
# Edit
# from multiprocessing import Pool

# def cook_food(order):
#     print(f"Chef is cooking order {order}")

# if __name__ == '__main__':
#     orders = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # 10 food orders
#     with Pool(processes=4) as pool:  # 4 chefs (workers)
#         pool.map(cook_food, orders)  # Assign orders to chefs
# 🔹 What Happens?
# 4 processes (chefs) cook at the same time.
# Orders are processed faster than if there was only one worker.
# 2️⃣ multiprocessing.Queue(): Passing Data Between Processes
# 🔹 Think of it like a Conveyor Belt in a Factory
# Imagine a factory making burgers.
# One worker (producer) prepares the burger and places it on a conveyor belt (queue).
# Another worker (consumer) takes the burger from the conveyor belt and packs it.
# The queue helps pass items safely between workers.
# This is exactly what multiprocessing.Queue() does—it allows one process to send data, and another process to receive it safely.

# Python Example:
# python
# Copy
# Edit
# import multiprocessing

# def producer(queue):
#     for i in range(5):  # Make 5 burgers
#         print(f"Burger {i} prepared")
#         queue.put(i)  # Place burger on conveyor belt

# def consumer(queue):
#     for i in range(5):  # Pack 5 burgers
#         burger = queue.get()  # Take burger from conveyor belt
#         print(f"Burger {burger} packed")

# if __name__ == '__main__':
#     queue = multiprocessing.Queue()  # Create conveyor belt
#     p1 = multiprocessing.Process(target=producer, args=(queue,))
#     p2 = multiprocessing.Process(target=consumer, args=(queue,))
    
#     p1.start()
#     p2.start()
    
#     p1.join()
#     p2.join()
# 🔹 What Happens?
# Producer makes burgers and places them on the queue (conveyor belt).
# Consumer takes burgers from the queue and packs them.
# This helps pass data between processes safely.
# 3️⃣ multiprocessing.Lock(): Preventing Conflicts in Shared Resources
# 🔹 Think of it like a Bank ATM
# Imagine two people trying to withdraw money from the same bank account at the same time.
# If both withdraw money at the exact same moment, the balance might get messed up.
# The bank uses a lock so that only one person can access the account at a time.
# The second person must wait until the first person finishes.
# This is exactly what multiprocessing.Lock() does—it prevents multiple processes from accessing a shared resource at the same time.

# Python Example:
# python
# Copy
# Edit
# import multiprocessing

# def withdraw_money(account_balance, lock):
#     for _ in range(10000):  # 10,000 transactions
#         lock.acquire()  # Lock the account
#         account_balance.value -= 1  # Withdraw money
#         lock.release()  # Unlock the account

# if __name__ == '__main__':
#     balance = multiprocessing.Value('i', 10000)  # Bank balance = 10,000
#     lock = multiprocessing.Lock()  # Lock to prevent conflicts

#     p1 = multiprocessing.Process(target=withdraw_money, args=(balance, lock))
#     p2 = multiprocessing.Process(target=withdraw_money, args=(balance, lock))

#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()

#     print("Final Bank Balance:", balance.value)
# 🔹 What Happens?
# Two people try to withdraw money at the same time.
# The lock ensures only one transaction happens at a time.
# Without the lock, the balance might be calculated incorrectly due to race conditions.
# 🚀 Summary
# Concept	Real-Life Example	Purpose
# Pool(processes)	Restaurant with multiple chefs	Run multiple tasks in parallel
# Queue()	Factory conveyor belt	Pass data between processes safely
# Lock()	Bank ATM system	Prevent multiple processes from accessing a shared resource at the same time
# This makes multiprocessing faster, safer, and more efficient! 🚀

# Author : Jenis Surani
# Topic  : MultiProcessing
# Date   : 04/03/2025