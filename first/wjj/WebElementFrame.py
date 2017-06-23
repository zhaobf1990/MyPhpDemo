#incoding=gbk
from selenium import webdriver

import  time
import os

driver=webdriver.Chrome()
file_path="file:///"+os.path.abspath("frame.html")
driver.get(file_path)

driver.implicitly_wait(30)
# webdriverwait(driver,30).until(lambda driver:driver.switch_to_frame('f1'))
driver.switch_to_frame('f1')
driver.switch_to_frame('f2')

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id('su').click()
time.sleep(3)
driver.quit()