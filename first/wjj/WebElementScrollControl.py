#coding=gbk
from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.find_element_by_id('kw').send_keys('sele')
driver.find_element_by_id('su').click()
time.sleep(3)
js='var q=document.documentElement.scrollTop=10000'
driver.execute_script(js)
time.sleep(3)
js_='var q=document.documentElement.scrollTop=0'
driver.execute_script(js_)
time.sleep(3)
driver.quit()