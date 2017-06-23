#incoding=gbk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from json.decoder import BACKSLASH
from lib2to3.tests.support import driver

driver=webdriver.Chrome()
driver.get('http://www.baidu.com')

driver.find_element_by_id('kw').send_keys('seleniumm')
time.sleep(1)

driver.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)
time.sleep(1)
driver.find_element_by_id('kw').send_keys(Keys.SPACE)
driver.find_element_by_id('kw').send_keys('教程')
time.sleep(1)

driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
time.sleep(1)

driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')
time.sleep(1)
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'v')
time.sleep(1)
driver.find_element_by_id('su').send_keys(Keys.ENTER)
time.sleep(1)
driver.quit()

                            