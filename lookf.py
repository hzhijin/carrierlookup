# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 08:50:35 2022

@author: Golden Mars
"""

import freecarrierlookup
from PIL import Image
import pytesseract
from tqdm import tqdm
import pandas as pd
import time

def lookup(p):
	df = pd.read_excel('c.xlsx')
	pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
	
	for j in range(10):
		try:
			l = freecarrierlookup.FreeCarrierLookup()
			image, ocr = l.get_captcha()
			t = pytesseract.image_to_string(image)
			print(t)
		
			a = df[df.q == t].iloc[0]['a']
			try:
				a = int(a)
			except:
				pass
			print(a)
			time.sleep(2)
			
			i = l.lookup('1', p, a)
			df = pd.DataFrame(i,index = [0])
			return df
		except Exception as e:
			print(e)
			print('retrying')
			time.sleep(2)
	return pd.DataFrame()

p = '4235135997'
df = lookup(p)
if len(df) == 0:
	print('failed')
else:
	print(df)


