#coding=gbk
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest,time
from wjj import userinfo
un,pw=userinfo.fun()
print(un)
print(pw)

def login(self):
    driver=self.driver
    driver.find_element_by_id("Name").clear()
    driver.find_element_by_id("Name").send_keys(un)
    driver.find_element_by_id("Password").clear()
    driver.find_element_by_id("Password").send_keys(pw)
    driver.find_element_by_id("/html/body/div[2]/div/div/form/table/tbody/tr[3]/td/input").click()
    time.sleep(3)



