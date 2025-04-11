import argparse
import sys

# we use this two module to create command line utility

# let create an object of Argumentparse class that is present in argparse module

parser=argparse.ArgumentParser()

# now we add arguments to our command

parser.add_argument("--x",type=float,default=1.0,help="Enter first number.If you need help contact jenish surani")
parser.add_argument("--y",type=float,default=2.0,help="Enter second number.If you need help contact jenish surani")
parser.add_argument("--z",type=str,default="add",help="Enter operation .If you need help contact jenish surani")

# now we need to parse this arguments

args=parser.parse_args() # gives object of namespace class



def calculate(args):
    
    if args.z=="add":
        return args.x + args.y
    elif args.z=="sub":
        return args.x - args.y
    elif args.z=="mul":
        return args.x * args.y
    elif args.z=="div":
        return args.x / args.y
    else:
        return "InvalidOperation"
    
# sys.stdout gives standard output
#sys.stdout.write() will write the output on the consloe
# we calculate the result and then convert it to a string

sys.stdout.write(str(calculate(args)) + "\n")

