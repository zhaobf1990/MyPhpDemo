#coding=utf-8
from selenium import webdriver
import os
import time
from asyncio.tasks import sleep


driver=webdriver.Chrome()
# file_path="file:///"+os.path.abspath('checkbox.html')
file_path="file:///C:/Users/zhaobf/Desktop/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9%20(6)/checkbox.html";
driver.get(file_path)

checkboxs=driver.find_elements_by_css_selector('input[type=checkbox]')
print(checkboxs)
for checkbox in checkboxs:
    checkbox.click()
    time.sleep(0.5)
#打印当前页面上type为checkbox的个数
print(len(driver.find_elements_by_css_selector('input[type=checkbox]'))) 
print('ok') 
#把页面上从最后一个checkbox的勾开始倒数去掉 
i=0
for checkboxs[i] in checkboxs[2]:
    driver.find_elements_by_css_selector('input[type=checkbox]').pop().click()
    i=i+1      
    time.sleep(1)
#     i++

print('ok')      
driver.quit()

for checkboxs[i] in checkboxs[2]:
    driver.find_elements_by_css_selector('input[type=checkbox]').pop().click()
    i=i+1
    time.sleep(1)

    checkboxs = driver.find_elements_by_css_selector('input[type=checkbox]')