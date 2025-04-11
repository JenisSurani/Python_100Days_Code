import ctypes

# Load the compiled DLL
temp = ctypes.CDLL("./temp.dll")  

# Call the C function
temp.say_hello()
