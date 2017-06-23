#coding=utf-8
from selenium import webdriver
import os
import time

driver=webdriver.Chrome()
file_path="file:///"+os.path.abspath('checkbox.html')
driver.get(file_path)

checkboxs=driver.find_elements_by_css_selector('input[type=checkbox]')
for checkbox in checkboxs:
    checkbox.click()
    time.sleep(0.5)
#打印当前页面上type为checkbox的个数
print(len(driver.find_elements_by_css_selector('input[type=checkbox]'))) 
print('ok') 

checkboxs.pop().click() 
print(len(checkboxs))
print(len(driver.find_elements_by_css_selector('input[type=checkbox]'))) 
time.sleep(0.5)
driver.find_elements_by_css_selector('input[type=checkbox]').pop().click()
time.sleep(0.5)
driver.find_elements_by_css_selector('input[type=checkbox]').pop().click()

# checkboxs.reverse();
# for checkbox in checkboxs:
#     checkbox.click()
#     time.sleep(0.5)
# #把页面上从最后一个checkbox的勾开始倒数去掉 
# i=2
# for checkboxs in checkboxs:
#     driver.find_elements_by_css_selector('input[type=checkbox]').pop(i).click()
#     i=i-1      
#     time.sleep(1)

print('ok')      
time.sleep(2)
driver.quit()
