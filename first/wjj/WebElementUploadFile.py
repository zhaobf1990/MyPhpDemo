#incoding=gbk
from selenium import webdriver
import os
import time
driver=webdriver.Chrome()
file='file:///'+os.path.abspath('upload_file.html')
driver.get(file)

driver.find_element_by_name('file').send_keys('C:/Users/Administrator/PycharmProjects/PythonTest001/wjj/20161114140048.png')
time.sleep(3)
driver.quit()
