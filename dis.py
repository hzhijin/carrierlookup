# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 00:51:34 2022

@author: Golden Mars
"""
import requests
import pandas as pd
import zipcodes
from tqdm import tqdm
import re

import phonenumbers
from phonenumbers import carrier

# df = pd.DataFrame(zipcodes.list_all())
# pd.options.display.max_columns = 20

def getDis(url):
	headers = {
		'Host':'api-g.weedmaps.com',
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
		'Accept':'*/*',
		'Accept-Language':'en-US,en;q=0.5',
		'Accept-Encoding':'gzip, deflate, br',
		'Referer':'https://weedmaps.com/',
		'Origin':'https://weedmaps.com',
		'Connection':'keep-alive',
		'Sec-Fetch-Dest':'empty',
		'Sec-Fetch-Mode':'cors',
		'Sec-Fetch-Site':'same-site',
		}
	r = requests.get(url,headers = headers)
	df = pd.DataFrame(r.json()['data']['listings'])
	return df
	
# df = pd.DataFrame()	
# for i in tqdm(range(1,110)):
# 	url = 'https://api-g.weedmaps.com/discovery/v1/listings?page_size=100&page=' + str(i)
# 	dft = getDis(url)
# 	df = pd.concat([df,dft])
# 	df.to_excel('dis.xlsx')
	
# df['phone_number'] = df.phone_number.str.replace('[ \+\)\(-.]','')
# df.to_excel('dis1.xlsx')


df = pd.read_excel('dis.xlsx')
dfc = pd.DataFrame()
# for i in range(len(df)):
for i in tqdm(range(2,10)):
	p = df.iloc[i]['phone_number']
# 	p = '001' + p
	ro_number = phonenumbers.parse(p,'US')
	c = carrier.name_for_number(ro_number, "en")
	dfct = pd.DataFrame([c],columns = 'carrier')
	if len(dfct) == 0:
		print('failed')
	else:
		dfc = pd.concat([dfc,dfct])
		print(dfc)

