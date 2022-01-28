# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 08:43:42 2022

@author: Golden Mars
"""

from selenium import webdriver
# driver = webdriver.Firefox(executable_path='C:\Python\geckodriver.exe')
d = webdriver.Firefox()

url ='https://www.freecarrierlookup.com/getcarrier_free.php'
d.get(url)