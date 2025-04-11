from pypdf import PdfWriter
import os

# choose your directory

directory="D:\\CodeWithHarry\\Python\\Python_HandWritten_Notes\\New folder"


# don't use \ because it is escape character in python 
# instead of use \ use \\ "or" use /(forwardslash) "or" use raw strings(r"")

# example= "C://Myfile//temp//New folder"
# example= "C:\Myfile\temp\New folder" 
# example= r"C:/Myfile/temp/New folder"


#collecting all the pdfs from directory

pdfInFolder = [pdf for pdf in os.listdir(directory) if pdf.endswith(".pdf")]



# print(pdfInFolder)

# to merge the pdf use PdfWriter class:
#creating an object of PdfWriter class

merger=PdfWriter()

# Append each PDF to the writer
for pdf in pdfInFolder:
    
    # first we need to create the path
    path=os.path.join(directory,pdf)
    
    merger.append(path)
  
# save the merged pdf as name given

savedLocation = os.path.join(directory, "MergedPDF.pdf")  # Save in the same director
if os.path.exists(savedLocation):
    print("Already done")
else:
    merger.write(savedLocation)
    merger.close() # good practice to close the object to prevent any data loss!

    print(f"{pdfInFolder}   →  \"MergedPdf\"")
    print(f"Please Check your {directory}")
    
    
    



# Author : Jenis Surani
# Topic  : Ex-8 MergeThePDF
# Date   : 23/02/2025