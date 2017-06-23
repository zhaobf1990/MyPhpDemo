#incoding=gbk
from selenium import webdriver
import time
browser=webdriver.Chrome()
first_url="http://www.baidu.com"
browser.maximize_window()
browser.get(first_url)
second_url="http://news.baidu.com"
browser.get(second_url)
time.sleep(2)
browser.back()
time.sleep(2)
browser.forward()
            