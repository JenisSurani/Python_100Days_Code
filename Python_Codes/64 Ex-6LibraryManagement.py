class Library:
    
    def __init__(self):
        self.noOfBooks=0
        self.bookList=[]
        self.issuedBooks=[]
    
    def addBook(self,bookName:str):
        if bookName in self.bookList:
            print(f"'{bookName}' book is already in the Library")
        else:
            self.bookList.append(bookName)
            print(f"Book '{bookName}' added sucessfully in the library")
            self.noOfBooks+=1
    
    def issueBook(self,bookName:str):
        
      if bookName in self.bookList:
        self.bookList.remove(bookName)
        self.issuedBooks.append(bookName)
        print(f"The book '{bookName}' is sucessfully issued!")
        self.noOfBooks-=1
        return bookName
      else:
        print(f"'{bookName}' is not in the Library")
        
    def showAvailableBooks(self):
        return self.bookList
    
    def returnBook(self,bookName:str):
        
        if bookName in self.issuedBooks:
            self.issuedBooks.remove(bookName)
            self.bookList.append(bookName)
            print(f"'{bookName}' book is successfully returned")
            self.noOfBooks+=1
        else:
            print(f"'{bookName}' book in not issued from this Library")
            print(f"Please use addBook() to add '{bookName}' in Library")
            
    def noOfbook(self):
        # print(self.noOfBooks)
        # print(len(self.bookList))
        return self.noOfBooks==len(self.bookList) 
        
        
        
    # method noofbook len== -->gadabag


jen=Library()
jen.addBook("Jenish")
jen.returnBook("josd")
jen.addBook("jjo")
print(jen.showAvailableBooks())
print(jen.noOfbook())

# Author: Jenis Surani
# Topic: Ex-6 LibraryManagement
# Date: 16/02/2025