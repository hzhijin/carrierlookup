# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 08:26:10 2022

@author: Golden Mars
"""

import requests
import time
from tqdm import tqdm



url ='https://www.freecarrierlookup.com/getcarrier_free.php'

# headers = {

# 	'Host':'www.freecarrierlookup.com',
# 	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
# 	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
# 	'Accept-Language':'en-US,en;q=0.5',
# 	'Accept-Encoding':'gzip, deflate, br',
#  	'Referer':'https://www.google.com/',
#  	'Connection':'keep-alive',
#  	'Cookie':'PHPSESSID=pf8gfn05d6qeqcb6itcdgutm9u; __gads=ID=71273e954eb6eb07-227e1e7665d0009f:T=1643344661:RT=1643344661:S=ALNI_MbN2scDV9mTEJyjJPBlXC8P21UAlQ',
# 			 
# 	 
#  	'Upgrade-Insecure-Requests':'1',
#  	'Sec-Fetch-Dest':'document',
#  	'Sec-Fetch-Mode':'navigate',
#  	'Sec-Fetch-Site':'cross-site',
#  	'Sec-Fetch-User':'?1',
#  	'Cache-Control':'max-age=0',
# 	}
# r = requests.get(url,headers=headers)
# print(r.content)


headers = {
 	'Host':'www.freecarrierlookup.com',
 	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
 	'Accept':'application/json, text/javascript, */*; q=0.01',
 	'Accept-Language':'en-US,en;q=0.5',
 	'Accept-Encoding':'gzip, deflate, br',
 	'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
 	'X-Requested-With':'XMLHttpRequest',
 	'Content-Length':'74',
 	'Origin':'https://www.freecarrierlookup.com',
 	'Connection':'keep-alive',
 	'Referer':'https://www.freecarrierlookup.com/',
 	'Cookie':'PHPSESSID=pf8gfn05d6qeqcb6itcdgutm9u; __gads=ID=71273e954eb6eb07-227e1e7665d0009f:T=1643344661:RT=1643344661:S=ALNI_MbN2scDV9mTEJyjJPBlXC8P21UAlQ',
 	'Cookie':'PHPSESSID=7vk0acr99aj3dum811mfb9rlbd;',
 	'Sec-Fetch-Dest':'empty',
 	'Sec-Fetch-Mode':'cors',
 	'Sec-Fetch-Site':'same-origin',
 	}

data = 'test=456Tabo&cc=1&phonenum=4054122710&captcha_entered=on&sessionlogin=1'

r = requests.post(url,headers = headers,data=data)
print(r.content)