#coding=gbk
from selenium import webdriver
import os,time

source=open('D:/data.txt','r')
values=source.readlines()
source.close()
for serch in values:
    browser=webdriver.Chrome()
    browser.get('http://www.baidu.com')
    browser.find_element_by_id('kw').send_keys(serch)
    browser.find_element_by_id('su').click()
    time.sleep(1)
    browser.quit()
