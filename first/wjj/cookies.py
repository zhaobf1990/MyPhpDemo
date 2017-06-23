#coding=gbk
from selenium import webdriver

driver=webdriver.Chrome()
driver.get('http://122.225.105.112:8765/Account/Login')
driver.add_cookie()
cookie=driver.get_cookies()
print(cookie)
driver.quit()