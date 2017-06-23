#coding=UTF-8
from selenium import webdriver
import os
import  time

driver=webdriver.Chrome()
file_path='file:///'+os.path.abspath('checkbox.html')
driver.get(file_path)

#选择页面上所有tag name为 input的元素
inputs=driver.find_elements_by_tag_name('input')
print("执行")
#从中过滤出type为checkbox的元素，单机勾选
for input in inputs:
    if input.get_attribute('type')=='checkbox':
        input.click()
        time.sleep(1)
print('执行')       
        
driver.quit()