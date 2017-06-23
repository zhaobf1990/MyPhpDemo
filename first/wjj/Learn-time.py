#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from _elementtree import Element
from lib2to3.tests.support import driver

browser=webdriver.Chrome()
browser.get('http://www.baidu.com')

#webdriverwait()方法使用
element=WebDriverWait(browser, 10).until(lambda browser:browser.find_element_by_id("kw"))
element.send_keys('selenium')

browser.implicitly_wait(30)
 
browser.find_element_by_id('su').submit()
print('执行了')

#添加固定休眠时间
time.sleep(5)
browser.quit()

