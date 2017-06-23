#incoding=gbk
'''
Created on 2016年10月20日

@author: Administrator
'''

from selenium import webdriver
from asyncio.tasks import wait
import time

browser=webdriver.Chrome()
browser.get("http://instest.chediandian.com")
print('设置浏览器宽480、高800显示')
browser.set_window_size(400,800)
time.sleep(2)
browser.maximize_window()
time.sleep(5)
browser.quit()