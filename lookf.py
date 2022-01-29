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

clist = [{'name':'USA Mobility','web':'@usamobility.net'},
		 {'name':'Qwest Corporation','web':'@qwestmp.com'},
		 {'name':'Comcast','web':'no'},
		 {'name':'Google (Grand Central) BWI - Bandwidth.com - SVR','web':'no'},
		 {'name':'RCLEC, Inc.','web':'no'},
		 {'name':'USAMobility','web':'usamobility'},
		 {'name':'USAMobility','web':'usamobility'},
		 {'name':'USAMobility','web':'usamobility'},
		 {'name':'USAMobility','web':'usamobility'},
		 {'name':'USAMobility','web':'usamobility'},
		 {'name':'USAMobility','web':'usamobility'},
		 {'name':'USAMobility','web':'usamobility'},
		 {'name':'USAMobility','web':'usamobility'},
		 {'name':'USAMobility','web':'usamobility'},
		 {'name':'USAMobility','web':'usamobility'},
		 
		 
		 ]

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


