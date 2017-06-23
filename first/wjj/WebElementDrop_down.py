#incoding=gbk
from selenium import webdriver
import os
import time

driver=webdriver.Chrome()
file_path='file:///'+os.path.abspath('drop_down.html')
driver.get(file_path)
time.sleep(2)
m=driver.find_element_by_id('ShippingMethod')
m.find_element_by_xpath('//*[@id="ShippingMethod"]/option[3]').click()
time.sleep(2)
driver.quit()
