# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep


mobileEmulation = {'deviceName': 'Apple iPhone 6'}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)

driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)

driver.get('http://m.baidu.com')

sleep(3)
driver.close()