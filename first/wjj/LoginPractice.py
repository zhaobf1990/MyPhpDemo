#incoding=gbk
from selenium import webdriver
import time

browser=webdriver.Chrome()
browser.get('http://122.225.105.118:8765/Account/Login')
browser.maximize_window()
browser.find_element_by_id('txtLoginKey').clear()
browser.find_element_by_id('txtLoginKey').send_keys('test3')
time.sleep(1)
browser.find_element_by_id('txtPassword').clear()
browser.find_element_by_id('txtPassword').send_keys('15410011003')
time.sleep(1)
browser.find_element_by_id('txtVerifyCode').clear()
browser.find_element_by_id('txtVerifyCode').send_keys('1111')
time.sleep(1)
browser.find_element_by_xpath('/html/body/div/div/div/div/ul/li[4]/input').click()
time.sleep(1)

title=browser.title
print(title)
if title=='首页':
    print('title is right')
else:
    print('title is wrong')

now_url=browser.current_url
print(now_url)
 
if now_url=='http://122.225.105.118:8765/Home/Index':
    print('url is right')
else:
    print('url is wrong')
  