# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 02:42:08 2022

@author: Golden Mars
"""


import PyPDF2

pdfFileObj = open('omma_laboratory_list.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
pageObj = pdfReader.getPage(1)
t = pageObj.extractText()
print(t)
pdfFileObj.close()
