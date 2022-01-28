# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 22:42:55 2022

@author: Golden Mars
"""

import requests
import time
from tqdm import tqdm

url = 'https://www.freecarrierlookup.com/captcha/captcha.php'

for i in tqdm(range(int(1e4))):
	r = requests.get(url)
	with open('cap/reptcha'+str(i).zfill(6)+'.jpg', mode='wb') as f:
		f.write(r.content)
	time.sleep(5)
