x=10

def change_x():
    global x
    
    x=20
    
# change_x()

print(x)

a=[1,2,3]
print(len(a)) # it calls the __len__() of an list class

b=(1,2,3)
print(len(b)) # it calls the __len__() of an tuple class


# this is the copy version of the curl command in your cmd
import argparse
import requests
import sys

parser=argparse.ArgumentParser()

# parser.add_argument("url",help="Give url to download your file")
# means output argument is optional
parser.add_argument("-xx",help="Give file name as you want to save your download file",default=None)

args=parser.parse_args()
print(args)

# from tutorail44