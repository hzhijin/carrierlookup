# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 02:00:31 2022

@author: Golden Mars
"""
import requests
import pandas as pd
import zipcodes
from tqdm import tqdm
import re

verizon
att
t-mobile
sprint




df = pd.read_excel('dis.xlsx')
dfc = pd.DataFrame()
# for i in range(len(df)):
for i in tqdm(range(2,10)):
	p = df.iloc[i]['phone_number']
	c = lookup(p)
	dfct = pd.DataFrame([c],columns = ['carrier'])
	dfc = pd.concat([dfc,dfct])
	print(dfc)
		
# p = '4054122710'
# c = lookup(p)
# print(c)
	