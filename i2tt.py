# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 08:04:21 2022

@author: Golden Mars
"""

from PIL import Image
import pytesseract
from tqdm import tqdm
import pandas as pd

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

res = []
for i in tqdm(range(int(1e3))):
	f = Image.open('cap/reptcha'+str(i).zfill(6)+'.jpg')
	t = pytesseract.image_to_string(f)
	res.append(t)

df = pd.DataFrame(res,columns = ['q'])
dfu = df.drop_duplicates('q')
dfu.to_excel('c.xlsx')
