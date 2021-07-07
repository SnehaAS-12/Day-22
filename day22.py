#Read a jpeg image and print the image file
from PIL import Image
d=Image.open("/content/11.jpg")
import matplotlib.pyplot as plt
plt.imshow(a)


#Merge two pdf files using python script
pip install PyPDF2
import PyPDF2 
pdf1File = open('100 Python Interview Questions.pdf', 'rb')
pdf2File = open('Python Cheatsheet.pdf', 'rb')
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
pdfWriter = PyPDF2.PdfFileWriter()
for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
pdfOutputFile = open('Merged_Files.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1File.close()
pdf2File.close()


#Scrape a website and store the data into DB.
pip install bs4
import urllib.request
from bs4 import BeautifulSoup as bs
import re
import pandas as pd
page = urllib.request.urlopen("https://docs.python.org/3/library/random.html")
soup = bs(page)
names = soup.body.findAll('dt')
function_names = re.findall('id="random.\w+', str(names))
function_names = [item[4:] for item in function_names]
description = soup.body.findAll('dd')
function_usage = []
for item in description:
item = item.text
item = item.replace('\n', ' ')
function_usage.append(item)
print('list of function names:',function_names[:5])
print('\nfunction description:', function_usage[0])
print('\nnumber of items in function names:', len(function_names))
print('number of items in function description:', len(function_usage))
data=pd.DataFrame({'f_name':function_names,'f_usage':function_usage})
print(data)


#Write queries to filter the data in db
import pandas as pd
data = pd.read_csv("employees.csv")
data.columns =[column.replace(" ", "_") for column in data.columns] 
data.query('Senior_Management == True', inplace = True) 
print(data)

#another example
import pandas as pd 
data = pd.read_csv("employees.csv") 
data.columns =[column.replace(" ", "_") for column in data.columns] 
data.query('Senior_Management == True 
            and Gender =="Male" and Team =="Marketing" 
            and First_Name =="Johnny"', inplace = True) 
print(data)