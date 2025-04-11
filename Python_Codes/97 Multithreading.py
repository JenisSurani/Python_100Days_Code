import threading
import time
from concurrent.futures import ThreadPoolExecutor

# lock=threading.Lock() # created lock instance to apply lock when we enter critical section/region
# print(type(lock))
# def cook():
#     i=0
#     while True:
#         with lock: #Ensures only one thread prints at a time.
#             print("cooking..")
#         i+=1
#         if(i==10000):
#             break

# #Both threads were writing to the console at nearly the same instant.
# # Python does not guarantee atomic (one-by-one) print() operations in threads.
# # that's why you are seeing chatting.. cooking.. at some time in same line use lock to prevent those overlapping
# # Sometimes prints mix due to buffering & non-thread-safe print().
# # sing Locks (threading.Lock) ensures clean output.
# def chatting():
#  i=0   
#  while True:
#      with lock:
#             print("chatting..")
#      i+=1
#      if(i==10000):
#          break
        
# task1=threading.Thread(target=cook)
# task2=threading.Thread(target=chatting)

# task1.start()
# task2.start()

# task1.join()
# task2.join()

# print("Done")
        
# Java multithreading usually means concurrency, but it can achieve parallelism on multi-core CPUs.
# means in java we are managing both task like while chatting your cooking cooker is going on but at the same time we are following only one task either chatting or cooking but in python,

# Python multithreading always means concurrency, never parallelism
# means you can't cooking in cooker when you are chatting and while you cook food in cooker you can't chat means true concurrency nevere paralleism
# In python For true parallelism, use multiprocessing instead of multithreading.

#python will not start both task parelly like java dose
# it will give some time to cooking (during this chtting is off) and some time to chatting(while this cooking is off)--> achievs true concurrency, one task at one time 
# no paralism in multithreading


#  Python’s multithreading behavior is the same on both single-core and multi-core CPUs because of the GIL, which forces only one thread to execute at a time.
# ✔️ If you want true multi-core usage in Python, use multiprocessing instead of multithreading. 🚀\
    
# def thread_task(task):
#     # # with lock:
#     #     time.sleep(5)
#     #     print(task,"is done")
    
#     lock.acquire()
#     time.sleep(5)
#     print(task,"is done")
#     lock.release()
    
# tasks=[i+1 for i in range(10)]
# # print(tasks)
# threads=[]

# for task in tasks:
#     thread=threading.Thread(target=thread_task,args=(task,)) # args must be any iterable this is the iterbale of your target parameters
#     threads.append(thread) # save it to your threads list to join in future
#     thread.start()
    
# for thread in threads:
#     thread.join()
    
def sleep(n):
    time.sleep(n)
    return n

# time1=time.perf_counter()  # use for perfomance counting
# t1=threading.Thread(target=sleep,args=[1])
# t2=threading.Thread(target=sleep,args=[2])
# t3=threading.Thread(target=sleep,args=[4])

# t1.start()
# t2.start()
# t3.start()

# t1.join()
# t2.join()
# t3.join()

# time2=time.perf_counter()  
# print(time2-time1)


# Even though Python’s Global Interpreter Lock (GIL) allows only one thread to execute Python code at a time
# your example involves sleeping, which is an I/O-bound operation.

# Python’s GIL prevents true parallelism for CPU tasks, but NOT for I/O-bound tasks like sleep().
# Since sleep releases the GIL, all threads can "sleep" together.

# threads are useful for i/o bounds operations like downloading file from server,reading writing file
# because in that we can achieve parallism even though we can also do the same using multiproccessing but multiprocessing is hevayweight you know and multithreading is lightweight

#  Multithreading or asyncio is best for downloading multiple files efficiently! 
# becaue asyncio also acchieve paralism




# use of concurrent.futures module to scheduling threads in bulk
# from concurrent.futures import ThreadPoolExecutor

# if you have multiple url list and multiple args and you want to schedule task of downloading in bulk use map function 

# scheduling thread in bulk 
# it will handle join,start,and creating of thread internally

with ThreadPoolExecutor() as executor:# we will use this method as executor name
    time1=time.perf_counter()
    argu=[1,2,3,4,5,6]
    results=executor.map(sleep,argu)
    
    for result in results:
        print(result)
    time2=time.perf_counter()
    print(time2-time1) # 6 seconds
    
    # or
    # if you want to do it manually
    
    s1=executor.submit(sleep,11)
    s2=executor.submit(sleep,22)
    s3=executor.submit(sleep,33)
    print(s1.result())
    print(s2.result())
    print(s3.result())

# Author : Jenis Surani
# Topic  : Multithreading
# Date   : 04/03/2025