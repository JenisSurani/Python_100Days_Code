class Person:
    def __init__(self,occ,name):
        self._occupation=occ # # Using a single underscore to indicate it’s "private"
        # Private variable
        # it's just anotation not acutally private
        
        # To make occupation truly private, use double underscores (__).
        # check chatgpt link because it not truly private
        
        self._name=name
    
    # Getters in Python are methods that are used to access the values of an object's properties
    # They are used to return the value of a specific property, and are typically defined using the @property decorator. 
    
    # define getter
    @property
    def occupation(self):
        return self._occupation
    
    @occupation.setter
    def occupation(self,new_occ):
        if isinstance(new_occ, str) and new_occ.strip(): # strip returns {} if your string is empty which is falsy
            # explore falsy & truly
            self._occupation = new_occ
        else:
            print("Invalid name,Please Enter correct one")
        
    
jenish=Person("BusinessMan","Jenish")
print(jenish.occupation) # calls jenish.occupation(self) implicitly to get the value
jenish.occupation="Kingdom" # calls occupation(self,new_occ) implicitly to set the value
print(jenish.occupation)





# Use me please:
# https://chatgpt.com/share/67b07ca1-83e4-800f-9993-4faa7905bbbb



# Author: Jenis Surani
# Topic: Getters-Setters
# Date: 15/02/2025