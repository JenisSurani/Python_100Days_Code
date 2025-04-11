import temp111 as td
# this runs enitre temp11 module first

print(__name__) # runs directly-->main
# runs indirectly-->file name/module name/script name
# print(td.welcome()) 

# This is important to check the module first that any function call is made outside the if __name=="__main__" ,if yes then do not import that module
# because they module may have fun like dlt files as you import this it will run in your comp and dlt all files
# so it's good practice for the check 



#   otherwise use module like this only import impt methods not whole module
#  from temp11 import welcome

# Author: Jenis Surani
# Topic:  if __name__="__main__"
# Date: 12/02/2025