# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 02:42:08 2022

@author: Golden Mars
"""


import PyPDF2
import re
import pandas as pd


def parsePage(rr):
	namelist = re.findall(r'COUNTY&&&&&(.*?)&&&&&',rr[0])
	res = []
	i=1
	for r in rr[1:]:
		print(i)
		i+=1
		_lic = 'GAAA' + re.findall(r'&&&&&GAAA(.*?)&&&&&',r)[0]
		_trader = re.findall(r'e:(.*?)&&&&&',r)[0]
		_email = re.findall(_lic+r'&&&&&(.*?)&&&&&',r)[0]
		_phone = re.findall(r'&&&&&(?:\d ?){7,12}&&&&&',r)[0]
		_zip = re.findall(r'&&&&&(?:\d ?){5,5}&&&&&',r)[0]
		_county = re.findall(r'(.*?)&&&&&',r.split(_zip)[-1])[0]
		res.append((_trader,_lic,_email,_phone,_zip,_county,))
		try:
			_name2 = re.findall(r'(.*?)&&&&&',r.split(_zip)[-1])[1]
			namelist.append(_name2)
		except Exception as e:
			pass
	df = pd.DataFrame(res,columns = ['lic','trader','email','phone','zip','county'])
	df['name'] = namelist
	return df


pdfFileObj = open('omma_growers_list.pdf', 'rb')


pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

for i in range(pdfReader.numPages):
	pageObj = pdfReader.getPage(i)
	t = pageObj.extractText().replace('\n \n','&&&&&').replace('\n',' ')
	rr = t.split('Trade N')
	df = parsePage(rr)
	print(df.shape)

pdfFileObj.close()


