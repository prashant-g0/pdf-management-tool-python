"""
Author - Prashant Gupta

PDF management tool: 
This mini project is developed using Python.
It is designed to assist users with various actions on PDF files, 
such as converting them to different formats, extracting images, and performing other useful operations. 
This tool offers practical solutions for PDF management, making it easier for users 
to handle their documents efficiently.
"""

"""
Pre-requisites: install all the libraries before implementing the code. 
Run the below stated code in your terminal to download the python libraries.
1. pip install pdf2docx
2. pip install docx2pdf
3. pip install pdf2image
4. pip install pikepdf
Also download poopler and paste the bin file address inside poppler_path=r"" under choice == 3
"""
# Code:

# All import modules
from pdf2docx import Converter
from docx2pdf import convert
from pdf2image import convert_from_path
import pikepdf
from pikepdf import Pdf, Name, PdfImage
from pikepdf import Pdf
from glob import glob

# Welcome Statement
print("\nHii there, welcome to pdf management tool!\nHow can i help you today?")
# Display all the services
print("\nEnter:\n1. To convert pdf to docx file.\n2. To convert docx to pdf file.\n3. To extract each page as  image from pdf.\n4. To merge multiple pdf.\n5. To split pdf into multiple files.\n6. To encrypt a pdf with password.\n7. To exit\n")
# Perform all the desired services until command is END
while True:
    try:
        choice = int(input("\nEnter your choice: "))
    
        if choice == 1: # pdf to docx convertion
            userPdf = input("Enter pdf name: ") 
            newDOCX = "docx-pdf.docx"  
            obj = Converter(userPdf)
            obj.convert(newDOCX)
            obj.close()
            print("Docx file is created by name docx-pdf.docx.\n")

        elif choice == 2: # docx to pdf convertion
            userPdf = input("Enter docx file name: ")
            convert(userPdf, "Converted_pdf.pdf")
            print("Pdf file is created by name Converted_pdf.pdf.\n")

        elif choice == 3: # extract each page as image from pdf
            userPdf = input("Enter pdf file name: ")
            oldPDF = convert_from_path(userPdf, poppler_path= r"C:\Projects\Release-24.08.0-0\poppler-24.08.0\Library\bin")

            for i in range(len(oldPDF)):
                oldPDF[i].save("page"+str(i)+".jpg", "JPEG")
            print("The pages are extracted from the pdf by page nmumber.")

        elif choice == 4: # merge all pdfs present in your folder
            newPDF = Pdf.new()

            for file in glob("*.pdf"):
                oldPDF = Pdf.open(file)
                newPDF.pages.extend(oldPDF.pages)
            newPDF.save("mergedPDF.pdf")
            print("All pdf's merged successfully and saved.")
            
        elif choice == 5: # split pdfs into multiple pdfs
            userPdf = input("Enter pdf file name: ")
            oldPDF = pikepdf.Pdf.open(userPdf)

            for n, pageContent in enumerate(oldPDF.pages):
                newPDF = pikepdf.Pdf.new()
                newPDF.pages.append(pageContent)
                newPDF.save(f"split{n+1}.pdf")
            print("Pdf's are splitted and saved as split.pdf")

        elif choice == 6: # encrypt pdf with password
            userPdf = input("Enter pdf file name: ")
            passwrd = input("Enter your password: ")
            oldPDF = pikepdf.Pdf.open(userPdf)
            noExtract = pikepdf.Permissions(extract=False)
            oldPDF.save("protected.pdf", encryption=pikepdf.Encryption(user=passwrd, owner="prash",allow=noExtract))
            print("Your pdf is safe and saved as protected.pdf")

        elif choice == 7: # END command
            print("Program exiting...")
            break

        else: 
            print("ValueError: Invalid input! Try again...")

    except ValueError: # avoid crashing of the program if invalid input is given
        print("That's not a valid choice!")

